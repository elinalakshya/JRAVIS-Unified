import React from "react";

export default function ServiceCard({
  name,
  status,
}: {
  name: string;
  status: string;
}) {
  const color = status.startsWith("🟢")
    ? "bg-green-100 border-green-500"
    : status.startsWith("⚠️")
      ? "bg-yellow-100 border-yellow-500"
      : "bg-red-100 border-red-500";
  return (
    <div className={`p-5 border-2 rounded-2xl shadow-sm ${color}`}>
      <h2 className="text-xl font-semibold capitalize">
        {name.replace(/_/g, " ")}
      </h2>
      <p className="text-gray-700 mt-2">{status}</p>
    </div>
  );
}
