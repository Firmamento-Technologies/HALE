# Fase B — Avionica del Mercato Civile: Custom vs COTS (make-vs-buy, ingegneri, tempi)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Analisi del **parco di modelli civili già in commercio**, classificati per **strategia di avionica** (full custom / semi-custom / full COTS), + **costi, numero di ingegneri e tempistiche** per un prodotto certificabile |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Perimetro** | **Solo civile/commerciale.** Esclusi militare e "civile semi-militare"/dual-use difesa (no ScanEagle, AR3/AR5, JUMP 20, V-BAT, Flexrotor, linee difesa di Quantum, ecc.). Classe: ala fissa e VTOL ad ala fissa ~2–25 kg (mappatura, rilievo, ispezione, agricoltura, delivery, public-safety non-difesa). |
| **Relazione con** | `Avionica ed Elettronica di Bordo` (scelta componenti), `WP-B5 Costi TRL Make-vs-Buy` (stessa logica applicata al powertrain), `Nota Strategica` (sovranità) |
| **Impostazione** | Mercato + economia dell'ingegneria; **ottica certificazione ENAC/EASA (SORA SAIL III+)** come filtro. |

> ⚠️ **Onestà tecnica:** la classificazione custom-vs-COTS è basata su evidenza pubblica (fonti §7); dove il core avionico **non è dichiarato** è segnalato *(flag)*. Le cifre di costo/effort sono in parte **pubblicate** e in parte **modellate** (build-up FTE × costo pieno UE) — etichettate come tali. Nessuna è un preventivo.

---

## 0. Executive summary

1. **Tre strategie di avionica nel mercato civile:** **(A) full custom** (HW del flight controller **e** software di volo in casa), **(B) semi-custom** (integrazione custom di COTS: fork di PX4/ArduPilot, "COTS prodottizzato" tipo Auterion Skynode, oppure core COTS certificabile + elettronica di periferia propria), **(C) full COTS** (Pixhawk/Cube + ArduPilot/PX4 stock, o autopilota OEM usato "as-is").
2. **Chi usa avionica custom (A):** nel civile la **full custom sopravvive in pochi** — i **giganti verticalmente integrati** (**DJI**, **JOUAV**) per volume, e **pochi specialisti storici** dell'ala fissa da mappatura (**senseFly/AgEagle**, **Delair**, **Microdrones**, **Parrot** civile). Trimble/Gatewing (full custom) è stata **assorbita da Delair e dismessa**.
3. **Il mid-market occidentale è migrato su semi-custom (B).** Il pattern dominante oggi: **forkare PX4/ArduPilot** e avvolgerlo in elettronica custom + GCS brandizzata (**Wingtra**, **Skyfront**, **DeltaQuad**), oppure **comprare Auterion Skynode** e ribrandizzarlo (**Quantum Systems**, **Censys**). **Skynode** e il **Cube (CubePilot)** sono i due mattoni che trasformano un aspirante "A" in "B".
4. **Correzioni a miti comuni:** **Wingtra NON è full custom** (fork PX4 → **B**); **Quantum Systems NON è in-house** (ha **ritirato il suo autopilota nel 2021** per Skynode → **B**).
5. **Costo/tempo/ingegneri (verso certificabile, SORA SAIL III, DAL C tipico):**
   - **Full custom (A):** **~20–30 ingegneri**, **~4–6 anni**, **NRE ~€8–20M+** → è "montare una piccola casa avionica". Giustificato solo da **volumi alti (migliaia)** o **sovranità/IP**.
   - **Semi-custom (B):** **~10–14 ingegneri**, **~2–3,5 anni**, **NRE ~€3–7M**.
   - **COTS-certificabile (C):** **~5–8 ingegneri**, **~1–2 anni**, **NRE ~€0,8–2,5M** + HW ricorrente (Veronte 1x €6–7k / 4x €24–27k, o George ~$4k) + licenza data-package.
6. **Raccomandazione per Firmamento (SME, singolo prodotto ~25 kg):** **COTS-certificabile** come default (Veronte/George con data-package DAL), **semi-custom solo** per I/O/potenza custom che il box non ospita, **full custom mai** in questa fase (numeri fuori scala per una startup). Coerente con la logica **BUY-il-core / MAKE-l'integrazione** già usata per il powertrain (`WP-B5`).

---

## 1. Tassonomia delle strategie di avionica

| Classe | Definizione | Onere di certificazione (DO-178C/254/160G) |
|---|---|---|
| **(A) FULL CUSTOM** | HW del flight controller **e** software di volo progettati in casa (autopilota proprietario) | **Tutto a carico tuo** — devi generare l'intera evidenza DAL |
| **(B) SEMI-CUSTOM** | Integrazione custom di COTS: fork di PX4/ArduPilot; "COTS prodottizzato" (Skynode); **core COTS certificabile (Veronte) + board di periferia/potenza proprie** | **Misto** — erediti il DAL del core, **ma** ri-verifichi i fork e qualifichi le tue board |
| **(C) FULL COTS** | Pixhawk/Cube + ArduPilot/PX4 stock, **oppure** autopilota OEM (Veronte/MicroPilot) usato "as-is" | **Minimo lato tuo** — l'onere DAL è del fornitore; a te l'integrazione a livello velivolo |

> Nota: "COTS" non implica "non certificabile". **Veronte "as-is" (C)** è già certificabile perché il fornitore porta il pacchetto DAL; **ArduPilot/Cube stock (C)** invece **non lo è** (nessun DAL) → resta da dimostratore. La differenza la fa **il fornitore del core**, non il fatto di comprare.

---

## 2. Survey del parco civile (classificazione)

| Azienda | Modello | Uso civile | Classe | Evidenza / autopilota | 
|---|---|---|---|---|
| **DJI (Enterprise)** | Matrice M300/M350, M30 | Ispezione, public-safety, mapping | **A** | FC e firmware **proprietari** DJI (A3/N3-class), ESC/gimbal propri; nessuno stack open |
| **senseFly / AgEagle** | eBee X | Mappatura/rilievo ala fissa | **A** | Autopilota proprietario (origine EPFL), MCU Cortex-M4 + firmware C propri |
| **Delair** | UX11, DT26 (civile) | Mapping, ispezione lineare, long-range | **A** *(flag dual-use su DT26)* | "Delair-Tech autopilot", flight-control SW in casa; BVLOS DGAC; assorbì Gatewing |
| **Microdrones** | md4 / mdMapper | LiDAR/rilievo | **A** | OS proprietario "mdOS" + autopilota integrato su singola board |
| **Parrot** | Anafi / Anafi Ai (civile) | Fotogrammetria, ispezione | **A** | Firmware/FC proprietario chiuso (MAVLink-compatibile), Air SDK |
| **JOUAV** | CW-15/25/40 | Rilievo VTOL, energia, public-security | **A** *(flag)* | "All-digital bus avionics" proprietaria, INS+dual-GPS in casa, 400+ brevetti |
| **Trimble/Gatewing** | UX5 | Mappatura (storico) | **A** *(dismesso)* | Autopilota proprietario Gatewing; **linea ceduta a Delair (2016)** |
| **Wingtra** | WingtraOne GEN II | Tailsitter mappatura | **B** | **Fork PX4** (membro Dronecode) + controlli/failure custom + GCS WingtraPilot |
| **Quantum Systems** | Trinity Pro (civile) | Rilievo VTOL | **B** | **"Quantum-Skynode" = Auterion Skynode OEM** (PX4). **Ritirato l'autopilota proprio nel 2021** |
| **Censys** | Sentaero 5/6 | Ispezione BVLOS | **B** | **Auterion Skynode** (PX4 prodottizzato); vecchie unità con Cube Orange |
| **Skyfront** | Perimeter 8/8+ | Ibrido long-endurance | **B** | Firmware "proprietario **basato su Pixhawk/PX4**" + engine-control custom + GCS propria |
| **DeltaQuad** | Evo / Pro | VTOL mappatura/security | **B** | **PX4 + Cube Orange COTS** molto customizzato + companion board "Safety & Performance" propria |
| **Carbonix** | Volanti, Ottano | VTOL long-range (BVLOS) | **B** *(flag: core non dichiarato)* | "Carbonix autopilot software" su elettronica propria; core FC non pubblico (verosim. core OEM certificabile) |
| **Foxtech** | Great Shark, Nova | VTOL mapping/ispezione | **C** | Integratore: **Cube Orange / CUAV X7 / LEO-2** con ArduPilot/PX4 stock |
| **CUAV** | Raefly VT260/240 | VTOL mappatura | **C** | FC **CUAV X7** (standard Pixhawk) con **ArduPilot/PX4 stock** |
| **Event 38** | E400 VTOL | Fotogrammetria | **C** | **ArduPlane QuadPlane** su HW Pixhawk-class; opz. "Ironclad" |
| **Quaternium** | HYBRiX.20 | Ibrido long-endurance | **C** | Datasheet: "flight controller con **ArduPilot**", dual IMU |

### 2.1 Fornitori OEM di autopiloti da cui il civile compra
| Fornitore | Prodotto | Abilita la classe | Note |
|---|---|---|---|
| **CubePilot / Hex-ProfiCNC** | The Cube (Orange/Black) | B, C | Autopilot-on-module standard Pixhawk (ArduPilot/PX4) |
| **Auterion** | Skynode / X / S | B | "COTS prodottizzato": PX4 + mission computer + AuterionOS |
| **Embention** | Veronte 1x / 4x | B, **C certificabile** | **Certificabile DO-178C/254/160G** — il core della via "BUY certificabile" |
| **MicroPilot** | MP2x28 | C | OEM professionale (~850 clienti), non-ITAR |
| **UAV Navigation (Oesía)** | VECTOR | B, C | GNC OEM (aerospace-leaning, vende anche a OEM civili) |

---

## 3. Sintesi: chi usa custom, e dove va il mercato

- **Per volume/fatturato la classe A domina — ma per un solo motivo: DJI** (+ JOUAV in Cina). I due leader di volume sono **verticalmente integrati**; la full custom "diffusa" **non esiste**, è **concentrata in pochi giganti**.
- **Tra gli specialisti occidentali dell'ala fissa da mappatura (la nostra classe), la full custom è rara e in calo:** sopravvivono **senseFly/AgEagle, Delair, Microdrones** — e senseFly ha un autopilota di lignaggio EPFL **maturo, non ri-architettato**; Gatewing (full custom) è stata **assorbita e dismessa**. **La direzione è via dalla A.**
- **Il mid-market si è consolidato sulla B ("COTS forkato/prodottizzato"):** Wingtra/Skyfront/DeltaQuad **forkano** loro; Quantum/Censys **comprano Skynode**. **Skynode e il Cube sono i due mattoni** che rendono "B" un'azienda che altrimenti sarebbe "A".
- **La C è il tier a basso costo/integratore** (Foxtech, CUAV, Event 38, Quaternium): ArduPilot/PX4 stock su HW Pixhawk-standard.

> **Conteggio (19 piattaforme):** ~A 7 · B 6 · C 6 — ma **la A "vera e diffusa" nel nostro segmento sono 3 nomi storici**; tutti i nuovi entranti degli ultimi ~5 anni sono **B o C**.

**Implicazione per Firmamento:** un **nuovo entrante SME non fa avionica full custom** — non lo fa nessun nuovo entrante civile da anni. La scelta reale è **B vs C**, e con l'ottica certificazione la variante vincente della C è il **core COTS *certificabile* (Veronte/George)**.

---

## 4. Costi, ingegneri e tempi per un prodotto certificabile

**Target regolatorio:** SORA **SAIL III** (+ basso SAIL IV) → design-assurance che "morde": OSO#05/#10/#18/#24 a **robustezza media**, criteri di aeronavigabilità riferiti a **DAL C software** (talvolta **DAL B** per il core critico). **Non si costruisce a DAL A** qui → costo molto più basso della "leggenda DAL A".

### 4.1 Dati di ancoraggio (pubblicati)
- **DO-178C:** ~**$100/SLOC** a DAL alto (codice + evidenza). Produttività (SLOC/ing-giorno): **DAL A 3–12 · B 8–20 · C 15–40 · D 25–64** → **DAL C è 2–4× più produttivo (e più economico) di DAL A**.
- Un **componente software DO-178C** complesso: **18–36 mesi e "svariati milioni di $"**; un **sistema completo a DAL A: fino a $25M e 5+ anni**.
- **DO-160G:** 26 sezioni, tipiche 12–18 per box, ~4–8 settimane di laboratorio a campagna.
- **DER / liaison di certificazione:** **~$150–300+/ora**.
- **Autopiloti COTS certificabili (unit):** **Veronte 1x €5.900–7.000; 4x €23.500–27.000** (DO-178C/254 fino a **DAL B**, con **Certification Datapack + MoC SORA SAIL I–VI**); **uAvionix George G2 ~$4.000** (HW **DO-254 DAL-C**, DO-160G/MIL-STD-810H, SW DO-178C via Hionos).
- **Costo pieno ingegnere — Italia:** lordo medio ~€52–54k (junior ~€32k, senior ~€79–85k); on-cost datore ~+38%; **costo pieno/FTE-anno ~€100–120k mid** → **team avionico blended ≈ €110–140k/FTE-anno** *(overhead modellato)*.

### 4.2 Le tre strategie a confronto

| | **A — Full custom** | **B — Semi-custom** | **C — COTS-certificabile** |
|---|---|---|---|
| Cosa fai | FC HW (DO-254) + SW volo (DO-178C) in casa | Board periferiche/potenza custom + core certificabile integrato/forkato | Compri Veronte/George + datapack DAL, qualifichi a livello velivolo |
| **Ingegneri (picco)** | **~20–30 FTE** | **~10–14 FTE** | **~5–8 FTE** |
| Composizione | elettronica/PCB 3–4 · HW complesso/FPGA 2–3 · SW volo 5–7 · GNC 3–4 · RF/TLC 1–2 · sistemi 2–3 · safety&cert 2–3 (+DER) · V&V 4–6 · integrazione 2–3 | HW/PCB 2–3 · SW integr. 2–3 · GNC 1–2 · RF 1 · sistemi 1 · safety&cert 1–2 (+DER) · V&V 2–3 · integr. 1–2 | sistemi/integr. 1–2 · embedded/config 1–2 · GNC/flight-test 1 · HW integr. 1 · RF 0,5–1 · safety&cert 1–2 (+DER) · V&V 1–2 |
| **Tempo a certificabile (TRL 6–8)** | **~4–6 anni** | **~2–3,5 anni** | **~1–2 anni** |
| **NRE avionica** *(modellato)* | **€8–20M+** (→€25M+ se DAL A/B) | **€3–7M** | **€0,8–2,5M** |
| Quota certificazione *(modellato)* | ~40–60% NRE → €3,5–12M | €1,5–3,5M | inclusa (dossier SORA/OSO) |
| HW ricorrente/unità | il tuo (ammortizzi l'NRE) | core COTS + tue board | **Veronte €6–27k / George ~$4k** + licenza datapack *(decine–basse centinaia k€, modellato)* |
| Rischio chiave | costo/tempo da casa avionica | **ogni fork erode il credito di certificazione** ereditato | dipendenza dal fornitore del core |
| Quando conviene | volumi **alti (migliaia)** o IP/sovranità | serve I/O/potenza che il box non ospita | **default SME**, decine–basse migliaia di unità |

---

## 5. Make-vs-buy: la conclusione economica

- **BUY (C):** core certificato a **€6–27k/unità** (Veronte) o **~$4k** (George) + licenza limitata; programma a livello velivolo **~€0,8–2,5M in 1–2 anni con 5–8 persone**. Non ri-derivi l'evidenza DO-178C/254/160G che il fornitore **già possiede**.
- **BUILD (A):** **€8–20M+ NRE in 4–6 anni con 20–30 ingegneri** su 8+ discipline.
- **Breakeven:** per giustificare ~€10M+ di NRE contro un delta COTS di ~€10–25k/unità servono **volumi da alte centinaia a migliaia di unità**, *oppure* un driver non economico (**IP, sovranità/NDAA, capacità non disponibile, sicurezza di fornitura**).
- **SEMI-CUSTOM (B) è l'hedge:** costo limitato a **€3–7M / 2–3,5 anni / 10–14 FTE**, ti fa possedere I/O e architettura di potenza — **ma solo se disciplini il fork** così il credito di certificazione ereditato sopravvive.

---

## 6. Raccomandazione per Firmamento

1. **Baseline: C — COTS certificabile** (Embention **Veronte 1x**, EU 🇪🇸, o uAvionix **George**), con **data-package DAL** e MoC SORA del fornitore. È ciò che rende un SME **certificabile in 1–2 anni con 5–8 ingegneri**, non 4–6 anni con 25. Coerente con `Avionica ed Elettronica di Bordo` §2.
2. **Passa a B (semi-custom) solo dove serve davvero:** board di **potenza/IO** custom per i 4 ESC + genset + payload (`Avionica` §6), tenendo il **core certificato intatto** e i fork minimi/config-controlled.
3. **Full custom (A): no, in questa fase.** I numeri (€8–20M, 20–30 ingegneri, 4–6 anni) sono **fuori scala per una startup** e nessun nuovo entrante civile lo fa. Riconsiderabile **solo** a volumi alti o se la **sovranità** diventasse requisito contrattuale (difesa) — e anche lì, prima **B** che **A**.
4. **Nota sulla sovranità:** la tesi "sovrana italiana" (`Nota Strategica`) si difende meglio **possedendo l'architettura di sistema, l'integrazione e la catena italiana** (come per il powertrain, `WP-B5`) che **rifacendo l'autopilota**: Veronte è **UE (spagnolo)** — sovranità europea, non extra-UE — e l'IP di valore per Firmamento sta nell'**integrazione velivolo + missione**, non nel flight controller. **BUY il core, MAKE l'integrazione.**
5. **Impatto su `WP-B5`:** aggiungere l'avionica alle voci make-vs-buy con questi numeri; il costo di sistema "€150–800k" va rivisto includendo core certificabile + dossier.

---

## 7. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Prezzo licenza data-package DAL (Veronte/George) | RFQ diretta a Embention/uAvionix |
| Core avionico di Carbonix (non dichiarato) | Verifica diretta (benchmark del pattern "B con core certificabile") |
| NRE/cert-cost (qui modellati) | Acquisire "AFuzion — UAVs Applying DO-178C" + pacchetto EASA SAIL III MoC |
| Team reale disponibile in Italia | Mappare competenze DO-178C/DER sul territorio (scarse) → piano di reclutamento/consulenza |
| Scelta B vs C definitiva | Dipende da quanta I/O/potenza custom serve (output di `Avionica` §6) |

---

*Analisi first-order stage-appropriate. Classificazione da evidenza pubblica; cifre in parte pubblicate, in parte modellate (etichettate). Conclusione: nel civile la **full custom è ormai di pochi (DJI/JOUAV per volume; senseFly/Delair/Microdrones storici)**; i nuovi entranti fanno **B o C**. Per Firmamento SME: **COTS certificabile (Veronte/George) come baseline**, semi-custom per I/O, full custom escluso in questa fase — **BUY il core certificato, MAKE l'integrazione**.*

### Fonti principali
**Mercato/classificazione:** DJI A3 https://www.dji.com/a3 · senseFly eBee https://robotsguide.com/robots/ebee · Delair UX11 https://delair.aero/delair-commercial-drones-2/professional-mapping-drone-delair-ux11-2/ · Microdrones https://www.microdrones.com/en/content/benefits-of-the-microdrones-aircraft-platform/ · JOUAV CW-15 https://www.jouav.com/products/cw-15.html · Wingtra (PX4) https://px4.io/project/wingtraone-tailsitter-vtol/ · Quantum-Skynode https://quantum-systems.com/us/trinity-pro/ · Censys/Skynode https://auterion.com/product/skynode-x/ · Skyfront https://skyfront.com/integration · DeltaQuad https://px4.io/project/deltaquad-vtol/ · Foxtech https://www.foxtechfpv.com/foxtech-great-shark-330-vtol.html · CUAV X7 https://www.cuav.net/en/x7-plus-pro-en/ · Event 38 https://event38.com/fixed-wing/e400-vtol-drone/ · Quaternium HYBRiX datasheet https://content.ilabsolutions.com/wp-content/uploads/2019/10/Quaternium-Hybrix.20-Technical-Datasheet.pdf · CubePilot https://www.cubepilot.com/ · Embention Veronte https://www.embention.com/veronte/autopilots/ · MicroPilot https://www.micropilot.com/ · UAV Navigation https://www.uavnavigation.com/products/autopilots
**Costi/tempi/certificazione:** AFuzion DO-178C costs https://afuzion.com/do-178c-costs-versus-benefits/ · AFuzion UAV DO-178C https://afuzion.com/uavs-applying-do-178c-costs-versus-benefits/ · DO-254 effort https://www.militaryaerospace.com/commercial-aerospace/article/14227527/estimating-the-effort-and-cost-of-a-do-254-program · DO-160G https://afuzion.com/do-160g-introduction-for-avionics-testing/ · EASA SAIL III MoC https://www.easa.europa.eu/en/newsroom-and-events/news/easa-finalises-means-compliance-sail-iii-unmanned-aircraft-systems-uas · UAV Navigation SAIL III/IV https://www.uavnavigation.com/enabling-SAIL-III-SAIL-IV-operations · Veronte 4x prezzo https://avpay.aero/company/embention/product/professional-drone-autopilot-4x/ · George G2 prezzo https://irlock.com/products/george-g2-autopilot · Ingegnere aerospaziale Italia https://www.salaryexpert.com/salary/job/aerospace-engineer/italy · Costi datore Italia https://taxsummaries.pwc.com/italy/individual/other-taxes
