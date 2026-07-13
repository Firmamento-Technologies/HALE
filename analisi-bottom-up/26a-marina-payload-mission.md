# 26a — Variante marittima T-SORV: payload e mission profile per quattro missioni marittime

**Analisi bottom-up di payload EO/IR/RF per la variante marittima della piattaforma T-SORV**
Autore: Earth Observation Payload Expert · Data: 2026-07-13 · Progetto HALE / Firmamento Technologies

> **Perimetro.** Questa è una sezione aggiuntiva del report di fattibilità della piattaforma **T-SORV** (UAV fixed-wing, endurance 10-20 h, apertura > 10 m, MTOM 100-250 kg). La variante terrestre gemella — stessa cellula, missione diversa — è trattata in documento parallelo. **Qui si affronta solo la variante/missione marittima**: cosa cambia nel payload e nel Concept of Operations (ConOps) rispetto all'uso terrestre. Firmamento è **operatore di servizi**, non OEM: l'output è un servizio (Maritime Domain Awareness / SAR-support-as-a-service), non un velivolo venduto.
>
> **Metodo.** Per ciascuna delle quattro missioni richieste — (1) traffico commerciale, (2) traffico diportistico/turistico, (3) ricerca e soccorso incl. uomo in mare (MOB), (4) controllo fondali — si derivano i requisiti di sensore, si dimensiona il payload rispetto al budget di massa/potenza della cellula, si confronta con gli asset esistenti (Guardia Costiera, VTS, AIS satellitare, EMSA RPAS) e si emette un **verdetto di fattibilità onesto** (fattibile / fattibile con limiti / non fattibile con questo airframe). Ogni claim porta tag **[FATTO]** o **[STIMA]** con livello di confidenza.

---

## 0. Cosa cambia rispetto alla variante terrestre (sintesi)

| Dimensione | Variante terrestre | Variante marittima | Implicazione payload/ConOps |
|---|---|---|---|
| Sfondo scena | Suolo/vegetazione/edificato, alto contrasto termico e strutturale | Superficie mare: **basso e variabile contrasto termico**, sea clutter, sun glint, moto ondoso | IR/termico marittimo molto più difficile; serve stabilizzazione gimbal spinta e detection algoritmica |
| Cooperazione target | Bersagli non cooperanti (frane, incendi, infrastrutture) | Molti target **cooperanti via AIS** (navi), altri **non cooperanti** (diporto, dark vessels, MOB) | Nasce un layer RF (AIS/SART) assente a terra |
| Georiferimento | Punti a terra, DTM disponibile | Superficie mobile senza feature fisse | Tracking basato su fusione AIS + radar + EO, non su ortofoto |
| Link/BRLOS | LOS o rilanci terrestri | Operazione **offshore Beyond Radio Line of Sight**: serve **SATCOM** per C2 e downlink | Aumento massa/potenza avionica; latenza satellitare |
| Rischio a terra (SORA) | Sorvolo di persone/abitato → ground risk alto | Sorvolo mare → **ground risk ridotto**, ma air risk e ditching da gestire | SORA marittima potenzialmente più favorevole sul GRC |
| Recupero dato | Utile in ore/giorni per molti servizi | SAR/MOB: **latenza secondi-minuti**, azionabile in tempo reale | Downlink live prioritario, non store-and-forward |

**Punto chiave.** La variante marittima **aggiunge due sottosistemi assenti a terra** — un **ricevitore AIS** e un **payload RF/Direction-Finding per beacon di soccorso** — e **inasprisce** i requisiti di IR (basso contrasto sul mare) e di link (BRLOS/SATCOM). L'ottica EO ad alta risoluzione e il termico restano il nucleo comune con la variante terrestre.

---

## 1. Budget di massa e potenza del payload (vincolo dimensionante)

[STIMA · confidenza media] Per un fixed-wing MTOM 100-250 kg la frazione di payload utile realistica è ~15-25% della MTOM, ovvero **~15-60 kg**, da cui va sottratto l'incremento avionico marittimo (SATCOM, ~3-8 kg). **Payload sensoristico netto assunto: ~20-40 kg**, potenza elettrica disponibile per payload ~200-600 W a seconda del punto MTOM e dell'endurance target.

| Sottosistema candidato | Massa | Potenza | Note marittime |
|---|---|---|---|
| **Ricevitore AIS** (dual-channel VHF) | < 1 kg | < 5 W | Trascurabile; abilita l'intera missione 1 |
| **Gimbal EO/IR** con MWIR raffreddato + EO zoom (classe L3 WESCAM MX-8 / Trillium HD / Silent Sentinel) | ~8-20 kg | ~100-250 W | Cuore delle missioni 2 e 3; MWIR raffreddato preferibile su mare |
| **Gimbal EO/IR leggero** LWIR non raffreddato (classe Octopus / Workswell) | ~2-5 kg | ~30-60 W | Alternativa a basso costo; performance MOB inferiore |
| **Radar di ricerca marittima leggero** (classe pod ScanEagle/Flexrotor) | ~15-30 kg | ~200-500 W | **Al limite superiore MTOM**; penalizza endurance |
| **Ricevitore RF / DF** per 121,5 / 406 MHz / AIS-SART | ~2-5 kg | ~10-30 W | Complementare a EO/IR per SAR/MOB |
| **LiDAR batimetrico (ALB)** classe UAV (RIEGL VQ-840-G) | ~15 kg (ultra-light ~5 kg) | ~150-300 W | Fattibile in massa ma **incompatibile col profilo di missione** (vedi §6) |

[FATTO · confidenza alta] Il radar marittimo e l'ALB non possono coesistere con un gimbal EO/IR pesante e con endurance piena su una cellula da 100-250 kg: **il budget massa/potenza impone di scegliere**. La configurazione "tutti i sensori insieme" non è dimensionabile — è un trade, non un cumulo.

---

## 2. Calcoli abilitanti (assunzioni dichiarate)

### 2.1 GSD EO/IR ai regimi marittimi
Formula: **GSD [m] = (slant_range × pixel_size) / focal_length**. La T-SORV marittima non opera né a 120 m (drone COTS) né a 20 km (HALE): quota di pattugliamento assunta **~1.500-3.000 m AGL**, identificazione via gimbal a **slant range 3-15 km**.

| Canale | Sensore (assunzioni) | Slant range | GSD | Interpretazione |
|---|---|---|---|---|
| EO (identificazione) | 4.6 µm pixel, f=300 mm (tele) | 5 km | **~8 cm** | Legge nome/sigla nave, classifica scafo |
| EO | idem | 10 km | ~15 cm | Classifica imbarcazione |
| MWIR (raffreddato) | 15 µm pixel 640×512, f=300 mm | 5 km | **~25 cm** | Rileva/traccia scafo caldo |
| MWIR | idem | 10 km | ~50 cm | Detection nave, non persona |
| MWIR su **testa di persona in acqua** (~0,2 m) | idem, per 2-3 pixel sul target | **≤ ~2 km** | GSD ~10 cm | **Vincolo duro MOB**: oltre ~2 km il target è sub-pixel |

[FATTO · confidenza alta] Nel MWIR a queste aperture il sistema è vicino al **limite di diffrazione**, non resolution-limited: la GSD termica non si migliora aggiungendo pixel. La detection di una **persona in acqua** dipende quindi dalla firma termica differenziale, non dai "pixel sul bersaglio" — ed è per questo che il MOB richiede slant range corti e sweep width stretti (§2.3, §5).

### 2.2 Orizzonte radio VHF/AIS dall'alto (il vero moltiplicatore della missione 1)
[FATTO · confidenza alta] L'AIS opera in VHF a **161,975 MHz (AIS 1 / ch 87B) e 162,025 MHz (AIS 2 / ch 88B)** — propagazione a vista (LOS). L'orizzonte radio cresce con la quota: **d[km] ≈ 4,12 × √h[m]**.

| Antenna ricevente | Quota | Orizzonte radio AIS |
|---|---|---|
| Stazione costiera VTS | ~50 m | ~29 km |
| **T-SORV @ 1.500 m** | 1.500 m | **~160 km** |
| **T-SORV @ 3.000 m** | 3.000 m | **~226 km** |

[STIMA · confidenza alta] Un ricevitore AIS a 3.000 m "vede" un raggio ~8× superiore a una stazione costiera e **riempie i buchi di copertura AIS oltre l'orizzonte costiero e dietro promontori/isole**, con latenza continua (secondi) contro i minuti-ore e le **collisioni di messaggi** dell'AIS satellitare in aree ad alta densità come il Mar Ligure.

### 2.3 Copertura di ricerca per sortita (quanto mare pattuglia)
[STIMA · confidenza media] Modello IAMSAR a strisciate parallele: **area/ora ≈ velocità × spaziatura tracce (≈ sweep width del sensore)**. Velocità di ricerca assunta ~110 km/h (~30 m/s); endurance 10-20 h con ~2 h transito per lato → **~6-16 h on-station**.

| Modalità di ricerca | Sweep width tipica | Rateo | Per sortita on-station (6-16 h) |
|---|---|---|---|
| **Ricerca navi/imbarcazioni** (target grande, EO/IR + AIS + radar) | ~4-8 km | ~440-880 km²/h | **~2.600-14.000 km²** |
| **Ricerca MOB / oggetto piccolo** (sweep stretto per detection persona) | ~0,3-1 km | ~33-110 km²/h | **~200-1.760 km²** |

[FATTO · confidenza alta] Ordini di grandezza: un pattugliamento "navi" copre migliaia di km²; una ricerca "persona in acqua" copre centinaia di km². La **SRR italiana** (Search and Rescue Region) è ~500.000 km²: un singolo UAV **non "copre il Mediterraneo"**, ma satura un'**area-datum** (l'area di probabilità attorno all'ultima posizione nota) per molte ore consecutive — che è esattamente ciò che un elicottero non può fare.

---

## 3. Missione 1 — Sorveglianza traffico commerciale

**Payload:** ricevitore **AIS** (primario) + **radar** di ricerca marittima (se dimensionabile) + **EO/IR** (identificazione visiva).

[FATTO · confidenza alta] L'AIS è obbligatorio (SOLAS cap. V reg. 19) su navi da carico ≥ 300 GT in navigazione internazionale, tutte le navi ≥ 500 GT e tutte le navi passeggeri; le navi commerciali rilevanti **trasmettono già la propria identità e rotta**. Quindi per il traffico commerciale l'AIS a bordo non "scopre" navi ignote: **le correla e le geolocalizza a bassa latenza**, e soprattutto smaschera i **dark vessels** — chi ha spento o falsificato l'AIS — incrociando il plot AIS con radar/EO.

**Valore aggiunto reale di un UAV vs reti costiere/satellitari AIS esistenti** (Guardia Costiera, VTS, AIS-Sat):
- **Copertura oltre l'orizzonte costiero** senza infrastruttura fissa (§2.2): ~226 km da 3.000 m contro ~29 km da stazione costiera. [STIMA · alta]
- **Bassa latenza continua** dove l'AIS satellitare soffre revisit (decine di minuti-ore) e **collisioni di messaggi** in aree dense. [FATTO · alta]
- **Correlazione dark-vessel in tempo reale**: un contatto radar/EO **senza** eco AIS corrispondente è un target da interrogare — l'UAV lo classifica visivamente subito, mentre il satellite SAR fornisce lo stesso indizio con revisit di giorni (Sentinel-1: 6-12 gg) e non "sotto i 15 m" di scafo. [FATTO · alta]
- **Precedente operativo**: EMSA opera già RPAS (Hermes 900, e dal 2026 Airbus Flexrotor su framework €30M) proprio con questo pacchetto — EO/IR + radar multimodo + AIS + ricevitore distress — a conferma che l'architettura di payload è matura e la value-proposition "complemento persistente al satellite" è già validata da un ente europeo. [FATTO · alta]

**Verdetto missione 1: FATTIBILE.** L'AIS è banale in massa/potenza; l'EO/IR è condiviso con le altre missioni; il radar è l'unico elemento oneroso ed è **dimensionabile solo verso il vertice MTOM (200-250 kg), a costo di endurance**. Senza radar la missione resta valida (AIS + EO/IR), con minore capacità di scoperta dark-vessel in mare aperto.

---

## 4. Missione 2 — Sorveglianza traffico diportistico/turistico

[FATTO · confidenza alta] Le imbarcazioni da diporto piccole in gran parte **non montano AIS** o usano AIS Classe B non obbligatorio → **l'AIS non è il sensore primario**. Il **payload EO/IR ad alta risoluzione (gimbal) diventa il sensore primario**, l'AIS è solo contesto.

**Casi d'uso (rilevanti per l'economia turistica costiera ligure):**
- **Controllo distanze di sicurezza da costa e da aree protette** (limiti di navigazione/ancoraggio in AMP, corridoi di lancio, fasce bagnanti): EO con GSD ~8-15 cm a 5-10 km identifica scafo, rotta e posizione rispetto ai limiti. [STIMA · media]
- **Monitoraggio afflusso turistico costiero**: conteggio e densità imbarcazioni in rade e baie, mappe di pressione antropica (utile ad AMP liguri e Comuni). [STIMA · media]
- **Individuazione imbarcazioni in difficoltà** prima della chiamata di soccorso (deriva, assetto anomalo, persone in acqua vicino a scafo). [STIMA · media]

**Verdetto missione 2: FATTIBILE.** È la missione dove l'UAV persistente ha il vantaggio più netto: **nessun altro asset offre overwatch continuo su una fascia costiera diportistica** — la Guardia Costiera interviene su chiamata, il satellite passa e va. Requisito dimensionante = gimbal EO/IR di qualità + downlink live; radar non necessario (target piccoli e vicino costa). Attenzione **privacy** (§9): imagery su persone/natanti richiede minimizzazione e base giuridica.

---

## 5. Missione 3 — Ricerca e soccorso (SAR) incluso uomo in mare (MOB)

**Payload critico:** **IR/termico ad alta sensibilità** (MWIR raffreddato) + **ricevitore RF/DF** per beacon di soccorso.

### Onestà tecnica sul MOB (problema noto e non banale)
[FATTO · confidenza alta] La detection di una persona in acqua dall'aria via termico è **intrinsecamente difficile**, non un dettaglio:
- La sola **testa** emerge (~0,2 m), spesso bagnata → **contrasto termico ridotto e variabile** con ora del giorno, stagione, temperatura del mare; di giorno il sun glint e il riscaldamento superficiale possono **annullare o invertire** il contrasto. [FATTO · alta]
- **Sea clutter** e moto ondoso generano falsi positivi; il bersaglio è **piccolo, intermittente** (nascosto tra le onde). [FATTO · alta]
- Vincolo geometrico (§2.1): per 2-3 pixel sul target servono slant range **≤ ~2 km** → **sweep width stretto** → rateo di copertura basso (~33-110 km²/h). [STIMA · media]
- Lo stato dell'arte (studio *Low Contrast Challenge and Limitations of Thermal Drones in Maritime SAR*, Drones 2024, DOI 10.3390/drones8030076; benchmark **SeaDronesSee**, **MOBDrone** ~125k frame) documenta esattamente questi limiti e la necessità di detection AI dedicata: **il termico aiuta ma non "risolve" il MOB**, specie di giorno e con mare formato. [FATTO · alta]

**Implicazione:** il MOB richiede **fusione multi-sensore** (MWIR + EO + detection AI + eventuale illuminatore/SW light per notte) e va abbinato al layer RF.

### Layer RF / Direction Finding (complementare, ad alto valore)
[FATTO · confidenza alta] I dispositivi di segnalazione emettono su frequenze note:
- **EPIRB / PLB / ELT**: **406 MHz** (sistema Cospas-Sarsat) + **121,5 MHz** come homing beacon. [FATTO · alta]
- **AIS-SART** e dispositivi **MOB-AIS** personali: trasmettono sui canali AIS VHF (**161,975 / 162,025 MHz**), ricevibili dallo **stesso ricevitore AIS** già a bordo. [FATTO · alta]

[STIMA · alta] Un payload **RF/DF** che intercetta e triangola 406/121,5 MHz e AIS-SART trasforma l'UAV in un **homing su beacon a lunga persistenza**: se il naufrago indossa un PLB/MOB-AIS, la detection RF è **enormemente più robusta** del termico e non soffre di contrasto/clutter. Il termico serve per il naufrago **senza** beacon.

### Dove l'UAV aggiunge valore reale vs asset esistenti
[FATTO/STIMA · alta] Elicotteri Guardia Costiera e mezzi navali sono insuperabili in **risposta puntuale e recupero fisico** (l'UAV non recupera nessuno). Il valore dell'UAV è **ortogonale**: **persistenza su area vasta** — presidiare per 6-16 h consecutive l'area-datum (§2.3, centinaia di km² per il MOB, migliaia per la ricerca-natante), **estendendo la ricerca** e liberando l'elicottero per l'intervento. È un **moltiplicatore di ricerca**, non un sostituto del soccorso.

**Verdetto missione 3: FATTIBILE CON LIMITI.** Fattibile e ad alto valore per: (a) ricerca di **imbarcazioni/relitti** (target grande); (b) **homing su beacon** RF (PLB/EPIRB/AIS-SART). **Limitata e da non sovravendere** per il **MOB senza beacon**, dove il termico da aria è aleatorio (peggiore di giorno). Payload dimensionante = MWIR raffreddato + RF/DF + downlink live + coordinamento IMRCC.

---

## 6. Missione 4 — Controllo fondali

**Valutazione critica onesta.** Un payload EO/IR aereo convenzionale **non vede il fondale** se non in acque bassissime e otticamente cristalline (pochi metri, sole alto, mare calmo, torbidità nulla). La batimetria vera richiede **LiDAR batimetrico aviotrasportato (ALB)**.

[FATTO · confidenza alta] Stato dell'arte ALB:
- Sistemi ALB "classici" (RIEGL VQ-880-G, **Leica Chiroptera-5**, laser verde ~515-532 nm) sono progettati per **aeromobili con equipaggio** (elicottero, piccolo fixed-wing) e costi tipicamente **€1M+**. [FATTO · alta]
- Esiste ormai una classe **ALB "UAV-compatible"**: **RIEGL VQ-840-G (~15 kg)** e sistemi ultra-light (~5 kg, es. Fugro RAMMS). In **massa** sono compatibili con la T-SORV (rientrano nel budget di §1). [FATTO · alta]

[STIMA · confidenza media] **Ma la fattibilità non è di massa, è di profilo di missione ed economia:**
- L'ALB penetra al più **~1,5-2 volte la profondità di Secchi** (acque limpide poche decine di m al meglio; nel Mar Ligure costiero torbido spesso **pochi metri**), richiede **volo basso e lento** e passate a griglia da rilievo topografico — **l'opposto** del pattugliamento persistente ad alta quota per cui la T-SORV è concepita.
- È una **missione di rilievo idrografico programmato** (survey), non di **sorveglianza persistente**: usa la cellula in modo antitetico alle missioni 1-3 e ne annulla il vantaggio (persistenza).
- Costo del sensore (**€0,5-1M+**) e TRL/disponibilità commerciale a questa scala **fuori portata** per il modello di servizio Firmamento in fase pilota. [STIMA · media]

**Cosa resta realisticamente fattibile con la T-SORV (opzione a):** **monitoraggio costiero in acque bassissime e trasparenti con EO multispettrale** — qualità dell'acqua, torbidità, fioriture, e **mappatura di praterie di Posidonia** visibili in condizioni ottiche ideali (rilevante per le **AMP liguri**: Portofino, Cinque Terre, Bergeggi). Questo è **batimetria/bentonico qualitativo di superficie**, non idrografia metrica.

**Cosa va escluso (opzione b):** la **batimetria vera / cartografia dei fondali** con questo airframe va **esplicitamente ridimensionata nel ConOps**. Serve un **asset diverso**: ALB su aeromobile con equipaggio, **nave idrografica multibeam**, **AUV/ROV subacqueo**, o satellite/derived-bathymetry specializzato.

**Verdetto missione 4: NON FATTIBILE come "controllo fondali/batimetria" con questo airframe.** Declassare a **monitoraggio ottico costiero di superficie (multispettrale)** in acque basse e limpide, come sotto-prodotto opportunistico delle missioni costiere — non come missione autonoma.

---

## 7. Requisiti di missione trasversali

| Requisito | Missione diurna (1, 2) | Missione notturna (3 SAR/MOB) |
|---|---|---|
| Sensore primario | EO zoom + AIS | **MWIR raffreddato** + RF/DF; EO inutile al buio |
| Illuminazione | Non necessaria | Utile **illuminatore NIR/SW light** o faro per identificazione ravvicinata finale |
| Link/downlink | Live per identificazione | **Live prioritario a IMRCC**, latenza minima |
| Contrasto termico | — | Migliore di notte (mare più uniforme) ma comunque basso → limite MOB |

**Autonomia di ricerca su area.** [STIMA · media] Con 10-20 h di endurance (§2.3): ricerca-natante ~2.600-14.000 km²/sortita; ricerca-MOB ~200-1.760 km²/sortita. Un secondo velivolo in staffetta garantirebbe **presidio 24/7 dell'area-datum**.

**Integrazione con centri di coordinamento.** [FATTO · alta] L'interlocutore operativo è l'**IMRCC** (Italian Maritime Rescue Coordination Centre, Centrale Operativa del Comando Generale delle Capitanerie di Porto – Guardia Costiera, Roma) e le articolazioni MRSC territoriali. Il servizio deve fornire **feed EO/IR + plot AIS/radar + allarmi RF** in un formato ingeribile dai loro sistemi C2, sotto tasking dell'autorità SAR — **non** come sorveglianza autonoma.

**Link/BRLOS.** [FATTO · alta] Operando offshore oltre l'orizzonte radio, servono **SATCOM per C2 e downlink** (incremento massa/potenza avionica, §1) e gestione della **latenza satellitare** — differenza sostanziale rispetto alla variante terrestre, spesso in LOS.

---

## 8. Payload raccomandato complessivo

[STIMA · confidenza media-alta] Configurazione **baseline** (fattibile in massa/potenza/endurance su tutto lo spettro MTOM):

1. **Ricevitore AIS dual-channel** (< 1 kg, < 5 W) — abilita missione 1 e riceve AIS-SART/MOB-AIS.
2. **Gimbal EO/IR con MWIR raffreddato + EO zoom** (~8-15 kg, ~150-250 W) — cuore di missioni 2 e 3, utile in 1.
3. **Ricevitore RF/DF 406 / 121,5 MHz** (~2-5 kg) — homing beacon per SAR/MOB.
4. **SATCOM** per C2/downlink BRLOS (~3-8 kg).

→ **Totale baseline ~15-30 kg, ~200-350 W**: dentro il budget, con endurance preservata.

**Opzioni (trade esplicito, non cumulabili con endurance piena):**
- **+ Radar di ricerca marittima leggero** (~15-30 kg, ~200-500 W): solo su MTOM 200-250 kg, per scoperta dark-vessel in mare aperto (missione 1 avanzata), a **costo di endurance**.
- **ALB VQ-840-G**: **escluso** dal ConOps di sorveglianza; eventualmente come **missione di rilievo separata e occasionale**, non nella configurazione persistente.
- **EO multispettrale costiero**: opzione leggera per il monitoraggio ottico di superficie (missione 4 ridimensionata).

---

## 9. Falsifying observations (≥5)

1. **AIS-only è ridondante col satellite.** Se l'AIS satellitare (es. costellazioni commerciali) copre il Mar Ligure con latenza accettabile e senza collisioni, il vantaggio "AIS dall'alto" dell'UAV si assottiglia alle sole aree ombra costiere. *Test:* misurare latenza e tasso di collisione S-AIS reali sul Ligure vs picture UAV continua.
2. **Il radar non entra nel budget con endurance utile.** Se il radar marittimo leggero + gimbal + SATCOM porta l'endurance sotto ~8 h, la missione 1 "avanzata" (dark-vessel offshore) **non è fattibile** con questo airframe. *Test:* energy/mass budget con radar reale a bordo.
3. **Il MOB da termico ha detection probability troppo bassa di giorno.** Se in prove reali (mare 2-3, sole alto) la Pd su testa-di-persona a slant range operativi è bassa, **la missione 3 va venduta solo come ricerca-natante + homing RF**, non come MOB detection ottico. *Test:* trial con manichino termico/nuotatore, replica dello studio Drones 2024. **(Falsificazione sulla missione MOB.)**
4. **Il "controllo fondali" è tecnicamente non fattibile con questo airframe.** Se la torbidità costiera ligure limita la penetrazione ottica/ALB a pochi metri e il profilo survey è incompatibile con la persistenza, la missione 4 **cade** (o si riduce a monitoraggio ottico di superficie). *Test:* misure di profondità di Secchi lungo la costa target + prova EO multispettrale. **(Falsificazione sulla fattibilità del controllo fondali.)**
5. **Nessun mandato/tasking dall'autorità SAR.** Se IMRCC/Guardia Costiera non integra un feed di terzi nel proprio C2 o non affida tasking a un operatore privato, il servizio SAR-support **non ha canale operativo**, per quanto capace sia il payload. *Test:* MoU / interlocuzione istituzionale prima di dimensionare la flotta.
6. **La privacy blocca la sorveglianza diportistica sistematica.** Se la ripresa continua di natanti/persone in fascia costiera turistica non supera una DPIA (base giuridica, minimizzazione), la missione 2 va limitata a eventi/aree specifiche. *Test:* DPIA preliminare con il Titolare pubblico.

---

## 10. Compliance (sintesi)

- **GDPR** (Reg. UE 2016/679 + D.Lgs. 196/2003): imagery su persone/natanti (missione 2 soprattutto) → DPIA, base giuridica, minimizzazione. Missione SAR ha base giuridica forte (salvaguardia vita). Conf. media.
- **EASA/ENAC**: BVLOS marittimo in **categoria Specific**, SORA con **GRC ridotto sul mare** ma air-risk e C2/BRLOS via SATCOM da dimostrare; gestione ditching. Conf. alta.
- **Spettro/RF**: ricezione AIS/406/121,5 MHz è passiva; DF su frequenze di soccorso va coordinato con autorità (Cospas-Sarsat/Guardia Costiera). Conf. media.
- **SAR**: operazione sotto **coordinamento IMRCC**, non autonoma; nessun recupero fisico da parte dell'UAV. Conf. alta.

---

## Riga di fondo

La variante marittima della T-SORV è **fattibile e sensata su 2,5 delle 4 missioni**, purché venduta come **complemento persistente** agli asset esistenti (satellite AIS, VTS, Guardia Costiera, EMSA RPAS) — non come loro sostituto. Il **payload raccomandato** è compatto e condiviso: **ricevitore AIS + gimbal EO/IR con MWIR raffreddato + ricevitore RF/DF (406/121,5 MHz + AIS-SART) + SATCOM**, entro ~15-30 kg e ~200-350 W. Il **radar** è un'opzione dimensionabile solo al vertice MTOM e a costo di endurance. Il **"controllo fondali"** con questo airframe **non è fattibile** come batimetria e va esplicitamente ridimensionato a monitoraggio ottico costiero di superficie o affidato ad asset diversi (ALB con equipaggio, nave idrografica, AUV). Onestà sul **MOB**: il termico da aria è un moltiplicatore di ricerca, **non** un rilevatore affidabile di persona-in-acqua di giorno — il valore SAR vero sta nella **persistenza sull'area-datum** e nell'**homing su beacon RF**. Verdetto per missione:

| # | Missione | Payload primario | Verdetto |
|---|---|---|---|
| 1 | Traffico commerciale | AIS + (radar opz.) + EO/IR | **Fattibile** (radar solo a vertice MTOM) |
| 2 | Diportistico/turistico | EO/IR gimbal (AIS contesto) | **Fattibile** (vantaggio persistenza più netto) |
| 3 | SAR / MOB | MWIR + RF/DF | **Fattibile con limiti** (MOB ottico aleatorio; ottimo su natante + beacon) |
| 4 | Controllo fondali | ALB / multispettrale | **Non fattibile** come batimetria; ridimensionare a monitoraggio ottico costiero |

**Payload raccomandato complessivo:** AIS dual-channel + gimbal EO/IR MWIR raffreddato + RF/DF (406/121,5 MHz + AIS-SART VHF) + SATCOM; radar marittimo come opzione a vertice MTOM; ALB escluso.

---

## Fonti e confidenza

| Tema | Fonte | Confidenza |
|---|---|---|
| RPAS marittimi EO/IR+radar+AIS+distress; complementarità al satellite; Airbus Flexrotor €30M dal 2026; Hermes 900 | EMSA — RPAS portfolio, sensors portfolio, "Why RPAS", press release contratti ([emsa.europa.eu/rpas-systems](https://www.emsa.europa.eu/rpas-systems.html); [portfolio](https://www.emsa.europa.eu/rpas-systems/portfolio.html); [sensors](https://www.emsa.europa.eu/rpas-systems/sensors-portfolio.html)) | alta |
| Dark vessels, gap AIS, target <15 m sotto soglia Sentinel-1, revisit satellite | Starboard Maritime Intelligence; Off-Nadir Delta; studio Nature 2024 (72-76% pescherecci non tracciati) via search | alta / media |
| Difficoltà detection termica MOB, sea clutter, basso contrasto | *Low Contrast Challenge and Limitations of Thermal Drones in Maritime SAR — Pilot Study*, Drones 2024, DOI 10.3390/drones8030076; benchmark SeaDronesSee, MOBDrone (~125k frame) | alta |
| ALB: RIEGL VQ-880-G/Chiroptera-5 per aeromobili con equipaggio; VQ-840-G ~15 kg UAV-compatible; Fugro RAMMS ultra-light ~5 kg; laser verde ~515 nm | RIEGL/Leica Geosystems brochure; Hydro International; GPS World via search | alta (specifiche) / media (costo €1M+) |
| Frequenze soccorso: Cospas-Sarsat 406 MHz + 121,5 MHz homing; AIS-SART su VHF 161,975/162,025 MHz | Standard Cospas-Sarsat / SOLAS cap. V; conoscenza di dominio | alta |
| Obbligo AIS SOLAS (≥300 GT internazionale, ≥500 GT, navi passeggeri); diporto spesso senza AIS | SOLAS cap. V reg. 19; conoscenza di dominio | alta |
| GSD, orizzonte radio VHF (4,12·√h), copertura ricerca IAMSAR | Calcoli propri con assunzioni dichiarate (§2) | alta (deterministici) / media (assunzioni operative) |
| Budget massa/potenza payload, endurance trade | Stima ingegneristica su MTOM 100-250 kg; da validare con cellula reale | media |
| IMRCC / coordinamento SAR italiano | Guardia Costiera — Comando Generale Capitanerie di Porto; conoscenza di dominio | alta |

**Nota epistemica.** Le specifiche dei sensori, le frequenze e i precedenti EMSA sono **fatti verificati** (confidenza alta). I ratei di copertura, i budget massa/potenza e i giudizi di valore operativo sono **stime ragionate** (confidenza media) da falsificare con trial reali sulla cellula e sull'area target, e con l'interlocuzione IMRCC. Le quattro missioni **non sono ugualmente fattibili** con lo stesso airframe: 1-2 solide, 3 con limiti onesti sul MOB, 4 da ridimensionare.
