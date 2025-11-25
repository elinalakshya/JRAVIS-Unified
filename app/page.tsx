import Image from "next/image";
import Sidebar from "@/components/Sidebar";
import HeaderBar from "@/components/HeaderBar";
import KPIBox from "@/components/KPIBox";
import ActivityGraph from "@/components/ActivityGraph";
import IncomeList from "@/components/IncomeList";
import ChatBox from "@/components/ChatBox";
import LogoutWatcher from "@/components/LogoutWatcher";

export default function Home() {
  return (
    <div className="w-full min-h-screen bg-gradient-to-b from-black via-gray-900 to-black text-white flex">

      {/* AUTO LOGOUT (IDLE 2 min) */}
      <LogoutWatcher />

      {/* SIDEBAR */}
      <Sidebar />

      {/* MAIN CONTENT */}
      <div className="flex-1 flex flex-col px-6 py-4 gap-6">

        {/* HEADER */}
        <HeaderBar />

        {/* KPI BOXES */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <KPIBox label="Total Earnings" value="$12,540" icon="💰" />
          <KPIBox label="Today" value="$312" icon="⚡" />
          <KPIBox label="This Month" value="$4,289" icon="📈" />
          <KPIBox label="Active Streams" value="30" icon="🛰️" />
        </div>

        {/* GRAPH + INCOME LIST + CHAT */}
        <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">

          {/* GRAPH - takes 2 columns */}
          <div className="xl:col-span-2">
            <ActivityGraph />
          </div>

          {/* RECENT EARNINGS */}
          <IncomeList />
        </div>

        {/* CHAT BOX FULL WIDTH */}
        <div className="grid grid-cols-1 gap-6 pb-10">
          <ChatBox />
        </div>
      </div>
    </div>
  );
}
