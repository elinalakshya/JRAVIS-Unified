import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// ✅ Allow Replit & external preview hosts
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    allowedHosts: [".repl.co", ".replit.dev"],
  },
});
