import React from 'react';

interface DeviceFrameProps {
  children: React.ReactNode;
  deviceType: 'iPhone' | 'Galaxy' | 'iPad';
}

export const DeviceFrame: React.FC<DeviceFrameProps> = ({ children, deviceType }) => {
  return (
    <div className="relative mx-auto border-slate-800 bg-slate-900 border-[12px] rounded-[40px] shadow-2xl overflow-hidden">
      {/* Speaker / Notch Bar */}
      <div className="w-[120px] h-[18px] bg-slate-800 absolute top-0 left-1/2 -translate-x-1/2 rounded-b-xl z-20 flex items-center justify-center">
        <div className="w-10 h-1.5 bg-slate-700 rounded-full"></div>
      </div>
      <div className="relative z-10">{children}</div>
    </div>
  );
};
