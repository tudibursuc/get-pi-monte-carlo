import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig(async () => {
  const sveltePreprocess = (await import('svelte-preprocess')).default;

  return {
    root: 'app',
    plugins: [
      svelte({
        preprocess: sveltePreprocess(),
        compilerOptions: {
          // Enable Svelte 4 compatible component API mode
          compatibility: {
            componentApi: 4
          }
        }
      })
    ],
    server: { port: 5173 },
    build: { outDir: '../dist' }
  };
});
