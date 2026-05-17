# Allegato A.12 Relazione VIA Preliminare (versione completa v2.0)

> **Volume 2, Allegato A.12, Studio di Fattibilità HALE Firmamento Technologies**
> **Caso pilota**: Percorso 6A, VTOL JOUAV CW-30E, frazione Pentema (Torriglia, GE)
> **Riferimento normativo**: D.Lgs. 152/2006 Parte II (TUA) art. 19 e Allegato IV; DPR 357/1997 (recepimento Direttiva Habitat); L. 394/1991 Aree Protette; L.R. Liguria 12/1995 (Parco Antola); L.R. Liguria 32/2012 (procedure VIA regionali); Direttiva 92/43/CEE; Direttiva 2009/147/CE; L. 447/1995 (rumore); D.Lgs. 42/2004 (Codice Urbani); R.D. 3267/1923 (vincolo idrogeologico)
> **Versione**: 2.0, 17 maggio 2026
> **Scope**: Percorso 6A VTOL pilota Pentema (Y1). Percorso 6B HALE in §A.12.10 (outlook).
> **Stato**: documento *preliminary-grade* per **istruttoria Regione Liguria DG Ambiente, Ente Parco Antola, ARPAL**.

---

## Caveat fondamentale

Il presente documento è una **Relazione VIA preliminare** redatta a livello desk, con tre finalità:

1. supportare la **verifica di assoggettabilità** (screening) ai sensi dell'**art. 19 D.Lgs. 152/2006** e della L.R. Liguria 32/2012;
2. avviare lo **screening di Valutazione di Incidenza Ambientale (VIncA)** ex Allegato G DPR 357/1997 per il SIC/ZSC/ZPS IT1331402 "Parco Naturale dell'Antola";
3. fornire una base di discussione tecnica con Regione Liguria, Ente Parco Antola, ARPAL e Comune di Torriglia.

Il documento **non sostituisce** uno **Studio di Impatto Ambientale (SIA)** completo né una **Relazione di Incidenza completa** ex Allegato G/H DPR 357/1997. Qualora la Regione Liguria, nell'istruttoria di screening, ritenga il progetto assoggettabile a **VIA piena** o a **Valutazione di Incidenza appropriata**, la presente relazione costituisce baseline preliminare da integrare con rilievi di campo (avifauna nidificante, fonometria, bioacustica), modellazione di propagazione del rumore, mappatura GIS dei nidi noti e accordi formali con l'Ente Parco.

**Confidence aggregato del documento**: *medium*. Le assunzioni territoriali e di habitat poggiano su fonti pubbliche (SIC database, L.R. Liguria, Piano del Parco Antola), senza alcun rilievo in situ. La presente versione si dichiara espressamente come baseline iniziale, soggetta a revisione post-consultazione formale (M+6 / M+9).

---

## A.12.1 Inquadramento del progetto

### A.12.1.1 Soggetto proponente e finalità

| Voce | Dato |
|---|---|
| Proponente | Firmamento Technologies S.r.l. (società cooperativa in costituzione) |
| Capofila operativo pilota | Coop Fabrica (Legacoop Liguria) |
| Finalità | Erogazione **servizi pubblici e cooperativi** di monitoraggio EO, antincendio, supporto Protezione Civile e connettività complementare alle Aree Interne |
| Modello di business | Operatore di servizi (non OEM), vendita ore-volo e capacity wholesale |
| Sito pilota | Frazione **Pentema**, Comune di **Torriglia (GE)**, Liguria, Area SNAI Antola Tigullio |
| Bando | Cooding Prototypes 2025-26 (Coopfond / Legacoop) |
| Stato progetto | Studio di Fattibilità (Gate M+10/M+11), Fase 1 operativa M+12/M+24 |

### A.12.1.2 Descrizione tecnica delle operazioni VTOL

La piattaforma di riferimento è il **JOUAV CW-30E** Hybrid VTOL (alternative analoghe in *Allegato A.3 Trade Study TS-002*).

| Parametro | Valore | Note |
|---|---|---|
| MTOM | **< 25 kg** (Open/Specific EASA) | Classe acustica regolare Reg. UE 2019/945 |
| Apertura alare | ~3,5 m | UAS ala fissa con VTOL elettrico |
| Propulsione | **Ibrida**: 4 motori elettrici VTOL + 1 motore termico cruise (benzina) | Generatore on-board ricarica batterie |
| Quota operativa | **100-400 m AGL** (BVLOS Specific Category) | Min. 200 m AGL su perimetro SIC come da mitigazione §A.12.6 |
| Velocità cruise | 60-110 km/h | Endurance 6-8 h con tank pieno |
| Rumore di riferimento | **65-75 dB(A) @ 100 m** in cruise; **75-80 dB(A) @ 25 m** in fase VTOL | Fonte: scheda tecnica costruttore + benchmark EASA UAS |
| Emissioni CO₂ | **~0,4-0,7 kg CO₂/h fly** (motore termico ibrido, ~85% del tempo in cruise elettrico-assistito) | Benchmark vs Cessna 172 manned: ~30 kg CO₂/h |

Il profilo di missione tipico prevede decollo VTOL dall'elipiazzola di Pentema (~150 m² di area sgombera, su suolo già antropizzato, piazzale comunale o terreno cooperativa), salita a quota cruise (200-400 m AGL), pattuglia/sorveglianza su rotte pianificate (corridoi predefiniti che evitano i nidi noti, vedi §A.12.6), atterraggio VTOL sull'elipiazzola. La durata media della missione è di 2-4 ore.

**Frequenza operativa Y1 (anno pilota)**:
- **Target**: 80 missioni/anno (~1,5/settimana media)
- **Minimo bandabile**: 50 missioni/anno (~1/settimana)
- **Distribuzione stagionale**:
 - Inverno (dic-feb): missioni dimostrative e monitoraggio neve/frane (~10-15 missioni)
 - Primavera (mar-mag): **periodo critico di nidificazione avifauna**, ridotte +30% per buffer cautelativo (~10-15 missioni)
 - Estate (giu-set): **peak antincendio AIB**, priorità protezione civile (~35-45 missioni)
 - Autunno (ott-nov): monitoraggio frane post-pioggia e caccia (engagement Federcaccia) (~10-15 missioni)
- **Orario**: prevalentemente **diurno** (sunrise / sunset). Operazioni notturne (twilight e notte) **solo per emergenze Protezione Civile** (incendi, frane, ricerca persone) con buffer 500 m dai centri abitati.

L'infrastruttura ground prevede un hangar di Pentema in affitto o comodato su edificio esistente (CME Allegato A.9 opzione A, confidence high di disponibilità ~70%, vedi rischio RSK-OPS-009), così da evitare il consumo di suolo. Il backup (opzione B) è un light build < 100 m² su terreno già edificabile (fuori area SIC e fuori area vincolata sotto profilo paesaggistico). La Ground Station è mobile (container 20' o veicolo dedicato, parcheggio piazzale comunale Pentema). Le antenne C2 e payload sono al massimo due, pole-mount con altezza < 6 m, senza opere fondali permanenti.

**Confidence inquadramento progetto**: *high* (basato su TS-002 + RFQ JOUAV documentato).

---

## A.12.2 Inquadramento territoriale e ambientale

### A.12.2.1 Localizzazione e morfologia

| Parametro | Valore |
|---|---|
| Coordinate baricentriche | 44°31'N, 9°10'E (approx.) |
| Altitudine | 1100-1300 m s.l.m. (versante settentrionale Monte Antola, 1597 m) |
| Comune | Torriglia, Città Metropolitana di Genova |
| Bacino idrografico | Bacini Trebbia e Pentemina (affluenti Po) |
| Esposizione | Versante Nord-Nord-Est, pendenze 30-60% |
| Geomorfologia | Versanti franosi, copertura forestale prevalente (faggete e castagneti) |
| Clima | Montano-appenninico: precipitazioni 1500-2000 mm/anno, neve 1-3 mesi/anno |
| Popolazione | **14 abitanti ISTAT** (residenti permanenti); incremento turistico stagionale (Presepe di Pentema dicembre + escursionismo) |

### A.12.2.2 Vincoli ambientali e paesaggistici applicabili

Quadro sinottico dei vincoli sull'area di operazione:

| Vincolo | Riferimento normativo | Applicabilità Pentema | Implicazioni progetto |
|---|---|---|---|
| **Parco Naturale Regionale dell'Antola** | L.R. Liguria 12/1995 + Piano del Parco | **SÌ, area inclusa nel perimetro Parco** | Operazioni soggette a parere Ente Parco; Piano del Parco governance |
| **SIC/ZSC IT1331402** "Parco Naturale dell'Antola" | DPR 357/1997 (Habitat 92/43/CEE) | **SÌ, sito coincide largamente con perimetro Parco** | VIncA obbligatoria (screening minimo) |
| **ZPS IT1331578** "Parco Antola, Praglia, Pracaba, Antola..." (denominazione esatta da verificare in istruttoria) | DPR 357/1997 + Direttiva 2009/147/CE | **SÌ, area pSCI/ZPS sovrapposta o adiacente** | Tutela avifauna Allegato I Direttiva Uccelli |
| **Vincolo paesaggistico** ex D.Lgs. 42/2004 art. 142 | Codice Urbani, territori montani > 1600 m, fasce 300 m da corsi d'acqua, boschi | **SÌ parziale, aree boscate e > 1600 m solo parte Monte Antola** | Il sorvolo non costituisce attività edilizia; eventuali hangar light-build richiedono autorizzazione paesaggistica |
| **Vincolo idrogeologico** | R.D. 3267/1923 | **SÌ, quasi totalità dei versanti Pentema** | Nessuna opera fondale permanente su pendio; preferenza opzione A affitto edificio esistente |
| **Vincolo acque pubbliche / Diga del Brugneto** | TUA Parte III + concessioni CAP Genova | **SÌ, bacino imbrifero Brugneto a ~5-8 km** | Cautela sorvolo: nessuna operazione sopra specchio d'acqua a quote inferiori a 200 m AGL; coordinamento gestore CAP Holding |
| **IBA (Important Bird Area)** | BirdLife, non vincolante ma indicatore | Verifica IBA Antola Atlanti in istruttoria | Documento di sensibilità avifaunistica |
| **Aree percorse dal fuoco (L. 353/2000)** | Catasto incendi boschivi comunali | Verifica documenti Comune Torriglia | Eventuali vincoli decennali post-incendio |
| **Aree archeologiche** | D.Lgs. 42/2004 Parte II | Nessuna nota in area immediata Pentema | Nessun impatto atteso |

### A.12.2.3 Parco Naturale Regionale dell'Antola

Inquadramento (L.R. Liguria 12/1995): il Parco è stato istituito nel 1995, con modifiche L.R. successive, copre circa 4.700 ha e include i Comuni di Torriglia, Propata, Fascia, Gorreto, Rondanina e Fontanigorda. La gestione è affidata all'Ente Parco Antola (sede a Torriglia), che opera tramite Piano del Parco, Regolamento e Piani Pluriennali Socio-Economici.

La zonizzazione (riferimento Piano del Parco, da verificare nella versione vigente in istruttoria) si articola in:
- **Zona A, Riserve integrali**: tutela assoluta, attività antropiche escluse salvo ricerca scientifica autorizzata.
- **Zona B, Riserve orientate**: limitazioni alle attività antropiche, autorizzazioni specifiche.
- **Zona C, Aree di protezione**: presenza antropica tradizionale, attività agro-silvo-pastorali.
- **Zona D, Aree di promozione economica e sociale**: borghi e infrastrutture; Pentema rientra prevalentemente qui.

Implicazioni operative: hangar e ground station ricadono in Zona D (borgo Pentema) e sono ammissibili previa autorizzazione dell'Ente Parco. I corridoi di volo che attraversano le Zone A/B richiedono coordinamento con l'Ente Parco e valutazione di sensibilità dei biotopi. Lo Studio prevede una **Convenzione operativa** Firmamento-Ente Parco Antola entro M+9 (collegata a RSK-AMB-001 nuova proposta e a RSK-REG-011).

### A.12.2.4 Rete Natura 2000, SIC/ZSC e ZPS

**Sito SIC/ZSC IT1331402 "Parco Naturale dell'Antola"** (Direttiva 92/43/CEE).

Habitat di interesse comunitario presenti o potenzialmente presenti (verifica del formulario Natura 2000 in istruttoria):

| Codice habitat | Denominazione | Note |
|---|---|---|
| **9110** | Faggeti del *Luzulo-Fagetum* | Habitat prevalente versanti Pentema |
| **9130** | Faggeti dell'*Asperulo-Fagion* | Faggete neutrofile su suoli ricchi |
| **9180\*** | Foreste di versante, ghiaione e valloni del *Tilio-Acerion* | Habitat **prioritario** (\*), tutela rafforzata |
| **6210(\*)** | Formazioni erbose secche seminaturali (*Festuco-Brometalia*) | Prati montani, prioritario in presenza di siti notevoli di orchidee |
| **6510** | Praterie magre da fieno a bassa altitudine | Praterie da sfalcio |
| **8220** | Pareti rocciose silicee con vegetazione casmofitica | Affioramenti rocciosi versanti |

Specie di interesse comunitario (Allegati II e IV Direttiva Habitat 92/43/CEE):

| Specie | Categoria | Note di rilevanza per il progetto |
|---|---|---|
| **Lupo (*Canis lupus*)** | Allegato II e IV, **specie prioritaria** | Presenza accertata Appennino Ligure; disturbo da rumore VTOL ipotetico ma improbabile a 200+ m AGL diurni |
| **Capriolo (*Capreolus capreolus*)** | Allegato V (gestione) | Specie comune; disturbo trascurabile |
| **Lince eurasiatica (*Lynx lynx*)** | Allegato II e IV | Presenza non accertata, possibile passaggio |
| **Chirotteri** (*Myotis* spp., *Rhinolophus* spp.) | Allegato II e IV | Attività notturna, nessuna interferenza diretta con voli diurni VTOL |
| **Tritone alpestre (*Ichthyosaura alpestris*)** | Allegato IV | Habitat acquatici; nessuna interferenza |
| **Salamandra di Lanza (*Salamandra lanzai*)** | Allegato IV, area limite di distribuzione | Tutela alta; nessuna interferenza diretta da volo |

Specie ZPS di interesse comunitario (Allegato I Direttiva Uccelli 2009/147/CE):

| Specie | Allegato I | Stato locale | Sensibilità progetto |
|---|---|---|---|
| **Aquila reale (*Aquila chrysaetos*)** | I | Nidificante Appennino Ligure; ~2-4 coppie nel comprensorio Antola (stima Parco, da confermare con Ente Parco) | **ALTA**, buffer 500-1000 m dai nidi noti, periodo nidificazione (mar-lug) con restrizioni operative |
| **Gufo reale (*Bubo bubo*)** | I | Nidificante su pareti rocciose | **ALTA**, buffer 500 m dai nidi; attività crepuscolare/notturna, nessuna interferenza con voli diurni |
| **Pellegrino (*Falco peregrinus*)** | I | Nidificante pareti rocciose | **MEDIA**, buffer 300 m dai nidi |
| **Biancone (*Circaetus gallicus*)** | I | Migratore e possibile nidificante estivo | **MEDIA**, riduzione attività in periodo migratorio se segnalato |
| **Albanella minore (*Circus pygargus*)** | I | Migratore | **BASSA** |
| **Succiacapre (*Caprimulgus europaeus*)** | I | Nidificante a terra in radure | **MEDIA**, attività crepuscolare, nessuna interferenza con voli diurni |
| **Tottavilla (*Lullula arborea*)** | I | Praterie aperte | **BASSA** |
| **Averla piccola (*Lanius collurio*)** | I | Praterie con siepi | **BASSA** |

**Confidence inventario habitat/specie**: *medium-low*. I dati riportati poggiano su **fonti pubbliche secondarie** (formulario Natura 2000, atlanti regionali avifauna, letteratura). In fase istruttoria si dovranno acquisire l'estrazione del formulario standard Natura 2000 IT1331402, la mappa dei nidi noti dall'Ente Parco Antola e la lista aggiornata delle specie.

### A.12.2.5 Diga del Brugneto e risorsa idrica

La Diga del Brugneto, ad arco-gravità, insiste sul torrente Brugneto (affluente Trebbia) nel Comune di Rondanina (GE). Ha una capacità utile di circa 25 milioni di m³ e costituisce la riserva idropotabile primaria dell'area metropolitana di Genova. Il gestore è **CAP Holding S.p.A. / IRETI** (verifica del gestore in istruttoria, possibile cambiamento di gestione). La distanza dal sito di Pentema è di 5-8 km in linea d'aria, su versante adiacente.

Implicazioni per il progetto:
- il sorvolo dello specchio d'acqua è ammesso a quota ≥ 200 m AGL come da buffer cautelativo (vedi §A.12.6); è da evitare l'hovering sul lago salvo emergenze di Protezione Civile;
- il rischio di crash UAV in lago presenta probabilità < 1 evento / 1.000 ore di volo (target SORA SAIL II-III), e richiede protocollo di recovery e parere CAP Holding sul rischio di inquinamento da carburante residuo (massimo 3-5 L di benzina a bordo VTOL ibrido);
- è necessario il coordinamento con il **gestore diga** e con l'**Autorità di Bacino Distrettuale Appennino Settentrionale** (parere informativo).

### A.12.2.6 Stato acustico ante-operam

Pentema è zona prevalentemente silente, in ambiente rurale montano isolato. La classificazione acustica comunale (Comune di Torriglia, Piano di Classificazione Acustica ex L.R. Liguria 12/1998) si articola in due classi rilevanti per l'area:
- **Classe I, Aree particolarmente protette** (parchi e riserve naturali, scolastiche, sanitarie), applicabile alle aree SIC interne al Parco Antola;
- **Classe II, Aree prevalentemente residenziali**, riferita al borgo di Pentema.

Limiti di immissione (DPCM 14/11/1997 e L.R. 12/1998):

| Classe | Diurno (06:00-22:00) | Notturno (22:00-06:00) |
|---|---|---|
| I | **50 dB(A)** | **40 dB(A)** |
| II | 55 dB(A) | 45 dB(A) |

Il livello sonoro a terra durante le operazioni VTOL deve restare sotto **50 dB(A) diurni e 40 dB(A) notturni** quando l'immissione interessa la Zona Classe I. La stima 65-75 dB(A) @ 100 m del VTOL implica che a 200-300 m AGL in cruise il rumore al suolo si attesta intorno ai 45-55 dB(A) (attenuazione geometrica più parziale assorbimento atmosferico). Lo Studio richiede pertanto **monitoraggio fonometrico** in Y1 su 3 punti rappresentativi (vedi §A.12.6).

---

## A.12.3 Identificazione e valutazione degli impatti potenziali

Per ogni fattore ambientale si esplicitano descrizione, stima della magnitudine, classe (basso / medio / alto), **confidence** e mitigazioni.

### A.12.3.1 Atmosfera (aria, emissioni, clima)

Le sorgenti significative sono il motore termico ibrido VTOL (benzina, ~0,4-0,7 kg CO₂/h fly) e, in misura trascurabile per il pilota, l'eventuale generatore back-up della GS. I trasporti logistici a terra (van di supporto) restano fuori dal perimetro VIA.

Stima delle emissioni Y1: 80 missioni × 3 h media producono 240 ore di volo/anno; 240 h × 0,55 kg CO₂/h danno circa 130 kg CO₂/anno (centesimi rispetto a un'auto diesel media, intorno a 2.000 kg/anno per 15.000 km).

Confronto con le alternative:
- sorveglianza con elicottero manned (Eurocopter EC120): ~100 kg CO₂/h, su 240 h produrrebbe 24.000 kg CO₂/anno (circa 180× peggio);
- sorveglianza con drone elettrico puro (es. M300): emissioni zero in volo, autonomia 30-40 min insufficiente per BVLOS estese;
- pattugliamento gomma (4×4 Forestale): ~0,18 kg CO₂/km × 50 km/giorno × 80 missioni produce circa 720 kg CO₂/anno più il costo del personale.

**Magnitudine impatto**: **BASSO** (assoluto trascurabile, fortemente favorevole rispetto alle alternative).
**Confidence**: *high* (calcoli standard fattori emissione ISPRA).

### A.12.3.2 Acque (idrosfera)

Gli impatti diretti operativi sono nulli (volo aereo, nessuno scarico). Gli impatti indiretti riguardano il sorvolo della Diga del Brugneto (rischio inquinamento da carburante in caso di crash, circa 3-5 L di benzina; probabilità target SORA < 10⁻⁴/h volo) e l'eventuale impermeabilizzazione dell'hangar (opzione B light build), con gestione delle acque meteoriche secondo standard delle pavimentazioni.

Mitigazioni:
- buffer ≥ 500 m laterali dallo specchio d'acqua del Brugneto in operazioni di routine;
- sorvolo del Brugneto consentito solo per emergenze PC, con quota ≥ 200 m AGL;
- protocollo di emergency recovery in caso di crash (briefing CAP Holding e Vigili del Fuoco).

**Magnitudine impatto**: **TRASCURABILE-BASSO**.
**Confidence**: *medium* (richiede formalizzazione del protocollo CAP Holding).

### A.12.3.3 Suolo (geosfera e uso del suolo)

L'impatto operativo aereo è nullo (nessun consumo). Sul fronte dell'infrastruttura ground:
- **Opzione A preferita**: affitto o comodato di edificio esistente a Pentema, con **consumo di suolo zero** e nessuna nuova impermeabilizzazione (confidence disponibilità ~70%).
- **Opzione B fallback**: light build hangar < 100 m², impatto contenuto (~150 m² complessivi con piazzale), su terreno già edificabile fuori SIC e fuori da vincolo paesaggistico stringente.
- **Elipiazzola decollo VTOL**: utilizzo del piazzale comunale o di pista esistente, consumo di suolo zero.

Il vincolo idrogeologico R.D. 3267/1923 interessa quasi tutti i versanti di Pentema: l'opzione B richiede pertanto **autorizzazione vincolo idrogeologico** della Regione Liguria (Settore Difesa Suolo). La mitigazione coincide con la preferenza per l'opzione A.

**Magnitudine impatto**: **TRASCURABILE** (opzione A) o **BASSO** (opzione B).
**Confidence**: *medium-high*.

### A.12.3.4 Biodiversità, Fauna

#### Avifauna (impatto principale)

Le tipologie di disturbo rilevanti sono:
1. **Disturbo acustico**: 45-55 dB(A) al suolo a quota cruise 200-400 m AGL.
2. **Disturbo visivo**: oggetto in movimento percepibile dai raptor territoriali come potenziale competitor o predatore.
3. **Rischio collisione**: probabilità bassa per VTOL a quote 100-400 m AGL (sotto la maggior parte delle rotte migratorie principali; il corridoio Alpi Marittime / Stretto di Bonifacio è laterale). La letteratura indica meno di 0,1 incidenti / 100 ore di volo per piccoli UAS in aree montane (fonte: ricerche Sentinel e database bird-strike ENAC).
4. **Disturbo nidificazione**: critico nel **periodo riproduttivo (marzo-luglio)** per le specie sensibili:
 - **Aquila reale** (incubazione marzo-aprile, allevamento maggio-luglio), pari a 4-5 mesi di sensibilità acuta
 - **Gufo reale** (incubazione gennaio-aprile)
 - **Pellegrino** (incubazione marzo-maggio)
 - **Biancone** (incubazione aprile-giugno)

Stima della magnitudine:
- in assenza di mitigazioni il rischio è **MEDIO-ALTO** per il disturbo dell'aquila reale (specie iconica, con nidi noti potenzialmente in area corridoio volo);
- con le mitigazioni di §A.12.6 (buffer 500-1000 m dai nidi noti, riduzione +30% missioni mar-lug, quota minima 200 m AGL su SIC) il rischio atteso scende a **BASSO**.

**Confidence**: *medium-low*. Tutto dipende criticamente dall'acquisizione della **mappa dei nidi noti** dall'Ente Parco Antola (azione M+6); senza la mappa ogni stima resta teorica.

#### Mammiferi (lupo, ungulati, mesomammiferi)

Il disturbo acustico per il lupo: specie con elevata tolleranza al disturbo antropico in assenza di minaccia diretta; la letteratura indica che voli aerei a > 200 m AGL non producono displacement significativo (cfr. studi su lupi a Yellowstone e nell'Appennino Centrale). Per capriolo, cinghiale e daino il disturbo a quote operative resta trascurabile.

**Magnitudine impatto**: **BASSO**.
**Confidence**: *medium*.

#### Chirotteri (pipistrelli)

Il VTOL diurno non interferisce con l'attività crepuscolare/notturna dei chirotteri.
**Magnitudine impatto**: **TRASCURABILE**.
**Confidence**: *high*.

#### Erpetofauna ed entomofauna

Nessun impatto da volo aereo a quote di operazione.
**Magnitudine impatto**: **TRASCURABILE**.
**Confidence**: *high*.

### A.12.3.5 Vegetazione e habitat

L'impatto diretto su habitat è nullo: l'operazione resta aerea, senza contatto fisico con suolo o vegetazione (escluse le zone elipiazzola, già antropizzate). Le faggete 9110 / 9130 / 9180* (prioritario) e le praterie 6210 / 6510 non subiscono alcun impatto fisico. L'impatto indiretto è trascurabile (nessun atterraggio su habitat naturali, nessuna emissione di gas tossici significativa, nessuna infiltrazione di idrocarburi).

**Magnitudine impatto**: **TRASCURABILE**.
**Confidence**: *high*.

### A.12.3.6 Paesaggio

L'impatto strutturale dipende dall'opzione di hangar: l'opzione A non aggiunge alcuna struttura, mentre l'opzione B (hangar light build < 100 m² e 2 antenne pole-mount h < 6 m) produce un impatto visivo molto contenuto, mitigabile con finiture compatibili (legno, verde militare).

L'impatto visivo da volo è limitato: a quota 200-400 m AGL il VTOL ha dimensione apparente di 0,5-1 cm a vista nuda dal suolo, percepibile ma non invasivo. Il sorvolo su un dato punto in cruise è transitorio (60-90 secondi) e la frequenza di circa 1,5 missioni/settimana mantiene basso l'impatto cumulativo.

Il vincolo paesaggistico ex D.Lgs. 42/2004 richiede autorizzazione paesaggistica semplificata (DPR 31/2017) per l'opzione B; l'opzione A non richiede alcuna autorizzazione paesaggistica aggiuntiva.

**Magnitudine impatto**: **BASSO**.
**Confidence**: *medium-high*.

### A.12.3.7 Rumore (clima acustico)

Modello preliminare di propagazione (semplificato):

| Quota AGL | Rumore stimato al suolo direttamente sotto | Note |
|---|---|---|
| 100 m | ~65 dB(A) | Solo in fasi VTOL decollo/atterraggio sopra elipiazzola |
| 200 m | ~55-58 dB(A) | Cruise minimo |
| 300 m | ~50-52 dB(A) | Cruise nominale |
| 400 m | ~46-48 dB(A) | Cruise alto |

Modello: $L_p = L_p(d_0) - 20 \log_{10}(d/d_0) - \alpha \cdot d$, con $L_p(d_0=100m)=65$ dB(A) e $\alpha\approx 0{,}005$ dB/m (assorbimento atmosferico standard).

Confronto con i limiti di L. 447/1995, DPCM 14/11/1997 e L.R. Liguria 12/1998:

| Punto recettore | Classe | Limite diurno | Stima impatto cruise 300 m AGL | Verdetto |
|---|---|---|---|---|
| Borgo Pentema (residenze) | II | 55 dB(A) | 50-52 dB(A) | **OK** (< limite) |
| Aree SIC interne Parco | I | 50 dB(A) | 50-52 dB(A) | **borderline**, quota ≥ 250-300 m AGL su SIC |
| Aree esterne Parco | III | 60 dB(A) | < 55 dB(A) | OK |

Per le operazioni notturne il limite I/II di 40/45 dB(A) rende il cruise VTOL non compatibile salvo emergenze PC con deroga puntuale.

**Magnitudine impatto**: **BASSO-MEDIO** (mitigabile con quote operative e scheduling).
**Confidence**: *medium* (richiede una campagna fonometrica field in Y1 su 3 punti di misura, vedi §A.12.6).

### A.12.3.8 Salute umana

Gli impatti potenziali si distribuiscono su rumore (vedi §A.12.3.7, sotto soglia di disturbo cronico), EMI (le trasmissioni C2 e payload operano a potenze di decine di mW, ben sotto i limiti ICNIRP per esposizione popolazione), rischio incidentale di crash UAV su persone (target SORA SAIL II-III, *Ground Risk* dopo mitigazioni < 10⁻⁶/h volo) e operatori a terra ridotti (pilota remoto e visual observer, procedure SORA standard).

**Magnitudine impatto**: **TRASCURABILE-BASSO**.
**Confidence**: *high* (allineamento con A.11 Safety Case SORA).

### A.12.3.9 Patrimonio culturale e archeologico

I beni culturali noti includono il borgo storico di Pentema (architettura rurale tradizionale, non vincolato come bene puntuale ma soggetto al vincolo paesaggistico d'area), il presepe meccanico storico di Pentema (manifestazione culturale di dicembre, coordinamento eventuale con la Pro Loco) e nessun bene archeologico vincolato noto nell'area immediata delle operazioni.

Non sono attesi impatti fisici; resta un potenziale impatto **simbolico/percettivo** se l'operazione VTOL venisse percepita come intrusiva durante eventi tradizionali (es. Presepe dicembre).

**Mitigazione**: sospensione delle operazioni durante gli eventi pubblici tradizionali di Pentema (Presepe, 7-26 dicembre tipicamente) salvo emergenze PC.

**Magnitudine impatto**: **TRASCURABILE**.
**Confidence**: *high*.

### A.12.3.10 Sintesi impatti per fattore

| Fattore ambientale | Magnitudine impatto residuo (post-mitigazioni) | Confidence | Mitigazione chiave |
|---|---|---|---|
| Atmosfera (aria, clima) | Basso | high | Motore ibrido, ridotte ore volo; bilancio favorevole vs alternative |
| Acque | Trascurabile-Basso | medium | Buffer Brugneto, protocollo recovery |
| Suolo | Trascurabile (opzione A) | medium-high | Affitto edificio esistente |
| Avifauna nidificante | Basso | medium-low | **Buffer nidi, restrizioni mar-lug** (punto chiave) |
| Mammiferi | Basso | medium | Quota operativa, scheduling diurno |
| Chirotteri | Trascurabile | high | Voli diurni |
| Habitat | Trascurabile | high | Nessun contatto fisico |
| Paesaggio | Basso | medium-high | Opzione A, finiture compatibili |
| Rumore | Basso-Medio | medium | Quota minima 200-300 m AGL, scheduling, monitoraggio fonometrico |
| Salute umana | Trascurabile-Basso | high | SORA, procedure standard |
| Patrimonio | Trascurabile | high | Sospensione eventi pubblici |

**Conclusione preliminare**: impatti complessivi bassi e mitigabili con misure proporzionate.

---

## A.12.4 Valutazione di Incidenza Ambientale (VIncA) preliminare, Screening

### A.12.4.1 Quadro metodologico

La VIncA si applica a progetti potenzialmente capaci di **incidenza significativa** sui siti Rete Natura 2000 (SIC/ZSC/ZPS). Riferimenti normativi:
- **Direttiva 92/43/CEE art. 6.3**
- **DPR 357/1997 art. 5** e Allegati G/H (recepimento italiano)
- **Linee guida nazionali per VIncA** (MATTM 2019)
- **L.R. Liguria 28/2009** (recepimento e disciplina VIncA in Liguria)

La VIncA si articola in **4 livelli progressivi**:
1. **Screening (Livello I)**, *presente documento*
2. Valutazione appropriata (Livello II), se lo screening non esclude l'incidenza significativa
3. Valutazione soluzioni alternative (Livello III)
4. Misure compensative (Livello IV), solo in casi IROPI (Imperative Reasons of Overriding Public Interest)

### A.12.4.2 Identificazione siti Natura 2000 interessati

| Sito | Codice | Tipologia | Distanza/sovrapposizione |
|---|---|---|---|
| Parco Naturale dell'Antola | **IT1331402** | SIC/ZSC | **Sovrapposizione totale** con area operativa Pentema |
| Parco Naturale dell'Antola ZPS | **IT1331578** (verifica) | ZPS | Sovrapposizione totale o adiacenza stretta |
| (Eventuali altri SIC dell'Appennino Ligure adiacenti, verifica in istruttoria) | n/d | SIC/ZSC | Adiacenze < 5 km, possibile valutazione cumulativa |

### A.12.4.3 Caratterizzazione del progetto rispetto ai siti

Tipologia di interferenza:
- **Diretta fisica**: nessuna (operazione aerea, nessuna opera fondale su habitat tutelati).
- **Diretta sonora**: rumore al suolo 45-55 dB(A) su area SIC (Classe I con limite 50 dB(A)).
- **Diretta visiva**: oggetto in movimento percepibile da specie territoriali.
- **Indiretta**: minima (nessun consumo di risorse, nessuna emissione significativa).

Durata e ricorrenza:
- ogni singola missione: 2-4 ore;
- frequenza Y1: ~1,5 missioni/settimana;
- cumulativo Y1: ~240 ore di sorvolo/anno, pari al 2,7% del tempo totale annuale (240/8760 h).

### A.12.4.4 Valutazione preliminare incidenza significativa

Criteri Allegato G DPR 357/1997:

| Criterio | Valutazione preliminare |
|---|---|
| **Perdita di area di habitat** | NESSUNA, nessun consumo fisico di habitat tutelati |
| **Frammentazione habitat** | NESSUNA |
| **Perturbazione specie** (rumore, presenza) | **POTENZIALE su avifauna nidificante Allegato I**, mitigabile con buffer e restrizioni stagionali |
| **Modifica densità popolazione** | Non significativa con mitigazioni |
| **Cambiamento indicatori chiave** (acqua, qualità aria) | NESSUNO |
| **Cambiamenti climatici** | NESSUNO |

**Verdetto preliminare screening VIncA**: incidenza significativa improbabile applicando le mitigazioni proposte in §A.12.6 (in particolare buffer dai nidi di aquila reale e restrizione della stagione riproduttiva).

**Confidence verdetto**: *medium*. Tre variabili pesano:
1. acquisizione della mappa dei nidi noti dall'Ente Parco Antola (M+6);
2. eventuale rilievo bioacustico ante-operam Y1 (raccomandato);
3. conferma scientifica della densità di popolazione di aquila reale nel comprensorio Antola.

**Caveat**: qualora l'Ente Parco evidenzi nidi attivi entro buffer operativo, lo screening non è sufficiente e si attiva una **Valutazione di Incidenza Appropriata (Livello II)** con rilievi field dedicati.

### A.12.4.5 Specie target di attenzione prioritaria

**Tier 1 (attenzione alta)**:
- **Aquila reale (*Aquila chrysaetos*)**, Allegato I Uccelli
- **Gufo reale (*Bubo bubo*)**, Allegato I Uccelli
- **Lupo (*Canis lupus*)**, Allegato II e IV Habitat, specie prioritaria

**Tier 2 (attenzione media)**:
- Pellegrino, Biancone (Allegato I Uccelli)
- Chirotteri (Allegato II e IV Habitat), solo se operazioni notturne di emergenza

**Tier 3 (monitoraggio standard)**:
- Restanti specie Allegati I/II/IV non specificamente sensibili al sorvolo VTOL diurno

---

## A.12.5 Quadro di sintesi rischi ambientali e linkage Risk Register

### A.12.5.1 Rischi ambientali nel Risk Register (esistenti)

| Risk ID | Descrizione | P×I attuale | Stato |
|---|---|---|---|
| **RSK-REG-011** | VIA Pentema, ARPA Liguria richiede VIA per infrastruttura ground HALE | 2×2=4 GREEN | Monitor, VIA preliminare M+6 |
| **RSK-REG-024** | Codice Navigazione R.D. 327/1942, diritti sorvolo proprietà private e aree militari | 2×3=6 GREEN | Monitor |

### A.12.5.2 Nuovi rischi proposti

**RSK-AMB-001 (PROPOSTO)**, *Incidenza significativa avifauna nidificante in SIC/ZSC/ZPS IT1331402*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-001 |
| Categoria | Ambientale / Regolatorio |
| Descrizione | Disturbo di aquila reale e altre specie Allegato I Direttiva Uccelli nidificanti in SIC/ZSC/ZPS Parco Antola; l'Ente Parco o la Regione richiedono Valutazione di Incidenza Appropriata (Livello II) o impongono restrizioni operative stringenti (es. blocco mar-lug totale) |
| Probabilità (1-5) | 3 (medium, dipende dai nidi attivi entro 1000 m dai corridoi operativi) |
| Impatto (1-5) | 3 (medium, slittamento 6-9 mesi, €30-80k costi rilievi, riduzione operatività Y1 fino a -40%) |
| P×I | **9, AMBER** |
| Owner | environmental-consultant + Firmamento ops |
| Status | OPEN |
| Mitigation type | Mitigate + Avoid |
| Mitigazioni | 1) Acquisizione mappa nidi noti Ente Parco M+6; 2) Buffer 500-1000 m operativo dai nidi; 3) Restrizione operativa mar-lug +30% margine cautelativo; 4) Quota minima 200-250 m AGL su SIC; 5) Monitoraggio acustico Y1; 6) Eventuale rilievo bioacustico ante-operam |
| Residual P×I (post-mitigazione) | 1×2=2 GREEN |
| Trigger condition | L'Ente Parco rifiuta il parere favorevole sui corridoi operativi oppure il rilievo ante-operam evidenzia nidi attivi entro buffer |
| Falsifying observation | Se l'Ente Parco impone moratoria totale mar-lug, il modello operativo Y1 va rivisto (peak antincendio compromesso) |

**RSK-AMB-002 (PROPOSTO)**, *Inquinamento idrico Diga Brugneto in caso crash VTOL ibrido*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-002 |
| Categoria | Ambientale / Safety |
| Descrizione | Crash VTOL ibrido sopra bacino imbrifero Brugneto, sversamento 3-5 L di benzina e componenti elettrici (batterie LiPo), contestazione del gestore CAP Holding e di ARPAL |
| Probabilità (1-5) | 1 (low, target SORA crash rate < 10⁻⁴/h × buffer geografico Brugneto) |
| Impatto (1-5) | 4 (high, riserva idropotabile primaria Genova, danno reputazionale e costi di bonifica) |
| P×I | **4, GREEN** |
| Owner | safety-engineer + environmental-consultant |
| Status | OPEN |
| Mitigation type | Avoid + Mitigate |
| Mitigazioni | 1) Buffer ≥ 500 m laterali Brugneto in operazioni routine; 2) Quota ≥ 200 m AGL su lago; 3) Sorvolo solo emergenze PC; 4) Protocollo recovery con VVF; 5) Coordinamento CAP Holding entro M+9 |
| Residual P×I | 1×2=2 GREEN |
| Trigger | Singolo near-miss su bacino Brugneto |

**RSK-AMB-003 (PROPOSTO)**, *Superamento limiti acustici L. 447/1995 in punti recettori SIC Classe I*

| Campo | Valore |
|---|---|
| ID | RSK-AMB-003 |
| Categoria | Ambientale / Regolatorio |
| Descrizione | Il monitoraggio fonometrico Y1 evidenzia immissioni > 50 dB(A) diurni in aree SIC Classe I, con contestazione ARPAL e obbligo di deroga o revisione dei profili volo |
| Probabilità (1-5) | 2 (low-medium) |
| Impatto (1-5) | 2 (medium, revisione SOPs ed eventuale riduzione operatività -10/-20%) |
| P×I | **4, GREEN** |
| Owner | environmental-consultant + flight-ops |
| Status | OPEN |
| Mitigazioni | 1) Quota minima cruise 250 m AGL su SIC; 2) Modelli di propagazione ante-operam; 3) Campagna fonometrica Y1 su 3 punti; 4) Adattamento profili volo in caso di eccedenza |
| Residual P×I | 1×2=2 GREEN |

### A.12.5.3 Linkage RTM e gates

- **REQ-NF-AMB-01** (proposto in RTM): *Il sistema deve garantire compliance ambientale piena (VIA e VIncA) con la normativa italiana ed europea applicabile al sito pilota Pentema entro il gate M+9.* Verifica VRD-AMB-01 (parere screening VIA Regione Liguria favorevole) e VRD-AMB-02 (parere VIncA Ente Parco favorevole).
- Gate **M+6**: deliverable, engagement avviato con Ente Parco, Regione Liguria DG Ambiente e ARPAL.
- Gate **M+9**: deliverable, screening VIA e screening VIncA presentati e in istruttoria.
- Gate **M+10/M+11**: deliverable, pareri positivi almeno preliminari ottenuti, o trigger di re-baselining.

---

## A.12.6 Mitigazioni proposte

### A.12.6.1 Pacchetto mitigazioni avifauna (priorità massima)

| # | Mitigazione | Frequenza | Costo stimato | Confidence efficacia |
|---|---|---|---|---|
| M-AVI-01 | Acquisizione mappa nidi noti specie Allegato I (aquila reale, gufo reale, pellegrino, biancone) da Ente Parco Antola | Una-tantum M+6 + aggiornamento annuale | €0 (cooperazione Ente Parco) o €5-15k se rilievo ad-hoc | high |
| M-AVI-02 | **Buffer operativo 500 m da ogni nido noto** specie Allegato I; **1000 m da nidi aquila reale** in periodo riproduttivo | Ogni missione | €0 (planning SOPs) | high |
| M-AVI-03 | **Restrizione stagionale**: missioni in periodo riproduttivo (mar-lug) ridotte +30% rispetto al target nominale; eccezione = emergenza PC | Annuale stagionale | €0 (sched) | medium-high |
| M-AVI-04 | Quota minima cruise **200 m AGL** generalizzata; **250 m AGL su perimetro SIC**; **300 m AGL** su corridoi di nidificazione noti | Ogni missione | €0 (planning SOPs) | high |
| M-AVI-05 | Monitoraggio bioacustico ante-operam Y1 (3 stazioni autonome ARU, Autonomous Recording Units, 2-3 mesi mar-mag) | Una-tantum Y1 | €10-25k | medium |
| M-AVI-06 | Reporting bird-strike e near-miss avifauna a Ente Parco ed ENAC su base mensile | Mensile | €0 (procedurale) | medium |
| M-AVI-07 | Sospensione operativa immediata in caso di incidente con specie protetta, con indagine | Reattivo | n/a | n/a |

### A.12.6.2 Pacchetto mitigazioni rumore

| # | Mitigazione | Frequenza | Costo stimato |
|---|---|---|---|
| M-NOI-01 | Campagna fonometrica Y1 in 3 punti rappresentativi (borgo Pentema, perimetro SIC interno, recettore sensibile aquila se identificato), fonometro classe 1 cadenzato | Y1: 4 sessioni stagionali; Y2+: annuale | €8-15k Y1 |
| M-NOI-02 | Modelli predittivi di propagazione (CONCAWE-style o ISO 9613) per validare le quote operative ante-operam | Una-tantum M+9 | €5-10k |
| M-NOI-03 | Buffer 500 m da centri abitati Pentema per missioni notturne (nessuna operazione notturna salvo emergenza PC) | Ogni missione | €0 |
| M-NOI-04 | Profili volo "silent mode" (cruise > 250 m AGL, motore elettrico assistito al massimo % possibile) | Ogni missione | €0 (sched) |

### A.12.6.3 Pacchetto mitigazioni acque

| # | Mitigazione |
|---|---|
| M-ACQ-01 | Buffer ≥ 500 m laterali Diga Brugneto e ≥ 200 m AGL su specchio d'acqua |
| M-ACQ-02 | Protocollo emergency recovery in caso crash con briefing CAP Holding e Vigili del Fuoco |
| M-ACQ-03 | Coordinamento Autorità di Bacino Distrettuale Appennino Settentrionale (parere informativo) |

### A.12.6.4 Pacchetto mitigazioni paesaggio e suolo

| # | Mitigazione |
|---|---|
| M-PAE-01 | Priorità opzione A (affitto edificio esistente Pentema); opzione B solo se A indisponibile |
| M-PAE-02 | In opzione B, finiture esterne compatibili (legno, verde militare) e autorizzazione paesaggistica semplificata DPR 31/2017 |
| M-PAE-03 | Nessuna antenna pole-mount su crinali panoramici |
| M-PAE-04 | Sospensione operazioni durante eventi tradizionali Pentema (Presepe 7-26 dicembre) salvo emergenze PC |

### A.12.6.5 Cronoprogramma mitigazioni

| Mese | Azione |
|---|---|
| M+3 | Documento A.12 v2.0 (presente), invio informale a Ente Parco e Regione Liguria DG Ambiente |
| M+6 | Acquisizione mappa nidi Ente Parco, meeting tecnico Regione + ARPAL, convenzione Ente Parco in bozza |
| M+9 | Submission formale screening VIA (art. 19) e screening VIncA al Comune capofila / Regione |
| M+12 | Avvio campagna fonometrica e bioacustica field |
| M+18 | Review interim mitigazioni e tuning SOPs Y1 |
| M+24 | Bilancio Y1 di monitoraggio e revisione mitigazioni Y2 |

---

## A.12.7 Procedura VIA: classe applicabile e percorso autorizzativo

### A.12.7.1 Classificazione progetto ex Allegato IV D.Lgs. 152/2006

Verifica degli obblighi VIA:

| Riferimento | Soglia / Categoria | Applicabilità progetto |
|---|---|---|
| **Allegato II** TUA (VIA obbligatoria statale) | Aeroporti con piste > 1500 m, grandi infrastrutture | **Non applicabile** (operazioni UAS BVLOS, no aeroporto) |
| **Allegato II-bis** TUA (verifica assoggettabilità statale) | Modifiche/ampliamenti Allegato II | **Non applicabile** |
| **Allegato III** TUA (VIA obbligatoria regionale) | Aeroporti con piste 800-1500 m, piste ulteriori | **Non applicabile** |
| **Allegato IV** TUA (verifica assoggettabilità regionale) | Punto **7.d** "Aerodromi", soglia non specificata univocamente per UAS; **8.t** "Modifica/estensione progetti Allegati II/III/IV con incidenza rilevante su ambiente" | **Possibilmente applicabile** per analogia o estensione interpretativa |
| **Allegato IV** punto **7.l** | "Costruzione di linee aeree dell'energia elettrica…", non applicabile | No |

Considerazione interpretativa critica: il D.Lgs. 152/2006 e l'Allegato IV non disciplinano esplicitamente le operazioni UAS/BVLOS, perché il legislatore italiano del 2006 non aveva considerato la fattispecie. Le operazioni VTOL pilota Pentema non costituiscono "aerodromo" né infrastruttura permanente. L'**hangar light-build < 100 m²** (opzione B fallback) può rientrare in fattispecie locali (PUC Torriglia, vincolo paesaggistico DPR 31/2017) ma non sotto VIA statale o regionale. L'operatività in Parco Regionale, SIC/ZSC e ZPS attiva il regime VIncA e il parere dell'Ente Parco: questo costituisce il **canale autorizzativo prioritario**, non la VIA piena.

### A.12.7.2 Procedura raccomandata

Lo Studio attende come esito dello screening (art. 19 D.Lgs. 152/2006 e L.R. Liguria 32/2012) un giudizio di **non assoggettabilità a VIA piena**, motivato da:
1. assenza di consumo di suolo significativo (opzione A preferita);
2. assenza di emissioni significative;
3. assenza di opere infrastrutturali permanenti rilevanti;
4. operatività con UAS MTOM < 25 kg, classificato Specific EASA (non aeronautica civile manned);
5. impatti residui post-mitigazione classificati come bassi.

**Confidence verdetto di non assoggettabilità**: *medium* (~60-70%). La variabile critica resta l'interpretazione di Regione Liguria DG Ambiente e ARPAL. In una lettura estensiva (caso conservativo) la Regione può richiedere VIA piena, con ritardo +6/+18 mesi e costi +€30-100k.

Canale autorizzativo prioritario (sicuramente applicabile):

| Documento | Autorità | Tempistica attesa |
|---|---|---|
| **Verifica di Assoggettabilità a VIA** (screening art. 19) | Regione Liguria DG Ambiente | 60-90 giorni |
| **Screening Valutazione di Incidenza (VIncA)** ex DPR 357/1997 e L.R. 28/2009 | **Ente Parco Antola** (gestore SIC/ZSC/ZPS) + Regione Liguria | 60-90 giorni parallelo |
| **Parere paesaggistico** (se opzione B) DPR 31/2017 semplificato | Comune Torriglia + Soprintendenza | 60 giorni |
| **Parere vincolo idrogeologico** (se opzione B) | Regione Liguria Settore Difesa Suolo | 60-90 giorni |
| **Autorizzazione comunale** (PUC + edilizia) | Comune Torriglia | 60 giorni |
| **Coordinamento CAP Holding** (Diga Brugneto) | CAP Holding / IRETI | parere informativo 30 giorni |

Tempistiche totali stimate gate M+9 / M+12 per ottenere il set completo di pareri preliminari: 3-6 mesi, con possibile parallelizzazione.

### A.12.7.3 Scenario "VIA piena richiesta" (fallback)

Qualora la Regione Liguria richieda la VIA piena nonostante l'argomentazione di non assoggettabilità, lo Studio considera:

1. **Tempistica**: 12-18 mesi (con ricorsi fino a 24 mesi).
2. **Costi**: SIA (Studio Impatto Ambientale) completo €40-80k, oltre a consulenze tecniche e rilievi field.
3. **Impatto sul progetto**: slittamento Fase 1 operativa di 6-12 mesi, con effetto sul gate M+11.
4. **Strategia di mitigazione**:
 - engagement preventivo M+3/M+6 con la Regione per chiarire la fattispecie;
 - pre-application meeting e parere informale ARPAL prima della submission formale;
 - eventuale chiusura pre-emptive con percorso semplificato "Operazioni UAS sperimentali";
 - riduzione dello scope Y1 (per esempio solo missioni di emergenza PC, senza missioni di routine) per abbassare il profilo di rischio.

---

## A.12.8 Benefici ambientali (analisi controfattuale)

Il progetto genera **benefici netti positivi** rispetto agli scenari alternativi (sorveglianza manned, pattugliamento terrestre, non-intervento):

| Beneficio | Quantificazione preliminare | Confidence |
|---|---|---|
| Riduzione emissioni CO₂ vs elicottero manned | **-99% emissioni operative** (130 kg vs 24.000 kg CO₂/anno) | high |
| Riduzione emissioni CO₂ vs pattugliamento terrestre 4×4 | **-80%** (130 kg vs 720 kg CO₂/anno) | high |
| Antincendio precoce, riduzione superfici bruciate | Stima -10/-20% incendi controllati in early detection (letteratura DJI Wildfire reports) | medium |
| Monitoraggio frane, riduzione danni patrimoniali | €5-20M/anno per Liguria interna (stima conservativa, vedi Cap. 7 §7.11) | low-medium |
| Vigilanza anti-bracconaggio Parco Antola | Convenzione Ente Parco, beneficio gestionale | medium |
| Monitoraggio biodiversità (specie chiave) | Possibile servizio di ricerca scientifica con Università Genova / CNR | medium |

**Bilancio ambientale netto Y1 pilota**: fortemente positivo in chiave cost-benefit ambientale, con impatti residui contenuti e benefici cumulativi rilevanti.

---

## A.12.9 Engagement plan e governance ambientale

### A.12.9.1 Stakeholder ambientali e ruoli

| Stakeholder | Ruolo | Touchpoint | Owner Firmamento |
|---|---|---|---|
| **Regione Liguria DG Ambiente** | Autorità competente VIA regionale | Submission screening + audience tecnica | environmental-consultant + government-affairs |
| **ARPAL, Agenzia Regionale Protezione Ambiente Liguria** | Supporto tecnico Regione e monitoraggio | Consultazione ante-submission, monitoraggio rumore/aria | environmental-consultant |
| **Ente Parco Naturale Regionale Antola** | Gestore SIC/ZSC/ZPS e parere VIncA | Convenzione operativa, accesso mappe nidi | Firmamento ops + environmental-consultant |
| **Comune di Torriglia (Pentema)** | Autorità locale e accettabilità sociale | Workshop pubblico, autorizzazioni edilizie | community-engagement |
| **CAP Holding / IRETI** | Gestore Diga Brugneto | Coordinamento protocollo sorvolo | safety-engineer |
| **Autorità di Bacino Distrettuale Appennino Settentrionale** | Pianificazione acque | Parere informativo | environmental-consultant |
| **Soprintendenza Archeologia Belle Arti Paesaggio Liguria** | Vincolo paesaggistico | Solo in opzione B hangar | architect-consultant |
| **Federcaccia + Federazione Italiana Caccia Liguria** | Stakeholder venatorio (uso parco autunno) | Coordinamento periodo venatorio | community-engagement |
| **Università Genova + CNR-IBE** | Scienza biodiversità | Potenziale partnership monitoraggio | tech-transfer |

### A.12.9.2 Calendario engagement M+3 / M+12

| Mese | Azione | Stakeholder |
|---|---|---|
| **M+3** | Lettera informale e invio A.12 v2.0 | Regione Liguria + Ente Parco + ARPAL |
| **M+4** | Meeting tecnico (workshop tavola rotonda) | Regione + ARPAL + Ente Parco + Comune Torriglia |
| **M+5** | Bozza convenzione Firmamento / Ente Parco | Ente Parco |
| **M+6** | Acquisizione mappa nidi, dati formulario Natura 2000, condivisione documenti | Ente Parco |
| **M+7** | Pre-application meeting screening VIA e VIncA | Regione Liguria + ARPAL |
| **M+8** | Pareri informali Soprintendenza e CAP Holding | Soprintendenza + CAP Holding |
| **M+9** | **Submission formale** screening VIA e screening VIncA | Regione Liguria |
| **M+9** | Workshop pubblico Pentema (DPIA, accettabilità e ambiente combinati) | Comunità Pentema + Pro Loco |
| **M+10** | Risposte alle richieste di integrazioni Regione | Regione + ARPAL |
| **M+12** | Esiti attesi dei pareri preliminari | Regione + Ente Parco |

---

## A.12.10 Outlook Percorso 6B HALE stratosferico

Per il Percorso 6B (HALE solare a 20 km di quota), il quadro VIA cambia in modo sostanziale:

| Componente | 6A VTOL Pentema | 6B HALE |
|---|---|---|
| Rumore al suolo | 45-55 dB(A) | < 30-35 dB(A) (impercettibile da 20 km) |
| Emissioni operative | ~130 kg CO₂/anno | **ZERO** (100% solare a regime; manufacturing separato) |
| Impatto avifauna | Medio (mitigabile) | Trascurabile (HALE opera ben oltre la quota uccelli) |
| Impatto paesaggio | Basso | Trascurabile (HALE non visibile da terra) |
| Impatto stratosferico | n/a | **Nuovo dominio**, interazioni con aviazione commerciale, satelliti LEO, frammenti dopo end-of-life |
| Impatto cumulativo costellazione | n/a | Da valutare (multi-HALE, impatti nuovi) |
| Procedure VIA | Screening regionale | **VIA EU + ICAO + EASA HAPS framework** (orizzonte 2030+) |
| Procedure VIncA | Screening SIC/ZSC/ZPS | Non applicabile a quote stratosferiche |

In sintesi, il Percorso HALE richiede una **VIA dedicata di nuova generazione** in coordinamento con il framework EU HAPS (RMT EASA atteso 2027-2029); vedi Cap. 5 §5.10. La presente Relazione A.12 v2.0 non copre il Percorso 6B.

---

## A.12.11 Conclusioni preliminari

### A.12.11.1 Verdetto preliminare

1. **Procedura VIA applicabile**: Verifica di Assoggettabilità (screening art. 19 D.Lgs. 152/2006 e L.R. Liguria 32/2012). VIA piena non attesa.
2. **Procedura VIncA applicabile**: Screening VIncA (Livello I) ex DPR 357/1997 e L.R. Liguria 28/2009 per il SIC/ZSC/ZPS IT1331402.
3. **Esito atteso**: non assoggettabilità a VIA e assenza di incidenza significativa, con applicazione integrale delle mitigazioni proposte in §A.12.6.
4. **Confidence verdetto aggregato**: *medium* (~60-70%). Variabile critica: interpretazione di Regione Liguria ed Ente Parco.

### A.12.11.2 Gap residui pre-istruttoria

| Gap | Azione richiesta | Owner | Scadenza |
|---|---|---|---|
| Mappa nidi specie Allegato I | Acquisizione formale Ente Parco | environmental-consultant | M+6 |
| Formulario standard Natura 2000 IT1331402 aggiornato | Estrazione database MASE e verifica Regione | environmental-consultant | M+5 |
| Conferma classificazione acustica Comune Torriglia | Richiesta formale e Piano Classificazione | environmental-consultant | M+5 |
| Modello predittivo propagazione rumore | Affidamento studio acustico specialistico | environmental-consultant | M+8 |
| Parere informale ARPAL | Pre-application meeting | environmental-consultant + Firmamento | M+7 |
| Convenzione Ente Parco bozza | Trattativa | Firmamento + Ente Parco | M+9 |
| Protocollo CAP Holding Diga Brugneto | Coordinamento tecnico | safety-engineer | M+9 |
| Eventuali rilievi field bioacustica ante-operam | Decisione sull'esecuzione | environmental-consultant + science partner | M+10 |
| Studio Impatto Ambientale completo (se VIA piena richiesta) | Affidamento e redazione | environmental-consultant + SIA specialist | contingent M+12+ |

### A.12.11.3 Falsifying observations

Cinque scenari triggerano un re-baselining significativo:

1. l'Ente Parco Antola impone una moratoria totale mar-lug, con peak antincendio Y1 compromesso e reset del modello operativo;
2. la Regione Liguria richiede VIA piena, con slittamento +6/+18 mesi, costi +€30-100k e gate M+11 a rischio;
3. l'identificazione di nidi attivi di aquila reale nei corridoi operativi prioritari impone la riconfigurazione completa delle rotte;
4. ARPAL contesta il superamento dei limiti acustici dopo il monitoraggio, con riduzione operatività -10/-40%;
5. un incidente con specie protetta (bird-strike di specie Allegato I) determina sospensione operativa, indagine ENAC e danno reputazionale.

### A.12.11.4 Caveat di chiusura

La presente Relazione VIA Preliminare v2.0 è documento *preliminary-grade* destinato all'istruttoria della Regione Liguria. Non costituisce uno Studio di Impatto Ambientale (SIA) completo né una Relazione di Incidenza Appropriata completa. Qualora le autorità competenti richiedano tali documenti formali, la relazione costituisce baseline preliminare da integrare con rilievi field dedicati (avifauna nidificante con metodologia EBCC, bioacustica, fonometria L. 447/1995 in continuo), modelli di propagazione validati, mappatura GIS dettagliata e accordi formali con Ente Parco, ARPAL e gestori delle risorse.

**Confidence aggregato del documento: medium.** Caveat operativo per il progetto: la presente versione non è sufficiente per la chiusura del gate M+10/M+11 in assenza di pareri preliminari favorevoli di Regione Liguria ed Ente Parco; queste due risposte rappresentano condizioni necessarie per il Go Condizionato del Percorso 6A.

---

## A.12.12 Linkage al resto dello Studio di Fattibilità

| Riferimento | Linkage |
|---|---|
| **Cap. 1 §1.2.2 / §1.2.3** | Inquadramento territoriale Pentema e caratteristiche orografiche |
| **Cap. 2 §2.1** | Stakeholder S-04 Regione Liguria, S-05 Comune Torriglia, S-26 Ente Parco Antola |
| **Cap. 3 §3.x, RTM** | Requisito ambientale REQ-NF-AMB-01 (nuovo, proposto in questa relazione) |
| **Cap. 5 §5.0bis e §5.16** | Quadro normativo ambientale (TUA, Habitat, Uccelli, L.R. Liguria) |
| **Cap. 6 §6.x** | Trade study profili volo (DOCFAP), input quote operative e mitigazioni rumore |
| **Cap. 7 §7.11** | ESG e benefici ambientali quantificati |
| **Cap. 9 §9.x** | Gate decisionali M+6 / M+9 / M+10, milestone ambientali |
| **Allegato A.1 RTM** | Tracciabilità REQ-NF-AMB-01 verso VRD-AMB-01 e VRD-AMB-02 |
| **Allegato A.2 Risk Register** | RSK-REG-011 (esistente), RSK-REG-024 (esistente), RSK-AMB-001/002/003 (nuovi proposti) |
| **Allegato A.5 V&V Plan** | Verifica conformità ambientale (pacchetto V_AMB) |
| **Allegato A.9 CME** | Hangar Pentema opzione A vs B (input: A preferita) |
| **Allegato A.10 Piano Manutenzione** | Procedure ambientali, recovery, bird-strike reporting |
| **Allegato A.11 Safety Case SORA** | Ground Risk, Air Risk, ambientale interfacciato |
| **Allegato A.13 Documentazione fotografica** | Stato dei luoghi ante-operam, mappature di sensibilità |

---

## A.12.13 Riferimenti normativi e tecnici

### A.12.13.1 Normativa primaria

- **D.Lgs. 152/2006** (Testo Unico Ambientale) Parte II, art. 19 (Verifica di Assoggettabilità) e Allegati II/III/IV/V
- **D.Lgs. 104/2017**, recepimento Direttiva 2014/52/UE su VIA
- **DPR 357/1997**, recepimento Direttiva Habitat 92/43/CEE e Allegati G/H VIncA
- **L. 394/1991**, Legge quadro Aree Protette
- **L. 447/1995**, Legge quadro inquinamento acustico
- **DPCM 14/11/1997**, limiti di emissione acustica per zona
- **L. 353/2000**, incendi boschivi
- **D.Lgs. 42/2004**, Codice dei Beni Culturali e del Paesaggio (Codice Urbani)
- **R.D. 3267/1923**, vincolo idrogeologico
- **DPR 31/2017**, autorizzazione paesaggistica semplificata
- **D.Lgs. 36/2023 art. 41 e Allegato I.7**, PFTE incluse le relazioni specialistiche ambientali

### A.12.13.2 Normativa regionale Liguria

- **L.R. Liguria 12/1995**, istituzione del Parco Naturale Regionale dell'Antola
- **L.R. Liguria 32/2012**, procedure VIA regionali
- **L.R. Liguria 28/2009**, Valutazione d'Incidenza (recepimento DPR 357/1997)
- **L.R. Liguria 12/1998**, tutela dell'ambiente dall'inquinamento acustico
- **L.R. Liguria 38/1998**, disciplina VIA regionale (precedente, parzialmente abrogata)
- **L.R. Liguria 22/2009**, disciplina della caccia (interfaccia con uso del territorio)

### A.12.13.3 Direttive EU

- **Direttiva 92/43/CEE**, Habitat (allegati I, II, IV, V)
- **Direttiva 2009/147/CE**, Uccelli (precedente 79/409/CEE)
- **Direttiva 2014/52/UE**, VIA aggiornata
- **Direttiva 2000/60/CE**, Acque
- **Direttiva 2002/49/CE**, Rumore ambientale

### A.12.13.4 Linee guida tecniche

- **MATTM/MASE 2019**, Linee guida nazionali Valutazione di Incidenza
- **ISPRA**, manuali e linee guida VIA e VIncA
- **EBCC**, metodologie standard di censimento avifauna
- **ISO 9613-2**, propagazione acustica all'aperto
- **NASA SE Handbook Rev 2**, gate-driven (metodologia ingegneristica)

### A.12.13.5 Documentazione consultata

- Formulario standard Natura 2000 IT1331402 (estrazione richiesta in istruttoria)
- Piano del Parco Antola, Ente Parco Antola (versione vigente da verificare)
- Atlante Avifauna Nidificante Liguria (riferimento bibliografico)
- Catasto Incendi Boschivi Comune Torriglia
- Piano di Classificazione Acustica Comune Torriglia (verifica disponibilità)
- Rapporto SNAI Antola Tigullio 2021-2027

---

**Documento redatto da**: environmental-consultant (consulente ambientale Firmamento Technologies)
**Revisione**: review critica indipendente (rigore epistemico check)
**Data**: 17 maggio 2026
**Versione**: 2.0 (sostituisce v1.0 desk del 17 maggio 2026)
**Distribuzione interna**: project-manager, government-affairs, safety-engineer, flight-ops
**Distribuzione esterna proposta (post-revisione)**: Regione Liguria DG Ambiente, ARPAL, Ente Parco Antola, Comune Torriglia (lettera accompagnatoria M+3)
