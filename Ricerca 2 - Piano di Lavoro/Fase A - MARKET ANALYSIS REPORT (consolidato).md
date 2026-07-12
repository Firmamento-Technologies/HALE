# Fase A — MARKET ANALYSIS REPORT (consolidato)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Sintesi decisionale della Fase A (analisi di mercato del downstream) |
| **Versione** | 1.0 — consolidato |
| **Data** | 2026-07-12 |
| **Base** | 3 passate di deep research (marittimo/mercato · subacquea/PNS · downstream civile) + estrazione fonti primarie d'archivio (PSNAI, istruttoria Liguria) |
| **Metodo** | ~300 agenti di ricerca complessivi, verifica avversariale a voti; confidenze e caveat riportati per ogni dato |
| **Chiude** | Fase A del Piano di Lavoro (reset "market-first") |
| **Apre** | Fase B — analisi comparativa delle architetture (trade study) |

> **Documenti di dettaglio** (stessa cartella): `Fase A - Analisi di Mercato (Deep Research)` · `Fase A - Approfondimento Subacquea (PNS)` · `Fase A - Downstream Civile Terrestre (Deep Research)` · `Fonti primarie - Spesa pubblica SNAI (da archivio)`. Questo file **li sintetizza e li mette in ordine di priorità**.

---

## 0. Executive summary (decision-ready)

L'analisi di mercato "market-first" porta a **tre conclusioni operative**:

1. **Il prodotto è uno solo: una piattaforma aerea multi-ruolo modulare C3 < 25 kg**, con payload intercambiabili. Non un "barcone" generalista né due velivoli separati: **una cellula comune, tanti payload**. Il mercato valida la classe < 25 kg (i sistemi che vincono i contratti pubblici — Flexrotor, AR3/AR5 — sono proprio lì).

2. **La strategia è "multi-ancora → scala".** Due **ancore** politico-istituzionali, entrambe in **Liguria**, finanziano e legittimano il primo velivolo; il **mercato** ne sostiene la crescita:
   - **Ancora civile:** Aree Interne / SNAI (bando già vinto, Regione, Legacoop) → payload monitoraggio/emergenza.
   - **Ancora dual-use:** PNS / cluster subacqueo di La Spezia (NATO COE, EDF) → payload ISR/relay multi-dominio.
   - **Scala di mercato:** sorveglianza marittima (modello EMSA), ispezione infrastrutture, agricoltura di precisione.

3. **Le nicchie con domanda pagante più solida NON sono quelle di partenza.** La connettività alle aree interne (la promessa politica originaria) è **debole sul mercato e mal servita da un C3 a bassa quota**; le nicchie forti sono **marittimo istituzionale, monitoraggio rischi (incendi), ispezione infrastrutture e subacquea/dual-use**.

**Shortlist finale (colpo d'occhio):**

| # | Nicchia | Ruolo | Domanda pagante |
|---|---|---|---|
| **N1** | Sorveglianza marittima istituzionale | Scala | **Alta** (EMSA ~€30 mln/contratto) |
| **N2** | Subacquea / protezione infrastrutture (CUI) | Ancora dual-use + scala | **Alta** (PNS, EDF ~€30 mln) |
| **N3** | Monitoraggio rischi naturali (incendi/dissesto) | Ancora civile | **Alta** (Calabria €5 mln, modello) |
| **N4** | Ispezione infrastrutture lineari (energia/ferro/condotte) | Scala | **Media-alta** (Enel/Terna/RFI) |
| **N5** | Agricoltura di precisione / EO | Scala | Media (dato Italia da quantificare) |
| **N6** | Connettività aree interne | Funzione modulare + gancio politico | **Debole** (mercato) / alta (politica) |

---

## 1. Metodo e base evidenziale

- **3 passate di deep research** (harness fan-out + verifica avversariale a 3 voti): (A) mercato droni + marittimo di superficie; (B) dimensione subacquea + PNS; (C) downstream civile/terrestre. Più **estrazione diretta dei PDF d'archivio** (PSNAI, istruttoria Regione Liguria) per la spesa pubblica.
- **Convenzione confidenza:** *Alta* = confermato dalla verifica (voto ≥2/3), fonte primaria/multipla; *Media* = confermato ma fonte singola/secondaria; *Bassa* = fonte promozionale/non transferibile. Le cifre di mercato sono **direzionali**, da triangolare.
- **Limiti noti:** molte fonti (EUSPA, ESA, trade.gov, siti difesa) sono **bloccate dalla policy di egress (HTTP 403)** → cifre recuperate via ricerca, non lette verbatim. Diverse cifre-slogan (HAPS 1 mln km², divario digitale 2,6 mld persone, GNSS €300→580 mld) sono state **CONFUTATE** e non vanno usate.

---

## 2. Quadro di mercato (sizing)

| Livello | Cifra | CAGR | Anno | Conf. |
|---|---|---|---|---|
| TAM globale droni civili | 44,4 → **83,0 mld USD** | 7,2% | 2026→2035 | Alta |
| SAM Europa droni commerciali | 7,63 → **12,96 mld USD** | 9,3% | 2024→2030 | Media |
| SAM/SOM Italia professionale (B2B/B2G) | **~160 mln EUR** (+10% YoY) | — | 2024 | Media |
| Mercato EO totale (UE/glob.) | 3,5 → **7,9 mld EUR** | — | 2024→2034 | Alta |
| — di cui **servizi EO a valore aggiunto** | 2,8 → **6,7 mld EUR** | — | 2024→2034 | Alta |
| Mercato AUV/sistemi subacquei autonomi | ~3 → **>12 mld USD** | — | 2023→~2033 | Media |

**Struttura Italia:** ~657 operatori professionali (2024), settore **in consolidamento**; le operazioni aeree valgono ~96% del valore; espansione trainata dal **settore pubblico**. → *Non c'è spazio per un service provider generico: serve una nicchia.*

---

## 3. Le nicchie downstream — sintesi comparata

| Nicchia | Committente pagante | Ordine di grandezza | Fit C3 <25 kg | Confidenza domanda | Ruolo |
|---|---|---|---|---|---|
| **N1 Marittimo superficie** | EMSA, Frontex, Guardia Costiera | ~€30 mln/contratto quadro | ✅ (benchmark 25 kg) | **Alta** | Scala |
| **N2 Subacquea / CUI** | PNS, Marina/Difesa, EDF, operatori cavi (Terna/Sparkle) | PNS seed €2 mln/anno; EDF ~€30 mln | ✅ come gateway/relay | **Alta** | Ancora dual-use + scala |
| **N3 Monitoraggio rischi (incendi/dissesto)** | Regione, Protezione Civile, VVF | €5 mln (modello Calabria) | ✅✅ (fit ottimo) | **Alta** | Ancora civile |
| **N4 Ispezione infrastrutture lineari** | Enel, Terna, RFI, Snam, Autostrade | mercato ricorrente B2B | ✅ (tratte lunghe) | Media-alta | Scala |
| **N5 Agricoltura precisione / EO** | Aziende agricole, cooperative | segmento EO n°1 (~21%) | ✅ | Media | Scala |
| **N6 Connettività aree interne** | (poco provato) Protez. Civile, telco | non quantificato | ⚠️ solo tattico/locale | **Debole** | Funzione + politica |

**Nota di lettura:** il **Golfo di Genova** ospiterebbe già un servizio EMSA RPAS (AR-5 Evo, consorzio REACT) a supporto della Guardia Costiera — **domanda marittima finanziata sul territorio ligure**, da verificare come priorità (N1). Il **PNS di La Spezia** (N2) è la seconda ancora, stessa regione.

---

## 4. La strategia: "multi-ancora → scala", prodotto multi-ruolo

```
 ANCORE (finanziano/legittimano)                    SCALA (mercato pagante)
 ┌───────────────────────────┐                     ┌──────────────────────────┐
 │ N3 Aree interne / SNAI     │  ── payload ──►     │ N1 Marittimo (EMSA-like) │
 │  (civile, bando vinto)     │   monitoraggio      │ N4 Ispezione infrastrutt.│
 │ N2 PNS / La Spezia         │   ISR / relay       │ N5 Agricoltura / EO      │
 │  (dual-use, difesa/EDF)    │   EO / termico      │ (N2 come mercato subacq.)│
 └───────────────────────────┘                     └──────────────────────────┘
            ▲  entrambe in LIGURIA                          │
            └──────── UN'UNICA PIATTAFORMA C3 <25 kg MODULARE ┘
                       (payload intercambiabili)
```

- **Risolve la domanda aperta "generalista vs specializzati"** → **piattaforma comune modulare** (né barcone, né due velivoli).
- **Due ancore, non una:** l'aggancio dual-use (PNS/EDF) porta budget diversi e più capienti; l'aggancio civile (SNAI) porta il bando già vinto e la sponsorship politica. Stessa Liguria.
- **⚠️ La connettività** (N6, promessa politica) resta come **funzione di missione modulare** (relay tattico, gateway IoT di vallata) e **gancio narrativo**, non come business portante: un C3 a bassa quota non è un HAPS.

---

## 5. Shortlist finale con tesi di valore

- **N1 — Marittimo istituzionale.** Domanda pubblica ricorrente e finanziata (modello data-as-a-service EMSA); benchmark tecnico nella vostra classe; lead sul Golfo di Genova. *Il mercato di scala più solido.*
- **N2 — Subacquea / protezione infrastrutture (CUI).** Seconda ancora dual-use a La Spezia (PNS, NATO COE) + mercato in crescita; **varco competitivo libero**: il "gateway aereo leggero → dominio subacqueo" non è presidiato dagli incumbent (che sono pesanti: AWHero 200 kg). *Ancora + scala.*
- **N3 — Monitoraggio rischi (incendi/dissesto).** Proof-point diretto della strategia (Calabria €5 mln FESR per hub-drone); fit tecnico ottimo per un C3 ad alta persistenza; coerente con l'ancora aree interne e con Pentema. *L'ancora civile operativa.*
- **N4 — Ispezione infrastrutture lineari.** Committenti paganti multipli e ricorrenti (Enel, Terna, RFI); il vostro spazio è la **tratta lunga** dove la persistenza paga. *Scala B2B.*
- **N5 — Agricoltura di precisione / EO.** Segmento EO n°1 e in crescita; dato Italia/WTP da quantificare. *Scala, da validare.*
- **N6 — Connettività aree interne.** Debole sul mercato, forte in politica → **payload modulare + storytelling**, non business portante.

---

## 6. Profili di missione consolidati → INPUT FASE B

Griglia derivata dai sistemi realmente in servizio e dalle esigenze delle nicchie. **È l'input diretto per il trade study delle architetture (Fase B, WP-B1/B3).**

| Nicchia | Payload | Persistenza | Area/Raggio | Quota | Comms/Latenza | Lancio |
|---|---|---|---|---|---|---|
| N1 Marittimo | EO/IR + radar (8 kg) | 10–14 h | ampio, sul mare | ≤ ~21.000 ft | real-time + **BLOS/SATCOM** | anche da nave (5×5 m) |
| N2 Subacquea/gateway | relay comms + EO/IR + (acustico) | 12–22 h | costiero/offshore | bassa/media | **BLOS**, relay multi-dominio | shipborne |
| N3 Rischi/incendi | EO/**IR termico** + AI a bordo | **alta** (sorveglianza continua) | vallata/area interna | bassa | near-real-time | terrestre |
| N4 Ispezione lineare | RGB + **termografico** + geometrico | media-alta | tratte lunghe | bassa | store/relay | terrestre |
| N5 Agricoltura | **multispettrale**/EO | media | campi/comprensori | bassa | store | terrestre |
| N6 Connettività | **relay LTE/Wi-Fi/LoRaWAN** | alta | locale (vallata) | bassa | gateway | terrestre |

**Requisiti trasversali che la Fase B deve dimensionare:**
- **Endurance vs peso vs payload:** target ambizioso 24 h in classe < 25 kg → tensione fisica da quantificare (WP-B3).
- **BLOS/SATCOM:** essenziale per N1/N2 (relay, oltre-orizzonte).
- **Modularità:** bay payload intercambiabile 6–8 kg.
- **Lancio flessibile:** terrestre + shipborne (5×5 m) per N1/N2.

---

## 7. Mappa del funding / spesa pubblica attivabile

| Tipo | Canale | Importo | Conf. |
|---|---|---|---|
| **Civile (ancora N3)** | SNAI — CIPESS 41/2022 e 42/2022 | €100 mln + €100 mln | Alta (archivio) |
| | SNAI — incremento fondo | €120 mln | Alta (archivio) |
| | SNAI — riparto assegnazione | €172 mln (FSC 100 + FdR 72) | Media (da verificare) |
| | Modello regionale (analogo) | €5 mln (Calabria FESR) | Alta |
| | Bando **Cooding II / Coopfond** | (finanzia lo Studio) | — |
| **Dual-use (ancora N2)** | PNS — seed | €2 mln/anno dal 2023 | Alta |
| | Bando "Underwater Liguria" | ~€7,5 mln | Media (da verificare) |
| | **EDF 2026** — protezione fondali (consorzio) | ~€30 mln (scad. 29/9/2026) | Alta |
| | NATO DIANA / NIF | acceleratore/fondo | Media |
| **Mercato ricorrente** | EMSA / Frontex | ~€30 mln/contratto quadro | Alta |
| | Ispezione (Enel/Terna/RFI) | ricorrente B2B | Media |

**Lacuna residua sull'ancora:** voci **PNRR** (dissesto idrogeologico, connettività aree bianche/grigie) e budget **Protezione Civile** nazionale e **Regione Liguria** in EUR → **da recuperare** (i PDF d'archivio coprono SNAI, non PNRR/Protez. Civile).

---

## 8. Lacune residue e domande aperte (da chiudere prima dello Studio)

1. **PNRR + Protezione Civile/Liguria** in EUR (dissesto, connettività) — completa la metrica dell'ancora.
2. **Verifica lead Golfo di Genova** (EMSA/AR-5 Evo/REACT/Guardia Costiera) — domanda marittima sul territorio.
3. **Numeri di funding PNS** (€7,5 mln bando, ~€50 mln/anno) e **legge subacquea** — verificare sui PDF caricati (Slides_PNS, dossier Camera).
4. **Agricoltura di precisione Italia** — adozione, ettari, WTP per ettaro (Osservatorio Smart AgriFood PoliMi).
5. **Make-vs-buy** — integrare una piattaforma commerciale (Flexrotor/AR3) vs costruire; partner consorzio EDF.
6. **Cifre tabellari SNAI** (€172 mln, riparto) — verificare a vista sul PDF.

---

## 9. Ponte verso la FASE B (trade study delle architetture)

La Fase A consegna alla Fase B:
- **La shortlist nicchie** (N1–N6) con priorità.
- **I profili di missione** (§6) → requisiti tecnici (WP-B1).
- **Il vincolo di prodotto:** piattaforma **unica, modulare, C3 < 25 kg**, con payload intercambiabili e **BLOS**.

La Fase B dovrà:
1. Tradurre i profili di missione in **requisiti "shall"** (WP-B1).
2. Confrontare le **architetture** (VTOL ibrido, ala fissa lancio-assistito, box-wing, MALE leggero) su **mass/energy/link budget** (WP-B2/B3) — nodo chiave: **24 h in < 25 kg è fisicamente possibile? con quale propulsione/payload?**
3. **Matrice di trade-off pesata** sui parametri P1–P8 (WP-B4).
4. **Make-vs-buy** e **costi/tempi/TRL/rischi** (WP-B5/B6).
5. Confermare che **una piattaforma comune** serve N1–N5 meglio di due velivoli (WP-B7, ipotesi guida già emersa).

---

## 10. Indice documenti Fase A e fonti principali

**Documenti (cartella `Ricerca 2 - Piano di Lavoro/`):**
- `Piano di Lavoro - Seconda Ricerca HALE` — metodo e work package
- `Fase A - Analisi di Mercato (Deep Research)` — mercato + marittimo
- `Fase A - Approfondimento Subacquea (PNS)` — subacquea/dual-use
- `Fase A - Downstream Civile Terrestre (Deep Research)` — civile/terrestre
- `Fonti primarie - Spesa pubblica SNAI (da archivio)` — ancora (PSNAI/Liguria)
- **questo file** — sintesi consolidata

**Fonti chiave:** DRONEII · Grand View · trade.gov/Osservatorio PoliMi · **EUSPA EU Space Market Report 2026** · **EMSA** (Flexrotor/AR5, ~€30 mln) · Frontex/Heron · **PNS / NATO Underwater COE / CSSN** (La Spezia) · **EDF 2026** (seabed, ~€30 mln) · **Regione Calabria** (allerta incendi €5 mln) · **Aiviewgroup/RFI** (DOMUS) · **PSNAI** (CIPESS €100+100 mln) · istruttoria Regione Liguria.

---

*Sintesi decisionale della Fase A. Confidenze e caveat come dai report di dettaglio. Cifre di mercato direzionali (triangolare prima dello Studio). Alcune fonti bloccate da policy egress → recupero via ricerca. Chiude la Fase A e apre la Fase B (trade study).*
