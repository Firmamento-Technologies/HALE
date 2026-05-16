# Ricerche approfondite — Studio di Fattibilità HALE Firmamento Technologies

**Data raccolta:** maggio 2026
**Scopo:** dataset di riferimenti tecnici, regolatori, di mercato e di filiera per alimentare lo Studio di Fattibilità.
**Limite tecnico noto:** la network policy del runtime cloud blocca il download diretto delle fonti italiane (`x-deny-reason: host_not_allowed`). Le sintesi che seguono provengono da **ricerche web mirate** (WebSearch) e dalla conoscenza pubblica. Le URL sono lasciate per consultazione/download manuale dell'utente.

## ⚠️ Caveat epistemico generale (skill `epistemic-rigor`)

Questo documento contiene sintesi prodotte da **WebSearch su poche query** (non triangolazione completa) + **conoscenza pubblica**. Per ogni claim cruciale di mercato/finanziario:
- **Confidence prevalente: low-medium**
- Spesso **fonte singola** (commerciale o press)
- Non triangolato con dati ufficiali (Eurostat, ITU, EUSPA, AIAD, ENAC, AGCOM annual reports)

I numeri qui sono **utilizzabili come baseline esplorativa**, **NON come baseline di decisione finanziaria o gate review**. Per uso "investment-grade" è necessario il lavoro descritto in `riferimenti/audit-rigore-epistemico.md` (debito di rigore residuo DR-001 → DR-015).

**Base rate aerospace da tenere presente** (Regola 7):
- Startup aerospace → revenue operativo: 10-20%
- Programmi HALE solari → operativi commerciali: <30% (vedi lista falliti sotto)
- Studi di fattibilità → progetto realizzato: <50% aerospace
- Type Certification UAS innovativa <5 anni: ~10%

Lista programmi HALE solari falliti / cancellati / mai operativi:
- NASA Helios (crashed 2003)
- Aalto/SoftBank HAWK30 (cancellato 2020)
- Solara 50 / Titan Aerospace (acquisito Google 2014, dissolto 2017)
- Sanswire / StratXX / GlobeTel StratoSat (mai operativo, 2005-2015)
- ScanEagle Solar (R&D only)
- BlueBird PathFinder (cancellato)

→ Citare Zephyr/Sunglider/Skydweller come benchmark è **survivor bias** se non si menzionano anche i fallimenti.

---

## INDICE
1. [Quadro normativo italiano — Studio Fattibilità (art.41 D.Lgs.36/2023)](#1-quadro-normativo-italiano)
2. [Quadro normativo aviazione (ENAC/EASA/U-Space)](#2-quadro-normativo-aviazione)
3. [Spettro radio italiano (AGCOM/PNRF/ITU)](#3-spettro-radio-italiano)
4. [Standard 3GPP NTN](#4-standard-3gpp-ntn)
5. [Competitor HAPS — benchmark globale](#5-competitor-haps)
6. [Programma EuroHAPS — partner italiani](#6-programma-eurohaps)
7. [Mercato HAPS — TAM/SAM/CAGR](#7-mercato-haps)
8. [Piattaforme VTOL/MALE commerciali per Percorso 6A](#8-piattaforme-vtolmale-commerciali)
9. [Ricerca accademica italiana HAPS/UAV solari](#9-ricerca-accademica-italiana)
10. [Compositi a fibre naturali (lino) per aerospace IT](#10-compositi-fibre-naturali)
11. [Earth Observation italiana — Copernicus / ASI / Protezione Civile](#11-earth-observation-italiana)
12. [Finanziamenti — PNRR / EDF / Horizon / Coopfond](#12-finanziamenti)
13. [SNAI Liguria — comuni e aree](#13-snai-liguria)
14. [NASA SE Handbook — riferimento metodologico](#14-nasa-se-handbook)

---

## 1. Quadro normativo italiano

### D.Lgs. 36/2023 — Codice dei Contratti Pubblici (art. 41 e Allegato I.7)

**Due livelli di progettazione** (eliminato il "progetto definitivo" del D.Lgs. 50/2016):
1. **Progetto di Fattibilità Tecnico-Economica (PFTE)**
2. **Progetto Esecutivo (PE)**

L'**Allegato I.7** definisce i contenuti minimi di:
- **Quadro Esigenziale (QE)** — bisogni, vincoli, obiettivi
- **Documento di Fattibilità delle Alternative Progettuali (DOCFAP)** — = trade study NASA SE
- **Documento di Indirizzo della Progettazione (DIP)** — linee guida del RUP
- **PFTE** — il documento
- **Progetto Esecutivo (PE)**

**Elaborati tipici del PFTE:**
1. Relazione generale
2. Relazione tecnica + indagini/sopralluoghi/studi specialistici
3. Relazione di verifica preventiva interesse archeologico (se applicabile)
4. Altre relazioni specialistiche (geologica, idrogeologica, sismica, ambientale)
5. Studio di impatto ambientale (se VIA applicabile)
6. Elaborati grafici (planimetrie, sezioni, prospetti)
7. Calcoli preliminari (strutture, impianti)
8. Computo metrico estimativo
9. Quadro economico
10. Cronoprogramma
11. Piano economico-finanziario (NPV, IRR, payback, ROI)
12. Piano di manutenzione preliminare
13. Piano di sicurezza e coordinamento (per la salute dei lavoratori)
14. Documentazione fotografica del contesto

Fonti:
- [Allegato I.7 — codiceappalti.it](https://www.codiceappalti.it/DLGS_36_2023/Allegato_I_7_Contenuti_minimi_del_quadro_esigenziale,_del_documento_di_fattibilit%C3%A0_delle_alternative_progettuali,_del_documento_di_indirizzo_della_progettazione,_del_progetto_di_fattibilit%C3%A0_tecnica_ed_economica_e_del_progetto_esecutivo_/12883)
- [Allegati testo integrale — bosettiegatti.eu](https://www.bosettiegatti.eu/public/2023_0036_Allegati.pdf)
- [Elenco documenti PFTE rev.1 — Scuole Aperte Milano](https://www.scuoleapertemilano.it/documents/20126/470457961/3_Elenco+documenti+PFTE_REV1.pdf)
- [Art. 41 sintesi — BibLus](https://biblus.acca.it/art-41-nuovo-codice-appalti/)

### DTA Grottaglie 2020 (template aerospaziale di riferimento)

**Titolo:** "GROTTAGLIE. UN AEROPORTO VOLANO DI SVILUPPO. STUDIO DI FATTIBILITÀ di un evento internazionale dell'aerospazio a Grottaglie (TA)"
**Autori:** Giuseppe Acierno, Umberto Malusà
**Data:** maggio 2020
**Committente:** Distretto Tecnologico Aerospaziale (DTA) Puglia, per Regione Puglia — Determinazione n. 57 del 29 maggio 2019, Dipartimento Sviluppo Economico, Innovazione, Istruzione, Formazione e Lavoro — Sezione Internazionalizzazione

**Contenuti chiave:**
- Scenari evolutivi dell'industria aerospaziale (pre-Covid e post-Covid)
- Analisi di Grottaglie come location ottimale (sede GATB — Grottaglie Airport Test Bed)
- Analisi tecnica e infrastrutturale
- Scenario economico-finanziario
- Risk assessment

Riferimento: [DTA Studio Grottaglie PDF](https://www.dtascarl.org/wp-content/uploads/2024/05/GROTTAGLIE-studio-fattibilita.pdf)

### RINA — metodologia ricorrente

- Multi-disciplinary team per ogni feasibility study
- Italian broker ESA Technology Transfer dal 1992
- >150 feasibility study + 40 technology transfer projects
- Riferimento: design team del **Taranto-Grottaglie Spaceport** (collocazione affine al DTA), per accogliere Boeing 747-8 e Virgin Galactic White Knight Two
- Dimensioni valutate da RINA: strategic alignment, economic/financial robustness, risk exposure, **ESG performance**, consistency con good industry practice e financing standards
- Riferimento: [RINA Feasibility](https://www.rina.org/en/technical-and-economic-feasibility-studies)

---

## 2. Quadro normativo aviazione

### U-Space Italia — **stato aggiornato 2026 ⭐**

- **Reg. (UE) 2021/664, 665, 666** in vigore dal **26 gennaio 2023** in tutta UE
- **ENAC** ha pubblicato il **Regolamento U-Space — Edizione 1** in consultazione pubblica (avviso del **14 gennaio 2026**, contributi entro **aprile 2026** a `mobilita.innovativa@enac.gov.it`)
- **D-Flight** (joint ENAV+Leonardo+Telespazio+IDS+Techno Sky) è il **primo USSP+CISP europeo** certificato
- **Prima area U-Space italiana** = **R100 San Salvo** (Provincia di Chieti, Abruzzo) — attiva dal 28 novembre, 35 realtà territoriali coinvolte
- ENAC sta lanciando "il primo U-Space europeo" da gennaio 2026

Implicazione per HALE: il **6A VTOL a Pentema** si inserisce in un contesto U-Space in piena evoluzione regolatoria; possibile dialogo con D-Flight come USSP nazionale.

Fonti:
- [ENAC LG-2023/006-UAS Linee Guida U-Space](https://www.enac.gov.it/app/uploads/2023/12/LG-2023_006-UAS-Linee-Guida-U-Space.pdf)
- [ENAC comunicato gennaio 2026](https://comunicati.enac.gov.it/it/announcement/show/enac-da-gennaio-2026-lancia-il-primo-u-space-europeo-nonostante-la-sospensione-del-progetto-amazon-prime-air-in-italia)
- [D-Flight USSP/CISP — Quadricottero](https://www.quadricottero.com/2025/02/d-flight-prima-in-europa-doppia.html)

### Regolamento ENAC mezzi aerei a pilotaggio remoto

- Edizione 3 (2021) con emendamenti successivi
- Linee guida ENAC per Specific Category (SORA application)
- Riferimento normativo italiano principale, applicato in armonia con Reg.UE 2019/947

### Framework HAPS — gap normativo
- **Nessun regolamento europeo specifico per HAPS civili continuative in operazioni commerciali** alla data corrente
- EASA può procedere con **Special Condition** custom (es. SC-Light-UAS per UAS <600 kg, ma HALE è >600 kg in alcuni concept)
- ITU riconosce HAPS in Radio Regulations da WRC-19, ulteriori provvedimenti WRC-23 (Dubai 2023)

---

## 3. Spettro radio italiano

### AGCOM e PNRF
- **PNRF (Piano Nazionale Ripartizione Frequenze)** — gestito da **MIMIT**, aggiornato integrando le risultanze WRC-23
- **AGCOM** rilascia licenze individuali per usi commerciali del radio spettro (art. 11 D.Lgs. 259/2003, ora aggiornato dal D.Lgs. 207/2021 Codice Comunicazioni Elettroniche)
- Coordinamento internazionale ITU per allocazioni HAPS

### Bande HAPS riconosciute ITU
- **31-31.3 GHz** (WRC-19)
- **38-39.5 GHz** (WRC-19/WRC-23)
- **47.2-47.5 GHz** (WRC-19)
- **47.9-48.2 GHz** (WRC-19)
- **21.4-22 GHz** (Americas only)
- **24.25-27.5 GHz** (Americas, in discussione globalmente per WRC-27)
- Definizione HAPS ITU: stazione tra **20 km e 50 km** di quota in punto fisso nominale rispetto alla Terra

Fonti:
- [AGCOM Frequenze](https://www.agcom.it/competenze/comunicazioni-elettroniche/reti/frequenze)
- [MIMIT PNRF](https://www.mimit.gov.it/it/digitale/gestione-spettro-radio/piano-nazionale-ripartizione-frequenze)
- [ITU Radio Regulations 2024](https://www.aeranticorallo.it/itu-reso-disponibile-online-radio-regulations-2024-per-gestione-spettro-radio/)

---

## 4. Standard 3GPP NTN

### Timeline evoluzione standard NTN/HAPS

| Release | Documento chiave | Contenuto |
|---|---|---|
| **Rel-15 (2019)** | **TR 38.811** | Use cases NTN, channel models, scenari deployment, HAPS |
| **Rel-16 (2020)** | **TR 38.821** | Soluzioni NR per NTN, HAPS come "caso speciale" con delay/Doppler più bassi |
| **Rel-17 (2022)** | TS 38.300, TS 38.401 ecc. | Work Item NTN: LEO/GEO + implicit support HAPS |
| **Rel-18 (2024)** | NR-NTN enhancements | Mobility, regenerative payloads (first stage) |
| **Rel-19+** | NR-NTN advanced | Full **regenerative payload** (gNB on board), inter-satellite links, flexible scheduling |

### Implicazioni per HALE
- Lo standard NR-NTN **supporta HAPS senza modifiche UE** (TS 38.101-1)
- Il **payload telecom HALE** può ospitare un gNB "regenerative" già nello standard Rel-18/19
- Stesso UE 5G utente terrestre = compatibilità diretta

Fonti:
- [3GPP NTN Overview](https://www.3gpp.org/technologies/ntn-overview)
- [TR 38.811 PDF](https://hscc.csie.ncu.edu.tw/38811.pdf)
- [ArXiv survey NR-NTN 2103.09156](https://arxiv.org/pdf/2103.09156)

---

## 5. Competitor HAPS

### Benchmark tecnico (aggiornato 2025-2026)

| Piattaforma | Operatore | MTOW | Wingspan | Payload | Endurance dim. | Status 2026 |
|---|---|---|---|---|---|---|
| **Zephyr 8/S** | AALTO (Airbus spin) | 60-62 kg | 25 m | 5 kg | 64 giorni (Arizona) | **Commercial entry 2024**, NTT/Space Compass investimento 100M$ per Asia |
| **Sunglider** | AeroVironment + SoftBank | n/d | **78 m** | **75 kg** | flight test stratosferico Aug 2024 New Mexico | **Test, pre-commercial** |
| **Aurora Odysseus** | Boeing (Aurora Flight Sciences) | <880 kg | **74.1 m** | 25 kg + 250W | fino a 1 anno claim | **Sviluppo** |
| **Skydweller** | Skydweller Aero | **2549 kg** | **72 m** | **363 kg** | 90 giorni dimostrati | **Operational 2025** (US Navy AMPA) |
| **PHASA-35** | BAE Systems / Prismatic | 150 kg | 35 m | 15 kg | 24h@66kft, target 12 mesi | **Operativo 2026** |
| **HHAA (CIRA)** | CIRA Italia (EuroHAPS) | n/d (airship ibrido) | n/d | n/d | dimostratore | **Demo 2024 Sardegna+Fuerteventura** |
| **Stratobus** | Thales Alenia Space | dirigibile | n/d | grande | persistente | **Demo EuroHAPS in corso** |

### Posizionamento Firmamento Technologies HALE
- Categoria target: **micro/lite HALE** (più piccolo di Zephyr, comparabile per missione)
- Vantaggio competitivo: **focus territoriale italiano** + integrazione cooperative + missioni dual (telecom + EO)
- Sfida: competere in massa e tech con leader globali → puntare su **specializzazione geografica** + **partnership cooperative** + **sostenibilità (fibra di lino)**

Fonti:
- [Zephyr Airbus](https://www.airbus.com/en/products-services/defence/uas/zephyr) | [Wikipedia](https://en.wikipedia.org/wiki/Airbus_Zephyr)
- [Sunglider SoftBank](https://www.softbank.jp/en/corp/news/press/sbkk/2024/20241002_01/)
- [Odysseus Wikipedia](https://en.wikipedia.org/wiki/Aurora_Odysseus)
- [Skydweller](https://www.skydweller.aero/news/skydweller-aero-successfully-demonstrates-perpetual-flight/)
- [PHASA-35 Wikipedia](https://en.wikipedia.org/wiki/BAE_Systems_PHASA-35) | [Prismatic](https://www.prismaticltd.co.uk/phasa-35/)

---

## 6. Programma EuroHAPS ⭐ (Critico per Firmamento)

**Progetto European Defence Fund** che potrebbe diventare partner strategico/finanziatore per il Percorso 6B.

- **Coordinatore:** Thales Alenia Space (JV Thales 67% / Leonardo 33%)
- **Budget:** €63.52M totale, **€43M contributo UE** (EDF)
- **Selezione:** Commissione Europea, luglio 2022 (call EDF)
- **Durata:** 38 mesi
- **Partner principali:** **CIRA**, **Elettronica**, **Leonardo** (Italia), ONERA, CEA (Francia), INTA (Spagna), ESG, TAO (Germania)
- **Totale consorzio:** 21 partner + 18 subcontractor da 11 paesi

### Tre dimostratori HAPS in EuroHAPS:
1. **Stratobus ridotto** (Thales Alenia Space) — dirigibile
2. **HHAA — Hybrid High Altitude Airship** (**CIRA**, Italia) — dirigibile ibrido con superficie alare per lift extra (brevettato CIRA)
3. **ASBaS — Autonomous Stratospheric Balloon System** (ESG/TAO Germania) — pallone autonomo con 3 quote controllabili

### Demonstration flights
- **Sardegna (Italia)** — pianificato 2024
- **Fuerteventura (Canarie)** — pianificato 2024

### Implicazioni per Firmamento — ⚠️ correzioni epistemiche

**Errore di framing originario corretto:**
- EuroHAPS è **EDF (difesa)**, non programma civile.
- CIRA sviluppa **HHAA — Hybrid High Altitude Airship** (dirigibile ibrido con superficie alare) brevettato, **non** UAV solare HALE come Firmamento. Concept diversi.
- Il consorzio è chiuso (TAS/Leonardo/Elettronica IT + ONERA/CEA FR + INTA ES + ESG/TAO DE). **Firmamento NON è dentro** né è prossimo a esserlo.

**Posizione realistica:**
- EuroHAPS è **landscape** strategico-tecnico-industriale, non partner attuale o trampolino acquisito.
- CIRA è **possibile interlocutore** per partnership R&D futura sul Percorso 6B, ma da costruire da zero. Engagement deliberato Y1-Y2 necessario.
- Sinergie con **GATB Grottaglie** per il Percorso 6A: plausibile come **test bed** ma da formalizzare con accordo specifico.
- **Future call EDF/Horizon HAPS-related**: possibili, ma la maggior parte sarà aperta a consorzi grandi (Tier 1 EU aerospace). Firmamento accederà come **partner di consorzio**, **non** come prime.

→ Vedi `audit-rigore-epistemico.md` CLAIM-005 e INC-003 per correzione tassonomia HAPS vs HALE solare.

Fonti:
- [Italian Defence Tech — CIRA in EuroHAPS](https://www.italiandefencetechnologies.com/in-the-edf-eurohaps-project-cira-leads-the-development-of-the-italian-stratospheric-platform/)
- [Thales Alenia Space announcement](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-signs-contract-european-commission-and-announces-kickoff)

---

## 7. Mercato HAPS

### Dimensionamento globale (2024-2032)

| Fonte | Mercato | 2024 | 2030/2032 | CAGR | Note |
|---|---|---|---|---|---|
| MarkNtel Advisors | **HAPS strict** (pseudo-satellites) | $99M | **$240M (2030)** | **16%** | Solo HALE/HAPS |
| Coherent Market Insights | HAP wide (incl. airships) | $1.73B (2025) | $2.93B (2032) | 7.8% | Tutte le piattaforme |
| Credence Research | HAP wide | $1.74B | $3.10B (2032) | 7.4% | Tutte le piattaforme |
| Grand View Research | HAP wide | $1.54B (2023) | $2.66B (2030) | 8.4% | Tutte le piattaforme |

### Driver di mercato
- Persistent surveillance
- Broadband expansion (rural/digital divide)
- Solar-powered tech advances
- Disaster relief / emergency comms

### Composizione
- **UAV (HALE solari)**: 60% market share dominante
- Airship/dirigibili: 25-30%
- Balloon stratosferici: 10-15%

### Posizionamento Italia
- Mercato italiano potenziale (TAM-IT): stima 2-5% del globale (Italia ha mercato aerospace ~5% UE)
- **TAM-IT 2030 estimato:** $5-12M HAPS strict + $40-80M HAP wide
- **SAM-IT** (PA + Protezione Civile + cooperative + telco backhauling) - stima preliminare 30-40% del TAM
- **SOM** (Firmamento 5° anno operatività): 5-10% del SAM

Fonti:
- [MarkNtel HAPS 2030](https://finance.yahoo.com/news/high-altitude-pseudo-satellites-haps-105900735.html)
- [Coherent Market](https://www.coherentmarketinsights.com/industry-reports/high-altitude-platforms-market)
- [Grand View Research](https://www.grandviewresearch.com/industry-analysis/high-altitude-platforms-market-report)

---

## 8. Piattaforme VTOL/MALE commerciali

### JOUAV CW-30E — candidato baseline Percorso 6A

| Parametro | Valore | Note |
|---|---|---|
| MTOW | ~38 kg | hybrid VTOL fixed-wing |
| Payload max | **8 kg** | conforme al Briefing |
| Autonomia | **480 min (8 h)** | gas/heavy oil + batt |
| Data link range | **200 km** | ottimo per BVLOS Pentema |
| Propulsione | Hybrid gasoline / heavy oil + battery | |
| Operating temp | **-20°C / +55°C** | OK Liguria inverno |
| Wind resistance | 13.9-17.1 m/s | OK eccetto venti estremi |
| Pioggia | ≤10 mm/24h | OK eccetto eventi estremi |
| Anti-icing | Self-heating airspeed tube + battery | OK per Appennino ligure |

Pricing/lead time: **non disponibili pubblicamente** — richiedono contatto vendor (JOUAV ha distributori EU, lead time tipico 4-6 mesi).

Fonte: [JOUAV CW-30E datasheet](https://www.jouav.com/products/cw-30e.html)

### Alternative europee
- Quantum Trinity F90+ (DE): smaller payload, lighter regulations, ITAR-free EU
- Wingtra Gen II (CH): fotogrammetria, lighter scope
- FlyingBasket FB3 (IT-Bolzano): **made in IT**, payload pesante 100 kg, certificato classe

---

## 9. Ricerca accademica italiana

### Politecnico di Torino — DIMEAS ⭐
- **HELIPLAT** (anni 2000): HALE solar-powered + fuel cell H2, target 6-9 mesi
- Prototipo 1:3: wingspan 24 m, lunghezza 7 m (test fino a failure load)
- **SESA** (2007): primo solar light UAV europeo (35 kg)
- Ricerca corrente: **VESPAS-RPAS** (aerodynamic optimization, structural flexibility, aeroelasticity, solar cells)
- Pubblicazioni su ScienceDirect, ResearchGate

### Sapienza Università di Roma
- Materiali compositi con fibre naturali per aerospace sostenibile
- Caratterizzazione tecnica fibre vegetali (lino, canapa, basalto)

### Politecnico di Milano (Polimi)
- Material characterization flax fiber composite crashworthiness (politesi.polimi.it)
- Aeroelasticità velivoli flessibili (gruppo Mantegazza)

### UNIVPM Università Politecnica delle Marche
- Effetti invecchiamento compositi fibra di lino (umidità, ciclica)

Fonti:
- [POLITO DIMEAS HALE UAV](https://www.dimeas.polito.it/en/research/research_groups/design_of_aircraft_and_of_advanced_composite_aerospace_structures/design_manufacturing_and_flight_test_of_innovative_uav_unmanned_air_vehicles_powered_by_solar_energy_and_fuel_cells_fueled_by_hydrogen)
- [Sapienza](https://research.uniroma1.it/materiali-compositi-con-fibre-naturali-sviluppo-sostenibile-ambito-aeronautico)
- [Polimi crashworthiness](https://www.politesi.polimi.it/handle/10589/204938)
- [UNIVPM invecchiamento](https://tesi.univpm.it/handle/20.500.12075/16766)

---

## 10. Compositi fibre naturali

### Fibra di lino — proprietà aerospace

| Proprietà | CFRP (riferimento) | Lino UD | Ibrido lino/CFRP |
|---|---|---|---|
| E (modulo) | 135 GPa | 35-50 GPa | 80-100 GPa |
| ρ (densità) | 1.55 g/cm³ | 1.4 g/cm³ | 1.45-1.5 g/cm³ |
| Resistenza specifica | alta | media | media-alta |
| Smorzamento | basso | **5-10x CFRP** | medio |
| Sostenibilità | media (CO2 ridotta riciclo difficile) | **alta** | medio-alta |
| Costo | alto | medio | medio-alto |
| Vulnerabilità | impatto (BVID) | **umidità** | trade-off |

### Case study italiano: **Biogear** ⭐
- **Fuko (Roma) + Turtle Srl (Bologna)**
- Helicopter landing gear ibrido **CFRP + flax fiber**
- **-54% peso** vs struttura metallica
- Esempio commerciale italiano di applicazione aerospace

### Driver per HALE
- **Smorzamento naturale** del lino → riduzione flutter su ala high-AR
- **Carbon footprint** ridotto → narrativa ESG per finanziatori
- **Vulnerabilità umidità** → mitigazione con cappotti CFRP

Fonti:
- [CompositesWorld Biogear](https://www.compositesworld.com/articles/carbon-fiberflax-landing-gear-achieves-54-weight-reduction-via-tailored-layup-optimization)
- [MaTech compositi lino](https://matech.it/materiali/compositi-in-fibra-di-lino/)

---

## 11. Earth Observation italiana

### Copernicus + ASI
- **e-GEOS** (Telespazio 80% + ASI 20%) — servizi Copernicus per Italia
- Servizi rilevanti per HALE:
  - **Copernicus EMS** (Emergency Management Service) — attivato ripetutamente dalla **Protezione Civile Italiana** per alluvioni e frane in Liguria
  - **Servizio nazionale movimento del suolo** basato su Sentinel-1 (DInSAR)
  - Antincendio: avvistamento + allerta da satellite (ma con limiti di latenza/copertura)

### Vantaggio competitivo HAPS vs Copernicus
| Caso d'uso | HAPS @20 km | Copernicus Sentinel |
|---|---|---|
| Frane (DInSAR) | Persistent over AOI | Revisit 6-12 giorni (S-1) |
| Antincendio early detection | <5 min alert | Ore-giorni (S-2/S-3) |
| Risoluzione | 0.3-1 m | 10 m (S-2 ottico) |
| All-weather | OK (sotto le nuvole) | SAR (S-1) sì, ottico no |

### Protezione Civile + droni
- **ARPA Liguria** ha già una **rete UAS** del Dipartimento di Protezione Civile (esercitazione Spotorno 2024)
- Squadra Droni ANA-PC (Alpini): monitoraggio + recupero dispersi
- DiBRIS Università Genova: ricerca operativa squadre droni
- **Rete italiana**: Rescue Drones Network OdV

Fonti:
- [ASI Copernicus](https://www.asi.it/en/earth-science/copernicus/)
- [ARPA Liguria droni](https://www.arpal.liguria.it/home-page/notizie-tematiche/item/scenario-emergenziale-anche-i-droni-di-arpal-si-esercitano.html)
- [ISPRA Copernicus emergenze](https://www.isprambiente.gov.it/it/programma-copernicus/notizie/uso-del-prodotto-copernicus-a-supporto-delle-emergenze)

---

## 12. Finanziamenti

### Coopfond — Programma COODING (Legacoop) ⭐
- **COODING Prototypes 2025**: budget **€500k** (Fondo Servizi Reali)
  - Per gruppi di **≥10 cooperative aderenti Legacoop**
  - Contributi **max €50k/progetto**, **fino al 50% spese**
  - ✓ Allineato al perimetro Firmamento (rete 10 cooperative)
- **COODING-Invest**: budget **€2.5M** totali
  - Max **€250k per cooperativa**
  - Per innovazione/trasformazione digitale
- **Piano Legacoop totale**: €10.6M su 6 programmi
- Supporto **Fondazione PICO ETS**

### PNRR Aerospazio
- ESA: **€1.3 mld**
- ASI: **€880M**
- Programma **IRIDE**: costellazione 34+35 satelliti EO (SAR/ottico/iperspettrale/IR)
- **Space Factory 4.0** (Thales Alenia Space): sistema interconnessione fabbriche spaziali entro 2026
- **IS4Aerospace Torino** (Polito): €23.6M PNRR MUR — Hub innovazione aerospaziale

### European Defence Fund (EDF)
- **EDF 2026 Work Programme**: **€1 mld** approvato 17 dicembre 2025
- 31 call topic, 7 thematic + 3 non-thematic + 1 hypersonic + 2 medical countermeasures
- Programma in corso: **EuroHAPS** (€43M EU, CIRA partner italiano)

### Horizon Europe (civilian R&I)
- Pillar 2: Cluster 4 (Digital, Industry, Space) + Cluster 5 (Climate, Energy, Mobility)
- Calls aperti su NTN, UAS, EO, sustainable composites
- ASD-Eurospace: roadmap aerospace EU

Fonti:
- [Coopfond](https://www.coopfond.it/cosa-facciamo/finanziamenti/)
- [Legacoop bandi](https://generazioni.legacoop.coop/bandi-e-finanziamenti/)
- [PNRR Spazio MIMIT](https://www.mimit.gov.it/it/pnrr/progetti-pnrr/pnrr-tecnologie-satellitari-ed-economia-spaziale)
- [EDF Commission](https://defence-industry-space.ec.europa.eu/eu-defence-industry/european-defence-fund-edf-official-webpage-european-commission_en)
- [Horizon Europe](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en)

---

## 13. SNAI Liguria

### Aree SNAI 2021-2027 Liguria — 4 aree riconosciute

#### **Valli dell'Antola e del Tigullio** ⭐ (area target HALE/Pentema)
**16 comuni:** Bargagli, Borzonasca, Davagna, Fascia, Fontanigorda, Gorreto, Lumarzo, Mezzanego, Montebruno, Ne, Propata, Rezzoaglio, Rondanina, Rovegno, Santo Stefano d'Aveto, **Torriglia**

**Pentema è frazione del Comune di Torriglia (GE)** — confermato in SNAI Liguria.

#### Beigua-Sol — 8 comuni
Campo Ligure, Masone, Mele, Mioglia, Pontinvrea, Rossiglione, Sassello, Stella, Tiglieto, Urbe

#### Valle Arroscia — 11 comuni
Armo, Aquila d'Arroscia, Borghetto d'Arroscia, Cosio d'Arroscia, Mendatica, Montegrosso Pian Latte, Pieve di Teco, Pornassio, Ranzo, Rezzo, Vessalico

#### Val di Vara — 13 comuni
Beverino, Borghetto di Vara, Brugnato, Calice al Cornoviglio, Carro, Carrodano, Maissana, Pignone, Riccò del Golfo, Rocchetta di Vara, Sesta Godano, Varese Ligure, Zignago

### Importanza per HALE
- **Pentema (Torriglia)** è già in area SNAI riconosciuta → razionale finanziamento PA forte
- Espansione naturale: tutte le 4 aree liguri condividono problematiche simili (orografia, spopolamento, gap digitale)
- Possibile **scale-up regionale** post-pilota Pentema

Fonti:
- [Regione Liguria SNAI](https://www.regione.liguria.it/homepage-fondi-europei/cosa-cerchi/strategia-nazionale-aree-interne.html)
- [PoliticheCoesione SNAI 2021-2027](https://politichecoesione.governo.it/it/politica-di-coesione/strategie-tematiche-e-territoriali/strategie-territoriali/strategia-nazionale-aree-interne-snai/le-aree-interne-2021-2027/)
- [Elenco SNAI Liguria PDF](https://politichecoesione.governo.it/media/rpipea3z/elenco_aree_snai_14-20-e-21-27_20231012.pdf)
- [Dossier SNAI Regione Liguria](https://politichecoesione.governo.it/media/3171/snai-dossier-regionale-liguria.pdf)

---

## 14. NASA SE Handbook

- **Titolo:** NASA Systems Engineering Handbook
- **Edizione corrente:** NASA SP-2016-6105 **Rev 2** (supera SP-2007-6105 Rev 1)
- **Disponibile gratuitamente** (NASA pubblica dominio):
  - [nasa.gov PDF](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)
  - [LaRC LWS PDF](https://soma.larc.nasa.gov/lws/pdf_files/12%20NASA_SP-2016-6105%20Rev%202.pdf)
  - [NTRS](https://ntrs.nasa.gov/citations/20170001761)

**Nota:** download diretto bloccato dal runtime cloud. Si raccomanda download manuale da parte dell'utente e archiviazione in `riferimenti/fonti/NASA_SE_Handbook_Rev2.pdf` per riferimento offline.

---

## Bibliografia originale (utente — 20 fonti citate)

| # | Fonte | Categoria | Status download |
|---|---|---|---|
| 1 | [DTA Grottaglie Studio Fattibilità](https://www.dtascarl.org/wp-content/uploads/2024/05/GROTTAGLIE-studio-fattibilita.pdf) | Fac-simile aerospace IT | ⚠️ Blocked by runtime |
| 2 | [BibLus PFTE elaborati](https://biblus.acca.it/progetto-fattibilita-tecnico-economica-elaborati/) | Codice Contratti | ⚠️ Blocked |
| 3 | [ENAC AAM Business Plan PDF](https://www.enac.gov.it/app/uploads/2024/04/03_AAM-Business-Plan_web-1.pdf) | Template ENAC | ⚠️ Blocked |
| 4 | [AM tender D.Lgs.36](https://www.aeronautica.difesa.it/tender/...) | Esempio bando MIL | ⚠️ Blocked |
| 5 | [Camp Otranto ABMT](https://camp-otranto.com/wp-content/uploads/2024/04/04-WEB-ABMT-IT.pdf) | Studio aeroporto | ⚠️ Blocked |
| 6 | [MIMIT Progetto Marocco](https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf) | MIMIT prefattibilità | ⚠️ Blocked |
| 7 | [Tesi Polito aeroport](https://webthesis.biblio.polito.it/28852/1/tesi.pdf) | Accademico | ⚠️ Blocked |
| 8 | [Aeropolis Analisi Costi BP](http://www.aeropolis.it/workshop2014/workshop-24-5-2014/AnalisiCostiBusinessPlan24_05_14.pdf) | Workshop costi | ⚠️ Blocked |
| 9 | [RINA Feasibility Studies](https://www.rina.org/it/technical-and-economic-feasibility-studies) | RINA metodologia | ⚠️ Blocked |
| 10 | [TE2C presentazione](https://www.sogaer.it/sites/default/files/legacy/images/stories/societa/consulenti/presentazione_TE2C.pdf) | Studio ing. aeroportuale | ⚠️ Blocked |
| 11 | [Tesi Polito aerospace](https://webthesis.biblio.polito.it/14893/1/tesi.pdf) | Accademico | ⚠️ Blocked |
| 12 | [core.ac.uk 14692438](https://files01.core.ac.uk/download/pdf/14692438.pdf) | Accademico | ⚠️ Blocked |
| 13 | [CNI L'Ingegnere Italiano 390](https://www.cni.it/images/l_ingegnere_italiano/2025/LIngegnere_Italiano_n.390_web_ld.pdf) | Rivista CNI | ⚠️ Blocked |
| 14 | [Aosp Terni CV Corradi](https://www.aospterni.it/wp-content/uploads/2023/08/CV-RTP-CORRADI.pdf) | CV professionale | ⚠️ Blocked |
| 15 | [Sapienza Guidonia](https://sia.web.uniroma1.it/sites/default/files/allegati/SitoGuidonia_0.pdf) | Studio sito aeronautico | ⚠️ Blocked |
| 16 | [AM Regolamento amministrativo](https://www.aeronautica.difesa.it/wp-content/uploads/2024/02/Regolamento-amministrativo-ex-art.-15-D.Lgs_.-36.2023-POP-AMM-001_Ed.-20.pdf) | Norme AM | ⚠️ Blocked |
| 17 | [Regione Campania Aerospazio](https://regione.campania.it/assets/documents/06-aerospazio-rev-31-08.pdf) | Filiera regionale | ⚠️ Blocked |
| 18 | [Difesa cap tecnico AQ Prof](https://www.difesa.it/assets/allegati/58722/all1_annesso1capitolatotecnicoaqprof.pdf) | Difesa | ⚠️ Blocked |
| 19 | [Federico II Gravina tesi](http://www.fedoa.unina.it/1003/1/Tesi_Gravina_Francesco.pdf) | Tesi UniNa | ⚠️ Blocked |
| 20 | [Bologna AMS Laurea Cuoccio](https://amslaurea.unibo.it/id/eprint/9491/1/cuoccio_davide_tesi.pdf) | Tesi UniBo | ⚠️ Blocked |

**Tutte le 20 fonti sono bloccate dalla network policy del runtime cloud (`host_not_allowed`).** Per il download offline si raccomanda:
1. Esecuzione manuale del download dall'utente (postman/curl da workstation locale)
2. Salvataggio in `riferimenti/fonti/`
3. Conversione `.pdf → .md` con `pdftotext -layout` (toolchain già configurata nel repo)
