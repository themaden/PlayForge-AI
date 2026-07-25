import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#090d16",
        surface: "#111827",
        border: "#1f293d",
        brand: {
          50: '#f0f9ff',
          500: '#06b6d4',
          600: '#0891b2',
          700: '#0e7490',
        }
      },
    },
  },
  plugins: [],
};
export default config;
