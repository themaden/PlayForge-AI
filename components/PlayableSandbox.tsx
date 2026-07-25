import React, { useEffect, useRef } from 'react';
import { Play, RotateCcw, Monitor, Smartphone, Tablet } from 'lucide-react';

interface PlayableSandboxProps {
  htmlContent: string;
  deviceFrame: 'mobile' | 'tablet' | 'desktop';
  onDeviceChange: (device: 'mobile' | 'tablet' | 'desktop') => void;
}

export const PlayableSandbox: React.FC<PlayableSandboxProps> = ({
  htmlContent,
  deviceFrame,
  onDeviceChange
}) => {
  const iframeRef = useRef<HTMLIFrameElement>(null);

  useEffect(() => {
    if (iframeRef.current && htmlContent) {
      const doc = iframeRef.current.contentDocument;
      if (doc) {
        doc.open();
        doc.write(htmlContent);
        doc.close();
      }
    }
  }, [htmlContent]);

  const handleRestart = () => {
    if (iframeRef.current && htmlContent) {
      const doc = iframeRef.current.contentDocument;
      if (doc) {
        doc.open();
        doc.write(htmlContent);
        doc.close();
      }
    }
  };

  const getContainerDimensions = () => {
    switch (deviceFrame) {
      case 'tablet':
        return 'w-[540px] h-[720px]';
      case 'desktop':
        return 'w-[640px] h-[640px]';
      case 'mobile':
      default:
        return 'w-[360px] h-[640px]';
    }
  };

  return (
    <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-4 flex flex-col items-center">
      <div className="w-full flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-white flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
            <span>Live Interactive Sandbox</span>
          </h3>
          <p className="text-xs text-slate-400">Test playable touch interaction, mechanics and store CTA</p>
        </div>

        <div className="flex items-center space-x-2 bg-slate-900/90 p-1.5 rounded-xl border border-slate-800">
          <button
            onClick={() => onDeviceChange('mobile')}
            className={`p-2 rounded-lg text-xs font-medium transition ${
              deviceFrame === 'mobile' ? 'bg-cyan-500 text-white' : 'text-slate-400 hover:text-white'
            }`}
            title="iPhone 15 Portrait"
          >
            <Smartphone className="w-4 h-4" />
          </button>
          <button
            onClick={() => onDeviceChange('tablet')}
            className={`p-2 rounded-lg text-xs font-medium transition ${
              deviceFrame === 'tablet' ? 'bg-cyan-500 text-white' : 'text-slate-400 hover:text-white'
            }`}
            title="iPad Viewport"
          >
            <Tablet className="w-4 h-4" />
          </button>
          <button
            onClick={() => onDeviceChange('desktop')}
            className={`p-2 rounded-lg text-xs font-medium transition ${
              deviceFrame === 'desktop' ? 'bg-cyan-500 text-white' : 'text-slate-400 hover:text-white'
            }`}
            title="Square Banner View"
          >
            <Monitor className="w-4 h-4" />
          </button>
          <div className="h-4 w-px bg-slate-700 mx-1"></div>
          <button
            onClick={handleRestart}
            className="p-2 rounded-lg text-xs text-slate-300 hover:text-cyan-400 hover:bg-slate-800 transition"
            title="Restart Playable Scene"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Device Display Sandbox Wrapper */}
      <div className="w-full flex justify-center py-4 bg-slate-950/60 rounded-xl border border-slate-900 overflow-hidden relative min-h-[660px] items-center">
        <div className={`transition-all duration-300 relative rounded-3xl overflow-hidden shadow-2xl border-4 border-slate-700 bg-slate-900 ${getContainerDimensions()}`}>
          <iframe
            ref={iframeRef}
            className="w-full h-full border-none"
            title="Playable Ad Preview"
            sandbox="allow-scripts allow-same-origin allow-popups"
          />
        </div>
      </div>
    </div>
  );
};
