"use client";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { day: "Mon", income: 120 },
  { day: "Tue", income: 200 },
  { day: "Wed", income: 150 },
  { day: "Thu", income: 300 },
  { day: "Fri", income: 250 },
  { day: "Sat", income: 400 },
  { day: "Sun", income: 350 },
];

export default function ActivityGraph() {
  return (
    <div className="bg-black/30 border border-white/10 rounded-2xl p-6 w-full h-[320px]">
      <h2 className="mb-4 text-white/80 font-medium">Weekly Earnings</h2>

      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data}>
          <defs>
            <linearGradient id="colorIncome" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.6} />
              <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
            </linearGradient>
          </defs>

          <XAxis dataKey="day" stroke="#666" />
          <YAxis stroke="#666" />
          <Tooltip />

          <Area
            type="monotone"
            dataKey="income"
            stroke="#3b82f6"
            strokeWidth={3}
            fill="url(#colorIncome)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
