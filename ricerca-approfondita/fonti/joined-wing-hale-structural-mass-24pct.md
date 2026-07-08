# Analysis of Structural Characteristics of the HALE Joined-Wing Configuration UAV (+ aero-structural joined-wing hi-fidelity)

- **Fonti:**
  - Sun et al. (2025), "Analysis of Structural Characteristics of the HALE Joined-Wing Configuration UAV", International Journal of Aerospace Engineering (Wiley) — https://onlinelibrary.wiley.com/doi/10.1155/ijae/9931529 (DOI 10.1155/ijae/9931529)
  - "Aero-structural design of joined-wing aircraft based on high-fidelity model", Chinese Journal of Aeronautics — https://www.sciencedirect.com/science/article/pii/S1000936123003783
- **Data accesso:** luglio 2026
- **Tipo evidenza:** numerico (FEM/aero-strutturale alta fedeltà)

## Cosa supporta (claim del report 22)
- **Claim 3 (risparmio di massa strutturale): quantificato — MA rispetto alla flying wing, non al monoplano cantilever, e con vincolo di deformazione.**

## Estratti chiave
- "When limiting wingtip deformation to 10% of semi-span, the structural mass of the **joined-wing configuration is reduced by approximately 24.1% compared with that of the flying wing** configuration."
- Il rear wing supporta il front wing; la connessione forma un box torsion-resistant che aumenta la rigidezza e riduce la massa strutturale.

## Rilevanza per BOXY C3 — attenzione al benchmark
Il **24.1%** è un risparmio **vs flying wing** (config già pesante/flessibile), **non vs un monoplano cantilever convenzionale**, e vale sotto uno **specifico vincolo di deflessione (10% semiapertura)** tipico di ali high-AR flessibili. Non è trasferibile a un VTOL C3 rigido da 25 kg, dove la massa alare è già piccola (~2–3 kg) e i carichi modesti. Conferma il report 22: il vantaggio di massa strutturale è **reale in casi high-AR/flessibili** ma **trascurabile (≤2% MTOM) a scala C3**. Nota di sistema: questi lavori mostrano che il joined-wing è studiato **soprattutto per HALE/high-AR**, non per piccoli VTOL.
