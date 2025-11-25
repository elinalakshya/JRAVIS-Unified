"use client";

import { useState } from "react";
import { Lock } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function LoginScreen() {
  const [code, setCode] = useState("");

  const handleLogin = async () => {
    const res = await fetch("/api/auth/verify", {
      method: "POST",
      body: JSON.stringify({ code }),
    });

    const data = await res.json();

    if (data.ok) {
      localStorage.setItem("lakshya-auth", "true");
      window.location.href = "/dashboard";
    } else {
      alert("Wrong Lock Code");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black text-white px-6">
      <div className="w-full max-w-sm bg-zinc-900/60 backdrop-blur-xl rounded-2xl p-8 shadow-2xl border border-zinc-800">
        <h1 className="text-3xl font-bold text-center mb-8">Lakshya Login</h1>

        <div className="relative mb-6">
          <Lock className="absolute left-3 top-3 h-5 w-5 text-zinc-500" />
          <input
            type="password"
            placeholder="Enter Lock Code"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="
              w-full py-3 pl-10 pr-4 rounded-xl 
              bg-zinc-800 border border-zinc-700
              focus:ring-2 focus:ring-purple-500
              text-white placeholder-zinc-500
            "
          />
        </div>

        <Button
          onClick={handleLogin}
          className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-xl"
        >
          Unlock Dashboard
        </Button>
      </div>
    </div>
  );
}
