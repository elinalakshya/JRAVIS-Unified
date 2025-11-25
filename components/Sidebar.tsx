"use client";

import { Home, LogOut, Wallet, Bot, BarChart3 } from "lucide-react";

export default function Sidebar() {
  return (
    <div className="w-20 bg-black/30 border-r border-white/10 flex flex-col items-center py-6 gap-6">
      <Home className="text-white/80" size={26} />
      <BarChart3 className="text-white/80" size={26} />
      <Bot className="text-white/80" size={26} />
      <Wallet className="text-white/80" size={26} />

      <div className="mt-auto pb-4">
        <LogOut className="text-red-400" size={26} />
      </div>
    </div>
  );
}
