#!/usr/bin/env node
// peak-seeking-exit-sim.js — Init 3 execution pivot. LOG-ONLY, no orders.
//
// The 08-13 pulse-sweep showed a FIXED second exit pulse captures little of the
// +251% peak-ceiling (best time +25% total, one-outlier-driven). This tool tests
// the alternative the evidence pointed to: a PEAK-SEEKING exit set at the 04:30 ET
// exit decision — a resting sell-limit above our exit, or a trailing stop from the
// running high — walked across the real premarket SIP 5-min path, capped at 09:30
// ET (13:30Z, never holding into the open).
//
// Baseline = our actual 04:30 ET exit price. Positive = the peak-seeking rule beats
// selling at 04:30. Each name's fill is decided causally (bar order), so this is
// what the rule would realistically have captured, not the perfect intrabar peak.
const { execFileSync } = require("child_process");
// name, date, exitPrice (our real 04:30 ET fill, from premarket-exit-gap.csv)
const names = [
  ["PAVS","2026-08-06",6.65],
  ["CELZ","2026-08-06",0.8339],
  ["WAFU","2026-08-11",2.10],
  ["MTEN","2026-08-11",1.35],
  ["MGIH","2026-08-11",2.02],
  ["BAOS","2026-08-12",2.24],
  ["BOXL","2026-08-12",5.83],
  ["FF","2026-08-12",6.20],
  ["GXAI","2026-08-13",1.28],
  ["DARE","2026-08-18",0.83],
  ["GRSD","2026-08-18",2.01],
  ["ONFO","2026-08-18",2.26],
  ["SGLY","2026-08-18",5.35],
  ["XOS","2026-08-18",3.48],
  ["MSS","2026-08-19",2.20],
  ["TNON","2026-08-19",9.74],
];
const CAP = "13:30:00Z"; // 09:30 ET
const limits = [5,10,15,20,30]; // resting sell-limit % above exit
const trails = [8,12,15,20];    // trailing-stop % from running high

function fetchBars(sym, date){
  const out = execFileSync("node",["scripts/broker.js","bars",sym,"--start",`${date}T08:30:00Z`,"--json"],{encoding:"utf8"});
  const j = JSON.parse(out);
  const bars = (j.bars||j).filter(b=> b.t > `${date}T08:30:00Z` && b.t < `${date}T${CAP}`);
  return bars;
}

// Resting sell-limit at exit*(1+L/100). Fill at limit on first bar whose high reaches it.
// Else hold to cap, sell at last close.
function limitExit(bars, exit, L){
  const target = exit*(1+L/100);
  for(const b of bars){ if(b.h >= target) return {px:target, hit:true}; }
  const last = bars.length ? bars[bars.length-1].c : exit;
  return {px:last, hit:false};
}
// Trailing stop T% from running high (seeded at exit). Exit at stop when a bar low
// breaches it. Else hold to cap, sell at last close.
function trailExit(bars, exit, T){
  let hi = exit;
  for(const b of bars){
    hi = Math.max(hi, b.h);
    const stop = hi*(1-T/100);
    if(b.l <= stop) return {px:stop};
  }
  const last = bars.length ? bars[bars.length-1].c : exit;
  return {px:last};
}

const pct = (px,exit)=> (px-exit)/exit*100;
const rows=[];
const sumL = {}; limits.forEach(L=>sumL[L]=0);
const sumT = {}; trails.forEach(T=>sumT[T]=0);
for(const [sym,date,exit] of names){
  const bars = fetchBars(sym,date);
  const row={sym};
  for(const L of limits){ const r=limitExit(bars,exit,L); const g=pct(r.px,exit); row["L"+L]=g; sumL[L]+=g; }
  for(const T of trails){ const r=trailExit(bars,exit,T); const g=pct(r.px,exit); row["T"+T]=g; sumT[T]+=g; }
  rows.push(row);
}
const n = names.length;
const f = g => (g>=0?"+":"")+g.toFixed(1);
console.log("Resting sell-limit % above 04:30 exit (gain vs our exit, capped 09:30 ET):");
console.log("sym    "+limits.map(L=>("L"+L+"%").padStart(8)).join(""));
for(const r of rows) console.log(r.sym.padEnd(6)+" "+limits.map(L=>f(r["L"+L]).padStart(8)).join(""));
console.log("SUM   "+limits.map(L=>f(sumL[L]).padStart(8)).join(""));
console.log("MEAN  "+limits.map(L=>f(sumL[L]/n).padStart(8)).join(""));
console.log("");
console.log("Trailing stop % from running high (gain vs our exit, capped 09:30 ET):");
console.log("sym    "+trails.map(T=>("T"+T+"%").padStart(8)).join(""));
for(const r of rows) console.log(r.sym.padEnd(6)+" "+trails.map(T=>f(r["T"+T]).padStart(8)).join(""));
console.log("SUM   "+trails.map(T=>f(sumT[T]).padStart(8)).join(""));
console.log("MEAN  "+trails.map(T=>f(sumT[T]/n).padStart(8)).join(""));
