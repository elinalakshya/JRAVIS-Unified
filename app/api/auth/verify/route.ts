import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const { code } = await req.json();

  const LOCK_CODE = process.env.LOCK_CODE; // stored in Render secrets

  if (code === LOCK_CODE) {
    return NextResponse.json({ ok: true });
  }

  return NextResponse.json({ ok: false });
}
