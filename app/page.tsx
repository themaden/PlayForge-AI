'use client';
import { useState } from 'react';
type Project = {
  project_id: string; export_html: string; generation_duration_ms: number;
  game_concept: { title: string }; test_result: { checks: Record<string, boolean> };
  review_status?: string;
  generation_mode?: string; parent_project_id?: string;
  provenance?: { text_model?: string; image_model?: string };
  runtime_evaluation?: { passed: boolean; checks: Record<string, boolean>; errors: string[] };
  reviews?: { decision: string; feedback: string; created_at: string }[];
};
const api = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
export default function Home() {
  const [prompt, setPrompt] = useState('A royal rescue puzzle');
  const [duration, setDuration] = useState(15);
  const [project, setProject] = useState<Project | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [feedback, setFeedback] = useState('');
  const [restoreId, setRestoreId] = useState('');
  const [mode, setMode] = useState('local_template');
  const [images, setImages] = useState(false);
  const [browserChecks, setBrowserChecks] = useState(true);
  const [previous, setPrevious] = useState<Project | null>(null);
  async function request(path: string, body?: unknown) {
    const response = await fetch(api + path, body === undefined ? undefined : {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(typeof data.detail === 'string' ? data.detail : 'Check the input and try again.');
    return data;
  }
  async function act(action: () => Promise<Project>) {
    setBusy(true); setError('');
    try { setProject(await action()); }
    catch (e) { setError(e instanceof Error ? e.message : 'Request failed.'); }
    finally { setBusy(false); }
  }
  async function generate() {
    setProject(null); setFeedback('');
    setPrevious(null);
    await act(() => request('/api/generate', { prompt, duration, generation_mode: mode, generate_images: mode === 'local_ai' && images, evaluate_browser: browserChecks }));
  }
  function download() {
    if (!project || project.review_status !== 'approved') return;
    const url = URL.createObjectURL(new Blob([project.export_html], { type: 'text/html' }));
    const a = document.createElement('a'); a.href = url; a.download = project.project_id + '.html'; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  return <main className="max-w-5xl mx-auto p-6 text-slate-100 space-y-6">
    <header><h1 className="text-3xl font-bold">PlayForge Studio</h1>
      <p className="text-slate-400 mt-2">Create a tap puzzle, preview it and record your review.</p>
      <p className="text-sm text-slate-400">Choose a fast template or local AI with a generated background. Tap three different tiles; this is not a full match-3 game.</p>
    </header>
    <section className="space-y-3">
      <label className="block">Creative brief<textarea className="block w-full p-3 rounded bg-slate-800 mt-2" value={prompt} onChange={e => setPrompt(e.target.value)} maxLength={2000} /></label>
      <label className="block">Duration in seconds <input className="bg-slate-800 p-2 rounded" type="number" min={5} max={60} value={duration} onChange={e => setDuration(Number(e.target.value))} /></label>
      <label className="block">Generation mode <select aria-label="Generation mode" className="bg-slate-800 p-2 rounded" value={mode} onChange={e => setMode(e.target.value)}><option value="local_template">Template</option><option value="local_ai">Local AI</option></select></label>
      <label className="block"><input type="checkbox" disabled={mode !== 'local_ai'} checked={images} onChange={e => setImages(e.target.checked)} /> Generate a diffusion background</label>
      <label className="block"><input type="checkbox" checked={browserChecks} onChange={e => setBrowserChecks(e.target.checked)} /> Run browser checks, including waiting for the timer</label>
      {mode === 'local_ai' && <p className="text-sm text-slate-400">First use downloads several GB of model files. Local CPU inference can take several minutes. No paid API is called.</p>}
      <button className="bg-blue-600 px-5 py-2 rounded disabled:opacity-50" disabled={busy} onClick={generate}>{busy ? 'Working...' : 'Generate preview'}</button>
      <p className="text-sm text-slate-400">Only the tap puzzle template is implemented. Pull-the-pin and tile blast are not available.</p>
    </section>
    <section className="flex gap-3 flex-wrap">
      <input aria-label="Saved project ID" className="bg-slate-800 rounded p-2" placeholder="Saved project ID" value={restoreId} onChange={e => setRestoreId(e.target.value)} />
      <button disabled={busy || !restoreId} onClick={() => act(() => request('/api/projects/' + encodeURIComponent(restoreId)))}>Open saved project</button>
    </section>
    {error && <p role="alert" className="text-red-300">{error}</p>}
    {project && <>
      <section><h2 className="font-bold text-xl">{project.game_concept.title}</h2>
        <p className="text-sm text-slate-400">Saved ID: {project.project_id} | Generation: {project.generation_duration_ms} ms | Paid API cost: $0</p>
        <p className="text-sm text-slate-400">Mode: {project.generation_mode} {project.provenance?.text_model} {project.provenance?.image_model}</p>
        {project.parent_project_id && <p>Revision of: {project.parent_project_id}</p>}
        <iframe title="Playable preview" className="w-[360px] max-w-full h-[640px] border border-slate-600 mx-auto mt-4" sandbox="allow-scripts" srcDoc={project.export_html} />
      </section>
      <section><h2 className="font-bold text-xl">Code checks</h2>
        <ul>{Object.entries(project.test_result.checks).map(([name, passed]) => <li key={name}>{passed ? 'PASS' : 'FAIL'}: {name.replaceAll('_', ' ')}</li>)}</ul>
        <p className="text-sm text-slate-400">Static checks only. FPS, engagement and conversion lift have not been measured.</p>
        {project.runtime_evaluation && <><h3 className="font-bold mt-3">Browser evaluation: {project.runtime_evaluation.passed ? 'PASS' : 'FAIL'}</h3><ul>{Object.entries(project.runtime_evaluation.checks).map(([name, passed]) => <li key={name}>{passed ? 'PASS' : 'FAIL'}: {name.replaceAll('_', ' ')}</li>)}</ul>{project.runtime_evaluation.errors.map((error, i) => <p key={i} className="text-red-300">{error}</p>)}</>}
      </section>
      <section className="space-y-3"><h2 className="font-bold text-xl">Human review</h2>
        <p>Test three different taps, the timeout and the end screen. The CTA shows a demo message.</p>
        <p>Status: {project.review_status || 'pending'}</p>
        <textarea aria-label="Review feedback" className="w-full bg-slate-800 p-3 rounded" placeholder="Describe any changes needed" value={feedback} onChange={e => setFeedback(e.target.value)} maxLength={2000} />
        <div className="flex gap-3">
          <button className="bg-green-700 px-4 py-2 rounded disabled:opacity-50" disabled={busy} onClick={() => act(() => request(`/api/projects/${project.project_id}/review`, { decision: 'approved', feedback }))}>Approve</button>
          <button className="bg-amber-700 px-4 py-2 rounded disabled:opacity-50" disabled={busy || !feedback.trim()} onClick={() => act(() => request(`/api/projects/${project.project_id}/review`, { decision: 'changes_requested', feedback }))}>Request changes</button>
          <button className="bg-blue-700 px-4 py-2 rounded disabled:opacity-50" disabled={project.review_status !== 'approved'} onClick={download}>Download approved HTML</button>
          <button className="bg-purple-700 px-4 py-2 rounded disabled:opacity-50" disabled={busy || project.review_status !== 'changes_requested' || mode !== 'local_ai'} onClick={() => { setPrevious(project); act(() => request(`/api/projects/${project.project_id}/revise`, {generation_mode: mode, generate_images: images, evaluate_browser: browserChecks})); }}>Generate revision</button>
        </div>
        <p className="text-sm text-slate-400">Request changes first, then choose Local AI and generate a revision from saved feedback.</p>
        {previous && <p>Previous title: {previous.game_concept.title} → Current title: {project.game_concept.title}</p>}
        <ul>{project.reviews?.map((r, i) => <li key={i}>{r.decision}: {r.feedback || 'Approved without comment'} ({new Date(r.created_at).toLocaleString()})</li>)}</ul>
      </section>
    </>}
  </main>;
}
