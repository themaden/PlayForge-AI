import React from 'react';
import { Palette, Eye, Download, Image } from 'lucide-react';

interface AssetSpec {
  asset_id: str;
  name: str;
  asset_type: str;
  svg_data: str;
}

interface AssetStudioProps {
  assets: AssetSpec[];
}

export const AssetStudio: React.FC<AssetStudioProps> = ({ assets }) => {
  return (
    <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-base font-bold text-white flex items-center space-x-2">
          <Palette className="w-5 h-5 text-purple-400" />
          <span>Synthesized Playable Asset Gallery</span>
        </h3>
        <span className="text-xs text-purple-400 font-mono bg-purple-500/10 px-2.5 py-1 rounded-md border border-purple-500/30">
          Agent 3 Asset Pipeline
        </span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
        {assets.map((ast) => (
          <div key={ast.asset_id} className="glass-card p-3 rounded-xl border border-slate-800/80 flex flex-col items-center group">
            <div className="w-full h-28 bg-slate-950/80 rounded-lg flex items-center justify-center p-2 mb-2 border border-slate-900 overflow-hidden">
              <div dangerouslySetInnerHTML={{ __html: ast.svg_data }} />
            </div>
            <div className="text-xs font-bold text-slate-200 text-center truncate w-full mb-0.5">{ast.name}</div>
            <div className="text-[10px] text-slate-400 capitalize">{ast.asset_type}</div>
          </div>
        ))}
      </div>
    </div>
  );
};
