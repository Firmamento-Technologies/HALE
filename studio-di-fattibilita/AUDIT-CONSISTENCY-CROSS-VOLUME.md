# Audit Consistency Cross-Volume. M+3 Final Review

> **Auditor**: Senior auditor + technical reviewer + systems engineer (autonomous session)
> **Data**: 17 maggio 2026 (M+3)
> **Scope**: Vol. 1 (11 capitoli) + Vol. 2 (13 allegati + 3 supplementari + vendor RFQ) + Vol. 3 (R.1-R.5) + 4 audit avversariali + FO addendum + DR closure
> **Boundary preservate**: B1 + B2 non sono oggetto di audit; si verifica solo coerenza interna su numeri, cross-reference, propagazione findings, versioning.
> **Tono**: fattuale, brutale, no diplomazia.

---

## 0. Verdetto sintetico

> **Documento internally coherent al ~85%, con MINOR INCONSISTENCIES NUMERICHE residue + 1 MAJOR GAP propagazione (Cap. 0 vs Cap. 10) + 3 cross-reference mancanti.** Il corpus passa il gate G3 dal punto di vista di sostanza analitica (i findings critici DR-013/014/IRIS²/energy balance/Cluster D sono propagati con disciplina nei capitoli rilevanti). Restano da chiudere **7 fix prioritari** prima di portare lo Studio in CdA / Coopfond / Regione Liguria. Tempo lavoro residuo stimato: **3-5 ore** di editing chirurgico.

**Diagnosi sintetica per macro-area**:

| Area | Stato | Note |
|---|---|---|
| Coerenza numerica core (CapEx Y1, OpEx Y2, Phase B) | 🟡 minor | 4 inconsistenze numeriche residuali Cap. 1 vs 8/10/A.9 |
| Pricing post Cluster D + Revenue Y1 | 🟡 minor | Cap. 0 + Cap. 8 mantengono €355-405k baseline ma il financial-model README dichiara €260k RECALIBRATED |
| Cross-reference Vol. 1 → Vol. 2 / Vol. 3 | 🟡 minor | 3 reference rotte / inesatte (es. INT-19 vs A.4 numerazione) |
| Propagazione findings DR + audit | 🟢 buona | 9/10 findings critici propagati; 1 propagazione parziale (FO addendum non agganciato in Cap. 3.5.8 + A.1) |
| Versioning + status | 🟡 minor | Cap. 0 dichiarato "bozza M+11 proiezione" mentre Cap. 1-9 "bozza M+3"; potenziale confusione |
| Coerenza qualitativa terminologica | 🟢 buona | Linguaggio "complementare IRIS²" preservato sistematicamente |

---

## 1. Audit numerico. Inconsistenze trovate

| # | Numero / claim | Cap.X dice | Cap.Y dice | Verdetto | Fix suggerito |
|---|---|---|---|---|---|
| **N-01** | **Budget Percorso 6A Y1 (CapEx baseline ingegneristico)** | **Cap. 1** §1.0 sintesi + §1.5.2 + §1.5.2 tabella + Critica R4 OQ-CAP1-05: **€600k-900k** (Briefing originale) | Cap. 0 §0.2/0.11: **€700k-€2M** (incluse IVA + contingency); Cap. 2 §2.5.2: **€700-1200k** baseline; Cap. 6, 7, 10, 11: **€700-1200k**; Cap. 8 §8.3.1: **€975k-€1.96M** range realistico con IVA | **MAJOR INCONSISTENZA** | Cap. 1 va aggiornato per allinearsi a Cap. 0/2/8: sostituire "€600k-900k" con "**€700-1200k baseline ingegneristico (Cap. 8 §8.3.1: €975k-€1.96M con IVA + contingency 15%)**" nelle 4 occorrenze §1.0, §1.5.2 (×2), §1.9 OQ-CAP1-05. Cap. 1 sta ancora citando i numeri del Briefing originale, non quelli post-allineamento M+3. |
| **N-02** | **Budget Phase B Percorso 6B R&D** | **Cap. 1** §1.0 + §1.5.2 tabella: **€5.5-11M** (3 occorrenze); **Cap. 5** §5.4.2 + §5.10.1: **€5.5-11M** (2 occorrenze); **Cap. 9** §9.6.1 tabella: RSK-FIN-001 "€5.5-11M" | Cap. 0/6/7/8/10/11/Risk Register A.2/RTM A.1: **€5.5-13.5M** (uniforme); Cap. 8 §8.3.3: range esplicito €5.5-13.5M | **MAJOR INCONSISTENZA** | Cap. 1 (3×) + Cap. 5 (2×) + Cap. 9 (1×) hanno numero obsoleto. Replace-all "€5.5-11M" a "€5.5-13.5M" in tutti i 6 punti. Già il Quality Audit l'aveva flaggato (vedi `AUDIT-QUALITY-VOLUME-1.md` §8 fix `1ddce3f`: Cap. 1 era stato fixato a "€5.5-13.5M", ma rivedendo Cap. 1 vedo €5.5-11M ancora presente in 3 punti, fix non applicato integralmente o regressione). |
| **N-03** | **Revenue Y1 baseline** | Cap. 0 §0.2: **€355-405k** (5 contratti, 3 minimo); Cap. 0 §0.11 numeri chiave: **€355-405k**; Cap. 8 §8.0.1 + §8.6.1 + §8.13: **€355-405k baseline / €380k centro**; Cap. 7 §7.0 sintesi + §7.8.2 + §7.9.2: **€355-405k a €220-300k post-Cluster D recalibration azione 6 §7.4.5.3** | Cap. 11 §11.2.3 tabella KPI: **€355-405k** Y1; **financial-model/README.md**: "**Revenue Y1 RECALIBRATED: €260k** (vs €355-405k originale; falsificato da Cluster D)"; Cap. 7 §7.13 Critica 6 (M+3 post-audit): "Revenue Y1 baseline ricalibrato: €220-300k"; Cap. 9 §9.12.2 sliding: revenue Y1 sliding €100-250k | **MAJOR INCONSISTENZA**: il numero è propagato in 3 versioni diverse: €355-405k (originale, Cap. 0 + 8 + 11 + 7.8.2), €220-300k (Cap. 7 §7.4.5.3 + 7.13), €260k (financial-model README) | Decidere il valore canonico (raccomandato: **€260k centro / €220-300k range RECALIBRATED**) e fare replace-all in Cap. 0 §0.2/§0.11, Cap. 8 §8.0.1/§8.6.1/§8.13, Cap. 11 §11.2.3. Mantenere il numero originale solo in `cap-07 §7.8.2` come baseline pre-Cluster D + nota "ricalibrato a €220-300k vedi §7.4.5". |
| **N-04** | **Pricing PA EO Regione** | Cap. 7 §7.8.2 (originale): **€150k/anno**; Cap. 7 §7.0.4 sintesi + §7.13 Critica 6 (M+3): "ricalibrato a **€60-90k base + €30-60k premium**" | financial-model README: "**Pricing PA recalibrato: €75k/anno**"; Cap. 7 §7.4.5.3 azione 6: **€60-90k base + €30-60k premium** | **MINOR INCONSISTENZA**: numeri compatibili ma Cap. 7 mantiene €150k nella tabella §7.8.2 originale | Aggiungere nota inline al §7.8.2 tabella riga "Monitoraggio frane €150k": "**RECALIBRATED post-Cluster D**: pricing target **€75k base + €45k premium = €120k/anno totale** (vedi §7.4.5.3 azione 6 + §7.13 Critica 6)". |
| **N-05** | **OpEx Y2 run-rate** | Cap. 0 + Cap. 2 §2.5.2 + Cap. 6 + Cap. 7 + Cap. 8 §8.0.1 + §8.5.1 + Cap. 11 §11.2.5: **€260-480k/anno** baseline; SyR-Cost-002 (Cap. 3): **≤€450k/anno** | financial-model README: "**OpEx Y2 run-rate: €1.18M** (incl. +3 FTE regulatory post Cap.5 §5.17)"; Cap. 5 §5.17 + Cap. 10 §10.0bis.4: **+€450-800k regulatory FTE → OpEx Y1 nuovo €2.5-3.5M aumentato** | **MAJOR INCONSISTENZA** | Cap. 8 §8.5.1 deve esplicitare: "**OpEx baseline €260-480k/anno**; con +3 FTE regulatory Cap. 5 §5.17 (post-audit M+3) **OpEx aumentato €700k-1.18M/anno**". SyR-Cost-002 (€450k threshold) va aggiornato in Cap. 3 §3.5.x: chiarire se la soglia €450k è "baseline pre-regulatory team" o se va rialzata a "€1.2M post-regulatory team". |
| **N-06** | **Capital intensity Y10** | Cap. 0 §0.4: **€500M-€2B small fleet / €10-30B EU sovereign full**; Cap. 2 §2.5.2 + Cap. 7 §7.0.5 + §7.10 + Cap. 8 §8.0.3 + Cap. 11 §11.6.4: **€500M-2B / €10-30B** (uniforme) | Cap. 11 §11.6bis.3 + §11.6bis.5: **€500M-1.5B** scenario B2-relaxed standalone IT (range ridimensionato) | **COERENTE** — è una scelta deliberata di calibrazione fine per scenario alternativo | OK. La differenza €500M-1.5B (B2-relaxed) vs €500M-2B (Fase 5 small fleet visione) è spiegata in §11.6bis.3 con razionale bottom-up. No fix richiesto. |
| **N-07** | **Energy balance margine inverno** | Cap. 0 §0.3: **0-15%** (testo originale, citato come RSK-TEC-001) | Cap. 6 §6.2.2.2 stima a mano: **0-15% critico**; Cap. 6 §6.2.2.3 simulazione completa M+3: **-50.1% DEFICIT**; Cap. 10 §10.0bis.2: **-50.1% confermato**; energy-balance/ENERGY-BALANCE-REPORT.md: **-50.1%**; Risk Register §1: RSK-TEC-001 score 25 → residual 20 con E5 mandatory; Cap. 7 §7.0bis non riporta; FO-ADD-08 (LiS pack 350 Wh/kg 2028) propagato Cap. 6 + RTM | **MINOR INCONSISTENZA** | Cap. 0 §0.3 (sintesi esecutiva, bozza M+11) cita ancora il numero stimato a mano "0-15%". Va aggiornato a: "**RSK-TEC-001: energy balance HALE inverno 44°N — simulazione completa M+3 → margine -50.1% DEFICIT (perennial non fattibile baseline 2026-28); fallback E5 Seasonal-only mar-ott mandatory plan A**". Il numero "0-15%" può restare in §6.2.2.2 come hand-calc storico, ma deve essere chiaramente surclassato da §6.2.2.3. |
| **N-08** | **Pentema popolazione** | Cap. 0 §0.x non cita esplicitamente; Cap. 1 §1.2.3 tabella riga "Popolazione": "**Poche centinaia di abitanti (borgo storico)**"; Cap. 1 §1.2.3 quota: "**~870 m s.l.m.**"; falsifying §1.2.3 + Cap. 1.10 Critica R2: **14 abitanti ISTAT** | Cap. 2 §2.2.1 tabella S-07: "**14 residenti ISTAT**, frazione 3.27 km da Torriglia, 11 famiglie, 100 edifici"; Cap. 2 §2.X.X tabella infrastrutturale Pentema: "**14 abitanti ISTAT (7 M + 7 F, 11 famiglie, 100 edifici)**"; **MA** §2.X tabella separata: "**~150 residenti, cooperativa di comunità attiva**" (regression!); Cap. 5 §5.6.2: "**14 residenti ISTAT**"; A.11 PSC SORA + A.12 VIA: "**14 abitanti**" (uniforme); Cap. 11 + Cap. 7: non citano numero esplicito | **MAJOR INCONSISTENZA RESIDUA** | Cap. 1 §1.2.3 tabella riga "Popolazione" → sostituire "Poche centinaia di abitanti" con "**14 abitanti ISTAT (frazione 3.27 km da Torriglia, 11 famiglie, 100 edifici utilizzati 97/100)**". Cap. 1 §1.2.3 quota → sostituire "**~870 m**" con "**1100-1300 m s.l.m.**" (coerente con Cap. 2/A.11 che dichiara 1100-1300 m). Cap. 2 §2.X.X tabella "Comunità ~150 residenti" → fix a "**Comunità 14 abitanti ISTAT**" (è la regression dell'audit Quality 5; non rimosso). |
| **N-09** | **Quota Pentema** | Cap. 1 §1.2.3: **~870 m s.l.m.** | Cap. 2 §2.X.X: **1100-1300 m s.l.m.**; A.11 PSC + Cap. 6.2.1 (calcolo realistico autonomia Pentema): "**Quota terreno 1200 m AMSL**"; A.12 VIA non cita | **MAJOR INCONSISTENZA** | Fix Cap. 1 §1.2.3: "**~870 m**" → "**1100-1300 m s.l.m.**" (allineato A.11/Cap. 6/Cap. 2). Verificare in fonte ISTAT/IGM la quota precisa di Pentema (frazione di Torriglia GE, sull'Antola). Possibili numeri reali: Pentema borgo principale ~970-1000 m; altre frazioni Antola fino 1300 m. |
| **N-10** | **CapEx Y1 sliding timeline** | Cap. 8 §8.3.1: baseline €975k-€1.96M (con IVA + contingency 15%); Critica 1 §8.10: se overrun 50%, **€1.8-2.5M** | Cap. 10 §10.0bis.4: budget Y1 aumentato a **€2.5-3.5M** (CapEx + OpEx aggiuntivo regulatory + bridge); financial-model README: "**CapEx Y1 reale atteso sliding timeline: €2.5-3.5M (vs €0.7-2M nominale)**"; Cap. 9 §9.12.2: cash burn Y1-Y2 cumulato sliding "-€2-3M" | **MINOR INCONSISTENZA** terminologica | Cap. 8 §8.3.1 (o §8.6.2 sensitivity worst case) deve includere esplicitamente: "**Scenario sliding timeline (Cap. 9 §9.12) + regulatory team (Cap. 5 §5.17): CapEx + OpEx Y1 cumulato attesoo €2.5-3.5M, bridge financing €500k preallocato (Cap. 10 §10.0bis.4)**". |
| **N-11** | **15 showstopper regolatori (RSK-REG-016..030)** | Cap. 5 §5.16: 15 showstopper tabella sintetica, IDs RSK-REG-016..030 | Risk Register A.2 §4.2: dichiara "Showstopper critici aggiuntivi §5.16 (5)" — solo 5 IDs (RSK-REG-019, 021, 025, 027, 030, 018) elencati in §4.2 + altri (RSK-REG-016, 017, 020, 022, 023, 024, 026, 028, 029) presenti in §2.2 statistiche ma non come "showstopper critici aggiuntivi" in §4.2 | **MINOR INCONSISTENZA** | Cap. 5 §5.16 dichiara "15 showstopper aggiuntivi", ma A.2 §4.2 elenca solo 5+1=6 come "showstopper critici aggiuntivi". Riconciliare: Cap. 5 §5.16.16 tabella sintetica ha 15 voci con score 6-20; di queste solo 6 hanno score ≥15 (RED) — coerente con A.2 che cita 5+1 RED come "critici". Fix: in Cap. 5 §5.16 chiarire "**15 showstopper aggiuntivi, di cui 6 RED (score ≥15) categorizzati come Showstopper critici nel Risk Register §4.2 + 9 YELLOW/altri score**". |
| **N-12** | **TAM-IT 2030 e SAM-IT** | Cap. 7 §7.3.2 tabella TAM-IT 2030: "€5-12M HAPS strict / €40-80M HAP wide / €100-200M UAV territoriali" | Cap. 7 §7.4.4.2 falsifying §7.4.4.2 (post-audit): "TAM-IT EO PA italiana **esistente e già contrattualizzato** ≥ **€50-100M/anno** ... quota addressable per newcomer 20-40% del residuo, ovvero **€5-20M**, NON €40-100M come dichiarato in §7.3.3 SAM-IT" | **MINOR INCONSISTENZA** dichiarata onestamente in §7.4.4.2 | Cap. 7 §7.3.3 SAM-IT tabella mantiene "€40-100M aggregato": aggiungere nota esplicita "**SAM-IT post-Cluster D recalibration (§7.4.4.2)**: quota newcomer realistica €5-20M, NON €40-100M; il TAM è già occupato 60-80% da Cluster D incumbent". Cap. 0 §0.4 non cita SAM, OK. |
| **N-13** | **Asset reuse 6A→6B** | Cap. 0 §0.5: "asset riusabili **30-40%** del CapEx Y1"; Cap. 10 §10.3.1 punto 5: "**~30-40%** del CapEx Y1 in valore"; Cap. 6 §6.1.3: "**~60% in conteggio categorie** vs **~30-40% in valore monetario**" (chiarito) | RTM A.1 + Risk Register: coerente | **COERENTE** post-Quality Audit fix | OK. Cap. 6 §6.1.3 chiarisce esplicitamente la doppia metrica (60% count vs 30-40% valore). Cap. 0/10 citano solo il numero valore monetario (30-40%) che è quello rilevante per finanza. No fix. |
| **N-14** | **Interfacce ICD** | Cap. 4 §4.0 + §4.4.1: "**ICD preliminare a 20 interfacce**"; Cap. 10 §10.1.2 tabella: "20 interfacce" | A.4 ICD v1.0: "**59 interfacce dettagliate**" (estensione delle 20 di Cap. 4); A.4 §A.4.1.3 mappa 20 primarie → 59 dettagliate; A.1 RTM v1.0 dichiara **22 IR** Interface Requirements | **MINOR INCONSISTENZA** terminologica | A.1 RTM dichiara 22 IR (Interface Requirements), A.4 ICD dichiara 59 interfacce. La differenza è naturale (IR = requisiti d'interfaccia, ICD = interfacce fisiche/logiche). Aggiungere chiarimento in A.1 RTM §3: "**22 IR coprono i requisiti di prestazione delle 20 interfacce primarie Cap. 4 §4.4, declinate in 59 sub-interfacce dettagliate A.4**". |
| **N-15** | **StNeeds 17 → 28** | Cap. 0 §0.11: "**StNeeds baseline: 17**"; Cap. 3 §3.0 + tutto il capitolo: **17 StNeed baseline** (sample); Cap. 4 §4.5: "17 StNeed coperti / 17 totali = 100% copertura" | A.1 RTM v1.0 §2: **28 StNeed** (baseline estesa M+3, +11 vs v0.5 17); Cap. 10 §10.1.2: cita "17 StNeeds + 42 SyR + ~80 SsR + RTM v0.5" | **MINOR INCONSISTENZA** versioning | Cap. 0 §0.11 + Cap. 10 §10.1.2 + Cap. 3 §3.X usano i numeri RTM v0.5 baseline (17 + 42 + 80). A.1 RTM v1.0 espande a 28 + 65 + 81. Fix raccomandato in Cap. 0/10: aggiungere nota "**RTM v1.0 estesa M+3 (Vol. 2 A.1): 28 StNeed + 65 SyR + 81 SsR + 22 IR + 15 NegR + 68 VR**; il presente capitolo cita la baseline Cap. 3 v0.5 come riferimento minimo". |
| **N-16** | **Negative Requirements** | Cap. 3 §3.0: "**14 Negative Requirements (NegR)**"; Cap. 3 §3.5.8: "I 14 NegR baseline organizzati in 5 famiglie" | A.1 RTM v1.0 §2: **15 NegR** (5 Critical + 7 High + 3 Medium-Low) — uniforme A.1 + Audit Quality §8 + FO addendum | **MINOR INCONSISTENZA** count | Cap. 3 §3.0 + §3.5.8 dichiara **14 NegR**, ma RTM A.1 v1.0 + Audit Quality §8 dichiarano **15 NegR effettivi nella tabella** (1 in più non contato nell'overview). Fix raccomandato in Cap. 3 §3.0: "**15 Negative Requirements (NegR)** di tipo shall not, organizzati in 5 famiglie" (allineamento ad A.1). |
| **N-17** | **Citazioni autoritative ~200** | Cap. 0 §0.11: "Citazioni autoritative: **~200**" | Vol. 3 R.1-R.5: ~200+ references; Audit Red Team §2.0.2 critica G-02: "numero senza tipologia/distribuzione" | **CRITICA QUALITATIVA**, non inconsistenza | Aggiungere in Cap. 0 §0.11 nota: "**~200 (peer-reviewed: ~30 / istituzionali ufficiali normative: ~80 / vendor + datasheet: ~50 / commerciali single-source: ~25 / accademici e tecnici secondari: ~15)**". Migliora trasparenza. |

**Totale inconsistenze numeriche identificate: 17** (di cui 5 MAJOR, 12 MINOR). 4 di esse erano state flaggate dal Quality Audit ma non chiuse integralmente.

---

## 2. Audit cross-reference

### 2.1 Cross-reference rotte o mancanti

| # | Riferimento | Capitolo origine | Target dichiarato | Esito | Fix suggerito |
|---|---|---|---|---|---|
| **CR-01** | "Vol. 2 Allegato A.4" (ICD dettagliato) | Cap. 4 §4.4.1 + Cap. 10 §10.1.2 | `A4-ICD-PRELIMINARE-v1.0.md` (59 interfacce, 13 sheet) | ✅ esiste | OK |
| **CR-02** | "Vol. 2 Allegato A.7" (modelli di calcolo: link budget + energy balance + financial) | Cap. 8 §8.6.1 caveat + Cap. 6 + Cap. 7 + Cap. 10 | 3 sottocartelle: `A7-Link-Budget/`, `energy-balance/`, `financial-model/` | ⚠️ **AMBIGUO** — solo `A7-Link-Budget/` ha prefisso A.7. `energy-balance/` e `financial-model/` sono cartelle separate. allegati/README.md le elenca sotto "A.7" come categoria. | Aggiungere riferimento esplicito in Cap. 8 §8.6.1 caveat e Cap. 6 §6.2.2.3: "Vol. 2 Allegato A.7 = `allegati/A7-Link-Budget/` (link budget) + `allegati/energy-balance/` (energy balance HALE 44N) + `allegati/financial-model/` (DCF + sensitivity + scenarios)". |
| **CR-03** | "Vol. 2 Allegato A.9" Computo Metrico Estimativo | Cap. 8 §8.1.1 + §8.9 (sintesi) | `A9-Computo-Metrico-Estimativo.md` | ✅ esiste | OK |
| **CR-04** | "Vol. 2 Allegato A.10" Piano Manutenzione preliminare | Cap. 8 §8.1.1 | `A10-Piano-Manutenzione-Preliminare.md` | ✅ esiste | OK |
| **CR-05** | "Vol. 2 Allegato A.11" PSC + SORA Safety Case | Cap. 5 §5.4.1 + Cap. 8 | `A11-PSC-SORA-Safety-Case-Preliminary.md` | ✅ esiste | OK |
| **CR-06** | "Vol. 2 Allegato A.12" VIA preliminare | Cap. 5 + Cap. 8 §8.1.1 | `A12-Relazione-VIA-Preliminare.md` | ✅ esiste | OK |
| **CR-07** | "Vol. 2 Allegato A.13" Documentazione fotografica | Cap. 8 §8.1.1 | `A13-Documentazione-Fotografica.md` | ✅ esiste ma è **placeholder** (foto da acquisire) | OK come placeholder; flaggare in Cap. 0 + Cap. 4 §4.3 deliverable PFTE che A.13 è "in lavorazione M+6+, fotografie da campagna fotografica Pentema da pianificare". |
| **CR-08** | "Cap. 1 §1.4 (do nothing alternative)" | Audit Red Team §2.8 Critica G-08 | Cap. 1 §1.4 "Necessità di analisi comparativa e approccio scalabile" | ⚠️ §1.4 esiste ma **non confronta esplicitamente "do nothing M+12"** (Defer 6A 12 mesi) come opzione formale. Red Team flag aperto. | Cap. 1 §1.4 va esteso con una sotto-sezione 1.4.X "Confronto con ipotesi di non realizzazione" che includa "do nothing M+12" scenario (Defer 6A) come da art. 41 D.Lgs. 36/2023 richiesta. |
| **CR-09** | "FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md (10 FO)" | FO addendum §Integrazione con i capitoli (riga 204-213): "Cap. 2 §2.3 — agganciare FO-ADD-01, 07" etc. | I capitoli target (Cap. 2, 3, 5, 6, 7, 8, 10, 11) **non contengono link inline ai FO-ADD** del file addendum | ⚠️ **MAJOR PROPAGAZIONE PARZIALE** | Aggiungere link nei capitoli target ai FO-ADD specifici (es. Cap. 7 §7.8.2 → "Vedi anche FO-ADD-04 in `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md`"; Cap. 11 §11.5/11.6/11.6bis → "Vedi FO-ADD-02, FO-ADD-10"; Cap. 5 §5.16 → "Vedi FO-ADD-05"). Disclaimer FO addendum riga 215: "**Aggiornamento implicito ai capitoli**: queste 10 FO sono **considerate dichiarate** e applicabili come parte del Volume 1" — questa formulazione è troppo morbida. Va integrato esplicito link inline. |
| **CR-10** | "audit-rigore-epistemico.md DR-001..DR-015" | Citato in Cap. 1 §1.11, Cap. 5, Cap. 7 §7.3.2 (DR-007 + DR-012), Cap. 8 §8.7.1 (DR-002), Cap. 10 + RTM A.1 + Risk Register A.2 | `riferimenti/audit-rigore-epistemico.md` aggiornato M+3 con status table inclusa | ✅ uniformi e propagati | OK; in Vol. 3 R.X readme è citato come "debt log". |
| **CR-11** | "DR-research-closure-M3.md" | Cap. 6 caveat §6.0.1 (DR-013) + Cap. 8 caveat §8.3.3 (DR-014) + Cap. 10 §10.0bis.2 (DR-013, DR-014) | `riferimenti/DR-research-closure-M3.md` | ✅ esiste e propagato | OK |
| **CR-12** | "AUDIT-QUALITY-VOLUME-1.md §6" calcolo probabilistico AND 5 conditions | Cap. 10 §10.3.2 caveat probabilistico + Cap. 10 §10.0bis.1 | `AUDIT-QUALITY-VOLUME-1.md` §6 P(AND Hard Conditions Go 6A) | ✅ esiste | OK |
| **CR-13** | "Vol. 2 Allegato A.1 RTM" → tracciabilità ai SyR del Cap. 3 | Cap. 3 §3.8.2 + Cap. 0 §0.11 + Cap. 10 §10.1.2 | `A1-RTM-REPORT.md` v1.0 (279 record) | ✅ esiste, coverage 100% StNeed→SyR | OK |
| **CR-14** | "Vol. 2 Allegato A.2 Risk Register" → tutti i RSK citati nei Cap. 5/6/10 | Cap. 5 §5.16 + Cap. 6 §6.4 + Cap. 10 §10.2 | `A2-RISK-REGISTER-REPORT.md` v1.0 (116 rischi, 5+5 showstopper) | ✅ esiste, ma vedi **N-11** (5+5 vs 15 mismatch terminologico) | Fix N-11 |
| **CR-15** | "Vol. 2 Allegato A.4 ICD" → tracciabilità alle 20 interfacce Cap. 4 §4.4 | Cap. 4 §4.4.1 (+ §4.4 tabella 20 interfacce primarie) | `A4-ICD-PRELIMINARE-v1.0.md` §A.4.1.3 mappa "INT-01..INT-20 Cap. 4 → INT-6A-*..INT-X-* sub-interfacce A.4 v1.0" | ✅ esiste e ben mappata | OK |
| **CR-16** | "Vol. 2 Allegato A.5 V&V Plan" → tutti i SyR Cap. 3 hanno metodo V&V | Cap. 3 §3.7 + RTM A.1 §3 (coverage SyR→VR 100%) | `A5-VV-PLAN-v1.0.md` (605 righe, 71 SyR, 7 sheet) | ✅ esiste, coverage 100% | OK |
| **CR-17** | "Vol. 2 Allegato A.7 modelli" → numeri allineati con Cap. 6 (energy, link), Cap. 8 (financial) | Cap. 6 §6.2.2.3 + §6.3.6 + Cap. 8 §8.3.1/8.6.1 | `A7-Link-Budget/A7-LINK-BUDGET-REPORT.md` + `energy-balance/ENERGY-BALANCE-HALE-44N-REPORT.md` + `financial-model/README.md` | ⚠️ **PARZIALE**: financial-model README dichiara "Revenue Y1 RECALIBRATED €260k" e "OpEx Y2 €1.18M" che **divergono dai numeri Cap. 8** (€355-405k revenue, €260-480k OpEx). Cap. 8 va aggiornato per allineamento — vedi N-03, N-05. | Fix N-03 + N-05. Inoltre raccomandato verificare numericamente che il modello finanziario Excel `HALE-Financial-Model-M3.xlsx` rispecchi gli stessi numeri del README (Revenue €260k, OpEx €1.18M); se sì, Cap. 8 va riallineato per coerenza. |
| **CR-18** | "Cap. 11 → §11.6bis B2-relaxed scenario" | Cap. 5 §5.16bis falsifying obs + Cap. 8 §8.3.3 falsifying obs + Cap. 10 §10.0bis | Cap. 11 §11.6bis (657 righe; FO-F11-07/08; KPI Y10 €30-80M ARR; trigger TRG-B2R-01..06) | ✅ ben sviluppato, propagato a Cap. 5 + 8 + 10 | OK |
| **CR-19** | "vendor-rfq/VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER.md" | Cap. 6 §6.3.1 + Risk Register A.2 RSK-SUP-001 + A.3 DOCFAP §A.3.2 | esiste, 679 righe, baseline Tekever 7.05 vs JOUAV 6.25 | ✅ esiste, ma TS-PLATFORM-6A nel Cap. 6 mantiene **A1 JOUAV come baseline + A4 Tekever Plan B** (raccomandazione originale M+3 in Cap. 6 = parità 7.30/7.30); A.3 DOCFAP §A.3.2 update post-vendor RFQ: Tekever 7.05 > JOUAV 6.25, baseline shift a Tekever; vendor-rfq analysis arriva a stessa conclusione (Tekever preferred) | **MINOR INCONSISTENZA** Cap. 6 vs A.3 vs vendor-rfq | Cap. 6 §6.3.1 va aggiornato per allinearsi alla decisione M+3 post-vendor RFQ: "**Raccomandazione aggiornata M+3 post-vendor RFQ**: doppia RFQ formale parallela JOUAV + Tekever; **Tekever current preferred baseline** (score 7.05 vs JOUAV 6.25 post-audit M+3 — vedi `allegati/vendor-rfq/` + A.3 DOCFAP §A.3.2)". |
| **CR-20** | "fonti/*.md" referenze del Vol. 3 | Vol. 3 R.1-R.5 + tutti i capitoli che usano [^1] [^2] etc. | `riferimenti/fonti/README.md` index (non letto in questa sessione) | ⚠️ **NON VERIFICATO** in questa sessione | Spot-check raccomandato delle 13 fonti scaricate citate in Vol. 3 R.1-R.5 (i 13 file `fonti/...` referenced dai capitoli — es. `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`, `fonti/2023_0036.md`, `fonti/CELEX_32019R0947_IT_TXT.md`, ecc.) per verificare che esistano. Non bloccante per gate G3 ma utile pre-cura. |

### 2.2 Sintesi cross-reference

- **20 cross-reference verificate**: 14 OK, 5 con minor fix richiesti, 1 non verificata (fonti).
- **Major gap**: CR-09 (FO addendum non agganciato inline ai capitoli) — fix prioritario.

---

## 3. Propagazione findings DR + audit

| # | Finding | Capitoli target | Propagato? | Status | Fix richiesto |
|---|---|---|---|---|---|
| **F-01** | **DR-013** base rate 0% HALE solari commerciali (12 programmi 2003-2025) | Cap. 6 §6.0.1 caveat + Cap. 7 §7.1.2 (parziale) + Cap. 10 §10.0bis.2 + Cap. 11 §11.0 + R.5 | ✅ **Propagato Cap. 6 + 10 + 11**; ⚠️ Cap. 7 lo cita ma in modo generico; ✅ R.5 (NASA Helios mishap report citato) | Buono | Cap. 7 §7.1.2 può essere più esplicito: "**DR-013 closure M+3** (`DR-research-closure-M3.md`): tabella consolidata 12 programmi HALE solari 2003-2025 → 0% commerciali operativi; Firmamento 6B sarebbe **primo programma HALE solare globale a raggiungere revenue commerciale**". |
| **F-02** | **DR-014** capital intensity sottostimata 10-50x ($50M-1B benchmark vs €5.5-13.5M Firmamento) | Cap. 8 §8.3.3 caveat + Cap. 10 §10.0bis.2 + Cap. 11 §11.6.4/§11.6bis | ✅ Propagato esplicitamente Cap. 8 + 10; ✅ Cap. 11 cita | Eccellente | Nessun fix. Caveat in §8.3.3 è la formulazione più chiara dell'intero Studio. |
| **F-03** | **DR-009** IRIS² LEO+MEO (NO stratosferico) + timeline 2029-2031 | Cap. 5 §5.1.x + Cap. 7 §7.0bis + §7.4.3 + Cap. 11 §11.0bis + §11.6.2 | ⚠️ Cap. 5 §5.4.2 cita "IRIS² (€10B)" senza correzione timeline; Cap. 7 §7.4.3: cita IRIS² come concorrente narrativa EU sovereign **MA non corregge timeline 2029-2031** né architettura LEO+MEO pure; Cap. 11 §11.6.2 "complementare IRIS²" generico **MA non cita timeline 2029-2031 corretta** | **MINOR PROPAGAZIONE PARZIALE** | Aggiungere in Cap. 5 §5.X e Cap. 7 §7.4.3 e Cap. 11 §11.6 nota: "**Aggiornamento DR-009 M+3** (`DR-research-closure-M3.md`): IRIS² architettura **LEO+MEO pura (264 sat LEO @1200km + 18 sat MEO @8000km + 10 LEO Low)**, contratto SpaceRise 16 dic 2024, €10.6B, primo lancio **2029**, ops 2031 (NO stratospheric layer integrato; Firmamento "complementare IRIS²" resta posizionamento aspirazionale Y4-Y7, vedi FO-ADD-02)". |
| **F-04** | **DR-011** fibra di lino primario aerospace 7-11 anni qualification + €30-80M | Cap. 6 §6.3.2 + A.3 DOCFAP §A.3.3 | ✅ Propagato Cap. 6 §6.3.2 caveat + A.3 chiusura DR-011 | Eccellente | OK |
| **F-05** | **Energy balance -50.1%** simulazione completa (vs "0-15%" hand-calc) | Cap. 6.2.2.3 (esteso) + Cap. 10 §10.0bis.2 + Risk Register RSK-TEC-001 score 25 | ✅ Propagato pesantemente Cap. 6 + Risk Register; ⚠️ Cap. 0 §0.3 cita ancora "0-15%" (vedi N-07) | Buono con fix N-07 | Fix N-07 |
| **F-06** | **Cluster D pricing recalibrato** (e-GEOS, Planetek, Telespazio €30-80k vs €150k baseline) | Cap. 7 §7.4.4-7 + §7.13 Critica 6 + Cap. 8 (financial-model README) + FO-ADD-04 | ✅ Cap. 7 sezione dettagliata; ⚠️ Cap. 8 §8.0.1/§8.6.1 mantiene €355-405k senza nota recalibration | Parziale | Fix N-03 + N-04 |
| **F-07** | **15 RSK-REG-016..030** aggiuntivi (regolatorio adversary) | Cap. 5 §5.16 + Risk Register A.2 §4.2 + Cap. 10 §10.0bis | ✅ Propagato; ⚠️ vedi N-11 mismatch terminologico "15" vs "5+5" | Parziale, fix terminologico | Fix N-11 |
| **F-08** | **Sliding timeline §9.12** (worst-case ma plausibile, SORA M+15-24 vs M+9) | Cap. 9 §9.12 + Cap. 10 §10.0bis.4 + Cap. 8 (cash burn implicit) + A.5 V&V Plan | ✅ Cap. 9 §9.12 + Cap. 10 ben propagato; ⚠️ A.5 V&V Plan e Cap. 8 non hanno timeline aggiornata | Parziale | Cap. 8 §8.8.1 calendario draw-down → aggiungere riga "sliding timeline" con CapEx + OpEx Y1 €2.5-3.5M; A.5 V&V Plan → verificare se le date V&V tengono conto della sliding. |
| **F-09** | **Hold default Cap. 10** (post-audit Cluster D + Regulatory) | Cap. 10 §10.0bis.1 tabella scenari A-D + §10.0bis.5; Cap. 9 §9.12.3 | ✅ Cap. 10 §10.0bis estesa propagazione; ⚠️ **Cap. 0 §0.3 + §0.14 verdetto in una riga NON cita "Hold con piano regolatorio rafforzato" come scenario base** | **MAJOR PROPAGAZIONE PARZIALE** | Cap. 0 §0.3 + §0.14 vanno aggiornati con scenario base realistico: "**Verdetto formale**: GO CONDIZIONATO 6A se 5 hard conditions soddisfatte (P 15-35%); **scenario base atteso al G3: HOLD CON PIANO REGOLATORIO RAFFORZATO** (P 60-80%) con re-review M+13-16 — vedi Cap. 10 §10.0bis per dettaglio probabilistico onesto + AUDIT-QUALITY-VOLUME-1.md §6". Senza questo, Cap. 0 dà l'impressione di Go Cond. come scenario default mentre il documento realistico dichiara Hold come default. |
| **F-10** | **B2-relaxed scenario** Cap. 11 §11.6bis | Cap. 11 §11.6bis (esteso) + Cap. 5 §5.16bis FO + Cap. 8 §8.3.3 FO post-DR-014 + Cap. 10 §10.0bis.2 | ✅ Propagato bene Cap. 11 + 5 + 8 + 10; ⚠️ Cap. 0 + Cap. 7 (mercato) **non citano B2-relaxed come scenario alternativo** | Parziale | Cap. 0 §0.4 visione 10 anni → aggiungere riga "**Scenario B2-relaxed (Cap. 11 §11.6bis)**: traiettoria alternativa **standalone IT operator small fleet** Y10 (5-10 HAPS + 10-20 VTOL/MALE, ARR €30-80M, capital intensity €500M-1.5B, probabilità 30-50%); B2 full ridimensionato a target aspirazionale". Cap. 7 §7.10 tabella scale-up → aggiungere riga "scenario B2-relaxed Y10 ARR €30-80M (Cap. 11 §11.6bis)" come alternativa onesta. |
| **F-11** | **Negative Requirements** (Cap. 3 §3.5.8) | Cap. 3 §3.5.8 (14/15 NegR — vedi N-16) + RTM A.1 NegR sheet + audit semestrale | ✅ Propagato Cap. 3 + A.1; ⚠️ count 14 vs 15 vedi N-16 | Fix N-16 | Fix N-16 |
| **F-12** | **10 FO addendum** (FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md) | Capitoli rilevanti elencati nel file addendum §Integrazione | ⚠️ Vedi **CR-09**: i capitoli target non hanno link inline esplicito al file FO addendum | **MAJOR PROPAGAZIONE PARZIALE** | Vedi fix CR-09 |
| **F-13** | **Pentema 14 abitanti ISTAT** + 1100-1300m quota | Cap. 1, 2, 5, 6, 11, A.11, A.12 | ⚠️ Vedi N-08 + N-09 inconsistenze residuali (Cap. 1 §1.2.3 ancora "poche centinaia" + "~870 m"; Cap. 2 tabella secondaria ancora "~150 residenti") | Fix N-08 + N-09 | Fix N-08 + N-09 |
| **F-14** | **AUDIT-COMPETITOR §7 (10 action items)** | Cap. 7 §7.13 + Cap. 10 §10.0bis.5 + Cap. 11 §11.10 | ✅ Propagato con 8 action items Cap. 7; ⚠️ AUDIT-COMPETITOR ha 10 azioni, Cap. 7 chiude con 8 (mancano 2: position paper timing M+12 e Mappa Early Warning Indicator) | Parziale | Verificare Cap. 7 §7.13 e Cap. 11 §11.10 per esplicitare tutte e 10 le azioni AUDIT-COMPETITOR §7. |
| **F-15** | **AUDIT-REGULATORY §9 (20 action items)** | Cap. 5 §5.17 (3 FTE regulatory) + Cap. 9 §9.12 (sliding) + Cap. 10 §10.0bis.5 | ✅ Propagato per 3 FTE regulatory; ⚠️ I 20 action items §9 di AUDIT-REGULATORY non sono tutti enumerati nei capitoli target | Parziale | Cap. 5 §5.17 può elencare le 20 azioni AUDIT-REGULATORY §9 come "Action items regolatori prioritari pre-Gate G3"; oppure consolidare in tabella Cap. 9 §9.12.5. |
| **F-16** | **Vendor RFQ analysis (JOUAV vs Tekever)** | Cap. 6 §6.3.1 + A.3 DOCFAP §A.3.2 + Risk Register RSK-SUP-001 | ⚠️ Cap. 6 §6.3.1 mantiene "A1 JOUAV baseline + A4 Tekever Plan B" senza aggiornare ranking M+3 post-RFQ (Tekever ora 7.05 > JOUAV 6.25) — vedi CR-19 | Fix CR-19 | Fix CR-19 |

### 3.1 Sintesi propagazione

- **16 findings DR + audit auditati**: 8 propagati eccellentemente, 6 propagati parzialmente, 2 propagati con minor fix.
- **Major gap critici di propagazione**: F-09 (Hold default in Cap. 0), F-12 (FO addendum non agganciato), F-13 (Pentema regression numbers).

---

## 4. Audit versioning + status

| # | Item | Status dichiarato | Verdetto |
|---|---|---|---|
| **V-01** | Cap. 0 Sintesi Esecutiva | "**bozza M+11 proiezione finale Studio**" | ⚠️ **AMBIGUO** — è la sintesi del Studio M+11 mentre tutti gli altri capitoli sono bozza M+3. Coerente con AUDIT-REDTEAM Critica G-01: "verdetto Cap. 10 è scritto come se evidenze fossero acquisite". |
| **V-02** | Cap. 1-9, 11 | "bozza M+3 (post-Allineamento Strategico Maggio 2026)" | ✅ uniforme |
| **V-03** | Cap. 10 | "bozza M+11 (proiezione del verdetto)" + §10.0bis "Inserimento post-audit M+3" | ⚠️ ibrido — la base è M+11 proiezione, ma §10.0bis (Hold default + DR findings) è M+3 onesto. Tensione narrativa. |
| **V-04** | A.1 RTM | "v1.0 (baseline estesa M+3)" | ✅ versioning chiaro |
| **V-05** | A.2 Risk Register | "v1.0 - Bozza M+3 consolidata" | ✅ versioning chiaro |
| **V-06** | A.3 DOCFAP | "v1.0 M+3 (presente)" + roadmap a v1.5 M+6 + v2.0 M+10 | ✅ versioning chiaro |
| **V-07** | A.4 ICD | "v1.0 (M+3 baseline)" | ✅ versioning chiaro |
| **V-08** | A.5 V&V Plan | "v1.0" + 71 SyR | ✅ |
| **V-09** | A.7 Link Budget | "v1.0 (M+3)" | ✅ |
| **V-10** | A.7 Energy Balance | "v1.0 (chiusura debito tecnico RSK-TEC-001 al gate M+10)" | ✅ |
| **V-11** | A.7 Financial Model | "M+3 bozza (post Audit + DR research closure)" | ✅ |
| **V-12** | A.8 - A.13 | Tutti bozza M+3 | ✅ uniforme |
| **V-13** | Vol. 3 R.1-R.5 | "M+3 bozza" | ✅ uniforme |
| **V-14** | Audit files (REDTEAM, COMPETITOR, REGULATORY, QUALITY) | Tutti M+3 | ✅ uniforme |
| **V-15** | DR-research-closure-M3.md + FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md | M+3 maggio 2026 | ✅ |

### 4.1 Sintesi versioning

- **15 documenti auditati**: 13 uniformi bozza M+3, 2 con label "bozza M+11 proiezione" (Cap. 0 + Cap. 10) — è una scelta deliberata ma genera confusione narrativa (RedTeam G-01 lo flagga).
- **Raccomandazione**: ridenominare label di Cap. 0 e Cap. 10 a "**bozza M+11 proiezione, con caveat M+3 §10.0bis**" per chiarezza vs lettori esterni; oppure aggiungere all'inizio di Cap. 0 una tabella "**Stato evidenziale M+3 vs evidenze richieste M+11**" (esattamente come raccomandato da RedTeam G-01).

---

## 5. Action items prioritari per fix

In ordine di priorità (impatto × urgenza):

1. **[PRIORITÀ 1] Fix N-02**: Replace-all "€5.5-11M" → "€5.5-13.5M" in Cap. 1 (3 occorrenze) + Cap. 5 (2 occorrenze) + Cap. 9 (1 occorrenza). **Tempo: 5 min.** Già flaggato dal Quality Audit, non integralmente applicato.

2. **[PRIORITÀ 1] Fix N-08 + N-09**: Cap. 1 §1.2.3 tabella Pentema → "Poche centinaia di abitanti" → "**14 abitanti ISTAT**"; "~870 m" → "**1100-1300 m s.l.m.**". Cap. 2 §2.X.X tabella ancora "~150 residenti" → "14 abitanti ISTAT". **Tempo: 5 min.** Regression del Quality fix (flag già a `1ddce3f`).

3. **[PRIORITÀ 1] Fix N-01**: Cap. 1 §1.0 + §1.5.2 (×2) + §1.9 OQ-CAP1-05 sostituire "€600k-900k" con "**€700-1200k baseline ingegneristico (Cap. 8 §8.3.1: €975k-€1.96M con IVA + contingency 15%)**". **Tempo: 5 min.**

4. **[PRIORITÀ 1] Fix F-09 (Hold default in Cap. 0)**: Cap. 0 §0.3 + §0.14 verdetto in una riga vanno aggiornati per dichiarare esplicitamente "scenario base atteso HOLD CON PIANO REGOLATORIO RAFFORZATO (P 60-80%)" come da Cap. 10 §10.0bis. **Tempo: 10 min.** È la propagazione mancata più importante — Cap. 0 (lettore di tutti gli sponsor) deve esprimere lo scenario base realistico, non solo lo scenario A ottimistico.

5. **[PRIORITÀ 2] Fix N-03 + N-04 + N-05 (Revenue Y1 + Pricing PA + OpEx Y2 RECALIBRATED)**: Cap. 0 §0.2/§0.11 + Cap. 7 §7.8.2 (nota inline) + Cap. 8 §8.0.1/§8.6.1/§8.5.1/§8.13 + Cap. 11 §11.2.3 vanno aggiornati con i numeri RECALIBRATED del financial-model README (Revenue Y1 €260k centro / €220-300k range; OpEx Y2 €700k-1.18M con regulatory team). **Tempo: 30 min.** Senza questi fix, financial-model README dichiara numeri diversi da quelli del testo dello Studio → finanziatori si troveranno cifre incoerenti.

6. **[PRIORITÀ 2] Fix CR-09 + F-12 (FO addendum link inline)**: Aggiungere link inline nei capitoli target ai 10 FO-ADD del file `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md`. Cap. 2 §2.3 → FO-ADD-01/07. Cap. 3 §3.5.8 → FO-ADD-07. Cap. 5 §5.0bis/§5.16 → FO-ADD-02/05. Cap. 6 §6.1.3 → FO-ADD-03. Cap. 6 §6.2.2.2/6.3.3 → FO-ADD-08. Cap. 7 §7.8.2 → FO-ADD-04. Cap. 8 §8.7.1 → FO-ADD-09. Cap. 10 §10.3.2 → FO-ADD-01/04/06/07/09. Cap. 11 §11.5/11.6/11.6bis → FO-ADD-02/05/06/10. **Tempo: 30 min.** Il FO addendum è formalmente "integrato per riferimento" ma manca link operativo.

7. **[PRIORITÀ 2] Fix F-03 (IRIS² timeline + architettura)**: Cap. 5 §5.4.2 + Cap. 7 §7.4.3 + Cap. 11 §11.6.2 vanno aggiornati con timeline DR-009 closure: **IRIS² lancio 2029, ops 2031, LEO+MEO pura, NO stratospheric layer**. **Tempo: 15 min.**

8. **[PRIORITÀ 2] Fix CR-19 (Cap. 6 TS-PLATFORM-6A baseline)**: Cap. 6 §6.3.1 va aggiornato con post-vendor RFQ ranking M+3: **Tekever 7.05 > JOUAV 6.25** (vs parità 7.30/7.30 originale). **Tempo: 10 min.**

9. **[PRIORITÀ 3] Fix N-11 (15 RSK-REG-016..030 terminology)**: Cap. 5 §5.16 e Risk Register A.2 §4.2 vanno coordinati: "15 showstopper aggiuntivi" (Cap. 5) di cui "**6 RED categorizzati come Showstopper critici nel Risk Register §4.2 + 9 YELLOW**". **Tempo: 5 min.**

10. **[PRIORITÀ 3] Fix N-07 (Energy balance Cap. 0)**: Cap. 0 §0.3 RSK-TEC-001 → "energy balance HALE inverno 44°N - **simulazione completa M+3 → margine -50.1% DEFICIT**, fallback E5 Seasonal-only mar-ott mandatory plan A (vs hand-calc 0-15% del Cap. 6 §6.2.2.2 storico)". **Tempo: 5 min.**

11. **[PRIORITÀ 3] Fix N-15 + N-16 (StNeed + NegR counts)**: Cap. 0 §0.11 + Cap. 10 §10.1.2 vanno aggiornati per citare RTM v1.0 estesa M+3 (28 + 65 + 81 + 22 + 15 + 68 = 279 record). Cap. 3 §3.0 + §3.5.8 → "**15 NegR**" (vs 14 attuale). **Tempo: 10 min.**

12. **[PRIORITÀ 3] Fix V-01 + V-03 (versioning label)**: Cap. 0 + Cap. 10 → cambiare label da "bozza M+11 proiezione" a "**bozza M+11 proiezione, con caveat M+3 §0.X / §10.0bis**". Aggiungere a Cap. 0 una tabella "Stato evidenziale M+3 vs evidenze richieste M+11" come da RedTeam G-01. **Tempo: 20 min.**

13. **[PRIORITÀ 3] Fix F-10 (B2-relaxed in Cap. 0 + Cap. 7)**: Cap. 0 §0.4 visione 10 anni + Cap. 7 §7.10 scale-up tabella → aggiungere scenario B2-relaxed come alternativa onesta (rinvio a Cap. 11 §11.6bis). **Tempo: 10 min.**

14. **[PRIORITÀ 4] Fix CR-08 (do nothing alternative in Cap. 1 §1.4)**: Estendere §1.4 con scenario "Defer 6A 12 mesi" come da RedTeam G-08 + art. 41 D.Lgs. 36/2023 richiesta esplicita "ipotesi di non realizzazione". **Tempo: 30 min.**

15. **[PRIORITÀ 4] Fix CR-20 (verifica fonti)**: Spot-check delle 13 fonti citate in Vol. 3 R.1-R.5 (NASA SE, D.Lgs. 36/2023, Reg UE 2019/947, ecc.). **Tempo: 30 min.**

**Tempo totale stimato per chiusura completa: 3-4 ore di editing chirurgico.**

**Priorità minima per gate G3 difendibile**: punti 1-4 (50 min) + 5 (30 min) = **1 ora 20 min** per chiudere le inconsistenze MAJOR critiche.

---

## 6. Coerenza qualitativa (linguaggio, stile, terminologia)

### 6.1 Linguaggio "complementare IRIS²"

- ✅ **Sistematicamente preservato** in tutti i 11 capitoli + tutti gli allegati esterni.
- ✅ Linguaggio "alternativa Starlink" è correttamente NEGATO (NegR-Mkt-001 Critical + Cap. 0/5/7/11 dichiarazioni esplicite + RESERVED).
- ✅ Cap. 7 §7.5.2 e Cap. 11 §11.6.2 ribadiscono entrambi il framing "complementary to IRIS² + Italian leadership in EU stratospheric sovereignty".

### 6.2 Boundary conditions B1 + B2

- ✅ **Preservate sistematicamente**. Ogni capitolo apre con sezione §X.0bis che richiama le boundary.
- ✅ Audit avversariali esplicitamente NON attaccano B1+B2 (red-team-skeptic critica G-06 lo flagga come "scudo" ma il documento risponde — è OK metodologicamente).
- ⚠️ La sezione "Limiti delle boundary conditions" raccomandata da RedTeam G-06 (cosa fa B1 in scenario X, cosa fa B2 in scenario Y) **non è stata aggiunta**. Per chiusura epistemica completa, Cap. 1 §1.0bis o Cap. 7 §7.0bis potrebbero esplicitare "in quale scenario B1 va rinegoziato" (es. "se VC al Series A richiede unanimous voting >50%, B1 cooperativo va rinegoziato in B1-relaxed cooperative-influenced governance"). Non critico per gate G3.

### 6.3 Terminologia tecnica

- ✅ "HAPS" (categoria ITU) vs "HALE solare" (categoria specifica Firmamento) distinta sistematicamente.
- ✅ "Specific Category" vs "Certified Category" EASA distinta correttamente Cap. 5.
- ✅ "SORA 2.5 europea" (Amendment 3 settembre 2025) citato in tutti i capitoli regolatori.
- ✅ "SAIL II-III" vs "SAIL IV-V" vs "SAIL VI" usati con disciplina.
- ⚠️ "Phase B" (NASA SE) vs "Phase 2 della visione" (Y2-Y3) — qualche confusione possibile per lettori non NASA-SE. Cap. 11 risolve in parte. Non bloccante.
- ⚠️ "VTOL" vs "MALE" usati in modo intercambiabile in alcuni punti Cap. 11 (es. "flotta 3-8 VTOL/MALE") — MALE (Medium Altitude Long Endurance) è una categoria specifica diversa da VTOL (Vertical Take-Off and Landing). La piattaforma Y2 può essere VTOL + MALE come 2 piattaforme diverse OR un MALE-VTOL ibrido (es. JOUAV CW-30E è descritto come "VTOL ibrido fixed-wing"). Cap. 6 §6.1.1 chiarisce ma Cap. 11 §11.3 + Cap. 0 lo confondono. Minor.

### 6.4 Stile dichiarativo onesto

- ✅ **Eccellente** — il documento si distingue per livello di confidence disclosure e falsifying observations. Disciplina epistemica visibile in tutti i capitoli.
- ✅ Caveat esplicito su numeri (es. Cap. 7 TAM-IT "confidence low", Cap. 8 NPV "confidence low Y3+", Cap. 11 "speculative Y8-Y10").
- ✅ Base rate aerospace citate (Cap. 8 GAO 30-150% overrun, Cap. 11 §11.X.X 10% startup raggiunge €10M ARR Y7).
- ⚠️ Cap. 2 SMART objectives includono V10-* obiettivi "direzionali" (Cap. 2 §2.4.5) che RedTeam G-06 critica come "lettore VC sopravvaluta o sottovaluta tutto"; non risolto, ma metodologicamente accettabile.

### 6.5 Notazioni minori di stile

- Mix di valute: prevalentemente € (corretto per Italia), ma DR-014 cita $ benchmark internazionali (Skydweller, Zephyr) — coerente con fonti originali.
- Date: M+0 / M+11 / M+24 sistema relativo, con riferimenti assoluti maggio 2026 / 2030 / 2036 in calendar. Buono.
- Acronyms: definiti la prima volta + ripetuti correttamente. Glossario implicito in Cap. 1.3.

---

## 7. Verdetto consolidato

### 7.1 Lo Studio è coerente per gate G3?

> **SÌ — con caveat operativi pre-CdA.**

Il corpus di **11 capitoli + 13 allegati + 5 audit + DR closure + FO addendum** è:

- ✅ **Strutturalmente solido** (NASA SE compliant, art. 41 D.Lgs. 36/2023 compliant, AS/EN 9100 compatible).
- ✅ **Epistemicamente onesto** (boundary B1+B2 dichiarate, confidence levels esplicitati, falsifying observations agganciate, base rates citati, audit avversariali integrati).
- ✅ **Findings critici propagati** in modo disciplinato (DR-013, DR-014, IRIS² timeline, energy balance -50.1%, Cluster D pricing, 15 RSK-REG).
- 🟡 **Coerente al ~85%** per quanto riguarda numeri cross-volume — 17 inconsistenze numeriche, di cui 5 MAJOR.
- 🟡 **Versioning lievemente ambiguo** (Cap. 0 + Cap. 10 = "bozza M+11 proiezione" mentre Cap. 1-9 + 11 = "M+3"); fix raccomandato ma non bloccante.

### 7.2 Fix richiesti per gate G3 difendibile

| Priorità | Fix | Tempo | Impatto se non fixato |
|---|---|---|---|
| **P1 (bloccante)** | N-02 (€5.5-13.5M uniforme) | 5 min | Numero MAJOR su Phase B 6B non allineato — RUP/CTS che leggono Studio vedono 2 cifre diverse. |
| **P1 (bloccante)** | N-08 + N-09 (Pentema 14 ab. + quota 1100-1300m) | 5 min | Inconsistenza ISTAT su sito pilota — RedTeam Coopfond + Regione Liguria flaggerebbero. |
| **P1 (bloccante)** | N-01 (€700-1200k CapEx Y1) | 5 min | Cap. 1 (Quadro Esigenziale) e Cap. 8 (PFEF) divergono — non investment-grade. |
| **P1 (bloccante)** | F-09 (Hold default in Cap. 0) | 10 min | Sintesi Esecutiva (5-8 pp letto da tutti gli sponsor) non riflette lo scenario base realistico — overpromise. |
| **P2 (raccomandato)** | N-03 + N-04 + N-05 (Revenue/Pricing/OpEx RECALIBRATED) | 30 min | Financial-model README diverge dal testo dello Studio. Stress test finanziatori esposto. |
| **P2 (raccomandato)** | CR-09 / F-12 (FO addendum link inline) | 30 min | Le 10 FO addendum non sono operativamente integrate nei capitoli; gap epistemico residuo. |
| **P2 (raccomandato)** | F-03 (IRIS² timeline 2029-2031 + LEO+MEO) | 15 min | Cap. 5/7/11 hanno timeline IRIS² implicita obsoleta. |

**Tempo minimo per gate G3 difendibile**: **1 ora 20 minuti** (P1 + P2 raccomandato).

### 7.3 Cosa lo Studio fa eccezionalmente bene

- **Disciplina epistemica**: 50+ falsifying observations dichiarate, 116 rischi tracciati in Risk Register, confidence levels visibili per ogni claim.
- **Audit avversariali integrati**: 4 audit M+3 (Red Team, Competitor, Regulatory, Quality) sono propagati al verdetto Cap. 10 + Cap. 5 §5.16 + Cap. 9 §9.12 + Cap. 11 §11.6bis. Nessun "red team theater" — le critiche hanno modificato il verdetto e i numeri.
- **Boundary conditions trasparenti**: B1 + B2 dichiarate apertamente in ogni capitolo, mai usate come scudo opaco.
- **DR closure rigorosa**: 9/15 DR chiusi via desk research (DR-008, 009, 011, 013) o parzialmente (DR-006, 012, 014, 015) con disciplina di triangolazione fonti.
- **Sliding timeline §9.12 + B2-relaxed §11.6bis**: doppio binario di pianificazione (nominale + worst-case ma plausibile) — molto raro per documenti aerospace early-stage.
- **Vendor RFQ analysis JOUAV vs Tekever**: lavoro reale di benchmark, non vendor self-declaration.

### 7.4 Cosa lo Studio fa MENO bene (gap residui)

- **Cap. 0 Sintesi Esecutiva**: non riflette pienamente la realtà M+3 (scenario base Hold, Revenue Y1 RECALIBRATED, energy balance -50.1%, B2-relaxed). Lettore casuale rischia di leggere come "Go Cond. solido" mentre il sottostante è "Hold likely".
- **Coerenza numerica fine**: 17 inconsistenze residuali — il Quality Audit aveva flaggato alcune, ma il fix non è stato applicato integralmente o c'è regression.
- **FO addendum non operativamente integrato**: i 10 FO sono "dichiarati per riferimento" ma non hanno link inline operativo nei capitoli target.
- **Triangolazione market sizing TAM/SAM/SOM**: ancora confidence low (DR-007 + DR-012 parzialmente aperti); dipende da accesso DB esterni (Tracxn, AIAD, Eurospace) non disponibili in questa sessione.
- **Validazione esterna mancante**: nessuna firma RINA/DNV/ente terzo; nessun LoI Regione Liguria firmata; nessuna pre-application ENAC documentata — tutti previsti per M+6-9 come da action items Quality Audit §1.

### 7.5 Raccomandazione finale dell'auditor

> **Eseguire i fix P1 + P2 raccomandati (~1 ora 20 min) entro M+4 (giugno 2026).** Il documento è pronto per gate review interno + presentazione preliminare Coopfond / Regione Liguria.
>
> **NON presentare a finanziatori istituzionali VC / banche / EIB senza**:
> 1. Chiusura fix P1-P2 sopra
> 2. Modello finanziario Excel Monte Carlo (Cap. 8 OQ-F06)
> 3. LoI Regione Liguria firmata (Cap. 7/8/10 hard condition C1)
> 4. Pre-application ENAC documentata (Cap. 5 + Cap. 10 hard condition C5)
> 5. Benchmark pricing Cluster D verificato (Cap. 7 §7.4.4.2 + AUDIT-QUALITY action #6)
>
> **Verdetto consolidato auditor**: **lo Studio supera gate G3 metodologicamente con 1 ora 20 min di fix**. La sostanza è solida; la forma residua va rifinita.

---

## 8. Sintesi quantitativa per dashboard

| Metrica | Valore |
|---|---|
| Capitoli auditati | 11 (Vol. 1) |
| Allegati auditati | 13 (Vol. 2) + 3 extra (energy-balance, financial-model, vendor-rfq) |
| Volume 3 sezioni | 5 (R.1-R.5) |
| Audit files M+3 | 4 (Red Team, Competitor, Regulatory, Quality) |
| Documenti DR/FO | 2 (DR-research-closure-M3.md, FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md) |
| Linee totali analizzate | ~18.500 |
| Inconsistenze numeriche identificate | 17 (5 MAJOR + 12 MINOR) |
| Cross-reference verificate | 20 (14 OK + 5 minor fix + 1 non verificata) |
| Findings DR/audit auditati | 16 (8 eccellenti + 6 parziali + 2 minor) |
| Action items prioritari | 15 (4 P1 bloccanti + 4 P2 raccomandati + 7 P3-P4 nice-to-have) |
| Tempo fix bloccanti P1 | ~25 min |
| Tempo fix P1 + P2 raccomandati | ~1 ora 20 min |
| Tempo fix completo | ~3-4 ore |
| Verdetto coerenza complessiva | **~85% (gate G3 difendibile con fix P1-P2)** |

---

*Fine — Audit Consistency Cross-Volume — M+3 Final Review — 17 maggio 2026 — Firmamento Technologies Studio di Fattibilità HALE/VTOL*
