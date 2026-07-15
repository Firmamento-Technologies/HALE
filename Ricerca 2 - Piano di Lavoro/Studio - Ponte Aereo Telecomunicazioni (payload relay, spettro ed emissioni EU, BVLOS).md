# Studio — Ponte Aereo per le Telecomunicazioni (payload relay)
## Come implementarlo nella normativa europea sulle emissioni (RED/spettro), per uso BVLOS, con banda utile alle immagini in tempo reale
### Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio dedicato al **payload "ponte di telecomunicazioni"**: che cos'è, quale banda serve per le immagini in tempo reale, come farlo rientrare nella **normativa europea sulle emissioni radio (Direttiva RED 2014/53/UE + regime spettro CEPT/ETSI/AGCOM)**, cosa offre il mercato **off-the-shelf** e — se insufficiente — **stima tempi e iter regolatorio** per un prodotto proprietario. |
| **Versione / Data** | 0.1 — 2026-07-15 |
| **Collegato a** | `Fase A - MARKET ANALYSIS REPORT (consolidato)` (nicchia **N6 Connettività**) · `Fase B - Trade Study Architetture` (REQ-05 datalink, REQ-04 payload modulare) · `Guida - Certificazione ENAC-SORA per il volo BVLOS` (percorso autorizzativo) · `Nota Strategica - Alternativa Superiore a HALE` (§2.7 certificazioni). Chiude in parte **WP-B8** (normativa/spettro) sul lato telecomunicazioni. |
| **Ambito** | Il **payload di comunicazione** e il suo **spettro**, non la cellula aerea (già trattata nel Trade Study). Piattaforma di riferimento: **C3 < 25 kg, ala fissa ibrida, modulare** (raccomandazione repo). |
| **Onestà** | Standard del `Dossier di Verifica`: ogni affermazione decisiva è **✅ verificata**, **🟡 stima/ordine di grandezza** o **❌ da non usare**. Cifre di prodotto = da schede costruttore, **da confermare con RFQ**. Tempi/costi autorizzativi italiani **non pubblici → stime** (come per il BVLOS nella Guida ENAC). |

---

## 0. Messaggio chiave (per chi ha fretta)

1. **"Ponte aereo di telecomunicazioni" non è una cosa sola: sono tre cose diverse**, con normativa e maturità molto diverse (§2). Vanno tenute separate o si sbaglia il pitch.
2. **Il vincolo fisico del repository resta valido e va rispettato:** un **C3 < 25 kg a bassa quota NON è un HAPS** e **non può fare da infrastruttura di connettività regionale**. Il "ponte" credibile è **tattico/locale** — una **singola vallata, un cantiere, un'emergenza, una tratta punto-punto oltre-orizzonte** — non la copertura di una provincia (`Market §4`, `Downstream Civile §4`). Questo studio **conferma** quel caveat e ci costruisce sopra un caso d'uso **difendibile**.
3. **"Immagini in tempo reale" si traduce in un numero:** servono **~3–9 Mbit/s netti** con **latenza < 0,5 s** (H.265/HEVC). È un requisito **modesto e ampiamente alla portata** dei datalink COTS odierni (§3). Il collo di bottiglia **non è la banda**: è **la portata a bassa quota, la robustezza del link e l'autorizzazione allo spettro**.
4. **La "normativa europea sulle emissioni" per un drone-radio è la Direttiva RED 2014/53/UE** (marcatura CE del ricetrasmettitore) **+ il regime d'uso dello spettro** (bande, EIRP, autorizzazioni CEPT/ETSI/AGCOM). Sono **due permessi distinti**: (a) *l'apparato può essere immesso sul mercato?* (RED) e (b) *posso accendere quella frequenza in volo, lì?* (spettro). §4.
5. **Il mercato off-the-shelf è MATURO per due dei tre tipi di ponte** (relay RF/MANET e cellular-bonding): Silvus, Doodle Labs, Microhard, Persistent Systems, Elsight Halo sono prodotti conformi RED e nella nostra classe SWaP. **Il terzo tipo — la "cella volante" (Cell-on-Wings LTE/5G) su C3 — esiste ma è il pezzo più regolato e meno pronto** in Europa (§5–6).
6. **Raccomandazione: BUY del datalink, il "ponte" come payload modulare.** Non serve inventare la radio: serve **integrarne una conforme RED**, **scegliere la banda giusta per il regime BVLOS/SORA**, e **posizionare il ponte come funzione tattica** (relay + gateway IoT/LoRaWAN + video-backhaul di emergenza), coerente con N6 "gancio politico + payload", non "business portante" (§7). Il "make" proprietario ha senso **solo** sulla banda aeronautica protetta o su un requisito di sovranità di bando (§6).

---

## 1. Glossario minimo (le sigle radio, in parole semplici)

*(Come nella Guida ENAC: leggi questa prima e il resto diventa facile.)*

| Sigla | Per esteso | In parole semplici |
|---|---|---|
| **RED** | *Radio Equipment Directive* — Dir. 2014/53/UE | La legge europea che dice **quando un apparato radio può essere venduto/usato** (marcatura CE). |
| **EMC** | *Electromagnetic Compatibility* | Il tuo apparato **non deve disturbare** gli altri né farsi disturbare (un "requisito di emissione"). |
| **EIRP** | *Equivalent Isotropically Radiated Power* | La **potenza effettivamente irradiata** dall'antenna: è il numero che i limiti di legge fissano. |
| **ISM / SRD** | *Industrial-Scientific-Medical* / *Short Range Devices* | Le bande **"libere"** (2,4 GHz, 5,8 GHz, 868 MHz): niente licenza, ma **niente protezione dalle interferenze** e **potenza bassa**. |
| **C2 / CNPC** | *Command & Control* / *Control & Non-Payload Comms* | Il **"telecomando"** del drone (pilotaggio + telemetria), distinto dai **dati del payload** (il video). |
| **BLOS / BVLOS** | *Beyond Line of Sight* | Comunicazione (o volo) **oltre l'orizzonte/oltre la vista**. |
| **MANET** | *Mobile Ad-hoc Network* | Rete radio **a maglia auto-organizzante**: i nodi si ripetono a vicenda (relay/swarm). |
| **HAPS** | *High Altitude Platform Station* | Pseudo-satellite stratosferico (~20 km). **NON è la nostra macchina** — è la classe che *può* fare connettività regionale. |
| **CoW / Cell-on-Wings** | *Cell on Wings* | **Stazione radio-base (antenna telefonica) montata su drone**: crea una cella LTE/5G volante. |
| **RLAN / WAS** | *Radio LAN / Wireless Access Systems* | Il Wi-Fi (2,4 e 5 GHz) in senso regolatorio. |
| **CEPT / ECC** | Conferenza europea Poste e Telecom / Electronic Communications Committee | Chi **armonizza lo spettro** in Europa (l'ENAC delle frequenze, a livello UE). |
| **ETSI EN** | Standard armonizzato | La **norma tecnica** che, se rispettata, dà **presunzione di conformità** alla RED (es. EN 300 328 per il 2,4 GHz). |
| **AGCOM / MIMIT** | Autorità Garanzia Comunicazioni / Min. Imprese e Made in Italy | Chi **gestisce lo spettro in Italia** (piano frequenze + autorizzazioni). |
| **PNRF** | Piano Nazionale Ripartizione Frequenze | La "**mappa italiana**" di chi può usare quale frequenza. |

---

## 2. Che cos'è, davvero, un "ponte aereo di telecomunicazioni" — tre architetture da non confondere

La richiesta ("ponte aereo per le telecomunicazioni … che permetta un bitstream sufficiente alla comunicazione, con immagini in tempo reale") può voler dire **tre cose tecnicamente diverse**. Distinguerle è il primo atto onesto dello studio, perché **cambiano banda, normativa, maturità e caso d'uso**.

| # | Tipo di "ponte" | Cosa fa in pratica | Chi sono gli utenti a terra | Analogia |
|---|---|---|---|---|
| **T1** | **Relay/estensione di link (RF punto-punto o MANET)** | Il drone **ripete e allunga** un collegamento radio: porta il video/dati di un nodo remoto (a terra, in mare, in una valle cieca) fino a una stazione, **saltando l'orizzonte o un ostacolo**. Nessun "telefono" a terra: due estremi tecnici che il drone connette. | Squadre operative, sensori, un'altra piattaforma, una nave | **Ripetitore volante** / "specchio" radio |
| **T2** | **Gateway di accesso locale (Wi-Fi / LoRaWAN / IoT)** | Il drone porta in quota un **access point**: sotto di lui, dispositivi comuni (sensori LoRaWAN, terminali Wi-Fi) si agganciano e i loro dati salgono via backhaul (RF o SATCOM) verso Internet. | Sensori ambientali, IoT di vallata, presidio temporaneo | **Hotspot volante** locale |
| **T3** | **Cella telefonica volante (Cell-on-Wings LTE/5G)** | Il drone porta una **vera stazione radio-base**: gli **smartphone** normali sotto la sua impronta agganciano rete come con un'antenna a terra. | Cittadini/soccorritori con **telefono normale** | **Antenna telefonica volante** (COW) |

**Perché la distinzione è decisiva:**

- **T1 e T2** usano **bande "libere" o licenziabili come SRD/RLAN** (2,4 / 5,x / 868 MHz) oppure link proprietari, e il drone è **un utilizzatore radio come tanti** → **regime RED "standard", COTS maturo** (§5).
- **T3** trasforma il drone in **operatore/infrastruttura di rete mobile aerea**: tocca **spettro licenziato a un operatore telefonico** e, soprattutto, **l'uso aereo delle reti mobili terrestri non è ancora armonizzato in Europa** → **pezzo più regolato e meno pronto** (§4.5, §6).

> **Il ponte "credibile domani" per Firmamento è T1+T2** (relay tattico + gateway IoT/emergenza), coerente con la nicchia N6 come **funzione modulare**. **T3 (cella volante)** è un **gancio narrativo forte** (Protezione Civile, "riportiamo il segnale nel borgo isolato") ma va presentato come **traguardo condizionato**, non come capacità di partenza.

### 2.1 Il vincolo fisico — ribadito, perché regge il caso d'uso (non lo distrugge)

Il repository ha già stabilito, e questo studio **conferma**, che *«un piccolo drone a bassa quota NON può coprire aree ampie né fare da ponte a LEO come un HAPS»* (`Downstream Civile §4`). La geometria è impietosa: la **portata verso l'orizzonte radio** cresce ~con la **radice della quota**.

| Quota di volo del drone | Orizzonte radio (LOS) approx. | Copertura "a terra" utile | 🟡 |
|---|---|---|---|
| **120 m** (limite Open, tipico BVLOS basso) | **~44 km** teorici, in pratica **5–15 km** utili (ostacoli, terreno, margine link) | una **vallata**, un tratto di costa, un cantiere | stima geometrica standard (d≈4,12·√h[m]) |
| **500 m** (BVLOS Specific autorizzato) | ~92 km teorici | area comunale/valliva ampia | stima |
| **~20 km** (HAPS — **non è la nostra macchina**) | ~600 km | regionale | fuori scope C3 |

**Lettura strategica (allineata al repo):** a 120–500 m il "ponte" **serve bene una scala tattica/locale** — ed è **esattamente** ciò che chiede l'ancora aree interne (una valle isolata, un'emergenza, Pentema) e la sorveglianza costiera N1/N2. **Non promettere** copertura provinciale/regionale (era tra le cifre-slogan **❌ confutate**: HAPS 1 mln km², 2,6 mld persone — `Downstream Civile §4`). Il ponte è **un moltiplicatore di raggio per un servizio locale**, non un'infrastruttura sostitutiva delle telco.

---

## 3. "Immagini in tempo reale" → il numero: quanta banda serve davvero

La parola chiave della richiesta ("bitstream sufficiente … immagini in tempo reale") va **quantificata**, altrimenti non si dimensiona nulla. La buona notizia: **il requisito è modesto**.

### 3.1 Data-rate per il video (H.265/HEVC, lo standard dei datalink UAV moderni)

| Qualità video | Bitrate tipico (H.265) | Note | Conf. |
|---|---|---|---|
| **SD / "situational" 480p–720p** | **0,6–3 Mbit/s** | sufficiente per sorveglianza/riconoscimento grezzo | ✅ (benchmark settore) |
| **HD 1080p 30 fps** | **3–5 Mbit/s** (fino a ~9 Mbit/s) | il caso "immagini in tempo reale" standard; **3GPP indica ~9 Mbit/s per 1080p BVLOS** | ✅ (3GPP + schede encoder) |
| **4K / multi-sensore (EO+IR)** | **10–25 Mbit/s** | payload avanzato / doppio flusso | ✅ |
| **Latenza accettabile (near-real-time)** | **< 0,5 s** end-to-end (target 3GPP **~100 ms**) | oltre ~0,5 s la "diretta" degrada | ✅ |

> **Conclusione 3.1:** un **flusso HD in tempo reale = ~3–9 Mbit/s**. **H.265** dimezza il bitrate rispetto a H.264 a pari qualità → prezioso su link stretti/instabili. Con doppio sensore (EO+IR termico, come per N1/N3) si sta comunque **sotto i ~15–25 Mbit/s**.

### 3.2 I datalink COTS forniscono molto di più — la banda **non** è il collo di bottiglia

- Un **Doodle Labs Mesh Rider** a 20 MHz rende **~12 Mbit/s** netti e streamma video "ad alta fedeltà" **oltre 5 km**; un **Silvus StreamCaster 4×4 MIMO** arriva a **decine di Mbit/s** con relay/mesh (§5). ✅ (schede costruttore)
- Persino un **cellular-bonding** (Elsight Halo) aggrega più SIM LTE/5G per **decine di Mbit/s** dove c'è copertura. ✅

> **Conclusione 3.2 (importante per il pitch):** con ~3–9 Mbit/s richiesti e datalink che ne offrono 10–50+, **la banda per le immagini in tempo reale è un problema risolto dal mercato**. **Il vero dimensionamento è altrove:** (a) **portata a bassa quota** (§2.1), (b) **robustezza/continuità del link** su banda non protetta (§4), (c) **autorizzazione allo spettro in volo e BVLOS** (§4, §6). Lo studio deve spostare l'attenzione **dal "quanti Mbit" al "quale banda, con quale permesso, a quale robustezza SORA"**.

### 3.3 Link budget — perché la portata, non la banda, comanda

Il throughput di un link radio **crolla con la distanza** (perdita di spazio libero ∝ distanza²) e con la banda scelta. In pratica (ordini di grandezza, 🟡 da confermare con planning RF dedicato):

| Banda | Pro | Contro per il "ponte" | Portata utile realistica (aria-terra, quota bassa) |
|---|---|---|---|
| **868 MHz (SRD)** | ottima penetrazione/portata, robusta | **banda strettissima** (kbit/s–pochi Mbit/s): buona per **C2/telemetria e IoT**, **non** per video | decine di km per C2, non per video |
| **2,4 GHz (ISM/RLAN)** | buon compromesso portata/banda, antenne piccole | **affollatissima** (Wi-Fi ovunque) → interferenza | **5–20+ km** con MIMO/mesh, video HD |
| **5,x GHz (RLAN/SRD)** | tanta banda, meno congestione | portata minore, più direttiva | 3–10 km, video multi-Mbit/s |
| **Cellulare (LTE/5G licenziato)** | banda alta dove c'è copertura | **dipende dalla rete a terra** + nodo "uso aereo" (§4.5) | quanto arriva la rete |
| **SATCOM (LEO/GEO)** | copertura ovunque, vero BLOS | latenza/peso/costo; **regime proprio** | globale (backhaul) |
| **5030–5091 MHz (aeronautica protetta)** | **protetta da interferenze**, ideale per C2 sicuro BVLOS | **non ancora operativa per piccoli UAS in EU**, ecosistema immaturo | (futuro) |

> **Regola pratica:** per il **video HD del ponte** conviene **2,4/5,x GHz con radio MIMO/mesh**; per il **C2 robusto e l'IoT** conviene **sub-GHz (868 MHz) o cellulare**; per il **vero oltre-orizzonte** serve **SATCOM** o un **secondo drone-relay in catena** (mesh T1). Un ponte serio è quasi sempre **multi-banda** (ridondanza = anche requisito SORA, §4.6).

---

## 4. La "normativa europea sulle emissioni" per un drone-radio — cosa vuol dire e come rientrarci

Qui sta il cuore della richiesta. "Far rientrare il ponte nella normativa europea sulle emissioni" significa soddisfare **due permessi distinti e cumulativi**:

```
  (A) L'APPARATO PUÒ ESSERE MESSO SUL MERCATO E USATO?        → Direttiva RED 2014/53/UE  (marcatura CE)
  (B) POSSO ACCENDERE QUELLA FREQUENZA, IN VOLO, LÌ?          → Regime SPETTRO (CEPT/ECC + ETSI + AGCOM/PNRF)
  (+  E l'operazione di volo BVLOS è autorizzata?             → SORA/ENAC — vedi Guida ENAC, qui solo l'aggancio)
```

### 4.1 La Direttiva RED 2014/53/UE — i "requisiti essenziali" (i veri "requisiti di emissione")

Ogni ricetrasmettitore che **emette/riceve onde radio intenzionalmente** (il datalink del ponte lo fa) è **apparecchiatura radio** ai sensi della RED e deve rispettare **tre requisiti essenziali**: ✅

| Art. RED | Requisito essenziale | Cosa significa per il ponte |
|---|---|---|
| **Art. 3.1(a)** | **Salute e sicurezza** | Limiti di **esposizione ai campi EM** (persone), sicurezza elettrica. |
| **Art. 3.1(b)** | **Compatibilità elettromagnetica (EMC)** | L'apparato **non deve emettere disturbi** oltre soglia né esserne vittima. **È qui che vivono le "emissioni" spurie/fuori-banda** (out-of-band, spurious). |
| **Art. 3.2** | **Uso efficiente dello spettro** | Deve usare la banda **senza interferenze dannose**: potenza (EIRP), maschera di emissione, comportamento (es. duty cycle, LBT). |

**Come si dimostra (percorso pratico):** si adottano gli **standard armonizzati ETSI EN**; il loro rispetto dà **presunzione di conformità**. Poi **Dichiarazione UE di conformità + marcatura CE**. ✅

| Banda del ponte | Standard armonizzato di riferimento | Copre |
|---|---|---|
| 2,4 GHz (Wi-Fi/MIMO video) | **ETSI EN 300 328** | wideband 2400–2483,5 MHz |
| 5 GHz RLAN | **ETSI EN 301 893** | 5150–5350 / 5470–5725 MHz |
| 5,8 GHz e SRD generici >1 GHz | **ETSI EN 300 440** | SRD 1–40 GHz |
| Sub-GHz (868 MHz, IoT/C2) | **ETSI EN 300 220** | SRD 25–1000 MHz |
| EMC (trasversale) | **ETSI EN 301 489** (serie) | disturbi/immunità |

> **Punto pratico n.1:** se si **compra un datalink COTS già marcato CE/RED** (Silvus, Doodle, Microhard, Elsight…), **il grosso della RED è già assolto dal costruttore** per l'apparato. Restano a Firmamento: (a) **l'integrazione** (l'insieme drone+radio+antenne non deve degradare l'EMC né superare l'EIRP con antenne ad alto guadagno), (b) eventuale **ri-valutazione** se si cambiano antenne/potenza, (c) la **coerenza banda↔paese** (§4.3).

### 4.2 Attenzione: la RED **non basta** — serve anche il diritto d'uso della frequenza

La marcatura CE dice *"questo apparato è a norma"*. **Non dice** *"puoi trasmettere su quella frequenza, a quella potenza, in volo, in Italia"*. Quello è il **regime dello spettro** (§4.3–4.5). Confondere i due è l'errore classico.

### 4.3 Le bande "libere" (SRD/ISM/RLAN) — il percorso più semplice, con limiti di EIRP

Sono le bande dove il ponte T1/T2 vivrà. In UE sono armonizzate (Decisione SRD 2006/771/CE e agg.; raccomandazione ERC 70-03) e in Italia rientrano nell'**autorizzazione generale** (nessuna licenza individuale). **Ma hanno tetti di potenza bassi e nessuna protezione:** 🟡 (valori indicativi UE, da confermare su PNRF/ERC 70-03 vigenti)

| Banda | EIRP max tipico (UE) | Condizioni | Idoneità ponte |
|---|---|---|---|
| **2400–2483,5 MHz** | **100 mW (20 dBm) EIRP** | wideband, EN 300 328 | ✅ video HD a corto/medio raggio |
| **5150–5350 MHz** | 200 mW (indoor/condizionato) | RLAN, EN 301 893 | ⚠️ vincoli d'uso (spesso indoor) |
| **5470–5725 MHz** | 1 W EIRP (con DFS/TPC) | RLAN | ✅ ma DFS (radar) |
| **5725–5875 MHz (5,8)** | **25 mW EIRP** (SRD non-specifico) | basso | ⚠️ potenza bassa → raggio corto |
| **868 MHz (863–870)** | **25 mW**, con **duty cycle** / LBT | banda stretta | ✅ C2/telemetria/IoT, **non video** |

> **Punto pratico n.2 — il nodo "emissioni" più insidioso per un drone:** il limite è sull'**EIRP**, cioè **potenza + guadagno d'antenna**. Un drone che monta **antenne direttive ad alto guadagno** per allungare il raggio **può sforare l'EIRP** di legge pur usando una radio a norma. → **L'EIRP di sistema (radio+antenna) va calcolato e documentato**; è parte della conformità e va messo nel fascicolo tecnico. Inoltre l'uso **aereo** amplia l'"impronta" di interferenza (linea di vista verso molti ricevitori a terra): le autorità lo guardano con più attenzione che a terra.

### 4.4 Le bande licenziate (cellulare, link punto-punto dedicati)

Se il ponte usa **spettro cellulare** (LTE/5G come backhaul o come C2), quello spettro è **licenziato agli operatori telefonici**: Firmamento **non lo possiede**. Si usa **tramite SIM/servizio dell'operatore** (come Elsight Halo). Legale e semplice **a terra**; il nodo è l'**uso aereo** (§4.5). Per un **link dedicato punto-punto** in banda licenziata servirebbe un'**assegnazione individuale AGCOM/MIMIT** (iter lungo) → di norma **non conveniente** per il nostro caso.

### 4.5 Il nodo regolatorio vero: **l'uso aereo delle reti mobili terrestri** e la "cella volante" (T3)

Due punti che il pitch deve conoscere per non fare promesse false:

1. **Usare un normale terminale LTE/5G a bordo di un drone (per C2 o backhaul) non è, di default, un uso previsto/armonizzato in Europa.** Le reti terrestri sono progettate e licenziate per utenti **a terra**; un terminale **in quota** vede molte celle e può **interferire** verso l'alto. La **CEPT/ECC ha mandati aperti (2024–2026)** proprio per definire **condizioni armonizzate dell'uso aereo delle reti mobili e dei terminali "in cielo"**. → *Oggi* l'uso aereo cellulare è **possibile ma soggetto a condizioni/accordi con l'operatore e non pienamente armonizzato**; è un'**area in evoluzione**. 🟡 (mandati CEPT verificati; stato operativo IT da confermare con MIMIT/operatore)
2. **La "cella volante" (T3, Cell-on-Wings)** implica **trasmettere come stazione radio-base in banda di un operatore**: richiede **accordo con l'operatore licenziatario** e/o **spettro dedicato temporaneo** (scenari di emergenza/Protezione Civile). È **fattibile in progetti dedicati** (Nokia/Ericsson hanno dimostratori COW per disaster-recovery), **ma non è un "compra e vola"** e su un **C3 < 25 kg** i vincoli SWaP della radio-base sono stringenti.

> **Punto pratico n.3:** **T3 va trattato come traguardo condizionato** ("in partnership con un operatore, per scenari di emergenza autorizzati"), **non** come funzione nativa del prodotto. **T1/T2 in bande SRD/RLAN sono la via pronta.**

### 4.6 L'aggancio con la certificazione BVLOS (SORA) — perché "emissioni" e "permesso di volo" si parlano

Le due normative non sono separate: **la scelta di banda del ponte influenza il SORA** (vedi `Guida ENAC`). In particolare:

- Il **link C2** in banda **non protetta** (ISM) è più esposto a interferenze → **peggiora la robustezza** richiesta dagli **OSO** ai **SAIL** più alti. Per questo il BVLOS "serio" spinge verso **C2 ridondante (doppio link)** e, in prospettiva, verso la **banda aeronautica protetta 5030–5091 MHz** (§6).
- Un **payload di comunicazione potente** (EIRP alto, antenne direttive) è un **elemento da dichiarare** nel ConOps e può **alzare il rischio-aria percepito** se disturba altri sistemi. → progettare **entro i limiti EIRP** aiuta **due volte**: conformità RED **e** SORA più leggero.
- **Coerenza con le due regole d'oro della Guida ENAC:** restare **< 25 kg e < 3 m** tiene basso il costo autorizzativo; il ponte, essendo **payload modulare** (REQ-04), **non cambia la classe** del velivolo se resta nei limiti di massa/EIRP.

> **Sintesi §4:** il ponte "rientra nella normativa europea sulle emissioni" così: **(1)** datalink **marcato CE/RED** (o integrazione ri-valutata); **(2)** banda **SRD/RLAN in autorizzazione generale** con **EIRP di sistema entro i limiti** (2,4/5,x GHz per il video, 868 MHz per C2/IoT); **(3)** per il cellulare/T3, **accordo operatore** e attenzione all'**uso aereo** (area CEPT in evoluzione); **(4)** tutto **tracciato nel fascicolo tecnico** e **coerente col dossier SORA**.

---

## 5. Analisi di mercato — soluzioni off-the-shelf già disponibili

**Verdetto sintetico:** per i tipi **T1 (relay/MANET)** e **T2/backhaul (cellular-bonding)** **esistono prodotti maturi, conformi RED e nella classe SWaP di un C3**. Non serve inventare la radio. **T3 (cella volante)** è coperto solo da **soluzioni di progetto/partnership**, non da un COTS "da scaffale" per C3.

### 5.1 Datalink RF / MANET (T1 — relay, mesh, video oltre-orizzonte)

| Prodotto | Tipo | Banda | Throughput / portata (schede) | SWaP indicativo | Note per C3 | Conf. |
|---|---|---|---|---|---|---|
| **Silvus StreamCaster** (es. SC4200/MN-MIMO) | MANET 4×4 MIMO, relay/swarm | multi-banda (es. 1,3–2,5 GHz, personalizzabile) | decine di Mbit/s; **mesh multi-hop** (relay nativo) | modulo OEM leggero (sotto ~1 kg a seconda modello) | **Riferimento di categoria** per relay/mesh UAV; usato in ISR | ✅ scheda; 🟡 versione/peso da RFQ |
| **Doodle Labs Mesh Rider** (Mini / Nano² / Helix) | MANET, waveform proprietaria | bande difesa + ISM (2,4/5,x, sub-GHz) | **~12 Mbit/s @20 MHz**, video HD **>5 km** | **Nano² mini, poche decine di g** | Ottimo per **C3/SWaP stretto**; forma-fattore minuscola | ✅ scheda |
| **Microhard** (pDDL/Fusion) | radio/modem IP | 900 MHz / 2,4 / 5 GHz | Mbit/s, robusto, economico | leggero, diffuso | **Entry-level economico**, molto usato su UAS | ✅ |
| **Persistent Systems MPU5** | MANET (Wave Relay) | multi-banda | decine di Mbit/s, mesh scalabile | ~alcune centinaia di g (modulo) | Standard militare mesh; ottimo relay | ✅ scheda |
| **UAV Tactical / Silvus-like OEM vari** | vari | vari | vari | vari | mercato ampio e concorrenziale | 🟡 |

**Lettura T1:** il **relay/mesh video è un mercato risolto**. Un **secondo velivolo o un nodo a terra** in mesh estende il ponte **oltre-orizzonte** senza SATCOM. Banda per immagini in tempo reale: **abbondante**.

### 5.2 Connettività cellulare / bonding + SATCOM (T2/backhaul, BLOS)

| Prodotto | Tipo | Reti | Throughput | SWaP | Note | Conf. |
|---|---|---|---|---|---|---|
| **Elsight Halo** | **cellular bonding** multi-SIM (+SATCOM) | fino a 4× LTE/5G + Starlink/Iridium/Viasat + RF | aggrega decine di Mbit/s dove c'è copertura | **~93 g, 6,5 W** | **Best-in-class BVLOS**, palmo di mano, ideale C3; gestisce ridondanza link | ✅ scheda |
| **Terminali SATCOM LEO (Starlink Mini-class)** | backhaul satellitare | LEO | decine–centinaia di Mbit/s | Mini ~1 kg+ (peso/consumo non banali su C3) | **vero BLOS globale**; verificare SWaP/consumo e regime d'uso mobile/aereo | 🟡 |
| **SATCOM Iridium Certus** | backhaul stretto | LEO | fino a ~0,7 Mbit/s | leggero | banda bassa: **C2/telemetria/telecomando**, non video | ✅ |

**Lettura T2:** **Elsight Halo** è il candidato naturale di **backhaul robusto e ridondante** per il ponte (e per il **C2 BVLOS** — cellular bonding è una risposta diretta all'OSO "link affidabile"). Starlink-class dà banda vera ma **pesa/consuma** → da bilanciare col budget di massa C3 (Trade Study).

### 5.3 "Cella volante" LTE/5G su drone (T3) — solo soluzioni di progetto

| Approccio | Esempi/attori | Stato per C3 |
|---|---|---|
| **COW (Cell-on-Wings)** — radio-base miniaturizzata su UAV | dimostratori **Nokia**, **Ericsson**, operatori telco (disaster recovery) | **Progetto/partnership**, non COTS per C3; SWaP radio-base impegnativo |
| **Drone tethered come base aerea** | **Elistair** (tether) + modulo LTE | Maturo **ma tethered** (autonomia illimitata via cavo, **raggio limitato al cavo**, ~100 m): utile per eventi/emergenza statica, **non** per il "ponte" mobile long-endurance |
| **Small-cell nano su payload** | vari integratori | Fattibile in R&D; **richiede accordo operatore/spettro** (§4.5) |

**Lettura T3:** **niente "compra e vola"** per una cella telefonica su C3. Se il caso d'uso lo richiede (emergenza, borgo senza segnale), è un **progetto in partnership** con un operatore, con iter spettro dedicato → confluisce nella **stima "make/projected"** (§6).

### 5.4 Verdetto di mercato

| Tipo di ponte | Off-the-shelf sufficiente? | Prodotto/i di riferimento |
|---|---|---|
| **T1 — Relay/MANET video** | ✅ **Sì, maturo** | Doodle Labs, Silvus, Persistent, Microhard |
| **T2 — Gateway/backhaul (bonding+SATCOM+IoT)** | ✅ **Sì, maturo** | Elsight Halo (+ Starlink-class / LoRaWAN gateway) |
| **T3 — Cella telefonica volante (LTE/5G)** | ❌ **No COTS per C3** — solo progetto/partnership | COW Nokia/Ericsson; tethered Elistair (caso statico) |

> **Conseguenza:** il "ponte" **da mettere subito a prodotto** è **T1+T2 con datalink COTS conforme RED**, come **payload modulare**. Il "projected" proprietario (§6) ha senso **solo** su **T3** e/o sulla **banda aeronautica protetta 5030–5091 MHz** (C2 sicuro BVLOS) — le due frontiere non coperte dallo scaffale.

---

## 6. Se l'off-the-shelf non basta: stima tempistica e regolamentare del "projected" (make proprietario)

Dove il COTS **non** copre — **(a)** la **cella volante T3** su C3 e **(b)** un **C2 in banda aeronautica protetta 5030–5091 MHz** — serve un percorso di sviluppo proprietario. Di seguito la **stima** (ordini di grandezza, coerenti con `WP-B5` e `Guida ENAC`; cifre e tempi **da confermare**).

### 6.1 Doppio permesso da conquistare (ricorda §4)

| Fronte | Cosa va ottenuto | Chi decide | Tempo stimato 🟡 |
|---|---|---|---|
| **Apparato (RED)** | Progetto RF + prove EMC/spettro (EN 300 xxx / EN 301 489) → **Dichiarazione UE + CE** | Organismo notificato / autocertificazione su standard armonizzati | **6–12 mesi** (progetto→test→CE) |
| **Spettro d'uso** | Se **SRD/RLAN**: rientro in **autorizzazione generale** (rapido). Se **banda dedicata/licenziata/T3**: **assegnazione/accordo** (MIMIT/AGCOM/operatore) | AGCOM/MIMIT (+ operatore per cellulare) | SRD: **settimane**; dedicata/T3: **12–24+ mesi** |
| **Uso aereo cellulare (T3)** | Condizioni d'uso aereo (**mandati CEPT in corso**) + accordo operatore | CEPT/ECC → recepimento IT + operatore | **incerto** (dipende da armonizzazione UE, 2026→) |
| **Volo BVLOS (SORA)** | Autorizzazione ENAC (vedi Guida) — il payload comms **entra nel ConOps/OSO** | ENAC | **~7–18 mesi** (benchmark UE) |
| **Banda aeronautica 5030–5091** | Ecosistema/standard (DO-362A-class) **non ancora operativo per piccoli UAS in EU** | ICAO/CEPT/ENAC | **pluriennale** (frontiera) |

> **Nota chiave:** i quattro fronti **si sovrappongono**, non si sommano linearmente. Il critical path del "projected" è tipicamente **RED+test (≈1 anno)** in parallelo al **dossier SORA (≈1 anno)**; **T3 e la banda protetta aggiungono anni** e dipendono da decisioni UE fuori dal controllo di Firmamento.

### 6.2 Roadmap del payload "ponte" (proprietario, se/quando serve)

| Fase | Attività | TRL | Durata 🟡 | Costo ordine di grandezza 🟡 |
|---|---|---|---|---|
| **P0 — BUY & integra (subito)** | Integrare **datalink COTS conforme RED** (Doodle/Silvus + Elsight Halo) come **payload modulare**; misurare EIRP di sistema; fascicolo tecnico | 8–9 | **0–6 mesi** | **€20–80k** (radio + antenne + integrazione) |
| **P1 — Ponte T1/T2 a prodotto** | Payload relay+gateway (RF mesh + bonding + gateway LoRaWAN); prove di campo; evidenze per SORA (VLOS→BVLOS) | 7–8 | **6–12 mesi** | **€80–250k** (NRE integrazione + test + certificazione insieme) |
| **P2 — (opz.) IP proprietaria RF** | Waveform/gestione multi-banda propria, se requisito di **sovranità di bando** | 4–6 | **18–36 mesi** | **€0,5–2 mln** (come powertrain, §2.2.1 Nota Strategica) |
| **P3 — (frontiera) T3 / banda protetta** | Cella volante in partnership operatore **o** C2 in 5030–5091 | 3–5 | **3–5 anni** | **€mln + partner** (solo con finanziamento dedicato) |

> **Allineamento con la strategia repo (doppio binario BUY/MAKE):** **P0/P1 = BUY** (cash-flow, serve le ancore, rischio minimo). **P2/P3 = MAKE**, da attivare **solo** se un bando dual-use (EDF/PNS/DIANA) o un requisito Protezione Civile lo **finanzia** — esattamente la logica di `WP-B5` e `Nota Strategica §5`.

### 6.3 La leva regolatoria che conviene giocare **adesso**

- **Restare in autorizzazione generale (SRD/RLAN)** per il ponte T1/T2 → **zero iter spettro individuale**, time-to-market minimo.
- **VLOS-first anche per il ponte** (come per il BVLOS in generale): dimostrare il payload comms **a vista** produce le evidenze RF/affidabilità che **rafforzano il SORA** successivo.
- **Primo BVLOS in spazio ristretto/sandbox** (come Horus in R315): riduce sia il rischio-aria sia l'esposizione interferenziale del payload potente.
- **Design entro i limiti EIRP e < 3 m / < 25 kg**: la stessa scelta abbatte **contemporaneamente** costo RED e costo SORA (§4.6).

---

## 7. Raccomandazione

> **Il "ponte aereo di telecomunicazioni" di Firmamento è un PAYLOAD MODULARE (relay T1 + gateway T2), costruito su datalink COTS conformi RED, in bande SRD/RLAN in autorizzazione generale, dimensionato per il video HD in tempo reale (~3–9 Mbit/s) su scala tattica/locale — coerente con la nicchia N6 come funzione + gancio politico, NON come infrastruttura di connettività regionale.**

**I quattro pilastri, con evidenza:**

1. **Scope onesto (T1/T2, tattico/locale).** Un C3 a bassa quota non è un HAPS: il ponte serve **una valle, una costa, un'emergenza, una tratta oltre-orizzonte** — non una provincia. Regge il caso d'uso, non lo gonfia (`Market §4`, §2.1).
2. **Banda = problema risolto dal mercato.** ~3–9 Mbit/s bastano per le immagini in tempo reale (H.265); i datalink COTS ne offrono 10–50+. Il focus si sposta su **portata, robustezza, spettro** (§3).
3. **Conformità "emissioni" = RED (CE) + regime spettro + coerenza SORA.** Datalink marcato CE, **EIRP di sistema entro i limiti**, bande **libere** per partire, cellulare/T3 solo con **accordo operatore** (area CEPT in evoluzione). Progettare entro i limiti **alleggerisce anche il SORA** (§4).
4. **BUY subito, MAKE solo se finanziato.** P0/P1 (integrazione COTS) danno il ponte a prodotto in **≤12 mesi**; P2/P3 (IP RF proprietaria, cella volante, banda aeronautica) **solo** su bando dual-use dedicato (§6). È il **doppio binario** già scelto dal repository.

**Decisioni proposte per la riunione:**
1. Confermiamo il **ponte come payload modulare T1+T2** (relay + gateway), scope **tattico/locale**? *(racc.: sì)*
2. **Datalink di partenza (BUY):** **Doodle Labs/Silvus** (relay video RF) **+ Elsight Halo** (bonding/BLOS e C2 ridondante)? *(racc.: sì, RFQ a entrambi)*
3. **T3 (cella volante):** lo teniamo come **gancio narrativo/emergenza in partnership operatore**, non come capacità nativa? *(racc.: sì)*
4. **Banda:** **2,4/5,x GHz** per il video + **868 MHz/cellulare** per C2/IoT, tutto in **autorizzazione generale**? Attivare verifica su **PNRF/ERC 70-03 vigenti** e **stato uso aereo cellulare** con MIMIT/operatore?
5. **MAKE proprietario (P2/P3):** lo attiviamo **solo** se un bando (EDF/PNS/DIANA/Protezione Civile) lo finanzia?

---

## 8. Lacune residue e verifiche prima dello Studio

1. **Valori EIRP/duty-cycle vigenti** su **PNRF italiano** e **ERC Rec 70-03** (le cifre §4.3 sono ordini di grandezza UE → confermare a vista). 🟡
2. **Stato operativo dell'uso aereo cellulare in Italia** (condizioni operatore, esito **mandati CEPT 2024–2026**). 🟡
3. **SWaP reali** (peso, potenza, banda, prezzo) dei datalink candidati **via RFQ** (Doodle, Silvus, Persistent, Elsight) e **peso/consumo Starlink-class** su C3. 🟡
4. **Peso/EIRP del payload comms** e impatto sul **mass/energy budget** (Trade Study WP-B3) e sul **SORA** (OSO C2). 
5. **Caso T3 di emergenza**: interlocuzione **Protezione Civile + operatore** per capire se esiste domanda/finanziamento reale per la "cella volante" nelle aree interne.

---

## Fonti principali

**Normativa apparato ed emissioni (RED / EMC / spettro):**
- **Direttiva 2014/53/UE (RED)** — requisiti essenziali (salute/sicurezza, EMC art. 3.1(b), uso efficiente spettro art. 3.2): https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32014L0053
- **Reg. (UE) 2019/945** — l'UA che emette/riceve onde radio (non certificata) ricade nella RED.
- **Standard armonizzati ETSI:** EN 300 328 (2,4 GHz), EN 301 893 (5 GHz RLAN), EN 300 440 (SRD >1 GHz), EN 300 220 (SRD sub-GHz), EN 301 489 (EMC): https://www.etsi.org
- **Decisione SRD 2006/771/CE** e **ERC Recommendation 70-03** (bande SRD, EIRP, duty cycle) — CEPT/ECC: https://www.cept.org
- **AGCOM / MIMIT — PNRF** (Piano Nazionale Ripartizione Frequenze), regime autorizzazione generale SRD.

**Spettro UAS / uso aereo / banda aeronautica:**
- **Banda aeronautica protetta 5030–5091 MHz** (CNPC BVLOS), WRC-12, MOPS **RTCA DO-362A** — frontiera non ancora operativa per piccoli UAS in EU.
- **Mandati CEPT/ECC su UAS e uso aereo delle reti mobili (2024–2026)**: https://cept.org/ecc — mandato UAS (ECC-24-014) e lavori su terminali "in cielo".
- **3GPP** — requisiti connessione BVLOS (~9 Mbit/s per 1080p, ~100 ms latenza).

**Mercato off-the-shelf (datalink / bonding / COW):**
- **Doodle Labs Mesh Rider** (Mini/Nano²/Helix — ~12 Mbit/s@20 MHz, video >5 km): https://www.doodlelabs.com
- **Silvus Technologies StreamCaster** (MANET MIMO, relay/mesh UAV): https://silvustechnologies.com/applications/unmanned-systems/
- **Persistent Systems MPU5 / Wave Relay**; **Microhard** (pDDL/Fusion).
- **Elsight Halo** (cellular bonding + SATCOM, ~93 g, 6,5 W, BVLOS): https://www.elsight.com/
- **Cell-on-Wings (COW)** disaster-recovery — Nokia/Ericsson; **drone tethered LTE** — Elistair: https://elistair.com

**Documenti interni collegati:**
- `Fase A - MARKET ANALYSIS REPORT (consolidato)` (N6 connettività) · `Fase A - Downstream Civile Terrestre` (§4, vincolo fisico HAPS) · `Fase B - Trade Study Architetture` (REQ-04/05) · `Guida - Certificazione ENAC-SORA per il volo BVLOS` · `Nota Strategica - Alternativa Superiore a HALE` (§2.7).

> ⚠️ **Onestà (standard Dossier di Verifica):** i **limiti EIRP/duty-cycle** e lo **stato dell'uso aereo cellulare** vanno confermati su **fonte primaria vigente** (PNRF, ERC 70-03, esiti CEPT) — qui sono **ordini di grandezza UE**. Le **specifiche di prodotto** sono da **schede costruttore → confermare con RFQ**. **Tempi e costi autorizzativi italiani non sono pubblici → stime** (come per il BVLOS). Le cifre-slogan HAPS (copertura 1 mln km², 2,6 mld persone) restano **❌ confutate** e non vanno usate. Il vincolo fisico "C3 ≠ HAPS" è **confermato** e definisce lo scope tattico/locale del ponte.
