export default function BrainStatus() {
  return (
    <div className="p-6 rounded-xl bg-black/30 border border-gray-700">
      <h2 className="text-lg font-bold mb-4">JRAVIS BRAIN</h2>

      <div className="space-y-2">
        <div className="flex justify-between">
          <span>Status:</span>
          <span className="text-green-400 font-semibold">ACTIVE</span>
        </div>

        <div className="flex justify-between">
          <span>Status:</span>
          <span className="text-green-400 font-semibold">ACTIVE</span>
        </div>

        <div className="flex justify-between">
          <span>Last Loop:</span>
          <span>10:24 AM</span>
        </div>

        <div className="flex justify-between">
          <span>API:</span>
          <span>200 K</span>
        </div>
      </div>

      <div className="text-center mt-6">
        <img src="/logo.png" className="mx-auto h-24 opacity-90" />
        <div className="mt-2 text-2xl tracking-widest">LAKSHYA 2040</div>
      </div>
    </div>
  );
}
