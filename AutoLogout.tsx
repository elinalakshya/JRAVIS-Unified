"use client";

import { useEffect } from "react";

export default function AutoLogout() {
  useEffect(() => {
    let timer: NodeJS.Timeout;

    const resetTimer = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        window.location.href = "/login"; // redirect
      }, 120000); // 2 minutes
    };

    window.addEventListener("mousemove", resetTimer);
    window.addEventListener("keydown", resetTimer);
    resetTimer();

    return () => {
      clearTimeout(timer);
    };
  }, []);

  return null;
}
