import React, { useState } from 'react';
import { Wand2, Play, RefreshCw, Zap, ShieldAlert, Sparkles, Layers } from 'lucide-react';

interface PromptStudioProps {
  onGenerate: (data: { prompt: string; genre: string; duration: number; target_network: string; theme: string }) => void;
  isLoading: boolean;
}

export const PromptStudio: React.FC<PromptStudioProps> = ({ onGenerate, isLoading }) => {
  const [prompt, setPrompt] = useState("Create a 30-second Royal Match style puzzle save-the-king playable ad for Meta Ads");
  const [genre, setGenre] = useState("Match-3");
  const [duration, setDuration] = useState(30);
  const [network, setNetwork] = useState("Meta");
  const [theme, setTheme] = useState("Royal Rescue");

  const presets = [
    {
      name: "👑 Royal Match Rescue",
      prompt: "Create a 30-second Royal Match style puzzle save-the-king playable ad",
      genre: "Match-3",
      duration: 30,
      network: "Meta",
      theme: "Royal Rescue"
    },
    {
      name: "🗝️ Pull-The-Pin Hero",
      prompt: "Create a 15-second Pull the pin hero puzzle save treasure dodging lava playable ad",
      genre: "Pull-the-Pin",
      duration: 15,
      network: "TikTok",
      theme: "Dungeon Hero"
    },
    {
      name: "🧱 Tile Blast Defense",
      prompt: "Create a 30-second color tile tap blast rebuild castle wall playable ad",
      genre: "Tile Blast",
      duration: 30,
      network: "Google Ads",
      theme: "Kingdom Defense"
    }
  ];

  const handleApplyPreset = (preset: typeof presets[0]) => {
    setPrompt(preset.prompt);
    setGenre(preset.genre);
    setDuration(preset.duration);
    setNetwork(preset.network);
    setTheme(preset.theme);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onGenerate({ prompt, genre, duration, target_network: network, theme });
  };

  return (
    <div className="glass-panel rounded-2xl p-6 border border-slate-800 shadow-2xl space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="p-2 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-400">
            <Wand2 className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-white">Playable Prompt Studio</h2>
            <p className="text-xs text-slate-400">Specify game concept, mechanics & ad network specifications</p>
          </div>
        </div>
        <span className="text-xs font-semibold px-2.5 py-1 rounded-md bg-purple-500/10 text-purple-400 border border-purple-500/30">
          5-Agent Pipeline Active
        </span>
      </div>

      {/* Preset Chips */}
      <div>
        <label className="text-xs font-semibold text-slate-400 block mb-2">QUICK PRESET CONCEPTS</label>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {presets.map((p, idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => handleApplyPreset(p)}
              className="glass-card hover:bg-slate-800/80 p-3 rounded-xl text-left border border-slate-700/50 hover:border-cyan-500/50 transition group"
            >
              <div className="font-semibold text-sm text-slate-200 group-hover:text-cyan-300 transition mb-1">
                {p.name}
              </div>
              <div className="text-xs text-slate-400 truncate">{p.prompt}</div>
            </button>
          ))}
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="text-xs font-semibold text-slate-400 block mb-1">NATURAL LANGUAGE PLAYABLE PROMPT</label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            rows={3}
            className="w-full bg-slate-900/90 border border-slate-700/80 rounded-xl p-3.5 text-sm text-white focus:outline-none focus:border-cyan-500/80 transition resize-none"
            placeholder="Describe the playable game ad mechanics, goal, duration and visual style..."
          />
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">GENRE MECHANIC</label>
            <select
              value={genre}
              onChange={(e) => setGenre(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"
            >
              <option value="Match-3">Match-3 Rescue</option>
              <option value="Pull-the-Pin">Pull-the-Pin Hero</option>
              <option value="Tile Blast">Tile Blast Defense</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">AD DURATION</label>
            <select
              value={duration}
              onChange={(e) => setDuration(Number(e.target.value))}
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"
            >
              <option value={15}>15 Seconds (Fast Hook)</option>
              <option value={30}>30 Seconds (Standard)</option>
              <option value={45}>45 Seconds (Deep Engagement)</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">TARGET NETWORK</label>
            <select
              value={network}
              onChange={(e) => setNetwork(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"
            >
              <option value="Meta">Meta (Facebook/IG)</option>
              <option value="TikTok">TikTok Pangle</option>
              <option value="Google Ads">Google App Campaigns</option>
              <option value="Unity">Unity Ads (MRAID 3.0)</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">VISUAL THEME</label>
            <input
              type="text"
              value={theme}
              onChange={(e) => setTheme(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"
            />
          </div>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 via-blue-600 to-purple-600 hover:from-cyan-400 hover:via-blue-500 hover:to-purple-500 text-white font-bold text-base shadow-xl shadow-cyan-500/20 hover:shadow-cyan-500/40 transition duration-200 flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          {isLoading ? (
            <>
              <RefreshCw className="w-5 h-5 animate-spin" />
              <span>Orchestrating 5 AI Agents...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5" />
              <span>GENERATE PLAYABLE GAME AD</span>
            </>
          )}
        </button>
      </form>
    </div>
  );
};
