# Allegato A.2 - Risk Register Report v1.0

> **Volume 2 - Allegati tecnici - Studio di Fattibilita Piattaforma Aerea HALE/VTOL**  
> Firmamento Technologies srl coop - bando Cooding Prototypes (Coopfond / Legacoop)  
> Versione: **v1.0** - Data: **2026-05-17** - Stato: **Bozza M+3 consolidata**  
> Metodologia: NASA NPR 8000.4A + FMECA (MIL-STD-1629A) + FTA (ARP4761) + ISO 31000:2018  
> Conformita: D.Lgs. 36/2023 art. 41 + EASA SORA 2.5 + Part-IS + NIS2

---

## 1. Metodologia

Il Risk Register Firmamento HALE/VTOL e' costruito secondo **NASA NPR 8000.4A - Continuous Risk Management (CRM)**, con integrazione di:

- **FMECA** (MIL-STD-1629A / IEC 60812) per analisi guasto sottosistema a livello item (Payload EO, Avionica, Propulsione)
- **FTA** (ARP4761 / NUREG-0492 / IEC 61025) per top events critici (Loss of Vehicle BVLOS, Loss of Mission EO)
- **ISO 31000:2018** per principi di risk management end-to-end (identificazione, analisi, valutazione, trattamento, monitoring, communication)
- Compliance specifica aviation: **EASA SORA 2.5** (ED Decision 2025/018/R) + **Part-IS** (Reg.UE 2023/203)
- Compliance cyber: **NIS2** (D.Lgs. 138/2024) + ISO/IEC 27001 + Part-IS

### 1.1 Sistema di scoring P x I

| P (Probabilita) | Descrizione | Range qualitativo |
|---|---|---|
| 1 Very Low | Improbabile | < 5% |
| 2 Low | Possibile ma raro | 5-20% |
| 3 Medium | Possibile | 20-50% |
| 4 High | Probabile | 50-80% |
| 5 Very High | Quasi certo | > 80% |

| I (Impatto) | Tecnico | Schedule | Costo | Safety | Reputational |
|---|---|---|---|---|---|
| 1 Negligible | Aggiornamento doc | < 1 sett. | < 5k EUR | Nessuno | Nessuno |
| 2 Minor | Modifica subsystem | 1-4 sett. | 5-50k EUR | Incidente minore | Locale |
| 3 Moderate | Re-design subsystem | 1-3 mesi | 50-200k EUR | Ferite leggere | Regionale |
| 4 Major | Re-design system | 3-12 mesi | 200k EUR - 1M EUR | Ferite gravi | Nazionale |
| 5 Severe | Showstopper / catastrofe | > 12 mesi | > 1M EUR | Decesso / danni terzi | Internazionale |

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

## 2. Statistiche aggregate

**Totale rischi formalmente tracciati**: 116 (v1.0) → **119** (v1.5 M+6 con nuova categoria Ambientale post A.12 VIA v2.0)

### 2.1 Per categoria
| Categoria | N rischi v1.0 | N rischi v1.5 | Showstopper | RED | YELLOW | GREEN |
|---|---:|---:|---:|---:|---:|---:|
| **Ambientale (NEW v1.5)** | 0 | **3** | 0 | 0 | 1 (RSK-AMB-001) | 2 (RSK-AMB-002/003) |
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
| **TOTALE** | **116** | **119** | **5** | **17** | **67** | **35** |

### 2.2 Per status

| Status | N rischi |
|---|---:|
| Showstopper | 5 |
| Open-Critical | 12 |
| Open-High | 47 |
| Monitor | 34 |
| Open-Medium | 18 |

### 2.3 P x I matrix (baseline pre-mitigation)

| I \ P | P=1 | P=2 | P=3 | P=4 | P=5 |
|---|---|---|---|---|---|
| I=5 | 1 (GRN) | 5 (YEL) | 2 (RED) | 1 (RED) | 1 (RED) |
| I=4 | 0 (GRN) | 15 (YEL) | 14 (YEL) | 11 (RED) | 1 (RED) |
| I=3 | 0 (GRN) | 19 (GRN) | 23 (YEL) | 7 (YEL) | 1 (RED) |
| I=2 | 0 (GRN) | 2 (GRN) | 11 (GRN) | 2 (YEL) | 0 (YEL) |
| I=1 | 0 (GRN) | 0 (GRN) | 0 (GRN) | 0 (GRN) | 0 (GRN) |

### 2.4 Mitigation effectiveness

- **Pre-mitigation**: RED=17, YELLOW=66, GREEN=33
- **Post-mitigation (residual)**: RED=2, YELLOW=19, GREEN=95
- **RED reduction**: 17 -> 2 (88%)
- **YELLOW reduction**: 66 -> 19 (71%)

---

## 3. Top-25 rischi narrati

Ordinati per Score baseline (P x I) decrescente. Per ciascuno: descrizione, impatto sul progetto, mitigation status.

### 1. RSK-TEC-001 - Tecnico - Score 25 -> residual 20 (RED)

**Descrizione**: Energy balance HALE inverno 44N - deficit -50% confermato da simulazione (vs +0-15% stima a mano)  
**Trigger**: Simulazione 365gg M+3 mostra -50.1% margin solstizio dic; perennial flight NON fattibile baseline 2026-28  
**Owner**: propulsion-energy-engineer  
**Status**: Showstopper  
**Response**: Mitigate  
**Mitigation**: Plan A obbligato E5 'Seasonal-only mar-ott' (~7 mesi). Plan B Y6+: migrazione SS Li 450 Wh/kg o PEM+LH2. Plan C: ridimensionamento R&D-only fino tech 2030+  
**Residual P x I**: 5 x 4 = 20  
**Fase critica**: Y3-Y5 (Phase B 6B)  
**Confidence**: high  
**EWI**: Sim. allegato A.7 + monthly clear-sky variability + LiS pack TRL update trimestrale  
**Falsifying observation**: Se al gate G5 (M+24) sim. con dati operativi reali conferma deficit >30% giorni anche scenario E5, Percorso 6B terminato come operativo perennial  

### 2. RSK-REG-001 - Regolatorio - Score 20 -> residual 16 (RED)

**Descrizione**: Mancanza framework HAPS EASA/ENAC - no Special Condition aperto HALE solare civile  
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

**Descrizione**: Mancanza commitment funding Phase B 6B - 5.5-13.5M EUR mix EDF+Horizon+PNRR+equity  
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

**Descrizione**: Type Certification HALE timeline > 5 anni - no precedente HALE solare civile EU con TC emesso  
**Trigger**: EASA non apre RMT HAPS o Special Condition path entro 2028  
**Owner**: aviation-regulatory + sovereign-strategist  
**Status**: Showstopper  
**Response**: Mitigate+Accept  
**Mitigation**: Parallel approach: ops 6A genera revenue + esperienza mentre TC HALE matura. Engagement EASA Innovation Network + consortium CIRA/TAS per Special Condition collettiva  
**Residual P x I**: 4 x 3 = 12  
**Fase critica**: Y4-Y8  
**Confidence**: medium-high  
**EWI**: EASA RMT HAPS calendar + advisory bodies pubblicazioni + AALTO/Skydweller TC progress  
**Falsifying observation**: Se a Y5 (M+60) EASA non ha aperto RMT HAPS, Percorso 6B operativo commerciale rinviato a Y8+, scenario No-Go pieno se anche window IRIS2 chiusa  

### 5. RSK-HR-002 - Risorse Umane - Score 16 -> residual 9 (RED)

**Descrizione**: Reclutamento CISO + DPO + Head Regulatory - 3 ruoli senior in mercato compresso  
**Trigger**: Tempo hire > 9 mesi (vs target 3-6 mesi)  
**Owner**: HR + CEO  
**Status**: Open-Critical  
**Response**: Mitigate  
**Mitigation**: Headhunter specializzati; contratti competitivi (180-220k EUR/anno per CISO senior); part-time fractional CISO/DPO M+0-6; partnership consulting Legal/Cyber  
**Residual P x I**: 3 x 3 = 9  
**Fase critica**: Y0-Y1  
**Confidence**: medium  
**EWI**: Hire pipeline weekly + headhunter pipeline status  
**Falsifying observation**: Se ruoli senior non riempiti M+9, NIS2/Part-IS compliance a rischio + cap.OpEx esplode con consulting fees  

### 6. RSK-REG-008 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: EASA Part-21 design organisation approval (DOA) - richiesto per HALE Phase C  
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

**Descrizione**: EUROCONTROL Network Manager - coordinamento ATM-ANS HAPS FL400+ EU airspace  
**Trigger**: EUROCONTROL non rilascia procedure operative HAPS perennial entro Y4-Y5  
**Owner**: avionics-gnc-engineer + aviation-regulatory  
**Status**: Open-Critical  
**Response**: Mitigate  
**Mitigation**: Engagement EUROCONTROL precocemente (Y2-Y3); partecipazione workshop UAM/HAPS Network Manager; contributo definizione procedure  
**Residual P x I**: 3 x 3 = 9  
**Fase critica**: Y3+  
**Confidence**: medium  
**EWI**: EUROCONTROL Network Manager workplan + HAPS procedure pubblicate  
**Falsifying observation**: Se EUROCONTROL declina procedure HAPS perennial entro Y5, operativita cross-border bloccata; ridimensionamento operazioni IT-only  

### 8. RSK-REG-019 - Regolatorio - Score 16 -> residual 9 (RED)

**Descrizione**: Part-IS EASA Reg.UE 2023/203 - ISMS obbligatorio da feb 2026, CISO assente  
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

**Descrizione**: Affidamento PA art.50 D.Lgs.36/2023 - contratto Regione > 140k EUR richiede gara  
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

**Descrizione**: ENAV procedure FL400+ - HAPS perennial sopra FL400/FL650 senza procedure dedicate  
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

**Descrizione**: Batterie LiS - capacity allocation Northvolt/Italvolt incerta  
**Trigger**: Northvolt bankruptcy o Italvolt ritardo > 2 anni production  
**Owner**: propulsion-energy-engineer + supply-chain  
**Status**: Open-High  
**Response**: Mitigate  
**Mitigation**: Multi-vendor LiS pipeline (Oxis Energy heir, Lyten, NexTech); custom pack assembly con cell suppliers diversi  
**Residual P x I**: 3 x 3 = 9  
**Fase critica**: Y3+  
**Confidence**: medium  
**EWI**: Battery vendors financials + production timelines  

### 12. RSK-TEC-016 - Tecnico - Score 16 -> residual 9 (RED)

**Descrizione**: NTN payload winter unsustainable - margin -58.9% con P_payload 500 W (scenario E5)  
**Trigger**: Simulazione M+3 (DR-014) conferma deficit anche con payload pulse-mode  
**Owner**: propulsion-energy-engineer + telecom-ntn-payload-expert  
**Status**: Open-Critical  
**Response**: Mitigate  
**Mitigation**: NTN seasonal-only + payload pulse-mode duty-cycle < 30% + dedicated battery bank NTN  
**Residual P x I**: 3 x 3 = 9  
**Fase critica**: Y4-Y5  
**Confidence**: medium-high  
**EWI**: Sim. allegato A.7 update; product roadmap 5G NTN bypass requirements  

### 13. RSK-REG-021 - Regolatorio - Score 16 -> residual 6 (RED)

**Descrizione**: AgID/PSN hosting dati PA - cloud non qualificato blocca contratti Regione/PC  
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

**Descrizione**: NIS2 D.Lgs.138/2024 - registrazione ACN omessa, sanzioni fino 10M EUR / 2% fatturato  
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

**Descrizione**: Riduzione TRL gap M+24 - integrato HALE subsystem critici < TRL 5  
**Trigger**: Gate G5 review M+24 mostra TRL integrato propulsione/avionica/payload < 5  
**Owner**: systems-engineer + propulsion-energy-engineer  
**Status**: Open-Critical  
**Response**: Mitigate  
**Mitigation**: Roadmap TRL puntuale per sottosistema + milestone trimestrali + partnership prime per acceleration TRL (DR-013 finding)  
**Residual P x I**: 3 x 4 = 12  
**Fase critica**: Y3 (gate G5)  
**Confidence**: medium  
**EWI**: TRL milestone tracker + subsystem demo report + partnership signed  
**Falsifying observation**: Se TRL gap > 2 a M+24, Phase C-D non finanziabile; ridimensionamento seasonal-only + R&D-only mode  

### 16. RSK-FIN-004 - Finanziario - Score 15 -> residual 8 (RED)

**Descrizione**: OpEx Y1 underestimato - +450-800k EUR per 3 FTE regulatory (CISO+DPO+Head Reg.Aff)  
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

**Descrizione**: Aeroelasticita ala high-AR (AR>=25) - flutter, divergenza, instabilita non lineare  
**Trigger**: Analisi aeroelastica preliminare M+12 mostra flutter speed < 1.3x Vdive o divergenza < 1.5x Vc  
**Owner**: aero-structures-engineer  
**Status**: Showstopper  
**Response**: Mitigate  
**Mitigation**: Aeroelastic analysis non-lineare (NASTRAN+ZAERO o MSC.Nastran SOL145) + GVT (Ground Vibration Test) + flight test subscale + winglet/passive damping design. Tilted spar caps + balance mass.  
**Residual P x I**: 2 x 4 = 8  
**Fase critica**: Y3-Y4 (Phase B 6B)  
**Confidence**: medium-high  
**EWI**: Output FEA aeroelastico subscale + risultati GVT + base rate Helios/PHASA flutter events  
**Falsifying observation**: Se subscale flight test M+18-24 mostra divergence o flutter sotto envelope, ridisegno radicale ala richiesto - costo +1-2M EUR + delay 6-12 mesi  

### 18. RSK-MKT-001 - Mercato - Score 12 -> residual 9 (YELLOW)

**Descrizione**: Adozione lenta PA - cicli appalti pubblici 12-24 mesi vs piano 6-9 mesi  
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

**Descrizione**: Competitor Tier 1 AALTO-Leonardo JV - cattura 2-3 Regioni SNAI con pricing aggressivo  
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

**Descrizione**: Pricing pressure - PA italiana clienti price-sensitive vs servizi premium  
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

**Descrizione**: Single-customer concentration Liguria - alternanza politica regionale evapora anchor  
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

**Descrizione**: FCS DAL-C HALE custom - mancanza track record civile + costo qualification ~2-5M EUR  
**Trigger**: Vendor FCS DAL-C EU rifiuta development partnership o costo > budget  
**Owner**: avionics-gnc-engineer  
**Status**: Open-High  
**Response**: Mitigate  
**Mitigation**: Engagement early vendor EU (UAVOS, MicroPilot, Honeywell EU); partnership con CIRA su FCS Italian sovereign; budget riservato 2-3M EUR R&D  
**Residual P x I**: 2 x 4 = 8  
**Fase critica**: Y3-Y4  
**Confidence**: medium  
**EWI**: Quotation vendor FCS + RMT EASA on autonomy  

### 23. RSK-FIN-005 - Finanziario - Score 12 -> residual 6 (YELLOW)

**Descrizione**: Slittamento grant FESR/PNRR - tempi PA italiani median 18-30 mesi  
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

**Descrizione**: WACC effettivo > 18% se grant mix < 30% - NPV diventa negativo (sensitivity Cap.8)  
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

**Descrizione**: Cash flow gap Y2-Y3 - revenue ramp lento vs OpEx fixed  
**Trigger**: Revenue Y2 < 500k EUR (50% target)  
**Owner**: financial-cfo + business-model  
**Status**: Open-High  
**Response**: Mitigate  
**Mitigation**: Bridge financing Series A; cost flex su FTE variable; contratti pluriennali Regione anticipated payment  
**Residual P x I**: 2 x 3 = 6  
**Fase critica**: Y2-Y3  
**Confidence**: medium  
**EWI**: Revenue actuals monthly + cash burn rate  

---

## 3bis. Nuovi rischi ambientali proposti da A.12 VIA v2.0 (M+3 post audit batch 2)

> **Fonte**: refinement Allegato A.12 Relazione VIA Preliminare COMPLETE v2.0, §A.12.5 Linkage Risk Register. Nuova categoria **Ambientale** (n=3) da integrare al sheet `Categories` del Risk Register v1.5 M+6 (sostituirà v1.0 attuale di 116 rischi → v1.5 di 119 rischi, di cui 1 YELLOW + 2 GREEN).

### 26. RSK-AMB-001 - Ambientale - Score 12 -> residual 6 (YELLOW)

**Descrizione**: Disturbo avifauna nidificante in SIC IT1331402 Parco Antola: operazioni VTOL in stagione riproduttiva marzo-luglio possono indurre flushing aquila reale (Aquila chrysaetos, Allegato I Direttiva Uccelli) e gufo reale (Bubo bubo) con abbandono nido + perdita covata  
**Trigger**: Ente Parco Antola comunica nidificazione attiva in raggio < 500 m da corridoi volo M+6+, OR ARPAL/ISPRA segnala incidenti documentati di flushing UAV  
**Owner**: ambientalista esterno + operations + Ente Parco Antola  
**Status**: Open-Medium  
**Response**: Mitigate  
**Mitigation**: M-AVI-01 (buffer 500 m da nidi noti); M-AVI-02 (restrizione operativa marzo-luglio in zone nidificazione); M-AVI-03 (quota minima 200 m AGL su SIC vs minimo regolamentare 120 m); M-AVI-04 (acquisizione mappa nidi Ente Parco entro M+6); M-AVI-05 (engagement formale Ente Parco con convenzione operativa bozza M+9); M-AVI-06 (training piloti su comportamento avifauna); M-AVI-07 (osservazione visiva pre-volo + abort se avvistamento rapaci)  
**Residual P x I**: 2 x 3 = 6  
**Fase critica**: Y1+ (operazioni continuative)  
**Confidence**: medium (richiede mappa nidi da Ente Parco, ARPAL bioacustica)  
**EWI**: Report Ente Parco trimestrale + monitoring acustico passive 3 punti rappresentativi + audit ARPAL annuale  
**Falsifying observation**: Se al M+12 audit Ente Parco/ARPAL rileva ≥ 2 incidenti documentati di flushing nidi entro buffer 500 m, mitigation insufficiente: attivazione re-baseline corridoi volo + estensione restrizione stagionale a febbraio-agosto + eventuale sospensione operazioni in zone SIC critiche  
**Linkage**: A.12 VIA v2.0 §A.12.3 fauna + §A.12.4 VIncA + §A.12.6 mitigazioni; REQ-NF-AMB-01 nuovo per RTM v1.5; FO-AMB-01 (proposed)

### 27. RSK-AMB-002 - Ambientale - Score 9 -> residual 4 (GREEN)

**Descrizione**: Inquinamento acustico VTOL in area parco: 65-75 dB(A) a 100 m può superare limiti L. 447/1995 + classificazione acustica L.R. Liguria 12/1998 in fasce protette parco (Classe I notturna 40 dB / diurna 50 dB; Classe II diurna 55 dB) durante operazioni ravvicinate (< 100 m AGL su zone urbanizzate o eventi raduno)  
**Trigger**: Misurazione fonometrica Y1 > limiti tabella zonizzazione, OR esposto comunità Pentema/Torriglia per disturbo acustico (anche un solo cittadino può attivare Comune + ARPAL)  
**Owner**: operations + ambientalista esterno + Comune Torriglia  
**Status**: Open-Medium  
**Response**: Mitigate  
**Mitigation**: M-NOI-01 (modello propagazione rumore pre-pilota a 7 punti rappresentativi + classificazione acustica Comune Torriglia); M-NOI-02 (corridoi di volo evitano sorvolo Pentema centro abitato < 200 m AGL); M-NOI-03 (no operazioni notturne 22:00-06:00 salvo emergency PC); M-NOI-04 (campagna informativa preventiva comunità Pentema)  
**Residual P x I**: 2 x 2 = 4  
**Fase critica**: Y1+  
**Confidence**: medium-high (limite operativo conservativo VTOL CW-30E classe rumore moderata)  
**EWI**: Esposti Comune Torriglia + misure fonometriche ARPAL ad-hoc + feedback workshop comunità Pentema  
**Falsifying observation**: Se al M+12 ≥ 1 esposto cittadino formale OR ARPAL rileva sforamento > 5 dB rispetto limite zonale, mitigation insufficiente: re-baseline corridoi + eventuale relocation hangar Pentema  
**Linkage**: A.12 VIA v2.0 §A.12.3 rumore + §A.12.6 M-NOI; Cap. 2 §2.4 top-5 comunità Pentema (accettabilità sociale); FO-AMB-02 (proposed)

### 28. RSK-AMB-003 - Ambientale - Score 8 -> residual 3 (GREEN)

**Descrizione**: Impatto visivo paesaggistico VTOL in area vincolata D.Lgs. 42/2004: sorvolo paesaggi tutelati Parco Antola può configurare impatto visivo transitorio percepito dalla comunità + turisti, con potenziale opposizione associazioni ambientaliste (Italia Nostra, WWF, Legambiente) in fase istruttoria Regione  
**Trigger**: Esposto associazioni ambientaliste in fase consultazione pubblica VIA OR opposizione Comune Torriglia in DGR  
**Owner**: business-model + ambientalista esterno + Ente Parco + Comune Torriglia  
**Status**: Open-Low  
**Response**: Mitigate  
**Mitigation**: M-PAE-01 (engagement preventivo associazioni ambientaliste Italia Nostra Liguria + WWF Liguria + Legambiente Liguria); M-PAE-02 (comunicazione trasparente impatto transitorio + benefici ambientali controfattuale -99% CO₂ vs elicottero manned); M-PAE-03 (eventi pubblici Pentema con dimostrazione volo + Q&A comunità); M-PAE-04 (rispetto corridoi volo concertati con Ente Parco evitando viste paesaggistiche iconiche es. Monte Antola panoramica)  
**Residual P x I**: 1 x 3 = 3  
**Fase critica**: Y0-Y1 (fase istruttoria Regione + autorizzazione Parco)  
**Confidence**: medium  
**EWI**: Press monitoring associazioni ambientaliste + workshop Pentema feedback + Regione Liguria DGR esito  
**Falsifying observation**: Se al M+9 ≥ 2 associazioni ambientaliste pubblicano opposizione formale a Regione Liguria, mitigation insufficiente: re-design comunicazione + eventuale pivot site pilota alternative (es. Val Trebbia Comune Rondanina)  
**Linkage**: A.12 VIA v2.0 §A.12.3 paesaggio + §A.12.9 engagement plan; Cap. 7 §7.5.1 pilastro #3 sostenibilità + ESG narrative; FO-AMB-03 (proposed)

---

## 4. Showstopper formali (5+5)

### 4.1 Showstopper originali Cap. 6.4 + Cap. 10.2 (5)

| ID | Rischio | Score | Percorso | Mitigation status |
|---|---|---:|---|---|
| **RSK-TEC-001** | Energy balance HALE inverno 44N - deficit -50% confermato da simulazione (vs +0-... | 25 | 6B | Mitigate: Plan A obbligato E5 'Seasonal-only mar-ott' (~7 mesi). Plan B Y6+: migrazione SS... |
| **RSK-TEC-002** | Aeroelasticita ala high-AR (AR>=25) - flutter, divergenza, instabilita non linea... | 15 | 6B | Mitigate: Aeroelastic analysis non-lineare (NASTRAN+ZAERO o MSC.Nastran SOL145) + GVT (Gro... |
| **RSK-TEC-003** | Type Certification HALE timeline > 5 anni - no precedente HALE solare civile EU ... | 16 | 6B | Mitigate+Accept: Parallel approach: ops 6A genera revenue + esperienza mentre TC HALE matura. Eng... |
| **RSK-REG-001** | Mancanza framework HAPS EASA/ENAC - no Special Condition aperto HALE solare civi... | 20 | 6B | Mitigate: Engagement EASA Innovation Network + consortium CIRA/TAS per Special Condition c... |
| **RSK-FIN-001** | Mancanza commitment funding Phase B 6B - 5.5-13.5M EUR mix EDF+Horizon+PNRR+equi... | 20 | 6B | Mitigate: Mix funding: EDF (DG DEFIS) + Horizon Europe + PNRR Aerospazio + Series B equity... |

### 4.2 Showstopper critici aggiuntivi §5.16 (5)

Identificati dall'audit `regulatory-adversary` M+3, formalizzati in Cap. 5 §5.16. Score 15-20.

| ID | Rischio | Score | Owner | Deadline mitigation |
|---|---|---:|---|---|
| **RSK-REG-019** | Part-IS EASA Reg.UE 2023/203 - ISMS obbligatorio da feb 2026, CISO assente... | 16 | aviation-regulatory + CISO (new) | Y1 (M+0 → M+12) urgente |
| **RSK-REG-021** | AgID/PSN hosting dati PA - cloud non qualificato blocca contratti Regione/PC... | 16 | data-privacy + IT + DPO | Y1+ |
| **RSK-REG-025** | Affidamento PA art.50 D.Lgs.36/2023 - contratto Regione > 140k EUR richiede gara... | 16 | snai-funding + legal + business-model | Y0+ |
| **RSK-REG-027** | NIS2 D.Lgs.138/2024 - registrazione ACN omessa, sanzioni fino 10M EUR / 2% fattu... | 16 | CISO (new) + legal | Y0+ immediato |
| **RSK-REG-030** | ENAV procedure FL400+ - HAPS perennial sopra FL400/FL650 senza procedure dedicat... | 16 | avionics + sovereign-strategist + aviation-regulatory | Y3+ |
| **RSK-REG-018** | EUROCONTROL Network Manager - coordinamento ATM-ANS HAPS FL400+ EU airspace... | 16 | avionics-gnc-engineer + aviation-regulatory | Y3+ |

### 4.3 Implicazione per il verdetto Cap. 10

Il verdetto Cap. 10 "Go Condizionato 6A" presuppone:
- Tutti i 5 RSK-REG critical aggiuntivi mitigated entro M+9-12 (Part-IS, AgID, NIS2 sono **urgenti** M+0-3)
- 3 FTE senior (CISO, DPO, Head of Regulatory Affairs) hired entro M+6-9 (RSK-HR-002)
- OpEx Y1 aggiornato con +450-800k EUR (RSK-FIN-004)
- RSK-FIN-001 (funding Phase B) tracciato come precondizione gate G5

Scenario realistico (post Red Team M+3): 60-80% percorsi sono **Hold con piano** vs **Go pieno** al M+10/M+11.

---

## 5. FMECA results - sintesi

Vedi fogli XLSX: `FMECA_Payload`, `FMECA_Avionica`, `FMECA_Propulsione`.

### 5.1 Payload EO

**Top item RPN**:
- IR sensor WIRIS Pro LWIR - Calibrazione persa - RPN **48** - mitigation: NUC frequente + crosscheck con RGB + ground truth
- Downlink data RF/SATCOM - Interruzione bandwidth - RPN **24** - mitigation: Buffer + retry + alt downlink + ACM
- Camera RGB Phase One iXM 100 - Blur image - RPN **18** - mitigation: Gimbal damping + IBIS + post-processing deblur
- Gimbal Phase One IXM mount - Stuck position - RPN **18** - mitigation: Service interval + ridondanza motor 2oo3
- Gimbal - Vibration excess - RPN **18** - mitigation: Maintenance schedule + bearing monitor

**Mitigation obbligatoria** (RPN >= 40): IR sensor calibrazione persa (RPN 48). NUC frequente + crosscheck con RGB + ground truth.

### 5.2 Avionica

**Top item RPN**:
- Parachute deployment - Failure to deploy - RPN **30** - mitigation: Dual pyrotechnic + maintenance + test deployment
- GNSS dual-frequency - Spoofing detected - RPN **27** - mitigation: RAIM + IMU dead-reckoning + multi-constellation
- FCS autopilot DAL-C - Reboot unexpected - RPN **24** - mitigation: 2oo3 voting + watchdog + ECC memory
- IMU primary triplex - Drift gyro out of spec - RPN **18** - mitigation: Triplex IMU + crosscheck + Kalman filter
- GNSS - Jamming sustained - RPN **18** - mitigation: Multi-frequency + IMU fallback + Lost-Link

### 5.3 Propulsione

**Top item RPN**:
- Battery LiPo - Thermal runaway - RPN **40** - mitigation: Cell-level fuse + intumescent + BMS + ATEX storage
- Battery LiS - Thermal runaway HALE - RPN **40** - mitigation: Cell-level fuse + thermal monitor + emergency vent
- Hybrid engine gasoline 6A - Carburator clog - RPN **36** - mitigation: Fuel filter + quality control + maintenance
- Battery LiS HALE 6B - Capacity fade - RPN **36** - mitigation: Cycle monitoring + DoD limit + replacement at 80% SoH
- Propeller composite - Blade strike - RPN **27** - mitigation: Inspection pre-flight + replacement schedule + spare

---

## 6. FTA results - sintesi

### 6.1 Top event: Loss of Vehicle in BVLOS (Percorso 6A)

**Target SAIL III SORA 2.5**: P < 1E-5 / flight hour  
**Stima Firmamento (preliminare)**: P ~ 2-3E-5 / flight hour (**MARGINALE**)

**Cut sets dominanti**:
1. Avaria FCS critica (~1E-5/h) - SPOF mitigato da 2oo3 voting + watchdog + ECC
2. Avaria propulsione + landing fail (~1E-5/h) - mitigato da parachute dual + battery override
3. Severe weather encounter (~1E-5/h) - mitigato da NOWCAST integration + abort criteria
4. Cyber hijack (~1E-6/h) - mitigato da crypto + 2FA + air-gap FCS

**Single Points of Failure** (SPOF identificati):
- SPOF-1: autopilot DAL-C primary - **mitigato 2oo3 voting + formal verification**
- SPOF-2: parachute singolo - **mitigato dual pyrotechnic + ballistic backup**
- SPOF-3: SATCOM Iridium singolo - **mitigato Inmarsat dual-provider Phase B**

**Action items per SAIL III compliance**:
- Reduce FCS DAL-C failure rate (HW redundancy + formal verification)
- Improve weather forecast integration (NOWCAST + abort)
- Improve GNSS robustness (Galileo PRS opzionale Phase B)

### 6.2 Top event: Loss of Mission EO (Percorso 6A pilota Pentema)

**Target SLA cliente**: < 5% per missione  
**Stima Firmamento (preliminare)**: 15-20% / missione (**NON-CONFORME al target 5%**)

**Cut sets dominanti**:
1. Operational mission abort - meteo + Lost-Link + ATC (~7%) - **driver primario**
2. Quality below SLA - cloud cover + blur (~6%)
3. Payload EO failure (~3%) - mitigato da ridondanza
4. Data downlink/storage failure (~2%) - mitigato da buffer + retry

**Action items**:
- SLA realistico con cliente PA = 80-85% mission success rate (revisione target a 10-15% abort)
- Integrazione NOWCAST meteo + cloud cover prediction
- Buffer mission re-scheduling automatico

---

## 7. Residual risk profile

Post-mitigation, il profilo rischio aggregato e':

| Profilo | RED | YELLOW | GREEN | Totale | Note |
|---|---:|---:|---:|---:|---|
| Baseline | 17 | 66 | 33 | 116 | Pre-mitigation |
| Residual | 2 | 19 | 95 | 116 | Post-mitigation |

### 7.1 Profilo per percorso

**Percorso 6A (VTOL pilota Pentema)**:
- Showstopper: 0 nessuno bloccante (RSK-REG-001 e RSK-TEC-001/002/003 sono 6B-specific)
- RED residuali: principalmente operativi/regolatori transizione (Part-IS, NIS2, AgID/PSN)
- Profilo: **medio-basso** - compatibile con verdetto Go Condizionato

**Percorso 6B (HALE stratosferico R&D)**:
- Showstopper: 5 (RSK-TEC-001/002/003 + RSK-REG-001 + RSK-FIN-001)
- Mitigation strategy esiste ma **non garantita**
- Profilo: **alto** - compatibile con verdetto Hold / Go Condizionato Estremo

### 7.2 Caveat epistemico

Tutti i residual score sono **stime expert judgment** del risk-register-builder + safety engineer, con confidence dichiarato per ogni rischio. La probabilita di mitigation effettiva al M+9-12 dipende da:
- Hiring 3 ruoli senior (RSK-HR-002)
- Pre-application ENAC outcomes (RSK-REG-002)
- Funding mix outcomes (RSK-FIN-001 + RSK-MKT-001)
- Audit Part-IS + AgID outcomes (RSK-REG-019 + RSK-REG-021)

Re-assessment quarterly con re-scoring trimestrale.

---

## 8. EWI quarterly monitoring plan

Top-26 rischi monitorati con Early Warning Indicators dedicati. Frequenza minimum quarterly; rischi RED monthly. Vedi foglio XLSX `EWI` per dettaglio.

### 8.1 EWI ad alta frequenza (settimanale/mensile)

**18 EWI** ad alta frequenza:
- **RSK-TEC-004** (Mensile): Test bench HIL - trigger: Mismatch ICD > 2 critical - owner: systems-engineer
- **RSK-TEC-005** (Settimanale): GPS interference EASA bulletin - trigger: Eventi jamming Mar Ligure > 3/mese - owner: avionics-gnc-engineer
- **RSK-TEC-008** (Mensile): Battery thermal events sector - trigger: Recall cella o vendor incident - owner: propulsion-energy-engineer
- **RSK-REG-002** (Mensile): ENAC SAIL pre-app feedback - trigger: SAIL > III determination - owner: aviation-regulatory
- **RSK-REG-019** (Mensile): CISO hire + ISMS gap analysis - trigger: CISO non hired entro M+6 - owner: aviation-regulatory + CISO
- **RSK-REG-020** (Mensile): Settore UAS BVLOS incidents - trigger: Incidente grave settore IT - owner: ops + safety
- **RSK-REG-025** (Mensile): Procedura affidamento Regione - trigger: Avvio gara competitor incluso - owner: snai-funding + legal
- **RSK-REG-027** (Mensile): ACN classification notice - trigger: Firmamento classificata essenziale - owner: CISO + legal
- **RSK-FIN-001** (Mensile): Pipeline Phase B funding - trigger: Commitment < 30% al gate G5 - owner: financial-cfo
- **RSK-FIN-004** (Settimanale): FTE hire pipeline regulatory - trigger: 3 ruoli senior non riempiti M+9 - owner: HR + CFO

### 8.2 Quarterly review meeting

**Cadence**: Q+1, Q+2, Q+3, Q+4 (ogni 3 mesi)  
**Partecipanti**: Risk Manager (=CISO joint Head of Regulatory Affairs fino assunzione), CEO, owner ogni RED risk, observer Coopfond/Legacoop  
**Output**: aggiornamento P/I/Score, residual update, new risks identification, escalation Steering Committee  
**Documenti generati**: Risk Register vN+1 (versioning) + EWI dashboard + escalation log

---

## 9. Versioning roadmap

| Versione | Data target | Trigger | Owner | Note |
|---|---|---|---|---|
| v1.0 | 2026-05-17 | Consolidamento M+3 | senior risk manager | **Attuale** |
| v1.1 | 2026-08-17 (M+6) | Gate G2 review + 3 FTE senior hired status | risk-register + steering | Post-CISO + DPO hire
| v1.2 | 2026-11-17 (M+9) | Pre-gate G3 (M+10/M+11) | risk-register + steering | Hard conditions C1-C5 status update
| v2.0 | 2027-02-17 (M+12) | Gate G3 outcome + Y1 close | risk-register + auditor esterno | Major re-baseline pre-Y2 operations
| v2.1 | 2027-08-17 (M+18) | Mid-Y2 update | risk-register | Gate G4 preparation
| v3.0 | 2028-02-17 (M+24) | Gate G5 outcome - Phase B decision | risk-register + senior advisor | Major re-baseline pre-Phase B

### 9.1 Re-assessment triggers (oltre a versioning schedule)

- Cambio scope o requisiti (RTM update)
- Nuovo trade study completato
- Gate review imminente (G2/G3/G4/G5)
- Evento esterno (cambio regolatorio EASA/ENAC/AgID/AGCOM, market shock, geopolitical event)
- Incidente o near-miss interno o settore
- Hire 3 ruoli senior (CISO, DPO, Head Reg.Aff.) - re-balance owners
- EWI threshold breach (anche singolo)

---

## 10. Riferimenti

**Fonti normative e metodologiche**:
- NASA NPR 8000.4A - Agency Risk Management Procedural Requirements (vedi `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md` Annex N)
- MIL-STD-1629A - Procedures for Performing a Failure Mode, Effects and Criticality Analysis
- IEC 60812:2018 - Analysis techniques for system reliability - FMECA
- ARP4761 - Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems
- NUREG-0492 - Fault Tree Handbook
- IEC 61025:2006 - Fault tree analysis (FTA)
- ISO 31000:2018 - Risk Management - Principles and Guidelines
- D.Lgs. 36/2023 art. 41 (Codice dei Contratti - PFTE)
- Reg.UE 2019/947 + EASA SORA 2.5 (ED Decision 2025/018/R)
- Reg.UE 2023/203 - Part-IS Information Security
- D.Lgs. 138/2024 - recepimento NIS2
- Reg.UE 2024/1689 - AI Act
- D.Lgs. 81/2008 - Sicurezza sul lavoro

**Documenti di progetto** (cross-reference):
- `studio-di-fattibilita/cap-05-quadro-normativo.md` §5.16 - 15 showstopper regolatori
- `studio-di-fattibilita/cap-06-analisi-tecnica.md` §6.4 - Top-10 + FMECA Payload + FTA preliminari
- `studio-di-fattibilita/cap-10-raccomandazione-di-gate.md` §10.2 - Risk residuo aggregato
- `riferimenti/RESERVED-rischi-geopolitici.md` - 5 RSK-GEO (accesso ristretto)
- `studio-di-fattibilita/AUDIT-REDTEAM-VOLUME-1.md` - Red Team M+3
- `studio-di-fattibilita/AUDIT-COMPETITOR-VOLUME-1.md` - Competitor Intelligence M+3
- `studio-di-fattibilita/AUDIT-REGULATORY-VOLUME-1.md` - Regulatory Adversary M+3
- `.claude/skills/risk-register-builder/SKILL.md` - Metodologia operativa

---

*Fine documento - Allegato A.2 Risk Register Report v1.0 - 2026-05-17 - Firmamento Technologies*
