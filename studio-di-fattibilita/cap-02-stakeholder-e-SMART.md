# Capitolo 2 — Contesto, Stakeholder e Obiettivi SMART

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 2
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (sezioni "Quadro Esigenziale" e "obiettivi e indicatori")
> **Metodologia:** NASA SE Handbook Rev 2 [^1] §4.1 Stakeholder Expectations Definition + ISO/IEC/IEEE 15288 §6.4.1 Stakeholder Needs and Requirements Definition + SMART framework (Doran 1981) adattato a NASA Project Management
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor` (falsifiability, triangulation, source provenance, confidence levels, pre-mortem, steel-manning, base-rate)
> **Red Team review:** verifica condotta dall'agente `red-team-skeptic` — vedi §2.6

---

## 2.0 Sintesi del capitolo

Il presente capitolo definisce **il "perché" e il "per chi"** del progetto HALE/VTOL Firmamento Technologies, costituendo il **ponte logico** tra il Quadro Esigenziale del Cap. 1 (ai sensi dell'art. 41 D.Lgs. 36/2023) e l'apparato dei requisiti del Cap. 3 (NASA SE / RTM). Tre prodotti principali:

1. **Inquadramento del contesto strategico**: Aree Interne italiane come "Quadro Esigenziale ex art. 41" — criticità strutturali, politiche pubbliche di riferimento (SNAI 2021-2027, PSNAI 2025, PNRR, FESR Liguria, ENAC AAM 2021-2030) e posizionamento Firmamento.
2. **Mappa stakeholder consolidata**: estensione e raffinamento del set baseline §3.3 con 30 stakeholder classificati su 5 categorie, power/interest grid, top-5 stakeholder critici con strategia di engagement.
3. **Obiettivi SMART**: 30 obiettivi misurabili distribuiti su 4 orizzonti — Piano di Fattibilità (M+0→M+11), Percorso 6A (M+0→M+24), Percorso 6B (M+0→M+48) e visione 10 anni (Y1→Y10), ciascuno con KPI quantitativi, soglie di verifica e falsifying observation.

**Tesi del capitolo:** lo Studio di Fattibilità HALE/VTOL non è una scelta isolata di Firmamento Technologies, ma un'iniziativa che si **inserisce in una cornice di policy pubblica documentata** (SNAI/PSNAI, ENAC AAM, PNRR Aerospazio) e che dispone di **un set di stakeholder identificati con interesse esplicito** (Regione Liguria, Coopfond, 10 cooperative Legacoop, Protezione Civile Liguria) sufficiente a giustificare il proseguimento del Percorso 6A e la preparazione del Percorso 6B, fermo restando il **rigore delle Open Questions** e dei gate Go/No-Go formalizzati al Cap. 3.2.

**Stato dei lavori al M+3**: stakeholder map al **80% di completezza** (mancano LoI formali da Regione Liguria, ENAC, Coopfond 2026); obiettivi SMART **provvisori M+3**, da riconvalidare post-workshop Cooperative (M+6) e post pre-application meeting ENAC (M+6).

---

## 2.0bis Boundary conditions del progetto (richiamo)

Il capitolo presuppone — come **scelte strategiche-politiche** del fondatore, non come ipotesi da validare — due posizioni di progetto già consolidate in Cap. 3.0bis, Cap. 5.0bis, Cap. 7.0bis:

- **B1 — Modello cooperativo service-only + rete Legacoop**: Firmamento Technologies è **operatore di servizi**, non OEM aeronautico. La piattaforma HALE/VTOL non viene venduta ma utilizzata per erogare servizi ricorrenti (DaaS, IaaS, canone, outcome-based, ore-volo + analytics). La rete delle 10 cooperative Legacoop (capofila Fabrica) è scelta strutturale del progetto. Gli obiettivi SMART del presente capitolo riflettono questa scelta — non sono validate ipotesi alternative ("vendita diretta UAV", "spin-off OEM", etc.).
- **B2 — Visione 10 anni "nodo italiano di un futuro consorzio sovrano europeo HAPS"**: obiettivo strategico di lungo termine, complementare a IRIS² (LEO sovrano EU) e Galileo/Copernicus. Lo Studio di Fattibilità approva i passi 1-2 della roadmap (Percorso 6A operativo + Percorso 6B preparatorio R&D); la visione completa è vettore strategico — descritta in `riferimenti/visione-10-anni.md`.

Gli obiettivi SMART di lungo termine in §2.4.5 sono ancorati alla visione 10 anni come **orizzonte direzionale**, NON come commitment esecutivo del presente Studio.

---

## 2.1 Contesto strategico

### 2.1.1 Aree Interne italiane: criticità strutturali

Le **Aree Interne** italiane sono definite dalla Strategia Nazionale Aree Interne (SNAI) come «la parte maggioritaria del territorio italiano caratterizzata dalla significativa distanza dai centri di offerta di servizi essenziali»[^2]. La mappa SNAI 2020 — utilizzata dalla programmazione 2021-2027 — classifica i Comuni in: **cintura** (≤20 minuti da un polo di servizi), **intermedi** (≤40 min), **periferici** (≤75 min), **ultraperiferici** (>75 min). Le **Aree Interne** sono l'aggregato degli intermedi + periferici + ultraperiferici e rappresentano **circa il 53% dei Comuni italiani**[^2, §1.5].

**Dati strutturali rilevanti per il Quadro Esigenziale (fonte: PSNAI 2025 [^2])**:

| Dimensione | Indicatore | Valore | Implicazione progetto |
|---|---|---|---|
| **Estensione** | % Comuni IT in Aree Interne (mappa 2020) | ~53% | Mercato addressable potenzialmente ampio |
| **Estensione** | % superficie nazionale in Aree Interne | ~60% | Necessità copertura geografica estesa |
| **Demografia** | % popolazione IT in Aree Interne | ~22% (≈13M abitanti) | Densità bassa → infrastrutture terrestri non economiche |
| **Trend** | Variazione popolazione 2011-2024 | −3,7% Aree Interne vs −0,5% Italia | Spopolamento marcato — domanda di servizi territoriali |
| **Proiezione** | Comuni in declino demografico 2023→2043 | 75% del totale Comuni IT | Crisi strutturale di lungo periodo |
| **Mobilità** | Tempo medio accesso polo da ultraperiferici | >75 min | Servizi essenziali (sanità, scuola) difficili da raggiungere |
| **Digital divide** | Comuni con copertura banda ultra-larga ≥100 Mbps in Aree Interne | <40% (2024) | Connettività carente → opportunità HAPS |
| **Rischio idrogeologico** | % comuni Aree Interne con PAI alta/molto-alta | ~75% | Domanda monitoraggio frane / antincendio |

Le criticità che lo Studio affronta direttamente — e che giustificano la scelta di una piattaforma aerea persistente — sono tre, mutuate dal Briefing originale [^3] e validate dal PSNAI:

1. **Spopolamento e perdita di presidio del territorio** — abbandono di infrastrutture, riduzione della manutenzione, perdita di vigilanza ambientale.
2. **Divario digitale** — copertura banda larga / mobile carente in aree periferiche e ultraperiferiche, soprattutto in vallate alpine e appenniniche.
3. **Rischio idrogeologico e da incendi boschivi** — territori fragili, dispersione abitativa, difficoltà di intervento tempestivo da parte di Protezione Civile, Vigili del Fuoco, Carabinieri Forestali.

> **Falsifying observation §2.1.1**: se al M+24 l'analisi di mercato (Cap. 7) mostra che la **disponibilità reale** delle Amministrazioni Aree Interne a contrattare servizi EO/NTN da operatore privato è **strutturalmente inferiore a €20-30k/comune/anno** (sotto la soglia di sostenibilità del modello service-only), il pivot del progetto verso clienti B2B (utility, telco, agroforestale) diventa obbligatorio. **Probabilità: medium, Impatto: high**.

### 2.1.2 Politiche pubbliche di riferimento

Il progetto si inserisce in **cinque cornici di policy pubblica documentate**, citate qui in ordine di rilevanza diretta:

#### (a) SNAI 2021-2027 / PSNAI luglio 2025

La Strategia Nazionale Aree Interne, originaria del ciclo di programmazione 2014-2020, è stata **rifinanziata e ristrutturata** nel ciclo 2021-2027 [^2]:
- **Risorse nazionali 2021-2027**: €310M (in aggiunta ai €281,2M del ciclo 2014-2020), di cui 56 nuove Aree (di cui 13 con sole risorse regionali) [^2, §3.2].
- **Modalità di trasferimento**: anticipazione condizionata all'inserimento degli interventi nel sistema di monitoraggio nazionale.
- **Governance**: Cabina di regia centrale + Comitato Tecnico Aree Interne + Autorità Regionali Aree Interne (ARAI) + Aree Interne con Ente capofila [^2, §5.4].
- **Linee guida settoriali**: Trasporti, Scuola, Salute [^2, §6.1.1-3].

**Rilevanza per il progetto**: lo Studio di Fattibilità HALE/VTOL si presenta come **infrastruttura abilitante orizzontale** rispetto ai tre settori prioritari SNAI (mobilità, scuola, salute). Il PSNAI riconosce esplicitamente che i servizi essenziali nelle Aree Interne richiedono **innovazione tecnologica** + **partenariato pubblico-privato-cooperativo** [^2, §5.4.10] — apertura che il progetto può sfruttare.

#### (b) PNRR — Missione 1 (Digitalizzazione) e Missione 2 (Transizione ecologica)

Il **Piano Nazionale di Ripresa e Resilienza** include misure trasversali rilevanti per le Aree Interne [^2, §3.6]:
- **Missione 1 — Componente 2 — Digitalizzazione**: copertura banda ultra-larga, "Italia 1 Giga" (€6.7B), "Italia 5G" (€2B) — il progetto si propone come **complemento aereo** per copertura ultima-miglio in aree non economicamente servibili da torri terrestri.
- **Missione 2 — Componente 4 — Tutela del territorio**: investimenti su prevenzione rischio idrogeologico (€2.5B) e antincendio boschivo (€0.5B) — diretto match con use case del progetto.
- **Missione 5 — Componente 3 — Aree Interne**: investimento dedicato (€830M) con governance integrata SNAI.

#### (c) FESR Liguria 2021-2027 + DGR Regionali

Il **Programma Regionale FESR Liguria 2021-2027** [^4] alloca €0.6B circa, con priorità su:
- **OP1 — Europa più intelligente** (innovazione, digitalizzazione PMI)
- **OP2 — Europa più verde** (transizione energetica, rischio idrogeologico)
- **OP5 — Europa più vicina ai cittadini** (strategie territoriali, incluse Aree Interne)

**Rilevanza**: la Regione Liguria gestisce direttamente le risorse SNAI delle aree liguri (Antola-Tigullio, Beigua-Sol, Val di Vara, Valle Arroscia, Imperiese, Fontanabuona, Bormida, Valle Scrivia) [^5] — 8 aree complessive con ~16.000 km² e ~110.000 abitanti. Pentema (comune di Torriglia, area Antola-Tigullio) è dentro questo perimetro.

#### (d) ENAC AAM 2021-2030 (Advanced Air Mobility)

Il **Piano Strategico Nazionale Advanced Air Mobility** [^6], pubblicato da ENAC in 3 documenti (Piano + Roadmap + Business Plan), prevede investimenti complessivi di **€1.863,4M** in 3 wave di sviluppo per l'infrastruttura AAM italiana:
- Wave 1 (2021-2025): primi vertiporti, regolatoria base, pilot operations.
- Wave 2 (2025-2028): scale-up vertiporti, integrazione U-Space, primi operatori certified.
- Wave 3 (2028-2030): operazioni commerciali piene.

**Rilevanza**: il piano AAM **non include esplicitamente HAPS** (focus su eVTOL urbani/regionali), ma cita gli **UAS** come parte dell'ecosistema AAM. Firmamento Technologies può posizionarsi come **operatore UAS-AAM in area non-urbana** (aree interne / aerospaziale persistente), differenziandosi dal mainstream eVTOL urbano e completando lo spettro dell'AAM italiano.

#### (e) Quadro normativo (cf. Cap. 5)

Il dettaglio normativo è in Cap. 5; in sintesi, il progetto opera nella **categoria Specific** EASA per il Percorso 6A e in **categoria Certified** per il Percorso 6B. Le Regole rilevanti — Reg. UE 2019/947, 2019/945, 2021/664, ENAC APR Ed.3 + Emend.1, AMC/GM Amendment 3 (sett. 2025) — sono integralmente recepite. La policy pubblica più "abilitante" per il progetto è **EASA SORA 2.5 europea** (ED Decision 2025/018/R) che semplifica drasticamente la application BVLOS in categoria Specific [^7].

### 2.1.3 Posizionamento Firmamento in questo contesto

Firmamento Technologies si posiziona come:

1. **Operatore di servizi territoriali** (B1) — non OEM, non system integrator solo, non semplice fornitore di drone. Il modello equivalente è **Starlink come operatore broadband** (non OEM satellitare puro), traslato sul layer stratosferico aereo.
2. **Aggregatore della rete cooperativa Legacoop** — capofila tecnico-aerospaziale, con Fabrica capofila cooperativa per i bisogni dei territori.
3. **Anchor del cluster aerospaziale ligure** — Liguria è regione ad alta densità aerospaziale (DTA-Genova, Leonardo Helicopters Genova, IIT Genova, Aero Sekur, etc.); il progetto sfrutta questa massa critica industriale.
4. **Candidato a nodo italiano di una futura infrastruttura sovrana EU HAPS** (B2) — orizzonte 10 anni, complementare a IRIS², non sostitutivo.

**Differenziazione vs competitor globali** (vedi Cap. 7.5 per dettaglio):
- vs Aalto HAPS (Airbus), SoftBank Sunglider, Skydweller Aero: Firmamento si differenzia per (i) **modello service-only** (no product sale), (ii) **anchor cooperativo + territoriale**, (iii) **focus Aree Interne** (non urban / non global telco scale).
- vs incumbent IT (Leonardo, TAS, CIRA): Firmamento si propone come **operatore agile complementare**, non concorrente diretto; partnership target per Phase B.

> **Confidence §2.1.3**: medium. Il posizionamento è coerente con i documenti `riferimenti/visione-10-anni.md` e `RESERVED-rischi-geopolitici.md`. Validazione esterna manca (no benchmark indipendente del posizionamento di Firmamento in EU stratospheric ecosystem).

---

## 2.2 Mappa stakeholder consolidata

### 2.2.1 Classificazione stakeholder — 5 categorie + 30 entità identificate

In coerenza con NASA SE Handbook §4.1.1.2.1 [^1] e con la stakeholder map baseline del Cap. 3.3.1 (26 stakeholder), il presente capitolo **estende** la mappa con 4 stakeholder addizionali (S-27 → S-30) emersi dall'analisi PSNAI 2025 e dalle linee guida ENAC AAM, e riclassifica l'intero set su **5 categorie operative**:

| Categoria | Definizione | N° Stakeholder | Funzione nel progetto |
|---|---|---|---|
| **INTERNAL** | Proponente + capitale + team | 1 | Decisione, investimento, esecuzione |
| **CUSTOMER** | Soggetto pagante + utente finale del servizio | 8 | Definisce i requisiti, paga il servizio, valida valore |
| **REGULATOR** | Autorità che autorizza, vigila, certifica | 7 | Definisce limiti, autorizza operazioni, certifica compliance |
| **PARTNER** | Fornitore, co-progettista, finanziatore, alleato strategico | 9 | Co-esegue, finanzia, fornisce tecnologia / capacità |
| **COMMUNITY** | Soggetti coinvolti senza contratto diretto, ma con interesse / impatto | 5 | Accettabilità sociale, narrativa pubblica, advocacy |

**Tabella stakeholder estesa** (S-01 → S-30, ridenominata "consolidata M+3"; aggiunte rispetto a Cap. 3.3.1 evidenziate con **(+)**):

| ID | Stakeholder | Categoria | Ruolo (sintesi) | Leva engagement | Frequenza interazione | Owner agent |
|---|---|---|---|---|---|---|
| S-01 | Firmamento Technologies | INTERNAL | Proponente, capofila tecnico, decisore | (sé) | Continuativa | sovereign-strategist |
| S-02 | Fabrica (cooperativa capofila) | CUSTOMER | Aggregatore rete cooperative, co-progettista requisiti | Contratto di rete + workshop | Settimanale | business-model-strategist |
| S-03 | Rete 10 cooperative Legacoop | CUSTOMER | Utenti-pilota, beneficiari DaaS/IaaS | Workshop + abbonamenti DaaS | Mensile | business-model-strategist |
| S-04 | Regione Liguria | CUSTOMER + REGULATOR | Anchor customer + sponsor istituzionale + co-pianificatore SNAI | Accordo quadro + co-progettazione (art. 55 CTS) + LoI | Mensile | snai-funding-expert |
| S-05 | Comune di Torriglia (Pentema) | CUSTOMER + COMMUNITY | Sede pilota, autorizzazioni locali, beneficiario diretto | Convenzione + workshop pubblico | Mensile in pilota | snai-funding-expert |
| S-06 | Protezione Civile Liguria + ARPA Liguria | CUSTOMER | Cliente pilota PRIMARIO emergenze / monitoraggio | Convenzione operativa + ore-volo | Settimanale in stagione critica | aerospace-SE |
| S-07 | Comunità Pentema (**14 residenti ISTAT**, frazione 3.27 km da Torriglia, 11 famiglie, 100 edifici) | COMMUNITY | Accettabilità sociale, diritti privacy | Workshop pubblico + DPIA pubblica + canali web | Trimestrale (continuativa in pilota) | data-privacy-counsel |
| S-08 | ENAC | REGULATOR | Autorizzazione operativa SORA, certificazione, vigilanza | Pre-application meeting + Operations Manual + SORA application | Mensile inizialmente, poi trimestrale | aviation-regulatory-counsel |
| S-09 | EASA | REGULATOR | Framework europeo, Special Condition HAPS, NPA HAPS | Engagement RMT + comments NPA | Trimestrale | aviation-regulatory-counsel |
| S-10 | AGCOM | REGULATOR | Spettro radio, licensing, posizione HAPS bands | Istanza licenze + position paper | Trimestrale | telecom-ntn-payload-expert |
| S-11 | Garante Privacy | REGULATOR | Tutela dati personali, DPIA pareri | DPIA pubblica + protocollo Garante | Annuale (su richiesta) | data-privacy-counsel |
| S-12 | ENAV / D-Flight | REGULATOR + PARTNER | Integrazione U-Space, traffico aereo | Convenzione USSP/CISP + coordination | Settimanale in operativa | aviation-regulatory-counsel |
| S-13 | MIMIT (Direz. Aerospazio + Comunicazioni) | REGULATOR + PARTNER | Strategia nazionale, PNRR Aerospazio, PNRF, PSN AAM | Position paper + tavoli + bandi PNRR | Trimestrale | sovereign-strategist |
| S-14 | MIT (Trasporti) | REGULATOR | Vigilanza ENAC, politiche trasporti | Indiretto via ENAC | Annuale | aviation-regulatory-counsel |
| S-15 | ACN — Agenzia Cybersicurezza Nazionale | REGULATOR | NIS2 compliance, cyber-incident reporting | Notifica + audit cybersec | Annuale | cybersecurity-officer |
| S-16 | Coopfond + Fondazione PICO ETS | PARTNER (finanziatore) | Bando Cooding Prototypes + Cooding Invest | Erogazione + reporting + LoI | Mensile (gate review) | financial-cfo-analyst |
| S-17 | Commissione UE (DG CNECT, DEFIS, MOVE, GROW) | PARTNER + REGULATOR | Programmi EDF, Horizon, IRIS², EU Space, IPCEI | Risposta a call + dialogo policy | Trimestrale | sovereign-strategist |
| S-18 | ASI — Agenzia Spaziale Italiana | PARTNER + REGULATOR | Coordinamento spazio + EO + budget nazionale spazio | Position paper + tavoli + co-progetti | Trimestrale | sovereign-strategist |
| S-19 | CIRA — Centro Italiano Ricerche Aerospaziali | PARTNER (R&D) | Phase B HALE consortium, ricerca aero | Accordo R&D + co-progettazione | Mensile (in Phase B) | aerospace-SE |
| S-20 | POLITO — DIMEAS | PARTNER (R&D) | HELIPLAT lineage, R&D HALE, tesi/dottorati | Convenzione accademica + assegni | Mensile (in Phase B) | aero-structures-engineer |
| S-21 | DTA Puglia + GATB Grottaglie | PARTNER (test bed) | BVLOS test bed, area volo controllata | Convenzione test bed | Trimestrale | vtol-uas-specialist |
| S-22 | TIM, Vodafone, Iliad, WindTre, Open Fiber | PARTNER + Cust. potenziale | NTN backhaul, capacity wholesale, partnership futura | LoI commerciali, MoU | Trimestrale | telecom-ntn-payload-expert |
| S-23 | Leonardo + Telespazio + TAS | PARTNER + COMPETITOR | Incumbent aerospace IT, consorzio sovrano EU, acquisition risk | Dialogo strategico + position paper | Trimestrale | sovereign-strategist |
| S-24 | Vigili del Fuoco + Carabinieri Forestali | CUSTOMER | Antincendio, monitoraggio territoriale | Convenzione operativa + protocollo | Mensile in stagione | aerospace-SE |
| S-25 | ASL3 Genovese | CUSTOMER | Telemedicina rurale, supporto emergenze sanitarie | Convenzione + protocollo SSN | Trimestrale | business-model-strategist |
| S-26 | Ente Parco Antola, Ente Parco Aveto | CUSTOMER + COMMUNITY | Vigilanza ambientale, anti-bracconaggio, monitoraggio fauna | Convenzione + ore-volo | Stagionale | aerospace-SE |
| **S-27 (+)** | **DTA Liguria / Aero-cluster Liguria** | PARTNER | **Cluster aerospaziale regionale, lobbying, formazione** | **Membership + co-progetti** | **Trimestrale** | **business-model-strategist** |
| **S-28 (+)** | **UNCEM Liguria (Unione Naz. Comuni e Comunità Montane)** | COMMUNITY + CUSTOMER | **Aggregatore dei Comuni delle Aree Interne, advocacy** | **Position paper + workshop** | **Trimestrale** | **snai-funding-expert** |
| **S-29 (+)** | **Cassa Depositi e Prestiti (CDP) + EIB** | PARTNER (finanziatore futuro) | **Equity / debt strategico per Phase 3-4** | **Investor relations da M+24** | **Annuale (inizio); trimestrale in raising** | **financial-cfo-analyst** |
| **S-30 (+)** | **Stampa locale + nazionale + tech media** | COMMUNITY | **Narrativa pubblica, accettabilità sociale, branding** | **Press release + interviste + factsheet** | **Mensile** | **communications-lead** |

**Note di lettura**:
- Le **doppie categorie** (es. S-04 CUSTOMER+REGULATOR, S-12 REGULATOR+PARTNER) riflettono che alcuni stakeholder hanno ruoli ibridi nel ciclo di vita del progetto.
- La colonna **Owner agent** si riferisce agli agenti definiti in `.claude/agents/`, ciascuno responsabile della relazione operativa con lo stakeholder.
- La frequenza è **interazione strutturata** (workshop, meeting, report); le interazioni ad-hoc operative possono essere più frequenti.

### 2.2.2 Power/Interest grid

In coerenza con la metodologia Mendelow / NASA SE §4.1.1.2.1 [^1], gli stakeholder sono classificati su **due dimensioni**:
- **Power** (potere di influenzare l'esito del progetto): Low / Medium / High
- **Interest** (interesse a partecipare / impatto positivo dal progetto): Low / Medium / High

Quattro quadranti emergenti:
- **High Power + High Interest** = **Manage Closely** (engagement intenso, gestione proattiva)
- **High Power + Low Interest** = **Keep Satisfied** (informato ma non sovraingaggiato)
- **Low Power + High Interest** = **Keep Informed** (canali continui, leva narrativa)
- **Low Power + Low Interest** = **Monitor** (osservazione, no risorse dedicate)

| Stakeholder | Power | Interest | Quadrante | Strategia |
|---|---|---|---|---|
| **S-01 Firmamento** | High | High | Manage Closely | Internal (boundary) |
| **S-04 Regione Liguria** | High | High | **Manage Closely** | LoI + engagement diretto Assessorato Innovazione + Aree Interne |
| **S-08 ENAC** | High | Medium | **Manage Closely** | Pre-application + relazione continua direzione UAS |
| **S-16 Coopfond** | High | High | **Manage Closely** | Gate review + reporting trasparente |
| **S-09 EASA** | High | Low | Keep Satisfied | Engagement RMT + comments NPA (non perdere visibilità) |
| **S-10 AGCOM** | High | Low | Keep Satisfied | Istanza licenze + position paper banda HAPS |
| **S-11 Garante Privacy** | High | Medium | **Manage Closely** | DPIA pubblica + protocollo preventivo |
| **S-12 ENAV / D-Flight** | High | Medium | Manage Closely | Convenzione USSP/CISP appena attivata operazioni BVLOS |
| **S-13 MIMIT** | High | Medium | Manage Closely | Position paper + presenza tavoli AAM/Aerospazio |
| **S-17 Commissione UE** | High | Low (oggi) → High (Y3+) | Keep Satisfied | Mappatura programmi + risposta call selezionate |
| **S-23 Leonardo/TAS/Telespazio** | High | Medium (ambiguo) | **Manage Closely** | Dialogo strategico, no naive disclosure (vedi `RESERVED-...md`) |
| **S-02 Fabrica + S-03 Coop** | Medium | High | **Manage Closely** | Workshop strutturati + governance condivisa + abbonamenti DaaS |
| **S-06 PC Liguria + ARPA** | Medium | High | **Manage Closely** | Convenzione operativa + casi d'uso prioritari |
| **S-05 Comune Torriglia** | Low | High | Keep Informed | Delibera consiglio comunale + workshop pubblico Pentema |
| **S-07 Comunità Pentema** | Low | High | **Keep Informed** | Workshop pubblico + DPIA + canali web + sportello |
| **S-19 CIRA + S-20 POLITO** | Medium | Medium | Manage Closely (Y2+) | Convenzione R&D progressiva, attivata in Phase B |
| **S-21 DTA Puglia / GATB** | Medium | Medium | Manage Closely | Convenzione test bed BVLOS |
| **S-22 Telco IT** | Medium | Low (oggi) → High (Y5+) | Monitor (oggi) → Manage (Y5+) | Watch + LoI esplorativi |
| **S-24 VVF + CCFor** | Medium | High | Keep Informed | Convenzione operativa stagionale |
| **S-25 ASL3** | Medium | Medium | Keep Informed | Protocollo SSN telemedicina |
| **S-26 Enti Parco** | Low | High | Keep Informed | Convenzione vigilanza ambientale |
| **S-14 MIT** | Medium | Low | Monitor | Indiretto via ENAC |
| **S-15 ACN** | Medium | Low | Monitor → Keep Satisfied (NIS2 obblighi) | Notifica + audit |
| **S-18 ASI** | Medium | Low (oggi) → Medium (Y3+) | Monitor → Manage Closely (Y3+) | Position paper EO + ASI New Space |
| **S-27 DTA Liguria** | Low | High | Keep Informed | Membership cluster |
| **S-28 UNCEM Liguria** | Low | High | Keep Informed | Position paper + workshop |
| **S-29 CDP + EIB** | High (Y3+) | Low (oggi) | Monitor (oggi) → Manage (Y3+) | Investor relations da M+24 |
| **S-30 Stampa** | Medium | Medium | Manage Closely (selettivo) | Press strategy + factsheet |

**Visualizzazione concettuale del power/interest grid** (semplificata):

```
                         HIGH INTEREST
                              │
   Coopfond (S-16)            │            Regione Liguria (S-04)
   Coop Legacoop (S-02,03)    │            ENAC (S-08)
   Comunità Pentema (S-07)    │            Garante Privacy (S-11)
   PC + ARPA (S-06)           │            Coopfond (S-16)
   VVF + CCFor (S-24)         │            MIMIT (S-13)
   Enti Parco (S-26)          │            ENAV (S-12)
   UNCEM (S-28)               │            Leonardo/TAS (S-23 ambiguo)
                              │
─────────────────────────────────┼──────────────────────────────────
   LOW POWER                  │                          HIGH POWER
                              │
   Stampa locale (S-30)       │            EASA (S-09)
   MIT (S-14)                 │            AGCOM (S-10)
   ACN (S-15)                 │            CDP/EIB (S-29) [Y3+]
   ASI (S-18) oggi            │            Commissione UE (S-17) [Y3+]
   Telco IT (S-22) oggi       │            ASI (S-18) [Y3+]
                              │
                         LOW INTEREST
```

### 2.2.3 Stakeholder critici — Top-5 con strategia di engagement

Cinque stakeholder sono **show-stopper o show-maker** per il successo del Percorso 6A entro M+24:

#### Top-1 — Regione Liguria (S-04)

**Razionale di criticità**: senza anchor customer regionale, il modello B2G perde l'asse principale (40-50% ARR target Y3). Senza LoI Regione, la sostenibilità finanziaria Y1-Y2 è a rischio (cf. Cap. 7.9.2 e SyR-Cost-003).

**Soggetti chiave**: Assessorato Innovazione, Aree Interne, Protezione Civile, Trasporti; Direzioni Generali Coesione, Sviluppo Economico, Ambiente; ARAI Liguria.

**Engagement plan M+0 → M+12**:
- M+0-3: mappatura interlocutori + briefing iniziale + introduzione via Coopfond/Legacoop
- M+3-6: tavolo tecnico ristretto (3-5 partecipanti); presentazione caso Pentema; discussione DGR
- M+6: **LoI Regione Liguria firmata** (Open Question OQ-010, deadline M+6)
- M+6-9: protocollo operativo Protezione Civile + ARPA per pilota Pentema (use case prioritari UC-001/002)
- M+9-12: convenzione quadro pluriennale (3-5 anni) per servizi EO + emergenza

**KPI engagement**: LoI firmata M+6 (binary); convenzione operativa M+12 (binary); ≥ 1 visita tecnica congiunta a Pentema entro M+9.

> **Falsifying observation**: se al M+8 la Regione Liguria **non** ha firmato LoI nonostante engagement attivo (≥ 5 incontri documentati), attivazione **plan B**: pivot verso altre Regioni SNAI (Piemonte — Val Borbera, Marche — Sibillini, Calabria — Sila). Probabilità: medium-low (engagement informale già avviato M-3), impatto: high.

#### Top-2 — ENAC (S-08)

**Razionale di criticità**: senza ENAC favorevole, il SORA SAIL Pentema potrebbe essere classificato a livelli più alti (IV-V) — non operativi nel budget e nella tempistica 6A; senza autorizzazione BVLOS, il pilota Pentema è inattuabile.

**Soggetti chiave**: Direzione UAS ENAC; CIA (Centro Italiano Aerospazio) / DT (Direzione Tecnica); Direzione Generale ENAC.

**Engagement plan M+0 → M+12**:
- M+0-3: richiesta **pre-application meeting** (Open Question OQ-002, deadline M+6). Materiali: ConOps preliminare + descrizione missione + risk approach.
- M+3: **pre-application meeting** condotto; feedback documentato; SAIL preliminare confermato/rivisto
- M+3-6: redazione **Operations Manual** + **SORA application** + **Operator Declaration**
- M+6-9: submission SORA application
- M+9-12: review + integrazioni + autorizzazione

**KPI engagement**: pre-application meeting condotto M+3 (binary); SAIL ≤ III confermato M+6 (binary); autorizzazione operativa ricevuta M+12 (binary).

> **Falsifying observation**: se ENAC alla pre-application valuta Pentema **SAIL ≥ IV** non riducibile con mitigation reasonable, ri-design ConOps (es. operazioni VLOS + EVLOS), accettando riduzione perimetro casi d'uso, oppure riallocazione sito pilota (es. area meno popolata, GATB Grottaglie come test bed primario).

#### Top-3 — Coopfond + Fondazione PICO ETS (S-16)

**Razionale di criticità**: finanziatore del Piano di Fattibilità (€80-150k Cooding Prototypes + potenzialmente Cooding Invest M+12 in equity). Senza rinnovo o estensione bando, M+12 → M+24 ha funding gap.

**Soggetti chiave**: Coopfond CdA; Fondazione PICO ETS (operativo bando Cooding); Legacoop Liguria.

**Engagement plan**:
- M+0-1: erogazione contributo bando (post-firma CdA Firmamento 24 ottobre 2025 [^8])
- M+1-3: kick-off Piano di Fattibilità + reporting M+3
- M+3-6: report intermedio + verifica avanzamento + DR-002 (verifica Cooding 2026 disponibilità) chiusura
- M+6-9: workshop con Coopfond + altre cooperative finanziate
- M+9-11: report finale Piano di Fattibilità + raccomandazione gate
- M+11-12: candidatura **Cooding Invest** (equity ticket follow-on) — se ammissibile

**KPI engagement**: tutti i deliverable contrattuali consegnati on-time (binary); ≥ 1 visita Coopfond a Pentema entro M+9; partecipazione attiva a evento Cooding annuale.

#### Top-4 — Rete 10 cooperative Legacoop + Fabrica (S-02 + S-03)

**Razionale di criticità**: utenti-pilota, fonte primaria dei bisogni operativi. Senza partecipazione attiva delle cooperative, lo Studio di Fattibilità è "sopra le teste" del territorio e perde **legittimità co-progettuale** (art. 55 CTS, co-progettazione PA-Terzo Settore).

**Soggetti chiave**: Fabrica (capofila); F.U.T.U.R.A.; Monte di Capenardo; Coesi (Comunità Energetica); Val Pentemina (cooperativa di Pentema); Manario 2002; Terre del Magra; Verde Mare; Condiviso; Earth.

**Engagement plan**:
- M+0-3: workshop iniziale individuali con ciascuna cooperativa (10 sessioni semi-strutturate, 2-3h ciascuna)
- M+3-6: **workshop plenario** con tutte le 10 cooperative — validazione StNeeds Cap. 3 + bisogni operativi specifici
- M+6: **MoU** firmati con ciascuna cooperativa (OQ-011 closure)
- M+6-9: prototipo servizio DaaS per 2-3 cooperative pilota (Val Pentemina, Monte di Capenardo, Coesi)
- M+9-12: feedback + iterazione + estensione

**KPI engagement**: 10/10 cooperative coinvolte in workshop entro M+6 (binary); ≥ 8/10 MoU firmati entro M+6 (gate criterion §3.2.5); ≥ 2 cooperative attivamente piloti DaaS entro M+9.

> **Falsifying observation**: se al M+6 meno di **8 su 10** cooperative confermano partecipazione formalizzata (MoU), il modello di rete cooperativa è in crisi e va riesaminata l'aggregazione (ridurre ambito, cambiare capofila, etc.). Probabilità: low (engagement esistente forte), impatto: high.

#### Top-5 — Comunità Pentema (S-07)

**Razionale di criticità**: comunità di **14 residenti ISTAT** — accettabilità sociale del pilota su comunità così minuscola è critica per visibilità mediatica. Senza accettabilità — anche solo con uno o due cittadini ostili che attivano media o Garante — il pilota è bloccato. Vedi caso recenti drone deployments urbani 2023-2024 (sospensione rapida).

**Soggetti chiave**: Comune di Torriglia (Sindaco + Consiglio); cooperativa Val Pentemina (cooperativa di comunità di Pentema); abitanti — incluse leve di influencer locali (parroco, presidente Pro Loco, etc.).

**Engagement plan**:
- M+0-3: introduzione tramite Comune + Val Pentemina; sopralluogo tecnico
- M+3: **workshop pubblico** a Pentema (incontro aperto residenti) — presentazione progetto, casi d'uso, modalità operative
- M+3-6: **DPIA pubblica** preliminare + canali web + sportello informativo
- M+6: delibera Consiglio Comunale Torriglia + accordo con Pro Loco
- M+6-12: comunicazione continuativa + meccanismi di feedback (questionario, sportello, social)

**KPI engagement**: workshop pubblico Pentema condotto M+3 (binary); DPIA pubblica online M+6 (binary); ≥ 0 segnalazioni negative formali al Garante (target lifetime pilota).

> **Falsifying observation**: se al workshop pubblico M+3 emerge **opposizione strutturata** (es. mozione del Consiglio comunale contraria, raccolta firme, intervento Garante preventivo), riprogettazione completa del pilota — riduzione perimetro, scelta diversa di sito, rinforzo trasparenza. Probabilità: low (Pentema è cooperativa di comunità attiva, contesto culturale aperto a innovazione), impatto: high.

---

## 2.3 La rete delle 10 cooperative pilota Legacoop

### 2.3.1 Capofila Fabrica — ruolo di aggregazione

**Fabrica** (Società Cooperativa, CF 01482600119, Digital Ace) [^9] è capofila della rete cooperative pilota del progetto. Il ruolo di Fabrica è:

1. **Aggregazione organizzativa** — punto di contatto unico tra Firmamento Technologies e le 10 cooperative, riducendo overhead di coordinamento;
2. **Co-progettazione dei requisiti utente** — Fabrica conduce workshop con le cooperative, sintetizza bisogni, valida StNeeds (Cap. 3.3);
3. **Governance condivisa** — Fabrica partecipa al **Comitato di Pilotaggio** del progetto, decisore congiunto su milestone, scope, priorità use case;
4. **Comunicazione e advocacy verso Legacoop** — Fabrica connette il progetto al network Legacoop nazionale e regionale, abilitando scale-up Y2-Y3.

**Modello di governance Firmamento-Fabrica**:
- **Contratto di rete** (non JV, non RTI) — strumento agile, reversibile, low-overhead.
- **Comitato di Pilotaggio** mensile: 2 da Firmamento + 1 Fabrica + 1 rappresentante cooperative + 1 osservatore Coopfond (opzionale).
- **Decisioni con maggioranza qualificata** su scope cambiamenti rilevanti; **veto** di Fabrica solo su scelte che impattano direttamente bisogni cooperative (es. eliminazione di un use case prioritario).

### 2.3.2 Le 10 cooperative — profilo e bisogni operativi

Sulla base dell'elenco ufficiale [^9] e dell'analisi preliminare condotta nei primi mesi del Piano di Fattibilità, ecco il profilo sintetico:

| ID | Cooperativa | CF | Tipologia | Bisogno operativo principale dal sistema HALE/VTOL |
|---|---|---|---|---|
| C-01 | **Fabrica** (capofila) | 01482600119 | Cooperativa di lavoro (Digital Ace) | Coordinamento + servizi digitali alle altre cooperative |
| C-02 | F.U.T.U.R.A. | 02968850996 | Coop. di comunità ETS | Servizi digitali di prossimità per area appenninica |
| C-03 | Monte di Capenardo | 02480650106 | Coop. agricola | Monitoraggio EO multispettrale fondi agricoli + agroforestale |
| C-04 | Coesi (Comunità Energetica) | 01907300097 | CER | Monitoraggio infrastrutture energetiche distribuite |
| C-05 | **Val Pentemina** | 02956860999 | Coop. comunità Pentema | Servizi di prossimità Pentema + accettabilità sociale del pilota |
| C-06 | Manario 2002 | 01144840111 | Coop. (Ardesia / artigianato Fontanabuona) | Mappatura cave e monitoraggio sicurezza |
| C-07 | Terre del Magra | 01463680114 | Coop. di comunità (Val di Magra, SP) | Monitoraggio territoriale + protezione civile locale |
| C-08 | Verde Mare | 01532960117 | Coop. di comunità (costa-entroterra LA) | Vigilanza ambientale + turismo connesso |
| C-09 | Condiviso | 02272310992 | Coop. consortile | Servizi consortili tra cooperative |
| C-10 | Earth | 01051410114 | Coop. impresa sociale | Servizi territoriali + sostenibilità ambientale |

**Cooperative di supporto** (non finanziate, ma in rete estesa) [^9]: Olivicoltori Sestresi, Superfici Cooperativa, Ambiente Turismo Impresa 5 Terre, Ture Nirvane, Il Ce.Sto. Queste rappresentano un **pool di estensione M+12+** una volta validato il pilota Pentema.

**Distribuzione geografica** (approssimata, dalla lettura dei CF e dal contesto):
- 7 cooperative in Liguria (Genova, Spezia, Imperia, Savona — sovrapposte alle Aree Interne 14-20 e 21-27)
- 2 cooperative in territori limitrofi (Toscana, area Lunigiana-Magra)
- 1 cooperativa cross-regionale (Earth)

**Tipologia prevalente**: cooperative **di comunità** (Reg. UE 2019/945; D.Lgs. 112/2017 sull'impresa sociale; L. 142/2001), che presidiano servizi essenziali a livello locale. Questa tipologia è esplicitamente abilitata dall'art. 55 CTS (Codice Terzo Settore) alla **co-progettazione con la PA**, modalità che il progetto adotta come strumento di engagement con la Regione Liguria.

### 2.3.3 Modello di governance Firmamento + cooperative

Tre alternative di governance sono state considerate al M+3:

| Alternativa | Pro | Contro | Verdetto M+3 |
|---|---|---|---|
| **Contratto di rete** (L. 33/2009) | Agile, reversibile, no overhead amministrativo; ogni partecipante mantiene autonomia | Vincoli giuridici deboli; reciproci obblighi limitati | **Scelta baseline** |
| **JV / Newco** | Vincolo forte, allineamento incentivi, possibile aggregazione capitale | Overhead amministrativo + fiscale; reversibilità difficile; non adatto a fase pilota | Considerata per Y2-Y3 |
| **Consorzio cooperativo** (art. 27 L. 381/91) | Strumento storico Legacoop, riconoscimento istituzionale, accesso bandi cooperativi | Burocrazia notevole; richiede assemblea + statuto consortile | Considerata per Y3+ scale-up |
| **RTI / ATI** (associazione temporanea) | Standard per bandi PA; flessibile sul contratto | Vincolato al singolo bando; non sostiene scale-up continuativo | No per pilota |

> **Falsifying observation §2.3.3**: se al M+12 la rete cooperativa non genera **valore co-progettato misurabile** (es. nessuna iterazione significativa sui requisiti, nessun caso d'uso emergente dai workshop), il contratto di rete è "shell" e va sostituito o eliminato. Probabilità: low-medium, impatto: medium.

**Aspetti contrattuali pratici**:
- **Property of data**: data-commons cooperativo — i dati EO raccolti su territori cooperativi appartengono al data-commons (gestito da Firmamento ma con governance condivisa). Privacy-by-design integrato.
- **Pricing per cooperative**: tariffe agevolate vs PA (es. €5-15k/anno DaaS standard, €30-80k/anno DaaS+Analytics premium) — definite in Cap. 7.6.
- **Reciproci obblighi**: Firmamento eroga servizi tecnici; cooperative forniscono accesso al territorio + workshop + co-validazione + advocacy.

---

## 2.4 Obiettivi SMART del progetto

### 2.4.1 SMART in NASA SE — significato

Il framework **SMART** (Doran, 1981 [^10]) — Specific, Measurable, Achievable, Relevant, Time-bound — è stato adottato dalla NASA Project Management (NPR 7120.5) [^1] come standard per gli obiettivi di programma e di progetto. Ciascun obiettivo SMART deve rispondere a:

| Criterio | Domanda di test | Esempio di violazione |
|---|---|---|
| **S — Specific** | È chiaro cosa va fatto, da chi, per chi? | "Migliorare connettività" (no chi, cosa, dove) |
| **M — Measurable** | Esiste una metrica oggettiva di completamento? | "Servizio di qualità" (no soglia) |
| **A — Achievable** | È realistico nelle risorse e tempi dichiarati? | "Replicare Starlink in 12 mesi" (no, base rate aerospace) |
| **R — Relevant** | È coerente con la missione di progetto e gli stakeholder? | Obiettivo orfano, non collegato a StNeed |
| **T — Time-bound** | Quando viene verificato il completamento? | "Eventualmente, in futuro" |

In coerenza con la skill `epistemic-rigor`, ad ogni obiettivo SMART aggiungiamo:
- **Owner** — chi è responsabile (agent o stakeholder)
- **Confidence** — livello di confidenza nel raggiungimento (high / medium / low)
- **Falsifying observation** — quale evidenza renderebbe l'obiettivo non raggiungibile o sbagliato

### 2.4.2 Obiettivi SMART del Piano di Fattibilità (M+0 → M+11)

Il **Piano di Fattibilità** (lo Studio di Fattibilità stesso, finanziato dal bando Cooding Prototypes [^11]) ha come prodotto finale un dossier che supporta il gate M+10/M+11 (cf. Cap. 3.2). Gli obiettivi SMART operativi:

#### 🎯 PF-01 — Quadro Esigenziale e Stakeholder Map consolidata

> **Specific**: redigere il Quadro Esigenziale (Cap. 1) e la Stakeholder Map (Cap. 2 + 3.3) con ≥ 25 stakeholder identificati e profilati
> **Measurable**: 100% dei 17 StNeed baseline (Cap. 3.3.2) tracciati a almeno 1 stakeholder
> **Achievable**: si basa su documenti esistenti (Briefing, dossier SNAI, bandi)
> **Relevant**: prerequisito per Cap. 3 (RTM) e Cap. 7 (mercato)
> **Time-bound**: completato **M+3** (versione baseline); M+6 versione consolidata post-workshop
>
> **Owner**: aerospace-SE + business-model-strategist | **Confidence**: high (lavoro desk + workshop pianificati)
> **Falsifying obs**: se al M+6 meno di 17 StNeeds sono validati da almeno 1 stakeholder via workshop, baseline va re-eseguita.

#### 🎯 PF-02 — Validazione regolatoria preliminare ENAC

> **Specific**: condurre **pre-application meeting ENAC** per Percorso 6A; ottenere stima SAIL preliminare per Pentema
> **Measurable**: 1 pre-application meeting condotto + verbale; SAIL stima documentata
> **Achievable**: tempistica ENAC standard per pre-application 4-8 settimane
> **Relevant**: SyR-F-002 + criterio di gate M+10 (cf. Cap. 3.2.2)
> **Time-bound**: **M+6**
>
> **Owner**: aviation-regulatory-counsel | **Confidence**: medium (dipendenza da disponibilità ENAC)
> **Falsifying obs**: se al M+9 ENAC non ha calendarizzato pre-application, attivazione canale via MIMIT-DTA Aerospazio.

#### 🎯 PF-03 — Workshop validato delle 10 cooperative

> **Specific**: condurre workshop strutturati con ciascuna delle 10 cooperative pilota; consolidare StNeeds + use cases prioritari + bisogni operativi specifici
> **Measurable**: ≥ 10 workshop condotti (1 per cooperativa); ≥ 8 MoU firmati; ≥ 1 workshop plenario
> **Achievable**: cooperative già aggregate via Fabrica; tempistica realistica 3-4 mesi
> **Relevant**: criterio di gate M+10 §3.2.5; B1 boundary
> **Time-bound**: **M+6** workshop conclusi; **M+9** MoU firmati
>
> **Owner**: business-model-strategist + Fabrica | **Confidence**: medium-high
> **Falsifying obs**: se al M+6 meno di 8 cooperative su 10 confermano partecipazione → revisione modello di rete (cf. §2.3.3).

#### 🎯 PF-04 — LoI Regione Liguria firmata

> **Specific**: ottenere Letter of Intent firmata dalla Regione Liguria che dichiari interesse per la sperimentazione Pentema e disponibilità a contratto pilota Y1-Y2
> **Measurable**: 1 LoI firmata da Assessore competente; scope minimo: caso d'uso UC-001 (monitoraggio frane) + UC-002 (antincendio) + UC-003 (connettività emergenza)
> **Achievable**: engagement informale già avviato; processo formalizzazione 3-6 mesi tipico
> **Relevant**: anchor customer per modello B2G regionale (Cap. 7.2.1); criterio gate M+10 §3.2.3
> **Time-bound**: **M+6**
>
> **Owner**: snai-funding-expert + sovereign-strategist | **Confidence**: medium
> **Falsifying obs**: se al M+8 nessuna LoI, attivazione pivot verso Piemonte/Marche (cf. §2.2.3 Top-1 plan B).

#### 🎯 PF-05 — DPIA pubblica preliminare

> **Specific**: redigere Data Protection Impact Assessment preliminare ai sensi GDPR art. 35 per le operazioni 6A + 6B; pubblicarla online accessibile
> **Measurable**: 1 DPIA pubblica online; ≥ 3 stakeholder esterni consultati (Garante via informale, comunità Pentema, una cooperativa)
> **Achievable**: framework GDPR maturo; ETs di DPIA disponibili
> **Relevant**: SyR-C-003 + criterio gate M+10 §3.2.5
> **Time-bound**: **M+6**
>
> **Owner**: data-privacy-counsel | **Confidence**: high
> **Falsifying obs**: se Garante esprime parere preventivo negativo, ri-design operazioni + ConOps.

#### 🎯 PF-06 — Trade Studies chiave conclusi (DOCFAP)

> **Specific**: chiudere i 5 Trade Studies critici per il Percorso 6A (TS-PLATFORM, TS-MATERIAL, TS-PROP, TS-AVI, TS-PAYLOAD) — coerenti con NASA SE §6.8 [^1] e art. 41 DOCFAP
> **Measurable**: 5 Trade Study Reports redatti; ciascuno con matrice pesata + raccomandazione + open issues
> **Achievable**: lavoro engineering parallelizzabile; 4-6 mesi disponibili
> **Relevant**: criterio gate M+10 §3.2.1; chiude OQ-001/003/005/006/007 (Cap. 3.10)
> **Time-bound**: **M+10** tutti chiusi
>
> **Owner**: aerospace-SE + 5 owners specifici | **Confidence**: medium
> **Falsifying obs**: se uno o più TS rimangono "indecisi" per mancanza dati, gate M+10 verdetto HOLD per quel sottosistema.

#### 🎯 PF-07 — Risk Register baseline e mitigation plan

> **Specific**: redigere Risk Register con ≥ 30 rischi identificati + scoring P×I + mitigation plan per rischi rossi
> **Measurable**: Risk Register Vol. 2 con almeno 30 risk items; 0 rischi rossi senza mitigation plan
> **Achievable**: skill `risk-register-builder` + analisi FMECA/FTA in corso
> **Relevant**: criterio gate M+10 §3.2.1
> **Time-bound**: **M+10**
>
> **Owner**: aerospace-SE + risk-officer | **Confidence**: high
> **Falsifying obs**: emersione di un nuovo rischio rosso non mitigabile (es. ENAC nega SAIL feasible) → re-design.

#### 🎯 PF-08 — Quadro Economico ex art. 41 + business case completo

> **Specific**: redigere Quadro Economico Aeronautico (Cap. 8) con CapEx + OpEx + NPV + IRR + payback per Percorso 6A; piano finanziario Y1-Y4 con scenari worst/base/best
> **Measurable**: Cap. 8 redatto; NPV/IRR/payback calcolati; sensitivity completata
> **Achievable**: dati Cap. 7 + benchmark; tempistica 3-4 mesi
> **Relevant**: criterio gate M+10 §3.2.3; conformità art. 41 D.Lgs. 36/2023
> **Time-bound**: **M+10**
>
> **Owner**: financial-cfo-analyst | **Confidence**: medium
> **Falsifying obs**: NPV scenario base < 0 con WACC 12% → re-design business model o no-Go 6A.

#### 🎯 PF-09 — Documento di Studio integrato (3 volumi)

> **Specific**: consegnare lo Studio di Fattibilità completo (3 volumi: Studio + Allegati + Riferimenti) in formato docx/pdf, conformità art. 41 D.Lgs. 36/2023 + Allegato I.7
> **Measurable**: 1 dossier completo M+11; ≥ 12 capitoli Volume 1; ≥ 8 allegati tecnici Volume 2
> **Achievable**: skill `feasibility-study-framework` + lavoro coordinato dei vari agenti
> **Relevant**: prodotto finale per gate M+10/M+11 decisione finanziatori
> **Time-bound**: **M+11**
>
> **Owner**: aerospace-SE (coord) + tutti gli agenti | **Confidence**: medium-high
> **Falsifying obs**: gate intermedio M+9 con coverage RTM <80% → estensione termine M+13.

#### 🎯 PF-10 — Verdetto Go/Hold/No-Go formalizzato

> **Specific**: produrre raccomandazione di gate formale per Percorso 6A e Percorso 6B; documentare razionale + criteri valutati + dissensi (se presenti)
> **Measurable**: Cap. 10 redatto con verdetto chiaro; ≥ 1 review board interno (Firmamento + Fabrica + Coopfond invitato)
> **Achievable**: prerequisito gli output PF-01 → PF-09
> **Relevant**: prodotto finale dello Studio
> **Time-bound**: **M+11**
>
> **Owner**: sovereign-strategist + aerospace-SE + financial-cfo-analyst | **Confidence**: medium
> **Falsifying obs**: se uno o più dei 10 obiettivi sopra non sono raggiunti, verdetto sarà HOLD anziché GO.

### 2.4.3 Obiettivi SMART del Percorso 6A (M+0 → M+24)

Obiettivi del Percorso 6A operativo (pilota Pentema + scale-up regionale Y2):

#### 🎯 6A-01 — SORA autorizzazione operativa Pentema

> **Specific**: ottenere autorizzazione operativa ENAC per BVLOS a Pentema (SAIL ≤ III), conforme Reg. UE 2019/947 + AMC/GM Amendment 3
> **Measurable**: 1 autorizzazione ENAC; volo BVLOS Pentema autorizzato; Operations Manual approvato
> **Achievable**: PF-02 + 4-6 mesi processo SORA application
> **Relevant**: SyR-F-002 + funzione operativa
> **Time-bound**: **M+15** (post Studio di Fattibilità M+11)
>
> **Owner**: aviation-regulatory-counsel | **Confidence**: medium
> **Falsifying obs**: ENAC nega definitivamente SAIL III → ConOps re-design o sito alternativo.

#### 🎯 6A-02 — Piattaforma VTOL acquisita e integrata

> **Specific**: acquisire 1 piattaforma VTOL ibrida commerciale (JOUAV CW-30E o equivalente EU) con payload modulare EO RGB + IR + telecom
> **Measurable**: 1 piattaforma + 2 payload set + 1 GS fissa + 1 GS mobile operativi
> **Achievable**: vendor EU disponibili; budget CapEx ≤ €1.2M (SyR-Cost-001)
> **Relevant**: piattaforma operativa per use case UC-001/002/003/004
> **Time-bound**: **M+15**
>
> **Owner**: vtol-uas-specialist + procurement-officer | **Confidence**: medium-high
> **Falsifying obs**: vendor scelto non commercializzato in EU → re-source con +20-30% costo (cf. AS-008 Cap. 3.9.1).

#### 🎯 6A-03 — Primo volo operativo Pentema

> **Specific**: condurre primo volo BVLOS operativo a Pentema con piattaforma 6A + payload completo + missione UC-001 (mappatura test versanti)
> **Measurable**: 1 volo eseguito con successo; dati EO consegnati a Regione Liguria entro 48h
> **Achievable**: 6A-01 + 6A-02 prerequisiti
> **Relevant**: dimostrazione end-to-end del modello operativo
> **Time-bound**: **M+16**
>
> **Owner**: vtol-uas-specialist + aerospace-SE | **Confidence**: medium
> **Falsifying obs**: primo volo fallisce o incidente → root cause analysis + ripianificazione M+18.

#### 🎯 6A-04 — ≥ 50 missioni operative completate Y1

> **Specific**: completare almeno 50 missioni operative (mix di UC-001/002/003/004) entro Y1 dal primo volo
> **Measurable**: 50 missioni log-tracciate; KPI uptime ≥ 80%; ≥ 0 incidenti major
> **Achievable**: con SyR-O-001 (disponibilità ≥80% giorni/anno) + 1 piattaforma
> **Relevant**: prova di sostenibilità operativa + KPI visione 10 anni Fase 1
> **Time-bound**: **M+24**
>
> **Owner**: aerospace-SE + ops manager | **Confidence**: medium
> **Falsifying obs**: < 30 missioni Y1 → revisione SLA con clienti, prolungamento timeline.

#### 🎯 6A-05 — ≥ 3 contratti pluriennali firmati con PA + cooperative

> **Specific**: firmare ≥ 3 contratti pluriennali (≥ 2 anni) con: 1 Regione (Liguria), 1 cooperativa, 1 PA locale (PC o Comune)
> **Measurable**: 3 contratti firmati; durata media ≥ 2 anni
> **Achievable**: con LoI Regione + workshop cooperative + protocollo PC
> **Relevant**: dimostra modello service-only + revenue ricorrente (B1)
> **Time-bound**: **M+18** (1° contratto); **M+24** (3 contratti totali)
>
> **Owner**: business-model-strategist | **Confidence**: medium
> **Falsifying obs**: nessun contratto firmato M+18 → revisione pricing + scope.

#### 🎯 6A-06 — Revenue ricorrente Y1 ≥ €200k

> **Specific**: generare revenue ricorrente da contratti firmati ≥ €200k entro fine Y1 operativo
> **Measurable**: ARR ≥ €200k (cumulato Y1 + run-rate Y2 ≥ €350k)
> **Achievable**: SyR-Cost-003 (cf. Cap. 7.9.2 scenario base)
> **Relevant**: sostenibilità modello service-only + StNeed-016
> **Time-bound**: **M+24**
>
> **Owner**: business-model-strategist + CFO | **Confidence**: medium
> **Falsifying obs**: revenue Y1 < €100k → revisione drastica MVP scope (SyR-Cost-003 falsifying obs).

#### 🎯 6A-07 — Zero incidenti FATAL o major

> **Specific**: mantenere safety record con 0 incidenti FATAL o major (categoria Reg. UE 996/2010) durante operazioni Y1
> **Measurable**: 0 FATAL + 0 major; incidenti minor ≤ 2 (con report ENAC standard)
> **Achievable**: SyR-S-001/002/003 + SORA mitigation
> **Relevant**: prerequisito scale-up + licenza sociale + B1 cooperativa
> **Time-bound**: **M+24** (continuativo)
>
> **Owner**: safety-officer + ops manager | **Confidence**: high (con SyR-S applicati)
> **Falsifying obs**: 1 incidente FATAL → sospensione automatica + investigation + Go/No-Go review.

#### 🎯 6A-08 — NPS stakeholder ≥ 40

> **Specific**: misurare Net Promoter Score tra stakeholder pilota (PC, ARPA, cooperative, Comune); target NPS ≥ 40 al M+24
> **Measurable**: 1 indagine NPS Y1; ≥ 15 risposte da almeno 5 categorie stakeholder
> **Achievable**: benchmark NPS aerospace service ~30-50; target 40 conservativo
> **Relevant**: prerequisito scale-up SNAI Italia Y2
> **Time-bound**: **M+22** (indagine); **M+24** (report)
>
> **Owner**: business-model-strategist + customer-success | **Confidence**: medium
> **Falsifying obs**: NPS < 20 → re-design servizio + customer success program.

### 2.4.4 Obiettivi SMART del Percorso 6B (M+0 → M+48, R&D)

Il Percorso 6B è in **HOLD / Go Condizionato Estremo** al M+11. Gli obiettivi SMART sotto sono **preparatori R&D**, non commitment a manufacturing né operations:

#### 🎯 6B-01 — Engagement EASA HAPS framework

> **Specific**: aprire dialogo con EASA su Special Condition framework per HAPS civili; partecipare a NPA / RMT pubblici
> **Measurable**: ≥ 1 incontro tecnico EASA documentato; ≥ 1 contributo formale a NPA/RMT
> **Achievable**: EASA RMT.0731 NPA HAPS in roadmap 2024-2026
> **Relevant**: SyR-F-005 + criterio gate M+24 6B
> **Time-bound**: **M+24**
>
> **Owner**: aviation-regulatory-counsel + sovereign-strategist | **Confidence**: medium
> **Falsifying obs**: EASA non apre framework HAPS entro M+36 → 6B rinviato post-2030 (cf. AS-005 Cap. 3.9.1).

#### 🎯 6B-02 — Energy balance simulazione completa worst-case

> **Specific**: completare simulazione energy balance HALE solar + battery worst-case (solstizio inverno 21/12 a 44°N) con tech 2026
> **Measurable**: simulazione documentata; verdetto margin ≥ 30% (Go) o < 30% (seasonal fallback)
> **Achievable**: skill aerospace + propulsion engineer + dati panel/batterie 2026
> **Relevant**: SyR-P-006 (showstopper RSK-TEC-001)
> **Time-bound**: **M+10**
>
> **Owner**: propulsion-energy-engineer | **Confidence**: medium-low
> **Falsifying obs**: margin worst-case < 0% → seasonal-only fallback obbligatorio (cf. Critica 3 Red Team Cap. 3.11).

#### 🎯 6B-03 — Partnership R&D consortium

> **Specific**: formalizzare partnership R&D con almeno 2 di: CIRA, POLITO DIMEAS, Politecnico Milano, INTA, ONERA
> **Measurable**: ≥ 2 MoU R&D firmati; piano di lavoro Phase B condiviso
> **Achievable**: contatti informali con CIRA + POLITO esistenti (vedi `visione-10-anni.md` Fase 3)
> **Relevant**: SyR-F-005 + base scientifica necessaria
> **Time-bound**: **M+24** (MoU); **M+36** (work plan)
>
> **Owner**: aerospace-SE + sovereign-strategist | **Confidence**: medium
> **Falsifying obs**: nessun MoU R&D M+24 → 6B re-design verso solo-Firmamento (alto rischio).

#### 🎯 6B-04 — Mappa funding R&D HALE

> **Specific**: mappare ≥ 5 fonti di funding R&D HALE (PNRR Aerospazio, Horizon Europe, EDF, IPCEI, FESR + privati) con scadenze + criteri ammissibilità
> **Measurable**: mappa documentata Vol. 2 Allegato funding; ≥ 1 candidatura ammessa entro M+24
> **Achievable**: skill financial-cfo-analyst + monitoraggio attivo bandi
> **Relevant**: prerequisito CapEx Phase B ≥ €5.5M
> **Time-bound**: **M+18** (mappa); **M+24** (1° candidatura ammessa)
>
> **Owner**: financial-cfo-analyst + snai-funding-expert | **Confidence**: medium
> **Falsifying obs**: nessuna candidatura ammessa M+30 → Phase B differita o cancellata.

#### 🎯 6B-05 — Subscale flight test design

> **Specific**: definire progetto di subscale flight test (model 1:3 o 1:5 di HALE concept), inclusivo di obiettivi V&V + budget + sito (GATB Grottaglie target)
> **Measurable**: 1 documento di progetto subscale; 1 budget stimato; 1 schedule M+24-36
> **Achievable**: precondizione 6B-02 (energy balance positivo) + 6B-04 (funding)
> **Relevant**: TRL HALE 4 → 5 in roadmap (cf. visione-10-anni Fase 2)
> **Time-bound**: **M+30** (design); **M+42** (primo volo subscale)
>
> **Owner**: aerospace-SE + aero-structures + GATB | **Confidence**: low
> **Falsifying obs**: nessun funding per subscale entro M+30 → 6B in stand-by indefinito.

### 2.4.5 Obiettivi SMART della visione 10 anni (Y1 → Y10, sintetici)

Gli obiettivi 10 anni sono **direzionali** (boundary condition B2), non commitment esecutivo dello Studio. Sintetici per coerenza:

#### 🎯 V10-01 — Fase 1 Pentema validata e replicata

> **Specific**: completare Fase 1 (pilota Pentema) entro Y1, validata + replicabile in altre Aree Interne italiane
> **Measurable**: ≥ 3 contratti firmati Y1; ≥ 50 missioni; ≥ €200k revenue cumulato; 0 FATAL (= 6A-04/05/06/07 aggregati)
> **Time-bound**: **Y1** (M+24)
> **Confidence**: medium

#### 🎯 V10-02 — Scale-up Italia SNAI Y2-Y3

> **Specific**: estendere operazioni a 3+ regioni SNAI italiane (Piemonte, Marche, Calabria + altre); ARR ≥ €2-5M Y3
> **Measurable**: ≥ 10 contratti istituzionali attivi; flotta 3-8 piattaforme VTOL/MALE
> **Time-bound**: **Y3** (M+36)
> **Confidence**: low-medium (dipendente da Fase 1 + capital raise Series A)

#### 🎯 V10-03 — HALE prototipo Y4-Y6

> **Specific**: dimostrare HALE solare prototipo full-scale in volo > 7 giorni continuativi a 20 km di quota
> **Measurable**: 1 HALE > 7 gg volo persistent; TRL HALE = 7
> **Time-bound**: **Y6** (M+72)
> **Confidence**: low (vedi capital intensity caveat `visione-10-anni.md` §4)

#### 🎯 V10-04 — Costellazione italiana iniziale Y6-Y8

> **Specific**: 3-10 HAPS solari italiani operativi in cluster, perennial demonstration ≥ 30 gg per piattaforma
> **Measurable**: ≥ 3 HAPS operativi; ARR ≥ €30-80M; riconoscimento EU Sovereign Stratosphere ecosystem
> **Time-bound**: **Y8** (M+96)
> **Confidence**: low

#### 🎯 V10-05 — Consorzio EU Sovereign Stratosphere Y8-Y10

> **Specific**: posizionamento come **principal Italian node** in consorzio EU stratospheric layer
> **Measurable**: 10-30 HAPS EU operativi (mix IT+FR+DE+ES); programma EU equivalente IRIS² su HAPS attivo
> **Time-bound**: **Y10** (M+120)
> **Confidence**: low (vedi `visione-10-anni.md` §4-5 + RESERVED-rischi-geopolitici)

> **Falsifying observation aggregata visione 10 anni**: se entro Y4-Y5 non esiste programma EU specifico per HAPS sovereign con budget multi-miliardario, la Fase 5 (consorzio EU) è strutturalmente non finanziabile e va ridimensionata a "scala italiana standalone". Vedi `riferimenti/visione-10-anni.md` §4 per analisi completa capital intensity.

---

## 2.5 Vincoli e assunzioni iniziali

### 2.5.1 Vincoli regolatori (cf. Cap. 5)

Riassunti dal Cap. 5 (`cap-05-quadro-normativo.md`):
- **Percorso 6A**: SAIL ≤ III obbligatorio per fattibilità operativa Pentema (Reg. UE 2019/947 + AMC/GM Amendment 3 + ENAC APR Ed.3+Emend.1).
- **Percorso 6B**: categoria Certified richiesta — Type Certification con Special Condition negoziata caso per caso (no framework HAPS civile dedicato).
- **Spettro radio**: AGCOM licensing per LTE tattico 6A; ITU WRC-27 dialogo per banda HAPS 6B.
- **GDPR + NIS2**: DPIA pubblica + cybersecurity by design.
- **AS/EN 9100 + ISO 9001**: certificazione di gestione qualità + processi aerospaziali (target M+24).

### 2.5.2 Vincoli finanziari

Dalla strategia duale (CLAUDE.md) e dai SyR Cost (Cap. 3.5.7):
- **Percorso 6A**: CapEx Y1 **€700-1200k** baseline ingegneristico (vedi Cap. 8 §8.3.1 per Quadro Economico completo con IVA + contingency: €975k-€1.96M, scenario base €1.4M); OpEx run-rate Y2 **€260-480k/anno** (Cap. 8 §8.5.1).
- **Percorso 6B (R&D Phase B)**: investimento **€5,5-13,5M** (preparatorio R&D, non manufacturing); funding plan multi-source obbligatorio (PNRR + Horizon + EDF + equity).
- **Studio di Fattibilità (presente)**: budget bando Coopfond **€80-150k** (M+0 → M+11), eseguito in conformità Cooding Prototypes.
- **Capital intensity totale visione 10 anni**: €500M-€2B (small fleet) → €10-30B (EU sovereign scale); vedi `visione-10-anni.md` §4.

### 2.5.3 Vincoli temporali

Calendario dei gate decisionali (cf. Cap. 9 + skill `gate-review-checklist`):

| Gate | Mese | Obiettivo verdetto | Verdetto target |
|---|---|---|---|
| **M+3** | maggio 2026 | Baseline RTM + Stakeholder Map | Continue (informale) |
| **M+6** | agosto 2026 | RTM v0.6 + LoI Regione + Pre-app ENAC + Workshop cooperative | Continue (formale) |
| **M+10** | dicembre 2026 | Trade Studies + Risk Register + Quadro Economico | **Go Cond. 6A** / Hold 6B |
| **M+11** | gennaio 2027 | Studio Fattibilità completo + Verdetto formale | **GO / HOLD / NO-GO** |
| **M+12** | febbraio 2027 | Avvio Percorso 6A operativo / Cooding Invest candidatura | Continue (operativo) |
| **M+24** | febbraio 2028 | Pilota Y1 conclusivo + KPI ≥ target → scale-up Y2 | Go / Hold / Pivot |
| **M+36** | febbraio 2029 | Scale-up regionale + decisione Phase B HALE | Go / Hold |
| **M+48** | febbraio 2030 | Phase B HALE prototipo subscale | Continue / Hold |

### 2.5.4 Vincoli territoriali (Pentema + Aree Interne Liguria)

**Pentema (Torriglia, GE)** — frazione di **14 abitanti ISTAT** (7 M + 7 F, 11 famiglie, 100 edifici di cui 97 utilizzati, distanza 3.27 km dal capoluogo Torriglia) a 1100-1300 m s.l.m. nell'area SNAI Antola-Tigullio (2014-2020 + 2021-2027). Caratteristiche operative:

| Caratteristica | Valore | Implicazione |
|---|---|---|
| **Altitudine sito** | 1100-1300 m s.l.m. | Densità aria ridotta → ricalcolo curve prestazionali |
| **Orografia** | Valli incassate, crinali, dislivelli >500 m in 2 km | Shadow zones radio C2 → SATCOM L-band richiesto |
| **Meteo invernale** | Neve persistente Dic-Mar, T fino a -10°C | Limiti operativi VTOL standard; finestre stagionali |
| **Meteo estivo** | Termiche pomeridiane, raffiche montane fino 17 m/s | Vincoli wind margin operativi |
| **Connettività esistente** | Mobile 4G/5G discontinua; banda fissa via radio link | Necessità GS robusto + backup SATCOM |
| **Accessibilità terrestre** | Strada secondaria SP, 30 min da Torriglia, 1.5h da GE | Logistica trasporto piattaforma vincolata |
| **Comunità** | **14 residenti ISTAT** (7M + 7F), 11 famiglie, 100 edifici; cooperativa di comunità attiva | Accettabilità sociale favorita ma da curare per visibilità mediatica |
| **Spazio aereo** | Class G fino a 1500m AGL; class E sopra | Operazioni VLL ≤500 ft AGL semplificate da SORA 2.5 EU |

### 2.5.5 Assunzioni baseline (richiamo Cap. 3.9.1)

In coerenza con Cap. 3.9.1 (10 assunzioni baseline AS-001 → AS-010), le assunzioni più impattanti per il Cap. 2 sono:

| ID | Assunzione | Impatto se invalidata |
|---|---|---|
| **AS-001** | Regione Liguria mantiene impegno per pilota Pentema almeno fino M+24 | Pivot anchor customer (V10-01, 6A-05 a rischio) |
| **AS-002** | Coopfond rinnova bando Cooding nel 2026 con condizioni analoghe a 2025 | Funding gap M+12-24, candidatura alternative |
| **AS-003** | Almeno 8 cooperative su 10 mantengono adesione al gruppo pilota | Re-design rete cooperativa (§2.3.3 + PF-03) |
| **AS-004** | ENAC riconosce Pentema come SAIL II-III BVLOS feasible | ConOps re-design o cambio sito (6A-01 a rischio) |
| **AS-009** | Comunità Pentema accetta sperimentazione con DPIA pubblica | Workshop pubblico + relocate pilota (Top-5 falsifying obs) |

---

## 2.6 Red Team Check — Critical Review

L'agente `red-team-skeptic` ha condotto attacco strutturato al presente capitolo. Sintesi delle critiche e risposte:

### Critica 1 — "La stakeholder map è incompleta: mancano i potenziali competitor e i nemici del progetto"

**Razionale critica**: la mappa identifica 30 stakeholder ma nessuno classificato come "ostile" o "competitor diretto". I rischi geopolitici (vedi `RESERVED-rischi-geopolitici.md`) suggeriscono che Leonardo/TAS possano essere ambivalenti (S-23 doppia categoria) o Acquirer ostile. Inoltre Aalto HAPS (Airbus) o Skydweller potrebbero attivare difese commerciali se Firmamento cresce.

**Risposta**: corretto, parzialmente. S-23 (Leonardo/TAS) è già classificato come **PARTNER + COMPETITOR** con "Manage Closely" e nota "no naive disclosure". I competitor globali (Aalto, SoftBank, Skydweller) sono tracciati in Cap. 7.5 ma non in questo capitolo (scope: stakeholder con interesse diretto sul progetto IT/EU). I dossier riservati restano in `RESERVED-rischi-geopolitici.md`.

**Action item**: aggiungere a Cap. 2.2.1 (riedizione M+6) una sezione **"Competitor monitoring"** con mappatura sintetica di 5-7 player globali HAPS/UAV service operator + Early Warning Indicators.

### Critica 2 — "Gli obiettivi SMART '10 anni' sono di fatto non-falsificabili nel time horizon dello Studio"

**Razionale critica**: V10-03 (HALE prototipo Y6), V10-04 (costellazione Y8), V10-05 (consorzio EU Y10) sono troppo lontani per essere verificabili nello Studio di Fattibilità (chiude M+11). Sono **vision statement** travestiti da obiettivi.

**Risposta**: corretto. La sezione §2.4.5 è dichiarata esplicitamente "direzionale, non commitment esecutivo". I 5 V10-* sono il **vettore strategico** che giustifica la coerenza Percorso 6A + 6B; il rigore epistemico SMART è applicato pienamente a PF-* (M+11) e 6A-* (M+24), parzialmente a 6B-* (M+48), e in modo "boundary B2" a V10-*. Vedi `visione-10-anni.md` §4 (caveat capital intensity).

**Action item**: distinguere chiaramente in Cap. 11 (Roadmap post-fattibilità) tra "objectives" (Y1-Y3) e "vision pillars" (Y4-Y10) — il rigore SMART si applica solo ai primi.

### Critica 3 — "Il KPI Revenue Y1 ≥ €200k (6A-06) è ancora un numero buttato"

**Razionale critica**: nessuna validazione esterna di willingness-to-pay PA italiana per servizi EO/NTN da operatore privato. Cap. 7.13 critica 6 (pricing €150k/anno Regione "inventato") solleva lo stesso problema.

**Risposta**: corretto. SyR-Cost-003 falsifying obs già dichiara "revenue Y1 < €100k → revisione drastica MVP scope". L'obiettivo PF-08 (Quadro Economico) prevede scenari worst/base/best — il revenue Y1 dello scenario worst è ~€80-120k, accettato come ipotesi-limite.

**Action item**: benchmark contrattualistico con e-GEOS, Planetek, NHazca (operatori EO che lavorano con Regioni IT) — completato entro M+6 (cf. Cap. 7.13).

### Critica 4 — "L'assunzione AS-001 (Regione Liguria fino M+24) è 'wishful thinking'"

**Razionale critica**: la storia delle PMI italiane che si appoggiano su una Regione come anchor è piena di casi di switch politico / cambio assessore / re-priorizzazione di bilancio che hanno azzerato investimenti pluriennali. Esempi: progetti SNAI 14-20 cancellati al cambio giunta in 3 regioni (verificare).

**Risposta**: pertinente. Mitigazioni: (i) **plan B Top-1** (pivot Piemonte/Marche/Calabria); (ii) LoI Regione con scope minimo già **technicamente realizzabile** indipendentemente da scelte politiche (use case PC sono "neutrali"); (iii) tracciamento elezioni regionali Liguria 2025-2030 (ipotetiche tornate elettorali).

**Action item**: in Cap. 9 (Cronoprogramma) aggiungere check politico-istituzionale di Regione Liguria — verifica elezioni 2025 effettive + composizione attuale giunta entro M+3.

### Critica 5 — "Il Top-5 stakeholder dimentica gli investitori di Phase B (CDP, EIB)"

**Razionale critica**: il Top-5 (Regione, ENAC, Coopfond, Cooperative, Comunità) è corretto per Percorso 6A (Y1-Y2) ma per Percorso 6B (Y3-Y5) gli investitori istituzionali (CDP, EIB, fondi sovrani) diventano critici. La mappa attuale li ha come S-29 "monitor".

**Risposta**: corretto per Y3+. La power/interest grid §2.2.2 nota già che S-29 passa da "Monitor (oggi)" a "Manage Closely (Y3+)". Per Y1-Y2 i finanziatori sono Coopfond + Cooding Invest + small grants; per Y3+ il vector cambia.

**Action item**: in Cap. 8 (Economico-finanziario) sezione dedicata "Investor relations roadmap Y3-Y10" con engagement schedule CDP, EIB, fondi sovrani (RILEGGI con sovereign-strategist).

### Critica 6 — "Le falsifying observation sono dichiarate ma non c'è un trigger automatico per agire"

**Razionale critica**: l'obiettivo 6A-06 dice "revenue Y1 < €100k → revisione drastica MVP scope", ma chi controlla? Quando? Con quale gate? Le falsifying obs sono potenti solo se attivano un processo decisionale, non solo dichiarate.

**Risposta**: corretto, gap di processo. Le falsifying obs vanno legate ai **gate decisionali** (M+10, M+12, M+24) con review board che esamina lo stato di tutte le falsifying obs e decide se attivare contingency plan.

**Action item**: in Cap. 9 (Cronoprogramma) + Cap. 10 (Raccomandazione) formalizzare un **Falsifying Observations Tracker** che a ogni gate verifica lo stato di tutte le obs dichiarate; trigger automatico HOLD se ≥ 2 obs critiche risultano "fired".

### Critica 7 — "La governance Firmamento + Fabrica via 'contratto di rete' è troppo soft per un progetto da €5-10M complessivi"

**Razionale critica**: il contratto di rete è strumento agile ma con vincoli giuridici deboli; in caso di scale-up Y2-Y3 con flotta 3-8 piattaforme e ARR €2-5M, la governance leggera può esplodere (conflitti su IP, dati, revenue sharing).

**Risposta**: pertinente. Il contratto di rete è scelto per **Y1 (pilota)** dove la priorità è agilità e bassa overhead. Per Y2+ § 2.3.3 nota già che JV o consorzio cooperativo sono "considerati per Y2-Y3 / Y3+". 

**Action item**: in Cap. 11 (Roadmap post-fattibilità) trade study esplicito **TS-GOVERNANCE** per scegliere tra contratto di rete, JV, consorzio cooperativo, holding cooperativa — output target M+18.

### Verdetto Red Team

Il capitolo è **strutturalmente solido** ma con **azioni richieste prima del gate M+10**:

- ☐ Sezione "Competitor monitoring" aggiunta a §2.2 (versione M+6)
- ☐ Distinguere chiaramente in Cap. 11 "objectives" vs "vision pillars"
- ☐ Benchmark pricing PA italiana completato (cross-Cap. 7.13)
- ☐ Check politico-istituzionale Regione Liguria entro M+3
- ☐ Sezione "Investor relations Y3-Y10" in Cap. 8
- ☐ "Falsifying Observations Tracker" formalizzato in Cap. 9 + 10
- ☐ Trade Study "TS-GOVERNANCE" pianificato M+18

---

## 2.7 Open Questions (OQ-Cap2)

Le **Open Questions** specifiche del Cap. 2 (oltre alle OQ-010, OQ-011, OQ-016 già ereditate da Cap. 3.10):

| OQ-ID | Domanda | Trigger per chiusura | Owner agent | Deadline |
|---|---|---|---|---|
| **OQ-2.01** | Composizione attuale Giunta Regione Liguria + tempistica prossime elezioni regionali | Verifica DGR + sito Regione | snai-funding-expert | **M+3** |
| **OQ-2.02** | Posizione UNCEM Liguria su sperimentazioni aerospaziali in Aree Interne | Workshop UNCEM | snai-funding-expert | **M+6** |
| **OQ-2.03** | Disponibilità Comune di Torriglia a delibera di sostegno pilota Pentema | Riunione Consiglio Comunale | snai-funding-expert + business-model-strategist | **M+6** |
| **OQ-2.04** | Quale modello di property of data nei contratti con cooperative? | Discussione legal + Fabrica | data-privacy-counsel + business-model-strategist | **M+9** |
| **OQ-2.05** | Quale meccanismo di feedback continuo dalla comunità Pentema? | Workshop pubblico + sportello | data-privacy-counsel | **M+6** |
| **OQ-2.06** | Quali NPS strumenti / metodi per misurare soddisfazione stakeholder eterogenei? | Decisione metodologica | business-model-strategist | **M+12** |
| **OQ-2.07** | Quale strategia di comunicazione pubblica per il progetto (press, social, web)? | Plan comunicazione + budget | communications-lead | **M+9** |
| **OQ-2.08** | Quale frequenza e modalità di gate review dopo M+11 (operative pilot)? | Decisione governance | aerospace-SE + sovereign-strategist | **M+9** |

---

## 2.8 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §4.1.1.2.1 Stakeholder Identification, §6.8 Decision Analysis, NPR 7120.5 Project Management Requirements. Confidence: **high** (norma metodologica internazionale).

[^2]: Piano Strategico Nazionale delle Aree Interne (PSNAI), Ministro per gli Affari europei, il Sud, le politiche di coesione e per il PNRR, luglio 2025. Source: `Aree interne/psnai_finale_30072025_clean_ministro.md` (= `fonti/psnai_finale_30072025_clean_ministro.md`). Specifico: §1.4-1.5 Mappatura AI 2020, §3 Risorse 2021-2027, §5.4 Governance, §6 Visione strategica, Allegato 5 Mobilità, Allegato 7 Salute. **Confidence: high** (fonte istituzionale ufficiale italiana, 2025).

[^3]: Briefing "Progetto Piattaforma Aerea per le Aree Interne", Firmamento Technologies, M-3. Source: `da revisionare/Briefing_ Progetto Piattaforma Aerea per le Aree Interne.md`. **Confidence: high** (documento progetto, M-3 = aprile-dicembre 2025 attività).

[^4]: Programma Regionale FESR Liguria 2021-2027 (riferimento generale; documento ufficiale Regione Liguria). **Confidence: medium** (citazione generale, validazione specifica richiesta su importi e priorità per progetto).

[^5]: Rapporto di Istruttoria per la Selezione delle Aree Interne 2021-2027 — Regione Liguria, Comitato Nazionale Aree Interne (DPCoe), ottobre 2022. Source: `Aree interne/rapporto-istruttoria_regione-liguria.md`. Specifico: 4 aree confermate 14-20 (Antola-Tigullio, Beigua-Sol, Val di Vara, Valle Arroscia) + 4 nuove 21-27 (Imperiese, Fontanabuona, Bormida, Valle Scrivia). **Confidence: high** (fonte istituzionale, DPCoe).

[^6]: ENAC, Piano Strategico Nazionale Advanced Air Mobility (AAM) 2021-2030 + Allegato 1 Roadmap + Allegato 2 Business Plan. Sources: `fonti/01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.md`, `fonti/02_AAM-Italian-Ecosystem-Roadmap_web-1.md`, `fonti/03_AAM-Business-Plan_web-1.md`. **Confidence: high** (ENAC, fonte istituzionale italiana).

[^7]: EASA ED Decision 2025/018/R del 15 settembre 2025, Amendment 3 to Issue 1 of AMC/GM to Reg. UE 2019/947 — versione europea SORA 2.5. Source: `fonti/ed_decision_2025-018-r.md` + annex + explanatory note + corrigendum. **Confidence: high**.

[^8]: Lettera di formalizzazione Coopfond per il progetto HALE (24 ottobre 2025). Source: `bando/[Reg.Uff.CoopFond 2025U0001593-24-10-2025] - ProgettoHALE_CoodingII_LetetraPOstCDA-signed.md`. **Confidence: high** (lettera ufficiale).

[^9]: Elenco Cooperative supportanti il progetto HALE (Cooding Prototypes). Source: `bando/Elenco Cooperative.md`. **Confidence: high** (documento bando ufficiale).

[^10]: Doran, G. T. (1981). "There's a S.M.A.R.T. way to write management's goals and objectives". Management Review, 70(11), 35-36. Riferimento metodologico esterno. Adattato dalla NASA Project Management e da NPR 7120.5. **Confidence: high** (standard di management).

[^11]: Coopfond, Bando Cooding Prototypes 2025. Source: `bando/progetto prototype cooding.md`, `bando/Sintesi prototype cooding.md`, `bando/piano economico prototype cooding.md`, `bando/Business Plan.docx (1).md`. **Confidence: high** (documenti bando ufficiali).

[^12]: Codice del Terzo Settore (D.Lgs. 117/2017) art. 55 — co-programmazione e co-progettazione PA + Terzo Settore. Riferimento normativo per partnership Firmamento-Regione Liguria-cooperative.

[^13]: Skill `feasibility-study-framework` (`/.claude/skills/feasibility-study-framework/SKILL.md`); skill `epistemic-rigor` (`/.claude/skills/epistemic-rigor/SKILL.md`); skill `gate-review-checklist` (`/.claude/skills/gate-review-checklist/SKILL.md`); skill `risk-register-builder` (`/.claude/skills/risk-register-builder/SKILL.md`); skill `requirements-traceability-matrix` (`/.claude/skills/requirements-traceability-matrix/SKILL.md`); skill `trade-study-analysis` (`/.claude/skills/trade-study-analysis/SKILL.md`).

[^14]: Documento di visione 10 anni Firmamento Technologies. Source: `riferimenti/visione-10-anni.md`. Specifico: §1 obiettivo finale, §2 le 5 fasi, §3 vettore strategico, §4 capital intensity, §8 boundary conditions B1+B2. **Confidence: high** (documento interno progetto, baseline strategica).

---

## 2.9 Note di chiusura del capitolo

Il presente Cap. 2 costituisce il **ponte logico** tra il Quadro Esigenziale del Cap. 1 (art. 41 D.Lgs. 36/2023) e l'apparato dei requisiti tracciabili del Cap. 3 (NASA SE / RTM). Tre prodotti chiave consegnati:

1. **Inquadramento del contesto strategico** robusto su 5 cornici di policy (SNAI/PSNAI 2025, PNRR, FESR Liguria, ENAC AAM, framework normativo UE) con citazioni autoritative.
2. **Mappa stakeholder consolidata** con 30 entità classificate su 5 categorie + power/interest grid + top-5 stakeholder critici con strategia di engagement dettagliata e KPI binari.
3. **30 obiettivi SMART** distribuiti su 4 orizzonti (Piano di Fattibilità M+11, Percorso 6A M+24, Percorso 6B M+48, visione 10 anni Y10), ciascuno con owner, confidence, falsifying observation.

**Debolezze dichiarate onestamente** (cf. §2.6 Red Team):

1. **Stakeholder map** completa ma manca **competitor monitoring** esplicito → action M+6
2. **Obiettivi V10-** sono **vision pillars** (boundary B2), non veri SMART → da chiarire in Cap. 11
3. **Revenue Y1 ≥ €200k** ancora confidence medium → benchmark M+6 + LoI Regione M+6
4. **AS-001 Regione Liguria** assunzione critica → plan B mappato + check politico M+3
5. **Falsifying observations** dichiarate ma trigger di processo da formalizzare → Cap. 9 + 10
6. **Governance Firmamento-Fabrica** scelta baseline contratto di rete → TS-GOVERNANCE M+18

**Prossimi step richiesti** (in ordine di criticità per i gate M+6 e M+10):

1. **Check politico-istituzionale Regione Liguria** entro M+3 (OQ-2.01)
2. **Workshop strutturati con 10 cooperative** entro M+6 (PF-03, OQ-011)
3. **Pre-application meeting ENAC** entro M+6 (PF-02, OQ-002)
4. **LoI Regione Liguria** firmata entro M+6 (PF-04, OQ-010)
5. **DPIA pubblica preliminare** entro M+6 (PF-05, OQ-017)
6. **Workshop pubblico Pentema + delibera Comune Torriglia** entro M+6 (Top-5 plan, OQ-2.03)
7. **Benchmark pricing PA italiana** entro M+6 (cross-Cap. 7.13)
8. **Update Cap. 2** post-validazione esterna → versione M+9 per gate M+10

**Versionamento Cap. 2**:
- **v0.5 (M+3, presente)**: baseline post-Allineamento Strategico Maggio 2026 (30 stakeholder + 30 obiettivi SMART)
- v0.6 (M+6): post-workshop cooperative + LoI Regione + pre-app ENAC; stakeholder map espansa con competitor monitoring
- v0.8 (M+10): post-trade study + falsifying observations tracker formalizzato
- v1.0 (M+11): congelato per gate review

Il capitolo è **chiuso al M+3** con verdetto Red Team **OK con 7 action items** e 8 Open Questions Cap. 2 tracciate per la versione M+6.
