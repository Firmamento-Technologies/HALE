# Studio — Ponte Aereo per le Telecomunicazioni (relay/base-station aviotrasportata)
## BVLOS, conforme alla normativa europea sulle emissioni radio, con bitstream sufficiente per immagini in tempo reale

| | |
|---|---|
| **Documento** | Studio di fattibilità del **payload "ponte aereo TLC"** per la piattaforma C3 (< 25 kg) di Firmamento: come implementare un relay/gateway radio aviotrasportato che **(a)** rientri nella **normativa europea sulle emissioni** (RED + spettro), **(b)** operi in **BVLOS**, **(c)** garantisca una **banda (bitstream) sufficiente al video in tempo reale**. Include analisi del mercato *off-the-shelf* e, dove il mercato non basta, una **stima tempistica e regolamentare** del "make". |
| **A chi serve** | A chi deve capire *cosa comprare, cosa serve, quanto tempo e in che ordine* per aggiungere alla piattaforma la **funzione di connettività/relay** — con i piedi per terra sul quadro normativo. |
| **Versione / Data** | 0.1 — 2026-07-15 |
| **Collegato a** | `Nota Strategica - Alternativa Superiore a HALE` (§2.5, §2.7), `Guida - Certificazione ENAC-SORA per il volo BVLOS`, `Guida - Tecnologie e Costi per la Certificazione BVLOS (superare gli OSO)` (§2 datalink C2), `Fase A - Downstream Civile Terrestre` (§4 connettività — il verticale più fragile). |
| **Metodo / Onestà** | Stessa disciplina del `Dossier di Verifica`: **[verificato]** = dato pubblico con fonte; **[stima]** = fascia di settore; **[da verificare]** = da confermare su fonte primaria (ERC/REC 70-03, PNRF italiano, ENAC, RFQ vendor). **Nessun numero è inventato.** I limiti di potenza (EIRP/ERP) qui riportati sono **riferimenti tipici UE** da confermare sul testo vigente. |

---

## 0. In una frase (e la verità scomoda da tenere in faccia)

> Un drone **C3 (< 25 kg) a bassa quota** può fare un **ponte radio aereo tattico/locale** — estendere o rilanciare un collegamento su **una valle, un cantiere, uno scenario di emergenza** — con banda **ampiamente sufficiente al video HD/4K in tempo reale**. **Non** può fare da **infrastruttura di connettività regionale** né da **ponte verso i satelliti LEO**: quello è il mestiere degli **HAPS stratosferici (18–25 km)**, una classe fisicamente diversa (già stabilito in `Fase A §4`, con diverse cifre-slogan HAPS **confutate**). Il vero collo di bottiglia **non è la banda né l'hardware** (esistono a scaffale): sono **due autorizzazioni** — l'**uso aeronautico dello spettro** (molte bande "libere" sono legalmente *solo terrestri*) e il **BVLOS/SORA ENAC**.

Questo studio, coerentemente con il repository, **posiziona il ponte aereo TLC come funzione modulare di missione** (relay/gateway tattico, gancio politico "aree interne/emergenza") e **non** come il business portante — che resta monitoraggio rischi + ispezione lineare (`Fase A §7`).

---

## 1. Glossario — le sigle nuove (le altre sono nelle Guide ENAC-SORA)

| Sigla | Per esteso | In parole semplici |
|---|---|---|
| **RED** | *Radio Equipment Directive* 2014/53/UE | La **legge europea** che stabilisce cosa può essere immesso sul mercato UE se emette/riceve onde radio. Serve la **marcatura CE**. |
| **ETSI** | *European Telecommunications Standards Institute* | L'ente che scrive gli **standard armonizzati** (le "regole tecniche") con cui si dimostra la conformità alla RED. |
| **EN 300 328 / 301 893 / 300 220 / 300 440 / 301 489** | Standard armonizzati ETSI | Le "regole tecniche" per, rispettivamente: **2,4 GHz**, **5 GHz RLAN**, **SRD sub-GHz (868 MHz)**, **SRD 433/2,4/5,8 GHz**, **compatibilità elettromagnetica (EMC)**. |
| **SRD** | *Short Range Devices* | Apparati a **corto raggio** che usano bande **senza licenza** ma con **limiti di potenza** stringenti. |
| **EIRP / ERP** | *(Effective) Isotropic/Equivalent Radiated Power* | La **potenza effettivamente irradiata** dall'antenna. È **il numero che la legge limita** (non la potenza del trasmettitore). |
| **ERC/REC 70-03** | Raccomandazione CEPT sugli SRD | Il **documento di riferimento europeo** che elenca bande e limiti di potenza per gli apparati a corto raggio. |
| **CEPT / ECC** | Conferenza europea PT / Electronic Communications Committee | Gli enti che **armonizzano lo spettro** in Europa (le decisioni ECC diventano regole nazionali). |
| **PNRF** | Piano Nazionale di Ripartizione delle Frequenze | Il documento **italiano** (MIMIT) che dice **chi può usare quale frequenza** in Italia. |
| **MIMIT** | Min. Imprese e Made in Italy (ex-MISE) | L'**autorità italiana per lo spettro** (assegna frequenze e licenze sperimentali). Diverso dall'ENAC (che dà il permesso di *volo*). |
| **Backhaul** | — | Il **collegamento "di ritorno"** che porta i dati dal nodo aereo alla rete fissa/Internet (via terra, ponte radio o satellite). |
| **Access link** | — | Il collegamento tra il **nodo aereo e gli utenti/sensori** a terra (o il sensore video del drone stesso). |
| **Cell on Wings (CoW)** | Base station aviotrasportata | Il drone porta in volo una **cella LTE/5G**: gli smartphone a terra si agganciano ad essa. |
| **Aerial UE** | *Aerial User Equipment* | Il drone usato come **"telefono volante"**: si aggancia alle celle a terra come uplink/relay. Regolato da **ECC Decision (22)07**. |
| **HAPS / HIBS** | *High Altitude Platform Station / HAPS as IMT Base Station* | Piattaforma a **18–25 km** che fa da base station dal cielo. **Non è il nostro caso** (noi a bassa quota). |
| **MANET** | *Mobile Ad-hoc Network* | Rete radio **"a maglia"** in cui i nodi si ritrasmettono il segnale: robusta, si auto-forma. È la tecnologia-base del relay tattico. |
| **C2 link** | *Command & Control* | Il radiocomando **pilota↔drone** (il "telecomando"). **Diverso** dal link del payload TLC. |
| **DVB-x / COFDM** | Modulazioni broadcast/robuste | Forme d'onda usate nei **link video professionali** a bassa latenza. |

> ⚠️ **La distinzione che salva dagli errori:** un drone ha **due (o tre) collegamenti radio diversi**, con regole diverse: il **C2** (radiocomando, trattato negli OSO — `Guida OSO §2`), il **payload/access link** (video e dati verso l'utente) e l'eventuale **backhaul**. Questo studio riguarda **payload + backhaul**, non il C2.

---

## 2. Cos'è un "ponte aereo TLC" — architettura e ruoli

Un ponte aereo di telecomunicazioni è un **nodo di rete che vola**. Si scompone sempre in **tre pezzi**:

```
   UTENTI / SENSORI a terra          NODO AEREO (drone)              RETE FISSA / INTERNET
   (smartphone, IoT, camera,   ← ACCESS LINK →   RELAY   ← BACKHAUL →   (stazione a terra,
    squadra di soccorso)                       (instradamento)          ponte radio o SATELLITE)
```

Da qui discendono **tre ruoli** possibili, con regole di emissione **molto diverse**:

| Ruolo | Cosa fa il drone | Access link | Backhaul | Nota normativa emissioni |
|---|---|---|---|---|
| **R1. Relay/estensione di link** (il più realistico per un C3) | Rilancia un collegamento punto-punto o mesh: estende la portata "oltre la collina" | MANET / radio dedicata | MANET verso nodo a terra | Bande SRD/licenza-light; **problema uso aereo** (§3.3) |
| **R2. Cell on Wings** (cella LTE/5G volante) | Porta in volo una **piccola base station**: gli smartphone si agganciano | LTE/5G (bande MFCN, **licenziate**) | Satellite o ponte radio | **Serve spettro licenziato** dall'operatore mobile o autorizzazione dedicata |
| **R3. Aerial UE / hotspot** | Il drone si aggancia alle celle a terra come "telefono volante" e ridistribuisce (Wi-Fi/mesh) | Wi-Fi/mesh verso utenti | **Cellulare** verso rete | **ECC Decision (22)07** regola l'uplink aereo su bande MFCN |

> **Lettura strategica:** per una startup C3 civile/dual-use, **R1 (relay MANET)** è la strada tecnicamente e normativamente più pulita (hardware maturo, banda enorme, nessun operatore mobile da coinvolgere). **R2/R3** sono più "sexy" (portano *telefonia* alla popolazione) ma trascinano dentro lo **spettro licenziato** e gli **operatori mobili** — un percorso da partnership, non da prodotto autonomo.

---

## 3. La normativa europea sulle emissioni (il cuore nuovo di questo studio)

Qui "**emissioni**" significa **emissioni radio (uso dello spettro)**. La conformità si gioca su **due piani distinti** che vanno tenuti separati — confonderli è l'errore classico.

### 3.1 Piano 1 — Conformità dell'**apparato** (RED 2014/53/UE + marcatura CE)

Ogni radio immessa sul mercato UE deve essere conforme alla **Radio Equipment Directive 2014/53/UE**, in vigore dal 13/06/2016 [verificato]. Si dimostra la conformità tramite gli **standard armonizzati ETSI**, poi si appone la **marcatura CE**. Gli articoli 3.1 (sicurezza+EMC), 3.2 (uso efficiente dello spettro) e 3.3 (requisiti aggiuntivi) sono i pilastri.

| Banda | Standard armonizzato ETSI di riferimento | Uso tipico nel drone |
|---|---|---|
| **2400–2483,5 MHz** | **EN 300 328** [verificato] | Video/telemetria, Wi-Fi, alcune MANET |
| **5150–5725 MHz (RLAN)** | **EN 301 893** [verificato] | Wi-Fi 5 GHz, MANET a banda larga |
| **5725–5875 MHz (SRD)** | EN 300 440 | Link video FPV/analogici |
| **863–870 MHz (SRD)** | EN 300 220 | Telemetria, FTS/terminatore (869 MHz — cfr. Aermatica3D, `Guida OSO §1`) |
| **EMC (tutte)** | **EN 301 489** (serie) [verificato] | Compatibilità elettromagnetica di qualunque radio |

> **In pratica:** un payload TLC costruito con **moduli COTS già marcati CE** (radio Wi-Fi/MANET commerciali) **eredita gran parte della conformità RED**. La RED **non è il collo di bottiglia** se si comprano moduli conformi. **Il collo di bottiglia è il Piano 2.**

### 3.2 Piano 2 — Conformità dell'**uso dello spettro** (bande, potenza EIRP, e l'insidia dell'"uso aereo")

Anche con un apparato CE, **come e dove** lo si usa è regolato a parte. Due vincoli:

**(a) Limiti di potenza irradiata (EIRP/ERP).** Le bande "senza licenza" impongono tetti stringenti (riferimenti UE tipici via **ERC/REC 70-03**, *da verificare sul testo vigente e sul PNRF italiano*):

| Banda | Limite tipico UE | Nota |
|---|---|---|
| 2,4 GHz | **100 mW EIRP** [stima/da verificare] | Il classico Wi-Fi/telemetria |
| 5,15–5,35 GHz | 200 mW EIRP (indoor) | Vincolo *indoor* problematico per il volo |
| 5,47–5,725 GHz | 1 W EIRP (con DFS/TPC) | Più potenza, ma con controllo interferenze |
| 5,8 GHz (SRD) | **~25 mW EIRP** [stima/da verificare] | **Molto più basso che negli USA** → i link FPV "americani" **non sono legali** in UE alla stessa potenza |
| 868 MHz (SRD) | **25 mW ERP** [stima/da verificare] | Ottimo per IoT/telemetria a lungo raggio, banda stretta |

> **Conseguenza n.1:** la **potenza** limita la **portata** del ponte in banda libera. Per coprire distanze reali con banda alta si usano **antenne direttive** (che concentrano l'EIRP nel lobo utile) e/o **MANET multi-hop** (più salti brevi anziché un salto lungo), restando nei limiti. Salire di potenza *oltre* i limiti richiede **licenza** (§3.4).

**(b) L'insidia dell'uso aereo — il punto che quasi tutti sbagliano.** Molte bande SRD/RLAN sono armonizzate per uso **terrestre**; l'**impiego a bordo di aeromobile può essere ristretto o vietato** (una radio in volo "illumina" un'area enorme e interferisce con molte celle/reti a terra). → **Un modulo perfettamente CE può risultare *non autorizzato all'uso in volo* sulla banda scelta.** Questo è il vero nodo "emissioni" del ponte aereo, e va verificato **banda per banda sul PNRF italiano** e, se serve, sanato con **autorizzazione/licenza sperimentale MIMIT** [da verificare].

### 3.3 Il caso R2/R3 — reti mobili dal cielo (regole dedicate CEPT/ECC)

Quando il drone entra nelle **bande delle reti mobili (MFCN)** — perché fa da cella (R2) o da terminale aereo (R3) — non si è più nel "senza licenza": valgono regole dedicate.

- **ECC Decision (22)07** (approvata nov. 2022): condizioni tecniche armonizzate per l'uso di **"aerial UE" su LTE e 5G NR** nelle bande **703–733, 832–862, 880–915, 1710–1785, 1920–1980, 2500–2570 e 2570–2620 MHz** [verificato]. È la cornice che rende *legale e coordinato* il drone-terminale in volo — ma resta **spettro licenziato dell'operatore mobile**.
- **Mandato CEPT su UAS** (in corso): l'ECC sta lavorando a condizioni per spettro dedicato ai droni (C2 e comunicazioni) [verificato — mandato UE alla CEPT].
- **C2 aeronautico dedicato:** a livello ITU la banda **5030–5091 MHz** è destinata al **C2 degli UAS** (spettro aeronautico protetto) — rilevante per il *radiocomando*, non per il payload TLC [stima/nota di contesto].

### 3.4 Il caso HAPS/HIBS — perché **non** è la nostra strada (ma va citato con onestà)

Il **WRC-23** ha identificato le bande **2 GHz e 2,6 GHz** (e aperto 700–900 MHz, 1,7 GHz, 2,5 GHz) per l'uso di **HAPS come base station IMT (HIBS)** [verificato]. **Ma gli HAPS operano a 18–25 km** [verificato]: sono la classe che *davvero* fa connettività regionale e ponte verso i satelliti. **Un C3 a bassa quota non è un HAPS** (`Fase A §4`, cifre-slogan HAPS confutate). → Citiamo l'allocazione HAPS come **contesto** ("il regolatore sta aprendo spettro per la connettività dal cielo"), **non** come base regolatoria del nostro payload.

### 3.5 Il backhaul satellitare — un regime a parte

Se il backhaul (§2) è **satellitare** (terminale piatto tipo LEO su piattaforma), si entra nella regolazione **satellitare** (autorizzazione del servizio, terminale conforme, uso in mobilità/aereo da verificare col fornitore). È la via più semplice per **backhaul in aree senza rete a terra**, ma aggiunge **peso, consumo e un abbonamento dati**. Da valutare come opzione, non come default per un C3 di peso limitato.

### 3.6 Sintesi del quadro "emissioni"

| Domanda | Risposta sintetica |
|---|---|
| L'apparato è conforme UE? | **Sì facilmente**, con moduli COTS già CE (RED + ETSI). Non è il collo di bottiglia. |
| Posso usare la banda libera in volo? | **Da verificare banda-per-banda** (PNRF/ERC 70-03): l'**uso aereo** può essere ristretto → possibile **licenza sperimentale MIMIT**. **Questo è il vero nodo.** |
| Posso fare la cella LTE/5G volante? | Solo con **spettro licenziato** (operatore mobile) o regole dedicate (**ECC (22)07** per l'aerial UE). Percorso da **partnership**. |
| Posso fare l'infrastruttura regionale? | **No** con un C3 (fisica): quello è HAPS. Noi = **relay tattico/locale**. |

---

## 4. Il layer BVLOS (rimando alle Guide, con l'aggancio giusto)

Il ponte aereo **vive nel BVLOS**: un relay ha senso proprio *oltre l'orizzonte visivo*. Vale **tutto** quanto già scritto nelle Guide, con tre note specifiche:

1. **BVLOS = categoria Specific → SORA 2.5 (ENAC)** — nessuna scorciatoia lo cambia (`Guida ENAC-SORA §3`). Missione/area a **SAIL ≤ IV**.
2. **Non confondere i link:** gli OSO sul **C2 ridondante** (`Guida OSO §2`) riguardano il *radiocomando*, **non** il payload TLC. Il payload TLC **non deve degradare** il C2 (coesistenza in frequenza da progettare: bande separate, filtri).
3. **Spazio riservato come doppia scorciatoia:** volare in **spazio aereo segregato/sandbox** (come Horus in R315 — `Guida ENAC-SORA §9`) **aggira sia il DAA** (rischio-aria) **sia parte del problema-interferenze** (area controllata). → È la via di partenza anche per il ponte TLC.

> **Il messaggio:** il ponte aereo **non aggiunge un nuovo problema di volo**; eredita quello già mappato (SORA + spazio riservato) e **aggiunge un problema di spettro** (§3.2). I due dossier — **SORA/ENAC** e **frequenze/MIMIT** — vanno istruiti **in parallelo**.

---

## 5. Il "bitstream sufficiente" per immagini in tempo reale

La domanda pratica: **quanta banda serve** per portare **immagini in tempo reale**, e **quanta ne danno** le radio a scaffale? Risposta: **ne serve poca; le radio ne danno tanta.** Il video **non è il collo di bottiglia**.

**Quanta serve (video H.265/HEVC, riferimenti di settore [verificato]):**

| Qualità | H.265 (HEVC) | H.264 (confronto) |
|---|---|---|
| 1080p (Full HD) | **~2,25–3 Mbps** | ~4,5–6 Mbps |
| 1080p60 fluido | **~4–5 Mbps** | ~6–8 Mbps |
| 4K broadcast | **~12–16 Mbps** | ~25–35 Mbps |

Aggiungendo overhead di rete e margine, un **flusso 4K professionale sta in ~20 Mbps**; **più flussi HD simultanei** in poche decine di Mbps.

**Quanta ne danno le radio MANET a scaffale [verificato]:**

| Radio | Throughput dichiarato | Peso |
|---|---|---|
| **Silvus StreamCaster MINI 5200** | **fino a 100 Mbps** (2×2 MIMO, 2 W) | **182 g** |
| **Persistent Systems MPU5** | alto (3×3 MIMO) — datasheet su richiesta | — |

> **Verdetto banda:** **100 Mbps** di una singola MANET **coprono abbondantemente** un 4K (~20 Mbps) **o** 4–5 flussi HD simultanei. **La banda è un problema risolto** — con l'avvertenza che il throughput reale **cala con distanza, ostacoli e numero di nodi** (è condiviso nella mesh). Il dimensionamento reale si fa sul **link budget** (potenza EIRP legale §3.2 + antenne + quota), non sul picco di targa.

**Conseguenza di design:** poiché la banda avanza, conviene **spenderla in robustezza** (modulazione adattiva, ritrasmissione, latenza bassa COFDM) più che in risoluzione. Per l'ISR/soccorso, **HD fluido e stabile a bassa latenza batte il 4K instabile**.

---

## 6. Analisi di mercato — soluzioni *off-the-shelf* (già in commercio)

Domanda: **esiste già un "ponte aereo TLC BVLOS C3, conforme emissioni UE, con backhaul"** pronto all'uso? Risposta: **i mattoni sì, il prodotto integrato no.** Rassegna per famiglia.

### 6.1 Droni *tethered* (al cavo) per TLC — maturi ma **non BVLOS free-flying**

| Soluzione | Paese | Ruolo | Note | Stato/Prezzo |
|---|---|---|---|---|
| **Elistair Safe-T 2 + Orion 2** | 🇫🇷 Francia | Relay 4G/Wi-Fi da payload trasferibile | **Fino a 50 h** in volo (alimentato da terra via cavo), deploy 15 min, IP54, micro-tether 125 m | Commerciale, >70 Paesi [verificato] |
| **Hoverfly** | 🇺🇸 USA | Tethered comms/ISR militare | Persistenza al cavo | Commerciale |

> **Limite strutturale:** il *tethered* dà **persistenza infinita e nessun problema di endurance**, ma è **ancorato a terra (≤125 m)** → **non è il BVLOS free-flying** richiesto, e non estende la copertura "oltre la collina". Utile come **prodotto BUY immediato** per eventi/emergenza puntuale, **non** come il nostro ponte a lungo raggio.

### 6.2 Radio MANET (il "motore" del relay R1) — maturissime, **estere**

| Prodotto | Paese | Ruolo | Banda/throughput | Prezzo |
|---|---|---|---|---|
| **Silvus StreamCaster (MINI 5200 / 4400)** | 🇺🇸 USA | Nodo mesh video/dati | MIMO, **100 Mbps**, 550+ nodi | [preventivo] ~$4–8k [stima] |
| **Persistent Systems MPU5** | 🇺🇸 USA | Nodo mesh (Wave Relay) | 3×3 MIMO | [preventivo] |
| **Doodle Labs Mesh Rider** | 🇺🇸/🇸🇬 | Mesh multi-banda leggera | 25–34 g | [preventivo] |
| **Domo Tactical (DTC)** | 🇬🇧 UK | Link video COFDM/MANET | broadcast a bassa latenza | [preventivo] |

> **Nota emissioni (§3.2):** queste radio sono **multi-banda e configurabili**; la conformità UE dipende dalla **banda e potenza impostate** e dall'**autorizzazione all'uso aereo**. Vanno ordinate/configurate per bande **legali in UE e in volo** — non nelle configurazioni "US" ad alta potenza. **Mercato italiano nativo: scarso** → si integra prodotto estero (coerente con `Guida OSO §2` e `Nota Strategica §2.2`).

### 6.3 Cell on Wings / base station aviotrasportata (R2) — esiste ma **da spettro licenziato**

Base station LTE/5G miniaturizzate esistono (integrazioni Nokia/Ericsson in trial, small-cell COTS), ma:
- richiedono **spettro licenziato** (operatore mobile) → percorso **partnership**, non prodotto autonomo (§3.3);
- il **backhaul** resta da risolvere (satellite o ponte radio).
→ **Non è un off-the-shelf "plug&play"** per una startup senza accordo con un MNO.

### 6.4 Backhaul satellitare — disponibile, con costi/peso

Terminali piatti LEO (classe Starlink/OneWeb) danno **backhaul in aree senza rete**, ma **peso/consumo/abbonamento** e **uso in volo da verificare** col fornitore (§3.5). Opzione **valida per il backhaul**, non un ponte completo.

### 6.5 HAPS — **fuori classe** (contesto, non COTS per noi)

Player HAPS (stratosferici) danno connettività regionale, ma **non sono acquistabili come payload C3** e operano su un **regime spettro/quota diverso** (§3.4). **Escluso** dal nostro perimetro.

### 6.6 Verdetto di mercato

| Domanda | Risposta |
|---|---|
| Esistono i **componenti**? | ✅ **Sì, maturi** (MANET, tethered, small-cell, backhaul sat) — quasi tutti **esteri**. |
| Esiste il **prodotto integrato** "ponte aereo TLC BVLOS C3, emissioni-UE-compliant, con backhaul, chiavi in mano"? | ❌ **No.** Nessuno vende *quel* pacchetto per la classe C3 civile/dual-use italiana. |
| Dove sono i **gap**? | (1) **Autorizzazione uso aereo dello spettro** (§3.2); (2) **backhaul** integrato in < 25 kg; (3) **endurance** nel free-flying (i tethered barano col cavo); (4) **integrazione** payload↔C2↔piattaforma. |

→ **Conclusione:** si **compra il motore (MANET) e si integra**, ma il **ponte aereo BVLOS conforme è un lavoro di integrazione + autorizzazione**, non un acquisto. Questo giustifica una stima "make" (§7).

---

## 7. Se l'off-the-shelf non basta — stima tempistica e regolamentare del "make"

Poiché il **prodotto integrato non esiste** (§6.6), ecco la **stima** del percorso per realizzarlo, a **doppio dossier parallelo** (spettro + volo), coerente col binario BUY/MAKE della `Nota Strategica §5`. **Cifre e tempi sono [stima] su benchmark UE**, da confermare con RFQ, MIMIT ed ENAC.

### 7.1 I due dossier regolatori (da istruire in parallelo)

| Dossier | Autorità | Cosa serve | Tempo [stima] |
|---|---|---|---|
| **A. Spettro / Emissioni** | **MIMIT** (+ verifica PNRF/ERC 70-03) | Scelta bande **legali in volo**; conferma **CE (RED)** dei moduli; se necessario **autorizzazione/licenza sperimentale** per uso aereo; per R2/R3 **accordo MNO + ECC (22)07** | **3–9 mesi** (sperimentale) → più lungo se serve coordinamento MFCN |
| **B. Volo / BVLOS** | **ENAC** (SORA 2.5) | ConOps del relay, SAIL ≤ IV, spazio riservato/sandbox, OSO C2 (`Guida OSO`) | **7–18 mesi** (benchmark UE, `Guida ENAC-SORA §5`) |

> **Il nuovo rischio rispetto agli altri payload:** il **dossier A (spettro)** è **specifico del ponte TLC** e **non** è coperto dalle Guide esistenti (che trattano il volo, non le frequenze). È **la vera novità regolatoria** di questo payload e il primo motivo per cui va aperto **presto**.

### 7.2 Roadmap tecnica (allineata a M0→M36 della `Nota Strategica`)

```
M0–M6   INTEGRAZIONE BANCO
  • MANET COTS (Silvus/Persistent) su banda UE-legale + antenne direttive
  • Prova bitstream video H.265 (target: HD stabile a bassa latenza)
  • Verifica coesistenza payload↔C2 (bande separate)     [tecnico]
  • APERTURA dossier A (MIMIT/PNRF) e dossier B (SORA)    [regolatorio]

M6–M18  DIMOSTRATORE VLOS → BVLOS in spazio riservato
  • Relay R1 su vallata/sandbox; link budget reale
  • Backhaul: ponte radio a terra (default) o satellite (opzione)
  • Raccolta dati affidabilità (evidenza per il SORA, come da §4)

M18–M36 SERVIZIO
  • BVLOS in corridoio/sandbox esteso; casi emergenza/aree interne
  • (Opzionale) R2/R3 solo con partnership MNO
```

### 7.3 Stima costi incrementali del payload TLC (oltre al velivolo e al kit BVLOS base)

*(Solo la parte "ponte TLC", da sommare al kit BVLOS ~€8–15k pragmatico della `Guida OSO §10`. [v]=verificato, resto stima/preventivo.)*

| Voce | Fascia [stima] |
|---|---|
| Radio MANET (coppia, per relay) | €8.000–20.000 (2 nodi premium) [preventivo] |
| Antenne direttive + integrazione RF | €2.000–6.000 [stima] |
| Backhaul satellitare (opz.) — terminale + abbonamento | €2.000–6.000 + canone/anno [stima] |
| Test EMC/coesistenza + eventuale pre-compliance RED | €3.000–10.000 [stima] |
| **Dossier A — licenza sperimentale spettro (MIMIT)** | **tariffa modesta + consulenza [preventivo/da verificare]** |
| Dossier B — SORA (già nel budget BVLOS) | vedi `Guida OSO §8` |
| **Totale incrementale payload TLC** | **~€15.000–45.000 [stima]** (esclusi velivolo e kit BVLOS base) |

> **Come leggere:** il **grosso è integrazione + autorizzazione spettro**, non un componente esotico. Il payload TLC **non fa esplodere il budget** come farebbero un DAA non cooperativo o un SAIL III+ (`Guida OSO §10`) — a patto di **restare in banda libera/sperimentale (R1)** e **non** inseguire la cella LTE licenziata (R2) senza un MNO.

---

## 8. Rischi e contro-argomenti onesti

| Rischio / obiezione | Impatto | Mitigazione |
|---|---|---|
| **Uso aereo dello spettro non autorizzato** sulla banda scelta (§3.2) | **Alto** (è il nodo vero) | Verifica **PNRF/ERC 70-03** *prima* del design; via **licenza sperimentale MIMIT**; partire in **spazio riservato**. |
| **Confondere "CE (RED)" con "autorizzato a volare"** | Alto | Tenere separati **Piano 1 (apparato)** e **Piano 2 (uso)** (§3.1–3.2). CE ≠ permesso d'uso in volo. |
| **Il C3 non fa connettività regionale** (fisica, `Fase A §4`) | Alto se lo si promette | Vendere **relay tattico/locale**, non backbone; HAPS ≠ noi. **Niente cifre-slogan HAPS confutate.** |
| **R2/R3 richiedono un MNO** e spettro licenziato | Medio-alto | Trattare R2/R3 come **partnership**, non prodotto; partire da **R1 MANET**. |
| **Throughput reale < targa** (distanza/nodi) | Medio | Dimensionare sul **link budget**; antenne direttive; **HD robusto** invece di 4K fragile (§5). |
| **Hardware TLC estero** (sovranità) | Medio | Coerente con `Nota Strategica §2.2`: sovranità su **integrazione/architettura**, non sul modulo radio. |
| **Coesistenza payload↔C2** (interferenza sul radiocomando) | Medio | Bande separate, filtri, test EMC (§4, §7.3). |
| **Backhaul in area senza rete** | Medio | Satellite (§3.5) come opzione; altrimenti ponte radio verso nodo a terra. |

---

## 9. Raccomandazione (in una pagina)

1. **Perimetro onesto:** il ponte aereo del C3 è un **relay/gateway tattico-locale (R1, MANET)**, **funzione modulare di missione** (emergenza, aree interne, gancio politico), **non** infrastruttura di connettività regionale (che è HAPS). Coerente con `Fase A §4/§7` e `Nota Strategica §2.5`.
2. **Emissioni — due piani:** l'**apparato** è facile da rendere conforme (RED/CE con moduli COTS); il **vero lavoro è l'uso dello spettro** — verificare le bande **legali in volo** sul PNRF e, se serve, ottenere la **licenza sperimentale MIMIT**. **Aprire il dossier spettro presto**, in parallelo al SORA.
3. **Banda:** **non è un problema** — 100 Mbps di una MANET coprono 4K o più flussi HD; spendere il margine in **robustezza/bassa latenza**.
4. **Mercato:** **componenti maturi** (MANET, tethered, sat backhaul), **quasi tutti esteri**; **nessun prodotto integrato** "BVLOS C3 emissioni-UE + backhaul" → **si integra, non si compra**.
5. **Make:** ~**€15–45k incrementali** [stima] sul kit BVLOS base; due dossier paralleli — **A (spettro, MIMIT, 3–9 mesi)** e **B (BVLOS, ENAC, 7–18 mesi)**; dimostratore in **spazio riservato/sandbox** (aggira DAA e parte del problema interferenze).
6. **R2/R3 (cella/telefono volante):** solo via **partnership con un operatore mobile** (spettro licenziato, ECC (22)07) — **fase 2**, non partenza.

> **La frase da riunione:** *"Il ponte aereo è un **relay tattico** che sappiamo far volare (SORA) e far parlare **in regola** (spettro): la banda per le immagini in tempo reale è già risolta; il lavoro vero è **integrazione + due autorizzazioni** — e la connettività resta un **modulo/gancio**, non la promessa di coprire una regione."*

---

## 10. Domande aperte per la riunione

1. **Ruolo target del ponte:** confermiamo **R1 (relay MANET tattico)** come prodotto e **R2/R3 (cella/UE)** come fase-2-partnership?
2. **Bande candidate:** su quali bande **legali in volo in UE** progettiamo (2,4/5 GHz vs SRD sub-GHz)? Chi verifica il **PNRF** e apre l'eventuale **licenza sperimentale MIMIT**?
3. **Backhaul:** ponte radio a terra (default) o **satellite** (opzione peso/canone)?
4. **Consulenza spettro:** oltre alla consulenza SORA (EuroUSC-class), serve una **consulenza spettro/RF** per il dossier MIMIT — chi?
5. **Caso d'uso pilota:** **emergenza/Protezione Civile** (relay per squadre a terra) o **aree interne** (gateway IoT di valle)? *(Raccomandato: emergenza — domanda più concreta, spazio riservabile più facile.)*

---

## Fonti principali

**Normativa emissioni / spettro (UE):**
- Radio Equipment Directive **2014/53/UE** — EUR-Lex / Guida CE: https://ec.europa.eu/docsroom/documents/33162 · Wikipedia "Radio Equipment Directive (2014)" · ETSI RED: https://www.etsi.org/technologies/radio
- Standard armonizzati ETSI: EN 300 328 (2,4 GHz), EN 301 893 (5 GHz RLAN), EN 300 220 (SRD sub-GHz), EN 300 440 (SRD), EN 301 489 (EMC) — https://www.etsi.org/
- **ERC/REC 70-03** (SRD, bande e potenze) — CEPT/ECC (da consultare per i limiti EIRP/ERP vigenti).
- **ECC Decision (22)07** — aerial UE su LTE/5G NR (bande 703–733, 832–862, 880–915, 1710–1785, 1920–1980, 2500–2570, 2570–2620 MHz), nov. 2022 — https://docdb.cept.org/ · https://cept.org/
- **Mandato CEPT su UAS** (spettro droni, in corso) — https://cept.org/documents/ecc/81470/ecc-24-014_mandate-to-the-cept-on-uas
- **PNRF italiano** (MIMIT) — da consultare per l'uso nazionale/aereo delle bande.

**HAPS / spettro dal cielo (contesto, non nostro caso):**
- WRC-23: bande **2 GHz e 2,6 GHz** per HAPS/HIBS (18–25 km) — https://developingtelecoms.com/telecom-business/telecom-regulation/15959-wrc-23-identifies-more-spectrum-bands-for-5g-6g-and-haps.html · ITU HAPS backgrounder: https://www.itu.int/en/mediacentre/backgrounders/Pages/High-altitude-platform-systems.aspx

**Bitstream / video in tempo reale:**
- Bitrate H.265/H.264 (1080p ~2,25–3 Mbps; 4K ~12–16 Mbps HEVC) — arstech.net · antmedia.io · shoutcastnet.com

**Mercato off-the-shelf:**
- **Elistair** Safe-T 2 / Orion 2 (tethered comms 4G/Wi-Fi, fino a 50 h) — https://elistair.com/solutions/ · unmannedsystemstechnology.com
- **Silvus** StreamCaster MINI 5200 (100 Mbps, 182 g, 550+ nodi) — https://silvustechnologies.com/products/streamcaster-radios/ · uasweekly.com (gen. 2026)
- **Persistent Systems** MPU5 (Wave Relay, 3×3 MIMO) — https://persistentsystems.com/mpu5/
- Doodle Labs Mesh Rider, Domo Tactical (DTC) — datasheet vendor.

**Documenti del repository (base ENAC/BVLOS/mercato):**
- `Guida - Certificazione ENAC-SORA per il volo BVLOS` · `Guida - Tecnologie e Costi per la Certificazione BVLOS (OSO)` · `Nota Strategica - Alternativa Superiore a HALE` (§2.5, §2.7) · `Fase A - Downstream Civile Terrestre` (§4 connettività) · `Fase A - MARKET ANALYSIS REPORT`.

> ⚠️ **Onestà (come nel `Dossier di Verifica`):** i **limiti EIRP/ERP** e l'**ammissibilità dell'uso aereo** delle singole bande vanno **verificati sul testo vigente** (ERC/REC 70-03, PNRF, decisioni ECC) e con **MIMIT** — qui sono **riferimenti tipici [stima]**. I **prezzi MANET** e le **tariffe di licenza** sono **su preventivo/da verificare**. La tesi di fondo — **relay tattico sì, backbone regionale no; banda risolta; nodo = spettro + BVLOS** — è **robusta** e coerente con l'evidenza già consolidata nel repository (in particolare la fragilità del verticale connettività per un C3 a bassa quota, `Fase A §4`). Diversi siti istituzionali (EASA/EUR-Lex, ENAC, CEPT, vendor) bloccano il fetch automatico: dati raccolti via indicizzazione e corroborazione multipla.
