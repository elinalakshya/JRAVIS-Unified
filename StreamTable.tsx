"use client";
import { streams } from "@/lib/streams";

export default function StreamTable() {
  return (
    <div className="p-6 rounded-xl bg-black/30 border border-gray-700">
      <div className="flex space-x-4 mb-4">
        {["PHASE 1", "PHASE 2", "PHAISE", "THREEE"].map((tab) => (
          <button
            key={tab}
            className="px-4 py-1 rounded-lg text-xs border border-gray-600 bg-blue-900 text-white"
          >
            {tab}
          </button>
        ))}
      </div>

      <table className="w-full text-sm">
        <thead className="text-gray-400">
          <tr>
            <th className="text-left">#</th>
            <th className="text-left">STREAM NAME</th>
            <th>LAST RUN</th>
            <th>STATUS</th>
          </tr>
        </thead>

        <tbody className="text-gray-200">
          {streams.map((s, i) => (
            <tr key={i} className="border-t border-gray-700">
              <td>{i + 1}</td>
              <td>{s.name}</td>
              <td className="text-center">{s.time}</td>
              <td className="text-green-400">{s.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
