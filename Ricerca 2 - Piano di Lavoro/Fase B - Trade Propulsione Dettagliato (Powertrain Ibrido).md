# Fase B — Trade Propulsione Dettagliato: Powertrain Ibrido
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Trade propulsione dettagliato: architettura del powertrain ibrido (motore termico + buffer batteria), serie vs diretto, 5 motori vs 4 tilt-rotor |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-13 |
| **Input** | `Fase B - Trade Study Architetture` (§6 lacuna "Trade propulsione dettagliato"); concept CAD nel branch (ala fissa alto allungamento, elica traente al muso) |
| **Metodo** | Budget first-order di potenza/energia/massa + catena di rendimenti stadio-per-stadio + benchmark commerciali reali + matrice pesata delle configurazioni |
| **Scopo** | Rispondere al quesito: **per il volo di crociera (ala fissa) è meglio il motore termico in asse all'elica (diretto) o in serie a un alternatore (elettrico)?** e confrontare le configurazioni a **5 motori** (4 lift + 1 crociera) vs **4 motori tilt-rotor**. |
| **Nota** | Analisi **first-order** stage-appropriate per la fattibilità: stime parametriche esplicite, non design di dettaglio. Dove serve banco/CFD/test è indicato. |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** i numeri di massa/energia sono **stime parametriche** calcolate qui esplicitamente; i benchmark commerciali riportano **fonti**. Le percentuali di rendimento sono valori tipici di letteratura (banda), non misure sul nostro sistema.

---

## 0. Executive summary — la risposta al quesito

**Non è "l'alternatore" o "l'elica in asse" in assoluto: la risposta dipende da UNA condizione — se il velivolo deve fare VTOL o no.**

| Missione del velivolo | Architettura di crociera migliore | Perché |
|---|---|---|
| **Ala fissa pura, endurance-max (nessun hover)** | **Motore termico in asse all'elica (diretto)** | Nessuna doppia conversione: rendimento crociera **~97–99%** vs **~78–86%** della via elettrica. È ciò che fanno i benchmark endurance reali (ScanEagle, AR5). Protegge le 24 h. |
| **VTOL integrato (4+ rotori di sollevamento a bordo)** | **Dipende dal peso dell'hover:** se l'hover è breve (decollo/recupero) → crociera **diretta** + lift elettrici (A1); se l'hover è centrale o serve modo silenzioso → **serie** (A2) | Il bus elettrico, la batteria e i controller ci sono **già** per l'hover; in serie si riusano anche per la crociera, si fa girare il motore al punto di minimo consumo, si ha modalità silenziosa e ridondanza a batteria. **Il 100% dei VTOL ibridi _multirotore_ commerciali è serie; tra i VTOL _ad ala fissa_ a benzina prevale invece la crociera diretta (A1: JUMP 20, Foxtech Great Shark).** |

**Le tre configurazioni proposte, ordinate per la nostra missione (24 h è il driver, il VTOL è un modulo opzionale — cfr. Trade Study §5):**

| # | Configurazione | Architettura | Verdetto per HALE | Punteggio |
|---|---|---|---|---|
| **A1** | **5 motori, spingente/traente in asse al termico** (4 lift elettrici + 1 elica a trasmissione diretta ICE) | Ibrido **parallelo/diretto** (termico meccanico in crociera, batteria per il VTOL) | ✅ **Miglior endurance.** Evoluzione naturale del CAD attuale (elica al muso a trasmissione diretta) + modulo VTOL a batteria. **È il pattern reale di AeroVironment JUMP 20 e Foxtech Great Shark.** | **★ Raccomandato per l'endurance** |
| **A2** | **5 motori, spingente/traente elettrico su bus** (4 lift + 1 crociera elettrici; ICE→alternatore→bus+batteria) | Ibrido-**serie** puro | ✅ Miglior flessibilità operativa (silenzioso, ridondante). Paga ~5–12% di consumo in crociera. | ★ Raccomandato se serve modo elettrico/ridondanza |
| **A3** | **4 motori tilt-rotor** (gli stessi 4 rotori fanno VTOL e crociera; ICE→alternatore→bus+batteria) | Ibrido-**serie obbligato** (non si può mettere in asse un termico su 4 rotori basculanti) | ⚠️ Elegante come conteggio parti, ma **peggiore per l'endurance** (penalità serie su tutte le 24 h) + rischio meccanismo di tilt + eliche "di compromesso". | Ultimo per QUESTA missione |

**Osservazione dell'utente confermata dalla fisica:** con i tilt-rotor **non ha senso un termico per rotore** (4 motori termici basculanti = massa, vibrazioni, logistica, sincronizzazione impossibili). **Un solo alternatore che alimenta i 4 motori è l'unica opzione sensata** → il tilt-rotor **impone** l'architettura serie. Questo è il punto chiave: *scelta serie/diretto e conteggio motori NON sono indipendenti* (vedi §2).

**Raccomandazione sintetica:** cellula ad **ala fissa con elica al muso a trasmissione diretta** (motore termico in asse) come **spina dorsale dell'endurance**, con **piccolo alternatore/ISG sull'albero** per ricaricare il buffer e alimentare avionica/payload; **modulo VTOL a 4 rotori elettrici, rimovibile**, alimentato dalla batteria buffer per le sole missioni con decollo verticale. Se il caso d'uso è **hover-loiter frequente o modalità silenziosa obbligatoria** (ISR/marittimo), si passa alla variante **serie A2**. Il tilt-rotor A3 resta come opzione da valutare solo se il profilo di missione diventasse VTOL-intensivo.

---

## 1. Il quesito e il contesto

### 1.1 Da dove partiamo (concept nel branch)
Il CAD attuale nel repository mostra un **aliante motorizzato ad alto allungamento**: ala sottile di grande apertura, trave di coda snella, impennaggio a T e **una singola elica traente al muso** (configurazione *tractor*), con analisi CFD (Cp) già eseguita sull'ala. È la **"versione performance" (B)** del Trade Study: ala fissa ottimizzata per l'endurance. Il powertrain è concentrato in un pod al muso che aziona **un'unica elica in presa diretta** — che mappa naturalmente su **un motore termico in asse** o su **un singolo motore elettrico**.

### 1.2 Cosa è già stato deciso (Fase A/B)
- **Via energetica:** le 24 h a <25 kg sono possibili **solo** a combustibile/ibrido (batteria-sola ≈ 9–11 h; solare = supplemento ~4–15%). → il motore termico è **irrinunciabile** per l'endurance.
- **Architettura di cellula:** ala fissa vince sull'endurance; **VTOL come modulo opzionale rimovibile** (penalità −36% endurance se permanente, dato AR3 EVO).
- **Propulsione:** "ibrido-elettrico (generatore + buffer batteria)" già raccomandato in linea di principio — **ma senza scegliere serie vs diretto né il numero di motori**. Questo documento chiude quella lacuna.

### 1.3 Il quesito, formalizzato
Il team pone due domande accoppiate:
1. **Catena di trazione in crociera:** motore termico **in asse all'elica** (trasmissione meccanica diretta) **oppure** motore termico **in serie a un alternatore** che alimenta un motore elettrico sull'elica?
2. **Conteggio e ruolo dei motori:** **cinque** motori (4 per il decollo verticale + 1 per il resto della missione) **oppure quattro** (tilt-rotor: i 4 del decollo, dopo la transizione, diventano traenti)?

Con, come vincolo di sistema: **motore monocilindrico benzina + pacco batteria come buffer**, e la richiesta di **vagliare motori termici alternativi**.

---

## 2. Tassonomia rigorosa delle architetture

Le architetture proposte si collocano su una griglia a due assi: **(asse 1) sorgente della spinta di crociera** × **(asse 2) numero/ruolo dei motori**.

```
                    │  SPINTA CROCIERA = ICE IN ASSE   │  SPINTA CROCIERA = MOTORE ELETTRICO
                    │  (trasmissione diretta)          │  (ibrido-serie, ICE→alternatore)
────────────────────┼──────────────────────────────────┼──────────────────────────────────────
 5 MOTORI           │  A1                               │  A2
 (4 lift + 1 cruise)│  4 lift elettrici (batteria)      │  4 lift + 1 cruise elettrici
                    │  + 1 elica ICE diretta            │  tutti da ICE-alternatore + buffer
────────────────────┼──────────────────────────────────┼──────────────────────────────────────
 4 MOTORI           │  A4 — IMPOSSIBILE                 │  A3
 (4 tilt-rotor)     │  (un ICE non può azionare in asse │  4 tilt-rotor da ICE-alternatore
                    │   4 rotori che basculano)         │  + buffer batteria
```

### 2.1 A1 — Cinque motori, spingente/traente in asse al termico *(ibrido parallelo/diretto)*
- **Crociera:** l'elica principale (al muso, come nel CAD, o spingente) è **in presa diretta col motore termico** (eventuale riduttore leggero). Massimo rendimento.
- **VTOL:** 4 rotori **elettrici** su braccetti/booms, alimentati dalla **batteria** (l'ICE non li tocca).
- **Ricarica:** un **piccolo alternatore/ISG** (integrated starter-generator) sull'albero motore ricarica il buffer in crociera e alimenta avionica/payload/solare-assist.
- **Natura:** è di fatto un **ibrido parallelo "through-the-road"** — due catene distinte (termica per la crociera, elettrica per l'hover) che condividono solo la batteria/ISG.
- **Nota:** è la **minima modifica** al concept CAD esistente (aggiungi booms + 4 rotori + batteria; il muso resta a trasmissione diretta).

### 2.2 A2 — Cinque motori, spingente/traente elettrico su alternatore *(ibrido-serie puro)*
- **Crociera:** motore elettrico dedicato sull'elica principale.
- **VTOL:** 4 rotori elettrici.
- **Sorgente:** il **motore termico non tocca mai un'elica** — gira a giri/carico costante (punto di minimo consumo) trascinando l'alternatore che carica il **bus DC**; la **batteria buffer** livella i picchi (VTOL) e consente il **dash elettrico silenzioso**.
- **Natura:** **serie** classico (range-extender). Cinque motori elettrici, un genset.

### 2.3 A3 — Quattro motori tilt-rotor *(ibrido-serie obbligato)*
- **VTOL + crociera:** gli **stessi 4 rotori** basculano da verticale (hover) a orizzontale (crociera) dopo la transizione.
- **Sorgente:** obbligatoriamente **ICE→alternatore→bus+batteria** (vedi §2.4).
- **Vantaggio teorico:** nessun rotore "morto" in crociera (i lift diventano cruise) → conteggio motori minimo (4).
- **Prezzi da pagare:** meccanismo di tilt (attuatori, giunti, rischio in transizione), **eliche di compromesso** (un'elica buona per l'hover — alto diametro, basso passo — è mediocre in crociera e viceversa), 4 eliche di crociera aerodinamicamente peggiori di **una** ben adattata, penalità serie su **tutta** la crociera di 24 h.

### 2.4 A4 — Perché "4 motori con termico in asse" è impossibile (e l'utente ha ragione)
Per avere la spinta di crociera "in asse al termico" servirebbe che l'albero motore aziona l'elica **meccanicamente**. Ma nei tilt-rotor le eliche di crociera **sono** i 4 rotori basculanti, distribuiti sull'apertura e orientabili: **un solo motore termico non può azionarli meccanicamente** (dovrebbe avere 4 alberi cardanici basculanti — assurdo). L'unica via "in asse" sarebbe **un motore termico per rotore** = **4 motori termici basculanti**, che l'utente scarta correttamente: massa proibitiva, 4× vibrazioni/manutenzione, sincronizzazione di coppia e di beccheggio praticamente irrisolvibile, logistica carburante/avviamento ×4. **Conclusione: il tilt-rotor implica necessariamente l'architettura serie con un solo alternatore.** → *La scelta "serie vs diretto" e "4 vs 5 motori" sono accoppiate: 4 tilt-rotor ⟹ serie.*

### 2.5 A1b — Variante parallela integrata (menzione onesta)
Esiste una quarta architettura sensata: **ICE sull'elica di crociera con motore-generatore (ISG) sullo stesso albero**. In crociera l'ICE traina l'elica **direttamente** (max rendimento) e l'ISG **ricarica**; in fase VTOL l'ICE+ISG lavorano da **genset** per alimentare i 4 lift (oppure la batteria fa tutto). È la più **efficiente** in crociera *e* ricarica, ma aggiunge frizione/complessità sull'albero e mal si sposa con le vibrazioni di un **monocilindrico**. È un raffinamento di A1, da valutare in Fase C.

---

## 3. La domanda centrale: alternatore in serie vs elica in asse

### 3.1 La penalità fisica della via elettrica (doppia conversione)
Nell'ibrido-serie l'energia meccanica del motore viene **convertita due volte** (albero→elettricità→albero elica). Ogni stadio ha un rendimento < 1:

| Stadio (via serie: albero ICE → elica) | Rendimento tipico η |
|---|---|
| Generatore/alternatore (PMSG) | 0,90–0,94 |
| Raddrizzatore / elettronica di potenza | 0,96–0,98 |
| Bus DC / DC-DC / distribuzione | 0,98–0,99 |
| Inverter + motore elettrico | 0,90–0,94 |
| (Riduttore elica, se presente) | 0,97–0,99 |
| **Prodotto cumulato (senza riduttore extra)** | **≈ 0,78–0,86** |

| Via diretta (albero ICE → elica) | Rendimento tipico η |
|---|---|
| Riduttore/cinghia leggero (o presa diretta) | 0,97–0,99 |
| **Prodotto** | **≈ 0,97–0,99** |

**Penalità lorda della via serie in crociera ≈ 1 − 0,82/0,98 ≈ 15–18%** di potenza d'albero in più per la stessa spinta → **più carburante**, che erode direttamente le 24 h.

### 3.2 L'attenuante che riduce (non annulla) la penalità
La via serie **non** paga i 15–18% pieni, per due ragioni quantificabili:

1. **Il motore gira sempre al punto di minimo consumo.** Nella trasmissione diretta l'ICE è vincolato ai giri che l'elica/volo richiedono, spesso **fuori** dal suo punto ottimo di consumo specifico (BSFC). Un monocilindrico può avere BSFC che varia del **10–25%** sulla mappa. In serie l'ICE gira a **giri/carico fissi ottimali** → recupera ~**8–12%** rispetto a un diretto che lavora fuori-ottimo. 
2. **Riuso hardware** (vedi §3.4): non è efficienza di crociera ma di **sistema**.

**Penalità NETTA di consumo in crociera della via serie ≈ 5–12%** (non 15–18%). Su ~4 kg di carburante per 24 h, sono **~0,2–0,5 kg** in più, ovvero **~1–3 h** di endurance in meno a parità di carburante. **Non fatale, ma non trascurabile** quando l'intero valore del prodotto è "24 h".

### 3.3 Perché allora i benchmark di pura endurance usano il diretto
Gli UAV ad ala fissa che **massimizzano l'endurance senza VTOL** (Insitu ScanEagle ~22 kg con motore heavy-fuel spingente; AeroVironment **T-20** che fa **18+ h** con motore benzina a trasmissione diretta; AR5 ~20 h; la maggior parte dei classe 25 kg a lancio assistito) usano **motore in presa diretta sull'elica**: nessun VTOL a bordo → nessun bus elettrico da riusare → la doppia conversione sarebbe **peso e perdite gratis**. È la conferma pratica del §3.1: **senza VTOL, il diretto vince nettamente.**

### 3.4 Perché i VTOL ibridi usano invece la serie (il ribaltamento)
Nel momento in cui il velivolo **deve** fare hover, deve avere **spinta elettrica distribuita** (4+ rotori): un singolo albero meccanico **non può** sollevare in hover un quadplane. Quindi a bordo ci sono **già** bus DC, batteria, controller, motori. A quel punto:

- **Riuso hardware:** in serie lo **stesso** genset alimenta hover *e* crociera; l'hardware elettrico non è peso morto. In diretto (A1), invece, in crociera i 4 rotori+ESC+batteria sono **zavorra**, e in VTOL l'ICE è zavorra → **peggior utilizzo di massa**.
- **Motore al punto ottimo:** §3.2.
- **Modalità elettrica silenziosa** per tratti sensibili (ISR/marittimo) — impossibile col diretto sull'elica principale.
- **Ridondanza a batteria:** motore in avaria in crociera → si vola a batteria (riserva) per raggiungere il recupero o ritentare l'avviamento; spinta distribuita → tolleranza ai guasti.
- **Layout meccanico semplice:** nessun lungo albero/riduttore/giunto di tilt; il genset si monta isolato dalle vibrazioni.

**Bilancio:** la penalità di ~5–12% di consumo è **battuta** dai vantaggi di sistema **quando l'hover pesa nella missione**. Per questo — come documenta la §7 — **ogni VTOL ibrido _multirotore_ commerciale è serie**; nei VTOL _ad ala fissa_ a benzina, dove la crociera domina, prevale invece la crociera **diretta** (A1: JUMP 20, Foxtech Great Shark). La soglia è *quanto conta l'hover vs la crociera*.

### 3.5 La risposta netta al quesito
> **Se il velivolo di riferimento è l'ala fissa da endurance (il concept CAD, missione 24 h senza hover): motore termico IN ASSE all'elica (diretto) — è la scelta di massimo rendimento e minimo rischio, quella che protegge le 24 h.**
>
> **Se il velivolo deve integrare il VTOL (modulo installato): motore termico IN SERIE all'alternatore — perché il costo di crociera (~5–12%) è ripagato dal riuso del bus elettrico, dal motore al punto ottimo, dalla modalità silenziosa e dalla ridondanza.**
>
> **Il tilt-rotor (A3) elimina la scelta: impone la serie.** E paga la penalità serie su tutte le 24 h → è la peggiore proprio sul parametro che conta di più (endurance).

---

## 4. Dimensionamento first-order (potenza, energia, massa)

### 4.1 Potenza di crociera (dal Trade Study)
- P_elettrica crociera ≈ **350–500 W** (nominale ~400 W); avionica/payload ~45 W. → energia 24 h ≈ **8,5–12 kWh**.
- Potenza **d'albero** all'elica di crociera ≈ ~300–380 W (a valle di motore+ESC).

### 4.2 Potenza di VTOL (stima momentum theory)
Hover di 25 kg, 4 rotori. Con dischi piccoli (Ø ~0,40 m, area totale ~0,50 m²): P_ideale ≈ 245^1,5 / √(2·1,225·0,50) ≈ **3,5 kW**; con figura di merito ~0,6 e motore/ESC ~0,85 → **P_elettrica ≈ 6–7 kW**. Con dischi più grandi (Ø ~0,55 m, area ~0,95 m²) → **P_elettrica ≈ 4–5 kW**.

> **Il picco VTOL è ~10× la potenza di crociera.** Questo è il fatto dimensionante.

### 4.3 Peak-shaving: il buffer batteria disaccoppia genset e picco
Poiché il VTOL dura **poco** (transizione ~1–2 min per lato + eventuale hover breve) mentre la crociera dura **ore**, il genset può essere dimensionato sulla **media (crociera + ricarica)**, NON sul picco:

| Componente | Dimensionamento | Valore stimato |
|---|---|---|
| Genset (ICE+alternatore) | crociera ~0,4 kW + ricarica/margine | **~1,0–1,5 kW continui** |
| Picco VTOL | coperto **dalla batteria**, non dal genset | ~4–7 kW per ~2–4 min |
| Batteria buffer (energia VTOL) | ~5 kW × ~4 min + riserva | **~0,4–0,6 kWh utili** |
| Massa batteria buffer | a ~180 Wh/kg a livello pacco | **~2,2–3,3 kg** |

**Conseguenza:** grazie al buffer, **basta un piccolo motore termico** (classe 1–1,5 kW ≈ un monocilindrico 30–60 cc, o l'equivalente rotativo) invece di un motore capace del picco VTOL. Questo vale per **tutte** le architetture serie (A2, A3). In A1 (diretto), l'ICE è comunque piccolo (dimensionato sulla crociera) e il VTOL è **100% batteria**: batteria simile, ma il genset non ricarica un bus (serve un alternatore separato per ripristinare il buffer tra un ciclo VTOL e l'altro).

> **Ancoraggio commerciale:** i genset di classe pronti (Löweheiser HYBGEN 32 = 2,4 kW/3,7 kg; Pegasus GE70 = ~3,5 kW/3,5 kg; Foxtech NOVA-2400 = 2,4 kW/4,2 kg, ~830 g/kWh) sono **sovradimensionati** rispetto alla nostra crociera ad ala fissa (~0,4 kW) perché nascono per il mondo **multirotore** (dove la "crociera" è quasi-hover). Per un'**ala fissa** VTOL basterebbe la fascia bassa di quella potenza — il margine si usa per salita/ricarica rapida del buffer. Numeri reali del bus: un pacco 6S 16 Ah ~25C eroga ~10 kW in burst mentre il genset tiene ~2 kW → conferma il rapporto genset:picco ≈ 1:3–1:5.

### 4.4 Carburante e serbatoio
24 h ≈ **3,5–4,5 kg** di benzina (Trade Study). La penalità serie (§3.2) aggiunge **~0,2–0,5 kg**. Con la benzina a ~0,74 kg/L, il serbatoio è **~5–6 L** — gestibile nella cellula da 25 kg con payload 4–6 kg.

### 4.5 Bilancio di massa indicativo (25 kg, config A1 vs A2)
| Voce | A1 (diretto + VTOL batteria) | A2 (serie) |
|---|---|---|
| Motore termico | ~1,0–1,5 kg (monocilindrico ~30–60 cc) | idem |
| Alternatore/ISG | piccolo (~0,3–0,6 kg, solo ricarica) | grande (~1,0–1,8 kg, tutta la crociera) |
| Motore elettrico crociera | — (elica su ICE) | ~0,4–0,8 kg + ESC |
| 4 motori lift + ESC + booms | ~2,5–4 kg | ~2,5–4 kg |
| Batteria buffer | ~2,5–3,3 kg (tutta l'energia VTOL) | ~2,2–3,0 kg (buffer/peak-shaving) |
| Carburante 24 h | ~3,7–4,5 kg | ~4,0–5,0 kg (penalità serie) |
| **Nota** | miglior rendimento crociera; VTOL "a budget" | hardware riusato; +carburante, +modo silenzioso |

> I due bilanci sono **vicini**: A1 risparmia carburante ma spende in complessità di doppia catena; A2 spende carburante ma semplifica e aggiunge capacità. La scelta è **operativa**, non di sola massa (vedi §6).

---

## 5. Motori termici alternativi

Vincolo di partenza: **monocilindrico benzina**. È la scelta a **massimo TRL, minimo costo, miglior rapporto potenza/peso** — ma con **due debolezze** rilevanti per questo velivolo: **vibrazioni** (squilibrio del primo ordine di un singolo pistone) e **firma acustica/termica**, oltre a **BSFC** non ottimale e **TBO** breve. Le vibrazioni sono un problema **doppio**: (a) in A1 (diretto) si trasmettono a elica e cellula → **jitter del gimbal EO/IR** (degrada l'ISR!); (b) in A2/A3 (serie) sollecitano i cuscinetti dell'alternatore e la coppia di carica. Da qui l'interesse per alternative più regolari.

| Tecnologia | Potenza/peso | BSFC (consumo) | Vibrazioni | Multi-fuel / heavy-fuel | TRL/affidabilità | Adatto a… |
|---|---|---|---|---|---|---|
| **Monocilindrico 2T benzina** | ★★★★★ ottimo | ★★ scarso (ricco, olio in miscela) | ★ pessime (1° ordine) | ✗ benzina | ★★★★ maturo, TBO breve | Dimostratore economico |
| **Monocilindrico 4T benzina** | ★★★ | ★★★ migliore del 2T | ★★ | ✗/△ | ★★★★ | Endurance, più pulito |
| **Bicilindrico boxer/opposto** | ★★★ | ★★★ | ★★★★ bilanciato | ✗/△ | ★★★ | Riduce il jitter gimbal |
| **Rotativo / Wankel** | ★★★★★ eccellente, compatto | ★★ (rotary "beve") | ★★★★★ **regolarissimo** (no masse alterne) | ✓ spesso **heavy-fuel** | ★★★ (tenute apice) in miglioramento | **ISR/serie**: coppia liscia per l'alternatore, gimbal pulito |
| **Heavy-fuel 2T (HFE)** | ★★★ | ★★★ | ★★ | ✓✓ **JP-5/JP-8** | ★★★★ maturo (ScanEagle) | **Marittimo/difesa** (single-fuel, alta sicurezza a bordo nave) |
| **Micro-diesel (CI)** | ★★ pesante | ★★★★ ottimo | ★★ | ✓ gasolio/JP-8 | ★★ raro a 2–5 kW | Se conta il consumo e il peso è secondario |
| **Microturbina / turbogeneratore** | ★★★★★ | ★ pessimo a questa scala | ★★★★★ | ✓ multi-fuel | ★★★ | Solo serie ad **alta densità**, NON per 24 h (consuma troppo) |
| **Rotativo "X" tipo LiquidPiston** | ★★★★★ (promessa) | ★★★ (diesel/HF) | ★★★★ | ✓ heavy-fuel | ★★ emergente, TRL basso | Watch-item per la Fase C |

**Prodotti reali di riferimento (classe 2–10 kW):**

| Prodotto | Tipo | Potenza | Peso | P/W | BSFC (g/kWh) | Fuel | Impiego |
|---|---|---|---|---|---|---|---|
| Desert Aircraft **DA-50** | 1-cil 2T | 3,7 kW | 1,33 kg | **2,78 kW/kg** | ~500–600* | benzina | RC/UAV, riferimento P/W |
| **3W-55i** | 1-cil 2T | 4,0–4,4 kW | 1,79 kg | 2,46 kW/kg | ~450–550* | benzina | UAV |
| DA-70 (bicil. boxer) | 2-cil 2T | 5,6 kW | 1,9 kg | **2,95 kW/kg** | ~500* | benzina | upgrade "bilanciato" |
| **AIE 40ACS** (Wankel) | monorotore | 3,7 kW | **2,0 kg** | 1,85 kW/kg | n.p. | **multi-fuel/JP-8** | ★ **rotativo size-matched** |
| AIE **225CS** (Wankel) | monorotore | ~30 kW | 10 kg | ~3,0 kW/kg | ~340 (claim) | multi-fuel/JP-8 | core genset serie di fascia alta |
| **RCV DF35 / DF70** (4T valv. rot.) | 1-cil / boxer | 2,2 / 4,2 kW | 2,0 / 3,0 kg | 1,1 / 1,4 | **330 su JP-8** | JP-8/Jet-A | efficiente, heavy-fuel |
| **Cobra A99H** (HFE) | 3-cil 2T liq. | 6,5–7 kW | 3,65 kg | ~1,9 kW/kg | ~500 | **JP-8/JP-5** | ★ **HFE size-matched più liscio** |
| **Orbital N20** (HFE DI) | 1-cil DI | 2,95 kW | 4,97 kg | 0,59 kW/kg | n.p. | heavy-fuel | **field-proven su ScanEagle** |
| **LiquidPiston XTS-210** | rotativo "X" HEHC | ~20 kW | 19 kg | ~1,05 kW/kg | <350 (target) | heavy-fuel | emergente, **TRL basso** |

*BSFC dei monocilindrici a carburatore raramente pubblicato: banda tecnica accettata (EFI verso il basso).

**Letture chiave:**
- Per il **dimostratore**: **monocilindrico benzina** (2T economico ~2,5–2,9 kW/kg, o 4T più efficiente/pulito) — massimo TRL, minimo costo, rischio minimo. **Con isolamento antivibrante curato**, obbligatorio in A1 per non degradare il gimbal. TBO breve (~50–300 h) da mettere a budget.
- Per il **prodotto operativo ISR/marittimo**: due candidati forti a **sostituire** il monocilindrico:
  - **Rotativo/Wankel** (es. **AIE 40ACS**, 3,7 kW/2 kg, multi-fuel) — coppia **liscia** (nessuna massa alterna → bilanciamento quasi perfetto, ideale come genset serie e per un gimbal stabile), ottimo potenza/peso, spesso **heavy-fuel**. **Nota sul consumo (corregge un mito):** un Wankel EFI moderno (~340 g/kWh ai giri alti/costanti tipici dell'UAV) è **più efficiente del monocilindrico 2T a carburatore** (~450–600) che sostituisce — quindi il passaggio è **neutro-favorevole sul carburante**; è **peggiore** solo se confrontato con un buon 4T/diesel (~240–330). Vero prezzo: **usura tenute d'apice / consumo d'olio** (TBO) — mitigato dagli approcci a rotore raffreddato (AIE SPARCS).
  - **Heavy-fuel (HFE)** — quasi **obbligatorio** se il cliente è difesa/marittimo (requisito **shipborne** REQ-06): logistica a **carburante unico** (JP-8/JP-5) e **sicurezza** (alto punto di infiammabilità, critico a bordo nave). Size-matched: **Cobra A99H** (3-cil, ~1,9 kW/kg su JP-8, più liscio di un mono) o **Orbital N20** (field-proven su ScanEagle, ma P/W basso). Prezzo: potenza/peso e costo peggiori della benzina.
- **Microturbina**: seducente per densità e regolarità, ma il **consumo specifico** a questa scala **uccide** l'endurance → esclusa per la missione 24 h.

> **Raccomandazione motore:** benzina monocilindrica per il **dimostratore**; pianificare l'upgrade a **rotativo (regolarità + heavy-fuel)** o **HFE** per la versione **navale/difesa**. In ogni caso, **isolamento antivibrante** e — se A1 — **disaccoppiamento del gimbal** dalla cellula sono voci di progetto obbligate.

---

## 6. Matrice di trade-off delle configurazioni

Criteri e pesi (somma 100), tarati sui driver del progetto (endurance è re; VTOL è modulo; ISR/appeal contano):
P1 **Endurance/consumo crociera 22** · P2 Affidabilità/ridondanza 16 · P3 Semplicità meccanica/rischio 14 · P4 Capacità VTOL/hover 10 · P5 Modalità silenziosa/firma 10 · P6 Massa/efficienza di sistema 10 · P7 Maturità/TRL 10 · P8 Stabilità sensori (gimbal) 8. Score 1–5.

| Config | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | **TOT/100** |
|---|---|---|---|---|---|---|---|---|---|
| **A2 — 5 mot., elettrico su alternatore (serie)** | 4 | **5** | 4 | 4 | **5** | 4 | 4 | **5** | **86,8** |
| A1b — 5 mot., parallelo integrato (ISG) | **5** | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 73,2 |
| **A1 — 5 mot., elica in asse ICE (diretto)** | **5** | 3 | 3 | 3 | 2 | 3 | 4 | 3 | **68,8** |
| **A3 — 4 mot. tilt-rotor (serie)** | 3 | 3 | **2** | **5** | 4 | **5** | 2 | 4 | **66,8** |

*(Calcolo esplicito, punteggio normalizzato su 1–5: es. A2 = 22·(4/5)+16·(5/5)+14·(4/5)+10·(4/5)+10·(5/5)+10·(4/5)+10·(4/5)+8·(5/5) = 86,8. Punteggi indicativi, da validare col gruppo.)*

**Letture:**
- **A2 (serie, 5 motori) domina la matrice bilanciata (86,8):** vince su affidabilità/ridondanza, modo silenzioso, stabilità gimbal, semplicità meccanica e massa di sistema, e **cede solo 1 punto sul consumo di crociera** (P1=4 vs 5). **È l'architettura più versatile e la scelta "sicura"** — coerente col fatto che la serie domina l'intero mercato ibrido-UAV. La matrice **premia la versatilità operativa** (hover + silenzioso + ridondanza pesano insieme ~36/100).
- **⚠️ Ma la matrice bilanciata non cattura un fatto esistenziale:** per HALE l'endurance non è "un criterio fra tanti", è **il** proposito del prodotto. Il ~5–12% di carburante in più della serie può essere la differenza tra "24 h" e "21–23 h" — e quel divario **erode l'unica cosa che rende vendibile il velivolo**. Per questo la **revealed-preference del mercato** dei VTOL ad ala fissa a benzina (JUMP 20, Great Shark) è **A1**, non A2: chi vive di endurance **rifiuta** la doppia conversione. La matrice, con P1 a 22, sotto-pesa quanto l'endurance sia *dominante* in questa nicchia.
- **A1 (diretto) è lo specialista dell'endurance (68,8 nella matrice bilanciata, ma 1° se si pesa l'endurance come esistenziale):** imbattibile su P1 (consumo crociera) e alto TRL (è il pattern fielded di JUMP 20), a scapito di ridondanza, modo silenzioso e complessità della doppia catena. **A1b (parallelo ISG, 73,2)** lo migliora con ricarica e un minimo di ridondanza, a costo di complessità sull'albero (delicata con un monocilindrico).
- **A3 (tilt-rotor) ultimo (66,8):** miglior VTOL/hover e massa di sistema, ma **penalizzato su endurance, rischio meccanico (tilt) e TRL** (nessun tilt-rotor ibrido commerciale a 25 kg, §7.5). Buono solo se la missione fosse hover-intensiva; **subottimo per le 24 h ISR**.
- **Sensibilità (onesta):** la matrice bilanciata favorisce **A2 in modo robusto** (resta 1° anche pesando l'endurance a 30) — perché A2 perde poco su P1 e vince quasi tutto il resto. **A1 vince solo quando il criterio decisionale è "massima endurance a parità di costo/TRL, con VTOL leggero/occasionale"**, cioè quando si esce dalla logica multi-criterio e si ottimizza la sola metrica di prodotto. → **La scelta A1 vs A2 non è un numero di matrice: è una decisione di posizionamento** (endurance-puro vs piattaforma versatile).

---

## 7. Panorama commerciale — chi lo sta già facendo e come

*(Dati da ricerca dedicata 2023–2026. Le specifiche vendor sono spesso "di picco/record": dove noto, si distingue continuo vs picco e tipico vs record. Prezzi quasi mai pubblici.)*

### 7.1 La regola strutturale che decide l'architettura
Il censimento dei prodotti reali conferma la logica del §2–§3:

- **VTOL multirotore ibrido → 100% architettura SERIE.** Nessun ibrido multirotore commerciale è a trasmissione diretta: N rotori di sollevamento controllati in modo indipendente **non possono** condividere un solo albero (il controllo d'assetto avviene variando i giri dei singoli rotori). → il termico può solo generare. *(Fonte: censimento prodotti + MDPI Aerospace 9(2):63; MDPI Drones 8(11):634.)*
- **VTOL ad ala fissa a benzina → il pattern dominante è A1 (crociera a trasmissione DIRETTA + lift elettrici a batteria).** È la scelta di **AeroVironment JUMP 20**, **Foxtech Great Shark**, **CUAV Raefly** (vedi §7.3). La **serie piena** (A2) su ala fissa esiste soprattutto in R&D/compound-wing e nei velivoli-genset dedicati.

> **Conseguenza per HALE:** per un **VTOL ad ala fissa orientato all'endurance**, il mercato *converge su A1* (diretto per la crociera, elettrico per l'hover). La serie piena (A2) domina il mondo **multirotore/heavy-lift**, dove l'hover è il cuore della missione. Questo **rafforza** la nostra raccomandazione §0/§8.

### 7.2 I gruppi di generazione (genset) serie commerciali — la classe 2–6 kW
Sono i "mattoni" pronti per l'architettura serie (A2/A3) o per la ricarica-buffer in A1. Tutti a **benzina**, 2 tempi, con batteria buffer sul bus:

| Genset | Potenza continua | Motore | Peso | ~P/W | Bus | Note per la classe 25 kg |
|---|---|---|---|---|---|---|
| **Pegasus GE70** | ~3,5 kW (4,0 picco) | 70 cc **bicilindrico** 2T | 3,5 kg | ~1140 W/kg | 50 V | ✅ **ideale**: "UAV al limite dei 25 kg alimentati con facilità" |
| **Pegasus GE35** | ~1,75 kW (2,0 picco) | 35 cc **monocilindrico** 2T | 2,6 kg | ~770 W/kg | — | Payload leggeri |
| **Pegasus GD70** | 4,5 kW **d'albero** + ~1 kW aux | 70 cc 2T | n.p. | — | — | ⚠️ È la variante **a trasmissione diretta** (per ala fissa), non un genset — dimostra che anche i fornitori serie offrono il "diretto" |
| **Löweheiser HYBGEN 32** | 2,4 kW | 32 cc 2T + EFI | 3,7 kg | ~650 W/kg | 48 V | ✅ **integratore-friendly**: telemetria in ArduPilot/Mission Planner; EFI programmabile anche per **Wankel** |
| **Quaternium** (range-ext. HYBRiX) | 2,6 kW | 32 cc Zenoah 2T EFI | 3,5 kg | ~740 W/kg | — | ✅ nel drone HYBRiX 2.1 (MTOM 25 kg, record 8 h 10 min) |
| **Harris H2400 / H5000** | 2,4 / 4,3 kW | 2T EFI | 4,2 / 10 kg | ~570 / 430 W/kg | — | ✅ / heavy-lift (Carrier H6) |
| **AAC HAMR** (genset) | 2,0 kW | 35 cc **monocilindrico** EFI | integrato | — | — | ✅ multirotore serie a 6 motori, difesa (AFWERX) |
| **Foxtech Halo-2000 / 6000** | 2 / 6 kW | 2T mono / bicil. | — | — | 58 V (6000) | ✅ / sovradimensionato |

**Letture:** il **punto dolce** per un VTOL da 25 kg è un **genset benzina 2,4–4 kW, 3,5–5 kg, ~650–1140 W/kg, batteria come buffer di picco**. Löweheiser e Pegasus GE70 sono i riferimenti diretti; Löweheiser è notevole perché **apre l'ecosistema** (ArduPilot) e la sua EFI supporta il **Wankel** (ponte verso il §5).

### 7.3 I VTOL ad ala fissa a benzina — il pattern A1 "in carne e ossa"
Questi prodotti **sono** la nostra configurazione A1 (crociera termica diretta + 4 lift elettrici a batteria):

- **AeroVironment JUMP 20 — il benchmark esatto della configurazione A1.** Quadplane: **2 booms alari con 2 rotori elettrici ciascuno = 4 lift elettrici (solo VTOL)** + **1 elica traente a benzina al muso (crociera), a trasmissione diretta** (motore ~190 cc 4T EFI, derivato Honda, ~15 hp; variante heavy-fuel provata in volo nel 2024). Endurance **10–13 h**. → **è letteralmente A1 in scala ~95 kg.**
  - **Il dato d'oro (quantifica la penalità VTOL):** il gemello **T-20**, *stessa cellula e stesso motore*, ma **a catapulta senza rotori di lift**, fa **18+ h**. Il salto **18 h → 10–13 h** è la **misura reale della penalità del kit VTOL a 4 rotori** su un'ala fissa a benzina — coerente col −36% dell'AR3 EVO già citato nel Trade Study. *(Conferma: il VTOL va tenuto **modulare/rimovibile**.)*
- **Foxtech Great Shark Max 380 Hybrid** — VTOL ala fissa da **30 kg RTF**: **motore 120 cc bicilindrico 2T che aziona meccanicamente un'elica spingente da 26″ per la crociera** + **motori elettrici di lift separati a batteria**. Endurance 2 h con 15 kg / 4 h con 10 kg. → **A1 commerciale, a basso costo.**
- **CUAV Raefly VT370** — VTOL tandem-wing ibrido gasolina-elettrico, di nuovo **lift+cruise (quadplane)**, non tilt-rotor.

### 7.4 I VTOL a singolo gruppo motopropulsore (l'anti-tesi: zero rotori morti)
Filosofia opposta al quadplane: **un solo propulsore fa hover e crociera**, nessun rotore morto in crociera, nessun attuatore di tilt. Rilevanti perché sono i "cugini" più vicini a un concept a **singolo genset**:

- **Shield AI / Martin V-BAT** — **tail-sitter a ventola intubata singola** (2T EFI: 288 cc su V-BAT 128; ultima serie **heavy-fuel**): la **stessa** ventola fa hover e crociera, l'assetto in hover è dato da **alette deviatrici** nel getto. Endurance **11+ h** (13+ h heavy-fuel). *Nessuna ridondanza di propulsione (motore singolo).*
- **Aerovel/Airbus Flexrotor** — **tail-sitter a motore singolo** (28 cc 2T, ora anche HFE): **un'unica elica a passo variabile** (collettivo+ciclico in hover) fa tutto; 2 microrotori elettrici alle estremità solo per l'assetto in hover. **~25 kg, 30+ h.** *(È già benchmark nel Trade Study.)* → dimostra che a 25 kg si può avere endurance estrema **senza** carrozzeria VTOL a 4 rotori, al prezzo di un propulsore "di compromesso" e zero ridondanza.

### 7.5 Il tilt-rotor a 25 kg (config A3): quasi assente in versione ibrida
Dato importante per il nostro trade:
- **Nessun tilt-rotor ibrido commerciale nella classe ~25 kg.** I tilt-rotor di questa classe sono **tutti elettrici** (es. **Quantum Systems Vector**, tri-tilt-rotor ~8,5 kg, ~2 h, batteria); gli ibridi di questa classe sono **tutti lift+cruise (quadplane)**. Il tilt-rotor **ibrido** esiste **solo a livello accademico** (es. PMC8468980, "Hybrid VTOL Tilt-Rotor for increased endurance").
- **Perché:** un genset "vuole" alimentare una crociera **stazionaria** + un banco di lift elettrici **separato** → mappa naturalmente su lift+cruise, **non** su rotori che devono oscillare tra due punti di funzionamento. Più i noti problemi del tilt: **elica di compromesso**, **attuatore di tilt = guasto a punto singolo** in transizione, controllo non-lineare nel regime a tilt parziale.

> **Conseguenza:** A3 (4 tilt-rotor ibridi) sarebbe **territorio inesplorato commercialmente** a 25 kg → TRL basso, rischio alto. Conferma la sua ultima posizione in matrice (§6) per una piattaforma il cui KPI è l'endurance.

### 7.6 Alternative alla "sorgente elettrica": la fuel cell a idrogeno
Al posto dell'ICE-genset, una **cella a combustibile PEM** può fare da sorgente del bus serie:
- **Energia specifica di sistema ~800–1000 Wh/kg** (incl. serbatoio H₂ compresso) vs ~250 Wh/kg del Li-Po → 4–5× l'endurance a batteria. Esempi: **Intelligent Energy** (modulo 650 W, volo dimostrativo **12 h 7 min**), **Doosan DS30** (~2 h), **H3 Dynamics** (HYWINGS ~10 h claim). TRL di prodotto alto (7–9).
- **Ma:** transitori/picco deboli → **serve comunque una batteria buffer per il VTOL**; a 25 kg il **volume del serbatoio pressurizzato**, la massa di *balance-of-plant*, il costo e la **logistica di rifornimento H₂** la tengono di nicchia rispetto a un genset benzina/heavy-fuel (il cui *carburante* porta ~12.000 Wh/kg chimici e si rabbocca in secondi). → **Watch-item strategico** (narrativa "green" + dual-use), non baseline per il dimostratore.

### 7.7 Sintesi: la mappa commerciale → le nostre configurazioni

| Nostra config | Chi la fa già (benchmark reale) | Verdetto di maturità |
|---|---|---|
| **A1** (5 mot., crociera termica diretta + lift elettrici) | **AeroVironment JUMP 20**, **Foxtech Great Shark 380**, CUAV Raefly | ✅ **Pattern dominante e fielded** per VTOL ala fissa a benzina |
| **A2** (5 mot., serie pieno) | Pegasus G15, compound-wing 25 kg (MDPI 2024), genset Löweheiser/Quaternium/Harris/AAC | ✅ Maturo, dominante nel mondo **multirotore/heavy-lift** |
| **A3** (4 tilt-rotor ibridi) | **Nessuno a 25 kg** (tilt-rotor solo elettrici; ibrido solo accademico) | ⚠️ **Non commercializzato** in classe → TRL basso |
| Singolo propulsore (fuori dai 3, ma istruttivo) | V-BAT, Flexrotor | ✅ Alternativa "zero rotori morti" (compromesso propulsore, zero ridondanza) |

**Motori — chi usa cosa:** benzina 2T mono/bi (tutti i genset sopra; JUMP 20 usa un **4T** al muso); **heavy-fuel** dove il cliente è difesa/navale (**Orbital N20** su ScanEagle, **Cobra A99H**, NWUAV, V-BAT/Flexrotor heavy-fuel); **Wankel** per regolarità/multi-fuel (**AIE 40ACS** 3,7 kW/2 kg size-matched; Rotron/Austro su UAV più grandi, es. Camcopter S-100); **microturbina** solo su UAV ≥55 kg (UAV Turbines) — esclusa a 25 kg per consumo.

---

## 8. Raccomandazione

**Configurazione raccomandata, condizionata al profilo di missione dominante:**

1. **Se domina l'endurance ISR ad ala fissa (il cuore HALE, coerente col CAD):**
   → **A1/A1b — elica principale in asse al motore termico (trasmissione diretta)**, con **ISG/alternatore** per ricarica-buffer, avionica e solar-assist; **modulo VTOL a 4 rotori elettrici rimovibile** a batteria per i soli decolli confinati. Massimo rendimento di crociera, minimo rischio, minima modifica al concept esistente.

2. **Se serve hover-loiter frequente, decollo verticale operativo di routine, o modalità elettrica silenziosa obbligatoria (ISR sensibile/marittimo):**
   → **A2 — ibrido-serie a 5 motori** (4 lift + 1 crociera elettrici, ICE→alternatore→bus+buffer). Si accetta ~5–12% di consumo in più in cambio di ridondanza, silenzio, stabilità gimbal e semplicità meccanica. **È l'architettura del 100% dei VTOL ibridi commerciali di classe.**

3. **Tilt-rotor A3:** tenere come opzione **solo** se il profilo diventasse VTOL-intensivo; non è la scelta per una piattaforma il cui KPI è l'endurance.

**Elementi trasversali:**
- **Buffer batteria per peak-shaving** → genset piccolo (~1–1,5 kW) invece che dimensionato sul picco VTOL (~5 kW).
- **Motore:** benzina monocilindrica per il **dimostratore**; **rotativo o heavy-fuel** in vista per la versione **navale/difesa** (shipborne, single-fuel, coppia liscia).
- **Isolamento antivibrante** del gruppo termico (critico in A1 per il gimbal; importante in A2/A3 per l'alternatore).
- **Coerenza col Trade Study:** ala fissa = motore dell'endurance; VTOL = modulo. Questo documento specifica **come** realizzare la parte "ibrido-elettrico" lì raccomandata.

---

## 9. Rischi, lacune e prossimi passi

| Rischio / lacuna | Impatto | Azione |
|---|---|---|
| Rendimenti reali della catena serie (qui banda di letteratura) | Alto (tocca le 24 h) | Banco genset: misurare η alternatore→bus→motore sul nostro punto |
| BSFC reale del motore candidato sul punto ottimo | Alto | Prova al banco del monocilindrico/rotativo scelto |
| Vibrazioni monocilindrico → jitter gimbal (A1) e alternatore (A2) | Medio-alto | Caratterizzazione vibrazioni + montaggi isolati; valutare bicilindrico/rotativo |
| Potenza VTOL reale (disco, FoM) | Medio | Trade rotori/dischi + prove di hover |
| Transizione tilt-rotor (se A3) | Alto | Simulazione + prove; probabile esclusione per l'endurance |
| Heavy-fuel per requisito shipborne | Medio | Trade motore HFE se il cliente è marittimo/difesa |
| Massa e integrazione ISG (A1b) | Medio | Trade parallelo dedicato in Fase C |

**Prossimi passi:** (1) fissare il **profilo di missione dominante** (endurance-pura vs VTOL-operativo) → seleziona A1 vs A2; (2) **banco genset/motore** per i rendimenti e il BSFC reali; (3) **trade rotori VTOL** (numero, diametro, disk loading); (4) decisione **benzina vs rotativo vs HFE** legata al cliente (civile vs navale/difesa).

---

## 10. Fonti

> ⚠️ **Nota di qualità del dato:** le specifiche vendor sono spesso "di picco/record", non tipiche; alcuni siti (MDPI, NASA NTRS, Wikipedia, aieuk, rotronaero, liquidpiston e vari vendor) hanno bloccato il fetch automatico → i numeri sono stati raccolti da estratti di ricerca e **corroborati su più fonti indipendenti**. I numeri più critici (BSFC AIE 225CS, peso/SFC LiquidPiston, endurance record) vanno **confermati su datasheet primario / RFQ** prima dello Studio.

**Architettura serie/parallelo/diretto e rendimenti (teoria):**
- MDPI *Aerospace* 12(10):895 — Review of Hybrid-Electric Propulsion (rendimenti componenti, perdite AC-DC-AC 10–20%): https://www.mdpi.com/2226-4310/12/10/895
- MDPI *Drones* 8(11):634 — Improved Series Hybrid per compound-wing VTOL **25 kg** (60 cc ICE, PMSG, 4 lift): https://www.mdpi.com/2504-446X/8/11/634
- MDPI *Aerospace* 9(2):63 — serie vs parallelo, propulsione distribuita: https://www.mdpi.com/2226-4310/9/2/63
- MDPI *Energies* 14(22):7672 — Series Architecture on HEV (penalità doppia conversione): https://www.mdpi.com/1996-1073/14/22/7672
- Springer — Review Hybrid Propelled Aircraft (parallelo = più efficiente/leggero): https://link.springer.com/article/10.1007/s42496-023-00173-6
- NASA EAP — Aircraft Configurations (serie/parallelo/turboelettrico): https://www.nasa.gov/eap-aircraft-concepts/aircraft-configurations/
- NASA NTRS — Distributed Electric Propulsion (disaccoppiamento meccanico): https://ntrs.nasa.gov/api/citations/20180004729/downloads/20180004729.pdf
- ScienceDirect — Series Hybrid Configuration (conversioni multiple, η complessivo basso): https://www.sciencedirect.com/topics/engineering/series-hybrid-configuration
- RoyMech — Gear Efficiency (ingranaggio 98–99%/stadio): https://www.roymech.co.uk/Useful_Tables/Drive/Gear_Efficiency.html
- Wikipedia — Distributed propulsion: https://en.wikipedia.org/wiki/Distributed_propulsion

**Gruppi di generazione (genset) e VTOL ibridi commerciali:**
- Pegasus Aeronautics GE70/GE35/GD70/G15: https://www.pegasusaero.ca/ge70 · https://www.pegasusaero.ca/ge35 · https://www.pegasusaero.ca/gd70 · https://www.pegasusaero.ca/g15-sentinel
- Löweheiser HYBGEN 32 (2,4 kW/48 V/3,7 kg, ArduPilot, EFI Wankel-capable): https://www.loweheiser.com/hybrid-drone-generators/ · https://www.loweheiser.com/drone-efi-systems/
- Skyfront Perimeter 8 (serie, record 13 h): https://skyfront.com/perimeter-8 · https://skyfront.com/learn/hybrid-drone
- Quaternium HYBRiX 2.1 (25 kg, record 8 h 10 min): https://www.gpsworld.com/hybrix-multirotor-uav-flies-non-stop-for-8-hours/ · https://newatlas.com/drones/hybrix-hybrid-drone-10-hours/
- Harris Aerial Carrier H6 Hybrid (H2400/H5000): https://harrisaerial.com/carrier-drones/carrier-h6-hybrid/
- AAC HAMR (serie, 35 cc, difesa AFWERX): https://advancedaircraftcompany.com/hamr/
- Foxtech Great Shark Max 380 Hybrid (**A1 diretto**, 120 cc bicil.): https://www.foxtechfpv.com/foxtech-great-shark-max-hybrid-380-vtol.html · NOVA-2400 (2,4 kW/4,2 kg/830 g/kWh): https://www.foxtechfpv.com/foxtech-nova-2400-generator.html · Halo-6000: https://www.foxtechfpv.com/foxtech-halo-6000-efi-generator-for-hybrid-drone.html
- UAVHE PT1-124 (2T + booster-generatore 11 kW): https://www.unmannedsystemstechnology.com/company/uavhe/pt1-124/
- Hirth — generatori UAV integrati (PMSG su albero): https://hirthengines.com/high-performance-uav-generators/

**VTOL ad ala fissa (pattern lift+cruise, tilt-rotor, tail-sitter):**
- AeroVironment **JUMP 20** (datasheet primario, "front puller engine, gasoline"): https://www.avinc.com/uas/jump-20 · Technical Brief PDF: https://ezstack-source-1es5yaoqgtfar.s3.amazonaws.com/venue_668648_hall_item_675223/6JIeUe7IRkiABZOH4heE_JUMP20%20data%20sheet.pdf
- AeroVironment/Arcturus **T-20** (18+ h, no VTOL): https://www.designation-systems.net/dusrm/app4/jump-20.html · https://arcturus-uav.com/product/t-20
- JUMP 20 heavy-fuel flight test 2024: https://defensemirror.com/news/37096
- Insitu ScanEagle / RQ-21A Integrator (heavy-fuel, catapulta+SkyHook): https://www.insitu.com/products/scaneagle · https://www.uncrewed-systems.com/insitus-scaneagle-integrator/
- Aerovel/Airbus **Flexrotor** (tail-sitter, motore singolo, ~25 kg, 30+ h): https://www.airbus.com/en/products-services/defence/uas/flexrotor · https://www.airforce-technology.com/projects/flexrotor-small-tactical-unmanned-aerial-system/
- Quantum Systems **Vector** (tri-tilt-rotor, **solo elettrico**): https://quantum-systems.com/vector-ai/
- Shield AI / Martin **V-BAT** (tail-sitter ventola intubata, motore singolo, 11+ h): https://shield.ai/v-bat/ · https://www.airforce-technology.com/projects/v-bat-128/
- DeltaQuad Evo / Censys Sentaero (quadplane elettrici 4+1): https://www.deltaquad.com/products/evo · https://censystech.com/home-censys/sentaero-6-oth-bvlos/
- CUAV Raefly VT370 (ibrido tandem-wing lift+cruise): https://store.cuav.net/shop/cuav-raefly-vt370-vtol-uav/
- Misra et al. — Review VTOL Tilt-Rotor & Tilt-Wing UAVs (Wiley 2022): https://onlinelibrary.wiley.com/doi/10.1155/2022/1803638
- Impact of lift-propeller drag on lift+cruise eVTOL (ScienceDirect): https://www.sciencedirect.com/science/article/abs/pii/S1270963820311111
- Hybrid VTOL Tilt-Rotor for increased endurance (PMC8468980, solo accademico): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8468980/

**Motori termici alternativi:**
- Desert Aircraft DA-50/DA-70: https://www.desertaircraft.com/products/da-50r · https://www.desertaircraft.com/products/da-70
- 3W-55Xi / 28i: https://3w-modellmotoren.de/produkt/3w-55xi/?lang=en
- AIE 40ACS (Wankel 3,7 kW/2 kg): https://www.aieuk.com/40acs-5-bhp-wankel-rotary-engine/ · https://newatlas.com/aircraft/aie-40cc-wankel-engine/ · AIE 225CS: https://www.aieuk.com/225cs-40bhp-wankel-rotary-engine/
- Vantaggi Wankel su UAV (vibrazioni): https://www.aieuk.com/blog/harnessing-the-advantages-of-wankel-rotary-engines-in-uncrewed-aerial-vehicles-uavs/
- Rotron RT300/RT600 · Austro AE50R (Camcopter S-100): https://rotronaero.com/products/rt600-xe · https://en.wikipedia.org/wiki/Austro_Engine_AE50R
- RCV DF35/DF70 (4T valvola rotante, 330 g/kWh JP-8): https://www.nwuav.com/media/rcv-engines/df35-df70-air-cooled-engines.pdf
- Cobra Aero A99H (HFE 3-cil): https://www.cobra-aero.com/a99h · https://www.uncrewed-systems.com/cobra-aero-a99h/
- Orbital N20 (HFE DI, ScanEagle) · Currawong Corvid-50: https://www.currawongeng.com/corvid-29/
- Sky Power SP-110/SP-210 HF · NWUAV NW-44 (JP-8): https://skypower.online/engines/ · https://www.nwuav.com/products-nw-44-uav-hfe.html
- LiquidPiston XTS-210 (rotativo "X" heavy-fuel, emergente): https://liquidpiston.com/xts-210-engine-liquidpiston · https://www.globenewswire.com/news-release/2023/04/04/2640767/0/en/LiquidPiston-Introduces-XTS-210...
- UAV Turbines Monarch / PBS TJ (microturbina, SFC alto): https://uavturbines.com/ · https://www.pbsaerospace.com/aerospace-products/engines/turbojet-engines/tj-100-turbojet-engine
- Microturbina — confronto SFC vs pistone: https://en.wikipedia.org/wiki/Microturbine

**Fuel cell a idrogeno (alternativa sorgente serie):**
- Intelligent Energy (modulo 650 W, 12 h 7 min): https://www.intelligent-energy.com/our-industries/uav/
- Doosan Mobility DS30 · H3 Dynamics: https://www.doosanmobility.com/en/technology/tech_01/ · https://www.h3dynamics.com/h2solutionsforuav
- ScienceDirect — endurance drone con fuel-cell ibride: https://www.sciencedirect.com/science/article/pii/S1364032125008342

---

*Analisi first-order stage-appropriate per la fattibilità. Rendimenti e potenze sono bande di letteratura/parametriche, da raffinare con banco genset, misura BSFC e trade rotori. La matrice P1–P8 è indicativa: pesi e score da validare col gruppo in funzione del profilo di missione reale.*
