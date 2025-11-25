export default function IncomeList() {
  const items = [
    { stream: "Printables", amt: "$12.00", time: "5 min ago" },
    { stream: "YouTube Automation", amt: "$34.50", time: "30 min ago" },
    { stream: "Affiliate", amt: "$5.80", time: "1 hr ago" },
    { stream: "Meshy AI", amt: "$29.10", time: "2 hr ago" }
  ];

  return (
    <div className="bg-black/30 border border-white/10 rounded-2xl p-6 w-full">
      <h2 className="text-white/80 mb-4 font-medium">Recent Earnings</h2>

      <div className="flex flex-col gap-4">
        {items.map((item, i) => (
          <div
            key={i}
            className="flex justify-between p-3 bg-white/5 rounded-xl"
          >
            <div className="text-white">{item.stream}</div>
            <div className="text-green-400 font-semibold">{item.amt}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
