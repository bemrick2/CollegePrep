import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  // The parent email composer lives with its edge function (supabase/functions/send-weekly-digest/digest.ts) and is
  // imported by the in-app preview, so the dev server may read that folder.
  server: { fs: { allow: ['.', '../supabase/functions'] } },
})
