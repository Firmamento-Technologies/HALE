# 27 — Report di Fattibilità: T-SORV, piattaforma ad alta endurance per sorveglianza (terrestre + marittima)

> **Cosa è.** Report di fattibilità richiesto dall'utente per una nuova piattaforma, derivata dalle analisi HALE del progetto ma **non stratosferica**: UAV fixed-wing ad alta endurance per sorveglianza delle Aree Interne liguri, con una sezione dedicata alla variante di sorveglianza marittima. Sintetizza 7 documenti sezionali prodotti da esperti dedicati (`25a-f`, `26a`), ciascuno leggibile per il dettaglio tecnico completo.
> **Confidenza aggregata:** MEDIA-ALTA su fisica/regolatorio (ancorati a benchmark reali e testo normativo), MEDIA-BASSA su economia (nessun prezzo/contratto reale).

---

## 0. Chiarimento terminologico obbligatorio (leggere prima di tutto)

L'utente ha richiesto un'"alternativa in classe C3" con apertura alare **>10 m**, endurance **10-20h** e necessità di **certificazione ENAC**. Questi tre vincoli sono **incompatibili con la classe C3 EASA** (Reg. UE 2019/945: MTOM ≤25 kg, dimensione ≤3 m, abilita solo la categoria Open/A3 — nessuna "certificazione" nel senso pieno del termine). C3 è un'**etichetta di prodotto**, non una categoria operativa; la confusione è comune ma consequenziale.

Il report interpreta quindi la richiesta come una piattaforma nella fascia **T2/T3 "MID/MALE"** già definita nella tassonomia del progetto (`10-fasce-engineering.md`), che chiamiamo **T-SORV** (T2/T3 Sorveglianza), categoria regolatoria **Specific o Certified**. Se l'intento era diverso, va corretto — ma con i vincoli dati (apertura, endurance, certificazione) non esiste altra lettura tecnicamente coerente.

---

## 1. Il velivolo — punto di progetto consolidato

| Parametro | Valore | Fonte |
|---|---|---|
| Configurazione | Monoplano fixed-wing, **NON-VTOL**, high-AR, T-tail | `25a`, `14` |
| MTOM | **150-180 kg** (raccomandato ≤150 kg, vedi §5 spartiacque regolatorio) | `25b`, `25f` |
| Apertura (b) | **14 m** | `25b` |
| AR | 17 | `25b` |
| Superficie alare (S) | 11,5 m² | `25b` |
| L/D crociera | **~20-21** (banda 18-24) | `25b` |
| Quota operativa | **3.000 m AMSL** (banda 2.500-3.500 m) | `25a` |
| Endurance | **20h raggiungibile oggi** con ibrido ICE+buffer elettrico | `25c` |
| Lancio | Corsa su ruote (ROG) su sito di crinale/altopiano; catapulta come fallback | `25a`, `25b` |
| Materiali | CFRP standard (coerente coi verdetti già consolidati: lino solo secondarie) | `25b` |
| Payload | 15-30 kg, EO/IR modulare intercambiabile terra/mare | `25e`, `26a` |

---

## 2. Perché NON-VTOL — la decisione che ribalta il verdetto C3

Il trade study `14` (fascia C3, consegna punto-punto a Pentema) aveva **squalificato** la baseline non-VTOL: catapulta e recupero non stavano nello spazio confinato del borgo, perché il **sito di atterraggio coincideva con la destinazione della missione**.

Per T-SORV questa premessa **cade**: è una missione di **pattuglia ad area vasta**, non punto-punto. Il sito di lancio è scelto dove lo spazio esiste (crinale, altopiano, campo agricolo), **disaccoppiato** dall'area sorvegliata — Pentema si sorvola, non si lancia da lì. Tolto il gate di ammissibilità che l'aveva esclusa, la baseline non-VTOL **torna a vincere**: era già 1ª nella matrice pesata pura di `14` §7.1 (7,65/10, il punteggio più alto tra tutte le 7 architetture testate). Il VTOL è inoltre incoerente qui: penalità di massa 15-22% su un'apertura >10 m ed endurance 20h la rende un handicap, non un abilitante.

**Conseguenza pratica:** niente rotori di sostentamento, niente meccanismi di tilt — la semplicità meccanica e l'efficienza di crociera che il caso C3 non poteva permettersi qui sono la scelta giusta.

---

## 3. Quota operativa — la morfologia ligure comanda il numero

Crinali reali dell'Appennino ligure interno (Torriglia/Pentema, Val d'Aveto, Alta Val Trebbia), verificati: **Monte Antola 1.597 m**, **Monte Aiona 1.701 m**, **Monte Penna 1.735 m**, **Monte Maggiorasca 1.804 m** (vetta più alta della zona).

**Quota raccomandata: 3.000 m AMSL** (banda operativa 2.500-3.500 m), con margine ~1.200 m sopra la vetta più alta per garantire linea di vista libera su un'area di pattuglia multi-versante. Resta **profondamente in Classe G** (tetto FL195 ≈ 5.944 m, mai avvicinato — non è un vincolo stringente) e produce **GSD sub-metrico** sui sensori EO/IR.

**Vantaggio fisico non banale rispetto all'HALE**: a 3.000 m il sensore termico è **~10× più fine** che a 20 km (a quella quota era diffraction-limited a 2,4 m; qui è resolution-limited a 0,24-2,4 m secondo la scena). La bassa quota, oltre a risolvere l'energy balance (vedi §4), **migliora anche la missione**.

---

## 4. Endurance ed energia — l'opposto esatto del caso HALE

Punto centrale del report, verificato con lo stesso rigore usato per l'energy balance HALE (`ENERGY-BALANCE-HALE-44N-REPORT.md`), ma con esito diametralmente diverso:

| | HALE stratosferico (20 km, perennial) | T-SORV (3.000 m, missione 10-20h) |
|---|---|---|
| Propulsione praticabile | **Solo solare+batteria** (nessuna alternativa) | **Ibrido ICE+buffer elettrico** (oggi, TRL 8-9) |
| Ruolo del solare | **Abilitante/showstopper** (margine inverno -50,1%, DEFICIT) | **Marginale**, +0,3h (worst) a +14h (best), mai determinante |
| Massa energia per il target | Batteria LiS 20-35 kg su 100 kg MTOM, comunque insufficiente in inverno | **~13 kg di heavy-fuel** su 150-180 kg MTOM |
| Elettrico puro possibile? | No (perennial impossibile) | **No** per 20h (richiederebbe 103-144 kg di sola batteria, 69-96% del MTOM) |
| Verdetto | HOLD, seasonal-only fallback | **20h raggiungibili oggi**, confermato da benchmark reali |

**Benchmark di conferma**: Tekever AR3/AR5 (16-20h) e Hermes 450 (17-20h) — piattaforme reali della stessa classe già operative in Europa (EMSA), non stime.

**Raccomandazione**: ibrido serie ICE + buffer elettrico. Il carburante fa le 20h; il buffer batteria abilita una **modalità loiter silenziosa a comando** (30-60 min, motore spento) — il vero valore operativo per una sorveglianza discreta. **Il solare va escluso dalla baseline** e tenuto come kit opzionale R&D solo se emerge un requisito di silenzio esteso — includerlo comporta anche penalità aerodinamiche/di massa non trascurabili (vedi §6).

---

## 5. Regolatorio — lo spartiacque dei 150 kg e le due catene di autorità

**Terra**: doppio spartiacque — il **peso** (>150 kg → Certified per determinazione dell'autorità, art. 6.2 Reg. 947) e l'**apertura >10 m**, che porta l'iGRC in banda "20 m" tenendo alto il ground risk anche in area remota. Stima: **SAIL IV centrale** (range III-V), ben sopra il SAIL II del Percorso 6A VTOL a Pentema. Overlay privacy pesante (viabilità = persone/targhe; endurance lunga = sorveglianza persistente → DPIA/Garante). Tempi/costi: **2-4 anni / €1-5M+** in Specific; **3-7+ anni / €5-15M+** in Certified. **Nessun precedente civile italiano** per questa classe in BVLOS su territorio SNAI.

**Mare**: il ground risk **crolla al largo** (SAIL II-III offshore), ma tutti i colli di bottiglia reali sono **sotto costa**, dove vive la missione utile: **catena di autorità più lunga** (ENAC/ENAV + Guardia Costiera/Capitaneria per SAR e demanio + IIM per batimetria + vincoli Santuario Pelagos/AMP). Privacy più leggera (AIS è già pubblico), pesante solo con EO/IR identificante sotto costa.

**Leva comune**: l'**esclusione statale art. 2(3)(a) Reg. UE 2018/1139** — antincendio boschivo e SAR/guardia costiera sono espressamente elencati — può ridurre l'onere se il committente è pubblico. In entrambi i domini, **la leva risolutiva è istituzionale, non tecnica**: serve un committente pubblico che sponsorizzi il percorso, non un salto di ingegneria.

**Raccomandazione**: contenere il MTOM **≤150 kg** per restare nello spartiacque più favorevole (Specific, non Certified) — coerente col punto di progetto §1.

---

## 6. Aerostruttura — il trade-off si inverte rispetto al C3

A questa scala, il rapporto rischio aerodinamico/strutturale è **l'esatto opposto** del caso C3:

- **Aerodinamica: "facile".** Reynolds di crociera ~1,3×10⁶ (2-3,5× il C3), sopra la soglia transizionale che rendeva l'aerodinamica C3 così incerta. Polare robusta: CD0 ≈ 0,025, e ≈ 0,82, **L/D max ≈ 21** (banda 18-24) — numero passato al calcolo di endurance in §4.
- **Aeroelasticità: il rischio dominante.** Apertura 4,7× il C3, momento flessionale radicale ~30-35× superiore. A differenza del C3 (dove il margine flutter era scontato), qui **serve un inviluppo V-n + analisi di flutter dedicati** prima di dichiarare l'ala stabile — gestibile con ingegneria nota (AR 17, non 25+ come l'HALE; bassa quota = più smorzamento aerodinamico), **non la frontiera irrisolta dell'ala high-AR HALE**, ma nemmeno trascurabile.
- **Lancio**: carico di aggancio ~7 kN a 4g, rinforzo keel +2-4 kg (1-2% MTOM, vicino al CG, non influenza il flutter). Su siti di crinale con 150-250 m di spazio, il **decollo convenzionale su ruote è più semplice della catapulta**; quest'ultima resta un fallback per siti più ristretti.
- **Pannelli solari sull'ala**: area utile realistica **~5,5 m²** (banda 5,0-6,5), massa aggiuntiva **~13-15 kg** (7-8% MTOM), penalità L/D −3-5%, frequenze di flutter −3-5% (da includere nel modello aeroelastico se il kit viene montato). Coerente col verdetto §4: **bonus marginale/ESG**, mai un elemento abilitante a questa scala/quota.

---

## 7. Payload — terra: vantaggio fisico reale; mare: fattibilità differenziata per missione

### 7.1 Terrestre (antincendio, viabilità/dissesto)
Payload raccomandato: gimbal EO/IR multi-sensore (LWIR 640×512+, NEdT ≤50 mK) + RGB large-format + multispettrale (NDVI), ~15-30 kg totali. **No LiDAR di serie** (poco efficiente a questa quota/velocità), **no SAR** (troppo pesante per la classe, e comunque dominato dall'EGMS Copernicus gratuito per il monitoraggio lento delle frane).

Copertura: **80-120 km²/h netti** → ciclo completo di rivisitazione della Liguria interna (~3.050 km²) in **2-3 giorni**. Vantaggio netto su Sentinel-2 in risoluzione (40-400×) e latenza (minuti vs giorni) **solo per early-detection ed emergenza** — sul monitoraggio lento e wide-area, Copernicus gratuito resta lo strumento giusto e va **orchestrato, non replicato**.

### 7.2 Marittimo (dettaglio §8)
Valutazione onesta e **differenziata missione per missione**, non un giudizio unico sull'intera sezione marina.

---

## 8. Sezione dedicata — Sorveglianza marittima

### 8.1 Verdetto per missione (nessuna generalizzazione)

| Missione | Verdetto | Perché |
|---|---|---|
| **Traffico commerciale** | ✅ **FATTIBILE** | AIS a bordo è banale in massa/potenza; da 3.000 m l'orizzonte radio VHF copre ~226 km contro i ~29 km di una stazione costiera. Valore vero: correlazione **dark-vessel** in tempo reale (contatto radar/EO senza eco AIS). Architettura già validata da EMSA (Hermes 900, Airbus Flexrotor, contratto €30M dal 2026). |
| **Traffico diportistico/turistico** | ✅ **FATTIBILE** | Il diporto spesso non ha AIS attivo → il gimbal EO/IR diventa il sensore primario. Vantaggio di persistenza più netto: overwatch continuo su fascia costiera che nessun altro asset offre. Attenzione: overlay privacy/DPIA (identificazione di persone su imbarcazioni). |
| **SAR / uomo in mare (MOB)** | ⚠️ **FATTIBILE CON LIMITI** | Onestà tecnica dovuta: la detection termica di una persona in acqua da aria è **aleatoria** (basso/variabile contrasto, sea clutter), documentata in letteratura come problema non risolto. Molto migliore la detection del **natante** e l'**homing su beacon RF** (406/121,5 MHz Cospas-Sarsat, AIS-SART VHF). Il valore reale è la **persistenza sull'area-datum** di ricerca (centinaia-migliaia di km²/sortita per le 10-20h di endurance), non la sostituzione dell'elicottero. |
| **Controllo fondali (batimetria)** | ❌ **NON FATTIBILE con questo airframe** | L'EO/IR non vede il fondale oltre pochi metri d'acqua cristallina. La batimetria vera richiede LiDAR ALB (Airborne LiDAR Bathymetry, es. classe VQ-840-G), che pur entrando in massa (~15 kg) costa **€1M+** e impone un profilo di volo basso/lento da rilievo — **antitetico** alla missione di persistenza di questa piattaforma. **Ridimensionato** a monitoraggio ottico costiero di superficie (qualità dell'acqua, praterie di Posidonia in aree marine protette) in acque bassissime e trasparenti; la batimetria vera va affidata ad altri asset (nave idrografica, AUV, ALB con equipaggio). |

### 8.2 Payload marittimo raccomandato
Ricevitore AIS dual-channel + gimbal EO/IR con MWIR raffreddato + ricevitore RF/DF (406/121,5 MHz + AIS-SART) + SATCOM per operazioni oltre linea di vista, ~15-30 kg totali, 200-350 W — dentro il budget di massa/potenza della piattaforma condivisa con la variante terrestre, endurance preservata. Radar marittimo dedicato: solo al vertice MTOM (200-250 kg) e a costo di endurance — **opzione, non baseline**.

### 8.3 Regolatorio marittimo
Vedi §5 — SAIL II-III offshore ma catena di autorità sotto costa (ENAC/ENAV + Guardia Costiera + IIM + vincoli AMP/Santuario Pelagos), leva dell'esclusione statale art. 2(3)(a) ancora più diretta (SAR e guardia costiera espressamente elencati nell'elenco delle attività escluse).

### 8.4 Economia marittima
Delta payload marittimo su airframe condiviso: **€0,3-0,96M** (base ~€0,55M); standalone €2,1-4,1M. OpEx ~€0,75M/anno. **NPV@12%: -€6,8M (worst) / -€3,1M (base) / +€0,3M (best marginale)**. Comparabile naturale: contratto agenzia stile Guardia Costiera/EMSA/Frontex FASS. "Controllo fondali" **escluso dai ricavi** — non generabile con questo asset (§8.1).

---

## 9. Economia complessiva — il verdetto che decide tutto

| | Terrestre | Marittimo |
|---|---|---|
| CapEx (base) | ~€1,8M | ~€0,55M (delta su airframe condiviso) / €2,1-4,1M standalone |
| OpEx annuo | ~€0,6M | ~€0,75M |
| NPV@12% worst/base/best | **-€5,4M / -€2,3M / +€0,1M** | **-€6,8M / -€3,1M / +€0,3M** |
| Chi paga (comparabile) | Regione Liguria AIB (L.353/2000), Consorzi Forestali, PNRR dissesto (M2C4) | Guardia Costiera/EMSA/Frontex FASS (contratto agenzia pluriennale) |

**Verdetto netto: nessuna delle due varianti è finanziabile standalone entro il tetto ~€1M di Firmamento.** Il solo CapEx lo eccede in entrambi i casi, e l'NPV di base è negativo senza un ricavo già impegnato. **Entrambe richiedono un anchor pubblico pluriennale che copra gli OpEx PRIMA di ogni impegno di CapEx** — esattamente la logica *demand-first* già consolidata nel progetto per le altre piattaforme, e coerente col benchmark reale EMSA-Tekever (€7,5-15M/anno) già presente nello Studio.

**Sinergia terra/mare**: airframe condiviso + payload intercambiabile vale **€1-2,5M di CapEx e €0,2-0,4M/anno di OpEx risparmiati** rispetto a due piattaforme separate — un livello di modularità genuinamente difendibile (a differenza del caso T1-T2 già escluso in `10-fasce-engineering.md` §7). Non elimina però la dipendenza dall'anchor, e un uso realmente simultaneo (conflitto stagionale: picco antincendio estivo vs picco turistico estivo) **eroderebbe** parte del risparmio, richiedendo comunque 2 velivoli in alta stagione.

**Sequenza raccomandata**: il **Percorso 6A VTOL COTS** (già raccomandato nello Studio, dentro il tetto finanziabile, TRL 9) **viene prima** — genera il track-record operativo che serve a conquistare l'anchor pubblico. T-SORV viene **dopo, e solo anchor-gated**: complementare al 6A per missione (area vasta/endurance lunga vs punto-punto/agile), ma **in competizione di budget** con esso finché il tetto di finanziabilità resta ~€1M.

---

## 10. Sintesi dei verdetti (una riga per asse)

| Asse | Verdetto |
|---|---|
| Categoria | Non C3 — Specific/Certified, fascia T2/T3 |
| Configurazione | Non-VTOL, catapulta/ROG — corretto per missione ad area vasta |
| Quota | 3.000 m AMSL (banda 2.500-3.500 m), sopra i crinali reali con margine |
| Endurance | 20h raggiungibili OGGI con ibrido ICE+buffer elettrico, confermato da benchmark reali |
| Solare | Marginale/non abilitante — opposto esatto del caso HALE |
| Aerodinamica | Favorevole (Re alto) |
| Aeroelasticità | Rischio dominante ma gestibile con ingegneria nota |
| Regolatorio | SAIL IV terra / SAIL II-III mare offshore; 2-7 anni, €1-15M; nessun precedente italiano |
| Payload terra | Vantaggio fisico reale su GSD; valore solo su early-detection, non su wide-area lento |
| Payload mare | 3 missioni fattibili, 1 (fondali) non fattibile con questo airframe |
| Economia | **Non finanziabile standalone in nessuna delle due varianti — serve anchor pubblico pluriennale** |
| Sequenza | 6A prima (dentro budget), T-SORV dopo e solo anchor-gated |

---

## 11. Falsifying observations principali (aggregate dai 7 documenti sezionali)

1. Un sopralluogo che riveli **meno di 150 m** di spazio utile su ogni sito di crinale candidato riaprirebbe la valutazione VTOL.
2. Un'analisi di flutter dedicata che mostri **Vf < 1,2×Vd** all'AR 17 con le masse solari installate invaliderebbe il punto di progetto §1/§6.
3. Conferma ENAC in pre-application che l'iGRC reale su territorio SNAI ligure sia **superiore** alla stima (SAIL V-VI anziché IV) renderebbe il percorso Specific impraticabile, forzando Certified con costi/tempi molto più alti.
4. Un **committente pubblico pluriennale** (Regione Liguria AIB, Guardia Costiera/EMSA-style) che si impegni PRIMA del CapEx è l'unica condizione che sblocca la finanziabilità — la sua assenza rende l'intero progetto non attivabile, non solo rischioso.
5. Dati di volo reali che mostrino un tasso di **detection MOB** significativamente peggiore delle attese letterarie confermerebbe il limite già dichiarato in §8.1 e imporrebbe di riposizionare la missione SAR come "supporto ad area vasta", non "detection primaria".
6. Una **quotation vendor reale** (RFQ) per un airframe Tekever-class o equivalente europeo che risulti fuori dal bracket €1,25-3,2M cambierebbe l'intera economia di §9.

---

## 12. Documenti sezionali (dettaglio completo)

| # | Documento | Contenuto |
|---|---|---|
| `25a` | ConOps, morfologia e target di quota | ConOps, siti di lancio, dati orografici, decisione VTOL, requisiti RTM preliminari |
| `25b` | Aerostruttura ala>10m e solare | Punto di progetto, polare, aeroelasticità, lancio, area/massa solare |
| `25c` | Propulsione ed endurance 10-20h | Trade study propulsione, calcolo bottom-up masse energia, verdetto solare |
| `25d`/`26b` | Regolatorio ENAC terra e mare | Percorso Specific/Certified, SAIL, timeline/costi, catena di autorità marittima |
| `25e` | Payload EO terrestre | Sensori, GSD, copertura, confronto satellite |
| `26a` | Payload e missione marina | Verdetto per missione, payload raccomandato, limiti tecnici onesti |
| `25f`/`26c` | Economia terra e mare | CapEx/OpEx/NPV, verdetto finanziabilità, sinergia, sequenza |

---

### Riga di fondo

> T-SORV è **tecnicamente fattibile e ben fondato** su ogni asse ingegneristico: non-VTOL su area vasta è la scelta corretta (ribalta il verdetto C3 perché cade il vincolo di spazio confinato), 3.000 m domina la morfologia ligure reale, 20h sono raggiungibili oggi con propulsione ibrida convenzionale (il solare resta un bonus, non un abilitante — l'esatto opposto del caso HALE), l'aerodinamica è favorevole e l'aeroelasticità è un rischio gestibile con ingegneria nota. Il payload terrestre ha un vantaggio fisico reale sul satellite per l'early-detection; il payload marittimo è fattibile su 3 missioni su 4 (il controllo fondali va escluso con questo airframe). **Il collo di bottiglia non è tecnico: è economico.** Nessuna delle due varianti (terra o mare) è finanziabile standalone entro il tetto di ~€1M di Firmamento — entrambe richiedono un anchor pubblico pluriennale (Regione Liguria per l'antincendio, Guardia Costiera/EMSA-style per il mare) **prima** di ogni impegno di CapEx, con la stessa logica demand-first già consolidata nel resto del progetto. La sequenza corretta resta: **Percorso 6A prima** (dentro budget, genera il track-record), **T-SORV dopo, solo se e quando arriva l'anchor**.
