# Allegato A.12 — Relazione VIA Preliminare (versione completa v2.0)

> **Volume 2, Allegato A.12 — Studio di Fattibilità HALE Firmamento Technologies**
> **Caso pilota**: Percorso 6A — VTOL JOUAV CW-30E, frazione Pentema (Torriglia, GE)
> **Riferimento normativo**: D.Lgs. 152/2006 Parte II (TUA) art. 19 + Allegato IV; DPR 357/1997 (recepimento Direttiva Habitat); L. 394/1991 Aree Protette; L.R. Liguria 12/1995 (Parco Antola); L.R. Liguria 32/2012 (procedure VIA regionali); Direttiva 92/43/CEE; Direttiva 2009/147/CE; L. 447/1995 (rumore); D.Lgs. 42/2004 (Codice Urbani); R.D. 3267/1923 (vincolo idrogeologico)
> **Versione**: 2.0 — 17 maggio 2026
> **Scope**: Percorso 6A VTOL pilota Pentema (Y1). Percorso 6B HALE in §A.12.10 (outlook).
> **Stato**: Documento *preliminary-grade* per **istruttoria Regione Liguria DG Ambiente + Ente Parco Antola + ARPAL**.

---

## ⚠ Caveat fondamentale

Il presente documento è una **Relazione VIA preliminare** redatta a livello desk, finalizzata a:

1. supportare la **verifica di assoggettabilità** (screening) ai sensi dell'**art. 19 D.Lgs. 152/2006** + L.R. Liguria 32/2012;
2. avviare lo **screening di Valutazione di Incidenza Ambientale (VIncA)** ex Allegato G DPR 357/1997 per il SIC/ZSC/ZPS IT1331402 "Parco Naturale dell'Antola";
3. fornire base di discussione tecnica con **Regione Liguria, Ente Parco Antola, ARPAL, Comune di Torriglia**.

**NON sostituisce** uno **Studio di Impatto Ambientale (SIA)** completo, né una **Relazione di Incidenza completa** ex Allegato G/H DPR 357/1997. Qualora la Regione Liguria, nell'istruttoria di screening, ritenga che il progetto debba essere assoggettato a **VIA piena** o a **Valutazione di Incidenza appropriata**, la presente relazione costituisce **base preliminare** da integrare con: rilievi di campo (avifauna nidificante, fonometria, bioacustica), modellazione di propagazione del rumore, mappatura GIS dei nidi noti, accordi formali con l'Ente Parco.

**Confidence aggregato del documento**: *medium* — assunzioni territoriali e di habitat sono state verificate su fonti pubbliche (SIC database, L.R. Liguria, Piano del Parco Antola) ma **non sono stati eseguiti rilievi in situ**. La presente versione si dichiara espressamente come baseline iniziale, soggetta a revisione post-consultazione formale (M+6 / M+9).

---

## A.12.1 Inquadramento del progetto

### A.12.1.1 Soggetto proponente e finalità

| Voce | Dato |
|---|---|
| Proponente | Firmamento Technologies S.r.l. (società cooperativa in costituzione) |
| Capofila operativo pilota | Coop Fabrica (Legacoop Liguria) |
| Finalità | Erogazione **servizi pubblici e cooperativi** di monitoraggio EO, antincendio, supporto Protezione Civile e connettività complementare alle Aree Interne |
| Modello di business | Operatore di servizi (NON OEM) — vendita ore-volo / capacity wholesale |
| Sito pilota | Frazione **Pentema**, Comune di **Torriglia (GE)**, Liguria — Area SNAI Antola Tigullio |
| Bando | Cooding Prototypes 2025-26 (Coopfond / Legacoop) |
| Stato progetto | Studio di Fattibilità (Gate M+10/M+11) → Fase 1 operativa M+12-M+24 |

### A.12.1.2 Descrizione tecnica delle operazioni VTOL

**Piattaforma di riferimento**: **JOUAV CW-30E** Hybrid VTOL (alternative analoghe in *Allegato A.3 Trade Study TS-002*).

| Parametro | Valore | Note |
|---|---|---|
| MTOM | **< 25 kg** (Open/Specific EASA) | Classe acustica regolare Reg. UE 2019/945 |
| Apertura alare | ~3,5 m | UAS ala fissa con VTOL elettrico |
| Propulsione | **Ibrida**: 4 motori elettrici VTOL + 1 motore termico cruise (benzina) | Generatore on-board ricarica batterie |
| Quota operativa | **100-400 m AGL** (BVLOS Specific Category) | Min. 200 m AGL su perimetro SIC come da mitigazione §A.12.6 |
| Velocità cruise | 60-110 km/h | Endurance 6-8 h con tank pieno |
| Rumore di riferimento | **65-75 dB(A) @ 100 m** in cruise; **75-80 dB(A) @ 25 m** in fase VTOL | Fonte: scheda tecnica costruttore + benchmark EASA UAS |
| Emissioni CO₂ | **~0,4-0,7 kg CO₂/h fly** (motore termico ibrido, ~85% del tempo in cruise elettrico-assistito) | Benchmark vs Cessna 172 manned: ~30 kg CO₂/h |

**Profilo di missione tipico**:
- Decollo VTOL da elipiazzola Pentema (~150 m² area sgombera, suolo esistente già antropizzato — piazzale comunale o terreno cooperativa)
- Salita a quota cruise (200-400 m AGL)
- Pattuglia/sorveglianza su rotte pianificate (corridoi predefiniti evitando nidi noti — vedi §A.12.6)
- Atterraggio VTOL su elipiazzola
- Durata media missione: **2-4 ore**

**Frequenza operativa Y1 (anno pilota)**:
- **Target**: 80 missioni/anno (~1,5/settimana media)
- **Minimo bandabile**: 50 missioni/anno (~1/settimana)
- **Distribuzione stagionale**:
  - Inverno (dic-feb): missioni dimostrative + monitoraggio neve/frane (~10-15 missioni)
  - Primavera (mar-mag): **periodo critico nidificazione avifauna** → ridotte +30% buffer cautelativo (~10-15 missioni)
  - Estate (giu-set): **peak antincendio AIB** → priorità protezione civile (~35-45 missioni)
  - Autunno (ott-nov): monitoraggio frane post-pioggia + caccia (engagement Federcaccia) (~10-15 missioni)
- **Orario**: prevalentemente **diurno** (sunrise → sunset). Notturne (twilight + notte) **solo per emergenze Protezione Civile** (incendi, frane, ricerca persone) con buffer 500 m da centri abitati.

**Infrastruttura ground**:
- Hangar Pentema: **affitto/comodato edificio esistente preferito** (CME Allegato A.9 opzione A — confidence high di disponibilità: ~70%, vedi rischio RSK-OPS-009). NO consumo di suolo. Backup opzione B = light build < 100 m² su terreno già edificabile (NO area SIC, NO area vincolata paesaggio).
- Ground Station mobile: container 20' o veicolo dedicato (parcheggio piazzale comunale Pentema)
- Antenne C2 + payload: max 2 antenne pole-mount (h < 6 m) — NO opere fondali permanenti

**Confidence inquadramento progetto**: *high* (basato su TS-002 + RFQ JOUAV documentato).

---

## A.12.2 Inquadramento territoriale e ambientale

### A.12.2.1 Localizzazione e morfologia

| Parametro | Valore |
|---|---|
| Coordinate baricentriche | 44°31'N, 9°10'E (approx.) |
| Altitudine | 1100-1300 m s.l.m. (versante settentrionale Monte Antola, 1597 m) |
| Comune | Torriglia, Città Metropolitana di Genova |
| Bacino idrografico | Bacini Trebbia + Pentemina (affluenti Po) |
| Esposizione | Versante Nord-Nord-Est, pendenze 30-60% |
| Geomorfologia | Versanti franosi, copertura forestale prevalente (faggete + castagneti) |
| Clima | Montano-appenninico: precipitazioni 1500-2000 mm/anno, neve 1-3 mesi/anno |
| Popolazione | **14 abitanti ISTAT** (residenti permanenti); incremento turistico stagionale (Presepe di Pentema dicembre + escursionismo) |

### A.12.2.2 Vincoli ambientali e paesaggistici applicabili

**Quadro sinottico dei vincoli sull'area di operazione**:

| Vincolo | Riferimento normativo | Applicabilità Pentema | Implicazioni progetto |
|---|---|---|---|
| **Parco Naturale Regionale dell'Antola** | L.R. Liguria 12/1995 + Piano del Parco | **SÌ — area inclusa nel perimetro Parco** | Operazioni soggette a parere Ente Parco; Piano del Parco governance |
| **SIC/ZSC IT1331402** "Parco Naturale dell'Antola" | DPR 357/1997 (Habitat 92/43/CEE) | **SÌ — sito coincide largamente con perimetro Parco** | VIncA obbligatoria (screening minimo) |
| **ZPS IT1331578** "Parco Antola, Praglia, Pracaba, Antola..." (denominazione esatta da verificare in istruttoria) | DPR 357/1997 + Direttiva 2009/147/CE | **SÌ — area pSCI/ZPS sovrapposta o adiacente** | Tutela avifauna Allegato I Direttiva Uccelli |
| **Vincolo paesaggistico** ex D.Lgs. 42/2004 art. 142 | Codice Urbani — territori montani > 1600 m, fasce 300 m da corsi d'acqua, boschi | **SÌ parziale — aree boscate + > 1600 m solo parte Monte Antola** | Sorvolo NON costituisce attività edilizia; eventuali hangar light-build richiedono autorizzazione paesaggistica |
| **Vincolo idrogeologico** | R.D. 3267/1923 | **SÌ — quasi totalità dei versanti Pentema** | NO opere fondali permanenti su pendio; preferenza opzione A affitto edificio esistente |
| **Vincolo acque pubbliche / Diga del Brugneto** | TUA Parte III + concessioni CAP Genova | **SÌ — bacino imbrifero Brugneto a ~5-8 km** | Cautela sorvolo: NO operazioni sopra specchio d'acqua a quote inferiori a 200 m AGL; coordinamento gestore CAP Holding |
| **IBA (Important Bird Area)** | BirdLife — non vincolante ma indicatore | Verifica IBA Antola Atlanti in istruttoria | Documento di sensibilità avifaunistica |
| **Aree percorse dal fuoco (L. 353/2000)** | Catasto incendi boschivi comunali | Verifica documenti Comune Torriglia | Eventuali vincoli decennali post-incendio |
| **Aree archeologiche** | D.Lgs. 42/2004 Parte II | Nessuna nota in area immediata Pentema | Nessun impatto atteso |

### A.12.2.3 Parco Naturale Regionale dell'Antola

**Inquadramento** (L.R. Liguria 12/1995):
- Istituito: 1995, modifiche L.R. successive
- Superficie: ~4.700 ha
- Comuni: Torriglia, Propata, Fascia, Gorreto, Rondanina, Fontanigorda
- Gestore: Ente Parco Antola (sede Torriglia)
- Strumenti: Piano del Parco; Regolamento; Piani Pluriennali Socio-Economici

**Zonizzazione** (riferimento Piano del Parco — da verificare versione vigente in istruttoria):
- **Zona A — Riserve integrali**: tutela assoluta, attività antropiche escluse salvo ricerca scientifica autorizzata
- **Zona B — Riserve orientate**: limitazioni attività antropiche, autorizzazioni specifiche
- **Zona C — Aree di protezione**: presenza antropica tradizionale, attività agro-silvo-pastorali
- **Zona D — Aree di promozione economica e sociale**: borghi e infrastrutture; Pentema rientra prevalentemente qui

**Implicazioni progetto**:
- Hangar/ground station in **Zona D** (borgo Pentema) → ammissibili con autorizzazione Ente Parco
- Corridoi di volo che attraversano **Zone A/B** richiedono coordinamento Ente Parco + valutazione sensibilità biotopi
- Necessaria **Convenzione operativa** Firmamento ⇄ Ente Parco Antola entro M+9 (collegata RSK-AMB-001 nuova proposta + RSK-REG-011)

### A.12.2.4 Rete Natura 2000 — SIC/ZSC + ZPS

**Sito SIC/ZSC IT1331402 "Parco Naturale dell'Antola"** (Direttiva 92/43/CEE):

**Habitat di interesse comunitario** (presenti o potenzialmente presenti — verifica formulario Natura 2000 in istruttoria):

| Codice habitat | Denominazione | Note |
|---|---|---|
| **9110** | Faggeti del *Luzulo-Fagetum* | Habitat prevalente versanti Pentema |
| **9130** | Faggeti dell'*Asperulo-Fagion* | Faggete neutrofile su suoli ricchi |
| **9180\*** | Foreste di versante, ghiaione e valloni del *Tilio-Acerion* | Habitat **prioritario** (\*) — tutela rafforzata |
| **6210(\*)** | Formazioni erbose secche seminaturali (*Festuco-Brometalia*) | Prati montani, prioritario se siti notevoli orchidee |
| **6510** | Praterie magre da fieno a bassa altitudine | Praterie da sfalcio |
| **8220** | Pareti rocciose silicee con vegetazione casmofitica | Affioramenti rocciosi versanti |

**Specie di interesse comunitario** (Allegati II + IV Direttiva Habitat 92/43/CEE):

| Specie | Categoria | Note di rilevanza per il progetto |
|---|---|---|
| **Lupo (*Canis lupus*)** | Allegato II + IV — **specie prioritaria** | Presenza accertata Appennino Ligure; disturbo da rumore VTOL ipotetico ma improbabile a 200+ m AGL diurni |
| **Capriolo (*Capreolus capreolus*)** | Allegato V (gestione) | Specie comune; disturbo trascurabile |
| **Lince eurasiatica (*Lynx lynx*)** | Allegato II + IV | Presenza non accertata, possibile passaggio |
| **Chirotteri** (*Myotis* spp., *Rhinolophus* spp.) | Allegato II + IV | Attività notturna → no interferenza diretta con voli diurni VTOL |
| **Tritone alpestre (*Ichthyosaura alpestris*)** | Allegato IV | Habitat acquatici; no interferenza |
| **Salamandra di Lanza (*Salamandra lanzai*)** | Allegato IV — area limite distribuzione | Tutela alta; no interferenza diretta da volo |

**ZPS — Specie di interesse comunitario** (Allegato I Direttiva Uccelli 2009/147/CE):

| Specie | Allegato I | Stato locale | Sensibilità progetto |
|---|---|---|---|
| **Aquila reale (*Aquila chrysaetos*)** | I | Nidificante Appennino Ligure; ~2-4 coppie nel comprensorio Antola (stima Parco — da confermare con Ente Parco) | **ALTA** — buffer 500-1000 m nidi noti, periodo nidificazione (mar-lug) restrizioni operative |
| **Gufo reale (*Bubo bubo*)** | I | Nidificante su pareti rocciose | **ALTA** — buffer 500 m nidi; attività crepuscolare/notturna → no interferenza voli diurni |
| **Pellegrino (*Falco peregrinus*)** | I | Nidificante pareti rocciose | **MEDIA** — buffer 300 m nidi |
| **Biancone (*Circaetus gallicus*)** | I | Migratore + possibile nidificante estivo | **MEDIA** — riduzione attività in periodo migratorio se segnalato |
| **Albanella minore (*Circus pygargus*)** | I | Migratore | **BASSA** |
| **Succiacapre (*Caprimulgus europaeus*)** | I | Nidificante a terra in radure | **MEDIA** — attività crepuscolare → no interferenza voli diurni |
| **Tottavilla (*Lullula arborea*)** | I | Praterie aperte | **BASSA** |
| **Averla piccola (*Lanius collurio*)** | I | Praterie con siepi | **BASSA** |

**Confidence inventario habitat/specie**: *medium-low* — i dati riportati sono compilati su base **fonti pubbliche secondarie** (formulario Natura 2000, atlanti regionali avifauna, letteratura). **Richiesto in fase istruttoria**: estrazione formulario standard Natura 2000 IT1331402 + acquisizione mappa nidi noti dall'Ente Parco Antola + lista specie aggiornata.

### A.12.2.5 Diga del Brugneto e risorsa idrica

**Inquadramento**:
- Diga ad arco-gravità sul torrente Brugneto (affluente Trebbia), Comune di Rondanina (GE)
- Capacità utile: **~25 milioni m³** — riserva idropotabile primaria area metropolitana Genova
- Gestore: **CAP Holding S.p.A. / IRETI** (verifica gestore in istruttoria — possibile cambiamento gestione)
- Distanza dal sito Pentema: **~5-8 km** in linea d'aria (versante adiacente)

**Implicazioni progetto**:
- Sorvolo dello specchio d'acqua: ammesso a quota ≥ 200 m AGL come da buffer cautelativo (vedi §A.12.6 mitigazioni); evitare hovering sul lago salvo emergenze Protezione Civile
- Rischio di crash UAV in lago: probabilità < 1 evento / 1.000 ore di volo (target SORA SAIL II-III) → necessario protocollo recovery + parere CAP Holding sul rischio inquinamento da carburante residuo (max ~3-5 L benzina a bordo VTOL ibrido)
- Coordinamento con **gestore diga** + **Autorità di Bacino Distrettuale Appennino Settentrionale** (parere informativo)

### A.12.2.6 Stato acustico ante-operam

Pentema è **zona prevalentemente silente**: ambiente rurale montano isolato. Classificazione acustica comunale (Comune di Torriglia, Piano di Classificazione Acustica ex L.R. Liguria 12/1998):
- **Classe I — Aree particolarmente protette** (parchi e riserve naturali, scolastiche, sanitarie): applicabile alle aree SIC interne al Parco Antola
- **Classe II — Aree prevalentemente residenziali**: borgo Pentema

**Limiti di immissione (DPCM 14/11/1997 + L.R. 12/1998)**:

| Classe | Diurno (06:00-22:00) | Notturno (22:00-06:00) |
|---|---|---|
| I | **50 dB(A)** | **40 dB(A)** |
| II | 55 dB(A) | 45 dB(A) |

**Implicazione**: il livello sonoro a terra durante operazioni VTOL deve restare al di sotto di **50 dB(A) diurno / 40 dB(A) notturno** se l'immissione interessa Zona Classe I. La stima 65-75 dB(A) @ 100 m del VTOL implica che a **200-300 m AGL** in cruise il rumore al suolo è stimabile a **45-55 dB(A)** (attenuazione geometrica + parziale assorbimento atmosferico). Questo richiede **monitoraggio fonometrico** Y1 in 3 punti rappresentativi (vedi §A.12.6).

---

## A.12.3 Identificazione e valutazione degli impatti potenziali

Per ogni fattore ambientale: descrizione → stima magnitudine → classe (basso / medio / alto) → **confidence** → mitigazioni.

### A.12.3.1 Atmosfera (aria, emissioni, clima)

**Sorgenti**:
- Motore termico ibrido VTOL (benzina): ~0,4-0,7 kg CO₂/h fly
- Generatore back-up GS (se utilizzato): trascurabile per pilota
- Trasporti logistici terra (van veicoli supporto): non oggetto specifico VIA

**Stima emissioni Y1**:
- 80 missioni × 3 h media = **240 ore di volo/anno**
- 240 h × 0,55 kg CO₂/h ≈ **~130 kg CO₂/anno** (centesime di un'auto diesel media: ~2.000 kg/anno per 15.000 km)

**Confronto alternative**:
- Sorveglianza con elicottero manned (Eurocopter EC120): ~100 kg CO₂/h → 240 h → **24.000 kg CO₂/anno** (~180× peggio)
- Sorveglianza con drone elettrico puro (es. M300): emissioni zero in volo, ma autonomia 30-40 min insufficiente per BVLOS estese
- Pattugliamento gomma (4×4 Forestale): ~0,18 kg CO₂/km × 50 km/giorno × 80 missioni ≈ **720 kg CO₂/anno** + costo personale

**Magnitudine impatto**: **BASSO** (assoluto trascurabile, fortemente favorevole vs alternative)
**Confidence**: *high* (calcoli standard fattori emissione ISPRA)

### A.12.3.2 Acque (idrosfera)

**Impatti diretti operativi**: **NESSUNO** (volo aereo, no scarichi).
**Impatti indiretti**:
- Sorvolo Diga Brugneto → rischio inquinamento da carburante in caso crash (~3-5 L benzina) → probabilità target SORA < 10⁻⁴/h volo
- Eventuale impermeabilizzazione hangar (opzione B light build): gestione acque meteoriche standard pavimentazioni

**Mitigazioni**:
- Buffer ≥ 500 m laterali dallo specchio d'acqua Brugneto in operazioni di routine
- Sorvolo Brugneto consentito **solo per emergenze PC** + quota ≥ 200 m AGL
- Protocollo emergency recovery in caso crash (briefing CAP Holding + Vigili del Fuoco)

**Magnitudine impatto**: **TRASCURABILE-BASSO**
**Confidence**: *medium* (richiede formalizzazione protocollo CAP Holding)

### A.12.3.3 Suolo (geosfera + uso del suolo)

**Impatto operativo aereo**: **NESSUNO** (no consumo).

**Impatto infrastruttura ground**:
- **Opzione A preferita**: affitto/comodato edificio esistente Pentema → **consumo suolo zero**, no nuova impermeabilizzazione (confidence disponibilità ~70%)
- **Opzione B fallback**: light build hangar < 100 m² → impatto **molto contenuto** (~150 m² complessivi con piazzale), su terreno già edificabile fuori SIC e fuori vincolo paesaggistico stringente
- **Elipiazzola decollo VTOL**: utilizzo piazzale comunale o pista esistente → **consumo suolo zero**

**Vincolo idrogeologico R.D. 3267/1923**: presente quasi totalità versanti Pentema. Opzione B richiede **autorizzazione vincolo idrogeologico** Regione Liguria (Settore Difesa Suolo). Mitigazione = opzione A preferita.

**Magnitudine impatto**: **TRASCURABILE** (opzione A) / **BASSO** (opzione B)
**Confidence**: *medium-high*

### A.12.3.4 Biodiversità — Fauna

#### Avifauna (impatto principale)

**Tipologie di disturbo**:
1. **Disturbo acustico**: 45-55 dB(A) al suolo a quota cruise 200-400 m AGL
2. **Disturbo visivo**: oggetto in movimento percepibile da raptor (territoriali) come potenziale competitor o predatore
3. **Rischio collisione**: bassa probabilità per VTOL a quote 100-400 m AGL (sotto la maggior parte rotte migratorie principali — corridoio Alpi Marittime / Stretto Bonifacio è laterale) — letteratura indica **< 0,1 incidenti / 100 ore volo** per piccoli UAS in aree montane (fonte: ricerche Sentinel + ENAC bird-strike database)
4. **Disturbo nidificazione**: critico in **periodo riproduttivo (marzo-luglio)** per:
   - **Aquila reale** (incubazione marzo-aprile, allevamento maggio-luglio): pari a 4-5 mesi di sensibilità acuta
   - **Gufo reale** (incubazione gennaio-aprile)
   - **Pellegrino** (incubazione marzo-maggio)
   - **Biancone** (incubazione aprile-giugno)

**Stima magnitudine**:
- In assenza di mitigazioni: rischio **MEDIO-ALTO** per disturbo aquila reale (specie iconica + nidi noti potenzialmente in area corridoio volo)
- Con mitigazioni §A.12.6 (buffer 500-1000 m da nidi noti + riduzione +30% missioni mar-lug + quota minima 200 m AGL su SIC): rischio atteso **BASSO**

**Confidence**: *medium-low* — dipende criticamente dall'acquisizione **mappa nidi noti** dall'Ente Parco Antola (azione M+6). Senza la mappa, ogni stima è puramente teorica.

#### Mammiferi (lupo, ungulati, mesomammiferi)

**Disturbo acustico**: lupo è specie con elevata tolleranza al disturbo antropico se non associato a minaccia diretta; letteratura indica che voli aerei a > 200 m AGL non causano displacement significativo (cfr. studi su lupi Yellowstone + Apennino Centrale). Capriolo, cinghiale, daino: disturbo trascurabile a quote operative.

**Magnitudine impatto**: **BASSO**
**Confidence**: *medium*

#### Chirotteri (pipistrelli)

VTOL diurno → **no interferenza** con attività crepuscolare/notturna chirotteri.
**Magnitudine impatto**: **TRASCURABILE**
**Confidence**: *high*

#### Erpetofauna + entomofauna

Nessun impatto da volo aereo a quote di operazione.
**Magnitudine impatto**: **TRASCURABILE**
**Confidence**: *high*

### A.12.3.5 Vegetazione e habitat

**Impatto diretto su habitat**: **NESSUNO** — operazione aerea senza contatto fisico con suolo/vegetazione (escluse zone elipiazzola, già antropizzate).

**Faggete 9110 / 9130 / 9180\* (prioritario)**: nessun impatto fisico.

**Praterie 6210 / 6510**: nessun impatto fisico.

**Impatto indiretto**: trascurabile (no atterraggi su habitat naturali, no emissioni gas tossici significative, no infiltrazione idrocarburi).

**Magnitudine impatto**: **TRASCURABILE**
**Confidence**: *high*

### A.12.3.6 Paesaggio

**Impatto strutturale**:
- Opzione A: nessuna nuova struttura
- Opzione B: hangar light build < 100 m² + 2 antenne pole-mount h < 6 m → impatto visivo **molto contenuto**, mitigabile con finiture compatibili (legno, verde militare)

**Impatto visivo da volo**:
- VTOL a quota 200-400 m AGL: dimensione apparente ~0,5-1 cm a vista nuda dal suolo → percepibile ma non invasivo
- Durata sorvolo: transitorio (60-90 secondi su un dato punto in cruise)
- Frequenza: ~1,5 missioni/settimana → impatto cumulativo basso

**Vincolo paesaggistico D.Lgs. 42/2004**: opera ground richiede autorizzazione paesaggistica semplificata (DPR 31/2017) se opzione B; opzione A nessuna autorizzazione paesaggistica aggiuntiva.

**Magnitudine impatto**: **BASSO**
**Confidence**: *medium-high*

### A.12.3.7 Rumore (clima acustico)

**Modello preliminare di propagazione (semplificato)**:

| Quota AGL | Rumore stimato al suolo direttamente sotto | Note |
|---|---|---|
| 100 m | ~65 dB(A) | Solo in fasi VTOL decollo/atterraggio sopra elipiazzola |
| 200 m | ~55-58 dB(A) | Cruise minimo |
| 300 m | ~50-52 dB(A) | Cruise nominale |
| 400 m | ~46-48 dB(A) | Cruise alto |

Modello: $L_p = L_p(d_0) - 20 \log_{10}(d/d_0) - \alpha \cdot d$, con $L_p(d_0=100m)=65$ dB(A) e $\alpha\approx 0{,}005$ dB/m (assorbimento atmosferico standard).

**Confronto con limiti L. 447/1995 + DPCM 14/11/1997 + L.R. Liguria 12/1998**:

| Punto recettore | Classe | Limite diurno | Stima impatto cruise 300 m AGL | Verdetto |
|---|---|---|---|---|
| Borgo Pentema (residenze) | II | 55 dB(A) | 50-52 dB(A) | **OK** (< limite) |
| Aree SIC interne Parco | I | 50 dB(A) | 50-52 dB(A) | **borderline** → quota ≥ 250-300 m AGL su SIC |
| Aree esterne Parco | III | 60 dB(A) | < 55 dB(A) | OK |

**Operazioni notturne**: limite I/II = 40/45 dB(A) → cruise VTOL **non compatibile** salvo emergenze PC con deroga puntuale.

**Magnitudine impatto**: **BASSO-MEDIO** (mitigabile con quote operative + scheduling)
**Confidence**: *medium* (richiede campagna fonometrica field Y1 con 3 punti misura — vedi §A.12.6)

### A.12.3.8 Salute umana

**Impatti potenziali**:
- Rumore: vedi §A.12.3.7 — sotto soglia disturbo cronico
- EMI (interferenze elettromagnetiche): trasmissioni C2 + payload a potenze decine di mW, ben sotto limiti ICNIRP per esposizione popolazione
- Rischio incidentale crash UAV su persone: target SORA SAIL II-III, *Ground Risk* dopo mitigazioni < 10⁻⁶/h volo
- Operatori a terra: ridotti (pilota remoto + visual observer), procedure SORA standard

**Magnitudine impatto**: **TRASCURABILE-BASSO**
**Confidence**: *high* (allineamento con A.11 Safety Case SORA)

### A.12.3.9 Patrimonio culturale e archeologico

**Beni culturali noti**:
- Borgo storico di Pentema (architettura rurale tradizionale, NON vincolato come bene puntuale ma soggetto a vincolo paesaggistico d'area)
- Presepe meccanico storico di Pentema (manifestazione culturale dicembre — coordinamento eventuale con Pro Loco)
- Nessun bene archeologico vincolato noto in area immediata operazioni

**Impatti**: nessun impatto fisico; potenziale impatto **simbolico/percettivo** se l'operazione VTOL fosse percepita come intrusiva durante eventi tradizionali (es. Presepe dicembre).

**Mitigazione**: sospensione operazioni durante eventi pubblici tradizionali Pentema (Presepe — 7-26 dicembre tipicamente) salvo emergenze PC.

**Magnitudine impatto**: **TRASCURABILE**
**Confidence**: *high*

### A.12.3.10 Sintesi impatti per fattore

| Fattore ambientale | Magnitudine impatto residuo (post-mitigazioni) | Confidence | Mitigazione chiave |
|---|---|---|---|
| Atmosfera (aria + clima) | Basso | high | Motore ibrido + ridotte ore volo; bilancio favorevole vs alternative |
| Acque | Trascurabile-Basso | medium | Buffer Brugneto + protocollo recovery |
| Suolo | Trascurabile (opzione A) | medium-high | Affitto edificio esistente |
| Avifauna nidificante | Basso | medium-low | **Buffer nidi + restrizioni mar-lug** ← punto chiave |
| Mammiferi | Basso | medium | Quota operativa + scheduling diurno |
| Chirotteri | Trascurabile | high | Voli diurni |
| Habitat | Trascurabile | high | No contatto fisico |
| Paesaggio | Basso | medium-high | Opzione A + finiture compatibili |
| Rumore | Basso-Medio | medium | Quota minima 200-300 m AGL + sched + monitoraggio fonometrico |
| Salute umana | Trascurabile-Basso | high | SORA + procedure standard |
| Patrimonio | Trascurabile | high | Sospensione eventi pubblici |

**Conclusione preliminare**: impatti complessivi **basso-bassi e mitigabili** con misure proporzionate.

---

## A.12.4 Valutazione di Incidenza Ambientale (VIncA) preliminare — Screening

### A.12.4.1 Quadro metodologico

La VIncA si applica per progetti che possono avere **incidenza significativa** su siti Rete Natura 2000 (SIC/ZSC/ZPS). Riferimenti:
- **Direttiva 92/43/CEE art. 6.3**
- **DPR 357/1997 art. 5** e Allegati G/H (recepimento italiano)
- **Linee guida nazionali per VIncA** (MATTM 2019)
- **L.R. Liguria 28/2009** (recepimento e disciplina VIncA in Liguria)

La VIncA si articola in **4 livelli progressivi**:
1. **Screening (Livello I)** ← *presente documento*
2. Valutazione appropriata (Livello II) — se screening non esclude incidenza significativa
3. Valutazione soluzioni alternative (Livello III)
4. Misure compensative (Livello IV) — solo in casi IROPI (Imperative Reasons of Overriding Public Interest)

### A.12.4.2 Identificazione siti Natura 2000 interessati

| Sito | Codice | Tipologia | Distanza/sovrapposizione |
|---|---|---|---|
| Parco Naturale dell'Antola | **IT1331402** | SIC/ZSC | **Sovrapposizione totale** con area operativa Pentema |
| Parco Naturale dell'Antola ZPS | **IT1331578** (verifica) | ZPS | Sovrapposizione totale o adiacenza stretta |
| (Eventuali altri SIC dell'Appennino Ligure adiacenti — verifica in istruttoria) | — | SIC/ZSC | Adiacenze < 5 km — possibile valutazione cumulativa |

### A.12.4.3 Caratterizzazione del progetto rispetto ai siti

**Tipologia di interferenza**:
- **Diretta fisica**: NESSUNA (operazione aerea, no opere fondali su habitat tutelati)
- **Diretta sonora**: rumore al suolo 45-55 dB(A) su area SIC (Classe I → limite 50 dB(A))
- **Diretta visiva**: oggetto in movimento percepibile da specie territoriali
- **Indiretta**: minima (no consumo risorse, no emissioni significative)

**Durata e ricorrenza**:
- Ogni singola missione: 2-4 ore
- Frequenza Y1: ~1,5 missioni/settimana
- Cumulativo Y1: ~240 ore di sorvolo/anno = **2,7% del tempo totale annuale** (240/8760 h)

### A.12.4.4 Valutazione preliminare incidenza significativa

**Criteri Allegato G DPR 357/1997**:

| Criterio | Valutazione preliminare |
|---|---|
| **Perdita di area di habitat** | NESSUNA — no consumo fisico habitat tutelati |
| **Frammentazione habitat** | NESSUNA |
| **Perturbazione specie** (rumore, presenza) | **POTENZIALE su avifauna nidificante Allegato I** — mitigabile con buffer + restrizioni stagionali |
| **Modifica densità popolazione** | Non significativa con mitigazioni |
| **Cambiamento indicatori chiave** (acqua, qualità aria) | NESSUNO |
| **Cambiamenti climatici** | NESSUNO |

**Verdetto preliminare screening VIncA**: **incidenza significativa improbabile** con applicazione delle mitigazioni proposte in §A.12.6 (in particolare buffer da nidi aquila reale + restrizione stagione riproduttiva).

**Confidence verdetto**: *medium* — dipende da:
1. Acquisizione mappa nidi noti dall'Ente Parco Antola (M+6)
2. Eventuale rilievo bioacustico ante-operam Y1 (raccomandato)
3. Conferma scientifica densità popolazione aquila reale comprensorio Antola

**Caveat**: in caso Ente Parco evidenzi nidi attivi entro buffer operativo, **lo screening NON è sufficiente** e si attiva una **Valutazione di Incidenza Appropriata (Livello II)** con rilievi field dedicati.

### A.12.4.5 Specie target di attenzione prioritaria

**Tier 1 (attenzione alta)**:
- **Aquila reale (*Aquila chrysaetos*)** — Allegato I Uccelli
- **Gufo reale (*Bubo bubo*)** — Allegato I Uccelli
- **Lupo (*Canis lupus*)** — Allegato II + IV Habitat, specie prioritaria

**Tier 2 (attenzione media)**:
- Pellegrino, Biancone (Allegato I Uccelli)
- Chirotteri (Allegato II + IV Habitat) — solo se operazioni notturne emergenza

**Tier 3 (monitoraggio standard)**:
- Restanti specie Allegati I/II/IV non specificamente sensibili al sorvolo VTOL diurno

---

## A.12.5 Quadro di sintesi rischi ambientali e linkage Risk Register

### A.12.5.1 Rischi ambientali nel Risk Register (esistenti)

| Risk ID | Descrizione | P×I attuale | Stato |
|---|---|---|---|
| **RSK-REG-011** | VIA Pentema — ARPA Liguria richiede VIA per infrastruttura ground HALE | 2×2=4 GREEN | Monitor — VIA preliminare M+6 |
| **RSK-REG-024** | Codice Navigazione R.D. 327/1942 — diritti sorvolo proprietà private + aree militari | 2×3=6 GREEN | Monitor |

### A.12.5.2 Nuovi rischi proposti

**RSK-AMB-001 (PROPOSTO)** — *Incidenza significativa avifauna nidificante in SIC/ZSC/ZPS IT1331402*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-001 |
| Categoria | Ambientale / Regolatorio |
| Descrizione | Disturbo aquila reale + altre specie Allegato I Direttiva Uccelli nidificanti in SIC/ZSC/ZPS Parco Antola → Ente Parco / Regione richiede Valutazione di Incidenza Appropriata (Livello II) o impone restrizioni operative stringenti (es. blocco mar-lug totale) |
| Probabilità (1-5) | 3 (medium — dipende da nidi attivi entro 1000 m corridoi operativi) |
| Impatto (1-5) | 3 (medium — slittamento 6-9 mesi + €30-80k costi rilievi + riduzione operatività Y1 fino a -40%) |
| P×I | **9 — AMBER** |
| Owner | environmental-consultant + Firmamento ops |
| Status | OPEN |
| Mitigation type | Mitigate + Avoid |
| Mitigazioni | 1) Acquisizione mappa nidi noti Ente Parco M+6; 2) Buffer 500-1000 m operativo da nidi; 3) Restrizione operativa mar-lug +30% margine cautelativo; 4) Quota minima 200-250 m AGL su SIC; 5) Monitoraggio acustico Y1; 6) Eventuale rilievo bioacustico ante-operam |
| Residual P×I (post-mitigazione) | 1×2=2 GREEN |
| Trigger condition | Ente Parco rifiuta parere favorevole su corridoi operativi OPPURE rilievo ante-operam evidenzia nidi attivi entro buffer |
| Falsifying observation | Se Ente Parco impone moratoria totale mar-lug → modello operativo Y1 va rivisto (peak antincendio compromesso) |

**RSK-AMB-002 (PROPOSTO)** — *Inquinamento idrico Diga Brugneto in caso crash VTOL ibrido*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-002 |
| Categoria | Ambientale / Safety |
| Descrizione | Crash VTOL ibrido sopra bacino imbrifero Brugneto → sversamento ~3-5 L benzina + componenti elettrici (batterie LiPo) → contestazione gestore CAP Holding + ARPAL |
| Probabilità (1-5) | 1 (low — target SORA crash rate < 10⁻⁴/h × buffer geografico Brugneto) |
| Impatto (1-5) | 4 (high — riserva idropotabile primaria Genova, danno reputazionale + costi bonifica) |
| P×I | **4 — GREEN** |
| Owner | safety-engineer + environmental-consultant |
| Status | OPEN |
| Mitigation type | Avoid + Mitigate |
| Mitigazioni | 1) Buffer ≥ 500 m laterali Brugneto in operazioni routine; 2) Quota ≥ 200 m AGL su lago; 3) Sorvolo solo emergenze PC; 4) Protocollo recovery con VVF; 5) Coordinamento CAP Holding entro M+9 |
| Residual P×I | 1×2=2 GREEN |
| Trigger | Singolo near-miss su bacino Brugneto |

**RSK-AMB-003 (PROPOSTO)** — *Superamento limiti acustici L. 447/1995 in punti recettori SIC Classe I*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-003 |
| Categoria | Ambientale / Regolatorio |
| Descrizione | Monitoraggio fonometrico Y1 evidenzia immissioni > 50 dB(A) diurno in aree SIC Classe I → ARPAL contesta + obbligo deroga / revisione profili volo |
| Probabilità (1-5) | 2 (low-medium) |
| Impatto (1-5) | 2 (medium — revisione SOPs + eventuale riduzione operatività -10-20%) |
| P×I | **4 — GREEN** |
| Owner | environmental-consultant + flight-ops |
| Status | OPEN |
| Mitigazioni | 1) Quota minima cruise 250 m AGL su SIC; 2) Modelli propagazione ante-operam; 3) Campagna fonometrica Y1 in 3 punti; 4) Adattamento profili volo se eccedenza |
| Residual P×I | 1×2=2 GREEN |

### A.12.5.3 Linkage RTM e gates

- **REQ-NF-AMB-01** (proposto in RTM): *Il sistema deve garantire compliance ambientale piena (VIA + VIncA) con la normativa italiana ed europea applicabile al sito pilota Pentema entro il gate M+9.* → Verifica VRD-AMB-01 (parere screening VIA Regione Liguria favorevole) + VRD-AMB-02 (parere VIncA Ente Parco favorevole).
- Gate **M+6**: deliverable = engagement Ente Parco + Regione Liguria DG Ambiente + ARPAL avviato
- Gate **M+9**: deliverable = screening VIA + screening VIncA presentati e in istruttoria
- Gate **M+10/M+11**: deliverable = pareri positivi (almeno preliminari) ottenuti, o trigger di re-baselining

---

## A.12.6 Mitigazioni proposte

### A.12.6.1 Pacchetto mitigazioni avifauna (priorità massima)

| # | Mitigazione | Frequenza | Costo stimato | Confidence efficacia |
|---|---|---|---|---|
| M-AVI-01 | Acquisizione mappa nidi noti specie Allegato I (aquila reale, gufo reale, pellegrino, biancone) da Ente Parco Antola | Una-tantum M+6 + aggiornamento annuale | €0 (cooperazione Ente Parco) o €5-15k se rilievo ad-hoc | high |
| M-AVI-02 | **Buffer operativo 500 m da ogni nido noto** specie Allegato I; **1000 m da nidi aquila reale** in periodo riproduttivo | Ogni missione | €0 (planning SOPs) | high |
| M-AVI-03 | **Restrizione stagionale**: missioni in periodo riproduttivo (mar-lug) ridotte +30% rispetto a target nominale; eccezione = emergenza PC | Annuale stagionale | €0 (sched) | medium-high |
| M-AVI-04 | Quota minima cruise **200 m AGL** generalizzata; **250 m AGL su perimetro SIC**; **300 m AGL** su corridoi di nidificazione noti | Ogni missione | €0 (planning SOPs) | high |
| M-AVI-05 | Monitoraggio bioacustico ante-operam Y1 (3 stazioni autonome ARU — Autonomous Recording Units, 2-3 mesi mar-mag) | Una-tantum Y1 | €10-25k | medium |
| M-AVI-06 | Reporting bird-strike + near-miss avifauna a Ente Parco + ENAC mensilmente | Mensile | €0 (procedurale) | medium |
| M-AVI-07 | Sospensione operativa immediata se incidente con specie protetta + indagine | Reattivo | n/a | n/a |

### A.12.6.2 Pacchetto mitigazioni rumore

| # | Mitigazione | Frequenza | Costo stimato |
|---|---|---|---|
| M-NOI-01 | Campagna fonometrica Y1 in 3 punti rappresentativi (borgo Pentema, perimetro SIC interno, recettore sensibile aquila se identificato) — fonometro classe 1 cadenzato | Y1: 4 sessioni stagionali; Y2+: annuale | €8-15k Y1 |
| M-NOI-02 | Modelli predittivi propagazione (CONCAWE-style o ISO 9613) per validare quote operative ante-operam | Una-tantum M+9 | €5-10k |
| M-NOI-03 | Buffer 500 m da centri abitati Pentema per missioni notturne (no operazioni notturne salvo emergenza PC) | Ogni missione | €0 |
| M-NOI-04 | Profili volo "silent mode" (cruise > 250 m AGL, motore elettrico assistito max % possibile) | Ogni missione | €0 (sched) |

### A.12.6.3 Pacchetto mitigazioni acque

| # | Mitigazione |
|---|---|
| M-ACQ-01 | Buffer ≥ 500 m laterali Diga Brugneto e ≥ 200 m AGL su specchio d'acqua |
| M-ACQ-02 | Protocollo emergency recovery in caso crash + briefing CAP Holding + Vigili del Fuoco |
| M-ACQ-03 | Coordinamento Autorità di Bacino Distrettuale Appennino Settentrionale (parere informativo) |

### A.12.6.4 Pacchetto mitigazioni paesaggio e suolo

| # | Mitigazione |
|---|---|
| M-PAE-01 | Priorità opzione A (affitto edificio esistente Pentema); opzione B solo se A indisponibile |
| M-PAE-02 | Se opzione B → finiture esterne compatibili (legno, verde militare); autorizzazione paesaggistica semplificata DPR 31/2017 |
| M-PAE-03 | NO antenne pole-mount su crinali panoramici |
| M-PAE-04 | Sospensione operazioni durante eventi tradizionali Pentema (Presepe 7-26 dicembre) salvo emergenze PC |

### A.12.6.5 Cronoprogramma mitigazioni

| Mese | Azione |
|---|---|
| M+3 | Documento A.12 v2.0 (presente) → invio informale Ente Parco + Regione Liguria DG Ambiente |
| M+6 | Acquisizione mappa nidi Ente Parco + meeting tecnico Regione + ARPAL; convenzione Ente Parco bozza |
| M+9 | Submission formale screening VIA (art. 19) + screening VIncA al Comune capofila / Regione |
| M+12 | Avvio campagna fonometrica + bioacustica field |
| M+18 | Review interim mitigazioni + tuning SOPs Y1 |
| M+24 | Bilancio Y1 monitoraggio + revisione mitigazioni Y2 |

---

## A.12.7 Procedura VIA: classe applicabile e percorso autorizzativo

### A.12.7.1 Classificazione progetto ex Allegato IV D.Lgs. 152/2006

**Verifica obblighi VIA**:

| Riferimento | Soglia / Categoria | Applicabilità progetto |
|---|---|---|
| **Allegato II** TUA (VIA obbligatoria statale) | Aeroporti con piste > 1500 m, grandi infrastrutture | **NO applicabile** (operazioni UAS BVLOS, no aeroporto) |
| **Allegato II-bis** TUA (verifica assoggettabilità statale) | Modifiche/ampliamenti Allegato II | **NO applicabile** |
| **Allegato III** TUA (VIA obbligatoria regionale) | Aeroporti con piste 800-1500 m, piste ulteriori | **NO applicabile** |
| **Allegato IV** TUA (verifica assoggettabilità regionale) | Punto **7.d** "Aerodromi" — soglia non specificata univocamente per UAS; **8.t** "Modifica/estensione progetti Allegati II/III/IV con incidenza rilevante su ambiente" | **POSSIBILMENTE applicabile** per analogia o estensione interpretativa |
| **Allegato IV** punto **7.l** | "Costruzione di linee aeree dell'energia elettrica…" / non applicabile | NO |

**Considerazione interpretativa critica**:
- Il D.Lgs. 152/2006 + Allegato IV **non disciplina esplicitamente** operazioni UAS/BVLOS — il legislatore italiano del 2006 non aveva considerato la fattispecie
- Le operazioni VTOL pilota Pentema **NON costituiscono "aerodromo"** né infrastruttura permanente
- L'**hangar light-build < 100 m²** (opzione B fallback) potrebbe rientrare in fattispecie locali (PUC Torriglia, vincolo paesaggistico DPR 31/2017) ma **non per VIA statale/regionale**
- Operatività in **Parco Regionale + SIC/ZSC + ZPS** attiva il regime VIncA + parere Ente Parco — questo è il **canale autorizzativo prioritario**, non la VIA piena

### A.12.7.2 Procedura raccomandata

**Esito atteso screening (art. 19 D.Lgs. 152/2006 + L.R. Liguria 32/2012)**: **NON ASSOGGETTABILE a VIA piena** in ragione di:
1. assenza di consumo di suolo significativo (opzione A preferita)
2. assenza di emissioni significative
3. assenza di opere infrastrutturali permanenti rilevanti
4. operatività con UAS MTOM < 25 kg → categoria Specific EASA (non aeronautica civile manned)
5. impatti residui post-mitigazione classificati basso

**Confidence verdetto NON ASSOGGETTABILITÀ**: *medium* (≈60-70%). Variabile critica = interpretazione Regione Liguria DG Ambiente + ARPAL. Se la Regione interpreta **estensivamente** la fattispecie (caso conservativo), può richiedere VIA piena → ritardo +6-18 mesi + costi +€30-100k.

**Canale autorizzativo prioritario (sicuramente applicabile)**:

| Documento | Autorità | Tempistica attesa |
|---|---|---|
| **Verifica di Assoggettabilità a VIA** (screening art. 19) | Regione Liguria DG Ambiente | 60-90 giorni |
| **Screening Valutazione di Incidenza (VIncA)** ex DPR 357/1997 + L.R. 28/2009 | **Ente Parco Antola** (gestore SIC/ZSC/ZPS) + Regione Liguria | 60-90 giorni parallelo |
| **Parere paesaggistico** (se opzione B) DPR 31/2017 semplificato | Comune Torriglia + Soprintendenza | 60 giorni |
| **Parere vincolo idrogeologico** (se opzione B) | Regione Liguria Settore Difesa Suolo | 60-90 giorni |
| **Autorizzazione comunale** (PUC + edilizia) | Comune Torriglia | 60 giorni |
| **Coordinamento CAP Holding** (Diga Brugneto) | CAP Holding / IRETI | parere informativo 30 giorni |

**Tempistiche totali stimate gate M+9 → M+12** per ottenere set completo pareri preliminari: **3-6 mesi** (parallelizzazione possibile).

### A.12.7.3 Scenario "VIA piena richiesta" (fallback)

Se la Regione Liguria richiede VIA piena nonostante l'argomentazione di non assoggettabilità:

1. **Tempistica**: ~12-18 mesi (con ricorsi → fino a 24 mesi)
2. **Costi**: SIA (Studio Impatto Ambientale) completo €40-80k + consulenze tecniche + rilievi field
3. **Impatto sul progetto**: slittamento Fase 1 operativa di 6-12 mesi → impatto su gate M+11
4. **Strategia di mitigazione**:
   - Engagement preventivo M+3-M+6 con Regione per chiarire fattispecie
   - Pre-application meeting + parere informale ARPAL prima della submission formale
   - Eventuale chiusura pre-emptive con percorso semplificato "Operazioni UAS sperimentali"
   - Ridurre scope Y1 (es. solo missioni emergenza PC, no missioni routine) per minimizzare profilo di rischio

---

## A.12.8 Benefici ambientali (analisi controfattuale)

Il progetto produce **benefici netti positivi** rispetto agli scenari alternativi (sorveglianza manned, pattugliamento terrestre, non-intervento):

| Beneficio | Quantificazione preliminare | Confidence |
|---|---|---|
| Riduzione emissioni CO₂ vs elicottero manned | **-99% emissioni operative** (130 kg vs 24.000 kg CO₂/anno) | high |
| Riduzione emissioni CO₂ vs pattugliamento terrestre 4×4 | **-80%** (130 kg vs 720 kg CO₂/anno) | high |
| Antincendio precoce → riduzione superfici bruciate | Stima -10-20% incendi controllati in early detection (letteratura DJI Wildfire reports) | medium |
| Monitoraggio frane → riduzione danni patrimoniali | €5-20M/anno per Liguria interna (stima conservativa, vedi Cap. 7 §7.11) | low-medium |
| Vigilanza anti-bracconaggio Parco Antola | Convenzione Ente Parco — beneficio gestionale | medium |
| Monitoraggio biodiversità (specie chiave) | Possibile servizio ricerca scientifica Università Genova / CNR | medium |

**Bilancio ambientale netto Y1 pilota**: **fortemente positivo** in chiave cost-benefit ambientale (impatti residui contenuti, benefici cumulativi rilevanti).

---

## A.12.9 Engagement plan e governance ambientale

### A.12.9.1 Stakeholder ambientali e ruoli

| Stakeholder | Ruolo | Touchpoint | Owner Firmamento |
|---|---|---|---|
| **Regione Liguria DG Ambiente** | Autorità competente VIA regionale | Submission screening + audience tecnica | environmental-consultant + government-affairs |
| **ARPAL — Agenzia Regionale Protezione Ambiente Liguria** | Supporto tecnico Regione + monitoraggio | Consultazione ante-submission + monitoraggio rumore/aria | environmental-consultant |
| **Ente Parco Naturale Regionale Antola** | Gestore SIC/ZSC/ZPS + parere VIncA | Convenzione operativa + accesso mappe nidi | Firmamento ops + environmental-consultant |
| **Comune di Torriglia (Pentema)** | Autorità locale + accettabilità sociale | Workshop pubblico + autorizzazioni edilizie | community-engagement |
| **CAP Holding / IRETI** | Gestore Diga Brugneto | Coordinamento protocollo sorvolo | safety-engineer |
| **Autorità di Bacino Distrettuale Appennino Settentrionale** | Pianificazione acque | Parere informativo | environmental-consultant |
| **Soprintendenza Archeologia Belle Arti Paesaggio Liguria** | Vincolo paesaggistico | Solo se opzione B hangar | architect-consultant |
| **Federcaccia + Federazione Italiana Caccia Liguria** | Stakeholder venatorio (uso parco autunno) | Coordinamento periodo venatorio | community-engagement |
| **Università Genova + CNR-IBE** | Scienza biodiversità | Potenziale partnership monitoraggio | tech-transfer |

### A.12.9.2 Calendario engagement M+3 → M+12

| Mese | Azione | Stakeholder |
|---|---|---|
| **M+3** | Lettera informale + invio A.12 v2.0 | Regione Liguria + Ente Parco + ARPAL |
| **M+4** | Meeting tecnico (workshop tavola rotonda) | Regione + ARPAL + Ente Parco + Comune Torriglia |
| **M+5** | Bozza convenzione Firmamento ↔ Ente Parco | Ente Parco |
| **M+6** | Acquisizione mappa nidi + dati formulario Natura 2000 + condivisione documenti | Ente Parco |
| **M+7** | Pre-application meeting screening VIA + VIncA | Regione Liguria + ARPAL |
| **M+8** | Pareri informali Soprintendenza + CAP Holding | Soprintendenza + CAP Holding |
| **M+9** | **Submission formale** screening VIA + screening VIncA | Regione Liguria |
| **M+9** | Workshop pubblico Pentema (DPIA + accettabilità + ambiente combinati) | Comunità Pentema + Pro Loco |
| **M+10** | Risposte a richieste integrazioni Regione | Regione + ARPAL |
| **M+12** | Esito attesi pareri preliminari | Regione + Ente Parco |

---

## A.12.10 Outlook Percorso 6B HALE stratosferico

Per il Percorso 6B (HALE solare a 20 km di quota), il quadro VIA è **molto diverso**:

| Componente | 6A VTOL Pentema | 6B HALE |
|---|---|---|
| Rumore al suolo | 45-55 dB(A) | < 30-35 dB(A) (impercettibile da 20 km) |
| Emissioni operative | ~130 kg CO₂/anno | **ZERO** (100% solare a regime; manufacturing separato) |
| Impatto avifauna | Medio (mitigabile) | Trascurabile (HALE opera ben oltre quota uccelli) |
| Impatto paesaggio | Basso | Trascurabile (HALE non visibile da terra) |
| Impatto stratosferico | n/a | **Nuovo dominio** — interazioni con aviazione commerciale, satelliti LEO, frammenti dopo end-of-life |
| Impatto cumulativo costellazione | n/a | Da valutare (multi-HALE → impatti new) |
| Procedure VIA | Screening regionale | **VIA EU + ICAO + EASA HAPS framework** (orizzonte 2030+) |
| Procedure VIncA | Screening SIC/ZSC/ZPS | Non applicabile a quote stratosferiche |

**Conclusione 6B**: il Percorso HALE richiede una **VIA dedicata di nuova generazione** in coordinamento con framework EU HAPS (RMT EASA atteso 2027-2029) — vedi Cap. 5 §5.10. La presente Relazione A.12 v2.0 **NON copre il Percorso 6B**.

---

## A.12.11 Conclusioni preliminari

### A.12.11.1 Verdetto preliminare

1. **Procedura VIA applicabile**: **Verifica di Assoggettabilità (screening art. 19 D.Lgs. 152/2006 + L.R. Liguria 32/2012)** — *NON VIA piena* attesa
2. **Procedura VIncA applicabile**: **Screening VIncA (Livello I)** ex DPR 357/1997 + L.R. Liguria 28/2009 per SIC/ZSC/ZPS IT1331402
3. **Esito atteso**: **NON ASSOGGETTABILITÀ a VIA + ASSENZA INCIDENZA SIGNIFICATIVA** con applicazione integrale delle mitigazioni proposte in §A.12.6
4. **Confidence verdetto aggregato**: ***medium (≈60-70%)*** — variabile critica = interpretazione Regione Liguria + Ente Parco

### A.12.11.2 Gap residui pre-istruttoria

| Gap | Azione richiesta | Owner | Scadenza |
|---|---|---|---|
| Mappa nidi specie Allegato I | Acquisizione formale Ente Parco | environmental-consultant | M+6 |
| Formulario standard Natura 2000 IT1331402 aggiornato | Estrazione database MASE + verifica Regione | environmental-consultant | M+5 |
| Conferma classificazione acustica Comune Torriglia | Richiesta formale + Piano Classificazione | environmental-consultant | M+5 |
| Modello predittivo propagazione rumore | Affidamento studio acustico specialistico | environmental-consultant | M+8 |
| Parere informale ARPAL | Pre-application meeting | environmental-consultant + Firmamento | M+7 |
| Convenzione Ente Parco bozza | Trattativa | Firmamento + Ente Parco | M+9 |
| Protocollo CAP Holding Diga Brugneto | Coordinamento tecnico | safety-engineer | M+9 |
| Eventuali rilievi field bioacustica ante-operam | Decisione su esecuzione | environmental-consultant + science partner | M+10 |
| Studio Impatto Ambientale completo (se VIA piena richiesta) | Affidamento + redazione | environmental-consultant + SIA specialist | contingent M+12+ |

### A.12.11.3 Falsifying observations

Triggeranno re-baselining significativo:

1. **Ente Parco Antola impone moratoria mar-lug totale** → peak antincendio Y1 compromesso → reset modello operativo
2. **Regione Liguria richiede VIA piena** → slittamento +6-18 mesi, costi +€30-100k, gate M+11 a rischio
3. **Identificazione nidi attivi aquila reale in corridoi operativi prioritari** → riconfigurazione completa rotte
4. **ARPAL contesta superamento limiti acustici post-monitoraggio** → riduzione operatività -10-40%
5. **Incidente con specie protetta (bird-strike specie Allegato I)** → sospensione operativa + indagine ENAC + danno reputazionale

### A.12.11.4 Caveat di chiusura

**La presente Relazione VIA Preliminare v2.0 è documento *preliminary-grade* destinato a istruttoria Regione Liguria. NON costituisce uno Studio di Impatto Ambientale (SIA) completo né una Relazione di Incidenza Appropriata completa. Qualora le autorità competenti richiedano tali documenti formali, la presente relazione costituisce baseline preliminare da integrare con: rilievi field dedicati (avifauna nidificante con metodologia EBCC, bioacustica, fonometria L. 447/1995 in continuo), modelli di propagazione validati, mappatura GIS dettagliata, accordi formali con Ente Parco + ARPAL + gestori risorse.**

**Confidence aggregato documento: medium.** **Caveat operativo per progetto**: la presente versione **non è sufficiente per chiusura gate M+10/M+11 senza pareri preliminari favorevoli** Regione Liguria + Ente Parco; queste due risposte rappresentano **condizioni necessarie** per Go Condizionato Percorso 6A.

---

## A.12.12 Linkage al resto dello Studio di Fattibilità

| Riferimento | Linkage |
|---|---|
| **Cap. 1 §1.2.2 – §1.2.3** | Inquadramento territoriale Pentema + caratteristiche orografiche |
| **Cap. 2 §2.1** | Stakeholder S-04 Regione Liguria + S-05 Comune Torriglia + S-26 Ente Parco Antola |
| **Cap. 3 §3.x — RTM** | Requisito ambientale REQ-NF-AMB-01 (nuovo, proposto in questa relazione) |
| **Cap. 5 §5.0bis + §5.16** | Quadro normativo ambientale (TUA, Habitat, Uccelli, L.R. Liguria) |
| **Cap. 6 §6.x** | Trade study profili volo (DOCFAP) → input quote operative e mitigazioni rumore |
| **Cap. 7 §7.11** | ESG e benefici ambientali quantificati |
| **Cap. 9 §9.x** | Gate decisionali M+6 / M+9 / M+10 → milestone ambientali |
| **Allegato A.1 RTM** | Tracciabilità REQ-NF-AMB-01 → VRD-AMB-01 + VRD-AMB-02 |
| **Allegato A.2 Risk Register** | RSK-REG-011 (esistente) + RSK-REG-024 (esistente) + RSK-AMB-001/002/003 (nuovi proposti) |
| **Allegato A.5 V&V Plan** | Verifica conformità ambientale (V_AMB pacchetto) |
| **Allegato A.9 CME** | Hangar Pentema opzione A vs B (input qui A preferita) |
| **Allegato A.10 Piano Manutenzione** | Procedure ambientali + recovery + bird-strike reporting |
| **Allegato A.11 Safety Case SORA** | Ground Risk + Air Risk + ambientale interfacciato |
| **Allegato A.13 Documentazione fotografica** | Stato dei luoghi ante-operam + mappature sensibilità |

---

## A.12.13 Riferimenti normativi e tecnici

### A.12.13.1 Normativa primaria

- **D.Lgs. 152/2006** (Testo Unico Ambientale) Parte II — art. 19 (Verifica di Assoggettabilità) + Allegati II/III/IV/V
- **D.Lgs. 104/2017** — Recepimento Direttiva 2014/52/UE su VIA
- **DPR 357/1997** — Recepimento Direttiva Habitat 92/43/CEE + Allegati G/H VIncA
- **L. 394/1991** — Legge quadro Aree Protette
- **L. 447/1995** — Legge quadro inquinamento acustico
- **DPCM 14/11/1997** — Limiti emissioni acustiche per zona
- **L. 353/2000** — Incendi boschivi
- **D.Lgs. 42/2004** — Codice dei Beni Culturali e del Paesaggio (Codice Urbani)
- **R.D. 3267/1923** — Vincolo idrogeologico
- **DPR 31/2017** — Autorizzazione paesaggistica semplificata
- **D.Lgs. 36/2023 art. 41 + Allegato I.7** — PFTE incluse Relazioni specialistiche ambientali

### A.12.13.2 Normativa regionale Liguria

- **L.R. Liguria 12/1995** — Istituzione Parco Naturale Regionale dell'Antola
- **L.R. Liguria 32/2012** — Procedure VIA regionali
- **L.R. Liguria 28/2009** — Valutazione d'Incidenza (recepimento DPR 357/1997)
- **L.R. Liguria 12/1998** — Tutela ambiente da inquinamento acustico
- **L.R. Liguria 38/1998** — Disciplina VIA regionale (precedente, parzialmente abrogata)
- **L.R. Liguria 22/2009** — Disciplina caccia (interfaccia uso territorio)

### A.12.13.3 Direttive EU

- **Direttiva 92/43/CEE** — Habitat (allegati I, II, IV, V)
- **Direttiva 2009/147/CE** — Uccelli (precedente 79/409/CEE)
- **Direttiva 2014/52/UE** — VIA aggiornata
- **Direttiva 2000/60/CE** — Acque
- **Direttiva 2002/49/CE** — Rumore ambientale

### A.12.13.4 Linee guida tecniche

- **MATTM/MASE 2019** — Linee guida nazionali Valutazione di Incidenza
- **ISPRA** — Manuali e linee guida VIA + VIncA
- **EBCC** — Metodologie standard di censimento avifauna
- **ISO 9613-2** — Propagazione acustica all'aperto
- **NASA SE Handbook Rev 2** — gate-driven (metodologia ingegneristica)

### A.12.13.5 Documentazione consultata

- Formulario standard Natura 2000 IT1331402 (estrazione richiesta in istruttoria)
- Piano del Parco Antola — Ente Parco Antola (versione vigente da verificare)
- Atlante Avifauna Nidificante Liguria (riferimento bibliografico)
- Catasto Incendi Boschivi Comune Torriglia
- Piano di Classificazione Acustica Comune Torriglia (verifica disponibilità)
- Rapporto SNAI Antola Tigullio 2021-2027

---

**Documento redatto da**: environmental-consultant (consulente ambientale Firmamento Technologies)
**Revisione**: red-team-skeptic (epistemic-rigor check)
**Data**: 17 maggio 2026
**Versione**: 2.0 (sostituisce v1.0 desk del 17 maggio 2026)
**Distribuzione interna**: project-manager, government-affairs, safety-engineer, flight-ops
**Distribuzione esterna proposta (post-revisione)**: Regione Liguria DG Ambiente, ARPAL, Ente Parco Antola, Comune Torriglia (lettera accompagnatoria M+3)
