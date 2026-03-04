// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    build: {
      cssCodeSplit: false,
      rollupOptions: {
        output: {
          assetFileNames: '_astro/[name][extname]',
        }
      }
    }
  }
});