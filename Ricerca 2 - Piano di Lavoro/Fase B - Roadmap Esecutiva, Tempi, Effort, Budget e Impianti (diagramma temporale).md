# Fase B — Roadmap Esecutiva: Tempi, Effort, Budget, Remunerazioni e Impianti
## Firmamento Technologies · Piattaforma UAS certificabile classe C3 (BVLOS, SAIL alto)

| | |
|---|---|
| **Documento** | **Diagramma temporale** dell'intero progetto: per **ogni** blocco di lavoro indica **durata, effort (persone/mesi), budget, remunerazioni/finanziamento, laboratori e macchinari** (da possedere vs terziarizzare). Definisce inoltre **come si gestisce il workflow** durante il progetto vero (non lo studio di fattibilità). |
| **Versione / Data** | 0.1 — bozza · 2026-07-16 |
| **Input** | `Trade Study Architetture` (architettura raccomandata), `WP-B5 Costi TRL Make-vs-Buy` (ancore di costo/tempo/TRL), `Avionica ed Elettronica di Bordo` + `Avionica del Mercato Civile — Custom vs COTS` (dimostratore→prodotto, effort avionico), `Telemetria/Data Link/GCS`, `Guida — Tecnologie e Costi per la Certificazione BVLOS`, `Nota Strategica`. |
| **Confidenza** | ⚠️ **Numeri = stime parametriche esplicite**, coerenti con le ancore già nel repository (WP-B5: dimostratore €2–3 mln / prodotto €5–10 mln in 3–4 anni; Custom-vs-COTS: avionica COTS-certificabile 5–8 ing., 1–2 anni). **Non sono preventivi**: vanno chiusi con RFQ, come già indicato negli altri WP. |

> ⚠️ **DISAMBIGUAZIONE — oggetto di questo documento.**
> Questo **NON** è l'**HALE** (piattaforma pseudo-satellitare d'alta quota) che lo Studio **sconsiglia al committente** perché fuori dal suo rapporto costo/beneficio. L'oggetto qui è la **piattaforma alternativa raccomandata**: **UAS ala fissa ad alto allungamento, classe C3 (< 25 kg e < 3 m), propulsione ibrido-elettrica a genset (serie), lancio assistito, modulo VTOL opzionale/removibile, payload modulare 4 kg, endurance di progetto ~20–22 h**, pensata per essere **certificabile a SAIL alto e altamente operabile** — cioè commercialmente competitiva. "Studio di Fattibilità H.A.L.E." resta il **nome del progetto/deliverable**; il **velivolo non è un HALE**.

---

## 0. Sintesi (come leggere questa roadmap)

1. **Il progetto vero corre su due binari in parallelo** (come già stabilito in `WP-B5`): **BUY** (integrare/operare subito una piattaforma commerciale per fatturare e servire le ancore) e **MAKE** (sviluppare il velivolo proprietario). Questa roadmap dettaglia il **MAKE**, ma tiene il BUY come **linea di ricavo che remunera** parte del MAKE.
2. **Il MAKE ha due assi distinti che NON vanno confusi** (nodo chiarito con il gruppo): l'asse **dimostratore→prodotto** e l'asse **airframe nuovo**. Il **dimostratore** (su avionica open Cube/PX4) serve a **smaltire il rischio d'integrazione nuovo** — transizione VTOL, powertrain genset, EMC — **non** a "rifare l'autopilota". L'autopilota si **compra** (BUY) sia nel dimostratore (Cube/PX4) sia nel prodotto (Veronte/George): **nessuno lo riscrive da zero**.
3. **L'esperienza pregressa del team (APS Dope HUBS: due droni ala fissa già volati) è un acceleratore, non un doppione**: rende lo **Stadio 1 / dimostratore più corto ed economico** (toolchain, GCS, RFD868x, procedure di collaudo già padroneggiate). È valorizzata nella stima dei tempi (Fase 3).
4. **Orizzonte a prodotto certificabile e operabile: ~42–48 mesi** (3,5–4 anni), con **primo fatturato dal ~mese 6** (binario BUY / servizi VLOS) e **primo BVLOS in spazio riservato** prima del BVLOS in spazio condiviso.
5. **Impianti: si possiede ciò che serve per *lavorare* (non produrre in serie)** — banco compositi (laminazione/finitura da stampo, cura in forno, sacco a vuoto), **stampa 3D** (maschere, dime, modelli, parti non strutturali), **banco elettronico** (stazioni saldanti professionali, alimentatori, oscilloscopio, strumenti CAN) — e si **terziarizza** ciò che è capital-intensive o richiede accreditamento: **assemblaggio PCB (saldatura a punta calda / reflow SMT), CNC metalli, camera EMC accreditata (DO-160G), galleria del vento, test ambientali/strutturali**.

---

## 1. Il modello di workflow del progetto vero

### 1.1 Doppio binario (dalla `WP-B5`)

```
BINARIO BUY  (subito, genera cassa)          BINARIO MAKE (finanziato, genera IP)
─────────────────────────────────           ────────────────────────────────────
Integra/opera piattaforma COTS               Progetta e costruisce il velivolo C3
Servizi VLOS/EVLOS (ispezione,               proprietario: dimostratore → prodotto
sorveglianza) → RICAVO dal mese ~6           certificabile SAIL alto
        │                                             │
        └──────────► i ricavi e i bandi dual-use ─────┘  RE-MUNERANO il MAKE
                     (EDF/PNRM/DIANA/PNS, SNAI/Liguria)
```

**Regola operativa (dalla `Nota Strategica`, regola n.3):** *VLOS-first, revenue-first*. Non si aspetta il BVLOS per fatturare; i dati VLOS diventano **evidenza per il SORA BVLOS** istruito in parallelo.

### 1.2 I due assi del MAKE (il chiarimento chiave)

| Asse | Domanda a cui risponde | Strumento giusto | Perché |
|---|---|---|---|
| **Dimostratore → Prodotto** | *"Il concetto vola e la missione regge?"* poi *"Genero l'evidenza di certificazione?"* | Dimostratore su **Cube/PX4** (aperto, iterazione rapida, ~€300) → prodotto su **Veronte 1x / George** (pacchetto DAL) | La scatola certificabile è ottimizzata per il *configuration control*, non per l'R&D: farci sopra la messa a punto è più lento e caro, ed erode il credito di certificazione |
| **Airframe nuovo (VTOL+genset)** | *"So gestire transizione, bus del genset, EMC dei 4 motori?"* | **Iron-bird a terra + dimostratore in volo** | È il **delta reale** rispetto ai due ala-fissa già volati dal team: è QUI che il dimostratore guadagna il suo costo |

> **Anti-pattern da evitare (e da non riproporre nei documenti):** "salto il dimostratore e faccio tutto una volta sulla scatola certificabile". Non fa risparmiare un giro — fa fare l'R&D con lo strumento sbagliato. **Il dimostratore non è "farla due volte": è fare i due mestieri giusti (de-risking veloce ≠ evidenza di assurance).**

### 1.3 Cadenza di gestione (governance del progetto)

- **Stage-gate**: ogni Fase si chiude con un **gate decisionale** (criteri go/no-go espliciti, §7). Nessuna Fase a valle parte senza il gate a monte superato.
- **Sprint tecnici** (2–4 settimane) dentro le Fasi, con **backlog** per disciplina (aero, strutture, powertrain, avionica, SW, sistemi, safety&cert).
- **Design reviews formali**: SRR (requisiti) → PDR (preliminare) → CDR (dettaglio) → TRR (prima dei test) → FRR (prima del primo volo). Sono anche **evidenza per gli OSO di progetto** (SORA).
- **Configuration control fin da subito** sul ramo "prodotto" (necessario perché il credito di certificazione del core Veronte/George sopravviva ai fork).

---

## 2. Il diagramma temporale (Gantt sintetico)

Orizzonte **M0–M48**. Le Fasi **si sovrappongono** (concurrent engineering): un blocco parte quando ha gli input, non quando finisce il precedente.

```
                        ANNO 1                 ANNO 2                 ANNO 3                 ANNO 4
                  Q1   Q2   Q3   Q4      Q1   Q2   Q3   Q4      Q1   Q2   Q3   Q4      Q1   Q2   Q3   Q4
F0 Setup & Kickoff  ██                                                                                
F1 Prelim design    ░░  ███ ██                                                                        
   + BUY launch       ███████████████████████████████████████████████████████████████████████  (ricavi)
F2 Detailed design         ██  ████ ███                                                              
   + procurement            
F3 Dimostratore                  ░░  ███ ████ ████ ███                                               
   (build+flight)                     └ iron-bird ┘└ volo/transizione/genset/EMC ┘                   
F4 Prodotto cert.                              ░░  ███ ████ ████ ████ ███                            
   + data-package DAL                              └ migrazione Veronte/George ┘ └ DVR ┘             
F5 Certificazione                                             ░░  ███ ████ ████ ███                  
   + ingresso ops                                                 └ SORA SAIL alto ┘ └ prime ops ┘   
────────────────────────────────────────────────────────────────────────────────────────────────────
Gate               G0        G1        G2/PDR    CDR      G3(1°volo) G4       DVR      G5(BVLOS ok)
```

Legenda: `██` lavoro pieno · `░░` avvio/rampa · la barra BUX (ricavi) è continua dal ~mese 6.

---

## 3. Scomposizione per Fase — durata, effort, budget, remunerazione, impianti

> Costo pieno persona usato: **~€7–10k/persona-mese** (≈ €85–120k/anno), differenziato: profili junior/APS più bassi, profili senior/safety&cert e consulenti DER/SORA più alti (§5.3). PM = persone-mese.

### Fase 0 — Setup & Kickoff · **M0–M3 (3 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | Team-core, allestimento officina/laboratori, freeze dei requisiti ("shall"), RFQ ai fornitori shortlist, impostazione governance e configuration control |
| **Effort** | picco **4 FTE** · ~**12 PM** (systems lead, aero/strutture, avionica/SW, project/quality) |
| **Budget personale** | **~€90–120k** |
| **CAPEX impianti (una-tantum)** | **~€150–300k** — allestimento banco compositi, stampa 3D, banco elettronico, strumentazione (§4) |
| **Remunerazione/finanziamento** | Seed/equity + eventuale contributo APS; costi d'avvio candidabili a bandi startup/innovazione regionali |
| **Impianti coinvolti** | Acquisto e messa a punto di TUTTA la dotazione interna (§4) |
| **Gate G0** | Requisiti congelati, officina operativa, RFQ emesse |

### Fase 1 — Progetto preliminare + lancio binario BUY · **M3–M9 (6 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | Progetto preliminare (aero/pesi/energia di dettaglio, layout genset, architettura avionica/link), **PDR**; in parallelo **acquisto e avvio operativo della piattaforma COTS** per i primi servizi VLOS (cassa) |
| **Effort** | picco **6 FTE** · ~**34 PM** |
| **Budget personale** | **~€270–350k** |
| **CAPEX/OPEX aggiuntivi** | **Piattaforma BUY** €100–250k (o leasing); licenze CAD/CFD; formazione piloti BVLOS ~€1,5–2,5k/pilota |
| **Remunerazione/finanziamento** | **Primo fatturato dal ~mese 6** (servizi VLOS); domande bandi dual-use avviate (EDF/PNRM/PNS) |
| **Impianti** | Banco elettronico (prototipazione avionica), stampa 3D (mock-up, mascheratura), CFD (in-house/cloud) |
| **Gate G1 / PDR** | Preliminare approvato, link budget verificato, BUY operativo e fatturante |

### Fase 2 — Progetto di dettaglio + approvvigionamento sottosistemi · **M6–M15 (9 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | Progetto di dettaglio cellula/strutture, **stampi compositi**, integrazione powertrain genset, scelta e ordine avionica/ESC/link, **CDR**. Prep. banco iron-bird |
| **Effort** | picco **8 FTE** · ~**60 PM** |
| **Budget personale** | **~€480–600k** |
| **CAPEX/OPEX** | Sottosistemi + payload di test (avionica dimostratore, genset, ESC, gimbal) **€200–500k**; **stampi** (CNC terziarizzato) €40–120k |
| **Remunerazione/finanziamento** | Ricavi BUX in crescita + **primo bando dual-use** atteso in erogazione |
| **Impianti** | Banco compositi (primi stampi/parti), stampa 3D (dime, fixture), banco elettronico (cablaggi, integrazione CAN); **CNC stampi terziarizzato** |
| **Gate G2 / CDR** | Progetto congelato per il dimostratore, ordini piazzati |

### Fase 3 — Costruzione dimostratore + campagna di volo · **M12–M28 (16 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | **Iron-bird** (genset+avionica+bus DC a terra) → **dimostratore in volo su Cube/PX4** per smaltire **transizione VTOL, comportamento genset, EMC motori↔magnetometro**, logica lost-link, scenari di lancio/recupero. Iterazione firmware libera |
| **Effort** | picco **9 FTE** · ~**110 PM** |
| **Budget personale** | **~€850k–1,1 mln** |
| **CAPEX/OPEX** | Materiali compositi + 2–3 prototipi/iterazioni **€300–600k**; hardware dimostratore (Cube Orange+ ~€350, RFD868x, ESC, genset di test); **campagne EMC pre-scan interne + una campagna accreditata**; noleggio spazio riservato/sandbox per il volo |
| **Remunerazione/finanziamento** | **Cuore del finanziamento a bando dual-use** (è il "premio di rischio tecnologico" che EDF/PNRM/DIANA finanziano) + ricavi BUX |
| **⏱️ Sconto tempo dagli asset Dope HUBS** | La toolchain open, la GCS e le procedure di collaudo già padroneggiate accorciano il rodaggio del dimostratore: **~2–4 mesi risparmiati** sul fronte "far volare e strumentare", concentrando l'effort sul **delta nuovo** (transizione/genset/EMC) |
| **Impianti** | Banco compositi (pieno regime parti dimostratore), stampa 3D (parti funzionali non strutturali, condotti, staffe), banco elettronico (harness, integrazione, debug CAN), **iron-bird** (auto-costruito); **camera EMC accreditata terziarizzata**; galleria del vento (università) opzionale per il box-wing flagship |
| **Gate G3 / 1° volo (FRR→volo)** | Transizione VTOL dimostrata, genset stabile sul bus, EMC sotto controllo, lost-link deterministico |

### Fase 4 — Prodotto certificabile + data-package DAL · **M24–M42 (18 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | **Migrazione avionica** dal dimostratore al **core certificabile** (Veronte 1x o George = "un Cube reso certificabile"); board di potenza/IO custom (semi-custom solo dove serve); redazione **dossier SORA/ConOps**, OSO, avvio **DVR** per il SAIL alto; GCS su stack certificabile (Veronte Pipe/PCS o Auterion) |
| **Effort** | picco **8 FTE** (+ **consulenti DER/SORA** a chiamata) · ~**130 PM** |
| **Budget personale** | **~€1,2–1,6 mln** |
| **CAPEX/OPEX** | **Core certificabile** Veronte 1x €6–7k (o 4x €24–27k se serve fail-operational) / George ~$4k + **licenza data-package DAL**; GNSS anti-jam €0,8–3k; **consulenza SORA** €3–15k; **DVR EASA €250/h → decine di k€**; camere di prova ambientali/EMC accreditate |
| **Remunerazione/finanziamento** | Ricavi BUX consolidati + secondo bando/PNRM; il DVR è la voce che porta il conto verso le sei cifre → va coperta da bando |
| **Impianti** | Banco elettronico (integrazione core certificabile, test HIL); **assemblaggio PCB delle board custom terziarizzato (saldatura a punta calda / reflow SMT presso EMS house)**; **camera EMC accreditata (DO-160G) terziarizzata**; test ambientali terziarizzati |
| **Gate G4 / DVR** | Data-package DAL acquisito, dossier SORA completo, DVR avviato/superato |

### Fase 5 — Certificazione operativa + ingresso in servizio · **M36–M48 (12 mesi)**
| Voce | Valore |
|---|---|
| **Obiettivo** | Ottenimento **autorizzazione ENAC (SORA 2.5, SAIL alto)**; volo BVLOS **prima in spazio riservato**, poi estensione; dimostrazione operativa; **prime operazioni contrattualizzate** |
| **Effort** | picco **6 FTE** (+ piloti/operatori) · ~**60 PM** |
| **Budget personale** | **~€550–750k** |
| **CAPEX/OPEX** | Chiusura DVR/consulenza; **assicurazione RC BVLOS** €300–1.000+/anno; **OPEX SATCOM** (Iridium Certus 100 ~€60–200/mese/velivolo); D-Flight PRO + QR (~€140); tariffa ENAC (€355 + conguaglio) |
| **Remunerazione/finanziamento** | **Transizione a ricavo prevalente** (servizi BVLOS, data-as-a-service) + code dei bandi |
| **Impianti** | GCS certificabile, kit di campo, ground data terminal; nessun nuovo impianto pesante |
| **Gate G5 / BVLOS ok** | Autorizzazione ottenuta, prima operazione a valore, prodotto "operabile" |

---

## 4. Laboratori, impianti e macchinari — possedere vs terziarizzare

> Principio (dalla richiesta del gruppo): **si possiede ciò che serve a *lavorare* i pezzi e a integrare/collaudare** (uso quotidiano, iterazione rapida, riservatezza dell'IP); **si terziarizza ciò che è capital-intensive, a bassa frequenza d'uso o che richiede accreditamento** (produzione di serie, saldatura a punta calda/SMT, camere accreditate, grandi macchine utensili).

### 4.1 Da POSSEDERE (dotazione interna)

| Impianto / macchinario | A cosa serve | Perché in casa | CAPEX indicativo |
|---|---|---|---|
| **Laboratorio compositi (lavorazione, non serie)** — banco di laminazione, **pompa da vuoto + kit sacco a vuoto**, **forno di cura** (dimensione sezioni d'ala), stoccaggio stampi, aspirazione/estrazione fumi, cappa resine, DPI | Laminazione e **finitura da stampo** delle parti in carbonio/vetro (cellula, longheroni, carenature), riparazioni, iterazioni | Iterazione rapida e riservatezza; è "lavorare" i compositi, non produrli in serie | **€40–90k** |
| **Stampa 3D** — FDM grande formato (+ 1 stampante a resina SLA/MSLA per dettaglio) | **Dime, maschere, fixture di assemblaggio**, condotti, staffe non strutturali, **modelli in scala per galleria/CFD**, mock-up | Serve ogni settimana, azzera i lead-time interni | **€8–25k** |
| **Banco elettronico** — **stazioni saldanti professionali** (temp-controllata + aria calda per rework), alimentatori da banco, **oscilloscopio**, analizzatore logico, multimetri, **strumenti CAN/DroneCAN**, crimpatrici, camera termica economica | Prototipazione avionica, **costruzione cablaggi (harness)**, integrazione e **debug del bus CAN**, pre-scan EMC di prima approssimazione | Cuore dell'integrazione: va fatto in casa, di continuo | **€15–40k** |
| **Banco iron-bird** (auto-costruito) | Powertrain genset + avionica + bus DC **a terra**, prima del volo: transitori, sensori, isolamento guasti | De-risking del delta nuovo senza rischiare il velivolo | **€20–60k** (materiali + genset di test) |
| **Officina meccanica leggera** — trapano a colonna, sega a nastro, utensili manuali, banco, **thrust stand** per motori/eliche | Assemblaggio, montaggio, prove spinta motori | Frequente e a basso costo | **€10–25k** |
| **GCS + kit di volo** — laptop/tablet rugged, ground data terminal, antenna tracking, RC di override | Collaudo e operazioni | Operativo | **€10–30k** |

**Totale dotazione interna indicativa: ~€110–270k** (una-tantum, Fase 0–2).

### 4.2 Da TERZIARIZZARE (fornitori/partner)

| Servizio esterno | Perché fuori casa | Quando serve | Fornitore tipico |
|---|---|---|---|
| **Assemblaggio PCB — saldatura a punta calda / reflow SMT** delle board custom | Richiede linea SMT/forno a rifusione e stencil: capital-intensive e a bassa frequenza. **OK appoggiarsi a EMS house** (come da indicazione del gruppo) | Fase 4 (board di potenza/IO custom) | EMS/PCBA house IT/UE |
| **CNC metalli / stampi** (alluminio, acciaio), waterjet, taglio laser | Grandi macchine utensili, poco usate | Fase 2 (stampi), su richiesta | Officine CNC terze |
| **Camera EMC accreditata (DO-160G)** | Accreditamento indispensabile per l'evidenza di certificazione | Fase 3 (una campagna) + Fase 4 | Laboratori accreditati UE |
| **Galleria del vento** | Impianto non replicabile in casa | Fase 3 (soprattutto box-wing flagship) | Università (es. Pisa/Politecnici) |
| **Test ambientali/strutturali accreditati** (vibrazioni, clima, statica) | Accreditamento + attrezzatura pesante | Fase 4 | Laboratori accreditati |
| **Autoclave** (solo se si adottano prepreg ad alta pressione) | Molto costosa; la baseline usa **cura in forno + sacco a vuoto** (in casa) | Solo se richiesto dal materiale | Terzisti compositi |
| **Consulenza SORA + liaison DER** | Competenza scarsa e a chiamata | Fase 4–5 | EuroUSC Italia, Murzilli, DER indip. |

> **Nota sovranità/IP:** ciò che è **differenziante** (integrazione di sistema, powertrain, laminazione delle parti chiave) resta in casa; ciò che è **commodity accreditata** (SMT, EMC, CNC) si compra. È la stessa logica **"BUY il core / MAKE l'integrazione"** dell'avionica.

---

## 5. Personale e remunerazioni

### 5.1 Composizione del team (rampa)
Da `WP-B5` (6–10 persone) e `Custom-vs-COTS` (avionica COTS-cert.: 5–8 ing.):

| Disciplina | F0 | F1 | F2 | F3 | F4 | F5 |
|---|---|---|---|---|---|---|
| Systems / project lead | 1 | 1 | 1 | 1 | 1 | 1 |
| Aerodinamica / prestazioni | 1 | 1 | 1 | 1 | 0,5 | — |
| Strutture / compositi | — | 1 | 2 | 2 | 1 | — |
| Powertrain (genset/ibrido) | — | 1 | 1 | 1,5 | 1 | 0,5 |
| Avionica / integrazione | 1 | 1 | 1 | 1,5 | 2 | 1 |
| Software / GNC / flight-test | — | 1 | 1 | 1,5 | 1,5 | 1 |
| Safety & certificazione (+DER a chiamata) | 0,5 | 0,5 | 1 | 1 | 1,5 | 1,5 |
| Operazioni / piloti | — | 0,5 | — | — | 0,5 | 1,5 |
| **Picco FTE** | **~4** | **~6** | **~8** | **~9** | **~8** | **~6** |

### 5.2 Effort e costo del personale per Fase (riepilogo)

| Fase | Durata | ~PM | Costo personale |
|---|---|---|---|
| F0 Setup | 3 mesi | 12 | €90–120k |
| F1 Preliminare + BUY | 6 mesi | 34 | €270–350k |
| F2 Dettaglio + procurement | 9 mesi | 60 | €480–600k |
| F3 Dimostratore | 16 mesi | 110 | €850k–1,1 mln |
| F4 Prodotto certificabile | 18 mesi | 130 | €1,2–1,6 mln |
| F5 Certificazione + ops | 12 mesi | 60 | €550–750k |
| **Totale MAKE** | **~48 mesi** (sovrapposte) | **~406 PM ≈ 34 persone-anno** | **~€3,4–4,5 mln (solo personale)** |

### 5.3 Modello di remunerazione (chi paga chi, e come)

- **Nucleo dipendente / assimilato:** ingegneri a tempo (costo pieno **~€85–120k/anno** blended; junior/APS più bassi, senior più alti — ancore Italia da `Custom-vs-COTS` §4.1).
- **Membri APS Dope HUBS:** transizione da **volontariato/collaborazione** a **inquadramento retribuito** man mano che il progetto si finanzia; la loro esperienza pregressa è un **conferimento di valore** (accorcia F3).
- **Consulenti a chiamata (partita IVA):** **DER / liaison di certificazione ~€150–300/ora**; **consulente SORA** €3–15k a pacchetto; specialisti CFD/aeroelasticità spot.
- **Assegni/borse di ricerca** su quota-parte finanziata da bandi (personale junior, dottorandi in convenzione con università partner della galleria del vento).
- **Fonti che remunerano il lavoro:**
  - **Ricavi binario BUY** (servizi VLOS→BVLOS, data-as-a-service) — dal mese ~6;
  - **Bandi dual-use R&D** (EDF, PNRM, NATO DIANA, PNS) — pagano il **premio di rischio** di F3–F4;
  - **Fondi territoriali** (SNAI, Regione Liguria) coerenti con le ancore;
  - **Seed/equity** per F0–F1 (prima che ricavi e bandi entrino a regime).

---

## 6. Budget consolidato

| Fase | Personale | Impianti (CAPEX) | Sottosistemi/prototipi/test/cert | Totale Fase |
|---|---|---|---|---|
| F0 | €90–120k | €150–300k | — | **€0,24–0,42 mln** |
| F1 | €270–350k | (in F0) | BUY €100–250k + licenze | **€0,37–0,60 mln** |
| F2 | €480–600k | — | €240–620k | **€0,72–1,22 mln** |
| F3 | €850k–1,1 mln | (iron-bird incl.) | €300–600k + EMC/galleria | **€1,15–1,7 mln** |
| F4 | €1,2–1,6 mln | — | core cert. + DVR + test €0,2–0,5 mln | **€1,4–2,1 mln** |
| F5 | €550–750k | — | cert./assic./OPEX €0,1–0,25 mln | **€0,65–1,0 mln** |
| **TOTALE** | **~€3,4–4,5 mln** | **~€0,15–0,3 mln** | **~€1,0–2,3 mln** | **≈ €4,5–7,5 mln in ~4 anni** |

> Coerente con le ancore `WP-B5`: **dimostratore volante ~€2–3 mln** (qui: F0→F3 ≈ €2,5–4 mln) e **prodotto operativo/certificabile verso €5–10 mln in 3–4 anni** (qui: totale ≈ €4,5–7,5 mln). Il **binario BUY** e i **bandi** ne coprono una quota significativa: il capitale "a rischio" netto è inferiore al totale lordo.

---

## 7. Milestone e criteri di gate (go/no-go)

| Gate | Mese ~ | Criterio di superamento |
|---|---|---|
| **G0** — Kickoff | M3 | Requisiti "shall" congelati; officina/lab operativi; RFQ emesse |
| **G1 / PDR** | M9 | Progetto preliminare approvato; link budget verificato; **BUY operativo e fatturante** |
| **G2 / CDR** | M15 | Progetto di dettaglio congelato per il dimostratore; ordini piazzati |
| **G3 / 1° volo** | M22–26 | **Transizione VTOL** dimostrata; **genset stabile** sul bus DC; **EMC** sotto controllo; lost-link deterministico |
| **G4 / DVR** | M38–42 | Core certificabile integrato; **data-package DAL** acquisito; dossier SORA completo; **DVR** avviato/superato |
| **G5 / BVLOS** | M46–48 | **Autorizzazione ENAC (SAIL alto)**; prima operazione BVLOS a valore |

---

## 8. Rischi di schedule (e mitigazioni)

| Rischio | Effetto sui tempi | Mitigazione |
|---|---|---|
| **Box-wing flagship** (TRL 4–5) tira i tempi | +6–12 mesi se messo sul percorso critico | Tenerlo **fuori dal percorso critico**: prima la variante *performance* (ala fissa, TRL 8–9), il box-wing come **traccia parallela finanziata dai bandi** |
| **DVR / SAIL alto** (voce a sei cifre, EASA €250/h) | Dilata F4–F5 e il budget | Partire **BVLOS in spazio riservato** (SAIL più basso), salire per stadi; ingaggiare DER **presto** |
| **Lead-time avionica certificabile** (Veronte/George su preventivo) | Ritarda F4 | RFQ già in F0; **dimostratore su Cube/PX4 non dipende** da quei lead-time |
| **EMC motori↔magnetometro** (rischio aperto in `Avionica` §9) | Può richiedere ri-layout | **Iron-bird + INS a doppia antenna** (heading da GNSS) in F3, prima del congelamento |
| **Bandi non allineati nel tempo** | Buco di cassa in F3–F4 | **Ricavi BUY** come cuscinetto; scaglionare le domande; F0–F1 su seed |
| **Competenze DO-178C/DER scarse in Italia** | Colli di bottiglia F4 | Piano di reclutamento/consulenza già in `Custom-vs-COTS` §7; convenzioni universitarie |

---

## 9. Come questo documento si aggancia agli altri WP

- **Architettura** e requisiti "shall": `Trade Study Architetture` (§5 raccomandazione).
- **Ancore costo/tempo/TRL**: `WP-B5` (§3 costi, §4 make-vs-buy).
- **Dimostratore→prodotto e effort avionico**: `Avionica ed Elettronica di Bordo` (§2), `Avionica del Mercato Civile — Custom vs COTS` (§4).
- **Telemetria/link/GCS** (dimostratore open → stack certificabile): `Telemetria, Data Link e GCS` (§2 processo per stadi, §5.2).
- **Costi di certificazione BVLOS/OSO/DVR**: `Guida — Tecnologie e Costi per la Certificazione BVLOS`.
- **Posizionamento e regola VLOS-first/revenue-first**: `Nota Strategica` (§ regole).

---

*Bozza first-order, stage-appropriate. Tutti i numeri di costo/tempo/effort sono **stime parametriche** coerenti con le ancore del repository, da chiudere con RFQ e con l'ENAC prima di consolidare un budget contrattuale. **Oggetto: la piattaforma C3 ibrida certificabile raccomandata — non l'HALE pseudo-satellitare**, che lo Studio sconsiglia al committente.*
