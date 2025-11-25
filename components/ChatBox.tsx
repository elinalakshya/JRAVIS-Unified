"use client";

import { useState } from "react";

export default function ChatBox() {
  const [messages, setMessages] = useState([
    { from: "jravis", text: "Boss, system stable and earning mode active." },
  ]);

  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;

    setMessages([...messages, { from: "user", text: input }]);
    setInput("");

    setTimeout(() => {
      setMessages((m) => [
        ...m,
        { from: "jravis", text: "Acknowledged Boss." },
      ]);
    }, 800);
  };

  return (
    <div className="bg-black/30 border border-white/10 rounded-2xl p-6 w-full h-[360px] flex flex-col">
      <h2 className="text-white/80 mb-3 font-medium">JRAVIS Chat</h2>

      {/* Chat window */}
      <div className="flex-1 overflow-y-auto space-y-3 pr-2 custom-scroll">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-3 rounded-xl max-w-[80%] ${
              msg.from === "user"
                ? "bg-blue-600 ml-auto text-white"
                : "bg-white/10 text-white/80"
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      {/* Input */}
      <div className="mt-4 flex gap-2">
        <input
          className="flex-1 bg-white/10 p-3 rounded-xl text-white outline-none"
          placeholder="Message JRAVIS…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="bg-blue-600 px-4 rounded-xl" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}
