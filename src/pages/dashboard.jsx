import React from "react";
import dynamic from "next/dynamic";

// ✅ Load the JRAVIS Dashboard dynamically (no SSR) to avoid backend calls during build
const JravisDashboard = dynamic(() => import("../components/JravisDashboard"), {
  ssr: false,
  loading: () => (
    <div className="min-h-screen flex items-center justify-center bg-black text-slate-400">
      <div className="text-center">
        <div className="animate-spin border-4 border-slate-700 border-t-indigo-500 rounded-full w-10 h-10 mx-auto mb-4"></div>
        <p>Loading JRAVIS Dashboard...</p>
      </div>
    </div>
  ),
});

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-black text-slate-200 font-sans">
      <JravisDashboard />
    </div>
  );
}
