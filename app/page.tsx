"use client";
import { useEffect, useState } from "react";
import ServiceCard from "./components/ServiceCard";

export default function Dashboard() {
  const [status, setStatus] = useState<{ [k: string]: string }>({});

  const load = async () => {
    const r = await fetch("/api/status");
    const data = await r.json();
    setStatus(data);
  };

  useEffect(() => {
    load();
    const id = setInterval(load, 15000);
    return () => clearInterval(id);
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 p-10">
      <h1 className="text-4xl font-bold mb-6 text-gray-800">
        JRAVIS Dashboard v5
      </h1>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(status).map(([k, v]) => (
          <ServiceCard key={k} name={k} status={v} />
        ))}
      </div>
    </main>
  );
}
