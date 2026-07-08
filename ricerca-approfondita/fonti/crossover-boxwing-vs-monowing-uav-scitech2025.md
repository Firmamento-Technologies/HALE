# Investigation of Flight Conditions where Box-Wing Outperforms Mono-Wing Configurations for Small UAVs

- **Autori:** (small-UAV box-wing study; preprint arXiv 2021, versione rivista AIAA SciTech Forum 2025)
- **Venue / URL / DOI:**
  - arXiv preprint: https://arxiv.org/abs/2112.02872 (arXiv:2112.02872)
  - AIAA SciTech Forum 2025, paper AIAA 2025-0256: https://arc.aiaa.org/doi/10.2514/6.2025-0256 (DOI 10.2514/6.2025-0256)
- **Data accesso:** luglio 2026
- **Tipo evidenza:** numerico, low-Reynolds VLM/CFD comparativo su piccoli UAV (teorico-computazionale, NON galleria/volo)

## Cosa supporta (claim del report 22)
- **Claim 2 (il guadagno svanisce in crociera attrito-dominata): CONFERMATO E RAFFORZATO.**
- **Claim 1 (riduzione indotta reale ma condizionata): supportato.**

## Estratti chiave
- "Box-wing configurations are advantageous when induced drag is higher than friction drag due to their ability to suppress the tip vortices... the box-wing produces a lower induced drag when compared to the monowing of the same aspect ratio, primarily due to the breaking of the large wing tip vortex from the monowing into two weak vortices in the box-wing."
- "The box-wing also exhibits a **higher total drag due to a higher parasitic drag** compared to the monowing at equal aspect ratio, which results in a **lower total L/D than the conventional design at a lower total lift**."
- "Although mono-wing configurations exhibit superior aerodynamic efficiency in certain regimes, box-wing designs perform better in circumstances like high velocities and increased lift demands."
- "Low aspect ratio box-wing configurations show improved gust tolerance and stability in longitudinal and lateral dynamics. In contrast, no substantial difference in flight dynamics is observed between box-wing and mono-wing designs for high aspect ratio configurations."

## Rilevanza per BOXY C3
Conferma la logica fisica del report 22: il box vince **solo** quando l'indotta supera l'attrito (alto CL / alto carico), e **perde in L/D totale** quando l'attrito domina e a basso CL. La penalità di superficie bagnata (paratie/winglet) è esplicitamente citata come causa del maggior drag parassita. Il vantaggio in dinamica/raffica è marginale e concentrato su config a **basso** AR.
