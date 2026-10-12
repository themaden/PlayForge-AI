import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'PlayForge Studio',
  description: 'Local HTML5 tap puzzle prototype with code checks and human review.',
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
