import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../static/react-hero',
    emptyOutDir: true,
    lib: {
      entry: 'src/main.jsx',
      name: 'HeroReactBackground',
      formats: ['iife'],
      fileName: () => 'hero-react.js'
    }
  }
});
