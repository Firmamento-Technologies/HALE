# Resoconto di revisione tecnica del repository — 15/07/2026

| | |
|---|---|
| **Oggetto** | Revisione critica indipendente di tutto il materiale presente nel repository H.A.L.E. (Firmamento Technologies) |
| **Perimetro** | I 14 documenti markdown della cartella `Ricerca 2 - Piano di Lavoro` (il corpus "vivo"). I file `.docx`/`.pdf` d'archivio (`da revisionare`, `Aree interne`, `bando`, `cad`, `Progetto concettuale struttura HALE.docx`) sono trattati come **input/base dati**, non come deliverable da giudicare. |
| **Metodo** | Lettura integrale; verifica di merito dei calcoli fisici first-order (rifatti a mano); controllo di coerenza interna documento-per-documento; confronto tra le conclusioni e l'evidenza citata. Nessun peso dato al fatto che una tesi fosse "già scritta": ogni conclusione è stata rivalutata da zero. |
| **Criterio dichiarato dal committente** | Valutare **quel che c'è**, non segnalare come "buchi" gli argomenti che è ovvio non siano ancora stati studiati; giudicare se **le conclusioni sono ragionevoli**. |
| **Nota sul nome file** | Richiesto "resoconto 15/07"; la `/` è separatore di percorso → salvato come `resoconto 15-07.md`. |

---

## 1. Giudizio sintetico

Il lavoro presente è, nel complesso, **di qualità metodologica alta e con conclusioni in larga parte ragionevoli e ben fondate**. Il nucleo fisico (energia/endurance, powertrain) è corretto al livello first-order che dichiara; il nucleo normativo (SORA/BVLOS/C3) è accurato e operativamente utile; l'impianto strategico ("ancora → scala", make-vs-buy) è coerente. Il progetto ha soprattutto **un tratto distintivo raro**: una disciplina esplicita "verificato vs stima vs confutato" (il `Dossier di Verifica`) che tiene onesto tutto il resto.

I limiti reali non sono di "conclusioni sbagliate" ma di **quattro tipi di fragilità**: (a) un **difetto di tracciabilità** — alcune correzioni del Dossier non sono state recepite in tutti i documenti derivati; (b) un **bilancio di massa che non chiude** perché omette la struttura; (c) una **tensione irrisolta tra "C3" ed endurance** che attraversa tutto il posizionamento; (d) un **singolo strappo allo standard di evidenza** sul box-wing. Nessuno è fatale; tutti sono chiudibili. Li dettaglio sotto.

---

## 2. Punti di forza (cosa regge, e perché)

**2.1 La catena energetica è corretta.** Ho rifatto i conti di `Trade Study §3`:
- Crociera: con MTOM 25 kg, V≈18 m/s, L/D≈16, P_aero = W·V/(L/D) = 245·18/16 ≈ 276 W; a valle di rendimento propulsivo ~0,6 → ~460 W elettrici. La banda dichiarata **350–500 W è corretta**.
- Batteria-sola: 24 h × ~400 W ≈ 9,6 kWh → a 160–200 Wh/kg a livello **pacco** servono ~48–60 kg. Conclusione "impossibile, realistico ~9–11 h": **solida**. La correzione cella↔pacco del Dossier (B6) rafforza ulteriormente la tesi.
- Solare: 1,4 m² × 24% × ~5,5 kWh/m²/gg estivi × perdite ≈ 1,5–1,75 kWh ≈ **~15% del fabbisogno estivo, ~4% invernale**. I numeri tornano e — cosa notevole — **il progetto resiste all'hype del "drone solare"** e qualifica il solare come supplemento e leva narrativa, non come motore. Questa è onestà tecnica, non marketing.

**2.2 Il trade di propulsione è la parte tecnicamente più forte.** L'analisi serie-vs-diretto è corretta: la doppia conversione della via serie (gen 0,90–0,94 × raddrizzatore × inverter × motore) dà ~0,78–0,86 cumulato contro ~0,97–0,99 del diretto; la penalità lorda ~15–18% si riduce a **~5–12% netti** grazie al motore tenuto al punto di minimo consumo. Il conto della potenza VTOL (T^1,5/√(2ρA): 245^1,5/√(2·1,225·0,5) ≈ 3,5 kW ideali → 6–7 kW elettrici) è **esatto**, e la deduzione "picco VTOL ≈ 10× la crociera → genset dimensionato sulla media + buffer per il picco" è corretta e ben usata. L'intuizione che **il tilt-rotor _impone_ la serie** (non si accoppia meccanicamente un termico a 4 rotori basculanti), e quindi che "serie/diretto" e "4/5 motori" **non sono scelte indipendenti**, è genuinamente acuta e ben argomentata.

**2.3 L'uso dei benchmark rivelati è corretto.** La penalità VTOL non è assunta ma **misurata** su dati reali: AR3 EVO 22 h→14 h (−36%) e, in modo indipendente, T-20 18 h → JUMP 20 10–13 h con lo stesso motore/cellula ma con il kit a 4 rotori. Due fonti che convergono sulla stessa conclusione ("VTOL modulare/rimovibile") sono un argomento robusto.

**2.4 Il blocco normativo è accurato e decision-useful.** C3 = <25 kg **E** <3 m; BVLOS = sempre "Specific" + SORA; strategia "VLOS-first, ricavi-first" con SORA istruito in parallelo. Corrisponde ai casi italiani reali (E-Distribuzione, Horus in R315, FlyingBasket LUC). La `Guida - Tecnologie e Costi` che scompone i costi per OSO e mostra che "spazio riservato vs condiviso" e "SAIL basso vs alto" spostano il budget di un ordine di grandezza è **tecnicamente corretta e concretamente spendibile**.

**2.5 La logica di mercato è coerente.** Il punto metodologico "l'ancora si misura con la spesa pubblica attivabile, non con il TAM" è corretto e non banale. Il posizionamento "quadrante libero {C3 <25 kg}×{ibrido}×{long-endurance}×{civile/dual-use}" diventa difendibile **dopo** la correzione onesta che Sky Eye Rapier esiste (ma a 50 kg/difesa). L'autocorrezione, invece di nascondere il concorrente, lo cita come prova di fattibilità: è la mossa giusta.

**2.6 Il Dossier di Verifica è il vero asset del repository.** 48 claim, verifica avversariale, citazioni verbatim, verdetti conservativi, e — punto raro — **la correzione dell'errore più grave lo ha trovato il progetto stesso** (le cifre SNAI "€100+100 mln" erano un artefatto d'estrazione PDF: refutate e sostituite con €198,6 mln + €11,4 mln da fonte parlamentare). Questo dà credibilità all'intero corpus.

---

## 3. Debolezze di merito (conclusioni da sfumare o da chiudere)

**3.1 Il bilancio di massa non chiude — manca la struttura.** È il rilievo tecnico più importante. Il team vuole **simultaneamente**: 24 h + payload 6 kg + modulo VTOL + assistenza solare + <25 kg. Il bilancio in `Trade Propulsione §4.5` elenca motore, alternatore, motori lift+booms, batteria buffer e carburante (≈14–18 kg per A1), ma **non conteggia la cellula, l'avionica e le celle solari**. Con una frazione strutturale realistica (empty-weight ~30–40% dell'MTOM ≈ 8–10 kg) + payload 6 kg, il totale sfonda i 25 kg. Il benchmark AR3 EVO fa 25 kg/6 kg/22 h **ma da ala fissa, senza kit VTOL a 4 rotori e senza solare**: impilarci sopra il modulo VTOL (2,5–4 kg) e il solare fa saltare il budget. La conclusione qualitativa ("la fisica non concede tutte e tre le cose") è giusta; ciò che manca è **il conto che mostra quanto payload si perde quando il VTOL è installato**. Finché il mass budget non include la struttura, "24 h + 6 kg + VTOL + solare < 25 kg" resta **non dimostrato**, anzi verosimilmente non simultaneamente fattibile.

**3.2 La tensione "C3 (<3 m)" vs "endurance (apertura lunga)" è il nodo centrale non sciolto.** Un'ala ottimizzata per l'endurance (L/D 14–20, alto allungamento) tende a **superare i 3 m** di apertura — l'AR3 EVO, benchmark di prestazione del progetto, è 3,5–4,2 m. Ma **>3 m = perdita della classe C3** e di ogni scorciatoia (STS/PDRA). Quindi il claim-bandiera "prima piattaforma **C3** long-endurance" rischia di essere **internamente contraddittorio**: con un'ala convenzionale si ottiene *o* la long-endurance *o* la classe C3 (<3 m), non entrambe. L'unico modo per tenere entrambe è che il box-wing consegni compattezza **e** efficienza insieme — che oggi è non dimostrato (vedi 3.3). Il repository sfiora il punto (bonus normativo del box-wing) ma non lo affronta di petto.

Correlato: **"C3" è usato con due significati diversi** — "classe di peso ~25 kg" e "classe normativa C3 open". Il Dossier (S15) ha esplicitamente avvertito che i sistemi che "validano" la classe (Flexrotor, AR3/AR5) **non sono C3-normativi**. Perciò l'affermazione ricorrente "il mercato valida la classe C3 <25 kg" è corretta solo per il **peso**, non per la **classe normativa**, che invece non è market-validata ed è in tensione con l'endurance. Da disambiguare ovunque.

**3.3 Il box-wing è l'unico punto in cui lo standard di evidenza si abbassa.** Il resto del corpus vive di "verificato vs stima". Sul box-wing, però, `WP-B5` e la `Nota Strategica` reintroducono un vantaggio di prestazione (aerodinamica + rigidità + compattezza "insieme") appoggiandosi a **"prime simulazioni interne del team" (rettifica 2026-07-14)** di cui **nel repository non esistono né dati né metodo né file** — e che servono a riaprire una conclusione che la letteratura peer-reviewed citata (MDPI 2023: beneficio solo strutturale-aeroelastico) e la verifica del claim IDINTOS L/D 18 avevano ridimensionato. Sul piano fisico un beneficio di resistenza indotta del box-wing (sistema di Prandtl) **esiste in teoria**, ma ai bassi numeri di Reynolds di un mini-UAV l'area bagnata extra e il drag di interferenza alle giunzioni tendono a mangiarlo — per questo la letteratura è cauta. Inoltre c'è una **contraddizione interna**: il vantaggio del box-wing nasce dall'estendere l'apertura effettiva, mentre "renderlo compatto (<3 m) per restare C3" sacrifica proprio quel meccanismo. Verdetto: il box-wing va tenuto **chiaramente subordinato** all'ala fissa convenzionale come baseline, e la "rettifica da simulazioni interne" andrebbe declassata a ipotesi da validare, non usata per pareggiare la matrice.

**3.4 Le matrici pesate sono illustrative, non decisive — ed è giusto dirlo.** Il `Trade Propulsione §6` lo ammette con onestà: A2 (serie) vince la matrice (86,8 vs 68,8) ma la raccomandazione è A1, perché "l'endurance non è un criterio fra tanti, è **il** proposito del prodotto" e la matrice la sotto-pesa. Bene l'onestà — ma la conseguenza è che **le decisioni reali sono prese su base narrativa/di posizionamento, non dal punteggio**. Lo stesso vale nel `Trade Study Architetture`: il box-wing supera l'ala fissa (81,4 vs 79,8) **solo grazie al criterio soggettivo P9 "Innovazione/Appeal" (peso 15, il più alto ex-aequo)**; l'analisi di sensibilità stessa mostra che abbassando P9 l'ala fissa torna prima. Il "flagship box-wing" è quindi una scelta **appeal-driven, non performance-driven**: legittimo per gli obiettivi del progetto (P8/P9 contano davvero per bandi e politica), ma va reso trasparente e non spacciato per esito tecnico.

**3.5 Rischio di sovra-lettura del mercato EMSA.** I contratti EMSA ~€30 mln sono **tetti di accordo-quadro pluriennali, subappaltati**, e vanno a grandi prime (Airbus/TEKEVER/IAI). Il corpus lo dice (bene), ma la headline dell'`One-pager` ("chi paga davvero: EMSA ~€30 mln") può indurre a leggerli come ricavo indirizzabile: per un nuovo entrante C3 la porta realistica è **sub-fornitore/operatore locale**, non sfidante frontale. Sfumatura di framing, non errore.

---

## 4. Difetti di coerenza interna (correzioni del Dossier non recepite)

Questo è il rilievo più **azionabile**: il `Dossier di Verifica` ha corretto vari claim, ma le correzioni sono state propagate soprattutto nello **strato di sintesi/strategia** (One-pager, Nota Strategica, Trade Study, WP-B5, Guide — tutti puliti) e **non** in modo completo nello **strato di output grezzo Fase A** e nel report consolidato. Elenco puntuale:

1. **`Fase A - Downstream Civile Terrestre` — errore refutato ancora presente come fatto.** §0 messaggio #6 (riga 24) e §5 tabella (righe 81–83) riportano ancora **"€100+100 mln CIPESS, €120 mln fondo, €172 mln (FSC 100 + FdR 72)"** — esattamente le cifre che il Dossier (claim **A1, CONFUTATO**) ha dichiarato inesistenti. Il banner di correzione in testa **non copre** questa sezione. È il residuo più serio.
2. **`Fase A - Downstream Civile Terrestre` §1 (righe 32–34) e msg #4 (riga 22):** "servizi EO a valore aggiunto €2,8→6,7 mld — **Confidenza Alta**", in contraddizione diretta col Dossier **D1** (cifra **non verificabile** indipendentemente, da non citare come dato EUSPA).
3. **`Fase A - MARKET ANALYSIS REPORT (consolidato)` §2 (riga 60):** stessa cifra EO value-added marcata "**Alta**" — contraddice D1. Trattandosi del documento **consolidato v1.0**, è più grave che nell'output grezzo.
4. **`Fase A - MARKET ANALYSIS REPORT (consolidato)` §10 (riga 192):** tra le "Fonti chiave" compare ancora **"PSNAI (CIPESS €100+100 mln)"** — la cifra refutata, citata come fonte-pilastro.
5. **`Fase A - Approfondimento Subacquea` §3 (riga 63):** "**1,2 mln km di condotte offshore — Alta**", in contraddizione col Dossier **S11** (sovrastima ~10×; da evitare il valore). Anche qui il banner in testa non copre S11.
6. **`Fase A - Approfondimento Subacquea` §7 (riga 109) e msg #6 (riga 29):** budget EDF topic "**~€30 mln**", mentre il Dossier **S18** lo ha corretto a **~€20 mln** (i ~€30 mln sono l'intera call). Il documento porta contemporaneamente il banner corretto (€20 mln) e il corpo non corretto (€30 mln): contraddizione interna.
7. **`Fonti primarie - Spesa pubblica SNAI` — footer (riga 48):** nota di chiusura stantia "*Voci discorsive (CIPESS €100+100 mln, fondo €120 mln) lette in modo netto*", che contraddice il corpo dello stesso file (che quelle cifre le scarta). Refuso residuo, minore.

**Lettura d'insieme:** il metodo dichiara "catena di tracciabilità unica" e "correzioni da recepire nei report"; il difetto è che la propagazione si è fermata a metà. È una **pulizia editoriale**, non una riscrittura — ma finché non è fatta, un lettore che apra i documenti Fase A grezzi o il consolidato **trova ancora dati che il progetto stesso ha già refutato**, il che eroderebbe proprio la credibilità che il Dossier costruisce.

---

## 5. Osservazioni minori

- **Efficienza motori piccoli (Dossier B7):** il range 22–28% è corretto per motori UAV medi (~100–500 cc) ma ottimistico per i 2T <100 cc (un 55 cc reale ~14%). I conti di carburante usano la fascia media: per il *dimostratore* con motorino piccolo il consumo reale potrebbe essere peggiore → margine da tenere. Già segnalato dal Dossier, ma non ribaltato nei budget.
- **Coerenza classe AR3 EVO:** ottimo che sia stato corretto ("non è C3"); va solo verificato che il messaggio "benchmark di peso, non di classe normativa" sia uniforme in tutti i documenti (nel consolidato e nell'One-pager la parola "C3" resta ambigua).
- **Cartella `da revisionare`:** contiene i 4 `.docx` della 1ª ricerca (relazione comparativa HALE/VTOL, studio SNAI Liguria ~250 pag., briefing, divulgativo). Non li ho aperti in dettaglio (non testuali via tool) ma il Piano di Lavoro li tratta correttamente come base-dati/benchmark da riusare, non da rifare: impostazione condivisibile.
- **CAD (`cad/`):** immagini concept coerenti con l'"aliante motorizzato ad alto allungamento, elica traente al muso" descritto nel Trade Propulsione. Nessuna analisi strutturale/aeroelastica presente — legittimo a questo stadio.

---

## 6. Conclusione sulla ragionevolezza

**Le conclusioni principali sono ragionevoli e reggono all'esame:** (a) 24 h a <25 kg richiede propulsione a combustibile/ibrida, non batteria né solare; (b) il solare è supplemento; (c) il VTOL va tenuto modulare/rimovibile; (d) per l'ala fissa da endurance la crociera a trasmissione diretta è la scelta giusta, la serie se serve hover/silenzio, il tilt-rotor è ultimo; (e) BVLOS è un problema normativo prima che tecnologico, da aggredire VLOS-first; (f) strategia "ancora → scala" con doppio binario BUY/MAKE. Tutte sono coerenti con l'evidenza citata e con la fisica ricalcolata.

Le **due conclusioni da trattare con più cautela** di quanto il corpus faccia sono: il **box-wing come "candidato di prestazione"** (oggi appeal-driven e sotto-supportato) e la **fattibilità simultanea di "24 h + payload pieno + VTOL + solare + C3<3m"** (il mass budget non lo dimostra e la fisica dell'apertura lo mette in dubbio). Non invalidano l'impianto: lo delimitano.

---

## 7. Cosa manca ancora (lista ordinata)

*(Macro-argomenti; ordinati per priorità logica verso lo Studio di Fattibilità. Esclusi gli argomenti che è ovvio non siano ancora stati affrontati per fase.)*

1. **Chiusura del bilancio di massa completo** — includere frazione strutturale, avionica e celle solari, e mostrare esplicitamente il payload residuo con e senza modulo VTOL: è la verifica che oggi manca per dire se "<25 kg" chiude davvero.
2. **Scioglimento della tensione C3 vs endurance** — decidere se il prodotto è C3-normativo (<3 m, con perdita di endurance) o solo classe-peso ~25 kg (>3 m, sempre "Specific"): oggi il posizionamento le tiene entrambe senza dimostrarlo.
3. **Validazione aerodinamica reale** — L/D e potenza di crociera dedicati; soprattutto CFD + galleria + dimostratore in scala per il box-wing a basso Reynolds (le "simulazioni interne" citate non sono nel repository).
4. **Recepimento completo delle correzioni del Dossier** nei documenti derivati (§4 di questo resoconto): pulizia di tracciabilità, non riscrittura.
5. **Dati di costo/prezzo reali** — RFQ ai vendor e banche dati procurement (TED/EU, Gazzetta Ufficiale): prezzi di sistema, valore effettivo dei contratti EMSA, canoni DaaS, €/ora di volo, costo del powertrain per le opzioni make/licenza.
6. **Dimensionamento quantitativo dei segmenti terrestri** (TAM/SAM/SOM Italia/Liguria/UE) — incendi, dissesto, ispezione lineare, agricoltura (con WTP per ettaro): oggi nessuna cifra segmentata è sopravvissuta alla verifica.
7. **Spesa pubblica attivabile oltre SNAI** — PNRR (dissesto idrogeologico, banda ultralarga aree bianche/grigie), budget Protezione Civile nazionale e Regione Liguria in EUR.
8. **Verifica dei lead territoriali** — servizio EMSA sul Golfo di Genova (AR-5 Evo/REACT/Guardia Costiera), bando "Underwater Liguria" ~€7,5 mln, numeri di funding effettivi del PNS.
9. **Banco prova propulsione** — rendimenti reali della catena serie, BSFC del motore candidato al punto ottimo, potenza VTOL reale (disco/FoM), e vibrazioni monocilindrico → jitter gimbal (critico per l'ISR).
10. **Definizione dei payload reali** per nicchia (peso, potenza, costo di EO/IR, SAR, relay, sonobuoy) — il vincolo payload→piattaforma è ancora solo parametrico.
11. **Istruttoria del percorso certificativo** — dossier SORA, scelta SAIL/area, consulenza, e chiusura delle incognite normative (deadline transizione SORA 2.0→2.5, IT-PDRA applicabile al caso).
12. **Modello economico-finanziario e funding roadmap** (Fase C) — unit economics, break-even, TCO, costo di ciclo-vita/ora, attrition; e **strategia di consorzio EDF** (l'accesso dual-use è mediato, non diretto).
13. **Make-vs-buy con numeri** — economia reale dell'integrare una piattaforma commerciale (Flexrotor/AR3/AR5) come service provider vs costruire il velivolo proprietario.
14. **Redazione dello Studio di Fattibilità 2.0** (deliverable finale D-C) — l'integrazione decision-ready di Fasi A/B/C, ancora da produrre.

---

*Revisione indipendente. I calcoli fisici first-order sono stati ricontrollati a mano e risultano coerenti con quanto dichiarato nei documenti; le cifre di mercato e di costo restano — per esplicita ammissione del corpus — direzionali/stime da confermare via RFQ e procurement. Il giudizio complessivo è positivo sul metodo e sulle conclusioni-nucleo, con i quattro cantieri aperti indicati ai §3–§4 come priorità di chiusura.*
