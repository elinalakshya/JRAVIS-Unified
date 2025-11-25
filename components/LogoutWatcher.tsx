"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function LogoutWatcher() {
  const router = useRouter();

  useEffect(() => {
    let timer: NodeJS.Timeout;

    const resetTimer = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        router.push("/login");
      }, 2 * 60 * 1000); // 2 minutes
    };

    window.onload = resetTimer;
    document.onmousemove = resetTimer;
    document.onkeydown = resetTimer;
    document.onclick = resetTimer;
    document.onscroll = resetTimer;

    resetTimer();
  }, [router]);

  return null;
}
