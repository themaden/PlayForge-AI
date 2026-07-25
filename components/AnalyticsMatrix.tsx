import React from 'react';
import { BarChart3, TrendingUp, Sparkles, CheckCircle, Flame } from 'lucide-react';

export const AnalyticsMatrix: React.FC = () => {
  const variants = [
    {
      name: "Variant A: Fail Hook (Water Rise)",
      hook: "Immediate fail prompt at 3s if no tap",
      predictedCtr: "4.82%",
      predictedCvr: "18.4%",
      retentionScore: "94/100",
      status: "Recommended Winner 🏆"
    },
    {
      name: "Variant B: Instant Victory Hook",
      hook: "1 tap win trigger with instant gem match",
      predictedCtr: "3.91%",
      predictedCvr: "14.2%",
      retentionScore: "82/100",
      status: "Control"
    },
    {
      name: "Variant C: Pull Pin Speed Test",
      hook: "Dynamic hand tutorial pointing to top pin",
      predictedCtr: "4.15%",
      predictedCvr: "16.8%",
      retentionScore: "89/100",
      status: "Challenger"
    }
  ];

  return (
    <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-white flex items-center space-x-2">
            <BarChart3 className="w-5 h-5 text-emerald-400" />
            <span>A/B Creative Variant & CTR Prediction Matrix</span>
          </h3>
          <p className="text-xs text-slate-400">AI-computed conversion velocity models comparing playable hook variants</p>
        </div>

        <span className="text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-md border border-emerald-500/30">
          Agent 5 Optimization Matrix
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {variants.map((v, idx) => (
          <div key={idx} className="glass-card p-4 rounded-xl border border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-white">{v.name}</span>
              <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${idx === 0 ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-slate-800 text-slate-400'}`}>
                {v.status}
              </span>
            </div>

            <p className="text-xs text-slate-300 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800/60">
              💡 {v.hook}
            </p>

            <div className="grid grid-cols-3 gap-2 text-center pt-2">
              <div className="bg-slate-950/60 p-2 rounded-lg border border-slate-900">
                <div className="text-[10px] text-slate-400">Est. CTR</div>
                <div className="text-sm font-bold text-emerald-400">{v.predictedCtr}</div>
              </div>

              <div className="bg-slate-950/60 p-2 rounded-lg border border-slate-900">
                <div className="text-[10px] text-slate-400">Est. CVR</div>
                <div className="text-sm font-bold text-cyan-400">{v.predictedCvr}</div>
              </div>

              <div className="bg-slate-950/60 p-2 rounded-lg border border-slate-900">
                <div className="text-[10px] text-slate-400">Retention</div>
                <div className="text-sm font-bold text-purple-400">{v.retentionScore}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
