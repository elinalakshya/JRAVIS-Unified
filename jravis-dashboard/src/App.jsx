import React from "react";
import "./index.css";

export default function App() {
  return (
    <div className="min-h-screen bg-[var(--mission-bg)] text-[var(--mission-text)] flex flex-col items-center justify-center p-10">
      <h1 className="text-5xl font-bold jravis-header neon-text mb-6">
        JRAVIS CONTROL CENTER
      </h1>
      <p className="text-[var(--mission-subtext)] mb-10">
        Monitoring all systems — VA BOT • DAILY REPORT • BACKEND • PHASE 4
      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
        {/* Daily Report Card */}
        <div className="jravis-card pulse-neon text-center">
          <h2 className="text-xl neon-text mb-2">Daily Report</h2>
          <p>Status: ✅ Online</p>
          <p>Last Run: 10:00 AM IST</p>
        </div>

        {/* VA Bot Card */}
        <div className="jravis-card text-center">
          <h2 className="text-xl neon-text mb-2">VA BOT</h2>
          <p>Status: ⚙️ Active</p>
          <p>Next Task: Report Sync</p>
        </div>

        {/* Income Panel */}
        <div className="jravis-card text-center">
          <h2 className="text-xl neon-text mb-2">Income Summary</h2>
          <p>Total Earned: ₹12,45,200</p>
          <p>Next Update: Every 24 Hours</p>
        </div>
      </div>

      <footer className="mt-10 text-sm text-[var(--mission-subtext)]">
        Mission 2040 • Powered by JRAVIS & Dhruvayu
      </footer>
    </div>
  );
}
