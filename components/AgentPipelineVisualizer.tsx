import React from 'react';
import { Gamepad2, Code, Palette, TestTube2, TrendingUp, CheckCircle2, Loader2, Circle } from 'lucide-react';

interface AgentPipelineVisualizerProps {
  currentStage: number; // 0 to 5
  agentOutputs?: {
    concept?: any;
    codeSnippet?: string;
    assetCount?: number;
    testResult?: any;
    optimizationReport?: any;
  };
}

export const AgentPipelineVisualizer: React.FC<AgentPipelineVisualizerProps> = ({ currentStage, agentOutputs }) => {
  const agents = [
    {
      id: 1,
      name: "Game Design Agent 🎮",
      role: "Game Concept & Mechanics",
      icon: Gamepad2,
      color: "from-blue-500 to-cyan-500",
      detail: agentOutputs?.concept ? `${agentOutputs.concept.title} (${agentOutputs.concept.mechanic})` : "Formulating core puzzle mechanics..."
    },
    {
      id: 2,
      name: "Code Generation Agent 👨‍💻",
      role: "Phaser 3.80 Scene Logic",
      icon: Code,
      color: "from-cyan-500 to-teal-500",
      detail: agentOutputs?.codeSnippet ? "Generated PlayableScene.js (Phaser 3.80)" : "Synthesizing touch handlers and score loops..."
    },
    {
      id: 3,
      name: "Asset Generation Agent 🎨",
      role: "SVG & Sprite Pipeline",
      icon: Palette,
      color: "from-purple-500 to-pink-500",
      detail: agentOutputs?.assetCount ? `Synthesized ${agentOutputs.assetCount} vector assets & hand overlay` : "Synthesizing UI sprites and hand pointer..."
    },
    {
      id: 4,
      name: "Gameplay Testing Agent 🧪",
      role: "Virtual Bot QA & Latency",
      icon: TestTube2,
      color: "from-amber-500 to-yellow-500",
      detail: agentOutputs?.testResult ? `TTFA: ${agentOutputs.testResult.time_to_first_action_sec}s | ${agentOutputs.testResult.engagement_rating}` : "Simulating bot taps and verifying playability..."
    },
    {
      id: 5,
      name: "Optimization Agent 📈",
      role: "Conversion & Hook Booster",
      icon: TrendingUp,
      color: "from-emerald-500 to-green-500",
      detail: agentOutputs?.optimizationReport ? `+${agentOutputs.optimizationReport.ctr_boost_estimate_percent}% CTR Boost Applied` : "Injecting high-CTR hooks & sticky CTA..."
    }
  ];

  return (
    <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-base font-bold text-white flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-ping"></span>
          <span>Multi-Agent Orchestration Pipeline</span>
        </h3>
        <span className="text-xs text-slate-400 font-mono">5 ACTIVE AGENTS</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-5 gap-3">
        {agents.map((ag) => {
          const Icon = ag.icon;
          const isDone = currentStage > ag.id;
          const isActive = currentStage === ag.id;

          return (
            <div
              key={ag.id}
              className={`rounded-xl p-4 border transition-all duration-300 ${
                isActive
                  ? 'bg-slate-800/90 border-cyan-500/80 shadow-lg shadow-cyan-500/10 scale-102'
                  : isDone
                  ? 'bg-slate-900/60 border-slate-700/60 opacity-90'
                  : 'bg-slate-950/40 border-slate-800/40 opacity-40'
              }`}
            >
              <div className="flex items-center justify-between mb-3">
                <div className={`p-2 rounded-lg bg-gradient-to-r ${ag.color} text-white`}>
                  <Icon className="w-4 h-4" />
                </div>
                {isDone ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                ) : isActive ? (
                  <Loader2 className="w-4 h-4 text-cyan-400 animate-spin" />
                ) : (
                  <Circle className="w-4 h-4 text-slate-600" />
                )}
              </div>

              <div className="font-bold text-xs text-white mb-0.5">{ag.name}</div>
              <div className="text-[11px] text-slate-400 mb-2">{ag.role}</div>

              <div className="text-[10px] text-slate-300 font-mono bg-slate-900/80 p-2 rounded border border-slate-800/60 truncate">
                {ag.detail}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
