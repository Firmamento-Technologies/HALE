# 00 — Sintesi strategica: ripartenza da zero (service-first)

> **Natura del documento.** Sintesi di sei ricerche indipendenti condotte *ripartendo da zero*, senza assumere le conclusioni pregresse dello Studio (impianto 6A/6B, scelta HALE/JOUAV). La piattaforma è stata trattata come **variabile da determinare**, non come premessa. Ogni flusso aveva mandato di **falsificare** l'idea, non di difenderla. È un documento di **supporto alla decisione**, non un verdetto chiuso: la scelta strategica finale è dell'utente.
>
> **Fonti:** i sei report in questa cartella (`01-connettivita` … `06-finanziabilita`) + lo script link-budget `lb_bottomup.py`. Confidenza dichiarata per ogni claim.

---

## 1. La domanda, ribaltata

Non *"come costruiamo un HALE?"* ma:

> **Qual è il servizio che serve alle Aree Interne, quanto vale, e qual è la piattaforma minima e finanziabile che lo eroga con il miglior rapporto costi/benefici?**

Servizio ipotizzato: portare **connettività + osservazione** ("un po' il mestiere del satellite, ma limitato") a un borgo/valle montana (caso pilota: **Pentema, Torriglia GE**), come **servizio ricorrente** erogato da un operatore cooperativo, **finanziabile** da Regione / Legacoop / CDP / Coopfond.

---

## 2. Cosa dicono i sei flussi (convergenza)

| # | Flusso | Verdetto sintetico | Confidenza |
|---|--------|--------------------|-----------|
| 1 | **Connettività** | Il link RF **non è il vincolo** (D2D chiude a ogni quota per prossimità). Ma per la **sola banda larga Starlink batte l'aereo di 1–3 ordini di grandezza**. Razionale solo come *resilienza d'emergenza / IoT d'area*, connettività **secondaria**. | Alta (link+prezzi); Media (requisiti-quota) |
| 2 | **Osservazione Terra** | La maggior parte dei servizi EO è **dominata da Copernicus (gratis) o da drone COTS a noleggio**. Unico discriminante: la **persistenza** (loitering), utile a **2 soli servizi** (early-detection incendi, overwatch emergenza). Piattaforma minima: **VTOL/fixed-wing 6–10 h**, non MALE/HALE. | Alta (fatti); Media (giudizio economico) |
| 3 | **Mercato** | Mercato pagante **piccolo**: SOM base **€250–500k/anno** (best <€1,8M, grant inclusi). Tetto d'investimento razionale **~€1–1,2M e solo se in prevalenza grant**. HALE (€5,5–11M) **non ripagato di 1–2 ordini di grandezza**. Segmento più solido: **B2G territorio, EO grant-anchored**. | Alta (budget); Bassa-Media (SOM) |
| 4 | **Regolatorio** | Costo/tempo di compliance cresce **a scalini** → il minimo attrito **spinge verso il basso**. Percorso: **C3 <25 kg Open A3 subito** (€1–5k) → **piccolo UAS BVLOS Specific SAIL II** (non III). HALE = Certified, 5–8 anni, **nessun framework HAPS**. | Alta (categorie); Media (SAIL) |
| 5 | **Costi piattaforme** | **Comprare COTS batte costruire custom.** Box-wing C3 custom→prodotto certificato = **€3–10M+**, come una piccola flotta VTOL COTS ma senza colmare requisiti. **Aerostato tethered** (€150–700k) è l'unico che dà persistenza **senza moltiplicatore di flotta** (ma su un solo punto). | Alta (prezzi COTS); Media (custom/aerostato) |
| 6 | **Finanziabilità** | Tetto "sicuro" **Taglia A ~€1M** (prob. 60–75%), **non facile**: stacking 5–6 strumenti + **equity founder €150–350k** + CapEx su 18–24 mesi. Coop di comunità con cassa minima (€20–100k) **non coprono il cofinanziamento**. Taglia B (€3–8M) solo con equity esterna + veicolo SpA. HALE fuori portata. | Alta (Coopfond €50k certo); Media (mix) |

**La convergenza è netta e in una sola direzione:** *piccolo, COTS, sotto €1M, servizio EO/territoriale grant-anchored; HALE (e in gran parte MALE) fuori portata di questo veicolo.*

---

## 3. Il risultato scomodo: il "triangolo impossibile"

Incrociando i flussi emerge una **contraddizione strutturale** che la vecchia impostazione nascondeva. I tre vertici che vorremmo tutti insieme:

- **(A) Servizio che si differenzia davvero** dai sostituti gratuiti/economici (Starlink, Copernicus, droni COTS). L'unico candidato reale è la **presenza persistente su area vasta** (resilienza d'emergenza multi-valle + overwatch continuo) — ciò che *né* il satellite *né* il drone-spot offrono.
- **(B) Piattaforma finanziabile & a basso attrito regolatorio**: COTS / piccolo VTOL / singolo aerostato tethered, sotto ~€1M.
- **(C) Finanziabile dall'ecosistema cooperativo** (tetto ~€1M).

**Se ne ottengono due, non tre:**

| Vuoi… | Ottieni | Ma violi |
|---|---|---|
| Connettività/resilienza persistente **su area vasta** (A) | serve ≥8–12 km di quota + endurance multi-giorno → **MALE/HALE** | **B** e **C** (decine–centinaia di M€) |
| Piattaforma economica & finanziabile (B+C) | drone COTS / VTOL breve / aerostato su **singolo punto** | **A** (servizi dominati dai sostituti, o copertura di un solo borgo) |

**Conseguenza (confidenza medio-alta):** *non esiste una piattaforma aerea dedicata che chiuda il business case come "sostituto del satellite" dentro l'inviluppo finanziabile.* La cornice "piattaforma pseudo-satellitare" **non sopravvive all'urto con Starlink + Copernicus**. Il VTOL a batteria — la classe più finanziabile — è ottimo per EO/emergenza spot ma **fallisce la persistenza** per la connettività continua; l'unica cosa che dà persistenza a basso costo (aerostato tethered) copre **un solo punto**, non una valle.

Questo **non** significa "progetto morto". Significa che **il valore non è nell'hardware, è nel servizio integrato che la cooperativa gestisce.**

---

## 4. La nicchia difendibile (se c'è)

Spostando il baricentro *dalla piattaforma al servizio*, resta una wedge stretta ma reale:

> **Operatore cooperativo di servizi territoriali di monitoraggio & resilienza per le Aree Interne**, *asset-light*, che **orchestra**:
> 1. **Copernicus** (gratis) per il wide-area lento (frane, vegetazione, post-incendio);
> 2. **droni COTS on-demand** (propri o a noleggio) per il dettaglio point-in-time (ispezioni, fronte-frana, plot);
> 3. **un aerostato/drone tethered** per la **persistenza locale** nelle finestre ad alto rischio (stagione incendi, emergenze Protezione Civile) — il vero elemento che nessun sostituto offre;
> 4. **connettività d'emergenza/IoT d'area** come funzione **secondaria** (LoRa 868 subito; broadband solo via hosting MNO, non banda HAPS dedicata).

Il differenziatore **non è il velivolo**: è **il servizio persistente, locale, organizzato e la resilienza in emergenza**, con la rete cooperativa come radicamento territoriale e canale verso la PA.

**Segmento pagante-àncora:** B2G territorio (Regione Liguria + Unioni SNAI + Enti Parco + Protezione Civile), grant-anchored. Solido non per willingness-to-pay ma per **allineamento a fondi che esistono** e a una missione pubblica.

---

## 5. La soluzione ingegneristica che ne deriva (per soglia di budget)

La piattaforma **non si sceglie a priori**: la seleziona il budget finanziabile. Ordinata per soglia:

| Soglia | Piattaforma con miglior costi/benefici | Cosa eroga |
|---|---|---|
| **≤ €1M (target)** | **Drone/VTOL COTS** (EO spot, €40–120k a programma) **+ 1 aerostato tethered** (persistenza locale, €150–700k) + orchestrazione Copernicus | EO territoriale + persistenza in finestra + IoT + resilienza single-point. **Finanziabile, basso attrito regolatorio.** |
| **< decine di M€** | Flotta **VTOL heavy ridondante** (2–3 unità, €2–5M) o **MALE** (benchmark EMSA €7,5–8,75M/anno) | Persistenza su area più ampia. **Richiede equity esterna + veicolo SpA.** |
| **centinaia di M€** | **HALE stratosferico** | Copertura regionale persistente. **Fuori portata del veicolo cooperativo.** |

**Build vs Buy:** *Buy COTS* vince nettamente per il servizio Y1. Costruire un velivolo custom (box-wing C3, o a maggior ragione HALE) ha senso **solo** se dichiarato esplicitamente come **banco-prova IP** per una traiettoria di lungo periodo, **finanziato a parte** (R&D: Horizon/EDF/EUSPA) e **scorporato dal conto economico del servizio**.

---

## 6. Raccomandazione operativa (a gate)

1. **Lo Studio di Fattibilità (€100k, già finanziato Coopfond €50k) è giustificato** — ma va **riorientato**: da "fattibilità di un HALE" a **"fattibilità di un operatore cooperativo di servizi territoriali di monitoraggio e resilienza"**, con la piattaforma come *scelta derivata*, non come tesi di partenza.
2. **Gate 0 — subito, <€50k:** servizio EO spot con drone **C3 in Open A3 VLOS**; orchestrazione Copernicus; **1 LoI Regione Liguria** + 1 convenzione con un Ente Parco/Unione SNAI. Zero SORA, zero rischio.
3. **Gate 1 — M+12, ≤€1M spalmato 18–24 mesi:** aggiungere **persistenza** (aerostato tethered su un sito pilota Pentema + un piccolo UAS BVLOS **Specific SAIL II**); connettività IoT/emergenza via hosting MNO. **Condizione d'ingresso:** equity founder €150–350k impegnato + ≥1 convenzione regionale pluriennale.
4. **Gate 2 — solo se il servizio dimostra ricavi:** valutare Taglia B (flotta VTOL/MALE) con veicolo SpA + equity di rischio.
5. **Traiettoria HALE:** mantenuta come **vettore strategico Y6+** e come **linea R&D separata** (banco-prova IP, fondi UE), **non** come procurement del servizio.

---

## 7. Pre-mortem e criteri di falsificazione (kill criteria)

Il progetto va **congelato o riorientato** se, entro le scadenze, si verifica uno di questi (dai flussi 3 e 6):

- **M+24:** manca una **convenzione regionale ≥ €100k/anno** *oppure* **≥ €150k di ricorrente non-grant** → *lo scenario base di mercato è falsificato*; stop a ogni investimento in piattaforma dedicata.
- **Gate 1:** il **founder non impegna l'equity** €150–350k → il cofinanziamento del €1M non si chiude (le coop non hanno cassa) → resta solo il perimetro Gate 0.
- **Aerostato tethered:** il **vento incanalato di valle a Pentema** (mai verificato su fonti indipendenti) rende inutilizzabile l'aerostato → la persistenza single-point più economica cade e va rivalutata la wedge.
- **Connettività:** **Starlink Direct-to-Cell** arriva a copertura utile prima del servizio → la componente connettività (già secondaria) diventa **irrilevante**.
- **EO:** se nessun ente firma per la **persistenza** (l'unico differenziatore), il servizio degrada a **rivendita di Copernicus + noleggio droni**, che non giustifica una struttura dedicata.

---

## 8. Cosa cambia rispetto all'impianto pregresso

- L'impostazione **6A (VTOL) / 6B (HALE)** partiva dalla **piattaforma**; qui la piattaforma è **derivata** dal servizio e dal budget → l'esito naturale è **più in basso** (COTS + aerostato) di quanto lo Studio attuale assuma.
- L'allegato SORA (`A11`) fissa **SAIL III** su una densità sovrastimata; a Pentema la densità reale (<5 ab/km²) porta un piccolo UAS a **SAIL II** → *scendere di piattaforma abbassa anche l'onere regolatorio* (doppio dividendo).
- Il capitolo mercato (`cap-07`) proietta un SOM (€1,5–3,5M) **non supportato** dai budget reali; la base realistica è **€250–500k/anno**.
- La tesi "operatore di servizi, non OEM" **è corretta e va spinta più a fondo**: il vantaggio è nell'**integrazione di servizio asset-light**, non nel possedere un velivolo esotico.

---

### Riga di fondo

> Ripartendo da zero, la ricerca **non** conferma un velivolo dedicato come risposta. Conferma un **operatore cooperativo di servizi territoriali** (Copernicus + drone COTS + un tocco di persistenza tethered), **sotto €1M**, con la connettività come funzione secondaria e l'HALE relegato a R&D di lungo periodo. La domanda vera per la decisione non è più *"quale velivolo"* ma *"esiste un cliente ancora (una convenzione regionale) disposto a pagare la persistenza?"* — ed è quello il primo esperimento da fare, non un aereo da costruire.
