import React from 'react';
import { Target, Zap, Clock, Activity } from 'lucide-react';

interface HeatmapOverlayProps {
  ttfa: number;
  difficultyScore: number;
  engagementRating: string;
  fps: number;
}

export const HeatmapOverlay: React.FC<HeatmapOverlayProps> = ({
  ttfa,
  difficultyScore,
  engagementRating,
  fps
}) => {
  return (
    <div className="glass-panel rounded-2xl p-5 border border-slate-800 space-y-4">
      <h4 className="text-sm font-bold text-white flex items-center space-x-2">
        <Activity className="w-4 h-4 text-cyan-400" />
        <span>Gameplay QA Telemetry & Heatmap Metrics</span>
      </h4>

      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div className="glass-card p-3 rounded-xl border border-slate-800">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>First Action Hook</span>
            <Clock className="w-3.5 h-3.5 text-cyan-400" />
          </div>
          <div className="text-lg font-bold text-cyan-300">{ttfa}s</div>
          <div className="text-[10px] text-emerald-400 font-semibold mt-0.5">Target: &lt;2.0s Hook</div>
        </div>

        <div className="glass-card p-3 rounded-xl border border-slate-800">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Difficulty Index</span>
            <Target className="w-3.5 h-3.5 text-purple-400" />
          </div>
          <div className="text-lg font-bold text-purple-300">{(difficultyScore * 100).toFixed(0)}%</div>
          <div className="text-[10px] text-slate-400 mt-0.5">Balanced Progression</div>
        </div>

        <div className="glass-card p-3 rounded-xl border border-slate-800">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Engagement Tier</span>
            <Zap className="w-3.5 h-3.5 text-amber-400" />
          </div>
          <div className="text-sm font-bold text-amber-300 truncate">{engagementRating}</div>
          <div className="text-[10px] text-amber-400 mt-0.5">Dream Games Standard</div>
        </div>

        <div className="glass-card p-3 rounded-xl border border-slate-800">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Target FPS</span>
            <Activity className="w-3.5 h-3.5 text-emerald-400" />
          </div>
          <div className="text-lg font-bold text-emerald-300">{fps} FPS</div>
          <div className="text-[10px] text-emerald-400 mt-0.5">Smooth WebGL Performance</div>
        </div>
      </div>
    </div>
  );
};
