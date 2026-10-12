"""Optional local inference. Model failures never become simulated AI results."""
import base64
import gc
import io
import json
import os
import re
from pathlib import Path
from threading import Lock
from pydantic import BaseModel, Field

MODEL_LOCK = Lock()
ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault('HF_HOME', str(ROOT / '.models'))
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')
TEXT_MODEL = 'Qwen/Qwen2.5-0.5B-Instruct'
IMAGE_MODEL = 'stabilityai/sd-turbo'


class CreativeBrief(BaseModel):
    title: str = Field(min_length=1, max_length=40)
    instruction: str = Field(min_length=1, max_length=100)
    cta: str = Field(min_length=1, max_length=40)
    image_prompt: str = Field(min_length=10, max_length=500)


def generate_brief(prompt: str) -> CreativeBrief:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    torch.set_num_threads(min(8, os.cpu_count() or 4))
    tokenizer = AutoTokenizer.from_pretrained(TEXT_MODEL)
    model = AutoModelForCausalLM.from_pretrained(TEXT_MODEL, torch_dtype=torch.float32)
    system = ('You design a simple game where the player taps three different tiles. '
              'Return only JSON with four string keys: title (under 40 characters), '
              'instruction (under 100 characters), cta (under 40 characters), '
              'image_prompt (under 500 characters describing a background with no text). '
              'Do not invent other mechanics. Example: '
              '{"title":"Forest Rescue","instruction":"Tap three different gems before time runs out",'
              '"cta":"PLAY NOW","image_prompt":"An enchanted forest clearing, stylized mobile game background, no text"}')
    last_error = None
    try:
        for attempt in range(2):
            messages = [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}]
            if attempt:
                messages.append({'role': 'user', 'content': 'Return valid JSON only. Use the four exact keys from the example and respect length limits.'})
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs = tokenizer(text, return_tensors='pt')
            with torch.inference_mode():
                output = model.generate(**inputs, max_new_tokens=250, do_sample=False)
            raw = tokenizer.decode(output[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True)
            try:
                match = re.search(r'\{.*\}', raw, flags=re.S)
                if match is None:
                    raise ValueError('Model did not return a JSON object')
                payload = json.loads(match.group())
                # Mechanics belong to the tested template; a small model must not
                # describe trees, pins or other interactions that are not implemented.
                payload['instruction'] = 'Tap three different gems before the timer ends'
                return CreativeBrief.model_validate(payload)
            except (ValueError, TypeError) as error:
                last_error = error
        raise ValueError(f'Local model output failed validation: {last_error}')
    finally:
        del model
        gc.collect()


def generate_background(prompt: str, seed: int = 42) -> str:
    import torch
    from diffusers import AutoPipelineForText2Image
    torch.set_num_threads(min(8, os.cpu_count() or 4))
    pipe = AutoPipelineForText2Image.from_pretrained(
        IMAGE_MODEL, variant='fp16', torch_dtype=torch.float32)
    pipe.enable_attention_slicing()
    try:
        image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0,
                     width=512, height=512, generator=torch.Generator('cpu').manual_seed(seed)).images[0]
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        return 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode('ascii')
    finally:
        del pipe
        gc.collect()
