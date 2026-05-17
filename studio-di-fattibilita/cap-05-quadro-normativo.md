# Capitolo 5 — Quadro Normativo e Regolamentare

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 5
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Stato:** capitolo redatto con fonti normative autoritative aggiornate al settembre 2025 (EASA ED Decision 2025/018/R)
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor` (falsifiability, triangulation, source provenance, confidence levels, pre-mortem, steel-manning, base-rate)
> **Red Team review:** verifica condotta dall'agente `regulatory-adversary` — vedi §5.13

---

## 5.0 Sintesi del capitolo

Il quadro normativo del progetto HALE/VTOL si compone di **cinque livelli interconnessi**: (1) regolamentazione UE per UAS — Reg. (UE) 2018/1139, 2019/947, 2019/945 e relativi AMC/GM aggiornati a settembre 2025 con la **versione europea di SORA 2.5**; (2) framework U-Space — Reg. (UE) 2021/664, 665, 666 + ENAC LG-2023/006; (3) recepimento nazionale italiano — ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed. 3 (2019) + Emendamento 1 (2020); (4) regolamentazione spettro radio — ITU Radio Regulations + PNRF (MIMIT) + provvedimenti AGCOM; (5) compliance trasversale — GDPR + NIS2 + standard tecnici aerospaziali (AS/EN 9100, DO-178C, ARP4754A).

I due percorsi del progetto si collocano in **categorie EASA radicalmente diverse**:

| Percorso | Categoria target | Maturità framework | Strategia |
|---|---|---|---|
| **6A — VTOL pilota Pentema** | **Specific** SAIL II-III | Maturo (SORA 2.5 settembre 2025) | SORA application + Operations Manual + Operator Declaration |
| **6B — HALE stratosferico** | **Certified** | **Immaturo** (no framework HAPS civile dedicato) | Type Certification innovativa, **Special Condition negoziata caso per caso** |

Il capitolo identifica formalmente **due showstopper regolatori** per il Percorso 6B (mancanza framework HAPS + tempistiche TC innovativa), e tre **gap operativi** per il Percorso 6A (SORA SAIL Pentema da pre-validare con ENAC, spettro AGCOM da licenziare, conformità Garante Privacy da formalizzare). Tutti sono **gestibili** con engagement deliberato; nessuno è insuperabile nel time horizon di progetto.

**Conformità formale richiesta** per la presentazione a bandi pubblici italiani:
- D.Lgs. 36/2023 art. 41 + Allegato I.7 (PFTE)
- Reg. UE 2019/947 + 2019/945 (UAS)
- AS/EN 9100 + ISO 9001 (sistemi di gestione)
- GDPR + D.Lgs. 196/2003 novellato

---

## 5.0bis Boundary conditions del progetto

Il capitolo presuppone — come **scelte strategiche-politiche** del fondatore, non come ipotesi da validare — due posizioni di progetto:

- **B1**: Firmamento Technologies opera con un **modello cooperativo** in partnership stabile con cooperative Legacoop (rete utenti-pilota, capofila Fabrica). Le considerazioni di governance privacy, conformità tecnica e modello operativo riflettono questa scelta strutturale.
- **B2**: L'obiettivo strategico di lungo termine è **costituire un nodo italiano di una futura infrastruttura sovrana europea HAPS**, complementare a IRIS² (LEO sovrano EU) e Galileo/Copernicus. Il presente Studio di Fattibilità approva i soli step intermedi (Percorso 6A pilota + Percorso 6B preparatorio R&D); l'orizzonte completo è descritto in `riferimenti/visione-10-anni.md`.

L'analisi regolatoria che segue è applicata a *come* sostenere e *come* attuare queste due posizioni, non a *se* siano gli obiettivi giusti.

> **🔬 Falsifying observation aggiuntiva linkata (B2 operazionalizzazione)**: vedi `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md` **FO-ADD-02** (linguaggio pubblico "complementare a IRIS²"). Trigger M+18: roadmap ufficiale IRIS² (DG CNECT) include "stratospheric layer" / "complementary platforms layer". Se NO al M+18, riformulazione posizionamento esterno (riduzione narrativo a "Italian operator of strategic stratospheric services" pur preservando B2 internamente).

---

## 5.1 Quadro Unione Europea — Aviazione Civile e UAS

### 5.1.1 Reg. (UE) 2018/1139 — Basic Aviation Regulation

Il **Regolamento di Base** [^1] disciplina la sicurezza dell'aviazione civile nell'Unione, conferendo all'**EASA** (European Union Aviation Safety Agency) il mandato di emettere norme tecniche delegate e atti di esecuzione su:
- Certificazione di prodotti aeronautici, parti, componenti
- Operazioni aeree e licenze del personale
- Servizi di gestione del traffico aereo (ATM/ANS)
- **Aeromobili senza equipaggio (UAS)** — artt. 55-58 e Allegato IX

Per il progetto HALE/VTOL, il Reg. 2018/1139 è la **fonte di delega primaria** per i regolamenti UAS dettagliati (Reg. 2019/947 e 2019/945) e per le AMC/GM (Acceptable Means of Compliance / Guidance Material) emesse da EASA.

### 5.1.2 Reg. (UE) 2019/947 — Operations UAS

Il **Regolamento Operations** [^2] è la base regolatoria primaria per **tutte le operazioni UAS nello Spazio Aereo UE**, applicabile dal 31 dicembre 2020. Stabilisce tre **categorie operative** in funzione del rischio:

| Categoria | Rischio | Caratterizzazione | Applicabilità a HALE/VTOL Firmamento |
|---|---|---|---|
| **Open** | Basso | UAS ≤ 25 kg MTOM, VLOS, ≤ 120 m AGL, non sopra assembramenti, classi C0-C4 | ❌ Non applicabile (BVLOS richiesto + sopra persone in alcuni scenari) |
| **Specific** | Medio | Operazioni con rischio elevato non Open, autorizzate caso per caso con **SORA** | ✅ **Categoria target Percorso 6A** |
| **Certified** | Alto | UAS sopra MTOM elevate, trasporto persone, sopra città grandi assembramenti, equiparate ad aviazione manned per Type Certificate | ✅ **Categoria target Percorso 6B HALE** (in assenza di alternative per operazioni civili continuative a 20 km) |

**Articolo 11 — Autorizzazione per la Categoria Specific:**

Per condurre un'operazione UAS in categoria Specific, l'operatore deve **prima dell'avvio del volo** ottenere un'autorizzazione operativa dall'autorità competente nazionale (in Italia: **ENAC**) [^2, art. 12.1]. La domanda comprende [^2, art. 11.2]:

> *"a) la descrizione delle caratteristiche dell'operazione UAS;
> b) le misure di mitigazione applicate, comprese le caratteristiche tecniche degli UAS;
> c) le procedure operative;
> d) la conferma dell'esistenza di una copertura assicurativa adeguata;
> e) la dimostrazione di un livello sufficiente di robustezza delle misure di mitigazione del rischio..."*

L'autorizzazione è subordinata alla dimostrazione che il rischio è **proporzionato** rispetto ai mezzi di mitigazione adottati, secondo la metodologia **SORA** (Specific Operations Risk Assessment).

### 5.1.3 Reg. (UE) 2019/945 — Design and Manufacture UAS

Il **Regolamento Design** [^3] disciplina i requisiti di prodotto applicabili agli UAS commercializzati nell'Unione, definendo **sette classi di prodotto** (C0-C6) con MTOM, velocità, livelli di rumorosità, equipaggiamenti minimi (es. trasponder/identificazione a distanza, geofencing) e standard di conformità CE.

Per il Percorso 6A (VTOL ibrido tipo JOUAV CW-30E, ~38 kg MTOM) la categoria di mercato Specific permette di **non vincolarsi alla classificazione C0-C6** (riservata alla categoria Open), purché l'UAS sia conforme ai requisiti EASA stabiliti caso per caso nell'autorizzazione operativa.

Per il Percorso 6B (HALE), la classificazione standard C0-C6 **non si applica**: il velivolo richiede un **Type Certificate** ai sensi del Reg. 2018/1139 art. 11, con applicazione di Certification Specifications custom (es. Special Condition Light UAS o equivalente per HAPS).

> **Falsifying observation** (Regola 1 — epistemic-rigor): se EASA, entro M+24, pubblica una Certification Specification specifica per HAPS che esclude la categoria di massa del nostro concept (es. < 200 kg MTOM), l'architettura di sistema va rivista con riduzione massa. Confidence framework: **medium** (basato su andamento NPA EASA 2024-2025).

### 5.1.4 EASA Acceptable Means of Compliance e Guidance Material — Amendment 3 (settembre 2025)

Il **ED Decision 2025/018/R** del 15 settembre 2025 [^4] è la **fonte autoritativa più aggiornata** sull'applicazione del Reg. 2019/947, ed emette l'**Amendment 3 a Issue 1 dell'AMC/GM**, che recepisce nella sua interezza la **versione europea di SORA 2.5** (sviluppata da JARUS — Joint Authorities for Rulemaking on Unmanned Systems) [^5].

**Cosa cambia con l'Amendment 3** (rilevanza per il progetto HALE):

1. **AMC1 to Article 11 sostituita** con la European version of SORA 2.5
2. **Annessi A, B ed E del JARUS SORA emendati**; introdotti **nuovi Annexi I e F**
3. **Cybersecurity**: i requisiti di dettaglio inclusi in JARUS SORA 2.5 sono stati estratti per essere disciplinati separatamente in Reg. UE su Information Security (art. 4(2) Reg. 2018/1139); per ora restano come **GM** (Guidance Material non vincolante)
4. **Adattamento europeo**: i passi del SORA che JARUS lascia a discrezione nazionale sono stati uniformati a livello EU dall'EASA. Tra le modifiche più significative:
   - Identificazione operazione **VLL** (Very Low Level) ≤ 500 ft AGL → applicabile al Percorso 6A
   - Trasformazione di "guidance" JARUS in "requirements" vincolanti per certi step

**Implicazioni per il Percorso 6A (VTOL Pentema):**
- La **SORA application** va costruita secondo SORA 2.5 europea (non SORA 2.0 generica)
- I 24 **OSO** (Operational Safety Objectives) della SORA 2.0 sono stati riarticolati nella SORA 2.5
- L'operatore deve dimostrare conformità ai **threshold** SAIL applicabili

> **Source provenance** [^4]: `fonti/ed_decision_2025-018-r.md` + `fonti/annex_to_ed_decision_2025-018-r_1.md` (3.3 MB, 196 menzioni SORA) + `fonti/explanatory_note_to_ed_decision_2025-018-r.md`.
> **Confidence: high** (norma in vigore, EASA è fonte primaria).

### 5.1.5 Metodologia SORA (Specific Operations Risk Assessment) 2.5

La metodologia SORA, ora codificata europea dall'Amendment 3 [^4], articola la valutazione del rischio operativo in **10 step**:

| Step | Output | Note |
|---|---|---|
| Step 0 | Pre-application evaluation | Identifica se SORA è il percorso adatto |
| Step 1 | ConOps description | Definizione dell'operazione |
| Step 2 | iGRC (intrinsic Ground Risk Class) | Densità popolazione sotto la rotta |
| Step 3 | Final GRC after mitigations (M1, M2, M3) | Mitigazione del rischio a terra |
| Step 4 | iARC (initial Air Risk Class) | Densità traffico nel volume operativo |
| Step 5 | Final ARC after strategic mitigation | Mitigazione del rischio aereo |
| Step 6 | Determine SAIL (Specific Assurance and Integrity Level) | I-VI in funzione di GRC × ARC |
| Step 7 | Identify applicable OSO | Lista OSO obbligatori per il SAIL |
| Step 8 | Identify Containment requirements | Requisiti di mantenimento operazione nei limiti |
| Step 9 | Operations Manual + Maintenance Manual + Procedures | Documentazione operativa |

**Per Pentema (Percorso 6A) — stima preliminare** (valori da confermare con pre-application meeting ENAC, DR-004 audit-rigore-epistemico.md):

- **iGRC**: 4-5 (UAS < 100 kg, profilo BVLOS, popolazione sparsa montana — caratteristica intermedia tra zona popolata e zona isolata)
- **Mitigazioni applicabili**: M1 strategic mitigation (geofencing + restricted area), M2 tactical mitigation (parachute / emergency landing)
- **Final GRC**: ≈ 2-3 dopo M1+M2
- **iARC**: b (low traffic VLL in Appennino Ligure, aree non controllate Classe G)
- **SAIL atteso**: **II o III**

> **Falsifying observation**: se l'autorità ENAC, nella pre-application, valuta GRC ≥ 6 (es. perché classifica Pentema come "densità popolazione moderate" anziché "sparse"), il SAIL salta a IV o V, con costi di compliance moltiplicati × 3-5 e tempi raddoppiati. **Probabilità: M, impatto: H**. Mitigazione preventiva: pre-application meeting con ENAC nei primi M+0-3.
> **Confidence stima preliminare: low-medium** (basata su SORA 2.5 + analogia con autorizzazioni precedenti italiane, non validata da ENAC).

### 5.1.6 Categorie operative VLOS / EVLOS / BVLOS

Il Reg. 2019/947 art. 2 [^2] e l'art. 26 del Regolamento ENAC APR Ed. 3 [^7] distinguono:

- **VLOS** (Visual Line Of Sight): pilota remoto in contatto visivo diretto con UAS
- **EVLOS** (Extended VLOS): contatto visivo via osservatore aggiuntivo
- **BVLOS** (Beyond VLOS): operazione oltre la distanza di visibilità — categoria target per missioni HALE/VTOL persistenti

Per BVLOS in Italia, oltre alla SORA application secondo SORA 2.5 europea, si applica l'**art. 26** del Regolamento ENAC [^7]: i SAPR (Sistemi Aeromobili a Pilotaggio Remoto) devono dimostrare:
- Sistema di rilevamento e separazione (Detect-And-Avoid) adeguato
- C2 link (Command & Control) robusto con fade margin ≥ 12 dB
- Procedure di Lost-Link con safe behaviour definito
- Copertura assicurativa specifica per BVLOS

---

## 5.2 U-Space — Spazio Aereo Dedicato per UAS

### 5.2.1 Reg. (UE) 2021/664 — U-Space Framework

Il Reg. 2021/664 [^6], applicabile dal **26 gennaio 2023**, istituisce il framework dello **spazio aereo U-Space** dell'UE per integrare le operazioni UAS nello spazio aereo civile. L'U-Space:

- È un **volume di spazio aereo designato** dall'autorità nazionale (in Italia: ENAC, su proposta di Comune/Operatore/Servizi)
- È gestito da uno o più **USSP** (U-space Service Provider) certificati
- Eroga servizi obbligatori (network identification, geo-awareness, UAS flight authorization, traffic information) e opzionali (weather, conformance monitoring, ecc.)
- Si appoggia a un **CISP** (Common Information Service Provider) per la gestione dati condivisi

Per il Percorso 6A (Pentema) l'U-Space è **applicabile potenzialmente**: se Regione Liguria + Comune Torriglia richiedono istituzione di un U-Space su Pentema, le operazioni Firmamento si svolgerebbero in coordinamento con USSP (probabilmente **D-Flight** — vedi §5.2.3).

### 5.2.2 Reg. (UE) 2021/665 e 2021/666 — Modifiche Connesse

Il Reg. 2021/665 [^non-incluso-source] modifica il Reg. 2017/373 per integrare l'U-Space nel sistema ATM/ANS. Il Reg. 2021/666 modifica il Reg. 923/2012 (SERA — Standardised European Rules of the Air) per le regole di circolazione applicabili a UAS in U-Space. Sono modifiche tecniche operative, da considerare nella fase di engagement con ENAV.

### 5.2.3 ENAC Linee Guida U-Space LG-2023/006

L'ENAC [^9] ha pubblicato le **Linee Guida U-Space Ed. 1** del **19 dicembre 2023**, in attuazione del Reg. UE 2021/664. Le Linee Guida disciplinano:

| Sezione | Contenuto |
|---|---|
| §7-12 | Istituzione di uno U-Space all'interno dello spazio aereo nazionale, soggetti titolati, Airspace Risk Assessment (ARA), provvedimento di istituzione |
| §13 | Certificazione USSP/CISP — domande, team di certificazione, verifica requisiti, rilascio certificato |
| §14-16 | Inizio/cessazione fornitura servizi, sorveglianza fornitore, fatturazione |

I **3 allegati** delle LG [^10] disponibili nel repository (`fonti/ALLEGATO-1...USSP.docx`, `ALLEGATO-2...U-SPACE.docx`, `ALLEGATO-3...CISP.docx`) forniscono i moduli di domanda di certificazione USSP, comunicazione fornitore, e domanda di certificazione CISP. Sono operativamente rilevanti se Firmamento decide di erogare direttamente servizi U-Space (non scenario base, **D-Flight** è il primo USSP+CISP certificato in EU [^11]).

**Stato U-Space Italia 2026 (aggiornato gennaio 2026):**
- ENAC ha pubblicato il **Regolamento U-Space Edizione 1** in consultazione pubblica (avviso 14 gennaio 2026, contributi entro aprile 2026)
- **D-Flight** è il primo **USSP + CISP** europeo certificato
- Prima area U-Space italiana: **R100 San Salvo** (Provincia di Chieti, Abruzzo), attiva da 28 novembre 2025

> **Source provenance**: ENAC LG-2023/006 (`fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md`), confidence **high**.

---

## 5.3 Quadro Italia — Recepimento e Normativa Nazionale

### 5.3.1 Recepimento — D.Lgs. 28 maggio 2018, n. 76

Il **D.Lgs. 76/2018** [^non-incluso] recepisce in Italia il quadro EU UAS pre-2019. È stato superato dal Reg. UE 2019/947 (direttamente applicabile) ma resta riferimento per le sanzioni amministrative nazionali.

### 5.3.2 ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Edizione 3 + Emendamento 1

Il **Regolamento APR Ed. 3** del 11 novembre 2019 + **Emendamento 1** del 14 luglio 2020 [^7] è il riferimento normativo italiano consolidato per UAS. Si articola in **38 articoli** che disciplinano:

| Capo | Articoli | Contenuto chiave |
|---|---|---|
| I — Generale | 1-5 | Premessa, applicabilità, scopo, fonti, definizioni |
| II — Caratteristiche APR | 6-7 | Classificazione APR, impiego SAPR |
| III — Operazioni | 8-13 | Operazioni non critiche / critiche, autorizzazione, APR ≤ 2 kg, certificazione di progetto |
| IV — Aeronavigabilità | 14-19 | Registrazione, aeronavigabilità, acustica, autorizzazione operatore, manutenzione |
| V — Personale | 20-23 | Pilota APR, attestati Operazioni Non Critiche / Critiche, Centri di Addestramento |
| VI — Spazio Aereo | 24-27 | Utilizzo spazio aereo, interagenza traffico, **BVLOS (art. 26)**, ANS |
| VII — Altre disposizioni | 28-34 | Documentazione, eventi, sanzioni, **Data Link (art. 31)**, Assicurazione, **Security (art. 33)**, **Protezione dati e privacy (art. 34)** |
| VIII — Disposizioni finali | 35-38 | Generalità, tariffe, transitorie, decorrenza |

**Articoli chiave per il Percorso 6A** (Pentema VTOL):

- **Art. 10 — Operazioni Critiche**: include operazioni urbane, su persone, BVLOS, sopra infrastrutture critiche. Le missioni Firmamento sono **operazioni critiche** in maggioranza, richiedendo l'autorizzazione operativa ai sensi del successivo Art. 11.
- **Art. 11 — Autorizzazione e dichiarazione**: distingue **autorizzazione** (operazioni critiche, soggette a SORA) e **dichiarazione** (scenari standard). Per Pentema BVLOS in Specific Category, è **autorizzazione**.
- **Art. 26 — BVLOS**: condizioni per le operazioni oltre la distanza di visibilità, inclusa la presentazione del **documento SORA emesso dal JARUS** (sostituito dalla versione europea per le AMC EASA dall'Amendment 3 di settembre 2025).
- **Art. 31 — Data Link**: standard di affidabilità del link C2.
- **Art. 33 — Security**: cybersecurity e prevenzione interferenze non autorizzate.
- **Art. 34 — Protezione dati e privacy**: rinvio al D.Lgs. 196/2003 + GDPR; trattamento dati personali tramite UAS.

> **Source provenance** [^7]: `fonti/Regolamento_APR_Ed_3_Emend_1.md`. **Confidence: high** (norma in vigore).

### 5.3.3 ENAC Linee Guida U-Space (vedi §5.2.3)

### 5.3.4 ENAC Piano Strategico Nazionale Advanced Air Mobility (AAM) 2021-2030

Il **Piano Strategico AAM** [^12], pubblicato da ENAC con il supporto di PwC Strategy, definisce la visione decennale italiana sulla mobilità aerea avanzata, articolata in tre pilastri:

1. **Piano Strategico** — visione politica
2. **Roadmap** (Allegato 1) — gap analysis regolatorio, tecnologico, infrastrutturale + interventi nel decennio
3. **Business Plan** (Allegato 2) — modelli economici, infrastrutture (vertiporti), investimenti

**Rilevanza per Firmamento:**
- Stabilisce il framework di **ecosistema italiano AAM** entro il quale HAPS può inserirsi come **layer stratosferico**
- Identifica stakeholder istituzionali: ENAC, ENAV, MIT, MIMIT, Leonardo, Telespazio, Aeroporti di Roma
- Stima investimenti **€1.8 mld 2021-2030** per realizzare l'ecosistema AAM
- Riconosce esplicitamente l'**Advanced Air Mobility** come categoria includente UAV, eVTOL, e (in prospettiva) HAPS

**Posizionamento Firmamento nel Piano AAM:**
Firmamento non è citata nominalmente nel Piano AAM (è di scala più piccola dei player istituzionali). Tuttavia, **lo Studio di Fattibilità HALE può argomentare l'inserimento di Firmamento** come operatore di servizi stratosferici nel framework AAM-Italy, posizionandosi come **complementare** (non concorrente) di Leonardo/TAS/Telespazio.

> **Source provenance** [^12]: `fonti/01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.md`, `fonti/02_AAM-Italian-Ecosystem-Roadmap_web-1.md`, `fonti/03_AAM-Business-Plan_web-1.md`. **Confidence: high**.

---

## 5.4 Strategia di Categoria EASA per i Due Percorsi

### 5.4.1 Percorso 6A — Specific Category, SAIL II-III

**Premessa**: il Percorso 6A utilizza una **piattaforma commerciale TRL 8-9** (es. JOUAV CW-30E o Quantum Trinity F90+) per missioni operative pilota a Pentema (Torriglia, GE) nell'arco dei primi 12 mesi.

**Iter regolatorio raccomandato:**

1. **M+0-3 — Pre-application meeting ENAC** (chiave: chiusura DR-004)
   - Presentazione ConOps preliminare a ENAC Direzione Regolamentazione UAS
   - Discussione classificazione SAIL preliminare
   - Identificazione gap documentali
2. **M+3-6 — Preparazione SORA application**
   - ConOps dettagliato
   - GRC e ARC computation con mitigazioni M1+M2+M3
   - SAIL determination e identificazione 24 OSO applicabili
   - Operations Manual + Procedure
3. **M+6-9 — Submission SORA + Operator Declaration**
   - Submission SORA application ENAC
   - Operations Manual + Maintenance Manual + Training Programme
   - Insurance certificate
   - Risposta a richieste integrazioni ENAC
4. **M+9-12 — Authorization issuance**
   - Autorizzazione operativa ENAC
   - Conduzione prime missioni pilota Pentema
   - Reporting eventi (art. 29 Reg. ENAC APR Ed. 3)

**Costi stimati iter regolatorio 6A** (`agents/aviation-regulatory-counsel.md`):
- SORA application + supporto legale: €30-80k
- Audit + integrazioni: €10-30k
- Pre-application meetings + travel: €5-15k
- **Totale**: €45-125k (incluso nel CapEx 6A)

> **Falsifying observation Percorso 6A**: se entro M+6 la pre-application ENAC genera un GRC > 5 o un SAIL ≥ IV, il modello operativo va ripensato (es. ridurre area di missione, eliminare BVLOS in fase iniziale). Probabilità: M, impatto: M-H. Mitigazione: M1+M2 documentate fin dal ConOps preliminare.

### 5.4.2 Percorso 6B — Certified Category, Special Condition HAPS

**Premessa**: il Percorso 6B sviluppa un **HALE solare** per operazioni stratosferiche (~20 km AGL) persistenti. Per operazioni civili commerciali, **non esiste alternativa** alla Certified Category secondo Reg. 2019/947.

**Gap noto** (showstopper #1 regolatorio 6B):
- **EASA non ha pubblicato** Certification Specifications dedicate per HAPS
- La **Special Condition Light UAS (SC-Light-UAS)** copre UAS < 600 kg MTOM ma non è progettata per operazioni continuative perennial in stratosfera
- Il framework Certified italiano richiede analogia caso-per-caso con aviazione manned

**Strategia operativa raccomandata:**

1. **M+0-12 — Engagement preliminare**
   - Identificazione Certification Authority appropriata (EASA Cologna come default)
   - Dialogue preliminare con EASA UAS Department e Innovation Network
   - Engagement parallelo CIRA (vedi §5.11.3) per partnership R&D consortium
2. **M+12-24 — Certification Plan**
   - Sviluppo Certification Basis custom
   - Identificazione standard applicabili (STANAG 4671, ARP4754A, DO-178C, ARP4761)
   - Identification Means of Compliance per requisiti non coperti da standard maturi
3. **M+24-48 — Compliance Demonstration**
   - Analisi + simulazioni + test ground
   - Test articolo subscale + GVT (Ground Vibration Test) + structural test
   - Documentazione di compliance progressive
4. **M+48+ — Type Certificate / Special Condition**
   - Issuance Type Certificate (TC) o Special Condition equivalente
   - Operating Certificate (AOC) per servizio commerciale

**Costi stimati iter regolatorio 6B** (`agents/aviation-regulatory-counsel.md`):
- Certification Plan + Means of Compliance negotiation: €500k-1.5M
- Compliance Demonstration (analisi + test): €1-3M (inclusi nel R&D €5.5-11M Phase B)
- TC issuance: €0.3-0.8M
- **Totale**: €2-5M (su 36-48 mesi)

**Tempistiche realistiche per il TC** (base rate aerospace certifications):
- TC custom per aircraft innovativo: **3-7 anni** in scenari ottimistici
- Esempio: PHASA-35 (BAE Prismatic) — operatività dichiarata "from 2026" con TC ancora in negoziazione, dopo 6+ anni di flight test
- Esempio: Zephyr AALTO Airbus — operatività "commerciale" da 2024, ma per **missioni Government/DoD**, non Certified civile generale

> **Falsifying observation Percorso 6B**: se entro M+24 EASA non ha aperto formalmente un percorso Special Condition o RMT (Rulemaking Task) per HAPS, il TC entro M+48-60 è strutturalmente non raggiungibile, e la Fase 3 della visione 10 anni va ridimensionata o rinviata.
> **Probabilità: M-H, impatto: H**. Vedi §5.10.1 (showstopper formale).

---

## 5.5 Spettro Radio

### 5.5.1 ITU Radio Regulations — Bande HAPS

L'**International Telecommunication Union** (ITU) disciplina globalmente l'allocazione delle bande radio nel **Radio Regulations** (Edition 2024, basata su WRC-23 Dubai). Le **bande dedicate HAPS** riconosciute dall'ITU sono [^13]:

| Banda | Range | Uso primario | Stato Italia |
|---|---|---|---|
| **6.4-6.7 GHz** | Gateway HAPS-terra | WRC-19 worldwide | Conferma WRC-23 |
| **27.9-28.2 GHz** | Gateway feeder | WRC-19 worldwide | Allocata |
| **31-31.3 GHz** | Gateway feeder | WRC-19 worldwide | Allocata |
| **38-39.5 GHz** | Service link (extended) | WRC-19 + WRC-23 enhancement | Coordinamento richiesto vs FSS |
| **47.2-47.5 GHz** | Service link (future) | WRC-19 | Future expansion |
| **47.9-48.2 GHz** | Service link (future) | WRC-19 | Future expansion |
| **24.25-27.5 GHz** | (in discussione WRC-27) | Solo Americas attualmente | Future expansion globale |

**Per il Percorso 6A** (VTOL pilota Pentema):
- Servizi locali con LTE/5G tattico → bande 2.4 GHz, 5.8 GHz (ISM) per C2 link, e bande operatori commerciali (700 MHz, 1.8 GHz, 2.6 GHz, 3.6 GHz) per il payload con accordo operatore
- C2 SATCOM backup → bande L (Iridium Certus) o Ka (Starlink/OneWeb), con vincolo geopolitico (vedi `RESERVED-rischi-geopolitici.md`)

**Per il Percorso 6B** (HALE):
- Service link → S-band (2.0-2.2 GHz NTN 3GPP n255/n256) oppure 700 MHz (5G NR rural)
- Feeder link → bande HAPS dedicate (31 GHz preferita per fade margin)

> **Source provenance**: ITU-R P.618-14 (`fonti/R-REC-P.618-14-202308-I.md`), 3GPP TR 38.811 (`fonti/38811.md`), 3GPP TR 38.821 v16.2.0 (`fonti/3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md`). **Confidence: high**.

### 5.5.2 AGCOM e Piano Nazionale di Ripartizione delle Frequenze (PNRF)

L'**AGCOM** (Autorità per le Garanzie nelle Comunicazioni) rilascia in Italia le licenze individuali per usi commerciali del radio spettro, ai sensi del **D.Lgs. 259/2003 — Codice delle Comunicazioni Elettroniche** (aggiornato dal D.Lgs. 207/2021). Il **PNRF — Piano Nazionale di Ripartizione delle Frequenze** è gestito dal **MIMIT** e integra i risultati delle WRC ITU.

**Iter di acquisizione licenza per HAPS in Italia (stimato):**

1. Identificazione banda HAPS ITU applicabile
2. Verifica allocation nel PNRF italiano (eventualmente richiesta di nuova allocazione)
3. Domanda di licenza individuale AGCOM
4. Parere tecnico MIMIT
5. Coordinamento internazionale ITU (se interferenze con paesi confinanti)
6. Rilascio licenza

**Tempistiche realistiche**: 12-36 mesi per banda HAPS dedicata, in funzione di:
- Disponibilità banda nel PNRF (sì/no)
- Coordinamento ITU richiesto
- Eventuali contestazioni operatori terrestri esistenti

> **Falsifying observation §5.5.2**: se AGCOM non istituisce un percorso licensing specifico per HAPS entro WRC-27 (novembre 2027), o se la pressione lobby degli operatori terrestri (TIM, Vodafone, Iliad, WindTre) blocca l'allocation, il payload telecom HALE è **inutilizzabile in operazione commerciale** in Italia fino a 2030+. Probabilità: M, impatto: H. Mitigazione: ingresso in tavolo AGCOM Spettro fin dalla Fase 2 della visione.

### 5.5.3 Conformità 3GPP NR-NTN

Lo standard **3GPP TR 38.811** (Rel. 15) [^14] e **3GPP TR 38.821 v16.2.0** (Rel. 16, marzo 2023) [^15] forniscono il framework per l'integrazione delle Non-Terrestrial Networks nello standard 5G NR. HAPS è **esplicitamente supportata** come scenario NTN [^14, §6.1.5]:

> *"NR UEs as defined by TS 38.101-1 can support HAPS deployments with no additional changes."*

Implicazione per Firmamento: il payload telecom HALE può ospitare un **gNB (next-generation Node B) regenerative** già nello standard, garantendo compatibilità diretta con UE 5G utenti terrestri. Releases 18 e 19 estendono ulteriormente le capacità (regenerative payloads, inter-satellite links, scheduling avanzato).

---

## 5.6 Privacy e Protezione dei Dati Personali

### 5.6.1 GDPR e D.Lgs. 196/2003 novellato

Il **Reg. (UE) 2016/679 — GDPR** [^16] disciplina il trattamento dei dati personali nell'UE, recepito in Italia dal **D.Lgs. 196/2003 "Codice Privacy"** come novellato dal **D.Lgs. 101/2018**. Per il progetto HALE/VTOL si applicano tutti i principi:

- **Liceità, correttezza, trasparenza** (art. 5.1.a)
- **Limitazione della finalità** (art. 5.1.b) — l'EO per monitoraggio frane non può essere usato per altri scopi senza nuova base giuridica
- **Minimizzazione** (art. 5.1.c) — risoluzione, durata, copertura proporzionate al bisogno
- **Esattezza** (art. 5.1.d)
- **Limitazione della conservazione** (art. 5.1.e) — definita per tipo di dato (imagery emergenza 30 giorni raw, prodotti derivati anonimi indefinitamente)
- **Integrità e riservatezza** (art. 5.1.f) — security misures

**Basi giuridiche del trattamento** per i casi d'uso del progetto (vedi `agents/data-privacy-counsel.md`):

| Caso d'uso | Base giuridica primaria | Base giuridica alternativa |
|---|---|---|
| Monitoraggio frane | Interesse pubblico (art. 6.1.e) | Compito istituzionale Protezione Civile |
| Antincendio boschivo | Interesse vitale (art. 6.1.d) in emergenza | Interesse pubblico (PC) |
| Connettività NTN | Contratto (art. 6.1.b) | Codice Comunicazioni Elettroniche |
| Mapping infrastrutture stradali | Interesse pubblico + minimizzazione | Anonimizzazione obbligatoria |
| Servizi cooperative agricole | Consenso (art. 6.1.a) della cooperativa proprietaria | Contratto |
| Borgo Pentema (sperimentale) | Necessità informativa + minimizzazione | Consenso informato comunità |

### 5.6.2 Posizione del Garante Privacy su Sorveglianza Aerea

Il **Garante Privacy Italia** ha pubblicato linee guida e provvedimenti relativi all'uso di UAS per sorveglianza:

- **FAQ Garante sui droni** — uso personale e professionale, principio di prossimità
- **Provv. Garante n. 386 del 9 settembre 2021** — istruzioni trattamento dati pandemia, applicabili a sorveglianza
- Linee guida **AI Act compliance** (2024) per sistemi biometrici

**Posizione di principio del Garante**: la **sorveglianza persistente continuativa** di un territorio è equiparabile a sorveglianza di massa, e richiede DPIA + base giuridica forte (preferibilmente **non** "interesse legittimo del titolare" art. 6.1.f, che il Garante ha più volte censurato per uso UAS).

**Implicazione per Firmamento:**
- DPIA preliminare obbligatoria (vedi Volume 2, Allegato A.12)
- Privacy-by-design hardware (blur volti/targhe a bordo)
- Geofence di esclusione su aree residenziali sensibili
- Conservazione differenziata: imagery non-emergenza max 30 giorni raw, prodotti derivati anonimi

> **Falsifying observation §5.6.2**: se il Garante Privacy, in risposta a un eventuale reclamo da cittadini Pentema o cooperative, emette provvedimento ex art. 58 GDPR sospendendo le missioni EO, l'intera linea di servizio EO ad alta risoluzione è bloccata fino a ridisegno con anonimizzazione hardware. Probabilità: L-M (Pentema comunità di **14 residenti ISTAT**, basso rischio numerico di reclami ma alto rischio mediatico se singolo evento polarizza), impatto: M. Mitigazione: **engagement preventivo comunità Pentema** + DPIA pubblica + governance condivisa (vedi `agents/data-privacy-counsel.md`).

### 5.6.3 Direttiva ePrivacy 2002/58/CE per Dati Telecom

I dati di traffico e metadati di comunicazione (payload telecom NTN) sono ulteriormente disciplinati dalla **Direttiva ePrivacy** (in attesa del nuovo Reg. ePrivacy UE). In Italia: D.Lgs. 196/2003 artt. 121-132.

---

## 5.7 Cybersecurity

### 5.7.1 Direttiva NIS2 (D.Lgs. 138/2024)

La **Direttiva (UE) 2022/2555 — NIS2**, recepita in Italia dal **D.Lgs. 138/2024**, disciplina la sicurezza delle reti e dei sistemi informativi per soggetti operanti in **settori essenziali e importanti**. Il servizio Firmamento può rientrare in:

- **Sezione 1 — settori essenziali**: Trasporti (aero); Infrastrutture digitali; Settore aerospaziale (in alcune accezioni)
- **Sezione 2 — settori importanti**: Servizi digitali; Ricerca

Implicazioni se Firmamento è qualificata **soggetto essenziale**:
- Adozione misure di gestione del rischio (art. 24 NIS2)
- Notifica incidenti significativi entro 24h all'**ACN — Agenzia per la Cybersicurezza Nazionale**
- Sorveglianza ACN
- Sanzioni amministrative

### 5.7.2 DO-326A / ED-202A — Airworthiness Security

Per la cybersecurity della parte volante (avionica + payload + link C2), si applica lo standard **DO-326A / ED-202A** (Airworthiness Security Process Specification), declinato in **DO-356A / ED-203A** (security methods). Riferimento per la fase di certification del Percorso 6B HALE.

---

## 5.8 Standard Tecnici Applicabili (Compliance Trasversale)

| Standard | Ambito | Applicabilità progetto HALE/VTOL |
|---|---|---|
| **AS/EN 9100** | Quality Management Aerospace | Cap. 5 dichiarazione di conformità (obbligatoria per bandi pubblici aerospaziali) |
| **ISO 9001** | Quality Management generale | Sistema di gestione qualità Firmamento |
| **ISO 14001** | Environmental Management | Sostenibilità (narrativa ESG fibra di lino) |
| **ISO/IEC 27001** | Information Security Management | NIS2 compliance |
| **ARP4754A** | Development of civil aircraft & systems | Process aircraft-level safety (DAL allocation) |
| **ARP4761** | Safety assessment process | FHA / PSSA / SSA — Cap. 6 |
| **DO-178C / ED-12C** | Software considerations | FCS, GNC, DAA software DAL-A/B/C |
| **DO-254 / ED-80** | HW design assurance | FPGA, ASIC certificati |
| **DO-326A / ED-202A** | Airworthiness Security | Cybersecurity volante |
| **DO-365B / ED-269** | Detect-And-Avoid | DAA performance (Reg.UE 2019/947) |
| **STANAG 4671** | UAV system airworthiness | Possibile riferimento per Special Condition HAPS |
| **EN 4179** | NDT aerospace personnel | Quality control compositi (Cap. 6, fibra di lino) |
| **EN 9110** | Maintenance Organisations | Cap. 9 Piano di Manutenzione |

> **Dichiarazione di conformità** richiesta per la presentazione dello Studio a bandi pubblici (vedi Cap. 5.9.2 e Vol. 2 dichiarazioni allegate).

---

## 5.9 Conformità al Codice dei Contratti Italiano (art. 41 D.Lgs. 36/2023)

### 5.9.1 PFTE — Struttura ex Allegato I.7

Il **D.Lgs. 36/2023 — Nuovo Codice dei Contratti Pubblici** [^17], art. 41, definisce **due livelli di progettazione** per opere pubbliche:

1. **Progetto di Fattibilità Tecnico-Economica (PFTE)** — il presente Studio
2. **Progetto Esecutivo (PE)** — fase successiva

L'**Allegato I.7** [^17, All. I.7] definisce i contenuti minimi di una serie di documenti progressivi:

| Documento ex art. 41 | Stato per il progetto Firmamento |
|---|---|
| **Quadro Esigenziale (QE)** | Cap. 1 dello Studio (= Inquadramento) |
| **Documento di Fattibilità delle Alternative Progettuali (DOCFAP)** | = sintesi dei Trade Study (Vol. 2 Allegato A.3) |
| **Documento di Indirizzo della Progettazione (DIP)** | Post-Studio (M+12+) |
| **Progetto di Fattibilità Tecnico-Economica (PFTE)** | = lo Studio di Fattibilità HALE complessivo |

**Elaborati minimi PFTE** [^17, All. I.7]:

1. Relazione generale
2. Relazioni specialistiche (geologica, idrogeologica, ambientale, sismica, archeologica)
3. Studio di Impatto Ambientale preliminare (se VIA applicabile)
4. Elaborati grafici (planimetrie, sezioni, prospetti)
5. Calcoli preliminari (strutture, impianti)
6. **Computo Metrico Estimativo**
7. **Quadro Economico**
8. Cronoprogramma
9. **Piano Economico-Finanziario** (NPV, IRR, payback, ROI)
10. Piano di Manutenzione preliminare
11. **Piano di Sicurezza e Coordinamento (PSC)** preliminare
12. Documentazione fotografica del contesto

**Stato di copertura nello Studio di Fattibilità Firmamento:**
- Documenti 1, 2, 5, 8: presenti nei Cap. 1-9
- Documenti 6, 7, 9: nel Cap. 8 + Vol. 2 Allegati
- Documenti 10, 11, 12: Vol. 2 Allegati A.10, A.11, A.13

### 5.9.2 Dichiarazioni di Conformità per Bandi Pubblici

Per la presentazione dello Studio a bandi pubblici italiani (Cooding Coopfond, PNRR Aerospazio, FESR Regione Liguria, Horizon Europe), il documento deve dichiarare conformità a:

- **D.Lgs. 36/2023 art. 41 e Allegato I.7** (PFTE)
- **D.Lgs. 76/2018 + Reg. UE 2019/947, 2019/945** (UAS)
- **Reg. UE 2021/664** + ENAC LG-2023/006 (U-Space, ove applicabile)
- **EASA AMC/GM Issue 1 Amendment 3** (settembre 2025) per la SORA
- **AS/EN 9100** + **ISO 9001** + **ISO/IEC 27001** (sistemi di gestione)
- **GDPR + D.Lgs. 196/2003 novellato** (privacy)
- **NIS2 + D.Lgs. 138/2024** (cybersecurity)
- **NASA SE Handbook Rev 2 (NASA/SP-2016-6105)** (metodologia ingegneristica — segnale di rigore, non obbligatoria per bandi italiani)

I template di dichiarazione sono allegati al Vol. 2 dello Studio (Allegato A.8).

---

## 5.10 Gap Analysis Regolatorio

### 5.10.1 Showstopper #1 — Mancanza Framework HAPS Civile

**Descrizione**: Né EASA né ENAC hanno pubblicato un framework regolatorio dedicato per operazioni HAPS civili continuative (autorizzazione, certificazione di tipo, integrazione spazio aereo). La SC-Light-UAS è limitata a UAS < 600 kg MTOM e non è progettata per perennial flight.

**Tempistiche realistiche per copertura**:
- Apertura RMT EASA dedicato HAPS: **2027-2029** (stima)
- Pubblicazione NPA: **2028-2030**
- Adozione Implementing Regulation: **2030-2032**
- Type Certificate primo HAPS commerciale civile EU: **2032-2035**

**Implicazione per il Percorso 6B**:
- Fase 3 della visione (M+36 → M+72) può procedere solo via **Special Condition negoziata caso per caso**
- Tempistiche TC realistiche: **5-8 anni** dall'avvio engagement formale, con costi €5-15M solo per la certificazione (incluso nel R&D Phase B €5.5-11M parzialmente)

> **Showstopper formalmente registrato come RSK-REG-001 nel Risk Register**: P = High (5), I = High (4), Score = 20 🔴. Mitigation: engagement EASA Innovation Network + partnership con EuroHAPS-adjacent (CIRA, TAS) per leveraging Special Condition consortium.

> **🔬 Falsifying observation aggiuntive linkate**: vedi `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md` **FO-ADD-05** (EASA HAPS framework apertura 2030 — al M+36 se no RMT/CRD/NPA aperto, path Certified 6B bloccato 5-10 anni aggiuntivi, trigger TRG-B2R-01 scenario B2-relaxed) + **FO-ADD-06** (CIRA partnership willingness al M+12 — se no LoI/MoU CIRA, pivot a POLITO DIMEAS HELIPLAT lineage).

### 5.10.2 Gap #2 — U-Space Italia in Costruzione

**Descrizione**: Il framework U-Space italiano è in fase di consultazione (Regolamento ENAC Edizione 1, gennaio 2026, contributi entro aprile 2026). La prima area U-Space italiana (R100 San Salvo, Abruzzo) è attiva da novembre 2025. L'estensione a Liguria e a Pentema non è schedulata.

**Implicazione per il Percorso 6A**:
- Le missioni VTOL Pentema possono procedere **senza** U-Space (lo spazio aereo Appennino Ligure è prevalentemente Classe G non controllato), con autorizzazione ENAC standard SORA
- Tuttavia, all'attivazione di un U-Space sopra Pentema (ipotetica entro M+12-24), le operazioni andranno integrate con USSP (D-Flight)
- Costo aggiuntivo stimato integrazione USSP: €5-20k/anno

**Probabilità di attivazione U-Space Pentema entro M+24**: L-M (Pentema non è priorità nazionale, ma Regione Liguria potrebbe richiederla).

### 5.10.3 Gap #3 — Spettro Radio HAPS Italia

**Descrizione**: Le bande HAPS dedicate ITU (6.4-6.7 / 27.9-28.2 / 31-31.3 / 38-39.5 / 47.2-48.2 GHz) non sono ancora pienamente allocate operative in Italia tramite licenza AGCOM. Il PNRF MIMIT le riconosce post-WRC-19/23 ma le procedure di licensing operativo sono in costruzione.

**Implicazione**:
- Percorso 6A: **gestibile** con bande ISM (C2) + accordi operatori (payload commerciale)
- Percorso 6B: **bloccante** per il payload NTN commerciale stratosferico senza licensing dedicato. Vedi Falsifying observation §5.5.2.

---

## 5.11 Strategia Regolatoria e Engagement Plan

### 5.11.1 Percorso 6A — Roadmap Operativa

Vedi §5.4.1 per l'iter dettagliato.

**KPI**:
- M+3: meeting ENAC con feedback documentato
- M+9: SORA application submitted
- M+12: autorizzazione operativa rilasciata + prime missioni Pentema

### 5.11.2 Percorso 6B — Strategia Certified

Vedi §5.4.2 per l'iter dettagliato.

**KPI**:
- M+12: framework Special Condition aperto da EASA o committment a RMT
- M+24: Certification Plan approvato
- M+48+: TC issuance (out-of-scope dello Studio attuale)

### 5.11.3 Engagement Plan Istituzionale

| Autorità / Stakeholder | Trigger | Frequenza | Owner | Documento di engagement |
|---|---|---|---|---|
| **ENAC** Direzione Regolamentazione UAS | Pre-application 6A | Q | aviation-regulatory-counsel | Lettera di intent + ConOps |
| **ENAC** Direzione AAM | Posizionamento HALE | Semestrale | sovereign-strategist | Position paper "Italian Stratospheric Layer" |
| **EASA** UAS Department | Special Condition 6B | Annuale | aviation-regulatory-counsel | Engagement letter + concept paper |
| **EASA** Innovation Network | Innovation track HAPS | Annuale | sovereign-strategist | RMT request |
| **AGCOM** Direzione Reti Servizi | Spettro HAPS | Semestrale | telecom-ntn-payload-expert | Domanda licensing + analisi non-interferenza |
| **MIMIT** Direzione Comunicazioni | PNRF + ITU coordination | Annuale | telecom-ntn-payload-expert | Posizionamento PNRF |
| **MIMIT** Direzione Aerospazio | Strategia nazionale + PNRR | Q | sovereign-strategist | Project briefing |
| **ENAV** | U-Space + spazio aereo | Semestrale | avionics-gnc-engineer | Operational coordination doc |
| **D-Flight** (USSP+CISP) | Integrazione U-Space | Sì se U-Space Pentema | avionics-gnc-engineer | Service agreement |
| **Garante Privacy** | DPIA + sorveglianza | Annuale | data-privacy-counsel | DPIA pubblica + governance |
| **ACN — Cybersicurezza** | NIS2 compliance | Annuale | (cybersec, futuro) | NIS2 audit annuale |
| **CIRA** | Partnership R&D 6B + EuroHAPS-adjacent | Q | sovereign-strategist | MOU R&D |
| **DTA Puglia / GATB** | Test bed BVLOS 6A | Annuale | vtol-uas-specialist | Service agreement |

---

## 5.12 Verdetto Regolatorio

Il quadro regolatorio è **sostanzialmente favorevole al Percorso 6A** (VTOL pilota Pentema in categoria Specific SAIL II-III) e **condizionalmente percorribile per il Percorso 6B** (HALE in categoria Certified, dipendente da apertura framework EASA HAPS).

**Verdetto Percorso 6A: GO** dal punto di vista regolatorio.
- Pre-condizioni: pre-application meeting ENAC entro M+3, SORA application entro M+9.
- Showstopper: nessuno bloccante; rischio gestibile RSK-REG-002 (SORA SAIL Pentema), mitigabile con M1+M2.

**Verdetto Percorso 6B: HOLD / Go Condizionato Estremo** dal punto di vista regolatorio.
- Pre-condizioni: engagement EASA + apertura formale framework Special Condition HAPS entro M+24-36.
- Showstopper formalmente registrato: RSK-REG-001 (mancanza framework HAPS) — non bloccante per la fase preparatoria R&D, bloccante per operatività commerciale.

Entrambi i verdetti sono coerenti con la raccomandazione del **Briefing** iniziale e con la **visione 10 anni** (`riferimenti/visione-10-anni.md`).

---

## 5.13 Red Team Check — Regulatory Adversary

L'agente `regulatory-adversary` ha condotto stress-test del presente capitolo. Sintesi (vedi anche `agents/regulatory-adversary.md` Scenari R1-R7):

**Critiche principali del Red Team:**

1. **Sul SAIL Pentema**: la stima preliminare GRC 4-5 → final 2-3 è **ottimistica**. ENAC potrebbe classificare Pentema "popolazione moderate" e portare GRC a 6, SAIL a IV-V. **Risposta**: la stima è dichiarata **low-medium confidence** ed è subordinata alla pre-application meeting (DR-004). La pianificazione 6A include questa contingency con €30k buffer SORA.

2. **Sul SORA 2.5 europea**: l'Amendment 3 di settembre 2025 è **fresca** (3 mesi dalla pubblicazione al M+0 Firmamento). Possibili evoluzioni dottrinali ENAC nei primi 6 mesi di applicazione. **Risposta**: l'engagement con ENAC nei primi 3 mesi serve specificamente a calibrare l'application su interpretazione corrente.

3. **Sul Percorso 6B Special Condition**: il claim "Special Condition negoziata caso per caso" è **astratto**. Nessuna HAPS commerciale civile ha ancora TC EU emesso. La base rate è 0/N. **Risposta**: registrato come RSK-REG-001 score 20 🔴, mitigazione tramite partnership con consorzio (CIRA + TAS) e engagement EuroHAPS-adjacent. Il Percorso 6B è dichiarato Hold / Go Condizionato Estremo proprio per riconoscere questa incertezza.

4. **Sul Garante Privacy**: il rischio sospensione missioni EO è **sottostimato** (P = L-M). Casi recenti (drone deployments urbani 2023-2024) hanno visto provvedimenti rapidi. **Risposta**: aggiunto come falsifying observation §5.6.2 e mitigazione preventive engagement comunità Pentema.

5. **Sul Golden Power**: il capitolo **non tratta** il rischio classificazione strategica IT (D.L. 21/2012). **Risposta**: il rischio è trattato in documento riservato `RESERVED-rischi-geopolitici.md` per scelta strategica del progetto, non nello Studio pubblico.

6. **Sull'engagement plan**: la frequenza dichiarata è **ottimistica** per le capacità di una PMI. **Risposta**: il plan è target; la prima fase prioritizza ENAC + EASA + Coopfond, gli altri stakeholder vengono attivati progressivamente.

**Verdetto Red Team**: il capitolo è **sostanzialmente robusto**, con le seguenti **azioni richieste** prima del gate review M+10:

- ☐ Pre-application meeting ENAC entro M+3 con feedback documentato
- ☐ Engagement preliminare EASA entro M+6
- ☐ DPIA preliminare pubblica entro M+6
- ☐ Position paper "Stratospheric Italian Layer" pubblicato entro M+12

---

## 5.14 Riferimenti

[^1]: Regolamento (UE) 2018/1139 del Parlamento Europeo e del Consiglio del 4 luglio 2018, recante norme comuni nel settore dell'aviazione civile, che istituisce un'Agenzia dell'Unione Europea per la Sicurezza Aerea ("Basic Regulation"). EUR-Lex.

[^2]: Regolamento di Esecuzione (UE) 2019/947 della Commissione del 24 maggio 2019, relativo alle regole e procedure per l'operazione di aeromobili senza equipaggio. **Source:** `fonti/CELEX_32019R0947_IT_TXT.md` — **confidence: high**.

[^3]: Regolamento Delegato (UE) 2019/945 della Commissione del 12 marzo 2019, relativo ai sistemi di aeromobili senza equipaggio e a operatori di paesi terzi. **Source:** `fonti/CELEX_32019R0945_IT_TXT.md` — **confidence: high**.

[^4]: EASA ED Decision 2025/018/R del 15 settembre 2025, Amendment 3 to Issue 1 of the Acceptable Means of Compliance and Guidance Material to Commission Implementing Regulation (EU) 2019/947 — 'AMC and GM to Regulation (EU) 2019/947 — Issue 1, Amendment 3'. **Source:** `fonti/ed_decision_2025-018-r.md` + `fonti/annex_to_ed_decision_2025-018-r_1.md` + `fonti/explanatory_note_to_ed_decision_2025-018-r.md` + `fonti/corrigendum_to_ed_decision_2025-018-r.md` — **confidence: high**.

[^5]: JARUS SORA 2.5 (Joint Authorities for Rulemaking on Unmanned Systems), ottobre 2024. Riferimento esterno: http://jarus-rpas.org

[^6]: Regolamento di Esecuzione (UE) 2021/664 della Commissione del 22 aprile 2021, relativo a un quadro normativo per lo U-space. **Source:** `fonti/CELEX_32021R0664_IT_TXT.md` — **confidence: high**.

[^7]: ENAC, Regolamento "Mezzi Aerei a Pilotaggio Remoto" Edizione 3 del 11 novembre 2019 + Emendamento 1 del 14 luglio 2020. **Source:** `fonti/Regolamento_APR_Ed_3_Emend_1.md` — **confidence: high**.

[^9]: ENAC, Linee Guida U-Space LG-2023/006-UAS Edizione 1 del 19 dicembre 2023. **Source:** `fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md` — **confidence: high**.

[^10]: ENAC, Allegati alla LG-2023/006: Allegato 1 — Domanda di certificazione USSP; Allegato 2 — Comunicazione del fornitore di servizi U-Space; Allegato 3 — Domanda di certificazione CISP. **Source:** `fonti/ALLEGATO-1...docx`, `ALLEGATO-2...docx`, `ALLEGATO-3...docx`.

[^11]: D-Flight S.p.A., comunicato 2025 — primo USSP+CISP europeo certificato (joint Leonardo+ENAV+IDS+Techno Sky+Telespazio).

[^12]: ENAC, Piano Strategico Nazionale Advanced Air Mobility (AAM) 2021-2030 + Allegato 1 Roadmap + Allegato 2 Business Plan. **Sources:** `fonti/01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.md`, `fonti/02_AAM-Italian-Ecosystem-Roadmap_web-1.md`, `fonti/03_AAM-Business-Plan_web-1.md` — **confidence: high**.

[^13]: ITU Radio Regulations 2024 (Edition 2024), Article 5 e Resolution 122 (WRC-19), 122-bis (WRC-23). Bande HAPS riconosciute.

[^14]: 3GPP TR 38.811 V15.4.0 (2020-09), Study on New Radio (NR) to support non-terrestrial networks. **Source:** `fonti/38811.md` — **confidence: high**.

[^15]: 3GPP TR 38.821 V16.2.0 (2023-03), Solutions for NR to support non-terrestrial networks (NTN) (Release 16). **Source:** `fonti/3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md` — **confidence: high**.

[^16]: Regolamento (UE) 2016/679 del Parlamento Europeo e del Consiglio del 27 aprile 2016 (GDPR).

[^17]: D.Lgs. 31 marzo 2023, n. 36 — Codice dei contratti pubblici. **Source:** `fonti/2023_0036.md` (testo integrale + Allegati, incluso I.7) — **confidence: high**.

---

## 5.16 Showstopper Regolatori Aggiuntivi (post-Audit Regulatory Adversary M+3)

> **Inserimento post-audit M+3**: l'audit `regulatory-adversary` (vedi `AUDIT-REGULATORY-VOLUME-1.md` §10) ha identificato **15 showstopper regolatori non coperti** dalle sezioni precedenti del Cap. 5. Sono qui formalizzati con riferimento normativo, impatto sul progetto, e mitigazione raccomandata. Tutti vanno aggiunti al Risk Register Vol. 2 Allegato A.2 con score P×I dedicato.

### 5.16.1 AI Act (Reg. UE 2024/1689) — sistemi onboard biometrici

- **Riferimento**: Reg. (UE) 2024/1689 — Artificial Intelligence Act, in vigore dal 1° agosto 2024, applicazione progressiva 2025-2027
- **Impatto progetto**: il payload IR LWIR + processing onboard per **antincendio / SAR (Search And Rescue) / sorveglianza territoriale** può rientrare nella categoria "alto rischio" (Annex III §1 biometria, §5 law enforcement) o "rischio inaccettabile" se identificazione biometrica remota real-time in spazi pubblici (art. 5)
- **Probabilità**: M (40-55%) — dipende dall'interpretazione dei sistemi IR di crisis detection
- **Mitigazione**: privacy by design hardware (blur on-board obbligatorio); esclusione esplicita di riconoscimento biometrico dal scope; engagement Garante + AGID per pre-clearance
- **Falsifying observation**: se al M+6 Garante o AgID classificano i sistemi IR onboard come "alto rischio AI Act", obbligo di conformity assessment + registrazione UE prima delle operazioni

### 5.16.2 EUSPA (EU Space Programme Agency)

- **Riferimento**: Reg. (UE) 2021/696 (EU Space Programme), EUSPA mandato dal 2021
- **Impatto progetto**: EUSPA gestisce Galileo, EGNOS, Copernicus downstream, **GOVSATCOM (governmental satcom services)**. HAPS-related services downstream possono incrociare la sua competenza per (a) accesso a EUSAT / GOVSATCOM, (b) co-finanziamenti, (c) accreditation servizi spaziali
- **Probabilità impatto**: M (30-45%) — più rilevante per Fase 4-5 (consorzio EU)
- **Mitigazione**: engagement EUSPA via CASSINI accelerator + workshop downstream services; mapping intersezione HAPS / GOVSATCOM
- **Falsifying observation**: se EUSPA emette guideline che escludono HAPS dai servizi spaziali downstream EU, accesso a fondi e accreditation EU ridotto

### 5.16.3 EUROCONTROL — coordinamento ATM-ANS HAPS spazio aereo europeo

- **Riferimento**: EUROCONTROL Convention 1960 + Reg. UE 2017/373 (ATM/ANS) + Network Manager Functions
- **Impatto progetto**: Phase B+C 6B HALE operazioni stratosferiche perennial richiedono **coordinamento Network Manager EUROCONTROL** per FL195+ in spazio aereo europeo. Non solo ENAV (nazionale)
- **Probabilità**: H (65-80%) per Fase 3+
- **Mitigazione**: engagement EUROCONTROL precocemente (Y2-Y3), partecipazione a workshop UAM/HAPS Network Manager
- **Falsifying observation**: se EUROCONTROL non rilascia procedure operative per HAPS perennial entro Y4-Y5, operatività cross-border bloccata

### 5.16.4 Part-IS EASA (Information Security) — Reg. UE 2023/203

- **Riferimento**: Reg. (UE) 2023/203 — Part-IS Information Security per organizzazioni aeronautiche; applicazione obbligatoria da febbraio 2026
- **Impatto progetto**: Firmamento come operatore UAS deve istituire un **Information Security Management System (ISMS)** conforme Part-IS, con CISO + audit + procedure documentate; vincolante prima di operazioni commerciali continuative
- **Probabilità**: H (75-85%) — applicabile dal 2026
- **Mitigazione**: assunzione CISO entro M+6; ISMS implementazione entro M+9
- **Falsifying observation**: se ENAC, in audit Part-IS, rileva non-conformità sostanziali, operazioni sospese fino a remediation

### 5.16.5 Codice Penale art. 432-bis — sicurezza traffico aereo

- **Riferimento**: Codice Penale art. 432-bis (Attentati alla sicurezza dei trasporti aerei) + reati colposi connessi (art. 449)
- **Impatto progetto**: in caso di incidente UAS BVLOS con conseguenze (anche solo near-miss vs aviazione manned), **responsabilità penale del PIC (Pilot in Command)** e dell'organizzazione (D.Lgs. 231/2001 modello organizzativo)
- **Probabilità incidente**: L-M (10-25%) ma impatto reputazionale + finanziario H
- **Mitigazione**: assicurazione RC + casco BVLOS adeguata (≥ €5M); D.Lgs. 231 compliance + modello organizzativo; SOPs rigorosi
- **Falsifying observation**: se incidente con conseguenza penale a Y1-Y2, intero modello operativo a rischio

### 5.16.6 AgID / PSN — Polo Strategico Nazionale per hosting dati PA

- **Riferimento**: D.L. 76/2020 (Semplificazioni) art. 33 + Determinazione AgID 307/2022 + Strategia Cloud Italia 2022-2026
- **Impatto progetto**: i dati EO acquisiti per conto della PA italiana (Regione, PC, Comune) **devono essere ospitati in cloud qualificato PSN** o in cloud "certificato AgID" per livelli di criticità medio/alto
- **Probabilità**: H (70-85%) per contratti PA pluriennali
- **Mitigazione**: scelta provider PSN-qualified (TIM Enterprise, Polo PSN, CDP Cloud Polo Strategico) o cloud "qualificato AgID" (Aruba, Engineering, Reply, Almaviva); audit AgID compliance
- **Falsifying observation**: se al M+9 dati Pentema sono stoccati in cloud non-PSN-qualified, contratti PA rifiutati

### 5.16.7 ATEX (Reg. UE 2014/34) — batterie LiS storage e atmosfere esplosive

- **Riferimento**: Direttiva 2014/34/UE (Equipment in Explosive Atmospheres — ATEX) + D.Lgs. 81/2008 Titolo XI
- **Impatto progetto**: storage e ricarica di batterie ad alta densità (LiS, Li-ion) in hangar Pentema → potenziale atmosfera esplosiva in caso di thermal runaway; classificazione zona ATEX + procedure obbligatorie
- **Probabilità**: M (40-60%) per Phase B 6B con batterie ad alta densità
- **Mitigazione**: hangar dedicato con ventilazione anti-esplosione; procedure ATEX; formazione operatori; assicurazione adeguata
- **Falsifying observation**: se ASL / VVF in ispezione classificano hangar come "zona 1 ATEX" senza protezioni adeguate, sospensione attività

### 5.16.8 RoHS (Direttiva 2011/65/UE) — sostanze pericolose in componenti elettronici

- **Riferimento**: Direttiva 2011/65/UE (Restriction of Hazardous Substances) + Direttiva 2017/2102 (Aggiornamento RoHS 3)
- **Impatto progetto**: componenti elettronici importati (incluse alcune avioniche cinesi JOUAV) **devono essere RoHS-compliant** per uso commerciale UE; non solo aerospace exemption
- **Probabilità**: M (30-50%) — molti componenti commerciali sono già compliant
- **Mitigazione**: verifica Declaration of Conformity (DoC) di ogni componente in BoM; audit RoHS pre-deployment
- **Falsifying observation**: se componente critico non-RoHS, sostituzione obbligatoria con impatto CapEx + schedule

### 5.16.9 Codice della Navigazione (R.D. 327/1942) + diritti di sorvolo

- **Riferimento**: Codice Navigazione art. 793 (sorvolo bassa quota), art. 794 (sorvolo aree militari/sensibili); D.Lgs. 96/2005
- **Impatto progetto**: voli BVLOS a bassa quota (≤ 500 m AGL) su proprietà private possono richiedere **autorizzazione proprietari** o concessione amministrativa; aree militari sensibili (es. base Aronia, base militare interna) → divieto
- **Probabilità**: L-M (15-30%) per Pentema (area rurale, pochi proprietari)
- **Mitigazione**: mappa aree militari/sensibili Liguria; consenso proprietari grandi appezzamenti; NOTAM coordinato
- **Falsifying observation**: contestazione legale da proprietari → sospensione missioni in attesa di accordo

### 5.16.10 Affidamento PA — vincoli Codice Contratti art. 50 + art. 124

- **Riferimento**: D.Lgs. 36/2023 art. 50 (procedure ordinarie) + art. 124 (procedure semplificate) + art. 137 (affidamento diretto)
- **Impatto progetto**: contratti PA con Firmamento possono richiedere **gara pubblica** se importo > soglie (€140k per servizi, salvo deroghe); affidamento diretto solo sotto soglia o per urgenza documentata
- **Probabilità**: H (70-85%) per contratti pluriennali Regione
- **Mitigazione**: pre-engagement Regione + accordo quadro (art. 59 D.Lgs.36); partnership Coopfond come veicolo non-gara (su determinati ambiti); accordi di programma SNAI
- **Falsifying observation**: contratto pluriennale €300k con Regione bocciato in fase amministrativa per mancanza di gara → rinvio M+6-12

### 5.16.11 Insurance BVLOS — Reg. UE 285/2004 + DM 25/02/2022

- **Riferimento**: Reg. (UE) 285/2004 (assicurazione obbligatoria operatori aerei) + DM Trasporti 25/02/2022 (massimali UAS)
- **Impatto progetto**: massimale assicurativo minimo per UAS BVLOS in Specific Category SAIL III ≈ **750.000 DSP (~€900k)**; per Certified Category ≥ €1.5M; premio annuo €15-50k stimato
- **Probabilità**: H (impatto OpEx)
- **Mitigazione**: tender assicurativo con broker specializzato aviation (Marsh, Aon, Willis Italia); copertura RC + casco + cyber + privacy
- **Falsifying observation**: se nessun assicuratore aviation offre copertura BVLOS Pentema a costi sostenibili (>€100k/anno), modello operativo finanziariamente non sostenibile

### 5.16.12 NIS2 operativo — D.Lgs. 138/2024 — termine registrazione gennaio 2025

- **Riferimento**: già citato in §5.7.1; aggiunta operativa: **termine registrazione presso ACN** era gennaio 2025
- **Impatto progetto**: Firmamento appena classificata "soggetto importante / essenziale" deve registrarsi entro 30 giorni dalla qualifica; sanzioni amministrative fino €10M / 2% fatturato
- **Probabilità**: H (75%) appena operativa
- **Mitigazione**: registrazione preventiva ACN + ISMS Part-IS (vedi §5.16.4)
- **Falsifying observation**: omessa registrazione + incidente cyber = sanzione + reputazione

### 5.16.13 Galileo PRS (Public Regulated Service) — se uso GNSS sicuro

- **Riferimento**: Decisione (UE) 2011/740 + Decreto MEF 6/12/2021 (organizzazione PRS Italia)
- **Impatto progetto**: per HAPS in operazioni dual-use civile-difesa (out-of-scope Studio attuale ma su tavolo Phase B 6B), accesso a **Galileo PRS** (signal anti-spoofing crittografato) richiede autorizzazione **CASD / Difesa**
- **Probabilità**: L (5-15%) Y1; M (30-45%) Phase B 6B se dual-use
- **Mitigazione**: per Y1 utilizzare GNSS standard L1/L5 + Galileo open service + anti-spoofing software-based; engagement CASD solo se dual-use Fase 3+

### 5.16.14 Direttiva Macchine (Reg. UE 2023/1230) — UAS come prodotto industriale

- **Riferimento**: Reg. (UE) 2023/1230 (Machinery Regulation, sostituisce Dir. 2006/42/CE; applicazione 20 gennaio 2027)
- **Impatto progetto**: ground equipment + GS + carrelli movimentazione UAS = "macchine" → marcatura CE Direttiva Macchine + Declaration of Conformity
- **Probabilità**: H (60-75%) per Phase B 6B con ground equipment custom
- **Mitigazione**: design CE-compliant fin dalla fase concept; collaborazione con ente notificato

### 5.16.15 ENAV operational coordination FL400+ — procedure dedicate

- **Riferimento**: Reg. UE 2017/373 (ATM/ANS) + ENAV procedure pubblicate AIP Italy
- **Impatto progetto**: HALE perennial sopra **FL400** (12 km) e specialmente FL650 (20 km) richiede **procedure ENAV ad hoc** per ascesa/discesa attraverso spazio aereo controllato; NOTAM dedicato + slot temporali
- **Probabilità**: H (70-85%) per Phase B 6B
- **Mitigazione**: engagement ENAV precoce (Y2); contributo a definizione procedure standard EUROCONTROL; testing in spazio aereo segregato (es. Sardinia, Apulia GATB)
- **Falsifying observation**: se ENAV declina procedure dedicate per HAPS perennial entro Y4, operatività italiana 6B bloccata

### 5.16.16 Tabella sintesi 15 showstopper aggiuntivi

| ID | Showstopper | Probabilità | Impatto | Score | Fase | Mitigation owner |
|---|---|---|---|---|---|---|
| RSK-REG-016 | AI Act sistemi biometrici onboard | M (40-55%) | M-H | 10-13 | Y1+ | data-privacy-counsel |
| RSK-REG-017 | EUSPA accreditation downstream | M (30-45%) | M | 6-9 | Y3+ | sovereign-strategist |
| RSK-REG-018 | EUROCONTROL HAPS coordination | H (65-80%) | H | 15-20 | Y3+ | avionics-gnc-engineer |
| RSK-REG-019 | Part-IS EASA Information Security | H (75-85%) | H | 15-20 | Y0+ (urgente) | aviation-regulatory + CISO new |
| RSK-REG-020 | Penale 432-bis (incidente BVLOS) | L-M (10-25%) | H | 6-15 | Y1+ | aviation-regulatory + ops |
| RSK-REG-021 | AgID/PSN hosting dati PA | H (70-85%) | M-H | 12-17 | Y1+ | data-privacy + IT |
| RSK-REG-022 | ATEX batterie | M (40-60%) | M | 8-12 | Y0+ | propulsion-engineer + safety |
| RSK-REG-023 | RoHS componenti | M (30-50%) | L-M | 4-8 | Y1 | systems-engineer |
| RSK-REG-024 | Codice Navigazione sorvolo proprietà | L-M (15-30%) | M | 3-9 | Y1+ | regulatory + community |
| RSK-REG-025 | Affidamento PA art. 50 D.Lgs.36 | H (70-85%) | M-H | 12-17 | Y0+ | snai-funding + legal |
| RSK-REG-026 | Insurance BVLOS sostenibilità | H | M | 12 | Y0+ | financial-cfo |
| RSK-REG-027 | NIS2 registrazione operativa | H (75%) | M-H | 12-17 | Y0+ (immediato) | CISO new |
| RSK-REG-028 | Galileo PRS dual-use | L (5-15%) Y1, M (30-45%) Y3+ | M | 3-9 | Y3+ | sovereign-strategist + CASD |
| RSK-REG-029 | Direttiva Macchine UAS+GS | H (60-75%) | M | 9-12 | Y3+ | systems-engineer |
| RSK-REG-030 | ENAV procedure FL400+ | H (70-85%) | H | 15-20 | Y3+ | avionics + sovereign-strategist |

**Impatto aggregato**: 15 nuovi RSK-REG-XXX da aggiungere al Risk Register. **5 con score H (15-20)** = showstopper effettivi: Part-IS, EUROCONTROL, AgID/PSN, Affidamento PA art.50, ENAV FL400+.

**Implicazione operativa per il verdetto Cap. 10**: il verdetto "Go Condizionato 6A" presupponeva l'assenza di showstopper regolatori aggiuntivi. Con questi 15 aggiunti, il verdetto realistico è **"Hold con piano regolatorio rafforzato"** come scenario base (vedi Cap. 10 §10.3.2 caveat probabilistico aggiornato).

---

## 5.16bis Update IRIS² Architecture (post DR-009 closure M+3)

> **Finding DR-009 (`riferimenti/DR-research-closure-M3.md`)**: la verifica con fonti primarie (SpaceRISE concession contract press release, Commissione UE Reg. UE 2023/588) ha confermato che **IRIS² è architettura LEO + MEO puro, SENZA layer stratosferico**. Primo lancio target 2029, operatività piena 2031, governato da SpaceRISE (Airbus + Eutelsat + Thales-Telespazio + Hispasat + OHB + Deutsche Telekom + Orange).

**Implicazione per il posizionamento "complementare a IRIS²"** (boundary B2 + Cap. 5.0bis + Cap. 7.0bis + Cap. 11):
- Il posizionamento "stratospheric layer complementary to IRIS²" è **aspirazione strategica Y4-Y7**, non baseline acquisita
- La complementarità è **opportunità di posizionamento gap-filler**, non integrazione tecnica predefinita
- Lo slittamento IRIS² (lancio 2029, ops 2031) **dà tempo a Firmamento** per posizionarsi nella narrativa "EU sovereign multi-orbit + stratospheric"
- **Action**: position paper "Italian Stratospheric Layer Complementary to IRIS² Multi-Orbit" (engagement DG CNECT + SpaceRISE) entro Y2 per validare il framing

**Falsifying observation §5.16bis**: se entro Y3 la Commissione UE o SpaceRISE pubblicano documenti ufficiali che escludono esplicitamente layer stratosferici dall'architettura sovrana EU multi-orbit, il posizionamento "complementare IRIS²" è falsificato. Trigger scenario B2-relaxed (Cap. 11 §11.6bis).

---

## 5.17 Aggiornamento Engagement Plan (post 15 showstopper)

L'engagement plan §5.11.3 va esteso con:

| Autorità aggiuntiva | Trigger | Frequenza | Owner |
|---|---|---|---|
| **AgID** (Agenzia per l'Italia Digitale) | Hosting dati PA cloud PSN-qualified | Annuale | data-privacy + IT |
| **AGID + Garante** insieme | AI Act sistemi biometrici | Annuale | data-privacy + sovereign |
| **EUROCONTROL** Network Manager | HAPS coordination procedures EU | Semestrale | avionics-gnc |
| **EUSPA** Bruxelles | Downstream services accreditation | Annuale | sovereign-strategist |
| **CASD / Difesa** | Galileo PRS dual-use (Phase B+) | Annuale (Y3+) | sovereign-strategist |
| **ASL / VVF** locale Liguria | ATEX hangar + safety operativa | Annuale | safety + ops |
| **Ente certificazione Direttiva Macchine** (TÜV, IMQ, Bureau Veritas) | CE marking GS + carrelli | Una tantum Y2-Y3 | systems-engineer |
| **Broker assicurativi aviation** (Marsh, Aon, Willis) | RC + casco + cyber BVLOS | Annuale | financial-cfo |

**Risorse FTE addizionali necessarie**:
- **CISO** (Chief Information Security Officer) — full-time per Part-IS + NIS2 + cyber audit
- **DPO** (Data Protection Officer) — part-time/full-time per GDPR + AgID + AI Act
- **Head of Regulatory Affairs** — full-time per coordinamento autorità multiple

Costo aggregato stimato Y1: **+€450-800k OpEx** (3 FTE qualificati). **Non incluso** nei budget Cap. 8 originali → da aggiungere come fixed cost obbligatorio per Y1.

---

## 5.15 Note di chiusura del capitolo

Il presente capitolo è una **bozza M+3 + aggiornamento post-audit M+3** redatta sulla base delle fonti normative autoritative aggiornate al settembre 2025 (EASA ED Decision 2025/018/R), estesa con 15 showstopper regolatori aggiuntivi identificati dall'audit `regulatory-adversary`. Le fonti scaricate coprono i regolamenti UE e italiani principali necessari per la base regolatoria del progetto.

**Debito di rigore residuo per il Cap. 5** (vedi `riferimenti/audit-rigore-epistemico.md`):
- ☐ DR-004 — ENAC SAIL stima per Pentema (pre-application meeting)
- ☐ DR-005 — AGCOM spettro HAPS Italia (consultazione AGCOM)
- ☐ DR-006 — Garante Privacy posizione su sorveglianza HAPS (analisi precedenti dedicata)

Questi item richiedono **engagement esterno** (non più solo desk research) e vanno chiusi nei primi 6 mesi di operatività del progetto, prima del gate M+10.

**Prossima revisione**: M+6 post pre-application meeting ENAC (gate M+6 architettura baselined).
