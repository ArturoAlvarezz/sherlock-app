/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cyber-dark': '#050509',
        'cyber-purple': '#bc13fe',
        'cyber-neon': '#bf00ff',
      },
      fontFamily: {
        'mono': ['"Fira Code"', '"Roboto Mono"', 'monospace'],
      },
      boxShadow: {
        'neon': '0 0 5px #bc13fe, 0 0 20px #bc13fe',
        'neon-strong': '0 0 10px #bc13fe, 0 0 40px #bc13fe',
      }
    },
  },
  plugins: [],
}
