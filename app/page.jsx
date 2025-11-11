"use client";
import React, { useEffect, useState } from "react";

export default function JRAVISDashboardPage() {
  const [statuses, setStatuses] = useState([]);
  const [locked, setLocked] = useState(false);
  const [lastActivity, setLastActivity] = useState(Date.now());
  const LOCK_TIMEOUT = 5 * 60 * 1000; // 5 minutes

  const services = [
    {
      key: "backend",
      name: "JRAVIS Backend",
      url: "https://jravis-backend.onrender.com/api/status",
    },
    {
      key: "brain",
      name: "JRAVIS Brain",
      url: "https://jravis-brain.onrender.com/api/status",
    },
    {
      key: "intelligence",
      name: "Intelligence Worker",
      url: "https://mission2040-intelligence-worker.onrender.com/api/status",
    },
    {
      key: "memory_sync",
      name: "Memory Sync Worker",
      url: "https://mission2040-memory-sync-worker.onrender.com/api/status",
    },
    {
      key: "daily_report",
      name: "Daily Report",
      url: "https://jravis-daily-report.onrender.com/api/status",
    },
    {
      key: "weekly_report",
      name: "Weekly Report",
      url: "https://jravis-weekly-report.onrender.com/api/status",
    },
    {
      key: "va_bot_connector",
      name: "VA Bot Connector",
      url: "https://va-bot-connector.onrender.com/api/status",
    },
    {
      key: "income_system_bundle",
      name: "Income System Bundle",
      url: "https://income-system-bundle.onrender.com/api/status",
    },
  ];

  // --- Fetch live statuses ---
  const fetchStatuses = async () => {
    const results = await Promise.all(
      services.map(async (srv) => {
        try {
          const res = await fetch(srv.url, { cache: "no-store" });
          const ok = res.ok;
          const body = await res.json().catch(() => ({}));
          return { ...srv, ok, info: { ok, body } };
        } catch (e) {
          return { ...srv, ok: false, info: { ok: false, error: e.message } };
        }
      }),
    );
    setStatuses(results);
  };

  useEffect(() => {
    fetchStatuses();
    const interval = setInterval(fetchStatuses, 15000);
    return () => clearInterval(interval);
  }, []);

  // --- Idle auto-lock system ---
  useEffect(() => {
    const updateActivity = () => setLastActivity(Date.now());
    window.addEventListener("mousemove", updateActivity);
    window.addEventListener("keydown", updateActivity);

    const lockCheck = setInterval(() => {
      if (Date.now() - lastActivity > LOCK_TIMEOUT) setLocked(true);
    }, 30000);

    return () => {
      window.removeEventListener("mousemove", updateActivity);
      window.removeEventListener("keydown", updateActivity);
      clearInterval(lockCheck);
    };
  }, [lastActivity]);

  const unlock = () => setLocked(false);

  // --- Lock Screen ---
  if (locked) {
    return (
      <div className="h-screen flex flex-col items-center justify-center bg-black text-green-400">
        <h1 className="text-3xl mb-4 glow-green">🔒 JRAVIS Locked</h1>
        <p className="text-green-300 mb-6">Session idle for 5+ minutes.</p>
        <button
          onClick={unlock}
          className="px-5 py-2 bg-green-800/30 border border-green-500 rounded-lg hover:bg-green-700/40 glow-green"
        >
          Unlock
        </button>
      </div>
    );
  }

  // --- Dashboard View ---
  return (
    <main className="min-h-screen bg-black text-green-300 p-8 font-mono">
      <header className="mb-10 text-center">
        <h1 className="text-4xl glow-green font-bold">JRAVIS</h1>
        <p className="text-green-500 mt-2">
          Mission 2040 • System Intelligence Control Panel
        </p>
      </header>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {statuses.map((service) => (
          <article
            key={service.key}
            className={`glow-box ${service.ok ? "online" : "offline"} flex flex-col p-4 rounded-xl text-sm`}
          >
            <div className="flex items-center justify-between mb-2">
              <h2 className="font-bold text-green-300">{service.name}</h2>
              <div
                className={`w-3 h-3 rounded-full ${
                  service.ok
                    ? "bg-green-400 shadow-[0_0_8px_#00ff99]"
                    : "bg-red-500 shadow-[0_0_8px_#ff3333]"
                }`}
              ></div>
            </div>
            <div className="text-green-200/80">
              {service.ok
                ? "✅ Online — Running Smoothly"
                : `❌ Offline — ${service.info?.error || "No Response"}`}
            </div>
          </article>
        ))}
      </div>

      <footer className="text-center mt-12 text-green-400 text-xs">
        JRAVIS v5 • Auto-refresh every 15s • Locked after 5 min idle
      </footer>
    </main>
  );
}
