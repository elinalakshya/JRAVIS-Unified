import React, { useEffect, useState, useRef } from "react";

// JRAVIS Dashboard
// Single-file React component (export default) using TailwindCSS
// - Dark futuristic AI control center look
// - Desktop + Mobile responsive
// - Polls health, earnings, tasks, and logs
// - Controls are present but DISABLED by default (to avoid disturbing deployed services)
// Usage: place in a React app (Vite / Next.js). Tailwind must be configured.

const POLL_INTERVAL = 6000; // ms

function StatusDot({ status }) {
  const color =
    status === "healthy"
      ? "bg-green-400"
      : status === "degraded"
        ? "bg-yellow-400"
        : "bg-red-500";
  return <span className={`inline-block w-3 h-3 rounded-full ${color}`} />;
}

export default function JravisDashboard() {
  const [health, setHealth] = useState({
    "jravis-backend": { status: "unknown" },
    "jravis-daily-report": { status: "unknown" },
    "va-bot": { status: "unknown" },
  });
  const [earnings, setEarnings] = useState({
    today: 0,
    week: 0,
    month: 0,
    total: 0,
  });
  const [tasks, setTasks] = useState([]);
  const [logs, setLogs] = useState([]);
  const [lastUpdate, setLastUpdate] = useState(null);
  const [controlsEnabled, setControlsEnabled] = useState(false); // must stay false to avoid disturbing
  const isMounted = useRef(true);

  // Helper: safe fetch with timeout
  async function safeFetch(url, opts = {}) {
    try {
      const controller = new AbortController();
      const id = setTimeout(() => controller.abort(), 10000);
      const res = await fetch(url, { ...opts, signal: controller.signal });
      clearTimeout(id);
      if (!res.ok)
        return { ok: false, status: res.status, text: await res.text() };
      const ct = res.headers.get("content-type") || "";
      if (ct.includes("application/json")) {
        const j = await res.json();
        return { ok: true, json: j };
      }
      const txt = await res.text();
      return { ok: true, text: txt };
    } catch (e) {
      return { ok: false, err: String(e) };
    }
  }

  // Polling functions
  async function pollHealth() {
    // endpoints (public): change if needed
    const services = {
      "jravis-backend": "https://jravis-backend.onrender.com/health",
      "jravis-daily-report": "https://jravis-daily-report.onrender.com/health",
      "va-bot": "https://va-bot.onrender.com/health",
    };

    const next = {};
    for (const [k, url] of Object.entries(services)) {
      const r = await safeFetch(url);
      if (r.ok && (r.json || r.text)) {
        next[k] = { status: "healthy", raw: r.json ?? r.text };
      } else if (r.status && r.status >= 400) {
        next[k] = { status: "down", raw: r.text ?? r.err };
      } else {
        next[k] = { status: "unknown", raw: r.err ?? r.text };
      }
    }
    if (isMounted.current) setHealth(next);
  }

  async function pollEarnings() {
    // placeholder endpoint; backend should expose this
    const url = "https://jravis-backend.onrender.com/api/earnings/summary";
    const r = await safeFetch(url);
    if (r.ok && r.json) {
      if (isMounted.current) setEarnings(r.json);
    }
  }

  async function pollTasks() {
    const url = "https://jravis-backend.onrender.com/api/tasks/recent";
    const r = await safeFetch(url);
    if (r.ok && r.json) {
      if (isMounted.current) setTasks(r.json.slice(0, 10));
    }
  }

  async function pollLogs() {
    const url = "https://jravis-backend.onrender.com/api/logs/recent";
    const r = await safeFetch(url);
    if (r.ok && r.json) {
      if (isMounted.current) setLogs(r.json.slice(0, 30));
    }
  }

  useEffect(() => {
    isMounted.current = true;
    // initial load
    (async () => {
      await Promise.all([
        pollHealth(),
        pollEarnings(),
        pollTasks(),
        pollLogs(),
      ]);
      setLastUpdate(new Date().toISOString());
    })();

    const id = setInterval(async () => {
      await Promise.all([
        pollHealth(),
        pollEarnings(),
        pollTasks(),
        pollLogs(),
      ]);
      setLastUpdate(new Date().toISOString());
    }, POLL_INTERVAL);

    return () => {
      isMounted.current = false;
      clearInterval(id);
    };
  }, []);

  // Controls (disabled by default)
  async function triggerReport() {
    if (!controlsEnabled)
      return alert(
        "Controls disabled to avoid changing live services. Enable Controls to use.",
      );
    const r = await safeFetch(
      "https://jravis-backend.onrender.com/api/trigger_report",
      { method: "POST" },
    );
    if (r.ok) alert("Triggered");
    else alert("Trigger failed");
  }

  // UI
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-black to-gray-900 text-slate-200 p-4 font-sans">
      <div className="max-w-7xl mx-auto">
        <header className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 bg-gradient-to-br from-indigo-600 to-pink-600 rounded-xl flex items-center justify-center text-xl font-bold">
              JR
            </div>
            <div>
              <h1 className="text-2xl font-bold">JRAVIS Control Center</h1>
              <div className="text-sm text-slate-400">
                AI ops · Live monitoring · Mission 2040
              </div>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <div className="text-sm text-slate-400 mr-2">Last sync</div>
            <div className="text-sm font-mono bg-slate-800 px-3 py-1 rounded">
              {lastUpdate ? new Date(lastUpdate).toLocaleString() : "—"}
            </div>
            <button
              onClick={() => {
                setControlsEnabled(!controlsEnabled);
              }}
              className={`px-3 py-2 rounded ${controlsEnabled ? "bg-red-600" : "bg-slate-700"}`}
            >
              {controlsEnabled ? "Controls: ON" : "Controls: OFF"}
            </button>
          </div>
        </header>

        <main className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left: System Health + Logs */}
          <section className="lg:col-span-2 space-y-6">
            <div className="bg-gradient-to-br from-slate-800/60 to-black/40 border border-slate-700 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-4">System Health</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {Object.keys(health).map((k) => {
                  const s = health[k]?.status || "unknown";
                  return (
                    <div
                      key={k}
                      className="p-3 rounded-lg bg-slate-900/40 border border-slate-700"
                    >
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                          <StatusDot status={s} />
                          <div>
                            <div className="text-sm text-slate-400">{k}</div>
                            <div className="text-sm font-medium">
                              {s === "healthy"
                                ? "Healthy"
                                : s === "down"
                                  ? "Down"
                                  : "Unknown"}
                            </div>
                          </div>
                        </div>
                        <div className="text-xs text-slate-500">
                          {health[k]?.raw
                            ? typeof health[k].raw === "string"
                              ? "raw"
                              : "json"
                            : "--"}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="bg-gradient-to-br from-slate-800/60 to-black/40 border border-slate-700 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-4">Activity Log</h2>
              <div className="h-64 overflow-auto bg-black/30 p-3 rounded">
                {logs.length === 0 ? (
                  <div className="text-slate-500">No activity yet.</div>
                ) : (
                  <ul className="space-y-2 text-sm font-mono">
                    {logs.map((l, idx) => (
                      <li key={idx} className="text-slate-300">
                        {new Date(l.ts || Date.now()).toLocaleTimeString()} •{" "}
                        {l.msg || JSON.stringify(l).slice(0, 120)}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            </div>
          </section>

          {/* Right: Earnings + Tasks + Controls */}
          <aside className="space-y-6">
            <div className="bg-gradient-to-br from-slate-800/60 to-black/40 border border-slate-700 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-4">Earnings Snapshot</h2>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <div className="text-sm text-slate-400">Today</div>
                  <div className="text-xl font-bold">₹{earnings.today}</div>
                </div>
                <div className="flex items-center justify-between text-slate-400">
                  <div className="text-sm">This week</div>
                  <div className="font-medium">₹{earnings.week}</div>
                </div>
                <div className="flex items-center justify-between text-slate-400">
                  <div className="text-sm">This month</div>
                  <div className="font-medium">₹{earnings.month}</div>
                </div>
                <div className="flex items-center justify-between text-slate-400">
                  <div className="text-sm">Total</div>
                  <div className="font-medium">₹{earnings.total}</div>
                </div>
              </div>
            </div>

            <div className="bg-gradient-to-br from-slate-800/60 to-black/40 border border-slate-700 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-4">Tasks</h2>
              <div className="space-y-2 text-sm">
                {tasks.length === 0 ? (
                  <div className="text-slate-500">No tasks</div>
                ) : (
                  <ul className="space-y-2">
                    {tasks.map((t, i) => (
                      <li
                        key={i}
                        className="flex items-start justify-between gap-3"
                      >
                        <div>
                          <div className="text-sm font-medium">
                            {t.title || t.name}
                          </div>
                          <div className="text-xs text-slate-400">
                            {t.status || "pending"}
                          </div>
                        </div>
                        <div className="text-xs text-slate-500">
                          {t.owner || ""}
                        </div>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            </div>

            <div className="bg-gradient-to-br from-slate-800/60 to-black/40 border border-slate-700 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-4">Controls</h2>
              <div className="space-y-3 text-sm">
                <button
                  onClick={triggerReport}
                  disabled={!controlsEnabled}
                  className={`w-full px-3 py-2 rounded ${controlsEnabled ? "bg-indigo-600" : "bg-slate-700/50 cursor-not-allowed"}`}
                >
                  Trigger Daily Report
                </button>
                <button
                  disabled
                  className="w-full px-3 py-2 rounded bg-slate-700/50 cursor-not-allowed"
                >
                  Restart Services
                </button>
                <div className="text-xs text-slate-500">
                  Controls are disabled by default to avoid disrupting live
                  services.
                </div>
              </div>
            </div>
          </aside>
        </main>

        <footer className="mt-8 text-center text-xs text-slate-500">
          JRAVIS · Mission 2040 · Dashboard
        </footer>
      </div>
    </div>
  );
}
