#!/usr/bin/env node
// premarket-exit-pulse-sweep.js — Init 3: for each seeded held name, price at each
// candidate fixed second-pulse time (Z) vs our 04:30 ET exit. Sums the realistic
// capturable gain per candidate time (NOT the perfect intrabar peak). LOG-ONLY.
const { execFileSync } = require("child_process");
// name, date, exitPrice
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
];
// candidate second-pulse times in Z (EDT: ET+4h)
const times = ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00"]; // Z
function etLabel(z){const[h,m]=z.split(":").map(Number);let e=h-4;return `${String(e).padStart(2,"0")}:${m===0?"00":m}ET`;}
const sums = {}; times.forEach(t=>sums[t]=0);
const rows=[];
for(const [sym,date,exit] of names){
  const out = execFileSync("node",["scripts/broker.js","bars",sym,"--start",`${date}T08:30:00Z`,"--json"],{encoding:"utf8"});
  const j=JSON.parse(out); const bars=j.bars||j;
  const row={sym};
  for(const t of times){
    // find bar at exactly date T t :00Z, else the last bar at/before it but same PM day <13:30Z
    const target=`${date}T${t}:00Z`;
    let chosen=null;
    for(const b of bars){ if(b.t>=`${date}T08:30:00Z` && b.t<`${date}T13:30:00Z` && b.t<=target) chosen=b; }
    if(chosen){ const g=(chosen.c-exit)/exit*100; row[t]=g; sums[t]+=g; }
    else row[t]=null;
  }
  rows.push(row);
}
console.log("sym    "+times.map(etLabel).map(s=>s.padStart(8)).join(""));
for(const r of rows){ console.log(r.sym.padEnd(6)+" "+times.map(t=>(r[t]==null?"    n/a":(r[t]>=0?"+":"")+r[t].toFixed(1)).padStart(8)).join("")); }
console.log("SUM   "+times.map(t=>("+"+sums[t].toFixed(1)).padStart(8)).join(""));
