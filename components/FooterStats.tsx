import React from 'react';
import { Cpu, Zap, ShieldCheck } from 'lucide-react';

export const FooterStats: React.FC = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
      <div className="glass-card p-4 rounded-xl border border-slate-800 flex items-center space-x-3">
        <Cpu className="w-6 h-6 text-cyan-400" />
        <div>
          <div className="text-xs text-slate-400">Multi-Agent Engine</div>
          <div className="text-sm font-bold text-white">5 Parallel Agents Active</div>
        </div>
      </div>

      <div className="glass-card p-4 rounded-xl border border-slate-800 flex items-center space-x-3">
        <Zap className="w-6 h-6 text-amber-400" />
        <div>
          <div className="text-xs text-slate-400">Generation Velocity</div>
          <div className="text-sm font-bold text-white">&lt; 3.0s Total Runtime</div>
        </div>
      </div>

      <div className="glass-card p-4 rounded-xl border border-slate-800 flex items-center space-x-3">
        <ShieldCheck className="w-6 h-6 text-emerald-400" />
        <div>
          <div className="text-xs text-slate-400">Ad Policy Compliance</div>
          <div className="text-sm font-bold text-white">Meta & TikTok Verified</div>
        </div>
      </div>
    </div>
  );
};
