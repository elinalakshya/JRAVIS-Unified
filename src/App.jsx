import React from "react";

export default function App() {
  const streams = [
    { name: "Elma Reels", status: "OK", time: "10:30 AM" },
    { name: "Printify POD Store", status: "OK", time: "10:28 AM" },
    { name: "Mesity AI Store", status: "RUNNING", time: "10:25 AM" },
    { name: "YouTube Automation", status: "OK", time: "10:22 AM" },
    { name: "Stock Image/Video", status: "OK", time: "10:18 AM" },
    { name: "KDP AI Publishing", status: "OK", time: "10:18 AM" },
    { name: "Stationery Export", status: "OK", time: "10:17 AM" },
  ];

  return (
    <div className="min-h-screen bg-[#0a0a0f] text-slate-200 p-6 flex flex-col gap-6">
      <header className="text-center">
        <h1 className="text-2xl font-bold text-[#00e0ff]">
          JRAVIS DASHBOARD v6
        </h1>
        <p className="text-slate-400 text-sm">PHASE 1 — GLOBAL SYSTEM STATUS</p>
      </header>

      <main className="grid md:grid-cols-3 gap-6">
        <section className="bg-[#11121a] rounded-2xl p-4 shadow-lg border border-slate-800">
          <h2 className="text-lg font-semibold mb-2">System Status</h2>
          <ul className="space-y-2 text-sm">
            <li>
              JRAVIS Brain: <span className="text-green-400">ACTIVE</span>
            </li>
            <li>
              VA Bot: <span className="text-green-400">ACTIVE</span>
            </li>
            <li>
              API Calls: <span className="text-sky-400">200 K</span>
            </li>
          </ul>
        </section>

        <section className="bg-[#11121a] rounded-2xl p-4 shadow-lg border border-slate-800 flex flex-col justify-between">
          <div>
            <h2 className="text-lg font-semibold mb-2">Income Summary</h2>
            <p className="text-slate-400 text-sm">Target 12 %</p>
          </div>
          <div className="text-center">
            <p className="text-3xl font-bold text-green-400">₹ 14 280</p>
            <p className="text-slate-400 text-xs">Today’s Earnings</p>
          </div>
          <div className="text-center">
            <p className="text-xl font-semibold">₹ 1.06 L / Month</p>
          </div>
        </section>

        <section className="bg-[#11121a] rounded-2xl p-4 shadow-lg border border-slate-800 flex flex-col">
          <h2 className="text-lg font-semibold mb-2">JRAVIS Assistant</h2>
          <div className="flex-1 text-slate-400 text-sm overflow-y-auto">
            <p>[10:30 AM] Elma Reels → OK</p>
            <p>[10:28 AM] Printify POD → OK</p>
            <p>[10:25 AM] Mesity AI → RUNNING</p>
          </div>
        </section>
      </main>

      <section className="bg-[#11121a] rounded-2xl p-4 border border-slate-800">
        <h2 className="text-lg font-semibold mb-3">Active Streams</h2>
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left border-collapse">
            <thead>
              <tr className="border-b border-slate-700 text-slate-400">
                <th className="p-2">#</th>
                <th className="p-2">Stream Name</th>
                <th className="p-2">Last Run</th>
                <th className="p-2">Status</th>
              </tr>
            </thead>
            <tbody>
              {streams.map((s, i) => (
                <tr
                  key={i}
                  className="border-b border-slate-800 hover:bg-slate-800/40"
                >
                  <td className="p-2">{i + 1}</td>
                  <td className="p-2">{s.name}</td>
                  <td className="p-2">{s.time}</td>
                  <td
                    className={`p-2 ${
                      s.status === "OK"
                        ? "text-green-400"
                        : s.status === "RUNNING"
                          ? "text-yellow-400"
                          : "text-red-400"
                    }`}
                  >
                    {s.status}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <footer className="text-center text-xs text-slate-500">
        JRAVIS Assistant Online | LAKSHYA 2040
      </footer>
    </div>
  );
}
