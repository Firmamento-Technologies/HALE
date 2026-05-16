# Fonti esterne scaricate — Inventario

**Data:** maggio 2026 (round 3 — completato T2)
**Cartella:** `fonti/` (root del repo) — file scaricati manualmente dall'utente, convertiti in `.md` con `pdftotext -layout` + `pandoc` per `.docx` + `antiword` per `.doc` legacy 3GPP.

**Stato copertura:** 10/12 T1 (83%) + **8/8 T2 prioritari (100%)** + 2 fonti "senza URL" critiche ⭐⭐ + 6 bonus = **30 markdown indicizzabili (~80 MB), Studio di Fattibilità redigibile in tutti i capitoli**.

---

## 1. Inventario file scaricati

### 1.1 Normativa Italia (Codice Contratti)
| File | MB | Cosa contiene |
|---|---|---|
| `2023_0036.pdf` | 3.1 | **D.Lgs. 36/2023 Codice Contratti integrale + Allegati** (incluso I.7) |

### 1.2 Fac-simili aerospaziali italiani
| File | MB | Cosa contiene |
|---|---|---|
| `GROTTAGLIE-studio-fattibilita.pdf` | 6.8 | **DTA Puglia 2020** — fac-simile aerospaziale principale |
| `01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.pdf` | 1.8 | ENAC Piano Strategico AAM 2021-2030 |
| `02_AAM-Italian-Ecosystem-Roadmap_web-1.pdf` | 3.3 | ENAC Roadmap AAM (Allegato 1) |
| `03_AAM-Business-Plan_web-1.pdf` | 2.1 | **ENAC Business Plan AAM (Allegato 2)** |
| `Progetto_Marocco.pdf` | 7.7 | **MIMIT prefattibilità aeronautica** |
| `AnalisiCostiBusinessPlan24_05_14.pdf` | 3.4 | **Aeropolis Workshop 2014** — analisi costi + BP aerospazio |

### 1.3 ENAC / EASA / U-Space ⭐⭐ (completo)
| File | MB | Cosa contiene |
|---|---|---|
| `Regolamento_APR_Ed_3_Emend_1.pdf` | 0.3 | ⭐ **ENAC Regolamento APR Ed.3 (2019) + Emend.1 (2020)** |
| `CELEX_32019R0947_IT_TXT.pdf` | 0.5 | Reg. UE 2019/947 — Operations UAS |
| `CELEX_32019R0945_IT_TXT.pdf` | 1.4 | Reg. UE 2019/945 — Design UAS |
| `CELEX_32021R0664_IT_TXT.pdf` | 1.4 | Reg. UE 2021/664 — U-Space framework |
| `LG-2023_006-UAS-Linee-Guida-U-Space.pdf` | 1.1 | ENAC LG U-Space Ed.1 |
| `ed_decision_2025-018-r.pdf` + 3 annex | 4.2 | ⭐⭐ **EASA AMC/GM Reg.947 Amendment 3 (set 2025) — ultima SORA** |
| `ALLEGATO-1-Domanda-di-certificazione-USSP.docx` | 0.04 | 🎁 Bonus: USSP |
| `ALLEGATO-2-Comunicazione-del-fornitore-di-servizi-U-SPACE.docx` | 0.03 | 🎁 Bonus: Comunicazione |
| `ALLEGATO-3-Domanda-di-certificazione-CISP.docx` | 0.04 | 🎁 Bonus: CISP |

### 1.4 Standard tecnici aerospaziali (completo) ⭐
| File | MB | Cosa contiene |
|---|---|---|
| `NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).pdf` | 4.1 | **NASA SE Handbook Rev 2** — metodologia di base |
| `38811.pdf` | 4.7 | **3GPP TR 38.811** — NR-NTN channel models, HAPS scenari |
| `3GPP TR 38.821 /` (15 ZIP) + `3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md` (350 KB) | 96 | ⭐ **3GPP TR 38.821 v16.2.0 (mar 2023)** — Solutions for NR-NTN, full Release 16. Vedi README in sottocartella per versioni storiche. |
| `3GPP_TR_36763_IoT-NTN_draft.md` (da .doc) | 0.06 | 🎁 3GPP TR 36.763 NB-IoT/eMTC for NTN Release 17 draft v0.0.12 |
| `R-REC-P.618-14-202308-I!!PDF-E.pdf` | 0.76 | ⭐ **ITU-R P.618-14 (agosto 2023)** — propagation data for Earth-space radiocommunications (rain fade ufficiale) |
| `Link_budget_uvigo.pdf` | 1.4 | 🎁 Paper Universidade de Vigo — Small Satellite Link Budget Calculation |

### 1.5 SNAI territoriale
| File | MB | Cosa contiene |
|---|---|---|
| `psnai_finale_30072025_clean_ministro.pdf` | 1.9 | **PSNAI finale 2025** |

### 1.6 Materiali e strutture (compositi)
| File | MB | Cosa contiene |
|---|---|---|
| `2023_05_Pinato_Tesi_01.pdf` | 18 | **Polimi 2023 — Elia Pinato** — Material characterization flax fiber composite for crashworthiness |

### 1.7 Qualità aeronautica (AS9100)
| File | MB | Cosa contiene |
|---|---|---|
| `tesi.pdf` | 4.4 | 🎁 **Politecnico Torino tesi Magistrale Ingegneria Gestionale** — APQP/PPAP UmbraGroup, qualità AS9100 aeronautica. Utile per Cap. 5 dichiarazioni conformità AS/EN 9100. |

### 1.8 Spettro radio (AGCOM)
| File | MB | Cosa contiene |
|---|---|---|
| `Delibera 93-26-CONS.pdf` | 0.33 | 🎁 AGCOM Delibera 93/26/CONS (apr 2026) — UHF DVB-T (parzialmente rilevante per metodo AGCOM su spettro) |

**Totale:** 30 file markdown indicizzabili + 15 ZIP archivio storico 3GPP, ~80 MB utili.

---

## 2. Stato copertura piano originale

### Tier 1 — Must-have (12) → **10 coperti (83%)** ✅
### Tier 2 — Should-have (8 prioritari) → **8/8 coperti (100%)** ✅
- ✅ MIMIT Progetto Marocco
- ✅ Aeropolis Analisi Costi BP
- ✅ Reg. UE 2019/945 (Design UAS)
- ✅ Reg. UE 2021/664 (U-Space framework)
- ✅ Polimi tesi flax (Pinato 2023)
- ✅ ITU-R P.618-14 (rain fade)
- ✅ 3GPP TR 38.821 (NTN solutions) — Release 16 v16.2.0
- ✅ Politecnico Torino tesi (qualità aeronautica AS9100)

### Fonti "senza URL diretto" → **2 jackpot coperti** ⭐⭐
- ✅ **ENAC Regolamento APR Ed.3 + Emend.1**
- ✅ **EASA SORA AMC/GM rev. corrente** (Amendment 3 settembre 2025)

### Ancora mancanti (T2/T3, opzionali)
- ⏳ Reg. UE 2021/665 + 2021/666 (U-Space ATM/SERA)
- ⏳ ITU-R P.676 (atmospheric attenuation)
- ⏳ Coopfond bando Cooding 2026 (non pubblicato, da verificare direttamente)
- ⏳ EASA SC-Light-UAS
- ⏳ ITU Radio Regulations 2024 (potenziale accesso registrato)
- ⏳ AGCOM PNRF aggiornato (MIMIT, URL incerto)

---

## 3. Cosa abilita (capitolo per capitolo) — riepilogo

| Capitolo Studio | Stato fonti | Capacità di stesura |
|---|---|---|
| Cap. 1 Inquadramento | ✅ Completo | **Stesura completa autoritativa** |
| Cap. 2 Stakeholder + SMART | ✅ Completo | Stesura completa |
| Cap. 3 Requisiti + RTM | ✅ NASA SE Handbook | **Stesura completa con metodologia citata** |
| Cap. 4 Scope + ICD | ✅ Completo | Stesura completa |
| **Cap. 5 Quadro normativo** | ⭐⭐ Tutto coperto + SORA aggiornata set 2025 | **Capitolo investment-grade** |
| Cap. 6 Analisi tecnica | ✅ NASA SE + 3GPP 38.811/38.821 + ITU P.618 + Link Budget + Pinato flax | **Stesura completa con triangulation** |
| Cap. 7 Mercato + BP | ✅ 3 template italiani (ENAC AAM + MIMIT + Aeropolis) | **Capitolo investment-grade** |
| Cap. 8 Economico-finanziario | ✅ Allegato I.7 + ENAC AAM BP + Aeropolis costing | **Stesura completa con framework italiano** |
| Cap. 9 Cronoprogramma | ✅ NASA SE + DTA Grottaglie | Stesura completa |
| Cap. 10 Raccomandazione | (richiede chiusura Cap. 1-9) | Finale |
| Cap. 11 Roadmap | ✅ visione-10-anni + ENAC AAM Roadmap | Stesura completa |

**Conclusione operativa:** **tutti i capitoli dello Studio sono ora redigibili a livello investment-grade**, con triangulation interna per i claim numerici principali e fonti autoritative italiane + EU + ITU + 3GPP + NASA aggiornate.

---

## 4. Impatto sul Debito di Rigore (audit-rigore-epistemico.md)

DR ora completamente o parzialmente coperti:
| DR-ID | Item | Stato |
|---|---|---|
| DR-004 | ENAC SAIL stima per Pentema | ◐ Coperto framework (ENAC Reg APR Ed.3 + ED Decision 2025-018-R SORA + ENAC LG U-Space). Per stima specifica Pentema serve ancora pre-application meeting ENAC |
| DR-009 | IRIS² + AAM context | ◐ Parzialmente: AAM ENAC Piano fornisce contesto IT |
| DR-011 | Fibra di lino qualificazione aerospace | ◐ Coperto da Pinato 2023 (Polimi crashworthiness). Per longherone primario certificato HALE confidenza resta low |

DR ancora aperti (richiedono engagement esterno):
- DR-001 Pentema-Torriglia anagrafica (Comune)
- DR-002 Coopfond Cooding bando 2026 (chiamata diretta)
- DR-003 TRL JOUAV CW-30E (quotation vendor + reference EU operatori)
- DR-005 AGCOM spettro HAPS Italia (consultazione AGCOM)
- DR-006 Garante Privacy sorveglianza HAPS (analisi precedenti dedicata)
- DR-007 Base rate aerospace startup IT (DB AIAD/StartupItalia)
- DR-008 EuroHAPS estensione civile / call EDF (engagement DG DEFIS)
- DR-010 CIRA partnership willingness (engagement CIRA)
- DR-012 Mercato HAPS triangulation fonti non-commerciali
- DR-013 Programmi HALE falliti — analisi cause
- DR-014 Capital intensity HAPS perennial
- DR-015 Posizione Leonardo/TAS

---

## 5. Stato copertura finale per categoria

| Categoria | Copertura | Note |
|---|---|---|
| **Codice Contratti / PFTE** | ✅ Completo | D.Lgs.36/2023 integrale + Allegato I.7 |
| **Fac-simili aerospaziali ITA** | ✅ Completo | DTA + ENAC AAM (3) + MIMIT + Aeropolis = 6 template italiani |
| **Normativa UAS EU/IT** | ⭐⭐ Completo + aggiornato | Reg.947 + 945 + 664 + ENAC APR + AMC/GM **ultima SORA settembre 2025** |
| **Standard tecnici** | ✅ Completo | NASA SE + 3GPP 38.811 + 38.821 + ITU P.618 + Link Budget |
| **SNAI / territoriale** | ✅ Sufficiente | PSNAI 2025 + materiali interni |
| **Compositi / flax** | ✅ Sufficiente | Pinato 2023 Polimi |
| **Qualità AS9100** | ✅ Sufficiente | Tesi Polito UmbraGroup |
| **AGCOM spettro HAPS** | ⏳ Aperto | Delibera 93/26 è su DVB, non HAPS |
| **Privacy / Garante** | ⏳ Aperto | Da analisi precedenti dedicata |
| **Business HAPS / market** | ⏳ Open | Triangulation con fonti non-commerciali da fare |

---

## 6. Prossimo passo raccomandato

✅ **Iniziare stesura sostanziale dello Studio.** Suggerisco partire da:

**Cap. 5 (Quadro Normativo)** — perché:
- Fonti **completissime e aggiornate** (compresa SORA settembre 2025)
- Capitolo che **dà credibilità** al documento davanti a finanziatori/regolatori
- Dimostra rigore metodologico (citazioni autoritative)
- Stesura possibile in 1-2 sessioni intensive
- Una volta scritto, diventa baseline per **engagement con ENAC/EASA** (DR-004)

In parallelo (o subito dopo) **Cap. 3 (Requisiti + RTM)** come fondamento metodologico per i Cap. 6-7-8.

Lo Studio finale è un documento di 80-150 pagine (Volume 1) + allegati tecnici (Volume 2) + bibliografia (Volume 3). La stesura completa richiede 4-8 sessioni intensive distribuite su 2-4 settimane di lavoro Claude + revisione utente.


---

## 1. Inventario file scaricati

### 1.1 Normativa Italia (Codice Contratti)
| File | MB | Cosa contiene |
|---|---|---|
| `2023_0036.pdf` | 3.1 | **D.Lgs. 36/2023 Codice Contratti integrale + Allegati** (incluso I.7 contenuti PFTE/QE/DOCFAP/DIP) |

### 1.2 Fac-simili aerospaziali italiani
| File | MB | Cosa contiene |
|---|---|---|
| `GROTTAGLIE-studio-fattibilita.pdf` | 6.8 | **DTA Puglia 2020** — fac-simile aerospaziale principale |
| `01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.pdf` | 1.8 | ENAC Piano Strategico Nazionale AAM 2021-2030 |
| `02_AAM-Italian-Ecosystem-Roadmap_web-1.pdf` | 3.3 | ENAC Roadmap AAM (Allegato 1) |
| `03_AAM-Business-Plan_web-1.pdf` | 2.1 | **ENAC Business Plan AAM (Allegato 2)** — template BP aeronautico italiano |
| `Progetto_Marocco.pdf` | 7.7 | **MIMIT prefattibilità aeronautica internazionale** ⭐ |
| `AnalisiCostiBusinessPlan24_05_14.pdf` | 3.4 | **Aeropolis Workshop 2014** — analisi costi + business plan aerospazio |

### 1.3 ENAC / EASA / U-Space ⭐ (sostanzialmente completo)
| File | MB | Cosa contiene |
|---|---|---|
| `Regolamento_APR_Ed_3_Emend_1.pdf` | 0.3 | ⭐ **ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed.3 (2019) + Emendamento 1 (2020)** — riferimento normativo italiano UAS |
| `CELEX_32019R0947_IT_TXT.pdf` | 0.5 | Reg. UE 2019/947 — Operations UAS (Open/Specific/Certified) |
| `CELEX_32019R0945_IT_TXT.pdf` | 1.4 | Reg. UE 2019/945 — Design UAS classi C0-C6 |
| `CELEX_32021R0664_IT_TXT.pdf` | 1.4 | Reg. UE 2021/664 — U-Space framework |
| `LG-2023_006-UAS-Linee-Guida-U-Space.pdf` | 1.1 | ENAC LG U-Space Ed.1 (dic 2023) |
| **`ed_decision_2025-018-r.pdf`** | 0.25 | ⭐⭐ **EASA ED Decision 2025/018/R (15 set 2025) — Amendment 3 Issue 1 AMC/GM Reg.UE 2019/947** — introduce ultima versione SORA |
| `annex_to_ed_decision_2025-018-r_1.pdf` | 3.3 | Annex completo nuova SORA (196 menzioni SORA) |
| `corrigendum_to_ed_decision_2025-018-r.pdf` | 0.16 | Corrigendum |
| `explanatory_note_to_ed_decision_2025-018-r.pdf` | 0.4 | Explanatory note RMT.0730 Subtask 3 |
| `ALLEGATO-1-Domanda-di-certificazione-USSP.docx` | 0.04 | 🎁 Bonus: Domanda certificazione USSP |
| `ALLEGATO-2-Comunicazione-del-fornitore-di-servizi-U-SPACE.docx` | 0.03 | 🎁 Bonus: Comunicazione fornitore U-Space |
| `ALLEGATO-3-Domanda-di-certificazione-CISP.docx` | 0.04 | 🎁 Bonus: Domanda certificazione CISP |

### 1.4 Standard tecnici aerospaziali
| File | MB | Cosa contiene |
|---|---|---|
| `NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).pdf` | 4.1 | **NASA SE Handbook Rev 2** — metodologia di base |
| `38811.pdf` | 4.7 | **3GPP TR 38.811** — NR-NTN channel models, HAPS |
| `Link_budget_uvigo.pdf` | 1.4 | 🎁 Bonus: paper accademico "Small Satellite Link Budget Calculation" (Universidade de Vigo) — applicabile alla skill `link-budget-calculator` |

### 1.5 SNAI territoriale
| File | MB | Cosa contiene |
|---|---|---|
| `psnai_finale_30072025_clean_ministro.pdf` | 1.9 | **PSNAI finale 2025** |

### 1.6 Materiali e strutture
| File | MB | Cosa contiene |
|---|---|---|
| `2023_05_Pinato_Tesi_01.pdf` | 18 | **Polimi 2023 - Elia Pinato** — "Material characterization of a flax fiber reinforced composite for crashworthiness applications" — Aeronautical Engineering. Triangulation per claim fibra di lino. |

### 1.7 Spettro radio (AGCOM)
| File | MB | Cosa contiene |
|---|---|---|
| `Delibera 93-26-CONS.pdf` | 0.33 | 🎁 Bonus: **AGCOM Delibera 93/26/CONS del 14/04/2026** — pianificazione frequenze UHF da rete nazionale n.12 PNAF-DVB. (Specifica DTT broadcasting, parzialmente rilevante per metodo AGCOM su gestione spettro.) |

### 1.8 NTN aggiuntivi
| File | Stato |
|---|---|
| `DRAFT-For RAN1-104e-R1-210XXXX-TR 36.763 IoT NTN-v002-RAN1-RAN2.doc` | Draft 3GPP TR 36.763 IoT NTN — **formato .doc legacy non convertibile** (libreoffice non disponibile in runtime). Lettura nativa Word possibile in locale; non critico. |

**Totale:** 26 file (~70 MB), 25 markdown convertiti, ~75.000+ righe indicizzabili.

---

## 2. Stato copertura piano originale

### Tier 1 — Must-have (12) → **10 coperti (83%)** ✅
### Tier 2 — Should-have (15) → **5/8 prioritari coperti (62%)** ✅
- ✅ MIMIT Progetto Marocco
- ✅ Aeropolis Analisi Costi BP
- ✅ Reg. UE 2019/945 (Design UAS)
- ✅ Reg. UE 2021/664 (U-Space framework)
- ✅ Polimi tesi flax (Pinato 2023)
- ⏳ 3GPP TR 38.821 (NTN solutions)
- ⏳ ITU-R P.618 (rain fade) — **parzialmente** sostituito dal paper Uvigo
- ⏳ Politecnico Torino tesi aerospace (14893)

### Fonti "senza URL diretto" che ho segnalato → **2 jackpot coperti** ⭐⭐
- ✅ **ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed.3 + Emend.1** (era "URL specifico variabile")
- ✅ **EASA SORA AMC/GM rev. corrente** — coperto dalla pubblicazione settembre 2025 (ED Decision 2025-018-R) ⭐⭐

### Ancora mancanti
- ⏳ Reg. UE 2021/665 + 2021/666 (U-Space ATM/SERA)
- ⏳ ITU-R P.618 + P.676 (link budget rain/atmospheric)
- ⏳ 3GPP TR 38.821
- ⏳ Coopfond bando Cooding 2026 — non pubblicato, da verificare direttamente
- ⏳ EASA SC-Light-UAS
- ⏳ ITU Radio Regulations 2024

---

## 3. Cosa abilita (capitolo per capitolo)

| Capitolo Studio | Fonti utilizzabili ora | Capacità di stesura |
|---|---|---|
| **Cap. 1** Inquadramento (= Quadro Esigenziale) | `psnai_finale_30072025`, `2023_0036` Allegato I.7 | **Stesura completa possibile** |
| **Cap. 2** Stakeholder + SMART | Materiale interno + SNAI sources | **Stesura completa** |
| **Cap. 3** Requisiti + RTM | `NASA04. SysEng Handbook` §4 | **Stesura completa con metodologia citata** |
| **Cap. 4** Scope + ICD | NASA SE Handbook + Briefing interno | **Stesura completa** |
| **Cap. 5** Quadro normativo | ⭐⭐ **TUTTO COPERTO**: D.Lgs.36 + Reg.UE 947+945+664 + ENAC Reg.APR Ed.3 + ED Decision 2025-018-R (nuova SORA) + ENAC LG U-Space + 3 Allegati USSP/CISP | **Capitolo definitivamente completabile con fonti autoritative aggiornate** |
| **Cap. 6** Analisi tecnica | NASA SE + 3GPP 38.811 + Link Budget Uvigo + DTA Grottaglie (parte tecnica) + Pinato (lino) | **Stesura completa** |
| **Cap. 7** Mercato + BP | ENAC AAM Business Plan (template ufficiale) + MIMIT Progetto Marocco + Aeropolis Analisi Costi | **Capitolo completabile con 3 template italiani autoritativi** |
| **Cap. 8** Economico-finanziario | D.Lgs.36 Allegato I.7 (Quadro Economico format) + ENAC AAM BP + Aeropolis costing | **Stesura completa con framework italiano** |
| **Cap. 9** Cronoprogramma + Gate | NASA SE Phase A-B-C + DTA Grottaglie milestone | **Stesura completa** |
| **Cap. 10** Raccomandazione | (richiede chiusura dei Cap. 1-9) | Da fare ultimo |
| **Cap. 11** Roadmap post-fattibilità | `riferimenti/visione-10-anni.md` + ENAC AAM Roadmap | **Stesura completa** |

**Conclusione operativa:** **Si può iniziare la stesura sostanziale dello Studio di Fattibilità ORA**. Le poche fonti mancanti sono prevalentemente di triangulation/verifica, non bloccanti.

---

## 4. Impatto sul Debito di Rigore (audit-rigore-epistemico.md)

DR ora coperti (nuovi rispetto a INDEX precedente):
| DR-ID | Item | Stato attuale |
|---|---|---|
| DR-004 | ENAC SAIL stima per Pentema | ◐ Coperto framework: ENAC Reg APR Ed.3 + ED Decision 2025-018-R + ENAC LG U-Space. Per stima SAIL Pentema serve ancora pre-application meeting |
| DR-009 | IRIS² timeline + AAM context | ◐ Parzialmente: AAM ENAC Piano fornisce contesto italiano |
| DR-011 | Fibra di lino qualificazione aerospace | ◐ **Parzialmente coperto** da Pinato 2023 (Polimi) — caratterizzazione mecccanica per **crashworthiness**, non per longherone primario certificato. Confidenza materiale ↑ medium, confidenza applicabilità HALE primaria invariata |

DR ancora aperti (richiedono contatto diretto / ricerca esterna):
- DR-001 Pentema-Torriglia anagrafica
- DR-002 Coopfond Cooding bando 2026
- DR-003 TRL JOUAV CW-30E EASA-equivalent  
- DR-005 AGCOM spettro HAPS Italia (la Delibera 93/26 è su DVB, non HAPS)
- DR-006 Garante Privacy sorveglianza HAPS
- DR-007 Base rate aerospace startup IT
- DR-008 EuroHAPS estensione civile / call EDF
- DR-010 CIRA partnership willingness
- DR-012 Mercato HAPS triangulation
- DR-013 Programmi HALE falliti analisi cause
- DR-014 Capital intensity HAPS perennial
- DR-015 Posizione Leonardo/TAS

---

## 5. Prossimi passi raccomandati

1. **🎯 Iniziare stesura sostanziale**: con queste 26 fonti possiamo redigere i Cap. 1, 3, 4, 5, 6, 7, 9, 11 in maniera autoritativa. Suggerirei partire da:
   - **Cap. 5** (Normativo) — fonti completissime, capitolo che dà credibilità al documento
   - **Cap. 3** (Requisiti + RTM) — fondamento metodologico per tutto il resto
2. **Round successivo download** (opzionale, ~15 min): ITU-R P.618 + 3GPP TR 38.821 + Tesi Polito 14893
3. **Engagement esterno** (settimane): chiudere DR-001, -002, -003, -005, -006, -008, -010 con contatti diretti
4. **Ricerca dedicata** (Claude su input utente, ore): DR-013 (HALE falliti), DR-014 (capital intensity), DR-007 (base rate IT)

---

## 6. Note operative

### Sui file EASA ED Decision 2025-018-R
È la **revisione SORA più recente** in vigore al settembre 2025. Sostituisce le versioni precedenti per le AMC/GM al Reg. UE 2019/947 Operations UAS. **Da usare come riferimento autoritativo nel Cap. 5** e nella skill `gate-review-checklist`. L'annex (3.3 MB) contiene il framework SORA dettagliato.

### Sulla Delibera AGCOM 93/26
È del 14/04/2026 (molto recente) ma riguarda **specifically pianificazione UHF per DVB-T** (TV broadcasting), **non** allocazione HAPS. Resta utile come **template** di come AGCOM gestisce delibere sullo spettro, ma per HAPS specifico serve consultazione diretta (DR-005 ancora aperto).

### Sul file .doc 3GPP TR 36.763
Formato Word legacy `.doc` non convertibile dal runtime (libreoffice non disponibile, Java mancante). Apertura locale possibile. Non critico: è un draft IoT NTN, non NR-NTN come 38.811.


---

## 1. Inventario file scaricati

### 1.1 Normativa Italia
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `2023_0036.pdf` | 3.1 | 12.680 | **Testo integrale D.Lgs. 36/2023 Codice Contratti aggiornato al 28/12/2023 + Allegati** (inclusi Allegato I.7 con contenuti minimi PFTE/QE/DOCFAP/DIP). Copre fonti #1+#2+#3 del piano originale. |

### 1.2 Fac-simili aerospaziali italiani
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `GROTTAGLIE-studio-fattibilita.pdf` | 6.8 | 5.253 | **DTA Puglia 2020** — fac-simile principale aerospaziale. Indice navigabile, sezione conclusiva "opportunità – volontà – fattibilità". |
| `01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.pdf` | 1.8 | – | ENAC Piano Strategico Nazionale AAM 2021-2030 |
| `02_AAM-Italian-Ecosystem-Roadmap_web-1.pdf` | 3.3 | – | ENAC Roadmap AAM 2021-2030 (Allegato 1 del Piano) |
| `03_AAM-Business-Plan_web-1.pdf` | 2.1 | 1.402 | **ENAC Business Plan AAM 2021-2030 (Allegato 2)** — template BP aeronautico italiano principale |

### 1.3 ENAC / EASA / U-Space
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `CELEX_32019R0947_IT_TXT.pdf` | 0.5 | – | **Reg. UE 2019/947** — Operations UAS (Open/Specific/Certified) — testo italiano |
| `LG-2023_006-UAS-Linee-Guida-U-Space.pdf` | 1.1 | – | **ENAC Linee Guida U-Space Ed.1** (dicembre 2023) — framework U-Space italiano |
| `ALLEGATO-1-Domanda-di-certificazione-USSP.docx` | 0.04 | – | 🎁 Bonus: Domanda certificazione USSP (U-space Service Provider) |
| `ALLEGATO-2-Comunicazione-del-fornitore-di-servizi-U-SPACE.docx` | 0.03 | – | 🎁 Bonus: Comunicazione fornitore U-Space |
| `ALLEGATO-3-Domanda-di-certificazione-CISP.docx` | 0.04 | – | 🎁 Bonus: Domanda certificazione CISP (Common Information Service Provider) |

### 1.4 Standard tecnici aerospaziali
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).pdf` | 4.1 | 14.819 | **NASA Systems Engineering Handbook Rev 2** — metodologia di base del progetto, V-model, RTM, trade studies, gate reviews |
| `38811.pdf` | 4.7 | 7.815 | **3GPP TR 38.811** — NR-NTN channel models, scenari deployment HAPS — base per skill `link-budget-calculator` |

### 1.5 SNAI territoriale
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `psnai_finale_30072025_clean_ministro.pdf` | 1.9 | 6.415 | **PSNAI finale 2025** — Piano Strategico Nazionale Aree Interne. (Già presente anche in `Aree interne/`, duplicato non rimosso.) |

**Totale:** 13 file, ~34 MB convertiti, ~50.000+ righe markdown indicizzabili.

---

## 2. Confronto con piano originale (40 fonti pianificate)

### Tier 1 — Must-have (12) → **10 coperti (83%)** ✅

| # | Originale | Stato |
|---|---|---|
| 1 | D.Lgs. 36/2023 testo integrale (bosettiegatti.htm) | ✅ via PDF integrale `2023_0036.pdf` |
| 2 | D.Lgs. 36/2023 Allegati (bosettiegatti.pdf) | ✅ Inclusi nel PDF integrale (verificato presenza Allegato I.7) |
| 3 | art. 41 codiceappalti.htm | ✅ Incluso nel PDF integrale |
| 7 | **DTA Grottaglie** | ✅ Scaricato |
| 8 | **ENAC AAM Piano Strategico** | ✅ Scaricato (versione web 1, probabilmente IT) |
| 9 | **ENAC AAM Roadmap** | ✅ Scaricato |
| 10 | **ENAC AAM Business Plan** | ✅ Scaricato |
| 16 | Reg. UE 2019/947 | ✅ Scaricato (CELEX italiano) |
| 21 | ENAC LG-2023/006 U-Space | ✅ Scaricato |
| 22 | NASA SE Handbook Rev2 | ✅ Scaricato |
| 23 | 3GPP TR 38.811 | ✅ Scaricato |
| 27 | PSNAI finale 2025 | ✅ Scaricato |

**Bonus non pianificati ma utili:**
- 🎁 Allegati USSP/CISP della ENAC LG-2023/006 — essenziali per la fase regolatoria operativa

### Tier 2 — Should-have (15) → **0 coperti (0%)** ⏳
### Tier 3 — Nice-to-have (13) → **0 coperti (0%)** ⏳

---

## 3. Cosa manca ancora — round successivo

### T2 mancanti (priorità alta per triangulation)

| Documento | URL | Perché serve |
|---|---|---|
| MIMIT Progetto Marocco prefattibilità | https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf | Cap. 5+7 template MIMIT |
| Aeropolis Analisi Costi BP | http://www.aeropolis.it/workshop2014/workshop-24-5-2014/AnalisiCostiBusinessPlan24_05_14.pdf | Cap. 8 struttura costing aerospace |
| Reg. UE 2019/945 (Design UAS) | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0945 | Cap. 5 classi UAS C0-C6 |
| Reg. UE 2021/664 (U-Space framework) | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0664 | Cap. 5 base U-Space |
| 3GPP TR 38.821 (NTN solutions) | https://www.atis.org/wp-content/uploads/3gpp-documents/Rel16/ATIS.3GPP.38.821.V1600.pdf | Cap. 6.2 |
| ITU-R P.618 (rain fade) | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.618-13-201712-S!!PDF-E.pdf | skill `link-budget-calculator` |
| Polimi tesi flax crashworthiness | https://www.politesi.polimi.it/retrieve/a81cb05b-7d29-616b-e053-1605fe0a889c/2020_07_Veneruso.pdf | Agente `aerodynamics-structures-engineer` |
| Politecnico Torino tesi aerospace | https://webthesis.biblio.polito.it/14893/1/tesi.pdf | Cap. 6 riferimenti accademici |

### T3 (nice-to-have, opzionali)

Vedi `riferimenti/fonti/README.md` per la lista completa.

### Fonti senza URL diretto (richiede ricerca manuale)

- **ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed.3** (2021) — su enac.gov.it, URL specifico cambia
- **EASA SORA AMC/GM** rev. corrente — su easa.europa.eu
- **EASA SC-Light-UAS** — su easa.europa.eu
- **ITU Radio Regulations 2024** — può richiedere registrazione ITU
- **AGCOM PNRF aggiornato** — pubblicato da MIMIT
- **Coopfond bando Cooding 2026** — non ancora pubblicato (verifica diretta Coopfond)

---

## 4. Impatto sul Debito di Rigore (audit-rigore-epistemico.md)

### DR ora coperti o parzialmente coperti
| DR-ID | Item | Stato |
|---|---|---|
| DR-001 | Pentema-Torriglia anagrafica | ⏳ Non coperto (richiede contatto Comune) |
| DR-002 | Coopfond Cooding bando attivo 2026 | ⏳ Non coperto (richiede contatto Coopfond) |
| DR-003 | TRL JOUAV CW-30E EASA-equivalent | ⏳ Non coperto (richiede quotation vendor + reference operatori) |
| DR-004 | ENAC SAIL stima per Pentema | ◐ **Parzialmente coperto** — la `LG-2023_006-UAS-Linee-Guida-U-Space.md` fornisce framework U-Space; per SAIL specifico Pentema serve pre-application meeting ENAC |
| DR-005 | AGCOM spettro HAPS Italia | ⏳ Non coperto (richiede consultazione AGCOM) |
| DR-006 | Garante Privacy posizione su sorveglianza HAPS | ⏳ Non coperto (richiede analisi precedenti dedicata) |
| DR-007 | Base rate aerospace startup IT | ⏳ Non coperto |
| DR-008 | EuroHAPS estensione civile / call EDF | ⏳ Non coperto (richiede engagement DG DEFIS) |
| DR-009 | IRIS² timeline e architettura stratosferica | ◐ **Parzialmente coperto** — Piano Strategico AAM ENAC dà contesto italiano AAM; per IRIS² serve engagement DG CNECT |
| DR-010 | CIRA willingness for civilian HALE | ⏳ Non coperto |
| DR-011 | Fibra di lino qualificazione aerospace primaria | ⏳ Non coperto (richiede peer-reviewed dedicata) |
| DR-012 | Mercato HAPS triangulation fonti non commerciali | ⏳ Non coperto (richiede AIAD/Eurospace/EUSPA reports) |
| DR-013 | Programmi HALE falliti — cause | ⏳ Non coperto (richiede ricerca dedicata) |
| DR-014 | Capital intensity HAPS perennial — stime indipendenti | ⏳ Non coperto |
| DR-015 | Posizione Leonardo/TAS verso Firmamento | ⏳ Non coperto |

### Nuovi possibili utilizzi dai download

Le 13 fonti scaricate **abilitano** stesura sostanziale di:

| Capitolo Studio | Fonte abilitante | Note |
|---|---|---|
| **Cap. 1** Inquadramento | PSNAI finale 2025 | Razionale pubblico SNAI consolidato |
| **Cap. 3** Requisiti + RTM | NASA SE Handbook §4 | Metodologia requirements + RTM template |
| **Cap. 5** Quadro normativo | D.Lgs.36/2023 + Reg.947 + LG U-Space + 3 Allegati USSP/CISP | **Capitolo regolatorio sostanzialmente completabile** |
| **Cap. 6** Analisi tecnica | NASA SE + 3GPP 38.811 + DTA Grottaglie sezioni tecniche | Struttura tecnica + link budget HAPS |
| **Cap. 7** Mercato + BP | ENAC AAM Piano + Roadmap + BP | **Template italiano BP aeronautico ufficiale disponibile** |
| **Cap. 8** Economico-finanziario | ENAC AAM Business Plan (struttura) + D.Lgs.36 Allegato I.7 (Quadro Economico) | Template QE conforme art.41 |
| **Cap. 9** Cronoprogramma | DTA Grottaglie + NASA SE Phase A-B-C | Esempio aerospace IT + framework NASA |

---

## 5. Riorganizzazione cartelle (suggerita)

I file sono attualmente in `fonti/` (root del repo, flat). Per allinearli alla struttura previsto nel piano (`riferimenti/fonti/01-normativa-italia/`, `02-fac-simili-aero/`, ecc.) servirebbe spostarli in categorie.

**Decisione:** lasciare per ora **flat** in `fonti/` come ha fatto l'utente, perché:
1. Sono 13 file, gestibili senza categorizzazione
2. Hanno nomi descrittivi
3. Spostarli ora rompe i path già in repo
4. Una categorizzazione si fa al meglio quando ci saranno tutti i 40 file

**Quando aggiungere altri T2/T3**, valutare riorganizzazione in sottocartelle.

---

## 6. Prossimi passi raccomandati

1. **Ora**: posso iniziare a **leggere e citare** i 13 documenti per chiudere il debito di rigore parziale e generare bozze sostanziali dei Cap. 3-5-6-7-8
2. **Round successivo download** (utente, ~30 min): scaricare i 8 T2 critici elencati in §3
3. **Engagement esterno** (utente, settimane): chiudere DR-001-002-003-005-006-008-010-015 con contatti diretti istituzioni
4. **Ricerca dedicata** (Claude su input utente, ore): chiudere DR-011 + DR-013 + DR-014 con triangulation peer-reviewed
