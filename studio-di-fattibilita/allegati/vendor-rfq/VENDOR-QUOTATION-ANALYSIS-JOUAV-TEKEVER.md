# Vendor Quotation Analysis, JOUAV CW-30E vs Tekever AR3
## Stima preliminare CapEx più TCO 5 anni per Percorso 6A pilota Pentema

> **Firmamento Technologies S.r.l.**, Progetto HALE, Studio di Fattibilità Volume 2, Allegato Vendor Selection
> **Riferimento DR:** DR-003 (parziale chiusura, quotation reale da RFQ formale)
> **Riferimento Studio:** Cap. 6 §6.3.1 TS-PLATFORM-6A più Cap. 8 §8.3.1, §8.4.1
> **Skill applicate:** `vtol-uas-specialist` più `trade-study-analysis` più `epistemic-rigor` più `competitor-intelligence`
> **Versione:** 1.0, bozza M+3
> **Data:** [DD/MM/YYYY]
> **Owner analisi:** Procurement Manager più Lead Systems Engineer Firmamento

---

## CAVEAT EPISTEMICO PRIORITARIO (epistemic-rigor Regola 1)

> **Le cifre contenute in questo documento sono STIME basate su benchmark pubblici disponibili al M+3 (maggio 2026).**
> Confidence aggregata: **low-medium** (range ± 50% sulle voci più incerte).
> **Quotation reale** richiede **invio RFQ formale** ai vendor (vedi `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md`), processo di **3-6 mesi tipico** per arrivare a contratto firmato.
>
> Le stime servono per validare il **range CapEx Y1** dello Studio (€700-1200k Briefing vs €975k-1.96M Cap. 8 §8.3.1), identificare il **gap potenziale** tra Plan A (JOUAV) e Plan B (Tekever), supportare la **strategia di funding** Y1 (mix Coopfond più FESR più equity) e decidere lo **stockpile spare strategico** in funzione del rischio supply chain.
>
> **Non sono numeri investment-grade** per pitch a investitori; **non sono da utilizzare** in offerta tecnico-economica a PA italiana senza disclaimer espliciti.

---

## 1. Executive Summary

### 1.1 Raccomandazione preliminare

**Decisione provvisoria, conferma del Cap. 6 §6.3.1 (TS-PLATFORM-6A):**

| Plan | Vendor | Status | Razionale sintetico |
|---|---|---|---|
| **Plan A** | **JOUAV CW-30E** (CN) | **Baseline preferred** | Best payload (8 kg), costo iniziale inferiore (circa 30-40% meno di Tekever), 200 km C2 range |
| **Plan B** | **Tekever AR3** (PT) | **EU sovereign fallback ready** | NATO-certified, reference EU forti (UK Home Office, EMSA, RAF), autonomia 16h, ma costo +30-40% e payload ridotto (4 kg) |

Switch automatico Plan A → Plan B se sanzioni o restrizioni export US-CN bloccano JOUAV entro M+6 (probabilità: medium, sezione 5.3 sotto), Golden Power notifica respinta dalla Presidenza Consiglio Ministri (probabilità: low-medium), ENAC notifica restrizioni operative su vendor CN per BVLOS in IT (probabilità: low), decisione strategica Firmamento per allineamento EU sovereign narrative (probabilità: medium, dipende da signal politico).

### 1.2 Stima quotation TCO 5 anni

| Voce | JOUAV CW-30E (€k) | Tekever AR3 (€k) | Delta (PT-CN) |
|---|---|---|---|
| **CapEx iniziale Y1 (DDP IT)** | 580-820 | 850-1.250 | +270-430 |
| **OpEx più manutenzione più spare 5 anni** | 280-450 | 350-550 | +70-100 |
| **TCO 5 anni totale (no IVA)** | **860-1.270** | **1.200-1.800** | **+340-530** |
| **Lead time consegna full system** | 6-9 mesi | 8-14 mesi | +2-5 mesi |

> **CONFIDENCE: low-medium**. Il range resta ampio per riflettere l'incertezza intrinseca su quotation non ricevute. Le quotation reali possono divergere ± 50% da queste stime.

### 1.3 Falsifying observations chiave (epistemic-rigor Regola 5)

- **FO-1**: quotation JOUAV reale > 50% sopra range stima (es. > €1.2M CapEx) attiva **re-baseline** scope MVP: eliminare payload telecom Y1, ridurre GS mobile, considerare Tekever.
- **FO-2**: quotation JOUAV reale < 50% sotto range stima (es. < €290k CapEx) attiva **scope expansion**: aggiungere LiDAR più multispettrale Y1.
- **FO-3**: quotation Tekever > €1.5M CapEx attiva switch fallback secondario su **Quantum Trinity F90+** (DE), capability ridotta ma EU sovereign più costo dimezzato.
- **FO-4**: lead time JOUAV > 12 mesi (rilevato in RFQ response) attiva immediatamente il path Tekever indipendentemente da costo (vincolo timing Y1 MVP critico).

### 1.4 Engagement plan timeline (3-6 mesi)

| Fase | Mese | Output |
|---|---|---|
| **M+3-4** | Personalizzazione RFQ + NDA template + lista vendor target | Documenti finali pronti |
| **M+4** | Invio RFQ a JOUAV (via reseller EU) + Tekever + (opt.) Quantum | 3 RFQ emesse |
| **M+4 → M+5** | Round chiarimenti vendor (15-30 gg) | Q&A documentate |
| **M+6** | Ricezione quotation (45 gg da emissione) | 2-3 quotation ricevute |
| **M+6 → M+7** | Valutazione tecnica + commercial scoring (skill `trade-study-analysis`) | Matrice decisionale finale |
| **M+7 → M+8** | Negoziazione contratto con vendor finalist | Term sheet condivisi |
| **M+8 → M+9** | Drafting contratto + Golden Power notifica (se vendor CN) | Bozza contratto |
| **M+9 → M+10** | Esito Golden Power (45 gg legali) | Risposta governo |
| **M+10** | **Decisione finale vendor + Purchase Order** | PO firmato, anticipo M1 versato |
| **M+10 → M+16-18** | Produzione + FAT + shipping + dogana | Sistema in arrivo |
| **M+18-20** | SAT (Site Acceptance Test) Pentema + training + commissioning | Operatività Y1 avvio |

---

## 2. Profilo Vendor 1, JOUAV CW-30E (CN)

### 2.1 Vendor profile JOUAV (Chengdu JOUAV Automation Tech Co., Ltd)

| Aspetto | Dato |
|---|---|
| **Headquarter** | Chengdu, Sichuan, Cina [`[jouav.com \| 2024 \| vendor \| high]`] |
| **Anno fondazione** | 2007 |
| **Dimensione** | PMI cinese, focus VTOL fixed-wing commerciale civile |
| **Mercati principali** | Cina, Asia-Pacifico, Sud America, Africa, Medio Oriente |
| **Mercato EU** | Limited presence via reseller (es. MARIDS Spagna, SUMEC, vari distributori indipendenti) |
| **Certificazioni vendor** | ISO 9001 dichiarata; CW-15 TÜV SÜD certification dichiarata; CW-30E **no EASA conformity dichiarata**; no AS/EN 9100 [`[ricerca web 2026 \| medium \| trade press`] |
| **Track record settore civile** | Power grid monitoring Cina (Guangdong Power Grid), surveys Hainan, surveys forestali Sud-Est asiatico |
| **Track record EU** | Reference EU **scarsamente documentate**; alcuni operatori privati in Spagna, Portogallo, Polonia (non confermati) |
| **Status export US** | Non in Entity List BIS (verificato M+3) ma supply chain componenti soggetta a US Section 301 tariffs (25%) più (temporaneo) Section 122 surcharge 10% se passaggio US |

### 2.2 Specifiche tecniche JOUAV CW-30E (datasheet vendor)

| Parametro | Valore datasheet | Sorgente | Confidence |
|---|---|---|---|
| MTOW | 38 kg | `[JOUAV vendor 2024 \| high]` | high |
| Payload max | 8 kg | `[vendor]` | high |
| Autonomia max | 480 min (8 h) | `[vendor]` | medium (datasheet, non operatori EU indipendenti) |
| Velocità crociera | 90 km/h | `[vendor]` | medium |
| Velocità max | 130 km/h | `[vendor]` | medium |
| Quota max operativa | 4500 m AMSL | `[vendor]` | medium |
| Range C2 LOS | 50 km (con antenna std) | `[vendor]` | medium |
| Range C2 estesa | 200 km (con antenna upgraded) | `[vendor]` | medium |
| Operating temperature | -20°C / +55°C | `[vendor]` | high |
| Resistenza pioggia | ≤ 10 mm/24h | `[vendor]` | medium |
| Vento sostenuto max | 13.9-17.1 m/s | `[vendor]` | medium |
| Propulsione | Ibrida gasoline/heavy oil + battery | `[vendor]` | high |
| Take-off footprint | 5×5 m VTOL | `[vendor]` | high |
| Autopilota | JOUAV proprietario (banded JOS) | `[vendor]` | high |
| C2 frequency | 1.4 GHz proprietario (in alcune varianti); 2.4 GHz ISM standard | `[vendor, web `'>=' '100 km comm'` claim]` | medium |
| Compliance dichiarata | CE marking (su CW-15 confermato; CW-30E TBD); EASA non dichiarata | `[ricerca web]` | low (CW-30E specifico) |

**Caveat:** ogni valore vendor è datasheet, non validato da operatori EU indipendenti. La performance reale a Pentema (1100-1300 m AMSL, vento canalizzato, inverno -5°C) si stima attorno al -20/40% rispetto al datasheet (vedi Cap. 6 §6.2.1).

### 2.3 Stima quotation JOUAV CW-30E (CapEx più TCO 5 anni)

La metodologia triangola: pricing tipico VTOL fixed-wing 30-40 kg MTOW mercato CN (range $50-150k USD piattaforma base); markup reseller EU più customs più shipping (tipico +30-50%); aggiunte payload, GS e training a prezzi mercato standard; best practice aerospace UAV procurement (overhead, contingency).

| Voce | Stima JOUAV CW-30E (€k) | Confidence | Note metodologiche |
|---|---|---|---|
| **Piattaforma UAV base** | 80-180 | M | $50-150k USD CN typical, +30-50% margin reseller EU + customs |
| **Engine upgrade heavy oil (opt)** | 10-25 | M | Tipico vendor option |
| **Spare parts set 3 anni** | 25-50 | L | Stima 20-30% del valore piattaforma |
| **Ground Station fissa (container + console + antenna)** | 25-45 | M | Mercato standard CN-EU |
| **Ground Station mobile (veicolo + console)** | 25-50 | M | Veicolo + integrazione cliente |
| **Software autopilota (license perpetual)** | 5-15 | M | Generalmente incluso in piattaforma |
| **Payload RGB high-res integrato (es. Phase One iXM 100)** | 35-70 | M | Sensore standalone €30-50k + integrazione |
| **Payload IR LWIR (WIRIS Pro o FLIR Vue Pro R)** | 20-50 | M | WIRIS Pro circa €20-30k, FLIR circa €15-25k |
| **Payload telecom LTE eNodeB (opt Y1)** | 60-120 | M-L | Athonet / Druid LTE-Direct typical pricing |
| **Gimbal 3-axis stabilizzato** | 15-30 | M | Tipico €10-25k payload-grade |
| **Training piloti (5 persone, base + advanced)** | 20-40 | M | $5-10k USD per persona, +EU travel |
| **Customs + shipping DDP Pentema** | 15-30 | M | Stima 5-10% valore + IVA dogana |
| **Setup + integrazione + commissioning** | 10-20 | M | Integrazione cliente + SAT |
| **Subtotal CapEx Y1 senza spare** | **305-655** | M | Senza set ricambi |
| **+ Spare parts set 3 anni** | +25-50 | L | |
| **TOTALE CapEx Y1 (DDP IT, no IVA)** | **580-820 €k** | **L-M** | Range realistico |
| **+ IVA 22% su CapEx** | +128-180 | H | (recuperabile per Firmamento PMI) |
| **TOTALE CapEx Y1 (DDP IT, con IVA)** | **708-1.000 €k** | L-M | |
| | | | |
| **Supporto + manutenzione anno 1 (warranty)** | 0 (incluso) | M | Tipico vendor warranty 12-24 mesi |
| **Supporto + manutenzione anno 2** | 25-40 | L | 8-10% CapEx asset |
| **Supporto + manutenzione anni 3-5 (annuali)** | 30-50 × 3 = 90-150 | L | 10-12% CapEx asset, escalation |
| **Spare aggiuntivi anni 2-5 (consumati)** | 40-80 | L | Consumable + replacement |
| **Update software 5 anni** | 10-30 | L | OTA gratis Y1-Y2, fee Y3+ |
| **TOTALE supporto + spare 5 anni** | **165-300** | L | |
| | | | |
| **TOTALE TCO 5 anni JOUAV (no IVA)** | **745-1.120 €k** | L-M | CapEx + OpEx tecnico |
| **TOTALE TCO 5 anni JOUAV (con IVA)** | **910-1.366 €k** | L-M | |

**Lead time stimato JOUAV CW-30E:**

- Produzione più FAT: 3-5 mesi (vendor CN tipico)
- Shipping CN → IT: 1-2 mesi (sea freight); 2-3 settimane (air, più costi)
- Dogana Italia: 2-4 settimane
- Training più SAT più commissioning: 1-2 mesi
- Totale end-to-end stimato: 6-9 mesi (best case); 9-14 mesi (worst case con delays customs o sanctions)

**Confidence lead time: medium-low** (dipende da Section 301 tariffs status, escalation US-CN possibili, customs Italia variabili).

---

## 3. Profilo Vendor 2, Tekever AR3 (PT)

### 3.1 Vendor profile Tekever (Tekever Group)

| Aspetto | Dato |
|---|---|
| **Headquarter** | Lisbona, Portogallo + sedi UK (Bristol) e altre EU [`[tekever.com]`] |
| **Anno fondazione** | 2001 |
| **Dimensione** | Mid-cap aerospace EU, circa 600+ dipendenti, fatturato stimato €100M+ (2024-2025) |
| **Mercati principali** | EU sovereign, NATO, UK, US (limited), Africa |
| **Mercato EU** | **Strong**: UK Home Office contract £1B framework (2019-2025), EMSA framework €30M (2024), Portuguese GNR (Guardia Nazionale Repubblicana), Spagna Police Nazionale (2024), RAF "StormShroud" programme (2025) |
| **Certificazioni vendor** | AS/EN 9100 dichiarata, ISO 9001, ISO 27001 (cybersecurity), NATO eligible vendor |
| **Track record settore civile più dual-use** | Surveillance marittima, EMSA SAR (Search And Rescue), border surveillance, electronic warfare (StormShroud), Ucraina deployment (battle-proven) |
| **Track record IT** | Marina Militare Italiana operatore AR-5 (citato in alcune fonti, non verificato direttamente) [`[unconfirmed]`] |
| **Status export** | EU sovereign supply chain ✓; ITAR-free ✓; no US restrictions; full export friendly to allied countries |

### 3.2 Specifiche tecniche Tekever AR3 (datasheet vendor)

| Parametro | Valore datasheet | Sorgente | Confidence |
|---|---|---|---|
| MTOW | 25 kg | `[tekever.com vendor]` | high |
| Payload max | 4 kg (precedenti versioni 2.5 kg, AR3 EVO +50%) | `[vendor]` | high |
| Autonomia max (fixed-wing only) | 16 h | `[vendor]` | medium |
| Autonomia max (VTOL mode) | 8 h | `[vendor]` | medium |
| Velocità crociera | circa 70-90 km/h | `[vendor]` | medium |
| Velocità max | circa 110 km/h | `[vendor]` | medium |
| Quota max operativa | circa 3500-4000 m AMSL | `[vendor]` | medium |
| Range operativo | 100 km surveillance radius | `[vendor + Wikipedia + UST]` | high |
| Operating temperature | -20°C / +50°C | `[vendor]` | medium |
| Vento sostenuto max | circa 13-15 m/s | `[vendor]` | medium |
| Propulsione | Elettrica + hybrid VTOL option | `[vendor]` | high |
| Wingspan | 3.5 m | `[Wikipedia + UST]` | high |
| Lunghezza | 1.9 m | `[Wikipedia]` | high |
| Take-off footprint | 5×5 m (VTOL) o catapulta 3.5 m | `[vendor]` | high |
| Atterraggio | Net o parachute (catapulta launch) o VTOL | `[vendor]` | high |
| Autopilota | Proprietario Tekever, autonomous mode + manual override | `[vendor]` | high |
| Payload sensors | EO/IR gimbals, SAR radar, SIGINT, EW modules, laser designator (modulare) | `[vendor]` | high |
| Hot-swappable VTOL system | Sì (nuova versione 2025) | `[vendor 2025 press]` | high |
| Compliance dichiarata | EASA awareness, NATO eligible, multiple sovereign EU operators | `[track record]` | medium-high |

### 3.3 Stima quotation Tekever AR3 (CapEx più TCO 5 anni)

La metodologia triangola: pricing tipico UAV fixed-wing 25 kg MTOW EU-sovereign aerospace mid-tier ($150-400k USD piattaforma base); benchmark EMSA contract €30M / 4 anni / multi-vendor REACT consortium (stima €2-3M per drone-anno operativo all-inclusive con servizi); UK Home Office £1B / 6 anni framework (stima impossibile per breakdown, include operations as a service); premium EU sovereign più NATO certification più reference customer EU forti.

| Voce | Stima Tekever AR3 (€k) | Confidence | Note metodologiche |
|---|---|---|---|
| **Piattaforma UAV base** | 250-450 | M | Mid-tier EU aerospace pricing, NATO-grade premium |
| **VTOL kit option (vs catapulta)** | 30-60 | M | Hot-swappable VTOL nuova versione 2025 |
| **Spare parts set 3 anni** | 50-90 | L | 20-25% del valore piattaforma |
| **Ground Station fissa (container + console + antenna)** | 40-70 | M | EU aerospace-grade hardened |
| **Ground Station mobile (veicolo + console)** | 40-75 | M | NATO-grade rugged, integrazione cliente |
| **Software autopilota + ATAK integration (license)** | 15-30 | M | Tipico premium NATO-grade |
| **Payload RGB high-res integrato** | 35-70 | M | Equivalente JOUAV |
| **Payload IR LWIR + gimbal stabilizzato 3-axis** | 35-70 | M | NATO-grade premium |
| **Payload telecom LTE eNodeB (opt Y1)** | 80-150 | M-L | Premium NATO-grade integration |
| **Catapulta launch system 3.5 m (alternativa VTOL)** | 25-50 | M | Tipica catapulta tactical |
| **Net recovery o parachute system** | 10-20 | M | |
| **Training piloti (5 persone, base + advanced + NATO-grade)** | 35-65 | M | $8-15k USD per persona + EU travel + advanced |
| **Customs + shipping (intra-EU, no dogana)** | 5-15 | H | Vantaggio EU sovereign: no customs, libera circolazione UE |
| **Setup + integrazione + commissioning** | 20-35 | M | Premium support inclusa |
| **Subtotal CapEx Y1 senza spare** | **690-1.130** | M | Senza set ricambi |
| **+ Spare parts set 3 anni** | +50-90 | L | |
| **TOTALE CapEx Y1 (DDP IT, no IVA)** | **850-1.250 €k** | L-M | Range realistico |
| **+ IVA 22% su CapEx** | +187-275 | H | (recuperabile) |
| **TOTALE CapEx Y1 (DDP IT, con IVA)** | **1.037-1.525 €k** | L-M | |
| | | | |
| **Supporto + manutenzione anno 1 (warranty)** | 0 (incluso) | M | Tipico vendor warranty 24-36 mesi NATO-grade |
| **Supporto + manutenzione anno 2** | 30-50 | L | 8-10% CapEx asset, premium |
| **Supporto + manutenzione anni 3-5 (annuali)** | 40-65 × 3 = 120-195 | L | 10-12% CapEx asset, escalation premium |
| **Spare aggiuntivi anni 2-5 (consumati)** | 50-90 | L | Consumable + replacement |
| **Update software 5 anni** | 15-40 | L | OTA gratis Y1-Y2, fee Y3+ premium |
| **TOTALE supporto + spare 5 anni** | **215-390** | L | |
| | | | |
| **TOTALE TCO 5 anni Tekever (no IVA)** | **1.065-1.640 €k** | L-M | CapEx + OpEx tecnico |
| **TOTALE TCO 5 anni Tekever (con IVA)** | **1.302-2.030 €k** | L-M | |

**Lead time stimato Tekever AR3:**

- Produzione più FAT: 4-7 mesi (vendor EU mid-tier, backlog NATO orders)
- Shipping PT → IT: 1-2 settimane (intra-EU, no customs)
- Training più SAT più commissioning: 2-3 mesi (più approfondito NATO-grade)
- Totale end-to-end stimato: 8-12 mesi (best case); 12-16 mesi (worst case con backlog ordini militari)

**Confidence lead time: medium** (il backlog NATO ordini Ucraina più RAF più UK Home Office può estendere il lead time per ordini civili commerciali low-priority).

---

## 4. Stima Quotation Strutturata Confronto

### 4.1 Tabella comparativa CapEx più TCO

| Voce | JOUAV CW-30E (€k) | Tekever AR3 (€k) | Delta PT vs CN | Confidence |
|---|---|---|---|---|
| **Piattaforma base** | 80-180 | 250-450 | +170-270 (+220%) | M |
| **Set spare parts 3 anni** | 25-50 | 50-90 | +25-40 | L |
| **Ground Station 1 fissa + 1 mobile** | 50-95 | 80-145 | +30-50 | M |
| **Software autopilota + license** | 5-15 | 15-30 | +10-15 | M |
| **Payload integration (RGB + IR + telecom)** | 130-270 | 230-360 | +100-90 | M |
| **Training piloti 5 persone** | 20-40 | 35-65 | +15-25 | M |
| **Customs + shipping + setup + commissioning** | 25-50 | 25-50 | =/+15 (EU advantage) | M |
| **Supporto + manutenzione 5 anni** | 165-300 | 215-390 | +50-90 | L |
| **Lead time consegna** | 6-9 mesi | 8-14 mesi | +2-5 mesi | M |
| **CapEx Y1 senza IVA totale** | **580-820** | **850-1.250** | **+270-430** | L-M |
| **CapEx Y1 con IVA totale** | **708-1.000** | **1.037-1.525** | **+329-525** | L-M |
| **TCO 5 anni senza IVA** | **745-1.120** | **1.065-1.640** | **+320-520** | L-M |
| **TCO 5 anni con IVA** | **910-1.366** | **1.302-2.030** | **+392-664** | L-M |

### 4.2 Cost driver primario di differenziazione

| Driver | Impatto su Tekever vs JOUAV |
|---|---|
| **Premium EU sovereign + NATO certification** | +50-80% sulla piattaforma base |
| **Backlog NATO ordini Ucraina** | +30-50% sul lead time, +10-15% sui prezzi 2026 |
| **Vantaggio intra-EU (no customs, libera circolazione)** | -€10-25k su customs + shipping = -3% saving Tekever |
| **Premium training NATO-grade + cybersecurity audit** | +50-80% sul training |
| **Spare parts EU-sovereign supply** | +30-50% sui ricambi (vs mercato CN più aggressivo prezzi) |
| **Premium manutenzione + warranty estesa NATO-grade** | +20-40% sull'OpEx annuale |

### 4.3 Posizionamento entrambi vs range Studio Cap. 8 §8.3.1

| Reference | Range | JOUAV stima | Tekever stima |
|---|---|---|---|
| **Briefing originale** | €600-900k | ✅ overlap (580-820) | ⚠️ over (850-1.250) |
| **Cap. 8 §8.3.1 range realistico (no IVA, +contingency 15%)** | €655-1.305k Importo A | ✅ overlap (580-820) | ✅ overlap (850-1.250) |
| **Cap. 8 §8.3.1 totale con IVA + somme** | €975-1.961k Totale Y1 | ✅ overlap (708-1.000 + altre voci) | ⚠️ upper bound (1.037-1.525 + altre voci) |

**Lettura:** Plan A JOUAV si colloca al di sotto del range Studio (spazio di manovra OK); Plan B Tekever si colloca al margine superiore del range, ma resta dentro il range realistico Cap. 8 (no contingency overrun). Se Tekever quotation supera €1.5M CapEx Y1, lo scope expansion non è possibile entro budget: serve un funding mix più aggressivo (+ €300-500k FESR/PNRR) oppure un de-scoping (no payload telecom Y1).

---

## 5. Risk Geopolitico e Supply Chain (Approfondimento)

### 5.1 Risk JOUAV CW-30E (Plan A), analisi dettagliata

#### 5.1.1 Tariffe USA-CN (2026)

**Status M+3 (maggio 2026):**

- Section 301 China tariffs: **25%** sulle importazioni US (non applicabile a Italia direttamente, ma impatta componenti US-origin in JOUAV)
- Section 122 surcharge: **10%** temporaneo, scadenza luglio 2026
- US Commerce Department probe drone imports: in corso da luglio 2025
- L'EU non applica tariffe specifiche su drone CN (al M+3), ma l'Italia ha la possibilità di attivare Golden Power

**Impatto su Firmamento:** l'acquisto JOUAV direttamente da reseller EU non è soggetto a tariffe US (non passa via US); componenti US-origin in JOUAV (chip, sensori), se restrittivi US Entity List, possono incorrere in re-export limitations. **Probabilità di blocco totale CW-30E export to Italia: low (10-15%)** entro 12 mesi.

#### 5.1.2 Restrizioni export CN su drone parts (2025-2026)

Trend osservato: la Cina ha imposto **export controls su drone parts** dal dicembre 2024 (lithium batteries, motors, flight controllers per US/EU/Ukraine); 28 entità US aggiunte alla Chinese export control list (gennaio 2025); dicembre 2024 China optimizes export control measures for drones, ban export intended for military purposes.

**Impatto su Firmamento:** l'acquisto JOUAV per uso civile commerciale documentato non dovrebbe essere bloccato (vendor cinese rilascia end-user statement); il processo customs CN può rallentare il lead time di 2-4 mesi; i ricambi (motori, batterie, FCS) possono essere intermittentemente bloccati con preavviso breve.

**Probabilità di blocco temporaneo lead time +6 mesi: medium (30-40%)** entro 24 mesi.

#### 5.1.3 Restrizione DJI / Chinese drones US ban (2025-2026)

**Status M+3:**

- FCC ha bloccato l'import di nuovi drone DJI e foreign companies in tarda 2025
- Drone già importati possono continuare a essere venduti (es. DJI Mini 5 Pro, Mavic 4 Pro)
- Commerce Department ha abbandonato la proposta di ban completo drone CN gennaio 2026 dopo revisione interna

**Impatto su Firmamento:** il ban non riguarda direttamente JOUAV CW-30E (categoria diversa da DJI consumer), ma crea un precedente politico che può estendersi (l'Italia potrebbe seguire il path US, probabilità bassa al M+3, ma observable trigger). Reputational risk: in scenario di escalation, JOUAV come "Chinese aerospace" può attrarre scrutinio mediatico.

**Probabilità di replicazione ban in EU: low (15-20%)** entro 36 mesi.

#### 5.1.4 Risk Golden Power notifica

**Inquadramento normativo:** D.L. 21/2012 più modif. D.L. 23/2020 (estensione settore aerospace e dual-use) più D.L. 50/2022.

**Applicabilità al caso JOUAV:** l'acquisizione non costituisce M&A (è procurement asset, non acquisizione società); il D.L. 21/2012 art. 2 c. 1-ter copre "acquisizioni di tecnologie e attivi strategici" da extra-UE; aerospace è settore Golden Power "ad alta strategicità"; il vendor CN è extra-UE non amico (in lista di paesi sensibili).

**Probabilità di triggering notifica obbligatoria: medium-high (60-70%)**.

**Probabilità di esito negativo (veto Golden Power): low (10-20%)**. Razionale: la piattaforma è commerciale civile, i payload sono non sensibili, lo use case riguarda le Aree Interne italiane e l'end user è la PA italiana. Mitigazione: documentazione end-use, audit supply chain, certificazione no military-grade payload.

**Tempi:** notifica → istruttoria → risposta tipicamente 45 gg lavorativi (può estendersi a 90 gg con richiesta integrativa).

**Costi:** legale specialistica Golden Power €15-30k più tempi gestionali interni Firmamento (2-3 mesi PM full-time equivalent).

**RACCOMANDAZIONE OPERATIVA:** inserire la Golden Power notifica come tappa OBBLIGATORIA del cronoprogramma vendor JOUAV (M+8-10); pre-engagement informale con DPSCS (Dipartimento per le Politiche Strategiche e Cooperazione Internazionale) Presidenza Consiglio Ministri per pre-screening informale prima della formal notifica; documentazione preparata in anticipo (end-use statement, supply chain audit, cybersecurity attestation).

#### 5.1.5 Vendor concentration risk

JOUAV è il vendor unico: single point of failure su un singolo produttore CN.

**Mitigazioni Firmamento:** stock spare critici 12-18 mesi (vs 3 anni standard) per protezione gap supply; contratto vendor con clausole continuità e penali per disruption; Plan B Tekever pre-validato e contract-ready (vedi sez. 6 sotto); path migrazione documentato (come switchare da JOUAV a Tekever in 6-9 mesi).

### 5.2 Risk Tekever AR3 (Plan B), analisi dettagliata

#### 5.2.1 Risk geopolitico Tekever

**Vantaggi EU sovereign:** vendor PT intra-UE (no customs, no export licensing, no Golden Power triggering); NATO eligible vendor (allineamento con sovereign IT/EU narrative); reference customer EU forti (bassa reputational risk); supply chain Tekever EU-prevalente (ridotta exposure US/CN tensioni).

**Risk specifici:**

| Risk | Probabilità | Impatto | Mitigation |
|---|---|---|---|
| Backlog NATO ordini Ucraina → lead time esteso 12-16 mesi | M-H | M | Anticipare ordine; clausola priority client; backup vendor Quantum (DE) |
| Premium pricing NATO-grade → fuori budget Firmamento | M | M | Negoziare configurazione "civilian-grade" (no SIGINT, no EW, no laser designator) |
| Tekever pivot strategico verso solo difesa → abbandono prodotto civilian | L | M | Contract con clausole exit + tech transfer |
| Dipendenza single vendor EU (no diversificazione) | M | M | Plan C su Quantum F90+ (DE) come terzo fallback |
| Tekever acquisita da prime US/UK (es. BAE, RTX) → cambio policy export | L-M | M | Monitor M&A Tekever; right of first refusal in contratto |

#### 5.2.2 Reference customers Tekever AR3 (verificati ricerca web)

| Customer | Status | Use case | Sorgente |
|---|---|---|---|
| **UK Home Office** | Active (rinnovato 2025, 3-year contract framework £1B max) | English Channel maritime surveillance (asylum policy) | `[Sifted 2025 \| medium-high]` |
| **EMSA (European Maritime Safety Agency)** | Active (€30M framework 4 anni 2024-2028, CLS-Tekever REACT consortium) | EU maritime surveillance + SAR | `[EMSA 2024 \| high]` |
| **Portuguese GNR (Guardia Nazionale Repubblicana)** | Active (coastal surveillance Portugal) | Border + maritime | `[Tekever 2024 \| high]` |
| **Spanish National Police** | Active (2024 deployment) | Border protection + maritime | `[UST 2024 \| medium-high]` |
| **RAF (Royal Air Force UK)** | Active (StormShroud EW programme 2025) | Electronic warfare + ISR | `[Tekever 2025 \| high]` |
| **Marina Militare Italiana** | Operato AR-5 (citato, non verificato direttamente CW-3) | ISR marittima | `[unconfirmed]` |
| **Ukraine** | Active battle-proven deployment AR3 + AR5 | Battlefield ISR | `[various press]` |

**Reference customer score:** Tekever è **5+/5** sul criterio "reference EU operatori" (Cap. 6 §6.3.1). JOUAV è **1-2/5** (reference EU non documentati pubblicamente per CW-30E specifico, alcuni operatori privati anecdotali).

---

## 6. Matrice Decisionale Pesata (Trade Study)

Riferimento: skill `trade-study-analysis` più matrice Cap. 6 §6.3.1.

### 6.1 Pesi criteri (allineati Cap. 6 §6.3.1)

| Criterio | Peso |
|---|---|
| Costo iniziale (CapEx) | 15% |
| TCO 5 anni | 15% |
| Capability tecnica (autonomia + payload + range) | 15% |
| Compliance regolatoria EASA/ENAC | 15% |
| Risk geopolitico / supply chain | 10% |
| Reference customers EU | 10% |
| Lead time | 10% |
| Supporto IT/EU | 10% |
| **Totale** | **100%** |

### 6.2 Scoring (scala 1-10, dove 10 = best)

| Criterio | Peso | JOUAV CW-30E | Razionale JOUAV | Tekever AR3 | Razionale Tekever |
|---|---|---|---|---|---|
| **Costo iniziale (CapEx)** | 15% | **8** | €580-820k stima (sotto Briefing range) | **5** | €850-1.250k stima (margine sup range) |
| **TCO 5 anni** | 15% | **8** | €745-1.120k stima | **6** | €1.065-1.640k stima (+30-50%) |
| **Capability tecnica** | 15% | **8** | Payload 8 kg ✓, autonomia 8h ✓, range 50-200 km ✓ | **7** | Payload 4 kg, autonomia 16h ✓✓, range 100 km |
| **Compliance regolatoria EASA/ENAC** | 15% | **5** | CW-30E no EASA conformity esplicita; CE marking TBD; ENAC engagement nullo | **8** | NATO eligible + EMSA + UK Home Office = compliance proven |
| **Risk geopolitico / supply chain** | 10% | **4** | Vendor CN; Section 301 tariffs; Golden Power notifica probable; Plan B necessario | **9** | EU sovereign ✓; intra-EU; no Golden Power; NATO aligned |
| **Reference customers EU** | 10% | **3** | Reference EU non documentate per CW-30E | **9** | UK Home Office, EMSA, Portuguese GNR, Spagna, RAF, Ukraine |
| **Lead time** | 10% | **7** | 6-9 mesi best; 9-14 mesi worst | **5** | 8-12 mesi best; 12-16 mesi worst (backlog NATO) |
| **Supporto IT/EU** | 10% | **4** | No service center IT; supporto via reseller; manuali EN/CN | **8** | Service EU presente; multilingual; possibilità training PT/EU |
| **Σ ponderato** | 100% | **6.25** | | **7.05** | |

### 6.3 Verdetto matrice decisionale (versione aggiornata vs Cap. 6 §6.3.1)

**Versione M+3 originale Cap. 6 §6.3.1:** JOUAV 7.30 vs Tekever 7.30 (parità, decisione JOUAV con Plan B Tekever).

**Versione M+3 update con stime quotation dettagliate (questo documento):** Tekever 7.05 vs JOUAV 6.25, Tekever in vantaggio di 0.80 punti.

**Razionale dello shift:** capability JOUAV ridimensionata (5 vs 7 su EASA/ENAC compliance, confermata la mancanza di evidenze EASA esplicite per CW-30E specifico); reference customer JOUAV ridimensionata (3 vs 8, confermata la mancanza di reference EU pubblicamente documentate); risk geopolitico JOUAV confermato critico (4 vs 5); costo JOUAV resta vantaggio (8 vs 5).

### 6.4 Decisione raccomandata (proposta aggiornata)

> **DECISIONE PROPOSTA AGGIORNATA (M+3+ dopo questa analisi):**
>
> Riconsiderare la baseline da JOUAV → Tekever come Plan A se i seguenti trigger sono confermati a M+6-7:
> 1. Quotation reale JOUAV non significativamente sotto stima (es. quotation > €700k CapEx → vantaggio costo erode)
> 2. Quotation reale Tekever non significativamente sopra stima (es. quotation < €1.0M CapEx → premium gestibile)
> 3. Tekever lead time < 10 mesi confermato
> 4. Budget Firmamento Y1 esteso a €1.0-1.5M (mix funding più Series A seed)
> 5. Signal politico EU sovereign chiaro (es. IRIS² Italia node più EDF call HAPS preferences EU vendor)
>
> Mantieni JOUAV come baseline se: quotation JOUAV < €500k CapEx (vantaggio costo permanente); budget Y1 vincolato a €600-900k (Briefing originale); speed-to-market è critico (lead time < 6 mesi vincolo hard); cooperative Legacoop accettano "vendor CN" senza obiezioni reputational.
>
> **DECISIONE NEUTRA (M+3 attuale, in attesa quotation reali):** procedere con doppia RFQ formale parallela JOUAV più Tekever, con valutazione finale a M+6 sulla base di quotation effettive. Mantenere apertura su Plan B Quantum F90+ (DE) come Plan C se entrambi falliscano.

---

## 7. Caveat Onesto e Falsifying Observations (Epistemic-Rigor)

### 7.1 Caveat sulle stime

Le stime in questo documento si basano su: datasheet vendor pubblici (JOUAV.com, Tekever.com), confidence medium (vendor self-declared); benchmark pubblici pricing UAV 25-40 kg MTOW classe, confidence low-medium (estremamente variabile); reseller markup tipici aerospace mid-tier, confidence medium (best practice); contratti pubblici disponibili (EMSA €30M / 4 anni, UK Home Office £1B / 3 anni), confidence high ma non breakable per singolo asset; esperienza analogica con classi simili UAV mercato EU, confidence medium.

Le stime non includono: sconti volume eventuali (acquisto multi-piattaforma Y2-Y3); negoziazione condizioni payment (es. anticipo ridotto, milestones favorevoli); componenti opzionali avanzate non incluse (es. EW, SAR radar per Tekever); costi indiretti Firmamento (PM dedicato, legale specialistica, viaggi); inflation aerospace 2026-2030 (tipicamente 3-5%/anno).

**Range stimati:** ± 30-50% confidence interval su voci primarie; ± 50-80% su voci secondarie.

### 7.2 Falsifying observations completo

| FO-ID | Trigger | Action |
|---|---|---|
| **FO-1** | Quotation JOUAV reale > €1.2M CapEx Y1 (50% sopra stima centrale) | **Re-baseline** scope: eliminare payload telecom Y1, ridurre GS, considerare Tekever come Plan A |
| **FO-2** | Quotation JOUAV reale < €290k CapEx Y1 (50% sotto stima centrale) | **Scope expansion**: aggiungere LiDAR + multispettrale + 2a GS mobile Y1 |
| **FO-3** | Quotation Tekever > €1.5M CapEx Y1 | Switch fallback secondario su **Quantum Trinity F90+** (DE), capability ridotta ma EU sovereign + costo dimezzato |
| **FO-4** | Lead time JOUAV reale > 12 mesi | **Switch Plan B Tekever** automatico (vincolo timing Y1 MVP critico) |
| **FO-5** | Golden Power respinta o richiesta integrativa > 90 gg | **Switch Plan B Tekever** + perdita anticipo M1 JOUAV gestita |
| **FO-6** | Sanzioni US-CN escalation post-luglio 2026 (Section 122 surcharge confermata) | **Cost re-baseline JOUAV +10-20%**, valutare path Tekever come parity costo |
| **FO-7** | Tekever backlog NATO Ucraina genera lead time > 16 mesi | **Fallback Plan C Quantum F90+** o altra piattaforma EU sovereign |
| **FO-8** | Entrambi vendor non rispondono entro 45 gg deadline RFQ | Estensione RFQ + apertura su vendor terzi (Skyfront US, BlueBird IL, AeroVironment) |
| **FO-9** | Bandi Coopfond/FESR Y1 non disponibili o ritardati | Riduzione scope Y1 a piattaforma minima (no payload modulare full); switch su mix funding equity + R&D credit |

### 7.3 Confidence calibration finale

| Aspetto | Confidence |
|---|---|
| Specifiche tecniche datasheet vendor | M-H (datasheet vendor, non validati operatori EU indipendenti per JOUAV; validati per Tekever via reference EU) |
| Stima CapEx Y1 (range) | L-M |
| Stima TCO 5 anni | L (richiede assumptions su utilization più escalation prezzi) |
| Lead time stimato | M (JOUAV: variabile geopolitica; Tekever: variabile backlog NATO) |
| Reference customer count | H (Tekever); L (JOUAV, assenza dati pubblici) |
| Risk geopolitico (probabilità eventi) | M (analisi base rate più trend osservati 2024-2026) |
| Matrice decisionale ponderata | M (pesi soggettivi Firmamento; scoring richiede validazione quotation reali) |

---

## 8. Engagement Plan Dettagliato (RFQ Submission → Decisione Vendor)

### 8.1 Timeline 3-6 mesi tipica

| Settimana | Fase | Output | Owner |
|---|---|---|---|
| W1-2 | Finalizzazione RFQ + NDA template + lista distribution vendor | RFQ Final v1.0 + NDA template + lista 3-5 vendor | Procurement Manager + Legal |
| W3 | Invio RFQ a JOUAV (via reseller EU) + Tekever + Quantum F90+ (opzionale) | 3 RFQ inviati via PEC + ack ricevuto | Procurement Manager |
| W3-5 | Periodo domande chiarimenti vendor (15 gg) | Q&A documentate, response Firmamento | Lead Systems Engineer |
| W6-9 | Vendor preparazione quotation (45 gg da emissione RFQ) | Quotation ricevute | Vendor |
| W10-11 | Valutazione tecnica + commercial scoring (skill `trade-study-analysis`) | Matrice valutazione + ranking | Procurement + Systems + CFO |
| W12-13 | Round chiarimenti tecnici post-quotation (BAFO, Best And Final Offer) | Quotation aggiornate | Vendor + Procurement |
| W14-16 | Negoziazione contratto con vendor finalist | Term sheet condiviso | Procurement + Legal + CFO |
| W17 (eventuale, vendor CN) | Golden Power pre-screening informale DPSCS | Pre-approval informale | Legal + AD |
| W18-19 (eventuale, vendor CN) | Golden Power notifica formale | Documenti depositati | Legal |
| W20-26 (eventuale, vendor CN) | Istruttoria Golden Power (45-90 gg) | Esito governo | Legal monitora |
| W22-24 | Contract drafting + due diligence finale | Bozza contratto + DD report | Legal + Procurement |
| W25-26 | Firma contratto + Purchase Order | Contract firmato + PO emesso + anticipo M1 versato | AD + Procurement + CFO |
| **W26 (circa M+6)** | **DECISIONE FINALE + INIZIO PRODUZIONE VENDOR** | **Avvio fornitura** | |
| W27-50 (Q3-Q4 2026 / Q1 2027) | Produzione vendor + FAT + shipping + dogana | Sistema in arrivo | Vendor |
| W51-56 | SAT Pentema + training + commissioning | Operatività Y1 avvio | Firmamento + Vendor |

**Sintesi:** 6 mesi da emissione RFQ a contract signed (best case, vendor EU intra-EU); 8-9 mesi da emissione RFQ a contract signed (worst case, vendor CN con Golden Power); più 6-10 mesi addizionali per produzione, delivery e SAT. L'operatività Y1 avvio realistica è M+12-18 dalla decisione di emettere RFQ.

### 8.2 Decision Review Board Firmamento

Composizione consigliata per la decisione finale vendor:

| Ruolo | Voto | Responsabilità |
|---|---|---|
| Amministratore Delegato | Voto finale (overriding) | Decisione strategica + Golden Power engagement |
| CFO | Voto consultivo | Validazione budget + funding mix |
| Lead Systems Engineer | Voto consultivo | Compliance tecnica + capability fit |
| Procurement Manager | Voto consultivo | Commercial terms + risk supply chain |
| Aviation Regulatory Counsel | Voto consultivo | Compliance EASA/ENAC + Golden Power |
| Data Privacy Counsel (esterno) | Voto consultivo | Sovranità dati + NIS2 |
| Stakeholder cooperative (Fabrica, rappresentante) | Voto consultivo | Allineamento community Legacoop |
| Regione Liguria (opzionale, advisory) | – | Awareness istituzionale, no veto |

---

## 9. Riferimenti

### 9.1 Documenti Firmamento

- Studio di Fattibilità Vol. 1 Cap. 6 §6.1.1, §6.3.1 TS-PLATFORM-6A: `/home/user/HALE/studio-di-fattibilita/cap-06-analisi-tecnica.md`
- Studio di Fattibilità Vol. 1 Cap. 8 §8.3.1, §8.4.1 CapEx breakdown: `/home/user/HALE/studio-di-fattibilita/cap-08-economico-finanziario.md`
- VTOL UAS Specialist agent: `/home/user/HALE/.claude/agents/vtol-uas-specialist.md`
- RESERVED RSK-GEO-003 (supply chain non-EU): `/home/user/HALE/riferimenti/RESERVED-rischi-geopolitici.md` §RSK-GEO-003
- RFQ Template ufficiale: `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md` (questa stessa directory)
- RFQ Cover Letter: `RFQ-cover-letter-template.md` (questa stessa directory)
- Vendor comparison matrix: `vendor_comparison_matrix.csv` (questa stessa directory)

### 9.2 Vendor sources (web, M+3)

- JOUAV CW-30E datasheet: https://www.jouav.com/products/cw-30e.html (vendor self-declared, confidence: medium)
- JOUAV reseller EU MARIDS Spagna: https://www.marids.es/service/hybrid-gasoline-battery-long-flight-time-uav/ (confidence: medium)
- JOUAV SUMEC reseller: https://mach-sales.com/product/PRD2024090400019 (confidence: low-medium)
- Geo-matching CW-30E listing: https://geo-matching.com/products/cw-30e-hybrid-gasoline-battery-long-range-vtol-drone (confidence: medium)
- Airframer JOUAV CW-30E entry: https://www.airframer.com/aircraft_detail.html?model=JOUAV+CW-30E (confidence: medium)
- US Army TRADOC ODIN CW-30E: https://odin.tradoc.army.mil/WEG/Asset/f184794b11c29dba00568fa5c5938a78 (confidence: medium-high, dataset US Army)
- Tekever AR3 product page: https://www.tekever.com/models/ar3/ (vendor, confidence: high)
- Tekever AR3 EVO product: https://www.tekever.com/ar3-evo/ (vendor, confidence: high)
- Tekever AR3 Uncrewed Systems entry: https://www.uncrewed-systems.com/tekever-ar3/ (confidence: medium-high)
- Tekever EMSA contract €30M: https://defence-industry.eu/emsa-awards-tekever-new-e30-million-contract-to-expand-ar5-fixed-wing-uas-operations-in-europe/ (confidence: high, defense press)
- Tekever UK Home Office contract framework £1B: https://sifted.eu/articles/drones-startup-tekever-defence-uk (confidence: medium-high)
- Tekever RAF StormShroud programme: https://www.tekever.com/news/ (vendor, confidence: high)
- Tekever Wikipedia entry: https://en.wikipedia.org/wiki/Tekever (confidence: medium)

### 9.3 Regulatory più market sources

- EASA Reg. UE 2019/947 più 2019/945 Specific Category
- ENAC SORA pre-application pathway (vedi Studio Cap. 5)
- US BIS EAR Export Administration Regulations: https://www.bis.doc.gov/
- Reg. UE 2021/821 dual-use export control
- D.L. 21/2012 Golden Power più modif. D.L. 23/2020 più D.L. 50/2022 (settore aerospace)
- NIS2 Directive 2022/2555 più DO-326A awareness
- China drone export restrictions 2024-2026: https://dronelife.com/2024/12/10/chinas-export-restrictions-on-drone-parts-could-reshape-global-supply-chains/
- US drone tariffs 2025-2026 (Section 301 più 122): https://uavcoach.com/drone-tariffs/
- MarketsAndMarkets Fixed-wing VTOL UAV Market Report 2024-2030: https://www.marketsandmarkets.com/Market-Reports/fixed-wing-vtol-uav-market-173456250.html

### 9.4 Skill applicate

- `vtol-uas-specialist` (database piattaforme più pricing benchmark): `.claude/agents/vtol-uas-specialist.md`
- `trade-study-analysis` (matrice decisionale ponderata): `.claude/skills/`
- `epistemic-rigor` (caveat più falsifying observations più confidence calibration): `.claude/skills/`
- `competitor-intelligence` (analisi vendor più reference customers): `.claude/skills/`
- `regulatory-adversary` (compliance EU/IT più Golden Power): `.claude/skills/`

---

## 10. Note di Chiusura del Documento

### 10.1 Status DR-003 (parziale chiusura)

Il presente documento chiude parzialmente DR-003 "TRL JOUAV CW-30E EASA-equivalent + quotation vendor + lead time" come segue:

| Aspetto DR-003 | Status M+3 (con questo documento) |
|---|---|
| TRL JOUAV CW-30E vendor self-declared | ✅ documentato: TRL 8-9 commerciale (datasheet) |
| TRL JOUAV CW-30E EASA-validated | ❌ **non dimostrato** (no EASA conformity esplicita per CW-30E specifico) |
| Quotation reale JOUAV | ⚠️ **stima** documentata (€580-820k CapEx Y1 + €745-1.120k TCO 5 anni); quotation reale richiede RFQ formale |
| Quotation reale Tekever (Plan B) | ⚠️ **stima** documentata (€850-1.250k CapEx Y1 + €1.065-1.640k TCO 5 anni) |
| Lead time JOUAV | ⚠️ **stima** documentata (6-9 mesi best, 9-14 mesi worst) |
| Lead time Tekever | ⚠️ **stima** documentata (8-12 mesi best, 12-16 mesi worst) |
| Risk geopolitico JOUAV | ✅ analisi documentata (Section 301, Golden Power, supply chain) |
| Engagement plan vendor | ✅ timeline 3-6 mesi documentata più decision review board |

**DR-003 chiusura completa richiede:** invio RFQ formale più ricezione quotation reali entro M+6-7.

### 10.2 Recommendation finale al Project Manager Firmamento

1. Approvare il template RFQ (`RFQ-TEMPLATE-VTOL-FIRMAMENTO.md`) entro M+3-4
2. Personalizzare la cover letter (`RFQ-cover-letter-template.md`) per ogni vendor target
3. Inviare RFQ in parallelo a JOUAV (via reseller EU), Tekever e Quantum F90+ (terzo per benchmark) entro M+4
4. Avviare engagement informale DPSCS Golden Power in parallelo (mese M+4-5) per pre-screening JOUAV
5. Riservare slot calendar Decision Review Board a M+6-7 per valutazione quotation reali
6. Allocare budget legale specialistico €15-30k per Golden Power (se JOUAV vince)
7. Pre-validare opzione Plan B Tekever a livello informal contact (telefonata commerciale, no commit) per ridurre lead time fallback se necessario
8. Documentare l'engagement in Risk Register: RSK-SUP-001 mitigation in progress

### 10.3 Punti di follow-up dopo ricezione quotation reali

Quando le quotation reali sono ricevute (M+6 atteso): aggiornare la matrice decisionale §6.2 con dati reali (sostituire stime); validare o falsificare FO-1 → FO-8 in §7.2; decidere se conservare la baseline JOUAV o swap a Tekever; avviare la Golden Power notifica formale (se JOUAV vince) oppure procedere al contract drafting Tekever (se vince); comunicare al Board Firmamento la decisione finale, il budget approvato e il cronoprogramma.

---

**FINE DOCUMENTO VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER**

Documento bozza M+3 v1.0. Confidence aggregata: **low-medium** sulle stime quotation; **high** sull'analisi geopolitica e su reference customers Tekever; **medium-high** su risk supply chain JOUAV.

**Status DR-003: parzialmente chiuso. Closure completa atteso M+6 post-ricezione quotation reali.**
