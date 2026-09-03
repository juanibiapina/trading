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
  ["BTOG","2026-08-20",0.76],
  ["LOOP","2026-08-20",1.11],
  ["SUGP","2026-08-21",4.27],
  ["LGO","2026-08-21",0.6701],
  ["ISPC","2026-08-21",1.79],
  ["WLDS","2026-08-25",2.66],
  ["XPON","2026-08-26",6.42],
  ["YYGH","2026-08-26",2.02],
  ["WNW","2026-08-27",3.81],
  ["DAIC","2026-08-27",5.81],
  ["AEMD","2026-08-28",3.17],
  ["MODD","2026-08-28",3.82],
  ["KITT","2026-09-02",0.8702],
  ["PXS","2026-09-02",5.98],
  ["UFG","2026-09-03",0.61],
  ["GELS","2026-09-03",0.861],
];
const CAP = "13:30:00Z"; // 09:30 ET
const limits = [5,10,15,20,30]; // resting sell-limit % above exit
const trails = [8,12,15,20];    // trailing-stop % from running high
// OCO-floor variant (08-20 refinement after LOOP dumped): resting +10% sell-limit
// PAIRED with a protective stop at floor F% below the exit price. A faller that
// ticks down through the floor market-outs there instead of riding to PM-last.
// floors: 0 = stop exactly at exit (breakeven), else F% below exit.
const ocoFloors = [0, 5, 10, 15, 20]; // % below exit for the protective stop, limit fixed +10%

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

// OCO: resting +10% sell-limit AND protective stop at exit*(1-F/100). Causal, per
// bar. Within a bar, check the stop first (pessimistic): if the low breaches the
// floor, market-out at the floor; else if the high reaches the +10% target, fill
// the limit. Else hold to cap, sell at last close.
function ocoExit(bars, exit, F){
  const target = exit*1.10;
  const stop = exit*(1-F/100);
  for(const b of bars){
    if(b.l <= stop) return {px:stop, hit:"stop"};
    if(b.h >= target) return {px:target, hit:"limit"};
  }
  const last = bars.length ? bars[bars.length-1].c : exit;
  return {px:last, hit:"cap"};
}

const pct = (px,exit)=> (px-exit)/exit*100;
const rows=[];
const sumL = {}; limits.forEach(L=>sumL[L]=0);
const sumT = {}; trails.forEach(T=>sumT[T]=0);
const sumO = {}; ocoFloors.forEach(F=>sumO[F]=0);
for(const [sym,date,exit] of names){
  const bars = fetchBars(sym,date);
  const row={sym};
  for(const L of limits){ const r=limitExit(bars,exit,L); const g=pct(r.px,exit); row["L"+L]=g; sumL[L]+=g; }
  for(const T of trails){ const r=trailExit(bars,exit,T); const g=pct(r.px,exit); row["T"+T]=g; sumT[T]+=g; }
  for(const F of ocoFloors){ const r=ocoExit(bars,exit,F); const g=pct(r.px,exit); row["O"+F]=g; row["O"+F+"h"]=r.hit; sumO[F]+=g; }
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
console.log("");
console.log("OCO: resting +10% sell-limit paired with protective stop F% below exit");
console.log("(plain L10 shown for contrast; hit = which leg filled):");
console.log("sym      L10   "+ocoFloors.map(F=>("O"+F+"%").padStart(8)+"  hit    ").join(""));
for(const r of rows){
  let line = r.sym.padEnd(6)+" "+f(r["L10"]).padStart(6)+"  ";
  for(const F of ocoFloors){ line += f(r["O"+F]).padStart(8)+"  "+String(r["O"+F+"h"]).padEnd(6)+" "; }
  console.log(line);
}
let sline = "SUM   "+f(sumL[10]).padStart(6)+"  ";
for(const F of ocoFloors){ sline += f(sumO[F]).padStart(8)+"  "+"".padEnd(6)+" "; }
console.log(sline);
let mline = "MEAN  "+f(sumL[10]/n).padStart(6)+"  ";
for(const F of ocoFloors){ mline += f(sumO[F]/n).padStart(8)+"  "+"".padEnd(6)+" "; }
console.log(mline);
const posL10 = rows.filter(r=>r["L10"]>0).length;
console.log("");
console.log("positive count: L10 "+posL10+"/"+n+"   "+ocoFloors.map(F=>"O"+F+" "+rows.filter(r=>r["O"+F]>0).length+"/"+n).join("   "));
