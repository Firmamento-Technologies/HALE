# Guida alle Tecnologie e ai Costi per Superare gli Scogli Certificativi (OSO/SORA)
## Mercato (italiano ed estero), workflow operativo e stima dei costi — spiegata semplice

| | |
|---|---|
| **Documento** | Companion tecnologico della `Guida - Certificazione ENAC-SORA per il volo BVLOS`. Per ciascuna "modifica" richiesta dall'ENAC per superare gli obiettivi di sicurezza (OSO), indica **cos'è, chi la produce (Italia/estero), quanto costa**, con un **workflow di equipaggiamento** e una **stima dei costi per scenari**. |
| **A chi serve** | A chi deve **preventivare e comprare** ciò che serve per far volare un drone ~25 kg oltre la vista (BVLOS) — anche senza competenze tecniche pregresse. |
| **Versione / Data** | 0.1 — 2026-07-14 |
| **Nota onestà** | Molti prezzi di questo mercato **sono su preventivo** (non pubblici). Le cifre sono etichettate **[verificato]** (prezzo pubblico con fonte), **[preventivo]** (il venditore non pubblica), **[stima]** (fascia indicativa di settore). **Nessun prezzo è inventato.** |

---

## In una frase

> Per superare gli scogli certificativi servono alcune **dotazioni di sicurezza** (paracadute/blocco del volo, doppio radiocomando, anticollisione, "recinto elettronico", targa elettronica) più **servizi** (piano di volo, formazione, consulenza). **La sorpresa:** il costo dell'hardware "base" è **modesto (~€3.000)**; il conto **esplode** solo in due casi — se voli in **spazio aereo condiviso** (serve l'anticollisione vera, costosissima) o se punti a un **livello di rischio alto (SAIL III+)** che richiede prove di robustezza quasi da aeroplano. **Le scelte giuste di missione valgono più dell'hardware.**

---

## Le sigle nuove (le altre sono nella Guida ENAC-SORA)

| Sigla | Significato | In parole semplici |
|---|---|---|
| **OSO** | *Operational Safety Objective* | Gli **obiettivi di sicurezza** da dimostrare all'ENAC (una checklist che si allunga col rischio). |
| **SAIL** | *Specific Assurance and Integrity Level* | Il **livello di severità** dell'operazione (da I facile a VI severissimo). Più è alto, più cose servono. |
| **FTS** | *Flight Termination System* | Il sistema che **ferma il volo in sicurezza** (blocca i motori / apre il paracadute). |
| **C2** | *Command & Control link* | Il **collegamento radio** che comanda il drone. |
| **DAA** | *Detect And Avoid* | "**Vedere ed evitare**": il sistema che rileva altri velivoli e li schiva. |
| **RID** | *Remote ID* | La "**targa elettronica**" che identifica il drone in volo. |
| **ARC** | *Air Risk Class* | Il **rischio di scontro in aria**; si abbassa volando in spazi tranquilli/riservati. |
| **ADS-B** | *Automatic Dependent Surveillance–Broadcast* | Un segnale che dice "**io sono qui**": i velivoli attrezzati si vedono a vicenda. |
| **MANET** | *Mobile Ad-hoc Network* | Una **rete radio "a maglia"** in cui i nodi si ritrasmettono il segnale (robusta). |
| **MoC 2511** | *Means of Compliance Light-UAS.2511* | Lo **standard europeo** riconosciuto per i sistemi di blocco del volo (FTS). |
| **ASTM F3322** | Standard tecnico americano | Lo **standard di progetto/collaudo dei paracadute** per droni (include l'attivazione automatica). |
| **DOP** | *Drone Operation Plan* | Il **piano di volo** da caricare su D-Flight prima di operare. |
| **DVR** | *Design Verification Report* | La **verifica di progetto** che l'EASA richiede ai livelli di rischio alti (SAIL III+). **È la voce che fa esplodere i costi.** |
| **DOA** | *Design Organisation Approval* | L'**approvazione come "progettista di aeromobili"** (serve solo per certificare il mezzo, non all'operatore). |

---

## 1. Paracadute / blocco del volo (FTS) — la contromisura più richiesta

**Cos'è e cosa vuole l'ENAC.** Un **paracadute** riduce i danni se il drone cade. Ma da solo **non basta**: l'ENAC vuole in genere un **sistema che (a) fermi davvero il volo** (blocco motori) e **(b) si attivi da solo**, con **alimentazione e radio indipendenti** dal resto del drone (così funziona anche se l'autopilota o il radiocomando principale si guastano). Gli standard riconosciuti sono **ASTM F3322** (paracadute con attivazione automatica) e **MoC 2511** (blocco del volo/FTS).

**Il mercato (chi lo fa e quanto costa):**

| Prodotto | Paese | Adatto a | Note | Prezzo |
|---|---|---|---|---|
| **Galaxy GRS** GBS 10/350 | 🇨🇿 Cechia | 15–35 kg | Paracadute balistico, attivazione autonoma | **€1.270–1.550** [verificato] |
| **Drone Rescue DRS-25** | 🇦🇹 Austria | 15–25 kg | **Autonomo**, elettronica indipendente, senza pirotecnica; 600 g | **[preventivo]** (fascia simile) |
| **Opale SAFETECH ST160** | 🇫🇷 Francia | ≤25 kg | Paracadute + kit di attivazione elettronica | ST100 (≤9 kg) €412 [verificato]; ST160 **[preventivo]** |
| **ParaZero** PARASAFE | 🇮🇱 Israele | su misura (incl. VTOL/ala fissa) | **Bundle paracadute + FTS** (taglia i motori); ASTM F3322 | ~**$3.000–5.000+** [stima/rif. retail] |
| **Dronavia** Zephyr/Kronos | 🇫🇷 Francia (venduto in Italia) | classe DJI | **Primo FTS conforme MoC 2511** | FTS **€1.304** / paracadute+FTS **€3.502** [verificato] |
| **Aermatica3D — Terminatore di Volo** | 🇮🇹 **Italia** | classe DJI (FTS, non paracadute) | **FTS** con **radio indipendente 869 MHz**, doppio taglio motori; è il "Kit autorizzazione ENAC" | **[preventivo]** |

> **Da sapere:** per un 25 kg i pacchetti più solidi sono **DRS-25**, **Galaxy GBS 10/350**, **Opale ST160**, oppure **ParaZero** (che unisce paracadute + FTS). Se il paracadute **non** taglia i motori, si aggiunge un **terminatore indipendente** (Aermatica3D 🇮🇹 o Dronavia).
>
> **Costo per un 25 kg:** paracadute autonomo **~€1.300–2.500**; + terminatore separato (se serve) **~€1.300+**; bundle ParaZero **~€3.000–5.000**. **Voce realistica: €1.500–4.500** di hardware.

---

## 2. Doppio collegamento radio (C2 ridondante)

**Cos'è e cosa vuole l'ENAC.** Il **C2** è il "telecomando radio" tra pilota e drone. In BVLOS serve un **secondo collegamento indipendente**, così se un canale cade il drone **non perde il controllo**: o continua sul canale superstite, o va in atterraggio/blocco sicuri. Approcci comuni: **due radio su bande diverse**, **rete a maglia (MANET)**, oppure **cellulare multi-SIM "aggregato"** (più SIM in un tubo unico), eventualmente **+ satellite** per il lungo raggio.

**Il mercato:**

| Prodotto | Paese | Approccio | Peso | Prezzo |
|---|---|---|---|---|
| **Microhard** pMDDL2450 | 🇨🇦 Canada | Radio OEM su banda dedicata (ne servono 2 per la ridondanza) | piccolo | **$449,99** [verificato] |
| **Elsight Halo** | 🇮🇱 Israele | **4× cellulare aggregato + satellite** in un box <100 g — il più usato per il BVLOS | 93 g | **[preventivo]** (~$2.000–3.500 [stima]) + abbonamento dati |
| **Doodle Labs** Mesh Rider | 🇺🇸/🇸🇬 | Rete a maglia MANET, multi-banda | 25–34 g | **[preventivo]** |
| **Silvus** StreamCaster | 🇺🇸 USA | MANET tattico (fascia alta) | 295 g | **[preventivo]** (~$4.000–8.000 [stima]) |
| **uAvionix** microLink | 🇺🇸 USA | Multi-frequenza su spettro aeronautico protetto (C-band) | piccolo | **[preventivo]** |
| *Italia* | 🇮🇹 | Pochi produttori nativi: gli operatori italiani **integrano prodotti esteri** | — | — |

> **Costo per un 25 kg:** coppia OEM economica (2 radio) **~$900–1.300** [verificato]; **Elsight Halo** (soluzione "premium" più diffusa) **~$2.000–3.500** [stima] + SIM/dati; MANET tattico fino a **$6.000–10.000**. **Voce realistica: ~€1.000 (base) → €6.000+ (premium con satellite).**

---

## 3. Anticollisione (DAA) — oppure la scorciatoia dello spazio riservato

**Cos'è e cosa vuole l'ENAC.** Oltre la vista, il pilota non può schivare gli altri velivoli: serve un modo per **rilevarli ed evitarli (DAA)**. Due famiglie: **cooperativo** (tutti trasmettono la posizione via **ADS-B**/transponder: economico e leggero, ma "vede" solo chi è attrezzato) e **non cooperativo** (**radar** o **telecamere con IA** a bordo: vedono tutti, ma **pesanti e costosissimi**).

| Prodotto | Paese | Tipo | Prezzo |
|---|---|---|---|
| **uAvionix pingRX Pro** | 🇺🇸 USA | Cooperativo — ricevitore ADS-B | **$349** [verificato] |
| **uAvionix ping200X** | 🇺🇸 USA | Cooperativo — transponder (trasmette) | **~$5.500–7.000** [rivenditori] |
| **FLARM Atom UAV** | 🇨🇭 Svizzera | Cooperativo — FLARM + ADS-B + RID | **~$1.030** [indicativo] |
| **Aerobits** (TT-SC1, TR-1) | 🇵🇱 Polonia | Cooperativo — moduli ADS-B minuscoli, economici | **[preventivo]** (fascia bassa) |
| **Echodyne EchoFlight** | 🇺🇸 USA | **Non cooperativo** — radar a bordo | **[preventivo]** — **cinque cifre in USD** |
| **uAvionix Casia** (ex-Iris) | 🇺🇸 USA | **Non cooperativo** — telecamera + IA | **[preventivo]** — fascia alta |
| Radar da terra (Robin, Fortem, **Leonardo/IDS** 🇮🇹) | vari + 🇮🇹 | Non cooperativo — a terra, per corridoi | **[preventivo]** — servizio/difesa |

> **La scorciatoia che usano quasi tutti in Italia (costo ~€0):** volando in uno **spazio aereo riservato/segregato** (un volume "prenotato" con NOTAM + piano su D-Flight), il **rischio in aria crolla (ARC-a)** e **non serve alcun DAA elettronico**. → **È così che Horus ha ottenuto il BVLOS (spazio ristretto R315).**
>
> **Costo per un 25 kg:** **~€0** in spazio riservato; **~$350** (solo ricevitore ADS-B) fino a **~$7.000** (con transponder) per il cooperativo; **decine di migliaia** per il radar/ottico non cooperativo. → **Il DAA è la voce che può far esplodere il budget: evitarla con lo spazio riservato è la mossa n.1.**

---

## 4. "Recinto elettronico" (geofencing) + targa elettronica (Remote ID) — quasi gratis

**Cos'è.** Il **geofencing** impedisce al drone di uscire dall'area consentita; il **Remote ID** lo rende sempre identificabile in volo.

| Voce | Prodotto | Prezzo |
|---|---|---|
| **Geofencing** | Incluso **gratis** negli autopiloti open-source (ArduPilot/PX4) | **€0** [verificato] |
| **Remote ID** | **Dronetag** DRI/Beacon 🇨🇿 | **€49–139** [verificato] |
| **Remote ID** | **Aerobits idME** 🇵🇱 | **€79** [verificato] |

> **Costo per un 25 kg:** **~€50–150 in tutto.** È lo scoglio più economico.

---

## 5. Autopilota ridondante — dove il costo esplode a SAIL alto

**Cos'è e quando serve.** L'autopilota è il "cervello". A **rischio basso (SAIL I–II)** basta un autopilota con **sensori tripli ridondanti** e software open-source. A **rischio alto (SAIL III+)** l'ENAC/EASA chiedono **prove di robustezza di progetto** (come per un vero aeromobile): si passa ad autopiloti **certificabili**, molto più cari.

| Prodotto | Paese | Livello | Prezzo |
|---|---|---|---|
| **Cube Orange+** (CubePilot) | 🇦🇺/🇨🇳 | SAIL I–II — tripla IMU, + ArduPilot/PX4 gratis | **~$385** [verificato] |
| **Embention Veronte 4x/DRx** | 🇪🇸 Spagna | **SAIL III–V** — 3–4 core, certificato DO-178C/254 (DAL B) | **[preventivo]** — **quattro/cinque cifre in €** |
| **Auterion Skynode** | 🇨🇭/🇺🇸 | fascia enterprise/difesa | **[preventivo]** |
| **ArduPilot / PX4** | open-source | software (gira sul Cube) | **€0** — ma senza dossier di certificazione formale |

> **Costo per un 25 kg:** **~$385** (Cube + software gratis) a SAIL I–II; **quattro/cinque cifre in €** (Veronte, su preventivo) a SAIL III+. **Salire di SAIL cambia l'ordine di grandezza.**

---

## 6. D-Flight e piano di volo (DOP) — piccoli costi fissi

Per operare in BVLOS serve l'abbonamento **PRO** al portale nazionale **D-Flight** e il codice **QR PRO** del drone (che abilitano il piano di volo DOP). Tariffe **2026** [verificato]:

| Voce | Costo |
|---|---|
| Abbonamento D-Flight **PRO** (necessario per il BVLOS) | **€28/anno** |
| **QR PRO** del drone (necessario per DOP/BVLOS) | **€112** (per drone) |
| Abbonamento/QR **Base** (per il solo VLOS) | €7 + €7 |

> **Costo:** **~€140 il primo anno** (PRO + QR PRO). Trascurabile.

---

## 7. Formazione del pilota (emergenze + SORA)

Per il BVLOS il pilota, oltre al patentino base, deve seguire corsi avanzati: **COM** (comunicazioni), **CRM** (gestione delle emergenze), **SORA**, e la pratica **EU-STS-02** (scenario BVLOS). Prezzi italiani [verificato/stima]:

| Corso | Costo |
|---|---|
| Patentino base A1/A3 | €31 |
| CRM (gestione emergenze) | €290–600 |
| Pacchetto SORA+CRM+COM (es. EuroUSC Italia) | **€1.100** |
| Corso BVLOS EU-STS-02 (teoria+pratica+esame) | ~€800–1.200 |
| **Totale per un pilota "pronto BVLOS"** | **~€1.500–2.500** |

---

## 8. Consulenza SORA + prove di robustezza (design assurance)

- **Consulenza SORA** (redazione dossier ConOps + manuale operativo + accompagnamento ENAC): **[preventivo]** — nessuna azienda pubblica i prezzi. Ancore: **€1.000–5.000** per redigere un pacchetto SORA; realisticamente **€3.000–15.000+** per un 25 kg BVLOS a SAIL II–III. In Italia la più presente nei casi-simbolo è **EuroUSC Italia**; c'è anche **Aermatica3D** (che vende il "kit") e la pan-europea **Murzilli**.
- **Prove di robustezza di progetto (DVR)** — **solo a SAIL III/IV**: l'EASA verifica il progetto a **€250/ora, senza forfait** → da **qualche migliaio a decine di migliaia** di euro secondo la complessità. **È la voce che trasforma un SORA da poche migliaia a un programma a sei cifre.** (Il **DOA**, l'approvazione come progettista, serve per *certificare il mezzo*, non all'operatore.)
- **Assicurazione RC** (obbligatoria): standard €120–458/anno; per il **BVLOS** realisticamente **€300–1.000+/anno**.

---

## 9. Il workflow completo (cosa montare, in che ordine)

```
FASE 1 — PROGETTO DEL DRONE (mettere la sicurezza a bordo fin da subito)
  • Autopilota con sensori ridondanti (Cube Orange+ ~$385) + software (gratis)
  • Predisporre: paracadute/FTS, doppio radiocomando, geofencing, Remote ID
        ↓
FASE 2 — MONTAGGIO DELLE DOTAZIONI DI SICUREZZA
  • Paracadute/FTS autonomo (€1.300–2.500) [OSO rischio a terra]
  • Doppio collegamento radio C2 (€1.000–6.000) [OSO link C2]
  • Remote ID (€50–150) + geofencing (gratis) [OSO contenimento/identificazione]
        ↓
FASE 3 — SCELTA DELLO SPAZIO AEREO (la decisione che sposta di più il costo)
  • Spazio RISERVATO/sandbox → DAA = ~€0  ✅ (via consigliata all'inizio)
  • Spazio CONDIVISO → serve DAA (ADS-B ~$350 … radar decine di k€) ❌ caro
        ↓
FASE 4 — PARTE UMANA E DOCUMENTALE
  • Formazione pilota CRM+SORA+STS-02 (~€1.500–2.500)
  • D-Flight PRO + QR PRO (~€140) + piano di volo DOP
  • Consulenza SORA + manuale operativo (€3.000–15.000)
  • Assicurazione RC BVLOS (€300–1.000/anno)
        ↓
FASE 5 — LIVELLO DI RISCHIO (SAIL)
  • SAIL I–II → autopilota open-source basta, NIENTE DVR ✅
  • SAIL III+ → autopilota certificabile (Veronte, €quattro-cinque cifre)
               + DVR EASA (€250/h → decine di k€) ❌ "muro" di costo
        ↓
FASE 6 — DOMANDA ENAC (tariffa €355 + conguaglio) → autorizzazione
```

**Regola di lettura:** ogni voce serve a spuntare uno o più **OSO**. Le **due decisioni** che spostano il budget di un ordine di grandezza **non sono hardware**, sono: **(1) spazio riservato vs condiviso** (azzera o fa esplodere il DAA) e **(2) SAIL basso vs alto** (evita o impone il DVR).

---

## 10. Stima dei costi — tre scenari

*(Cifre in €. [v] = basato su prezzi verificati; il resto è stima/preventivo. Escluse antenne, integrazione e ricambi.)*

| Voce | 🟢 **Pragmatico** (spazio riservato, SAIL I–II) | 🟡 **Tipico** (SAIL II–III) | 🔴 **Alto** (spazio condiviso, SAIL III+) |
|---|---|---|---|
| Autopilota + software | ~350 [v] | ~350 [v] | 15.000–40.000+ (certificabile) |
| Paracadute / FTS | 1.500 | 2.500–4.000 | 3.000–5.000 |
| Doppio radio C2 | ~1.000 [v] | 2.500–3.500 (Halo) | 6.000–10.000 (+ satellite) |
| Anticollisione (DAA) | **0** (spazio riservato) | 350–1.000 (ADS-B) | 20.000–50.000+ (radar/ottico) |
| Geofencing + Remote ID | ~100 [v] | ~100 [v] | ~150 [v] |
| **Subtotale hardware** | **~€3.000** | **~€8.000–12.000** | **~€45.000–105.000+** |
| D-Flight PRO + QR | ~140 [v] | ~140 [v] | ~140 [v] |
| Formazione pilota | 1.500–2.500 [v] | 2.000–2.500 | 2.500 |
| Consulenza SORA + manuale | 3.000–6.000 | 5.000–15.000 | 15.000+ |
| Assicurazione RC (annua) | ~500 | 500–1.000 | 1.000+ |
| Prove di progetto (DVR) | **0** (non serve) | 0 o qualche k (se SAIL III) | 30.000–100.000+ |
| ENAC (tariffa + conguaglio) | 355 [v] + variabile | 355 + variabile | 355 + variabile |
| **TOTALE INDICATIVO** | **~€8.000–15.000** | **~€20.000–40.000** | **~€90.000–250.000+** |

**Come leggere la tabella:**
- Il percorso **🟢 pragmatico** (BVLOS in spazio riservato, rischio basso) — **quello che useremmo per partire** — costa **~€8.000–15.000**, di cui solo **~€3.000 di hardware**. È perfettamente allineato al benchmark UE ("~€5.000–20.000 senza verifica di progetto").
- Il salto al **🔴 alto** non è colpa dei componenti "base": è **il DAA non cooperativo (spazio condiviso)** e **il DVR (SAIL III+)** a portare il conto a **sei cifre**. Sono **scelte di missione**, non fatalità.
- **Voci "su preventivo" da chiudere con RFQ:** DRS-25/ParaZero (FTS), Elsight Halo (radio), Veronte (autopilota SAIL III+), consulenza SORA. Servono 3–4 preventivi per trasformare le stime in numeri fermi.

---

## 11. In sintesi (per chi ha fretta)

1. **Hardware "base" per il BVLOS ≈ €3.000** (autopilota + paracadute/FTS + doppio radio + Remote ID). Il geofencing è **gratis**.
2. **Il DAA (anticollisione) è la mina:** in **spazio riservato costa €0**; in spazio condiviso costa **decine di migliaia**. → partire in **spazio riservato/sandbox**.
3. **Il SAIL alto (III+) è il "muro":** impone autopilota certificabile + **DVR** (verifica di progetto EASA a €250/h) → **sei cifre**. → tenere **missione e area** a **SAIL ≤ II** all'inizio.
4. **I servizi (formazione, consulenza, assicurazione, D-Flight)** pesano **~€5.000–20.000**, più dell'hardware base — e la **consulenza SORA è su preventivo**.
5. **Percorso di partenza realistico: ~€8.000–15.000 tutto compreso**, in spazio riservato a SAIL basso.
6. **Componenti italiani** disponibili soprattutto per **FTS** (Aermatica3D) e **radar da terra/difesa** (Leonardo/IDS); per **radio, DAA a bordo e autopiloti** il mercato è **estero** → altra conferma dell'opportunità "sovranità" (vedi `Nota Strategica`, §2.2).

---

## Fonti principali

**Paracadute/FTS:** Galaxy GRS (galaxysky.cz; onedrone.com €1.270/1.550) · Drone Rescue DRS-25 (dronerescue.com) · Opale (opale-parachutes.com) · ParaZero (parazero.com) · Dronavia MoC 2511 (dronavia.com; megadron.pl €1.304/€3.502) · **Aermatica3D 🇮🇹** (aermatica.com/kit-autorizzazione-enac) · ASTM F3322 (store.astm.org/f3322-22.html).
**Datalink C2:** Elsight Halo (elsight.com) · Doodle Labs (doodlelabs.com) · Microhard pMDDL2450 $449,99 (modalai.com) · Silvus (silvustechnologies.com) · uAvionix microLink (uavionix.com).
**DAA / Remote ID / autopilota:** uAvionix pingRX $349 (uavionix.com) · Echodyne (echodyne.com) · FLARM Atom UAV (flarm.com) · Aerobits (aerobits.pl) · Dronetag €49–139 (dronetag.com) · ArduPilot geofence/RID gratis (ardupilot.org) · Cube Orange+ ~$385 (cubepilot/RMRC) · Embention Veronte (embention.com).
**Servizi/costi Italia:** D-Flight tariffe 2026 (d-flight.it; droneoperator.it) · ENAC R66-1A €355 / R66-1 €114 (enac.gov.it) · formazione (eurousc-italia.it; italdronacademy.com; dronipro.it) · consulenza SORA (eurousc-italia.it; murzilliconsulting.com) · DVR/EASA €250/h (easa.europa.eu) · assicurazioni (dronezine.it; nesios.com) · benchmark UK CAA SAIL 3 £10.380 (caa.co.uk).

> ⚠️ **Onestà:** i prezzi **[verificato]** sono pubblici e stabili; i **[preventivo]** non sono pubblicati (servono RFQ dirette); gli **[stima]** sono fasce di settore. Diversi siti (EASA, ENAC, D-Flight, vendor) bloccano il fetch automatico: dati raccolti via indicizzazione + corroborazione multipla. **Tempi e costi vanno confermati con 3–4 preventivi e con l'ENAC prima di consolidare un budget.**
