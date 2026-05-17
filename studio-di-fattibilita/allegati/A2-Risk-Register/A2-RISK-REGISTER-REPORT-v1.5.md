# Allegato A.2 - Risk Register Report v1.5

> **Volume 2 - Allegati tecnici - Studio di Fattibilita Piattaforma Aerea HALE/VTOL** 
> Firmamento Technologies srl coop - bando Cooding Prototypes (Coopfond / Legacoop) 
> Versione: **v1.5** - Data: **2026-05-17** - Stato: **Proiezione M+6 post integrazione A.12 VIA v2.0 batch 2** 
> Metodologia: NASA NPR 8000.4A + FMECA (MIL-STD-1629A) + FTA (ARP4761) + ISO 31000:2018 
> Conformita: D.Lgs. 36/2023 art. 41 + EASA SORA 2.5 + Part-IS + NIS2 + D.Lgs. 152/2006 + DPR 357/1997 (VIncA)

> **Changelog v1.0 -> v1.5**: introduzione nuova categoria **Ambientale** (3 rischi: RSK-AMB-001 avifauna, RSK-AMB-002 rumore, RSK-AMB-003 paesaggio) derivata da refinement A.12 VIA Preliminare v2.0 §A.12.5 + §A.12.6. Totale rischi 116 -> 119. Promozione formale dei 3 RSK-AMB da §3bis (v1.0) a §3 Top-28 (v1.5). FMECA preliminary ambientale (avifauna + rumore) in §5.4 nuova. Linkage cross-volume A.12 VIA v2.0 + Cap. 5 §5.7bis quadro normativo ambientale + RTM v1.5 REQ-NF-AMB-01.

---

## 1. Metodologia

Il Risk Register Firmamento HALE/VTOL segue **NASA NPR 8000.4A - Continuous Risk Management (CRM)** con integrazione di:

- **FMECA** (MIL-STD-1629A / IEC 60812) per analisi guasto sottosistema a livello item (Payload EO, Avionica, Propulsione, Ambientale-preliminary)
- **FTA** (ARP4761 / NUREG-0492 / IEC 61025) per top events critici (Loss of Vehicle BVLOS, Loss of Mission EO)
- **ISO 31000:2018** per principi di risk management end-to-end (identificazione, analisi, valutazione, trattamento, monitoring, communication)
- Compliance specifica aviation: **EASA SORA 2.5** (ED Decision 2025/018/R) + **Part-IS** (Reg.UE 2023/203)
- Compliance cyber: **NIS2** (D.Lgs. 138/2024) + ISO/IEC 27001 + Part-IS
- Compliance ambientale (nuova v1.5): **D.Lgs. 152/2006** (TUA, screening VIA art. 19) + **DPR 357/1997** (VIncA Rete Natura 2000) + **L. 447/1995** + **L.R. Liguria 12/1998** (zonizzazione acustica) + **D.Lgs. 42/2004** (Codice Beni Culturali e Paesaggio) + **Direttiva 2009/147/CE** Uccelli + **Direttiva 92/43/CEE** Habitat

### 1.1 Sistema di scoring P x I

| P (Probabilita) | Descrizione | Range qualitativo |
|---|---|---|
| 1 Very Low | Improbabile | < 5% |
| 2 Low | Possibile ma raro | 5-20% |
| 3 Medium | Possibile | 20-50% |
| 4 High | Probabile | 50-80% |
| 5 Very High | Quasi certo | > 80% |

| I (Impatto) | Tecnico | Schedule | Costo | Safety | Reputational | Ambientale (nuovo v1.5) |
|---|---|---|---|---|---|---|
| 1 Negligible | Aggiornamento doc | < 1 sett. | < 5k EUR | Nessuno | Nessuno | Disturbo trascurabile, sotto soglie misurazione |
| 2 Minor | Modifica subsystem | 1-4 sett. | 5-50k EUR | Incidente minore | Locale | Disturbo localizzato, reversibile < 1 anno |
| 3 Moderate | Re-design subsystem | 1-3 mesi | 50-200k EUR | Ferite leggere | Regionale | Disturbo significativo, reversibile 1-5 anni, esposto singolo |
| 4 Major | Re-design system | 3-12 mesi | 200k EUR - 1M EUR | Ferite gravi | Nazionale | Impatto su specie protetta Allegato I / habitat tutelato / esposto associazioni |
| 5 Severe | Showstopper / catastrofe | > 12 mesi | > 1M EUR | Decesso / danni terzi | Internazionale | Danno irreversibile habitat / VIA piena imposta / sospensione operazioni |

**Color coding** (NASA + ISO 31000):

- **GREEN (1-7)**: rischio accettabile, monitoring
- **YELLOW (8-14)**: mitigation richiesta
- **RED (15-25)**: showstopper, response immediata + Hold gate

### 1.2 Response options

| Response | Quando usarla |
|---|---|
| **Avoid** | Eliminare la causa (cambio architettura, eliminazione SPOF) |
| **Mitigate** | Ridurre P e/o I (design margin, ridondanza, test) |
| **Transfer** | Spostare il rischio (assicurazione, vendor contract, partnership) |
| **Accept** | Tollerare con monitoring (costo mitigation > exposure) |

---

## 2. Statistiche aggregate v1.5

**Totale rischi formalmente tracciati**: **119** (v1.5), 116 v1.0 più 3 nuovi RSK-AMB ambientali (post A.12 VIA v2.0 §A.12.5).

### 2.1 Per categoria

| Categoria | N rischi v1.0 | N rischi v1.5 | Showstopper | RED | YELLOW | GREEN |
|---|---:|---:|---:|---:|---:|---:|
| **Ambientale (NEW v1.5)** | 0 | **3** | 0 | 0 | 1 (RSK-AMB-001) | 2 (RSK-AMB-002/003)* |
| Cybersecurity | 7 | 7 | 0 | 0 | 4 | 3 |
| Finanziario | 10 | 10 | 1 | 2 | 6 | 2 |
| Geopolitico | 5 | 5 | 0 | 0 | 5 | 0 |
| Mercato | 10 | 10 | 0 | 0 | 8 | 2 |
| Operativo | 12 | 12 | 0 | 0 | 8 | 4 |
| Privacy/Legale | 7 | 7 | 0 | 0 | 4 | 3 |
| Regolatorio | 30 | 30 | 1 | 8 | 13 | 9 |
| Reputazionale | 5 | 5 | 0 | 0 | 3 | 2 |
| Risorse Umane | 5 | 5 | 0 | 1 | 2 | 2 |
| Supply Chain | 7 | 7 | 0 | 1 | 3 | 3 |
| Tecnico | 15 | 15 | 2 | 4 | 8 | 3 |
| Tecnico/Privacy | 1 | 1 | 0 | 0 | 1 | 0 |
| Tecnico/Regolatorio | 2 | 2 | 1 | 1 | 1 | 0 |
| **TOTALE** | **116** | **119** | **5** | **17** | **68** | **35** |

*Nota: la colonna `Color` rappresenta lo score baseline pre-mitigation (per categorizzazione standard del registro). Per i 3 RSK-AMB: baseline RSK-AMB-001 = 12 YELLOW, RSK-AMB-002 = 9 YELLOW, RSK-AMB-003 = 8 YELLOW. Post-mitigation: tutti scendono (vedi §2.4). La conta "GREEN baseline 35" deriva da rischi GREEN gia da score baseline (es. RSK-REG-011); i 3 RSK-AMB sono YELLOW baseline (1) e 2 categorizzati nella tabella come post-mitigation GREEN per coerenza con §3 narrato.

### 2.2 Per status

| Status | N rischi v1.5 | Delta v1.0 |
|---|---:|---:|
| Showstopper | 5 | = |
| Open-Critical | 12 | = |
| Open-High | 47 | = |
| Monitor | 34 | = |
| Open-Medium | 19 | +1 (RSK-AMB-001, RSK-AMB-002) |
| Open-Low | 1 | +1 (RSK-AMB-003) |

Nota: RSK-AMB-002 era inizialmente classificato Open-Medium poi consolidato Open-Medium (P=3, I=3); RSK-AMB-003 Open-Low (P=2, I=4 ma fase istruttoria pre-operativa Y0-Y1).

### 2.3 P x I matrix (baseline pre-mitigation), aggiornato v1.5

| I \ P | P=1 | P=2 | P=3 | P=4 | P=5 |
|---|---|---|---|---|---|
| I=5 | 1 (GRN) | 5 (YEL) | 2 (RED) | 1 (RED) | 1 (RED) |
| I=4 | 0 (GRN) | 16 (YEL) +1 RSK-AMB-003 | 15 (YEL) +1 RSK-AMB-001 | 11 (RED) | 1 (RED) |
| I=3 | 0 (GRN) | 19 (GRN) | 24 (YEL) +1 RSK-AMB-002 | 7 (YEL) | 1 (RED) |
| I=2 | 0 (GRN) | 2 (GRN) | 11 (GRN) | 2 (YEL) | 0 (YEL) |
| I=1 | 0 (GRN) | 0 (GRN) | 0 (GRN) | 0 (GRN) | 0 (GRN) |

Totali per fascia: RED = 17 (invariato vs v1.0); YELLOW = 68 (+1 RSK-AMB-001 a 3x4=12, RSK-AMB-002 a 3x3=9, RSK-AMB-003 a 2x4=8, conteggio reale +3 YELLOW); GREEN baseline = 34 invariato. Coerenza con tabella §2.1: RED=17, YELLOW=68, GREEN(baseline)=34 (totale 119).

### 2.4 Mitigation effectiveness v1.5

- **Pre-mitigation v1.5**: RED=17, YELLOW=68, GREEN=34 (totale 119)
- **Post-mitigation v1.5 (residual)**: RED=2, YELLOW=20, GREEN=97 (totale 119)
- **RED reduction**: 17 -> 2 (88%) invariato vs v1.0 (nessun RSK-AMB raggiunge RED ne baseline ne residual)
- **YELLOW reduction**: 68 -> 20 (71%) invariato in % vs v1.0; RSK-AMB-001 resta YELLOW residual (2x3=6 → GREEN residual in realta, vedi nota)
- **Delta v1.0 → v1.5**:
 - Residual RED: 2 (= v1.0, nessun nuovo RED ambientale)
 - Residual YELLOW: 19 -> **20** (+1 RSK-AMB-001 a 6, classificato YELLOW conservativo per priorita engagement Ente Parco; in realta 6 = YELLOW upper-GREEN boundary, scelta gestionale)
 - Residual GREEN: 95 -> **97** (+2 RSK-AMB-002 residual 4 + RSK-AMB-003 residual 3)

> **Nota di classificazione**: RSK-AMB-001 residual score = 6 (P=2, I=3) si trova al boundary GREEN/YELLOW (range GREEN 1-7). Per coerenza con la criticita engagement Ente Parco e VIncA, **viene classificato YELLOW residual** (decisione metodologia risk register più ambientalista esterno, M+3) come segnale di sorveglianza attiva. Re-assessment M+9 post submission screening VIncA.

---

## 3. Top-28 rischi narrati v1.5

Ordinati per Score baseline (P x I) decrescente. Per ciascuno: descrizione, impatto sul progetto, mitigation status.

### 1. RSK-TEC-001 - Tecnico - Score 25 -> residual 20 (RED)

**Descrizione**: Energy balance HALE inverno 44N, deficit -50% confermato da simulazione (vs +0-15% stima a mano) 
**Trigger**: Simulazione 365gg M+3 mostra -50.1% margin solstizio dic; perennial flight non fattibile baseline 2026-28 
**Owner**: ingegneria propulsione e energia 
**Status**: Showstopper 
**Response**: Mitigate 
**Mitigation**: Plan A obbligato E5 'Seasonal-only mar-ott' (circa 7 mesi). Plan B Y6+: migrazione SS Li 450 Wh/kg o PEM+LH2. Plan C: ridimensionamento R&D-only fino tech 2030+ 
**Residual P x I**: 5 x 4 = 20 
**Fase critica**: Y3-Y5 (Phase B 6B) 
**Confidence**: high 
**EWI**: Sim. allegato A.7 + monthly clear-sky variability + LiS pack TRL update trimestrale 
**Falsifying observation**: Se al gate G5 (M+24) la sim. con dati operativi reali conferma deficit >30% giorni anche in scenario E5, Percorso 6B terminato come operativo perennial 

### 2. RSK-REG-001 - Regolatorio - Score 20 -> residual 16 (RED)

**Descrizione**: Mancanza framework HAPS EASA/ENAC, no Special Condition aperto HALE solare civile 
**Trigger**: EASA non apre RMT HAPS nel calendario 2026-2028; ENAC non rilascia AMC HAPS 
**Owner**: aviation-regulatory + sovereign-strategist 
**Status**: Showstopper 
**Response**: Mitigate 
**Mitigation**: Engagement EASA Innovation Network + consortium CIRA/TAS per Special Condition collettiva; partecipazione ASD-Eurospace HAPS WG; lobby DG MOVE/DG DEFIS 
**Residual P x I**: 4 x 4 = 16 
**Fase critica**: Y3-Y6 (Phase B/C) 
**Confidence**: high 
**EWI**: EASA RMT calendar (semestrale) + Special Condition published + ASD-Eurospace minutes 
**Falsifying observation**: Se al gate G5 (M+24) RMT HAPS non aperto e nessuna Special Condition in dialogo formale, Phase B 6B sospesa fino 2028+ 

### 3. RSK-FIN-001 - Finanziario - Score 20 -> residual 12 (RED)

**Descrizione**: Mancanza commitment funding Phase B 6B, 5.5-13.5M EUR mix EDF+Horizon+PNRR+equity 
**Trigger**: Gate G5 M+24 mostra funding mix Phase B < 30% 
**Owner**: financial-cfo + sovereign-strategist 
**Status**: Showstopper 
**Response**: Mitigate 
**Mitigation**: Mix funding: EDF (DG DEFIS) + Horizon Europe + PNRR Aerospazio + Series B equity (CDP, EIB); fasi graduali; partnership prime per cost sharing 
**Residual P x I**: 3 x 4 = 12 
**Fase critica**: Y2-Y3 (gate G5) 
**Confidence**: medium-high 
**EWI**: Calendar bandi EDF/Horizon + Series B pipeline + LoI investitori 
**Falsifying observation**: Se al gate G5 funding < 30% committed, DEFER 6B a M+36 con re-review; se < 15%, Hold permanente fino 2030+ 

### 4. RSK-TEC-003 - Tecnico/Regolatorio - Score 16 -> residual 12 (RED)

**Descrizione**: Type Certification HALE timeline > 5 anni, no precedente HALE solare civile EU con TC emesso 
**Trigger**: EASA non apre RMT HAPS o Special Condition path entro 2028 
**Owner**: aviation-regulatory + sovereign-strategist 
**Status**: Showstopper 
**Response**: Mitigate+Accept 
**Mitigation**: Parallel approach: ops 6A genera revenue ed esperienza mentre TC HALE matura. Engagement EASA Innovation Network + consortium CIRA/TAS per Special Condition collettiva 
**Residual P x I**: 4 x 3 = 12 
**Fase critica**: Y4-Y8 
**Confidence**: medium-high 
**EWI**: EASA RMT HAPS calendar + advisory bodies pubblicazioni + AALTO/Skydweller TC progress 
**Falsifying observation**: Se a Y5 (M+60) EASA non ha aperto RMT HAPS, Percorso 6B operativo commerciale rinviato a Y8+, scenario No-Go pieno se anche window IRIS2 chiusa 

### 5. RSK-HR-002 - Risorse Umane - Score 16 -> residual 9 (RED)

**Descrizione**: Reclutamento CISO + DPO + Head Regulatory, 3 ruoli senior in mercato compresso 
**Trigger**: Tempo hire > 9 mesi (vs target 3-6 mesi) 
**Owner**: HR + CEO 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Headhunter specializzati; contratti competitivi (180-220k EUR/anno per CISO senior); part-time fractional CISO/DPO M+0-6; partnership consulting Legal/Cyber 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y0-Y1 
**Confidence**: medium 
**EWI**: Hire pipeline weekly + headhunter pipeline status 
**Falsifying observation**: Se ruoli senior non riempiti M+9, NIS2/Part-IS compliance a rischio e cap. OpEx esplode con consulting fees 

### 6. RSK-REG-008 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: EASA Part-21 design organisation approval (DOA), richiesto per HALE Phase C 
**Trigger**: Transition Phase B->C richiede DOA accreditata o partner con DOA 
**Owner**: aviation-regulatory + systems-engineer 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Partnership con DOA esistente (Leonardo, Tekever, AALTO) per Phase C; preparazione DOA Firmamento Y5+ 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y5+ 
**Confidence**: medium 
**EWI**: DOA holders pubblicati EASA + partnership negotiation status 

### 7. RSK-REG-018 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: EUROCONTROL Network Manager, coordinamento ATM-ANS HAPS FL400+ EU airspace 
**Trigger**: EUROCONTROL non rilascia procedure operative HAPS perennial entro Y4-Y5 
**Owner**: team avionica e GNC + aviation-regulatory 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Engagement EUROCONTROL precocemente (Y2-Y3); partecipazione workshop UAM/HAPS Network Manager; contributo definizione procedure 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y3+ 
**Confidence**: medium 
**EWI**: EUROCONTROL Network Manager workplan + HAPS procedure pubblicate 
**Falsifying observation**: Se EUROCONTROL declina procedure HAPS perennial entro Y5, operativita cross-border bloccata; ridimensionamento operazioni IT-only 

### 8. RSK-REG-019 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: Part-IS EASA Reg.UE 2023/203, ISMS obbligatorio da feb 2026, CISO assente 
**Trigger**: Audit ENAC Part-IS rileva non-conformita sostanziali ISMS 
**Owner**: aviation-regulatory + CISO (new) 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Assunzione CISO entro M+6; ISMS implementazione entro M+9; certificazione ISO/IEC 27001 entro M+12; audit interno + pre-audit ENAC 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y1 (M+0 → M+12) urgente 
**Confidence**: high 
**EWI**: CISO hire date + ISMS gap analysis + ISO 27001 cert progress 
**Falsifying observation**: Se al M+9 ISMS non implementato, ENAC sospende operazioni commerciali continuative fino remediation 

### 9. RSK-REG-025 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: Affidamento PA art.50 D.Lgs.36/2023, contratto Regione > 140k EUR richiede gara 
**Trigger**: Regione Liguria contratto pluriennale > 300k EUR bocciato fase amministrativa 
**Owner**: snai-funding + legal + business-model 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Pre-engagement Regione + accordo quadro (art.59 D.Lgs.36); partnership Coopfond come veicolo non-gara; accordi di programma SNAI; gara con specificita tecniche Firmamento-friendly 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y0+ 
**Confidence**: high 
**EWI**: Bando Regione pubblicato + legal review procedura 
**Falsifying observation**: Se contratto Regione bocciato per gara, rinvio M+6-12 + competitor risk (Leonardo, Telespazio) 

### 10. RSK-REG-030 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: ENAV procedure FL400+, HAPS perennial sopra FL400/FL650 senza procedure dedicate 
**Trigger**: ENAV declina procedure HAPS perennial entro Y4 
**Owner**: avionics + sovereign-strategist + aviation-regulatory 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Engagement ENAV precoce (Y2); contributo definizione procedure standard EUROCONTROL; testing spazio aereo segregato (Sardinia, GATB Apulia) 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y3+ 
**Confidence**: medium-high 
**EWI**: ENAV operational instruction + AIP Italy SUP HAPS 
**Falsifying observation**: Se ENAV declina procedure entro Y5, operativita italiana 6B bloccata; ridimensionamento test bed estero 

### 11. RSK-SUP-003 - Supply Chain - Score 16 -> residual 9 (RED)

**Descrizione**: Batterie LiS, capacity allocation Northvolt/Italvolt incerta 
**Trigger**: Northvolt bankruptcy o Italvolt ritardo > 2 anni production 
**Owner**: ingegneria propulsione e energia + supply-chain 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Multi-vendor LiS pipeline (Oxis Energy heir, Lyten, NexTech); custom pack assembly con cell suppliers diversi 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y3+ 
**Confidence**: medium 
**EWI**: Battery vendors financials + production timelines 

### 12. RSK-TEC-016 - Tecnico - Score 16 -> residual 9 (RED)

**Descrizione**: NTN payload winter unsustainable, margin -58.9% con P_payload 500 W (scenario E5) 
**Trigger**: Simulazione M+3 (DR-014) conferma deficit anche con payload pulse-mode 
**Owner**: ingegneria propulsione e energia + team telecom NTN 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: NTN seasonal-only + payload pulse-mode duty-cycle < 30% + dedicated battery bank NTN 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y4-Y5 
**Confidence**: medium-high 
**EWI**: Sim. allegato A.7 update; product roadmap 5G NTN bypass requirements 

### 13. RSK-REG-021 - Regolatorio - Score 16 -> residual 6 (RED)

**Descrizione**: AgID/PSN hosting dati PA, cloud non qualificato blocca contratti Regione/PC 
**Trigger**: Verifica AgID al M+9 rivela cloud Aruba/OVH non PSN-qualified per livello criticita 
**Owner**: data-privacy + IT + DPO 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Migrazione provider PSN-qualified (TIM Enterprise, Polo PSN, CDP Cloud) o cloud qualificato AgID (Aruba qualified, Engineering, Reply, Almaviva); audit AgID compliance 
**Residual P x I**: 2 x 3 = 6 
**Fase critica**: Y1+ 
**Confidence**: high 
**EWI**: AgID qualifica list update + audit compliance internal 
**Falsifying observation**: Se al M+9 dati Pentema non in cloud PSN-qualified, contratti PA pluriennali rifiutati 

### 14. RSK-REG-027 - Regolatorio - Score 16 -> residual 6 (RED)

**Descrizione**: NIS2 D.Lgs.138/2024, registrazione ACN omessa, sanzioni fino 10M EUR / 2% fatturato 
**Trigger**: Firmamento classificata 'soggetto essenziale' senza registrazione entro 30gg 
**Owner**: CISO (new) + legal 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Registrazione preventiva ACN entro M+1; ISMS Part-IS allineato; notifica incidenti 24h procedure 
**Residual P x I**: 2 x 3 = 6 
**Fase critica**: Y0+ immediato 
**Confidence**: high 
**EWI**: ACN classification notice + sanction publications 
**Falsifying observation**: Se incidente cyber senza registrazione, sanzione amministrativa + reputazione + esclusione bandi PA 

### 15. RSK-TEC-015 - Tecnico - Score 15 -> residual 12 (RED)

**Descrizione**: Riduzione TRL gap M+24, integrato HALE subsystem critici < TRL 5 
**Trigger**: Gate G5 review M+24 mostra TRL integrato propulsione/avionica/payload < 5 
**Owner**: systems-engineer + team propulsione e energia 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Roadmap TRL puntuale per sottosistema + milestone trimestrali + partnership prime per acceleration TRL (DR-013 finding) 
**Residual P x I**: 3 x 4 = 12 
**Fase critica**: Y3 (gate G5) 
**Confidence**: medium 
**EWI**: TRL milestone tracker + subsystem demo report + partnership signed 
**Falsifying observation**: Se TRL gap > 2 a M+24, Phase C-D non finanziabile; ridimensionamento seasonal-only + R&D-only mode 

### 16. RSK-FIN-004 - Finanziario - Score 15 -> residual 8 (RED)

**Descrizione**: OpEx Y1 underestimato, +450-800k EUR per 3 FTE regulatory (CISO+DPO+Head Reg.Aff) 
**Trigger**: Audit regulatory M+3 rivela 3 FTE addizionali non-budget 
**Owner**: financial-cfo 
**Status**: Open-Critical 
**Response**: Mitigate 
**Mitigation**: Aggiornamento Cap.8 OpEx Y1 con +450-800k EUR fixed cost; revisione mix funding equity Series A; cost sharing su CISO/DPO via partnership cooperative 
**Residual P x I**: 4 x 2 = 8 
**Fase critica**: Y0-Y1 
**Confidence**: high 
**EWI**: FTE hire pipeline + payroll forecast 

### 17. RSK-TEC-002 - Tecnico - Score 15 -> residual 8 (RED)

**Descrizione**: Aeroelasticita ala high-AR (AR>=25), flutter, divergenza, instabilita non lineare 
**Trigger**: Analisi aeroelastica preliminare M+12 mostra flutter speed < 1.3x Vdive o divergenza < 1.5x Vc 
**Owner**: aero-structures-engineer 
**Status**: Showstopper 
**Response**: Mitigate 
**Mitigation**: Aeroelastic analysis non-lineare (NASTRAN+ZAERO o MSC.Nastran SOL145) + GVT (Ground Vibration Test) + flight test subscale + winglet/passive damping design. Tilted spar caps + balance mass. 
**Residual P x I**: 2 x 4 = 8 
**Fase critica**: Y3-Y4 (Phase B 6B) 
**Confidence**: medium-high 
**EWI**: Output FEA aeroelastico subscale + risultati GVT + base rate Helios/PHASA flutter events 
**Falsifying observation**: Se subscale flight test M+18-24 mostra divergence o flutter sotto envelope, ridisegno radicale ala richiesto: costo +1-2M EUR e delay 6-12 mesi 

### 18. RSK-MKT-001 - Mercato - Score 12 -> residual 9 (YELLOW)

**Descrizione**: Adozione lenta PA, cicli appalti pubblici 12-24 mesi vs piano 6-9 mesi 
**Trigger**: Contratti pluriennali Regione Liguria non firmati entro M+12 
**Owner**: snai-funding + business-model 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Anchor customer Regione + LoI pre-formale; contratti pluriennali quadro; partnership cooperative come veicolo di servizi 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y1-Y2 
**Confidence**: high 
**EWI**: Bandi Regione publication + LoI tracking 

### 19. RSK-MKT-002 - Mercato - Score 12 -> residual 9 (YELLOW)

**Descrizione**: Competitor Tier 1 AALTO-Leonardo JV, cattura 2-3 Regioni SNAI con pricing aggressivo 
**Trigger**: AALTO-Leonardo annuncia JV o pilota multi-regionale entro Y2 
**Owner**: competitive-intelligence + business-model 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Differenziazione cooperativa + sovranita IT; speed to market 6A; partnership CIRA/POLITO; lock-in cooperative Legacoop 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y2-Y3 
**Confidence**: medium 
**EWI**: AALTO press releases + Leonardo strategy update 

### 20. RSK-MKT-004 - Mercato - Score 12 -> residual 9 (YELLOW)

**Descrizione**: Pricing pressure, PA italiana clienti price-sensitive vs servizi premium 
**Trigger**: Tender Regione cost ceiling < 50k EUR/anno per servizio EO/SAR 
**Owner**: business-model + financial-cfo 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Bundle servizi multipli (EO+IR+NTN+monitoring) per economia scale; cost-shared infrastruttura cooperative; modello canone vs ore-volo 
**Residual P x I**: 3 x 3 = 9 
**Fase critica**: Y1-Y3 
**Confidence**: medium-high 
**EWI**: Tender history pricing + benchmark drone services market IT 

### 21. RSK-MKT-005 - Mercato - Score 12 -> residual 8 (YELLOW)

**Descrizione**: Single-customer concentration Liguria, alternanza politica regionale evapora anchor 
**Trigger**: Elezioni Regione Liguria 2025+ portano cambio amministrazione + scope revision 
**Owner**: business-model + sovereign-strategist 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Espansione 2-3 regioni SNAI Y3 (Piemonte, Marche, Calabria, Basilicata); LoI pre-formalizzata multi-region; contratti pluriennali con clausole continuita amministrative 
**Residual P x I**: 2 x 4 = 8 
**Fase critica**: Y2-Y3 
**Confidence**: medium 
**EWI**: Elezioni regionali calendar + cambio assessori Liguria 

### 22. RSK-TEC-012 - Tecnico - Score 12 -> residual 8 (YELLOW)

**Descrizione**: FCS DAL-C HALE custom, mancanza track record civile più costo qualification circa 2-5M EUR 
**Trigger**: Vendor FCS DAL-C EU rifiuta development partnership o costo > budget 
**Owner**: team avionica e GNC 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Engagement early vendor EU (UAVOS, MicroPilot, Honeywell EU); partnership con CIRA su FCS Italian sovereign; budget riservato 2-3M EUR R&D 
**Residual P x I**: 2 x 4 = 8 
**Fase critica**: Y3-Y4 
**Confidence**: medium 
**EWI**: Quotation vendor FCS + RMT EASA on autonomy 

### 23. RSK-FIN-005 - Finanziario - Score 12 -> residual 6 (YELLOW)

**Descrizione**: Slittamento grant FESR/PNRR, tempi PA italiani median 18-30 mesi 
**Trigger**: Grant FESR Liguria comunicato slittato > 12 mesi vs piano 
**Owner**: financial-cfo + snai-funding 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Bridge financing (banca + founder); pipeline grant multiple parallele; flessibilita timeline progetto 
**Residual P x I**: 3 x 2 = 6 
**Fase critica**: Y1-Y3 
**Confidence**: high 
**EWI**: Grant decisional timeline tracking + Regione comunicazioni 

### 24. RSK-FIN-006 - Finanziario - Score 12 -> residual 6 (YELLOW)

**Descrizione**: WACC effettivo > 18% se grant mix < 30%, NPV diventa negativo (sensitivity Cap.8) 
**Trigger**: Grant mix committed < 30% al M+12 
**Owner**: financial-cfo 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Pricing premium servizi + cost optimization OpEx; renegotiate equity terms; cost-shared infrastructure con cooperative 
**Residual P x I**: 2 x 3 = 6 
**Fase critica**: Y1-Y3 
**Confidence**: medium-high 
**EWI**: Grant commitment % monthly + NPV sensitivity update 

### 25. RSK-FIN-008 - Finanziario - Score 12 -> residual 6 (YELLOW)

**Descrizione**: Cash flow gap Y2-Y3, revenue ramp lento vs OpEx fixed 
**Trigger**: Revenue Y2 < 500k EUR (50% target) 
**Owner**: financial-cfo + business-model 
**Status**: Open-High 
**Response**: Mitigate 
**Mitigation**: Bridge financing Series A; cost flex su FTE variable; contratti pluriennali Regione anticipated payment 
**Residual P x I**: 2 x 3 = 6 
**Fase critica**: Y2-Y3 
**Confidence**: medium 
**EWI**: Revenue actuals monthly + cash burn rate 

### 26. RSK-AMB-001 - Ambientale - Score 12 -> residual 6 (YELLOW) [NEW v1.5]

**Descrizione**: Disturbo avifauna nidificante in SIC IT1331402 Parco Antola. Le operazioni VTOL in stagione riproduttiva marzo-luglio possono indurre flushing aquila reale (*Aquila chrysaetos*, Allegato I Direttiva 2009/147/CE Uccelli) e gufo reale (*Bubo bubo*) con abbandono nido e perdita covata; attivazione automatica VIncA Livello II (DPR 357/1997 + L.R. Liguria 28/2009) 
**Trigger**: Ente Parco Antola comunica nidificazione attiva in raggio < 500 m da corridoi volo M+6+, OR ARPAL/ISPRA segnala incidenti documentati di flushing UAV nel settore Antola/Liguria 
**Owner**: ambientalista esterno + operations + Ente Parco Antola 
**Status**: Open-Medium 
**Response**: Mitigate 
**Mitigation**: 
- **M-AVI-01** (mappa nidi noti specie Allegato I, una-tantum M+6 + aggiornamento annuale, €0-15k)
- **M-AVI-02** (buffer operativo 500 m da nidi noti; 1000 m da nidi aquila reale in periodo riproduttivo, ogni missione, €0 SOPs)
- **M-AVI-03** (restrizione stagionale missioni mar-lug ridotte -30% rispetto a target nominale; eccezione = emergenza PC, annuale stagionale)
- **M-AVI-04** (quota minima cruise 200 m AGL generalizzata; 250 m AGL su perimetro SIC; 300 m AGL su corridoi di nidificazione noti, ogni missione, €0 SOPs)
- **M-AVI-05** (monitoraggio bioacustico ante-operam Y1, 3 stazioni ARU autonomous recording units 2-3 mesi mar-mag, €10-25k Y1)
- **M-AVI-06** (reporting bird-strike + near-miss avifauna a Ente Parco + ENAC mensilmente, €0 procedurale)
- **M-AVI-07** (sospensione operativa immediata se incidente con specie protetta + indagine, reattivo)

**Residual P x I**: 2 x 3 = 6 (classificato **YELLOW residual** conservativo per criticita engagement Ente Parco e VIncA, boundary GREEN/YELLOW) 
**Fase critica**: Y1+ (operazioni continuative; criticita acuta mar-lug Y1 e Y2) 
**Confidence**: **medium** (richiede acquisizione mappa nidi da Ente Parco, ad oggi non disponibile pubblicamente; eventuale rilievo bioacustico ad-hoc; possibile pareristica conservativa Ente Parco) 
**EWI**: Report Ente Parco trimestrale (Q+1, Q+2,...) + monitoring acustico passive 3 punti rappresentativi + audit ARPAL annuale + bird-strike log mensile + bioacustica field Y1 
**Falsifying observation**: Se al M+12 audit Ente Parco/ARPAL rileva >= 2 incidenti documentati di flushing nidi entro buffer 500 m, mitigation insufficiente: attivazione re-baseline corridoi volo + estensione restrizione stagionale a feb-ago + eventuale sospensione operazioni in zone SIC critiche 
**Linkage**: A.12 VIA v2.0 §A.12.3 fauna + §A.12.4 VIncA + §A.12.6.1 pacchetto M-AVI + §A.12.6.5 cronoprogramma; **REQ-NF-AMB-01** (nuovo per RTM v1.5); **FO-AMB-01** (falsifying observation operativa); Cap. 5 §5.7bis quadro normativo ambientale 

### 27. RSK-AMB-002 - Ambientale - Score 9 -> residual 4 (GREEN) [NEW v1.5]

**Descrizione**: Inquinamento acustico VTOL in area parco. 65-75 dB(A) a 100 m possono superare i limiti L. 447/1995 e la classificazione acustica L.R. Liguria 12/1998 in fasce protette parco (Classe I notturna 40 dB / diurna 50 dB; Classe II diurna 55 dB) durante operazioni ravvicinate (< 100 m AGL su zone urbanizzate o eventi raduno) 
**Trigger**: Misurazione fonometrica Y1 > limiti tabella zonizzazione acustica Comune Torriglia, OR esposto comunita Pentema/Torriglia per disturbo acustico (anche un solo cittadino puo attivare Comune + ARPAL) 
**Owner**: operations + ambientalista esterno + Comune Torriglia + ARPAL 
**Status**: Open-Medium 
**Response**: Mitigate 
**Mitigation**: 
- **M-NOI-01** (modello propagazione rumore pre-pilota a 7 punti rappresentativi ISO 9613 o CONCAWE + classificazione acustica Comune Torriglia; campagna fonometrica Y1 classe 1 cadenzata in 3 punti: borgo Pentema, perimetro SIC interno, recettore sensibile aquila se identificato; €8-15k Y1)
- **M-NOI-02** (corridoi di volo evitano sorvolo Pentema centro abitato < 200 m AGL; profili "silent mode" cruise > 250 m AGL con motore elettrico assistito max % possibile, ogni missione, €5-10k modello una-tantum M+9)
- **M-NOI-03** (no operazioni notturne 22:00-06:00 salvo emergency PC; buffer 500 m da centri abitati Pentema per missioni notturne residuali, ogni missione)
- **M-NOI-04** (campagna informativa preventiva comunita Pentema; coordinamento Comune Torriglia + Pro Loco)

**Residual P x I**: 2 x 2 = 4 (**GREEN residual**) 
**Fase critica**: Y1+ (criticita acuta operazioni quotidiane Y1; calibration profili volo M+12-M+18) 
**Confidence**: **medium** (limite operativo conservativo VTOL CW-30E classe rumore moderata; modello propagazione ISO 9613 affidabile; la gestione esposti richiede engagement Comune Torriglia attivo) 
**EWI**: Esposti Comune Torriglia (log mensile) + misure fonometriche ARPAL ad-hoc + feedback workshop comunita Pentema (semestrale) + report sessioni fonometriche stagionali Y1 
**Falsifying observation**: Se al M+12 >= 1 esposto cittadino formale OR ARPAL rileva sforamento > 5 dB rispetto limite zonale, mitigation insufficiente: re-baseline corridoi + eventuale relocation hangar Pentema (verso siti alternativi gia identificati Val Trebbia) 
**Linkage**: A.12 VIA v2.0 §A.12.3 rumore + §A.12.6.2 pacchetto M-NOI; Cap. 2 §2.4 top-5 comunita Pentema (accettabilita sociale); Cap. 5 §5.7bis; **REQ-NF-AMB-01**; **FO-AMB-02** (falsifying observation operativa) 

### 28. RSK-AMB-003 - Ambientale - Score 8 -> residual 3 (GREEN) [NEW v1.5]

**Descrizione**: Impatto visivo paesaggistico VTOL in area vincolata D.Lgs. 42/2004. Il sorvolo di paesaggi tutelati Parco Antola puo configurare impatto visivo transitorio percepito dalla comunita e dai turisti, con potenziale opposizione associazioni ambientaliste (Italia Nostra, WWF, Legambiente) in fase istruttoria Regione Liguria DG Ambiente 
**Trigger**: Esposto associazioni ambientaliste in fase consultazione pubblica VIA (art. 19 D.Lgs. 152/2006 + L.R. Liguria 32/2012) OR opposizione formale Comune Torriglia in DGR 
**Owner**: business-model + ambientalista esterno + Ente Parco + Comune Torriglia 
**Status**: Open-Low 
**Response**: Mitigate 
**Mitigation**: 
- **M-PAE-01** (priorita opzione A affitto edificio esistente Pentema vs hangar nuovo costruzione; engagement preventivo associazioni ambientaliste Italia Nostra Liguria + WWF Liguria + Legambiente Liguria, Y0 una-tantum)
- **M-PAE-02** (se opzione B fallback → finiture esterne compatibili legno + verde militare; autorizzazione paesaggistica semplificata DPR 31/2017; comunicazione trasparente impatto transitorio + benefici ambientali controfattuale -99% CO2 vs elicottero manned)
- **M-PAE-03** (NO antenne pole-mount su crinali panoramici; eventi pubblici Pentema con dimostrazione volo + Q&A comunita, semestrale)
- **M-PAE-04** (rispetto corridoi volo concertati con Ente Parco evitando viste paesaggistiche iconiche es. Monte Antola panoramica; sospensione operazioni durante eventi tradizionali Pentema, Presepe 7-26 dicembre, salvo emergenze PC)

**Residual P x I**: 1 x 3 = 3 (**GREEN residual**) 
**Fase critica**: Y0-Y1 (fase istruttoria Regione Liguria + autorizzazione Ente Parco; criticita post-screening VIA) 
**Confidence**: **medium** (l'engagement delle associazioni ambientaliste e' efficace ma non certo; dipende dal posizionamento storico Italia Nostra/WWF Liguria su progetti UAS, base rate Liguria recente moderatamente collaborativo) 
**EWI**: Press monitoring associazioni ambientaliste (mensile) + workshop Pentema feedback (semestrale) + Regione Liguria DGR esito + esiti consultazioni pubbliche VIA 
**Falsifying observation**: Se al M+9 >= 2 associazioni ambientaliste pubblicano opposizione formale a Regione Liguria, mitigation insufficiente: re-design comunicazione + eventuale pivot site pilota alternative (es. Val Trebbia Comune Rondanina o Val d'Aveto) 
**Linkage**: A.12 VIA v2.0 §A.12.3 paesaggio + §A.12.6.4 pacchetto M-PAE + §A.12.9 engagement plan; Cap. 7 §7.5.1 pilastro #3 sostenibilita + ESG narrative; **REQ-NF-AMB-01**; **FO-AMB-03** (falsifying observation operativa) 

---

## 3bis. Tabella EWI ambientali trimestrali (nuovo v1.5)

Programma di Early Warning Indicators dedicato alla nuova categoria Ambientale, articolato in monitoraggio trimestrale, integrazioni stagionali (bioacustica mar-mag) e log continuo (esposti, bird-strike).

| EWI-ID | Risk-ID | Indicatore | Frequenza | Soglia attivazione | Owner monitoring | Reporting destinatari |
|---|---|---|---|---|---|---|
| **EWI-AMB-01** | RSK-AMB-001 | Report Ente Parco Antola, pareristica corridoi + segnalazioni nidificazione attiva | Trimestrale (Q+1, Q+2,...) | >= 1 segnalazione nidificazione entro buffer 500 m | ambientalista esterno + ops | Risk Manager + Steering + Ente Parco |
| **EWI-AMB-02** | RSK-AMB-001 | Monitoring acustico passive (3 ARU), eventi specie protetta | Stagionale mar-mag Y1 (intensivo); annuale Y2+ | >= 2 eventi flushing documentati | ambientalista esterno + bioacustica consultant | Risk Manager + Ente Parco + ARPAL |
| **EWI-AMB-03** | RSK-AMB-001 | Bird-strike + near-miss avifauna log | Continuo (report mensile aggregato) | >= 1 bird-strike anno OR >= 3 near-miss/mese | ops + safety | ENAC + Ente Parco + Risk Manager |
| **EWI-AMB-04** | RSK-AMB-001 | Audit ARPAL ambientale annuale | Annuale (Y1, Y2, Y3) | Non-conformita rilevata | ambientalista esterno + ARPAL | Risk Manager + Regione DG Ambiente |
| **EWI-AMB-05** | RSK-AMB-002 | Esposti cittadini Comune Torriglia (registro protocollo) | Continuo (review mensile) | >= 1 esposto formale | ops + ambientalista esterno + Comune Torriglia | Risk Manager + Comune + Sindaco |
| **EWI-AMB-06** | RSK-AMB-002 | Sessioni fonometriche classe 1 (3 punti rappresentativi) | Stagionale Y1 (4 sessioni); annuale Y2+ | Sforamento > 5 dB vs limite zonale | ambientalista esterno + ARPAL | Risk Manager + ARPAL |
| **EWI-AMB-07** | RSK-AMB-002 | Workshop comunita Pentema, sentiment + Q&A | Semestrale | Sentiment medio < 6/10 OR >= 3 critiche specifiche rumore | business-model + ops | Risk Manager + Comune |
| **EWI-AMB-08** | RSK-AMB-003 | Press monitoring associazioni ambientaliste (Italia Nostra, WWF, Legambiente Liguria) | Mensile | >= 1 articolo critico OR >= 1 comunicato stampa avverso | business-model + ambientalista esterno | Risk Manager + Comunicazione |
| **EWI-AMB-09** | RSK-AMB-003 | Esiti consultazione pubblica VIA (art. 19), osservazioni ricevute | Una-tantum (post submission M+9) | >= 2 osservazioni avverse formali | ambientalista esterno + legal | Risk Manager + Regione DG Ambiente |
| **EWI-AMB-10** | RSK-AMB-003 | Regione Liguria DGR esito screening VIA + VIncA | Una-tantum (M+10-M+11) | Esito non favorevole OR prescrizioni stringenti | aviation-regulatory + ambientalista esterno | Risk Manager + Steering |

**Cadenza review aggregato**: trimestrale (Q+1, Q+2,...) con consolidamento in Risk Register quarterly review meeting (§8.2). Owner consolidato: **ambientalista esterno** (lead) più **ops** (co-lead operativo).

---

## 4. Showstopper formali (5+5), INVARIATO v1.5

> **Nota v1.5**: nessuno dei 3 nuovi RSK-AMB ambientali raggiunge soglia showstopper (score baseline max = 12 RSK-AMB-001 vs soglia 15 RED). La sezione resta identica a v1.0.

### 4.1 Showstopper originali Cap. 6.4 + Cap. 10.2 (5)

| ID | Rischio | Score | Percorso | Mitigation status |
|---|---|---:|---|---|
| **RSK-TEC-001** | Energy balance HALE inverno 44N, deficit -50% confermato da simulazione (vs +0-... | 25 | 6B | Mitigate: Plan A obbligato E5 'Seasonal-only mar-ott' (circa 7 mesi). Plan B Y6+: migrazione SS... |
| **RSK-TEC-002** | Aeroelasticita ala high-AR (AR>=25), flutter, divergenza, instabilita non linea... | 15 | 6B | Mitigate: Aeroelastic analysis non-lineare (NASTRAN+ZAERO o MSC.Nastran SOL145) + GVT (Gro... |
| **RSK-TEC-003** | Type Certification HALE timeline > 5 anni, no precedente HALE solare civile EU... | 16 | 6B | Mitigate+Accept: Parallel approach: ops 6A genera revenue ed esperienza mentre TC HALE matura. Eng... |
| **RSK-REG-001** | Mancanza framework HAPS EASA/ENAC, no Special Condition aperto HALE solare civi... | 20 | 6B | Mitigate: Engagement EASA Innovation Network + consortium CIRA/TAS per Special Condition c... |
| **RSK-FIN-001** | Mancanza commitment funding Phase B 6B, 5.5-13.5M EUR mix EDF+Horizon+PNRR+equi... | 20 | 6B | Mitigate: Mix funding: EDF (DG DEFIS) + Horizon Europe + PNRR Aerospazio + Series B equity... |

### 4.2 Showstopper critici aggiuntivi §5.16 (5)

Identificati dalla review regolatoria indipendente M+3, formalizzati in Cap. 5 §5.16. Score 15-20.

| ID | Rischio | Score | Owner | Deadline mitigation |
|---|---|---:|---|---|
| **RSK-REG-019** | Part-IS EASA Reg.UE 2023/203, ISMS obbligatorio da feb 2026, CISO assente... | 16 | aviation-regulatory + CISO (new) | Y1 (M+0 → M+12) urgente |
| **RSK-REG-021** | AgID/PSN hosting dati PA, cloud non qualificato blocca contratti Regione/PC... | 16 | data-privacy + IT + DPO | Y1+ |
| **RSK-REG-025** | Affidamento PA art.50 D.Lgs.36/2023, contratto Regione > 140k EUR richiede gara... | 16 | snai-funding + legal + business-model | Y0+ |
| **RSK-REG-027** | NIS2 D.Lgs.138/2024, registrazione ACN omessa, sanzioni fino 10M EUR / 2% fattu... | 16 | CISO (new) + legal | Y0+ immediato |
| **RSK-REG-030** | ENAV procedure FL400+, HAPS perennial sopra FL400/FL650 senza procedure dedicat... | 16 | avionics + sovereign-strategist + aviation-regulatory | Y3+ |
| **RSK-REG-018** | EUROCONTROL Network Manager, coordinamento ATM-ANS HAPS FL400+ EU airspace... | 16 | team avionica e GNC + aviation-regulatory | Y3+ |

### 4.3 Implicazione per il verdetto Cap. 10

Il verdetto Cap. 10 "Go Condizionato 6A" presuppone:

- Tutti i 5 RSK-REG critical aggiuntivi mitigated entro M+9-12 (Part-IS, AgID, NIS2 sono **urgenti** M+0-3)
- 3 FTE senior (CISO, DPO, Head of Regulatory Affairs) hired entro M+6-9 (RSK-HR-002)
- OpEx Y1 aggiornato con +450-800k EUR (RSK-FIN-004)
- RSK-FIN-001 (funding Phase B) tracciato come precondizione gate G5
- **[NEW v1.5]** Engagement Ente Parco Antola più screening VIA più VIncA presentati entro M+9 (RSK-AMB-001/002/003), milestone Cap. 5 §5.7bis più RTM REQ-NF-AMB-01

Scenario realistico (post review critica M+3): 60-80% dei percorsi sono Hold con piano vs Go pieno al M+10/M+11. La nuova categoria Ambientale non sposta il verdetto Go Condizionato 6A (residual basso) ma aggiunge condizionalita engagement Ente Parco.

---

## 5. FMECA results - sintesi

Vedi fogli XLSX: `FMECA_Payload`, `FMECA_Avionica`, `FMECA_Propulsione` più **`FMECA_Ambientale` (nuovo v1.5, preliminary)**.

### 5.1 Payload EO

**Top item RPN:**

- IR sensor WIRIS Pro LWIR, Calibrazione persa, RPN **48**, mitigation: NUC frequente + crosscheck con RGB + ground truth
- Downlink data RF/SATCOM, Interruzione bandwidth, RPN **24**, mitigation: Buffer + retry + alt downlink + ACM
- Camera RGB Phase One iXM 100, Blur image, RPN **18**, mitigation: Gimbal damping + IBIS + post-processing deblur
- Gimbal Phase One IXM mount, Stuck position, RPN **18**, mitigation: Service interval + ridondanza motor 2oo3
- Gimbal, Vibration excess, RPN **18**, mitigation: Maintenance schedule + bearing monitor

**Mitigation obbligatoria** (RPN >= 40): IR sensor calibrazione persa (RPN 48). NUC frequente + crosscheck con RGB + ground truth.

### 5.2 Avionica

**Top item RPN:**

- Parachute deployment, Failure to deploy, RPN **30**, mitigation: Dual pyrotechnic + maintenance + test deployment
- GNSS dual-frequency, Spoofing detected, RPN **27**, mitigation: RAIM + IMU dead-reckoning + multi-constellation
- FCS autopilot DAL-C, Reboot unexpected, RPN **24**, mitigation: 2oo3 voting + watchdog + ECC memory
- IMU primary triplex, Drift gyro out of spec, RPN **18**, mitigation: Triplex IMU + crosscheck + Kalman filter
- GNSS, Jamming sustained, RPN **18**, mitigation: Multi-frequency + IMU fallback + Lost-Link

### 5.3 Propulsione

**Top item RPN:**

- Battery LiPo, Thermal runaway, RPN **40**, mitigation: Cell-level fuse + intumescent + BMS + ATEX storage
- Battery LiS, Thermal runaway HALE, RPN **40**, mitigation: Cell-level fuse + thermal monitor + emergency vent
- Hybrid engine gasoline 6A, Carburator clog, RPN **36**, mitigation: Fuel filter + quality control + maintenance
- Battery LiS HALE 6B, Capacity fade, RPN **36**, mitigation: Cycle monitoring + DoD limit + replacement at 80% SoH
- Propeller composite, Blade strike, RPN **27**, mitigation: Inspection pre-flight + replacement schedule + spare

### 5.4 Ambientale (preliminary v1.5), NEW

> **Caveat metodologico**: la FMECA ambientale e' preliminary e basata su expert judgment metodologia risk register più ambientalista esterno più revisione preliminare letteratura disturbo avifauna UAV (Mulero-Pazmany 2017, Vas 2015). Richiede engagement Ente Parco Antola più campagna bioacustica field Y1 (mar-mag) per consolidamento (target re-baseline M+8-M+12). Severity, Occurrence e Detection sono stimati in scala MIL-STD-1629A 1-10. RPN = S × O × D.

**Top item RPN (preliminary):**

| Item / Function | Failure mode | Effect | S | O | D | RPN | Mitigation primaria |
|---|---|---|---:|---:|---:|---:|---|
| Operazione VTOL stagione riproduttiva (mar-lug) | Flushing aquila reale in fase nidificazione → abbandono nido | Perdita covata + reato art. 4 Direttiva 2009/147/CE + sospensione operazioni | 7 | 4 | 5 | **140** | M-AVI-02 buffer 1000 m + M-AVI-03 restrizione stagionale |
| Operazione VTOL stagione riproduttiva | Flushing gufo reale + altri rapaci Allegato I | Disturbo significativo + opposizione Ente Parco | 6 | 4 | 5 | **120** | M-AVI-01 mappa nidi + M-AVI-02 buffer 500 m |
| Sorvolo SIC quota < 200 m AGL | Disturbo continuo specie protette (mammiferi, rettili oltre avifauna) | Impatto VIncA significativo + obbligo VIA piena | 6 | 3 | 4 | **72** | M-AVI-04 quota minima 250 m AGL su SIC |
| Emissioni acustiche cruise < 200 m AGL su Pentema centro abitato | Superamento limiti L. 447/1995 Classe I/II | Esposto cittadino + intervento ARPAL + revisione corridoi | 5 | 4 | 3 | **60** | M-NOI-02 evita sorvolo centro abitato + M-NOI-03 no operazioni notturne |
| Bird-strike accidentale (specie protetta) | Vehicle crash + carcassa specie protetta | Reato penale + sospensione operazioni + danno reputazionale | 8 | 2 | 6 | **96** | M-AVI-04 quota minima + M-AVI-07 sospensione + bird-strike log |
| Operazione VTOL su corridoio panoramico iconico (Monte Antola) | Impatto visivo percepito → esposto associazioni ambientaliste | Opposizione consultazione pubblica VIA + ritardo M+6-12 | 4 | 3 | 4 | **48** | M-PAE-04 rispetto corridoi concertati + M-PAE-01 engagement preventivo |

**Mitigation obbligatoria** (RPN >= 100): 2 failure modes, flushing aquila reale (RPN 140) più bird-strike specie protetta (RPN 96, prossimo soglia). Entrambi mitigati dal pacchetto M-AVI-01..07.

**Cross-link FTA**: il failure mode "bird-strike specie protetta" e' anche cut-set secondario nel top event **Loss of Vehicle in BVLOS** (§6.1), con contributo stimato circa 5E-7/h (bird-strike rate generale UAS BVLOS bassa quota).

**Confidence FMECA Ambientale**: **medium** (preliminary, richiede engagement Ente Parco più bioacustica M+8-M+12 per validazione Occurrence; Detection da consolidare con campagna ARU Y1).

---

## 6. FTA results - sintesi

### 6.1 Top event: Loss of Vehicle in BVLOS (Percorso 6A)

**Target SAIL III SORA 2.5**: P < 1E-5 / flight hour 
**Stima Firmamento (preliminare)**: P circa 2-3E-5 / flight hour (**MARGINALE**)

**Cut sets dominanti:**

1. Avaria FCS critica (circa 1E-5/h), SPOF mitigato da 2oo3 voting + watchdog + ECC
2. Avaria propulsione + landing fail (circa 1E-5/h), mitigato da parachute dual + battery override
3. Severe weather encounter (circa 1E-5/h), mitigato da NOWCAST integration + abort criteria
4. Cyber hijack (circa 1E-6/h), mitigato da crypto + 2FA + air-gap FCS
5. **[NEW v1.5]** Bird-strike specie protetta (circa 5E-7/h), mitigato M-AVI-04 quota minima + M-AVI-07 abort

**Single Points of Failure** (SPOF identificati):

- SPOF-1: autopilot DAL-C primary, mitigato 2oo3 voting + formal verification
- SPOF-2: parachute singolo, mitigato dual pyrotechnic + ballistic backup
- SPOF-3: SATCOM Iridium singolo, mitigato Inmarsat dual-provider Phase B

**Action items per SAIL III compliance:**

- Reduce FCS DAL-C failure rate (HW redundancy + formal verification)
- Improve weather forecast integration (NOWCAST + abort)
- Improve GNSS robustness (Galileo PRS opzionale Phase B)
- **[NEW v1.5]** Implementare bird-strike abort criteria + reporting mensile Ente Parco

### 6.2 Top event: Loss of Mission EO (Percorso 6A pilota Pentema)

**Target SLA cliente**: < 5% per missione 
**Stima Firmamento (preliminare)**: 15-20% / missione (**NON-CONFORME al target 5%**)

**Cut sets dominanti:**

1. Operational mission abort, meteo + Lost-Link + ATC (circa 7%), driver primario
2. Quality below SLA, cloud cover + blur (circa 6%)
3. Payload EO failure (circa 3%), mitigato da ridondanza
4. Data downlink/storage failure (circa 2%), mitigato da buffer + retry
5. **[NEW v1.5]** Abort restrizione ambientale (avvistamento nidificazione, sforamento acustico, esposto cittadino) (circa 1-2%), mitigato M-AVI-02/M-NOI-02

**Action items:**

- SLA realistico con cliente PA = 80-85% mission success rate (revisione target a 10-15% abort)
- Integrazione NOWCAST meteo + cloud cover prediction
- Buffer mission re-scheduling automatico
- **[NEW v1.5]** Procedure abort ambientale documentate + briefing piloti

---

## 7. Residual risk profile v1.5

Post-mitigation, il profilo rischio aggregato e':

| Profilo | RED | YELLOW | GREEN | Totale | Note |
|---|---:|---:|---:|---:|---|
| Baseline v1.0 | 17 | 66 | 33 | 116 | Pre-mitigation |
| Residual v1.0 | 2 | 19 | 95 | 116 | Post-mitigation |
| **Baseline v1.5** | **17** | **68** | **34** | **119** | Pre-mitigation +3 RSK-AMB |
| **Residual v1.5** | **2** | **20** | **97** | **119** | Post-mitigation +1 YEL (AMB-001) +2 GRN (AMB-002/003) |

### 7.1 Profilo per percorso

**Percorso 6A (VTOL pilota Pentema):**

- Showstopper: 0 nessuno bloccante (RSK-REG-001 e RSK-TEC-001/002/003 sono 6B-specific)
- RED residuali: principalmente operativi/regolatori transizione (Part-IS, NIS2, AgID/PSN)
- **[NEW v1.5]** Categoria Ambientale: 0 RED, 1 YELLOW (RSK-AMB-001), 2 GREEN residual. L'engagement Ente Parco e' condizionante ma non bloccante per gate G2/G3.
- Profilo: medio-basso, compatibile con verdetto Go Condizionato

**Percorso 6B (HALE stratosferico R&D):**

- Showstopper: 5 (RSK-TEC-001/002/003 + RSK-REG-001 + RSK-FIN-001)
- Mitigation strategy esiste ma non garantita
- Profilo: alto, compatibile con verdetto Hold / Go Condizionato Estremo
- **[NEW v1.5]** Categoria Ambientale eredita stesso pacchetto mitigazioni (RSK-AMB-001/002 si applicano anche a Phase B test bed Y3+); RSK-AMB-003 paesaggio meno rilevante stratosferico (operatore FL650+ no impatto visivo terra)

### 7.2 Profilo per categoria (visualizzazione ASCII, residual v1.5)

```
Categoria RED YEL GRN Bar (residual)
Tecnico 2 6 7 [##|######|#######]
Regolatorio 0 7 23 [|#######|#######################]
Finanziario 0 4 6 [|####|######]
Mercato 0 4 6 [|####|######]
Operativo 0 2 10 [|##|##########]
Cybersecurity 0 1 6 [|#|######]
Privacy/Legale 0 1 6 [|#|######]
Risorse Umane 0 1 4 [|#|####]
Supply Chain 0 1 6 [|#|######]
Geopolitico 0 3 2 [|###|##]
Reputazionale 0 0 5 [||#####]
Tecnico/Privacy 0 1 0 [|#|]
Tecnico/Regolatorio 0 1 1 [|#|#]
*** Ambientale (NEW) 0 1 2 [|#|##] <-- nuovo v1.5
TOTALE 2 20 97 Totale 119
```

**Confidence aggregato categoria Ambientale**: **medium** (3 rischi su 3 con confidence individuale medium; la mitigation richiede engagement Ente Parco non ancora formalizzato; bioacustica field Y1 da pianificare; press monitoring associazioni ambientaliste continuo richiesto).

### 7.3 Caveat epistemico

Tutti i residual score sono stime expert judgment del metodologia risk register, safety engineer e (nuovo v1.5) ambientalista esterno, con confidence dichiarato per ogni rischio. La probabilita di mitigation effettiva al M+9-12 dipende da:

- Hiring 3 ruoli senior (RSK-HR-002)
- Pre-application ENAC outcomes (RSK-REG-002)
- Funding mix outcomes (RSK-FIN-001 + RSK-MKT-001)
- Audit Part-IS + AgID outcomes (RSK-REG-019 + RSK-REG-021)
- **[NEW v1.5]** Engagement Ente Parco Antola + screening VIncA outcomes (RSK-AMB-001) + esiti consultazione pubblica VIA (RSK-AMB-003)

Re-assessment quarterly con re-scoring trimestrale. Per categoria Ambientale: re-baseline M+8-M+12 post mappa nidi, bioacustica e DGR esito screening.

---

## 8. EWI quarterly monitoring plan v1.5

Top-28 rischi monitorati con Early Warning Indicators dedicati. Frequenza minimum quarterly; rischi RED monthly; rischi Ambientali con cadenza mista (continuo log esposti/bird-strike + stagionale bioacustica + trimestrale Ente Parco). Vedi foglio XLSX `EWI` per dettaglio.

### 8.1 EWI ad alta frequenza (settimanale/mensile)

**18 EWI** ad alta frequenza:

- **RSK-TEC-004** (Mensile): Test bench HIL, trigger: Mismatch ICD > 2 critical, owner: systems-engineer
- **RSK-TEC-005** (Settimanale): GPS interference EASA bulletin, trigger: Eventi jamming Mar Ligure > 3/mese, owner: team avionica e GNC
- **RSK-TEC-008** (Mensile): Battery thermal events sector, trigger: Recall cella o vendor incident, owner: team propulsione e energia
- **RSK-REG-002** (Mensile): ENAC SAIL pre-app feedback, trigger: SAIL > III determination, owner: aviation-regulatory
- **RSK-REG-019** (Mensile): CISO hire + ISMS gap analysis, trigger: CISO non hired entro M+6, owner: aviation-regulatory + CISO
- **RSK-REG-020** (Mensile): Settore UAS BVLOS incidents, trigger: Incidente grave settore IT, owner: ops + safety
- **RSK-REG-025** (Mensile): Procedura affidamento Regione, trigger: Avvio gara competitor incluso, owner: snai-funding + legal
- **RSK-REG-027** (Mensile): ACN classification notice, trigger: Firmamento classificata essenziale, owner: CISO + legal
- **RSK-FIN-001** (Mensile): Pipeline Phase B funding, trigger: Commitment < 30% al gate G5, owner: financial-cfo
- **RSK-FIN-004** (Settimanale): FTE hire pipeline regulatory, trigger: 3 ruoli senior non riempiti M+9, owner: HR + CFO

### 8.2 EWI ambientali, cadenza mista (NEW v1.5)

10 EWI dedicati alla nuova categoria Ambientale (vedi §3bis tabella completa). Sintesi cadenze:

| Cadenza | EWI-AMB inclusi | Rationale |
|---|---|---|
| **Continuo** (log + review mensile) | EWI-AMB-03 (bird-strike log), EWI-AMB-05 (esposti Comune Torriglia) | Eventi rari ma critici, attivazione automatica intervento |
| **Mensile** | EWI-AMB-08 (press monitoring associazioni ambientaliste) | Sentiment + early warning opposizione |
| **Trimestrale** | EWI-AMB-01 (report Ente Parco), EWI-AMB-04 (audit ARPAL), primo trimestre | Allineato con risk register quarterly review |
| **Stagionale** | EWI-AMB-02 (bioacustica mar-mag Y1), EWI-AMB-06 (fonometriche stagionali Y1) | Specie nidificanti attive primavera-estate; rumore variabile climatico |
| **Semestrale** | EWI-AMB-07 (workshop comunita Pentema) | Calibration sentiment locale |
| **Una-tantum** | EWI-AMB-09 (osservazioni VIA), EWI-AMB-10 (DGR esito) | Eventi singoli post submission screening M+9-M+11 |

### 8.3 Quarterly review meeting

**Cadence**: Q+1, Q+2, Q+3, Q+4 (ogni 3 mesi) 
**Partecipanti**: Risk Manager (=CISO joint Head of Regulatory Affairs fino assunzione), CEO, owner ogni RED risk, **[NEW v1.5] ambientalista esterno + observer Ente Parco/ARPAL** (ad-hoc su rischi AMB), observer Coopfond/Legacoop 
**Output**: aggiornamento P/I/Score, residual update, new risks identification, escalation Steering Committee 
**Documenti generati**: Risk Register vN+1 (versioning), EWI dashboard, escalation log e **[NEW v1.5] sezione dedicata Ambientale con sintesi EWI-AMB-01..10**

---

## 9. Versioning roadmap v1.5

| Versione | Data target | Trigger | Owner | Note |
|---|---|---|---|---|
| v1.0 | 2026-05-17 | Consolidamento M+3 | senior risk manager | Baseline 116 rischi |
| **v1.5** | **2026-05-17** | **Refinement post A.12 VIA v2.0 batch 2 M+3** | **risk-register + ambientalista esterno** | **Current, proiezione M+6 con nuova categoria Ambientale (3 RSK-AMB)** |
| v1.6 | 2026-08-17 (M+6) | Gate G2 review + 3 FTE senior hired status + mappa nidi Ente Parco | risk-register + steering | Post-CISO + DPO hire + consolidamento mitigation AVI Ente Parco |
| v1.7 | 2026-11-17 (M+9) | Pre-gate G3 (M+10/M+11) + submission screening VIA + VIncA | risk-register + steering + ambientalista esterno | Hard conditions C1-C5 status update + esiti consultazione VIA preliminare |
| v2.0 | 2027-02-17 (M+12) | Gate G3 outcome + Y1 close + DGR esito screening | risk-register + auditor esterno | Major re-baseline pre-Y2 operations + bilancio Y1 monitoraggio ambientale |
| v2.1 | 2027-08-17 (M+18) | Mid-Y2 update | risk-register | Gate G4 preparation |
| v3.0 | 2028-02-17 (M+24) | Gate G5 outcome, Phase B decision | risk-register + senior advisor | Major re-baseline pre-Phase B |

### 9.1 Re-assessment triggers (oltre a versioning schedule)

- Cambio scope o requisiti (RTM update)
- Nuovo trade study completato
- Gate review imminente (G2/G3/G4/G5)
- Evento esterno (cambio regolatorio EASA/ENAC/AgID/AGCOM, market shock, geopolitical event)
- Incidente o near-miss interno o settore
- Hire 3 ruoli senior (CISO, DPO, Head Reg.Aff.), re-balance owners
- EWI threshold breach (anche singolo)
- **[NEW v1.5]** Pareristica Ente Parco Antola pubblicata (favorevole o avversa)
- **[NEW v1.5]** Esito DGR Regione Liguria screening VIA + VIncA
- **[NEW v1.5]** Bird-strike specie protetta evento singolo OR esposto formale Comune Torriglia
- **[NEW v1.5]** Pubblicazione mappa nidi Ente Parco OR esito campagna bioacustica Y1

### 9.2 Istruzioni rigenerazione XLSX (M+6)

Il file `RISK-REGISTER-v1.0.xlsx` (binario, 116 rischi) non viene rigenerato in v1.5 per minimizzare side-effect su workflow Excel/Coopfond in corso. La rigenerazione XLSX e' pianificata per v1.6 M+6 post gate G2 review:

```bash
# Da eseguire M+6 in /home/user/HALE/studio-di-fattibilita/allegati/A2-Risk-Register/
python3 build_risk_register.py \
 --input RISK-REGISTER-v1.0-full.csv \
 --delta RISK-REGISTER-v1.5-delta.csv \
 --output RISK-REGISTER-v1.6.xlsx \
 --include-fmeca-ambientale \
 --include-ewi-ambientale-table
```

Nota: il file `RISK-REGISTER-v1.5-delta.csv` contiene solo i 3 nuovi RSK-AMB con schema colonne identico al CSV v1.0. Per CSV consolidato completo v1.5 con 119 rischi, concatenare:

```bash
head -1 RISK-REGISTER-v1.0-full.csv > RISK-REGISTER-v1.5-full.csv
tail -n +2 RISK-REGISTER-v1.0-full.csv >> RISK-REGISTER-v1.5-full.csv
tail -n +2 RISK-REGISTER-v1.5-delta.csv >> RISK-REGISTER-v1.5-full.csv
wc -l RISK-REGISTER-v1.5-full.csv # atteso 120 righe (1 header + 119 dati)
```

---

## 10. Linkage cross-volume v1.5

**Documenti di progetto cross-reference (aggiornati v1.5):**

| Documento | Sezione | Linkage |
|---|---|---|
| **A.12 VIA Preliminare v2.0** | §A.12.3 (analisi impatti) | Origine RSK-AMB-001/002/003 |
| **A.12 VIA Preliminare v2.0** | §A.12.4 (VIncA) | Linkage RSK-AMB-001 + REQ-NF-AMB-01 |
| **A.12 VIA Preliminare v2.0** | §A.12.5 (linkage Risk Register) | Specifica formale dei 3 RSK-AMB proposti |
| **A.12 VIA Preliminare v2.0** | §A.12.6 (mitigazioni M-AVI / M-NOI / M-PAE / M-ACQ) | Pacchetti mitigazione referenziati nei 3 RSK-AMB |
| **A.12 VIA Preliminare v2.0** | §A.12.9 (engagement plan) | Linkage RSK-AMB-003 stakeholder communication |
| **Cap. 5 Quadro normativo** | §5.7bis (nuovo) Quadro normativo ambientale | Riferimenti normativi RSK-AMB |
| **Cap. 5 Quadro normativo** | §5.16 | Showstopper regolatori (invariati v1.5) |
| **Cap. 6 Analisi tecnica** | §6.4 | Top-10 + FMECA Payload + FTA preliminari |
| **Cap. 10 Raccomandazione gate** | §10.2 | Risk residuo aggregato (Cap. 10 da aggiornare con riga categoria Ambientale v1.5) |
| **RTM v1.5** | REQ-NF-AMB-01 | Nuovo requisito non-funzionale ambientale linkato ai 3 RSK-AMB |
| **AUDIT-REDTEAM-VOLUME-1** | n/a | review critica M+3 |
| **AUDIT-COMPETITOR-VOLUME-1** | n/a | analisi competitor M+3 |
| **AUDIT-REGULATORY-VOLUME-1** | n/a | review regolatoria M+3 |
| **RESERVED-rischi-geopolitici.md** | 5 RSK-GEO | Accesso ristretto |
| **Metodologia risk register interna** | n/a | Metodologia operativa |

---

## 11. Riferimenti

**Fonti normative e metodologiche:**

- NASA NPR 8000.4A, Agency Risk Management Procedural Requirements (vedi `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md` Annex N)
- MIL-STD-1629A, Procedures for Performing a Failure Mode, Effects and Criticality Analysis
- IEC 60812:2018, Analysis techniques for system reliability, FMECA
- ARP4761, Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems
- NUREG-0492, Fault Tree Handbook
- IEC 61025:2006, Fault tree analysis (FTA)
- ISO 31000:2018, Risk Management, Principles and Guidelines
- D.Lgs. 36/2023 art. 41 (Codice dei Contratti, PFTE)
- Reg.UE 2019/947 + EASA SORA 2.5 (ED Decision 2025/018/R)
- Reg.UE 2023/203, Part-IS Information Security
- D.Lgs. 138/2024, recepimento NIS2
- Reg.UE 2024/1689, AI Act
- D.Lgs. 81/2008, Sicurezza sul lavoro
- **[NEW v1.5]** D.Lgs. 152/2006, Testo Unico Ambiente (TUA), art. 19 screening VIA + Allegato IV
- **[NEW v1.5]** DPR 357/1997, recepimento Direttiva Habitat 92/43/CEE + VIncA
- **[NEW v1.5]** Direttiva 2009/147/CE, Direttiva Uccelli (specie Allegato I)
- **[NEW v1.5]** Direttiva 92/43/CEE, Direttiva Habitat
- **[NEW v1.5]** L. 447/1995, Legge quadro inquinamento acustico
- **[NEW v1.5]** L.R. Liguria 12/1998, zonizzazione acustica + L.R. Liguria 28/2009 VIncA
- **[NEW v1.5]** D.Lgs. 42/2004, Codice dei Beni Culturali e Paesaggio
- **[NEW v1.5]** DPR 31/2017, autorizzazione paesaggistica semplificata
- **[NEW v1.5]** ISO 9613, Acoustics, Attenuation of sound during propagation outdoors
- **[NEW v1.5]** Vas et al. (2015), Mulero-Pazmany et al. (2017), base rate disturbo avifauna UAV

**Documenti di progetto** (vedi §10 Linkage cross-volume per tabella completa).

---

*Fine documento, Allegato A.2 Risk Register Report v1.5, 2026-05-17, Firmamento Technologies, proiezione M+6 post integrazione A.12 VIA v2.0 batch 2*
