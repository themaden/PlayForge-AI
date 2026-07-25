import React, { useState } from 'react';
import { Download, Check, Copy, Code2, Globe, ShieldCheck } from 'lucide-react';

interface ExporterHubProps {
  exportHtml: string;
  projectName: string;
}

export const ExporterHub: React.FC<ExporterHubProps> = ({ exportHtml, projectName }) => {
  const [copied, setCopied] = useState(false);

  const handleDownload = (network: string) => {
    const blob = new Blob([exportHtml], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `PlayForge_${projectName.replace(/\s+/g, '_')}_${network}.html`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handleCopyCode = () => {
    navigator.clipboard.writeText(exportHtml);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const adNetworks = [
    { name: "Meta Ads (FB/IG)", badge: "Single-File HTML5", size: "< 2.1 MB", spec: "FbPlayable SDK Ready" },
    { name: "TikTok Pangle", badge: "Interactive ZIP / HTML", size: "< 1.8 MB", spec: "playableSDK Ready" },
    { name: "Google App Campaigns", badge: "Google Playable Standard", size: "< 2.5 MB", spec: "Inline Asset Bundle" },
    { name: "Unity Ads (MRAID)", badge: "MRAID 3.0 Standard", size: "< 1.9 MB", spec: "mraid.open() Hook" }
  ];

  return (
    <div id="export" className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-white flex items-center space-x-2">
            <Download className="w-5 h-5 text-amber-400" />
            <span>Single-File Ad Network Export Hub</span>
          </h3>
          <p className="text-xs text-slate-400">Download single-file HTML5 playable bundle compliant with ad platform policies</p>
        </div>

        <button
          onClick={handleCopyCode}
          className="flex items-center space-x-2 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 transition"
        >
          {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4 text-slate-400" />}
          <span>{copied ? "Copied Source!" : "Copy HTML5 Source"}</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {adNetworks.map((net, idx) => (
          <div key={idx} className="glass-card p-4 rounded-xl border border-slate-800 space-y-3 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-sm font-bold text-white">{net.name}</span>
                <ShieldCheck className="w-4 h-4 text-emerald-400" />
              </div>
              <div className="text-xs text-amber-400 font-mono mb-2">{net.badge}</div>
              <div className="text-[11px] text-slate-400 space-y-1">
                <div>📦 Max Bundle: {net.size}</div>
                <div>⚡ {net.spec}</div>
              </div>
            </div>

            <button
              onClick={() => handleDownload(net.name)}
              className="w-full py-2.5 rounded-lg bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-400 hover:to-orange-500 text-white text-xs font-bold transition flex items-center justify-center space-x-2 shadow-lg shadow-amber-500/10"
            >
              <Download className="w-3.5 h-3.5" />
              <span>EXPORT FOR {net.name.toUpperCase()}</span>
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
