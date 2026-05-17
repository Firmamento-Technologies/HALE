# Capitolo 0. Sintesi Esecutiva

> **Studio di Fattibilità, Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 0
>
> Destinatari: CdA Firmamento Technologies, Coopfond, Regione Liguria, MIMIT, ENAC, EASA, finanziatori, stakeholder istituzionali.
> Versione: bozza M+11 (proiezione finale Studio).
> Lunghezza target: 5-8 pagine A4.

---

## 0.0 Confidence aggregato dello Studio (alla milestone M+3)

Per ogni claim numerico o strategico del presente capitolo riportiamo il livello di confidence, costruito secondo le sette regole del rigore epistemico e i quattro cicli di review critica indipendente condotti alla milestone M+3.

| Claim | Confidence | Evidenze |
|---|---|---|
| CapEx Y1 €700k-2M | medium | Range che include contingency 15% e IVA. Le quotation vendor reali (JOUAV e Tekever) sono ancora pending nei DR-001/DR-003; il livello salirà a medium-high una volta acquisite. |
| OpEx Y2 RECONCILED €1.18M | medium-high | La componente regulatory team mandatory (€400-590k per CISO, DPO, Head Regulatory) è derivata dal Cap. 5 §5.17 sulla base di evidenza normativa diretta (Part-IS EASA, NIS2, AgID/PSN, art. 50, ENAV). Il baseline tecnico €260-480k proviene dai modelli stime interne di modellazione finanziaria. |
| Revenue Y1 €260k centrale (range €220-300k) RECALIBRATED | medium | Pricing post-audit Cluster D (benchmark Planetek Rheticus Puglia, e-GEOS PC Lazio, NHazca) con confidence high. La soglia €200k SyR-Cost-003 funge da hard floor. Il legacy €355-405k è stato falsificato e non rientra più nel modello operativo. |
| NPV 10y base +€3.5M / IRR 12-18% | low | Periodo out-of-window per validazione diretta dal terzo anno in poi. La sensitivity in Cap. 8 §8.6.3 mostra un range ampio. L'analisi Monte Carlo non è ancora stata condotta (DR-008). |
| Break-even Y5-Y6 | medium-low | Post-recalibration del revenue Y1; assume scale-up SNAI Y2-Y3 a una nuova regione l'anno mantenendo il pricing. |
| P(Go pieno gate G3) 5-15% | medium-high | Calcolo derivato dall'AND delle 5 hard conditions (Cap. 10 §10.0bis), con P marginali stimate da review critica indipendente. Coerente con il base rate startup deeptech (DR-013/DR-014). |
| P(HOLD piano rafforzato G3) 45-60% | medium-high | Scenario realistico atteso. Il pivot a sliding timeline §9.12 non comporta perdita di valore strategico. |
| 5 showstopper formali (Risk Register) | high | Identificati e quantificati dai quattro review critiche indipendenti. RSK-TEC-001 ha score 25 dopo la simulazione completa di energy balance HALE a 44°N (allegato A.7). |
| Visione 10 anni / B2 EU sovereign stratospheric layer | low-medium aspirazionale, non operativa | Boundary condition strategica, input progetto non falsificabile. B2 full con P 6-15%; B2-relaxed standalone IT small fleet con P 30-50%. Trigger in FO-ADD-10 e Cap. 11 §11.6bis. |
| Posizionamento "complementare IRIS²" | medium | IRIS² baseline LEO+MEO puro confermato (DR-009 closure). La finestra di opportunità stratospheric gap-filler è aperta Y2-Y4 (2027-2030). Falsificabile via FO-ADD-02 (M+18, roadmap DG CNECT). |
| 5 Pilastri vantaggio competitivo | mixed | Uno high (cooperative, se strutturazione giuridica), due medium (sostenibilità e service-only), due low (specializzazione geografica e approccio incrementale). Vedi Cap. 7 §7.5.1. |
| Capital intensity Y10 €500M-1.5B small fleet | low | Extrapolation 8-10 anni out-of-window. Bottom-up estimate Cap. 11 §11.6.4 con range largo, da affinare nei modelli benchmark internazionali del Vol. 2 financial model. |

> **Confidence aggregato Studio M+3**: MEDIUM-LOW. Lo Studio richiede validazione esterna prima del G3 effettivo M+10 e **non è investment-grade** per finanziatori istituzionali (VC top-tier, BEI, EIC) in assenza di LoI Regione Liguria firmata, vendor quotation reali, pre-application ENAC documentata, modello finanziario validato esternamente (RINA, DNV) e Monte Carlo analysis. Per Coopfond, Regione Liguria e bando Cooding Prototypes il livello aggregato medium è sufficiente all'istruttoria del bando e alla DGR regionale.

---

## 0.1 Il progetto

Firmamento Technologies propone lo sviluppo e l'attivazione di una piattaforma aerea unmanned, operata come erogatore di servizi e non come venditore di velivoli, a beneficio delle Aree Interne italiane: territori a bassa densità demografica, orografia complessa, carenza di servizi essenziali e divario digitale strutturale.

Lo Studio è redatto in conformità all'art. 41 D.Lgs. 36/2023 e all'Allegato I.7 del Codice dei Contratti Pubblici, con metodologia derivata dal NASA Systems Engineering Handbook Rev 2 e dai template italiani autoritativi (ENAC AAM Business Plan 2021-2030, MIMIT prefattibilità aero, DTA Puglia Studio Grottaglie).

Il caso pilota è la frazione di Pentema, nel Comune di Torriglia (Genova), area SNAI riconosciuta nel ciclo 2021-2027 (Valli dell'Antola e del Tigullio), Regione Liguria: un laboratorio italiano per le politiche pubbliche delle Aree Interne.

La rete di utenti-pilota è composta da dieci cooperative aderenti a Legacoop, con Fabrica come capofila. Le cooperative agiscono come utenti, co-progettisti e custodi di fabbisogni operativi reali.

---

## 0.2 Strategia duale (Percorso 6A + 6B)

Il progetto adotta una strategia duale a riduzione del rischio, articolata su due percorsi paralleli.

### Percorso 6A, VTOL Pilota Pentema (operativo, 0-12 mesi)

La tecnologia è una piattaforma commerciale Vertical Take-Off and Landing TRL 8-9, con baseline JOUAV CW-30E e Plan B Tekever AR3 ITAR-free EU, payload modulare EO + IR + telecom backup. I casi d'uso target sono cinque: monitoraggio del rischio idrogeologico per Regione Liguria e Protezione Civile, antincendio boschivo con early detection ≤ 5 min per VVF e Carabinieri Forestali, connettività di emergenza per PC e Comune di Torriglia, mapping infrastrutture rurali per i Comuni SNAI, servizi alle cooperative agricole e forestali aderenti a Legacoop.

Il budget CapEx Y1 è stimato in €700k-€2M, incluse IVA e contingency 15%. L'OpEx run-rate Y2 RECONCILED post Cap. 5 §5.17 si attesta su **€1.18M/anno centrale** (range €1.05-1.30M): vi rientrano €260-480k di baseline tecnico, €400-590k di regulatory team mandatory (CISO, DPO, Head Regulatory) e €115-230k di overhead amministrativo. Il legacy €260-480k/anno copre il solo OpEx tecnico e non è sufficiente sul piano operativo dopo l'identificazione, in Cap. 5 §5.17, dei 5+1 critical regolatori (Part-IS, AgID/PSN, NIS2, art. 50, ENAV, EUROCONTROL).

Il revenue Y1 baseline RECALIBRATED post audit Cluster D (M+3) si colloca a **€260k centrale** (range €220-300k) da cinque contratti pluriennali, con minimo SyR-Cost-003 di €200k come hard floor. Il pricing PA è ricalibrato a €60-90k/anno per la componente base e €30-60k/anno per la premium su persistence e sovranità, dopo la falsificazione del baseline originale €150k/anno (revenue €355-405k) operata dal benchmark Cluster D Planetek, e-GEOS e NHazca, attestato a €30-80k/anno. Il dettaglio è in Cap. 7 §7.4.4-5 e §7.8.2.

### Percorso 6B, HALE Stratosferico (R&D, 24-48+ mesi)

La tecnologia è una piattaforma High Altitude Long Endurance a propulsione solare, apertura 25-30 m, MTOW 80-150 kg, quota operativa 18-21 km (FL590-690), endurance target ≥ 30 giorni perennial estate (Y3) e 12 mesi a regime (Y5). I casi d'uso post-pilota includono osservazione persistente del territorio in chiave EO multispettrale, connettività NTN 5G NR (3GPP Rel-17/18 regenerative gNB) e servizi dual-use civile-difesa, questi ultimi potenziali e condizionati.

Il budget Phase B R&D è stimato in €5.5-13.5M nella finestra M+24 → M+48, con un mix di finanziamento al 50-75% di grant pubblico (EDF, Horizon, PNRR, ASI).

---

## 0.3 Verdetto dello Studio

### Percorso 6A: HOLD CON PIANO REGOLATORIO RAFFORZATO (scenario base, P 45-60%) / GO CONDIZIONATO (scenario ottimistico, P 5-15%)

Il caveat probabilistico, dichiarato onestamente dopo l'audit M+3, è che le cinque hard conditions del verdetto sono in AND logico. La P(AND tutte) realistica al gate G3 si colloca al 5-15% per il Go pieno e al 45-60% per l'Hold con piano e re-review M+13-16. Lo scenario base atteso è dunque l'Hold con piano rafforzato. Il dettaglio è in Cap. 10 §10.0bis.

Il Percorso 6A è tecnicamente, regolatoriamente, di mercato e finanziariamente fattibile entro l'orizzonte dei 12 mesi. Il Go pieno resta subordinato a cinque condizioni vincolanti al gate M+10-12: LoI o accordo formale con Regione Liguria firmato entro M+9; autorizzazione SORA ENAC SAIL II-III BVLOS operativa entro M+9; mix funding committed ≥ 60% entro M+10; almeno otto cooperative pilota su dieci che confermino partecipazione formale entro M+6; pre-application meeting ENAC con feedback documentato entro M+3-6.

### Percorso 6B: HOLD CON CRITERI DI USCITA ESTREMAMENTE STRINGENTI + pivot strutturale

Il pivot strategico alla milestone M+3 (DR-013 e DR-014) si fonda su tre constatazioni: il base rate di HALE solari commerciali operativi è prossimo allo zero, con dodici programmi falliti analizzati negli ultimi 22 anni; la capital intensity di benchmark internazionale si colloca in $50M-1B per programma, sicché €5.5-13.5M corrispondono in realtà a R&D di Fase 0/A, non al percorso completo verso l'operatività; di conseguenza la raccomandazione è di pivotare da "HALE proprietario Firmamento" a "Firmamento operatore di servizi su piattaforme prime contractor" (Aalto, Sceye, Skydweller, CIRA-EuroHAPS-successor).

La fattibilità tecnologica resta plausibile, ma rimangono aperti cinque showstopper. RSK-TEC-001 riguarda l'energy balance HALE in inverno a 44°N, con margine reale a -50.1% deficit (la simulazione completa dell'allegato A.7 supera la stima hand-calc "0-15% critico"); l'architettura E5 Seasonal-only marzo-ottobre diventa il plan A mandatory, mentre l'operatività perennial a 44°N non è fattibile con la tecnologia baseline 2026-2028; il punteggio RSK è stato aggiornato a 25. RSK-TEC-002 concerne l'aeroelasticità dell'ala high-AR. RSK-REG-001 attiene all'assenza di framework regolatorio HAPS UE (la EASA Special Condition non è ancora aperta). RSK-FIN-001 è il funding Phase B €5.5-13.5M non commitato al M+11. RSK-TEC-003 riguarda i tempi di Type Certification HALE superiori a cinque anni.

La Phase B R&D resta autorizzata solo subordinatamente al raggiungimento delle condizioni al gate G5 (M+24), incluso un funding mix con ≥ 50% pubblico ed engagement EASA aperto.

---

## 0.4 Visione 10 anni

Il posizionamento strategico target è quello di nodo italiano fondatore di una futura infrastruttura sovrana europea HAPS, complementare a IRIS² (LEO+MEO sovereign EU, €10B, governance SpaceRISE che comprende Airbus, Eutelsat, Thales-Telespazio, Hispasat, OHB, Deutsche Telekom e Orange; primo lancio 2029, operatività piena 2031, baseline LEO+MEO puro senza layer stratosferico secondo la closure DR-009 in M+3, vedi Cap. 5 §5.16bis) e a Galileo/Copernicus. La finestra strategica Y2-Y4 di Firmamento (2027-2030) si sovrappone alla fase pre-ops di IRIS², offrendo un'opportunità di posizionamento "stratospheric layer gap-filler" via engagement DG CNECT e SpaceRISE.

Il linguaggio pubblico raccomandato resta "complementare a IRIS²", mai "alternativa europea a Starlink", per ragioni geopolitiche dichiarate nel documento riservato.

Le cinque fasi della visione sono ordinate cronologicamente. In Y1 si esegue il pilota Pentema VTOL, con pilot validato e revenue tra €200k e €400k. In Y2-Y3 si effettua lo scale-up SNAI Italia su 3-4 regioni, con una flotta di 3-8 VTOL/MALE e R&D HALE subscale parallelo. In Y3-Y6 entra in servizio il primo HALE prototipo operativo italiano, accompagnato da un servizio commerciale HAPS pilota. In Y6-Y8 si forma la costellazione italiana di 3-10 HAPS, con servizi NTN ed EO persistente. In Y8-Y10 nasce il consorzio EU stratospheric layer (Italia, FR, DE, ES) con posizionamento ufficiale "EU sovereign stratospheric layer" complementare a IRIS².

La capital intensity dei dieci anni è dichiarata onestamente: €500M-€2B nello scenario "small fleet" (5-10 HAPS) e €10-30B nello scenario "EU sovereign full scale" (100+ HAPS, che richiede come precondizione esterna l'apertura di un programma EU equivalente IRIS²).

Lo Studio approva soltanto Y1-Y3 (Fasi 1 e 2). Le fasi 3-5 restano vettore strategico mantenuto, con decisione formale rinviata ai gate G5 (M+24), G6 (M+36) e successivi.

---

## 0.5 Modello di business

La boundary condition strutturale resta service-only, senza vendita di prodotto. Le linee di servizio (monitoraggio EO, connettività emergenza, analytics) sono erogate in quattro formati alternativi o combinati: canone fisso, ore-volo più analytics, outcome-based, DaaS (Data-as-a-Service). I canali distributivi prevalenti sono B2G regionale (con anchor Regione Liguria), B2G locale (PC, ARPA, Enti Parco) e B2B cooperative (rete Legacoop scaled).

Il vantaggio competitivo poggia su quattro pilastri: specializzazione geografica nelle Aree Interne italiane, modello cooperativo come barriera all'imitazione, sostenibilità e narrativa ESG (propulsione 100% solare ed elettrica, fibra di lino in strutture secondarie), approccio incrementale VTOL → MALE → HALE che produce asset riusabili stimati al 30-40% del CapEx Y1.

---

## 0.6 Quadro normativo

Lo Studio è conforme al D.Lgs. 36/2023 art. 41 e Allegato I.7 (Codice Contratti Pubblici), ai Reg. UE 2019/947 e 2019/945 (UAS Operations and Design), all'EASA AMC/GM Issue 1 Amendment 3 di settembre 2025 (versione europea di SORA 2.5), al Regolamento ENAC sui Mezzi Aerei a Pilotaggio Remoto Ed. 3 con Emendamento 1, al Reg. UE 2021/664 e alla Linea Guida ENAC LG-2023/006 (U-Space), al GDPR e al D.Lgs. 196/2003 novellato (privacy), alla Direttiva NIS2 e D.Lgs. 138/2024 (cybersecurity), agli standard AS/EN 9100 e ISO 9001 sui sistemi di gestione qualità aerospace.

La strategia regolatoria per il Percorso 6A poggia sulla Specific Category SAIL II-III BVLOS, con SORA application, Operations Manual e Operator Declaration verso ENAC. Per il 6B la strategia richiede la Certified Category via Special Condition HAPS negoziata con EASA, con timeline tipica nell'ordine dei 5-8 anni.

---

## 0.7 Stakeholder critici

| # | Stakeholder | Ruolo | Commitment richiesto |
|---|---|---|---|
| 1 | Regione Liguria | Anchor customer e sponsor istituzionale | LoI/DGR formale entro M+9 |
| 2 | Coopfond e Legacoop | Finanziatore primary e governance cooperative | Contratto Cooding e Cooding-Invest |
| 3 | Rete 10 cooperative (Fabrica capofila) | Utenti-pilota e co-progettisti | ≥ 8 su 10 confermano partecipazione M+6 |
| 4 | Comune Torriglia e comunità Pentema | Sede pilota e accettabilità sociale | Delibera comunale e workshop comunità |
| 5 | Protezione Civile Liguria e ARPA Liguria | Cliente operativo primario | Convenzione operativa e protocollo |
| 6 | ENAC | Regolatore aviazione civile | Autorizzazione SORA SAIL II-III BVLOS |
| 7 | EASA | Regolatore europeo | Engagement Innovation Network su framework HAPS |
| 8 | AGCOM | Regolatore spettro radio | Licensing temporaneo bande ISM o commerciali |
| 9 | Garante Privacy | Regolatore protezione dati | DPIA pubblica preliminare M+6 |
| 10 | CIRA | Partner R&D potenziale Phase B 6B | Letter of intent M+9-12 |

---

## 0.8 Risk aggregato

Sul Percorso 6A non emergono showstopper formali. Restano cinque rischi gialli con mitigation plan chiaro. Il profilo di rischio è medio-basso, compatibile con un Go Condizionato.

Sul Percorso 6B sono presenti cinque showstopper rossi (energy balance inverno, aeroelasticità ala high-AR, framework HAPS, funding Phase B, Type Certification timeline). Esiste una mitigation strategy, ma non è garantita. Il profilo è di rischio alto, compatibile soltanto con Hold o Go Condizionato Estremo.

---

## 0.9 Finanziamento

Il mix raccomandato per il Y1 del Percorso 6A, su target €0.75-1.75M, prevede €50k da Coopfond Cooding Prototypes 2026 (massimo, 5% del mix), €150-300k da Coopfond Cooding-Invest (15-20%), €300-500k da Regione Liguria FESR 2021-2027 (25-40%), €0-300k da PNRR Aerospazio e IS4Aerospace (0-20%), €200-500k di equity privato founder e seed (25-35%), e €50-150k da R&D tax credit ex L. 160/2019 (5-15%).

Per la Phase B 6B, su target €5.5-15.5M nella finestra M+24-48, il mix prevede €2-5M da EDF call HAPS post-EuroHAPS (30-40%), €1-3M da Horizon Europe Cluster 4 e 5 (15-25%), €1-2.5M da PNRR Aerospazio, ASI e MIMIT (15-20%), €1-2.5M di equity privato Series A/B (10-25%), e €0.5-1.5M da R&D tax credit e Patent Box (5-10%).

---

## 0.10 Cronoprogramma e gate

```
M+0 M+3 M+6 M+10/11 M+12 M+24 M+36 M+48
│ │ │ │ │ │ │ │
│ G0 │ G1 │ G2 │ G3 │ G4 │ G5 │ G6 │ Phase B end
│ │ │ │ ★ FEAS │ │ │ │
│ │ │ VERDICT │ │ │ │
│ STUDIO DI FATTIBILITÀ │ PILOTA 6A VTOL OP │ R&D 6B HALE PHASE B │
```

I gate principali sono quattro. G3 (M+10-11) è il FEASIBILITY GATE PRIMARIO e produce il verdetto Go / Hold / No-Go per ciascun percorso (oggetto del presente Studio). G4 (M+12) chiude il pilota VTOL 6A e attiva la decisione di scale-up SNAI. G5 (M+24) decide la Phase B 6B in modalità Go o Defer. G6 (M+36) è la midterm review della Phase B HALE.

---

## 0.11 Numeri chiave

| Metric | Valore |
|---|---|
| Durata Studio di Fattibilità | 11 mesi (M+0 → M+11) |
| Durata pilota 6A | 12 mesi (M+0 → M+12), operativo da M+9 |
| Durata Phase B 6B R&D | 24 mesi (M+24 → M+48) |
| CapEx 6A Y1 | €700k – €2M |
| OpEx 6A Y2 run-rate (RECONCILED post Cap. 5 §5.17) | €1.18M/anno centrale (range €1.05-1.30M); il legacy "tecnico-only" €260-480k/anno non è sufficiente operativamente |
| Revenue 6A Y1 baseline (RECALIBRATED) | €260k centrale, range €220-300k (min €200k SyR-Cost-003), post audit Cluster D |
| ARR Y3 target | €1.5-3.5M (scale-up Liguria + 1 regione) |
| ARR Y5 target | €3-8M (multi-regione + HAPS subscale) |
| Break-even cumulato | Y4-Y5 (scenario base) |
| NPV 10y scenario base | +€3-8M |
| IRR 10y scenario base | 18-25% |
| Payback semplice | 4-6 anni |
| Capital intensity Y10 small fleet | €500M – €2B |
| Capital intensity Y10 EU sovereign | €10-30B (precondizione esterna) |
| 10 cooperative pilota | Fabrica capofila + 9 aderenti |
| Stakeholder mappati | 30 |
| StNeeds baseline | 17 |
| System Requirements | 42 |
| Subsystem Requirements | ~80 sample (~200 in v1.0) |
| Showstopper formali | 5 (tutti su 6B) |
| Falsifying observations dichiarate | ~40 (totale Volume 1) |
| Citazioni autoritative | ~200 (totale Volume 1) |

---

## 0.12 Decisione richiesta

Ai destinatari del documento (CdA, Coopfond, Regione Liguria, altri sponsor) si chiede formalmente l'approvazione di sei punti: lo Studio di Fattibilità nei suoi tre volumi; il GO CONDIZIONATO sul Percorso 6A con piano di attivazione M+12; l'HOLD o GO CONDIZIONATO ESTREMO sul Percorso 6B con commitment al gate G5 (M+24); il budget Y1 6A nella sua composizione CapEx, OpEx e mix funding; l'engagement plan istituzionale Cap. 5.11.3; il master schedule M+12 → M+48.

---

## 0.13 Riferimenti

Per il dettaglio di ciascun argomento si rinvia ai Cap. 1-11 del Volume 1, agli Allegati Tecnici del Volume 2 e ai Riferimenti bibliografici del Volume 3.

Documenti di contesto: `riferimenti/visione-10-anni.md` per il vettore strategico decennale, `riferimenti/analisi-fac-simili-IT.md` per la mappatura art. 41 e NASA SE, `riferimenti/ricerche-approfondite.md` per il dataset di ricerca, `riferimenti/audit-rigore-epistemico.md` per gli audit di confidence e per la lista del debito di rigore.

Documento riservato ad accesso ristretto, non parte dello Studio pubblico: `riferimenti/RESERVED-rischi-geopolitici.md` con cinque rischi geopolitici e relative mitigation strategie.

---

## 0.14 Verdetto in una riga

> Lo Studio di Fattibilità raccomanda, come scenario base, l'**HOLD CON PIANO REGOLATORIO RAFFORZATO** sul Percorso 6A (P 45-60%, re-review M+13-16; eventuale GO pieno P 5-15% solo se le cinque hard conditions risultano soddisfatte simultaneamente in M+10-11) e l'**HOLD CON CRITERI USCITA STRINGENTI** sul Percorso 6B con pivot strutturale verso il modello "operatore di servizi su piattaforme prime contractor" (R&D Fase 0/A in M+24-48 subordinata al gate G5, non come path autonomo verso l'operatività). Il posizionamento strategico a 10 anni resta "complementare a IRIS²", con scenario realistico B2-relaxed "Standalone IT Operator Small Fleet" (€30-80M ARR Y10, P 30-50%) contro lo scenario B2 full "EU sovereign stratospheric layer 100+ HAPS" (P 6-15%).

---

*Firmamento Technologies, Studio di Fattibilità HALE/VTOL, Volume 1 Capitolo 0, bozza M+11, maggio 2026.*
