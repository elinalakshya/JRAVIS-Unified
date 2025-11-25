export default function MobileDashboard() {
  return (
    <div className="text-white p-4 space-y-4">
      <div className="text-center">
        <img src="/logo.png" className="mx-auto h-20" />
        <div className="text-xl tracking-widest mt-2">LAKSHYA 2040</div>
      </div>

      <div className="p-4 bg-black/30 rounded-xl border border-gray-700">
        <div className="text-center text-blue-300">T4 BOT | II OAISOR</div>

        <div className="space-y-2 mt-4">
          {[
            "Elina Reels",
            "Printify POD Store",
            "Mesty AI Store",
            "YouTube Automation",
          ].map((name, i) => (
            <div key={i} className="flex justify-between">
              <span>{name}</span>
              <span className="text-green-400">OK</span>
            </div>
          ))}
        </div>
      </div>

      <div className="p-4 bg-black/20 border border-gray-700 rounded-xl">
        <div className="text-gray-300 text-sm mb-2">
          Hit | How can I assist?
        </div>
        <input
          className="w-full bg-black/40 border border-gray-700 rounded-lg p-2"
          placeholder="How can I assist?"
        />
      </div>

      <button className="w-full py-3 rounded-lg bg-red-700">LOG OUT</button>
    </div>
  );
}
