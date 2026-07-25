import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'PlayForge AI - AI-Powered Playable Game Ad Generation Platform',
  description: 'Automated HTML5 Playable Game Ad Generation Platform powered by 5 AI Agents and Phaser 3.80 engine.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased bg-slate-950 text-slate-100 min-h-screen">
        {children}
      </body>
    </html>
  );
}
