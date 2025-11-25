"use client";
import { Progress } from "@/components/ui/progress";

export default function IncomeCard() {
  return (
    <div className="p-6 rounded-xl bg-black/30 border border-gray-700">
      <div className="text-sm font-semibold text-gray-300">
        INCOME → LIVE FEED
      </div>

      <Progress value={70} className="mt-4" />

      <div className="grid grid-cols-3 mt-4 text-gray-300 text-sm">
        <div>
          <div>Target</div>
          <div className="text-2xl text-white font-bold">12%</div>
        </div>

        <div>
          <div>Monthly</div>
          <div className="text-2xl text-white font-bold">₹1.06 L</div>
        </div>

        <div>
          <div>Daily</div>
          <div className="text-2xl text-white font-bold">₹14,280</div>
        </div>
      </div>
    </div>
  );
}
