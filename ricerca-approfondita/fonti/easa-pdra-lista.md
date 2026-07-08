# EASA — Predefined Risk Assessment (PDRA): lista e ambiti

- **Titolo:** Predefined Risk Assessment (PDRA) — EASA + guide tecniche (Murzilli, avtrain, BAZL CH, AESA ES)
- **URL primari:**
  - EASA: https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-drones/predefined-risk-assessment-pdra
  - Murzilli: https://murzilliconsulting.com/news/predefined-risk-assessment-guide-pdra/
  - AESA (ES): https://www.seguridadaerea.gob.es/en/ambitos/drones/operaciones-uas-drones/operaciones-con-uas-drones---categoria-especifica
  - avtrain PDRA-G02: https://avtrain.aero/article/cm7xca79r0006nxdcher3wd8e/what-is-pdra-g02-all-you-need-to-know
  - BAZL (CH): https://www.bazl.admin.ch/en/pdra-en
  - AMC/GM Art.11 (mirror): https://www.transpordiamet.ee/sites/default/files/documents/2024-08/PDRA.pdf
- **Data accesso:** luglio 2026 (via WebSearch; WebFetch/curl bloccati origin+policy)

## Cosa supporta
Verifica quali PDRA coprono la CONSEGNA/CARGO BVLOS rurale (claim report 13 §3.4). Un PDRA è un AMC all'art. 11 Reg. (UE) 2019/947: EASA ha già svolto la SORA, quindi l'operatore evita la SORA piena e riduce l'onere autorizzativo.

## Estratto (verbatim/parafrasi dalle fonti)
Lista PDRA pubblicati (AESA/EASA):
- **PDRA-S01 / S02** — derivati dagli standard scenario nazionali; **S02**: "surveillance, agricultural works, and **short range cargo** operations".
- **PDRA-G01** — "surveillance and **long range cargo** operations". BVLOS su **area scarsamente popolata**, **spazio non controllato**, **≤150 m AGL**, UA con **dimensione caratteristica ≤3 m** ed energia cinetica **≤34 kJ**, in spazio **riservato/segregato** per l'operazione → **ARC-a**, entro il raggio del C2 diretto (radio line of sight). → tipicamente **SAIL II**.
- **PDRA-G02** — "BVLOS over a sparsely populated area within a **restricted or danger zone**"; operazioni consentite solo in spazio **riservato/segregato**; volume operativo interamente entro spazio riservato/segregato.
- **PDRA-G03** — "linear inspections and agricultural works".

## Rilevanza per Firmamento (consegna medicale Pentema)
- **CORREGGE report 13**: **esistono** PDRA rilevanti al cargo (PDRA-G01 long-range, PDRA-S02 short-range). Ma i vincoli PDRA-G01 (≤3 m, ≤150 m AGL, **spazio riservato/segregato ARC-a**, rotta su area **scarsamente popolata**) mal si conciliano con: (a) arrivo su borgo popolato, (b) necessità di spazio segregato in Appennino, (c) carico DG (UN3373) che resta **fuori scope PDRA/SORA**.
- **Verdetto:** PDRA-G01 è un candidato per la TRATTA rurale, ma NON risolve né il drop sul borgo né la merce pericolosa. Numero/edizione da confermare in pre-app ENAC (AMC1 Art.11).
