import React from "react";

export default function KPIBox({ label, value, icon }) {
  return (
    <div className="bg-black/30 border border-white/10 rounded-2xl p-6 flex items-center gap-4 min-w-[220px]">
      <div className="text-blue-400">{icon}</div>
      <div>
        <div className="text-white/60 text-sm">{label}</div>
        <div className="text-2xl font-semibold">{value}</div>
      </div>
    </div>
  );
}
