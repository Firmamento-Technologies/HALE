# Aerodynamic Studies of Small Box-Wing Unmanned Aerial Vehicles

- **Venue:** Journal of Physics: Conference Series, Vol. 2235 (2022) 012070
- **URL / DOI:** https://iopscience.iop.org/article/10.1088/1742-6596/2235/1/012070/pdf — DOI 10.1088/1742-6596/2235/1/012070
- **Data accesso:** luglio 2026
- **Tipo evidenza:** numerico (CFD/aerodinamica low-Re su piccolo UAV box-wing pulito)

## Cosa supporta (claim del report 22)
- **Claim 2 (crossover indotta/attrito): CONFERMATO, con una PRECISAZIONE IMPORTANTE sul valore di crossover in Reynolds.**

## Estratti chiave
- "The box-wing design starts outperforming the mono-wing design **beyond a Reynolds number of approximately 4 × 10^5**, which is the point where the box-wing design's advantage in reducing induced drag outweighs the skin-friction drag increment from the wing surface."
- "The box-wing configuration exhibits **higher skin friction drag** than the mono-wing counterpart... attributed to the additional friction drag introduced by the winglets. This increased parasitic drag is due to the **greater wetted area** of the box-wing."
- "As cruise speed and Reynolds number increase, skin friction drag coefficient decreases... skin friction drag decreases in proportion to the fifth root of the Reynolds number." (→ a Re più alto l'attrito relativo cala e l'indotta pesa di più → il box guadagna).

## Rilevanza per BOXY C3 — nota critica
Il crossover documentato (**Re ≈ 4×10⁵**) coincide quasi esattamente con la crociera C3 calcolata nel report 22 (**Re ≈ 4.7×10⁵**). Questo rende il verdetto aerodinamico **genuinamente marginale e sensibile al CD0 dell'airframe**: per un UAV box-wing **pulito** (come quello di questo studio) il box può già pareggiare/vincere a quel Re; per un VTOL **sporco** (rotori esposti, CD0≈0.040 assunto nel report 22) il crossover si sposta a CL più alti e il mono resta avanti in crociera. Il discriminante è la pulizia aerodinamica, esattamente come sostiene il report 22.
