import React from 'react';
import { Sparkles, Gamepad2, Layers, Cpu, Download, BarChart2 } from 'lucide-react';

export const Navbar: React.FC = () => {
  return (
    <header className="sticky top-0 z-50 glass-panel border-b border-slate-800/80 px-6 py-4 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-purple-600 flex items-center justify-center shadow-lg shadow-cyan-500/20">
          <Gamepad2 className="w-6 h-6 text-white" />
        </div>
        <div>
          <h1 className="text-xl font-extrabold bg-gradient-to-r from-cyan-400 via-sky-300 to-purple-400 bg-clip-text text-transparent tracking-tight">
            PlayForge AI
          </h1>
          <p className="text-xs text-slate-400 font-medium">AI Playable Game Ad Generation Engine</p>
        </div>
      </div>

      <nav className="hidden md:flex items-center space-x-6">
        <a href="#studio" className="flex items-center space-x-2 text-sm text-cyan-400 font-semibold transition hover:text-cyan-300">
          <Sparkles className="w-4 h-4" />
          <span>Generator Studio</span>
        </a>
        <a href="#agents" className="flex items-center space-x-2 text-sm text-slate-300 hover:text-white transition">
          <Cpu className="w-4 h-4 text-purple-400" />
          <span>Multi-Agent Matrix</span>
        </a>
        <a href="#preview" className="flex items-center space-x-2 text-sm text-slate-300 hover:text-white transition">
          <Gamepad2 className="w-4 h-4 text-emerald-400" />
          <span>Live Ad Sandbox</span>
        </a>
        <a href="#export" className="flex items-center space-x-2 text-sm text-slate-300 hover:text-white transition">
          <Download className="w-4 h-4 text-amber-400" />
          <span>Single-File Exporter</span>
        </a>
      </nav>

      <div className="flex items-center space-x-3">
        <span className="hidden sm:inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
          <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse mr-2"></span>
          Phaser 3.80 Engine Ready
        </span>
      </div>
    </header>
  );
};
