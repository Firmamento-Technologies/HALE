# Audit Regulatory Adversary — Volume 1

> **Agente:** `regulatory-adversary` (impersona ENAC / EASA / AGCOM / Garante / ENAV / MIMIT / DG CNECT/DEFIS / Presidenza Consiglio Golden Power)
> **Target:** Volume 1 Studio di Fattibilità — capitoli 4, 5, 6, 9, 10
> **Versione:** M+3 (bozza), audit prodotto autonomamente in 30 min
> **Postura:** "ecco esattamente come ti blocchiamo" — niente "se", niente offerte di soluzione consulenziale, solo critica
> **Boundary rispettate:** B1 (cooperative + service-only) e B2 (visione EU sovereign) NON attaccate. Attaccato esclusivamente il *path* regolatorio

---

## 0. Verdetto sintetico

> **Il path regolatorio Firmamento NON regge nella formulazione attuale del Cap. 5.** Regge solo se il Cap. 5 viene riscritto con (a) presa d'atto realistica della **lentezza strutturale ENAC SAIL per BVLOS senza track record**, (b) **deconflittazione esplicita ENAV-ENAC-EASA-AGCOM-Garante** con owner contrattualmente vincolato, (c) **piano di contingency** per ogni "stuck path", (d) **3 risorse FTE dedicate al regulatorio** (oggi sono 0.5-1). Senza queste riscritture: P(blocco operativo M+12-M+18 su 6A) ≈ 35-45%; P(stalling permanente 6B fino a 2030+) ≈ 75%.
>
> **Verdetto operativo**: il **Go Condizionato 6A del Cap. 10 NON regge nei scenari peggiori** (vedi §8). Il **Hold 6B del Cap. 10 è formalmente corretto ma sotto-stima la profondità del blocco** (Special Condition HAPS è un *placebo strategico*, non un percorso reale).

---

## 1. Regulatory Threat Matrix

Dodici scenari di blocco, ognuno con riferimento normativo che lo renderebbe legittimo.

| ID | Scenario | Autorità | Riferimento normativo / precedente | Probabilità | Tempistica | Effetto progetto |
|---|---|---|---|---|---|---|
| **RA-01** | GRC Pentema riclassificato 6+ → SAIL IV-V → operatore senza track record non eleggibile | ENAC Direzione Regolamentazione UAS | AMC1 Art. 11 Reg. UE 2019/947 + SORA 2.5 EU Annex E (densità popolazione "sparse populated" vs "populated") | **H** (60-70%) | M+3-M+9 | Pilota Pentema **non parte in BVLOS Y1**; modello operativo collassa o ridotto a VLOS+EVLOS |
| **RA-02** | Richieste integrazioni successive su SORA application | ENAC | Reg. UE 2019/947 art. 12.5; prassi italiana (PA, art. 6 L. 241/1990) | **H** (75-85%) | M+6-M+18 | SORA approvazione slitta da M+9 atteso a M+15-M+24 reale |
| **RA-03** | AGCOM sospende licensing in attesa di WRC-27 (bande HAPS) | AGCOM Direzione Reti e Servizi | D.Lgs. 259/2003 art. 28, Codice Comunicazioni Elettroniche + Risoluzione 122-bis WRC-23 (deferral worldwide) | **H** (70-80%) per banda HAPS dedicata; **M** (40%) per bande commerciali con accordo operatore | M+12-M+48 | Payload telecom commerciale stratosferico **inutilizzabile in IT** fino al 2028-2030; 6A può usare ISM o accordi MVNO |
| **RA-04** | Garante apre procedimento ex art. 58.2 GDPR su segnalazione abitanti Pentema | Garante per la Protezione dei Dati Personali | GDPR art. 35 (DPIA) + 58.2.f (limitazione provvisoria); Provv. Garante n. 9/2019 droni; AI Act art. 5 (sorveglianza biometrica indiscriminata) per IR a bordo | **M-H** (40-55%) — Pentema piccolo ma media interesse mediatico alta | M+3-M+12 | Sospensione missioni EO + ridisegno hardware (blur on-board mandatorio) + DPIA pubblica anche se non era prevista |
| **RA-05** | ENAV declina coordinamento operativo HAPS sopra FL195 | ENAV S.p.A. + ENAC Direzione Spazio Aereo | Reg. UE 923/2012 (SERA) + Reg. UE 2017/373 (ATM/ANS) + ENAC Reg. APR Ed.3 art. 24-25 | **M-H** (55-70%) per HAPS perennial | M+24+ | 6B operativo impossibile in spazio aereo italiano; obbligo deportare operazioni fuori FIR italiano |
| **RA-06** | EASA dichiara non-procedibile la pre-application Special Condition HAPS perché TRL insufficiente | EASA UAS Department / Innovation Network | Reg. UE 2018/1139 art. 11; CRD/NPA process EASA (richiede dimostratore + safety case maturo) | **H** (75-85%) prima di TRL 5 dimostrato | M+12-M+36 | Pre-application archiviata; ripresentazione M+36-M+48 con perdita 2-3 anni |
| **RA-07** | Trasferimento competenza ENAC↔EASA↔ENAV (ping-pong) sulla certificabilità HALE | ENAC + EASA + ENAV | Reg. UE 2018/1139 (riparto competenze EASA/Stati Membri) + Memorandum Cooperation EASA-ENAC | **H** (80%) per qualunque richiesta non-standard | M+6-M+24 | Tempi raddoppiati su ogni domanda; nessun owner istituzionale chiaro per HAPS civile |
| **RA-08** | NIS2 designa Firmamento "soggetto essenziale" (operatore servizi essenziali aerei + infrastrutture digitali) | ACN — Agenzia Cybersicurezza Nazionale + MIMIT | D.Lgs. 138/2024 (recepimento NIS2) art. 3 e Allegato I (settori trasporti aerei + infrastrutture digitali); termine registrazione gennaio 2025 | **H** (70%) appena diventa operativa | M+9-M+18 | Obblighi gestione del rischio art. 24 + notifica incidenti 24h + sanzioni fino €10M / 2% fatturato; **NON c'è un CISO né SOC oggi** |
| **RA-09** | Golden Power notifica obbligatoria a primo round investimento esterno | Presidenza del Consiglio (DAGL + COPASIR ascolto) | D.L. 21/2012 art. 1-2 + DPCM 18 dicembre 2020 (estensione perimetro tecnologie strategiche + aerospace duale); precedente: golden power su Avio Spa 2022 | **L** (10-15%) early stage; **M-H** (45-60%) Series A+ se cap table include UK/USA/altri non-EU | M+12-M+36 | Notifica obbligatoria entro 10gg + sospensione 45gg + possibile veto/prescrizioni; effetti chilling su raccolta capitali |
| **RA-10** | MIMIT subordina finanziamenti aerospace al coordinamento con Leonardo/TAS/Telespazio | MIMIT Direzione Aerospazio + Dipartimento Politiche Spaziali | Strategia Nazionale Spazio 2023 + Piano Spaziale Nazionale; precedente Mirror Copernicus consortium-mandate | **M-H** (50-65%) per importi > €2M | M+12-M+24 | Phase B 6B subordinata a sub-contracting Tier1; Firmamento perde leadership IP HAPS |
| **RA-11** | DG CNECT/DEFIS chiude accesso fondi EDF/Horizon a operatori HAPS indipendenti per coerenza con IRIS²/EuroHAPS | Commissione UE — DG CNECT + DG DEFIS | Reg. UE 2023/588 IRIS² + EDF work programmes 2025-2027 (priorità consortium-led); precedente: PIVOTAL exclusion non-consortium bidders | **M** (35-50%) | M+18-M+36 | Funding Phase B 6B inaccessibile in autonomia, obbligo entrata in consorzio (CIRA/TAS) come *junior partner* |
| **RA-12** | ENAC sospende il procedimento SORA in attesa del nuovo Regolamento U-Space Italia (consultazione gennaio-aprile 2026) | ENAC | Avviso ENAC 14 gennaio 2026 (consultazione pubblica Reg. U-Space Ed.1); art. 7 L. 241/1990 (comunicazione avvio + sospensione) | **M** (30-45%) | M+3-M+12 | Pre-application rinviata fino a chiusura consultazione + adozione regolamento (Q3-Q4 2026 stima ottimistica) |

**Totale**: 12 scenari. **5 con probabilità H** (≥ 60%), **5 M-H** (35-65%), **2 L-M**. La distribuzione conferma che **almeno 3-4 scenari si verificheranno simultaneamente** nel primo anno operativo.

---

## 2. Worst-case timeline regolatoria

Se andasse male — non catastrofe, solo **prassi italiana normale** + lobbying incumbent + sovraccarico autorità:

```
M+3      M+6      M+9      M+12     M+18     M+24     M+36     M+48
│        │        │        │        │        │        │        │
│ Pre-app│ Stop   │ Risp.   │ SORA   │ Ric.    │ Auth   │ DPIA   │ ENAV
│ ENAC   │ U-Sp   │ ENAC:  │ subm   │ integr.│ Spec.  │ chiusa │ NoGo
│ rinvi- │ consul-│ "SAIL  │ ritard.│ #1+#2  │ SAIL II│ rivisi-│ HAPS
│ ata    │ taz.   │ V → no"│ M+15   │ ENAC   │ VLOS+  │ ta hw  │ FL400
│        │        │        │        │        │ EVLOS  │ +eng   │ +
│        │        │        │        │        │ subset │ retr.  │ Spec.
│        │        │        │        │        │ ridot- │        │ Cond.
│        │        │        │        │        │ to     │        │ EASA
│        │        │        │        │        │        │        │ rige-
│        │        │        │        │        │        │        │ ttata
│        │        │        │        │        │        │        │ (TRL)
```

**Slippage atteso** rispetto al Cap. 9 (cronoprogramma):

| Milestone (Cap. 9) | Pianificato | Worst-case realistico | Delta |
|---|---|---|---|
| Pre-app ENAC con feedback documentato | M+3 | M+6-M+9 | +3/+6 mesi |
| Submission SORA | M+6 | M+12-M+15 | +6/+9 mesi |
| Autorizzazione ENAC | M+9 | M+18-M+24 | +9/+15 mesi |
| Prima missione operativa Pentema | M+10 | M+22-M+30 (con scope ridotto a EVLOS) | +12/+20 mesi |
| Licenza spettro AGCOM (commercial) | M+12 (implicito) | M+30-M+48 o WRC-27+ | +18 mesi → indefinito |
| DPIA chiusa | M+12 | M+18-M+30 | +6/+18 mesi |
| EASA Special Condition HAPS aperto | M+24 | M+48-M+72 o mai prima TRL 5 dimostrato | +24/+48 mesi |
| Phase B 6B autorizzata | M+24-M+48 | M+48-M+72 con scope decimato | +24+ mesi |

**Conclusione**: la timeline ottimistica del Cap. 9 ha **margine zero** per scenari regolatori realistici. Il Gate G3 (M+10/M+11) si terrà **prima** che ENAC abbia anche solo dato il feedback definitivo sul SAIL. È un gate che decide **senza l'informazione regolatoria critica**.

---

## 3. Critical path regolatorio

Per ogni fase del business plan, autorizzazioni **prerequisite assolute** (senza le quali non si fa nulla) vs **nice-to-have** (utili ma non bloccanti).

### Fase 1 — Pilota VTOL Pentema (M+12 → M+24)

| Autorizzazione | Tipologia | Owner | Stato M+3 | Note adverse |
|---|---|---|---|---|
| ENAC SORA Specific Authorization SAIL II-III | **PREREQUISITO ASSOLUTO** | ENAC DRA UAS | Non avviata formalmente | Senza questa: **niente volo BVLOS, niente missione, niente revenue Y1**. Il PFTE non lo dice ma è il *single point of failure* operativo |
| Operator Registration ENAC (art. 14 Reg. UE 2019/947) | PREREQUISITO ASSOLUTO | ENAC | Non avviata | 4-8 settimane (forma); il problema non è il rilascio ma le precondizioni QMS |
| Polizza assicurativa BVLOS (Reg. CE 785/2004 livelli) | PREREQUISITO ASSOLUTO | Mercato assicurativo | Non scoutato seriamente | BVLOS premia ×3-5 vs VLOS; alcuni assicuratori italiani **non sottoscrivono BVLOS** senza track record |
| Attestato pilota UAS BVLOS (ENAC, art. 22 Reg. APR) | PREREQUISITO ASSOLUTO | ENAC + Centro Addestramento riconosciuto | Non avviato | 3-6 mesi reali |
| Approvazione SOC/QMS AS/EN 9100 (per credibilità SORA SAIL III) | "Nice to have" formalmente ma **de facto prerequisito** per SAIL III | Ente certificatore (RINA, DNV) | Solo "roadmap" dichiarata | Senza 9100 ENAC dirà "torna quando hai il QMS" |
| DPIA accettata implicitamente dal Garante (no reclami) | PREREQUISITO PRATICO (anche se non formalmente "autorizzazione") | DPO + Garante (silenzio assenso) | Solo "DPIA preliminare entro M+6" | Garante può intervenire ex post |
| Licenza AGCOM se banda licenziata; **comunicazione coexistence** se ISM | Prereq. se banda licenziata; nice-to-have se ISM | AGCOM | Non avviata | ISM 2.4 GHz: rischio interferenza WiFi locale |
| Autorizzazione MIT/Comune per area decollo/atterraggio + NOTAM | Prereq. operativo | Comune Torriglia + ENAC NOTAM Office | Non avviata | Comune piccolo, no esperienza UAS; richiede ordinanza sindacale |
| Conformità NIS2 (se classificato essenziale) | Prereq. legale se classificato | ACN | Non in Cap. 5 in modo operativo | Sanzioni amministrative se non registrato; **rischio reputazionale per bandi pubblici** |

### Fase 2 — Scale-up multi-regione SNAI (M+24 → M+36)

| Autorizzazione | Tipologia | Note adverse |
|---|---|---|
| SORA authorization replicata per ogni regione/area | PREREQUISITO per ogni nuovo sito | Ogni regione = nuovo procedimento ENAC (no "fast track" per multi-site, oggi) |
| Eventuale istituzione U-Space su area servita | "Nice to have" | Richiede iniziativa Regione + ARA + procedura LG-2023/006; tempi 12-24 mesi |
| Coordinamento D-Flight (USSP+CISP) | PREREQUISITO se U-Space attivo | Costi €5-20k/anno + dipendenza da soggetto privato con monopolio de facto |
| Licenza AGCOM per banda commerciale (se payload TLC) | PREREQUISITO operativo | Cf. RA-03 |

### Fase 3 — HALE Phase B (M+24 → M+48)

| Autorizzazione | Tipologia | Note adverse |
|---|---|---|
| EASA Special Condition HAPS aperta formalmente | **PREREQUISITO ASSOLUTO** | RA-06: probabilità apertura entro M+36 è bassa (15-25%) |
| EASA / ENAC autorizzazione **flight test stratosferico subscale** | PREREQUISITO ASSOLUTO | Per testare a FL400+ servono procedure ENAV dedicate + NOTAM + coord. FIR + autorizzazione MIT, oggi inesistenti |
| Allocazione spettro HAPS dedicata (6.4-6.7 / 31 / 47 GHz) | PREREQUISITO commerciale | RA-03: WRC-27 + 2 anni di licensing AGCOM = realistica solo da 2029-2030 |
| ENAV coordination per FL195+ traffic separation | PREREQUISITO operativo | RA-05: nessun framework, ENAV non ha incentivo |
| MIMIT/COPASIR clearance se considerato strategico | Possibile prereq. (Golden Power) | RA-09 |

**Verdetto sul critical path**: il Cap. 5 trattatutte queste autorizzazioni come **gestibili in parallelo**. In realtà sono **sequenziali con dipendenze hard** (es. SORA dipende da QMS dipende da pilot certified dipende da attestato dipende da Operations Manual che dipende dalla risposta ENAC sul SAIL). Una catena di **6-8 dipendenze hard** con tempi medi 60-180 giorni cad. = **18-36 mesi reali** vs **9 mesi pianificati**.

---

## 4. Critiche puntuali al Cap. 5

### Critica 1 — La stima SAIL II-III su Pentema è ottimistica oltre il difendibile

Il §5.1.5 dichiara iGRC 4-5 e final GRC 2-3 con M1+M2, SAIL II o III, confidence "low-medium". Verità ENAC:

- **Pentema NON è "popolazione sparse" omogenea**. È frazione abitata (~70-100 ab. residenti, ma fluttuanti weekend/estate) **dentro un Comune (Torriglia)** con borghi vicini (Bavastri, Pentema centro, frazioni dipendenti). Il SORA 2.5 Annex E (densità) calcola **iGRC su rettangolo operazionale**, non su singola frazione. Se il rettangolo include zone densità "controlled environment" (es. SP226 statale, sentieri Alta Via, rifugio Antola), la densità composita sale.
- **Mitigation M2 (parachute) è discutibile** per VTOL pesante (~38 kg) in orografia montana: il SORA 2.5 richiede dimostrazione di efficacia del paracadute in condizioni di terreno irregolare. Possibile reiezione M2.
- **Mitigation M1 (geofencing strict + restricted area)** richiede NOTAM permanente + accordo Comune + esclusione operazioni in finestre weekend/festivi. Lo Studio non lo prevede.
- **Base rate**: nessun operatore italiano di scala PMI ha ottenuto SAIL III BVLOS perennial per area montana abitata. Gli esempi (Aeronike, NUVAP, Aero International, Aermatica3D) sono **tutti SAIL II EVLOS o SAIL III con scope limitato** (corridoi industriali, no zone abitate).

**Risultato realistico**: ENAC chiederà di **dimostrare** la classificazione "sparse" con rilievo demografico ufficiale (ISTAT + Regione), o **dichiarerà GRC 6** con SAIL IV-V. SAIL IV richiede 24 OSO + audit indipendente + maturity Level "Enhanced" su 16 OSO. **Costi reali**: €150-250k (non €30-80k) + tempi 18-24 mesi.

**Cap. 5 da rivedere**: confidence stima da "low-medium" → "low". Aggiungere scenario SAIL IV come *base case*, non come falsifying observation marginal.

### Critica 2 — Il Cap. 5 tratta Special Condition HAPS come opzione "negoziabile". Non lo è (oggi).

Il §5.4.2 e §5.10.1 dichiarano "Special Condition negoziata caso per caso" + "Type Cert primo HAPS commerciale civile EU: 2032-2035". È **letteralmente la prassi EASA**, ma il Cap. 5 omette tre realtà:

1. **EASA non apre Special Condition su iniziativa applicant**. L'applicant può chiedere un *pre-application meeting* e ricevere "no priority assigned" sine die. EASA apre SC solo quando ha **mandato Commission UE o richiesta di un EU Member State** con safety case parziale. Esempio: SC-VTOL aperto dopo richiesta Volocopter + EU AAM strategy + Germania come sponsor. Firmamento da sola **non muoverà EASA**.
2. **"Negoziata caso per caso" significa**: 2-5 anni di dialogo + nessun commitment EASA. Vedi tempistiche Lilium SC-VTOL (~4 anni 2019-2023) e ancora non chiuso. Per HAPS la base è **zero precedenti**.
3. **PHASA-35 e Zephyr operano fuori framework Certified civile**: PHASA-35 BAE è **R&D experimental category UK CAA** + cliente DoD/MoD; Zephyr AALTO opera in **TC-UK + cliente Government**. Il Cap. 5 li cita come "fattibilità" ma **nessuno** ha ottenuto Type Certificate civile EASA. Esempio mancante: Solara/Titan Aerospace abbandonati, NASA Helios crashato, Aalto HAWK30 cancellato 2021.

**Risultato realistico**: la roadmap Cap. 5 + Cap. 11 verso operatività Y6-Y8 6B è **fantasia regolatoria**. La probabilità di Type Cert EU civile HAPS entro 2032 è ≤ 10%.

**Cap. 5 da rivedere**: §5.4.2 dichiarare apertamente "no chiari precedenti EASA per HAPS civile; possibile fallback su UK CAA experimental o Government client only; commerciale civile EU non realistico < 2035".

### Critica 3 — AGCOM: il Cap. 5 sottostima drasticamente la difficoltà del licensing

Il §5.5.2 stima 12-36 mesi per licensing banda HAPS dedicata. Verità AGCOM:

- **Le bande HAPS ITU non sono nel PNRF italiano operativo**. Sono "annotate" ma non c'è **procedura di domanda standard** né tariffa pubblicata. Una domanda Firmamento sarebbe **prima domanda mai presentata** → AGCOM apre **consultazione pubblica** (Reg. AGCOM organizzazione + funzionamento) → 6-12 mesi solo per la consultazione, prima di entrare nel merito.
- **Lobby telco**: TIM, Vodafone, Iliad, WindTre, Fastweb hanno interessi forti sullo spettro 700 MHz / 1.8 GHz / 2.6 GHz / 3.6 GHz. La banda 38-39.5 GHz (HAPS service link extended WRC-23) è **co-allocata FSS** (Inmarsat, Eutelsat) → interferenze richiedono **coordinamento commerciale** preventivo.
- **MIMIT (PNRF)** non aggiorna il piano senza pressione politica. Esempio: bande millimetriche 26/28 GHz hanno richiesto 4 anni di consultazione MIMIT-AGCOM (2018-2022) per essere assegnate al 5G mmWave.
- **Coordinamento internazionale ITU** (vicini: Francia, Svizzera, Slovenia, Croazia, Tunisia, Algeria) è **anni di procedimento** per bande non-standard.

**Risultato realistico**: licensing operativo banda HAPS in Italia = **5-10 anni**. Per Y1 6A serve fallback **inevitabile** su banda ISM (2.4 / 5.8 GHz) o **accordo MVNO** con operatore mobile esistente per il payload. Il Cap. 5 lo accenna solo nel C2 link 6A, non per il payload commerciale.

**Cap. 5 da rivedere**: §5.5.2 dichiarare "licensing banda HAPS dedicata = orizzonte 2030-2032 realistico; per Y1-Y3 servizi telecom 6A solo via accordi MVNO con operatori autorizzati esistenti, con margine commerciale ridotto".

### Critica 4 — Garante Privacy: probabilità sospensione missioni EO sottostimata

Il §5.6.2 dichiara probabilità "L-M" (basso-medio) per sospensione missioni EO da parte del Garante. La verità è:

- **Pentema è caso mediatico potenziale**: la "frazione abbandonata che vive grazie al drone" è esattamente lo storytelling che attrae attenzione mediatica, e con l'attenzione vengono **reclami strumentali** (vicini, gruppi ambientalisti, comitato territoriale anti-droni — il "no drone here" è movimento già attivo in Liguria, vedi caso Genova centro 2023).
- **Precedenti Garante restrittivi**: Provv. 1° febbraio 2024 contro Trenitalia (telecamere stazione); Provv. 9 marzo 2023 contro Comune Trento (riconoscimento facciale); Provv. n. 9/2019 su droni "Memory" Roma. Il Garante **ha precedenti forti** su sorveglianza area persistente.
- **AI Act art. 5** (operativo agosto 2026 — coincide con M+3 Firmamento!) vieta "sistemi di categorizzazione biometrica" e limita pesantemente "riconoscimento facciale in spazi pubblici". Il payload IR + EO ad alta risoluzione **può cadere in queste fattispecie** se la post-processing include rilevazione persone.
- **DPIA pubblica** (Cap. 5 dichiara M+6) è documento **complesso 50-80 pp**: richiede DPO certificato + analisi rischi + consultazione interessati. Non è un PDF di 20 pp.
- **Procedimento Garante art. 58 GDPR** può essere avviato d'ufficio senza reclami se il Garante "viene a sapere" di sorveglianza persistente (notizie stampa, dichiarazioni Firmamento sui media). Tempi: 30-90 gg per provvedimento d'urgenza, 6-12 mesi per istruttoria piena.

**Risultato realistico**: probabilità sospensione missioni EO Y1-Y2 = **35-50%**, non "L-M". Mitigation richiede **hardware-level blur** (non solo software), **policy consenso esplicito** (non interesse legittimo né interesse pubblico per casi non-emergenza), **architettura zero-knowledge** (Firmamento non vede mai immagini raw, solo prodotti derivati anonimizzati).

**Cap. 5 da rivedere**: §5.6.2 alzare probabilità a M-H; aggiungere AI Act compliance esplicita (oggi mancante); mandare DPIA pubblica a M+3 (non M+6) come prerequisito per qualunque engagement con comunità.

### Critica 5 — NIS2: Cap. 5 ha una "compliance" non operativa

Il §5.7.1 cita NIS2 (D.Lgs. 138/2024) ma:

- **Non dichiara se Firmamento è classificata "essenziale" o "importante"**. È determinante: settori essenziali hanno obblighi 3× più stringenti.
- **Non c'è CISO** nel team Firmamento dichiarato in Cap. 9. Per NIS2 art. 24 serve nominato + risk management + ISO/IEC 27001 (PFTE Cap. 5.8 lo cita solo come "applicabile", non implementato).
- **Termine registrazione ACN** era 28 febbraio 2025 (passato). Se Firmamento è classificata e non registrata, **sanzione amministrativa già attiva** + esclusione bandi pubblici (DL Cyber 2024).
- **Notifica incidenti 24h** richiede SOC h24 o contratto con MSSP. Costo €60-150k/anno minimo. Non in CapEx.
- **Cybersecurity DO-326A/ED-202A** (Cap. 5.7.2) è citata ma operatori non OEM aviation non implementano DO-326A; serve solo se Firmamento sviluppa avionica certificata (non scenario 6A con piattaforma JOUAV COTS).

**Risultato realistico**: NIS2 è **showstopper potenziale per bandi pubblici** post-2025. Cap. 5 lo tratta come compliance generica, non come adempimento operativo.

**Cap. 5 da rivedere**: aggiungere sezione §5.7.3 con autovalutazione NIS2 essenziale/importante; piano registrazione ACN; budget cybersec annuale; nomina CISO; roadmap ISO 27001.

### Critica 6 — ENAV / FL400+ coordination: completamente assente per 6B

Il Cap. 5 menziona ENAV come stakeholder engagement (§5.11.3) ma:

- **HAPS perennial a FL400+ attraversa**: spazio C controllato (FL195-FL245), classe A FL245+ (transito civile/militare), zone temporanee Difesa. Ogni *ascesa e discesa* dura 6-12 ore in volo lento → conflitto continuativo con traffico CAT controllato (Linate, Genova, Nizza routing).
- **ENAV ha pubblicato 0 procedure** per HAPS perennial. Non c'è SID/STAR, non c'è MOC, non c'è OAT/GAT framework. Lo Studio non ha **alcun documento di engagement** con ENAV (Cap. 5.11.3 dichiara "Semestrale, U-Space + spazio aereo, owner avionics-gnc-engineer" — ma nessun documento prodotto né timeline).
- **ENAV è SpA con azionariato MEF**. Non ha incentivo commerciale a fare R&D regolatorio per un newcomer. Risorse umane sono assorbite da Single European Sky 2+, U-Space, AAM, Drone Strategy 2.0 EU.
- **Precedente Zephyr**: i flight test stratosferici Airbus Zephyr in Italia non si sono fatti — sono stati spostati in Arizona (Yuma) e Australia (Wyndham) **proprio per assenza framework EU FL400+**.

**Risultato realistico**: 6B perennial in spazio aereo italiano = **impossibile prima di 2030+**. Test campaign subscale a FL195+ richiede 12-24 mesi di engagement ENAV/ENAC/EUROCONTROL solo per ottenere procedure dedicate.

**Cap. 5 da rivedere**: §5.4.2 aggiungere "ENAV coordination = blocker assoluto per 6B; alternative: test campaign all'estero (UK, Spagna Canarie EuroHAPS, Australia) per fase prototype".

### Critica 7 — Cap. 5 ignora il Codice della Navigazione e i diritti di sorvolo

- **Codice della Navigazione art. 743-797**: disciplina la navigazione aerea italiana. UAS sono assimilati per estensione, ma diritti di sorvolo su proprietà private (art. 794 — *navigazione su fondi altrui*) richiedono notifica per sorvoli ripetitivi.
- **Diritto comunale**: il sindaco di Torriglia può emettere **ordinanza ex art. 50 TUEL** per sospendere sorvoli su area comunale se contesta motivi di ordine pubblico/sanità/sicurezza. Precedente: Comune di Anguillara Sabazia 2019, Comune di Capri 2022 (ordinanze "no fly" turistico-residenziali).
- **Pareri Soprintendenza**: Pentema è in **area vincolo paesaggistico** (D.Lgs. 42/2004 art. 142 — territori montani > 1200 m) e probabilmente vincolo architettonico (borgo storico). Sorvoli ripetitivi possono richiedere parere Soprintendenza (silenzio-rifiuto non si applica).
- **Servitù militari**: Liguria ha aree con servitù militare (poligoni La Spezia/Ameglia, zone NOTAM Difesa). Lo Studio non verifica la sovrapposizione.

**Cap. 5 da rivedere**: aggiungere §5.3.5 "Diritti di sorvolo + vincoli territoriali" con autorizzazioni sindacali, paesaggistiche, militari.

### Critica 8 — Golden Power: Cap. 5 lo rimuove al documento riservato. Non basta.

Il §5.13 critica 5 dice "Golden Power trattato in RESERVED, non nello Studio pubblico". Errore:

- Il Cap. 8 (economico-finanziario) parla di **funding mix con Series A+** e **partnership EU/internazionale**. Senza Golden Power assessment nel Cap. 5 pubblico, **il documento è incompleto** per investitori istituzionali che fanno due diligence.
- Lo Studio è per **bandi pubblici italiani** (Coopfond, PNRR, FESR Regione Liguria). I valutatori (RUP, CTS regionali, MIMIT) **chiederanno esplicitamente** posizionamento Golden Power per qualunque tecnologia aerospace duale.
- Aerospace + UAV + payload EO/TLC = **perimetro automatico DPCM 18 dicembre 2020** (D.L. 21/2012). Notifica preventiva è **obbligatoria** per cambi di controllo o operazioni straordinarie.

**Cap. 5 da rivedere**: aggiungere §5.10.4 "Golden Power assessment preliminare" con (a) qualificazione perimetro tech strategiche, (b) procedure notifica preventiva, (c) impatto su capital raise.

### Critica 9 — AI Act (Reg. UE 2024/1689): non citato

Il Cap. 5 cita "AI Act compliance (2024)" en passant ma:

- **AI Act art. 5** (operativo 2 agosto 2026) vieta sistemi *biometric categorization* e limita sorveglianza spazi pubblici.
- **AI Act Annex III** classifica come "alto rischio": sistemi di gestione infrastrutture critiche, gestione traffico, sicurezza pubblica. Il payload EO per Protezione Civile + monitoraggio infrastrutture cade in Annex III.
- **High-risk AI** richiede: risk management system, quality management, technical documentation, post-market monitoring, human oversight, conformity assessment con Notified Body. Costo compliance €100-300k iniziali + €30-60k/anno.
- **CE marking** per high-risk AI obbligatorio dal 2 agosto 2027 (Cap. 9 lo manca completamente).

**Cap. 5 da rivedere**: aggiungere §5.6.4 "AI Act compliance" come adempimento operativo, non solo "compliance generica".

### Critica 10 — Codice Contratti (D.Lgs. 36/2023): il "service" Firmamento non è bandibile facilmente

Il §5.9 mappa la conformità PFTE al D.Lgs. 36/2023. Ma:

- **Firmamento è "operatore servizi" per PA** (Boundary B1). Gli affidamenti dalla PA richiedono **procedura ad evidenza pubblica** (Codice Contratti + Linee Guida ANAC).
- Per affidamenti diretti < €140k (art. 50 D.Lgs. 36/2023) basta determina; per importi maggiori serve **gara**. La Regione Liguria non può dare €500k/anno a Firmamento senza gara.
- L'opzione **Accordo Quadro pluriennale** (art. 59) richiede gara iniziale + framework agreement; tempi 8-14 mesi.
- L'opzione **Convenzione operativa ex art. 15 L. 241/1990** (citata in Cap. 4 INT-19) è **utilizzabile solo tra PA**, non tra PA e operatore privato. Firmamento non è PA. → Cap. 4 INT-19 ha errore giuridico.
- L'opzione **Partenariato Pubblico-Privato** (art. 174 D.Lgs. 36/2023) richiede tempi 12-24 mesi.
- L'opzione **In-house providing** non è disponibile (Firmamento non è in-house Regione).

**Risultato realistico**: la Regione Liguria può firmare **LoI politica** ma per contratti reali deve fare **gara o procedura negoziata**, che apre il rischio competitor (es. Elsag/Leonardo, Telespazio) che vincono per scala/credibilità.

**Cap. 5 da rivedere**: aggiungere §5.9.3 "Vincoli affidamento PA" con analisi procedure applicabili e tempi reali.

### Critica 11 — Insurance: requisito Reg. CE 785/2004 ignorato operativamente

- Reg. CE 785/2004 obbliga ad assicurazione per operatori aerei UE. Per UAS BVLOS senza track record, **i sottoscrittori italiani sono pochi** (Generali, Allianz, Lloyd's via broker). Premi BVLOS: **€15-40k/anno per copertura €1M minima**.
- Per SAIL III ENAC chiede **copertura ≥ €2-5M responsabilità terzi**. Premi salgono a **€40-100k/anno**.
- Esclusioni standard polizze italiane: **operazioni in area montana + condizioni invernali + presenza sciatori/escursionisti** = esclusione potenziale (Pentema è zona Alta Via Appennino, escursionismo intenso aprile-novembre).
- Cap. 8 (CapEx/OpEx) menziona "Assicurazione" ma non quantifica seriamente. Cap. 5 non gestisce il rischio "no insurer will underwrite us".

**Cap. 5 da rivedere**: aggiungere §5.3.6 "Copertura assicurativa BVLOS" con scouting mercato e fallback (es. Captive insurance via Coopfond mutualità).

### Critica 12 — Mancanza di un *engagement readiness assessment* per ogni autorità

Il Cap. 5.11.3 elenca 13 stakeholder istituzionali con "trigger / frequenza / owner / documento". Manca:

- **Persona di riferimento** (nome + ruolo) per ogni autorità → senza nome, è velleitario
- **Stato attuale relazione** (= "abbiamo già parlato con X" o "completamente cold")
- **Budget allocato** all'engagement (FTE + viaggi + consulenti)
- **Plan B se l'autorità non risponde** (es. "se ENAC non risponde a pre-app in 60gg, escaliamo a Direttore Generale via PEC")

**Cap. 5 da rivedere**: §5.11.3 trasformare in tabella **operativa**, non in lista di propositi.

---

## 5. Engagement gap analysis

Quali autorità sono **NON ingaggiate** oggi (M+3) e devono esserlo entro un milestone specifico per non bloccare il progetto.

| Autorità | Stato attuale | Deve essere ingaggiata entro | Cosa NON è stato fatto | Rischio se non ingaggiata in tempo |
|---|---|---|---|---|
| **ENAC DRA UAS** | Cold (mai PEC formale) | M+1 (PEC pre-app) | PEC pre-application + ConOps draft + dossier operatore | RA-01 + RA-02 amplificati |
| **ENAC Direzione AAM** | Cold | M+6 (posizionamento HALE) | Position paper "Italian Stratospheric Layer" | RA-06 amplificato |
| **EASA UAS Department** | Cold | M+9 (Innovation Network engagement) | Concept paper + lettera intent | RA-06 |
| **EASA Innovation Network** | Cold | M+12 (RMT request HAPS) | RMT request documentata | RA-06 |
| **AGCOM Direzione Reti e Servizi** | Cold | M+3 (lettera consultazione spettro) | Lettera consultazione + coexistence analysis preliminare | RA-03 |
| **MIMIT Direzione Comunicazioni** | Cold | M+6 (PNRF + WRC coordination) | Position paper bande HAPS | RA-03 + RA-10 |
| **MIMIT Direzione Aerospazio** | Cold | M+6 (PNRR + strategia spaziale) | Project briefing | RA-10 |
| **ENAV / D-Flight** | Cold | M+3 (engagement preliminare U-Space + FL coordination) | Lettera intent + meeting | RA-05 + ostacolo U-Space Pentema futuro |
| **Garante Privacy** | Cold | M+1 (consultazione informale + DPIA preliminare M+3) | DPIA pubblica + workshop pubblico Pentema | RA-04 |
| **ACN — Agenzia Cybersicurezza Nazionale** | Cold | M+6 (autovalutazione NIS2 + registrazione se applicabile) | Autovalutazione NIS2 + nomina CISO | RA-08 |
| **CIRA Centro Italiano Ricerche Aerospaziali** | Cold (informale forse) | M+9 (MOU R&D 6B) | MOU R&D + posizionamento EuroHAPS-adjacent | RA-11 amplificato |
| **DG CNECT (Commissione UE)** | Cold | M+12 (proposta Horizon / EDF / IRIS² complementarity) | Concept note IRIS² complementarity | RA-11 |
| **DG DEFIS (Commissione UE)** | Cold | M+12 | Concept note EU sovereign HAPS layer | RA-11 |
| **Soprintendenza Liguria (BAP)** | Cold | M+3 (verifica vincoli paesaggistici Pentema) | Parere preventivo + check vincoli | Critica 7 |
| **Sindaco Torriglia (ordinanze)** | Engagement leggero (Coopfond ?) | M+3 (accordo formale, ordinanza enabling) | Convenzione + ordinanza | Critica 7 |
| **Comando Aeronautica Militare 1° ROC** | Cold | M+6 (servitù militari + zone proibite Liguria) | Verifica sovrapposizione | Critica 7 |
| **Presidenza Consiglio — DAGL (Golden Power)** | Cold | M+12 (consultazione preventiva su perimetro tech strategiche) | Lettera ricognitiva preventiva | RA-09 |

**Gap critico**: **17 autorità non ingaggiate** oggi su un piano che dichiara di andare in volo BVLOS a M+10. Anche con team dedicato, 17 engagement paralleli richiedono **3-5 FTE regulatory** a tempo pieno per 6 mesi, non 0.5 FTE come Cap. 9.

---

## 6. Cosa serve a Firmamento per uscire da ogni scenario

(Non come consulente, ma come *condizione di sopravvivenza* identificata dall'avversario)

| Scenario | Condizione di sopravvivenza |
|---|---|
| **RA-01** (SAIL escalation) | Track record commerciale UAS BVLOS preesistente (acquisizione operatore con autorizzazioni in essere — es. Aermatica3D); o partnership operativa con operatore certificato che fornisce "ombrello" SORA |
| **RA-02** (richieste integrazioni) | Budget 3-5× il piano (€150-400k) + team interno SORA specialist + relazione personale ENAC (head-of-office level) |
| **RA-03** (AGCOM stuck) | Rinuncia esplicita payload TLC commerciale Y1-Y3; accordo MVNO con TIM/Vodafone/Iliad/WindTre (perdita ~60-80% margine) |
| **RA-04** (Garante stop) | DPIA pubblica + governance condivisa Pentema + privacy hardware blur + AI Act compliance + no immagini raw in archivio + DPO certificato dedicato |
| **RA-05** (ENAV no-go) | Test HALE all'estero (UK/Spagna/Australia); rinuncia operatività Italia per HAPS perennial fino a 2030+ |
| **RA-06** (EASA pre-app rejected) | Engagement preliminare via Member State sponsor (Italia = ENAC formal request a EASA); partnership con EuroHAPS consortium come junior partner |
| **RA-07** (ping-pong) | Memorandum trilaterale ENAC-EASA-ENAV con owner singolo (impossibile senza sponsor politico MIT) |
| **RA-08** (NIS2) | CISO + ISO 27001 + SOC contratto + budget cyber €100-200k/anno; registrazione ACN |
| **RA-09** (Golden Power) | Cap table 100% IT + nessun investitore extra-EU; notifica preventiva DAGL; relazione MIMIT preventiva |
| **RA-10** (MIMIT sub-contracting) | Accettare ruolo junior partner consortium con Leonardo/TAS; perdita IP leadership HAPS |
| **RA-11** (DG CNECT exclusion) | Posizionamento esplicito "complementare a IRIS²" (Boundary B2 già rispetta); entrata in consortium EuroHAPS; lobbying via Rappresentanza Italiana a Bruxelles |
| **RA-12** (ENAC sospensione U-Space) | Partecipazione attiva consultazione pubblica gennaio-aprile 2026; submission Firmamento in fase contributi; relazione politica per accelerare adozione |

**Common pattern**: tutte le condizioni di sopravvivenza richiedono o (a) tempo (3-7 anni) o (b) capitale (€2-10M aggiuntivo per regulatory) o (c) **rinuncia parziale a ambizioni** (no payload TLC, no operatività perennial IT, no IP leadership solo). Lo Studio non riconosce nessuna delle tre.

---

## 7. Critiche al Cap. 9 (engagement plan)

Il Cap. 9 §9.1.3 dichiara 4.0 Regulatory Engagement con:
- 4.1 Pre-application ENAC M+3-M+6
- 4.2 Engagement EASA M+6-M+9
- 4.3 AGCOM consultation M+6-M+10
- 4.4 Privacy/Garante DPIA M+3-M+9

**Critiche**:

1. **Frequenze irrealistiche per le capacità dichiarate**. Il Cap. 9 §9.1.3 dichiara 3-4 FTE M+0-3 e 5-7 FTE M+6-10. Di questi, **0 sono dedicati full-time al regulatorio**. Aviation-regulatory-counsel è consulente esterno (€80-150k/anno se full-time). Per 4 engagement paralleli + DPIA + 17 autorità + audit NIS2 + AI Act, serve un **Head of Regulatory Affairs** interno + 2-3 specialisti (legal + technical + cyber). Costo annuale: €350-600k. **Non in CapEx Cap. 8**.

2. **Ordinamento attività errato**. Garante (4.4) inizia M+3, ENAC (4.1) M+3, AGCOM (4.3) M+6. In realtà ENAC e Garante dovrebbero iniziare **M+0-1** perché sono i collo di bottiglia maggiori; AGCOM è meno urgente per 6A.

3. **Manca "regulatory horizon scanning"**: nessuno monitora gli aggiornamenti normativi continui (es. ENAC pubblica circolari mensili, EASA pubblica Opinion/Decision settimanalmente; AGCOM avvisi; Garante newsletter). Per una PMI, monitoring richiede **0.3-0.5 FTE dedicato** + sottoscrizioni informative (€10-30k/anno).

4. **Manca contingency per "no response"**. Il piano assume risposta autorità entro tempi standard. La PA italiana ha **silenzio-rifiuto** in molti casi (autorizzazioni complesse), oppure **silenzio-significativo prolungato**. Cap. 9 non ha "se ENAC non risponde a M+6, allora X".

5. **Frequenza meeting irrealistica**. ENAC pre-application meeting: 1 incontro M+3 + 1 follow-up M+6. ENAC non concede 2 meeting in 3 mesi per pre-application — concede 1 incontro e poi corrispondenza scritta. Stessa cosa AGCOM, Garante.

6. **Manca preparazione di un "campione politico"**. In Italia, per accelerare procedimenti complessi, serve **sponsor politico** (Assessore Regione + parlamentare locale + eventualmente Sottosegretario MIT). Cap. 9 non prevede engagement politico esplicito.

**Cap. 9 da rivedere**: dedicare workstream 4.0 Regulatory con (a) 1 Head + 2 FTE interni + 2 consulenti, (b) budget €350-600k/anno, (c) plan B per ogni autorità, (d) campione politico identificato (Assessore Regionale + parlamentare GE/Liguria).

---

## 8. Critiche al verdetto Cap. 10 regolatorio

Il Cap. 10 §10.3 dichiara "Go Condizionato 6A" con C1-C5 hard conditions. **Analisi probabilistica**:

| Hard Condition | P(soddisfatta entro M+9-10) realistica |
|---|---|
| C1 — LoI Regione Liguria firmata entro M+9 | 60-70% (politica favorevole ma timing PA italiana) |
| C2 — Autorizzazione SORA ENAC operativa entro M+9 | **15-25%** (vedi RA-01, RA-02; il base rate per SAIL III è 12-18 mesi minimi) |
| C3 — Mix funding ≥ 60% committed entro M+10 | 50-60% (Coopfond probabile; resto incerto) |
| C4 — ≥ 8/10 cooperative confermate entro M+6 | 70-80% |
| C5 — Pre-app ENAC con feedback documentato entro M+3-M+6 | 55-65% |

**P(tutte le 5 condizioni soddisfatte)** = 0.65 × 0.20 × 0.55 × 0.75 × 0.60 ≈ **3-7%**.

Il Cap. 10 §10.6 critica 1 dichiara P(tutte) "~25-60%". È **sopravvalutato di 4-10×**. La realtà: il Go Condizionato 6A diventa Hold automatico in ~93-97% degli scenari realistici.

**Implicazione**: il verdetto Cap. 10 va riformulato:
- **Go Condizionato 6A** → **Hold con piano regolatorio rafforzato** come default; Go solo se C2 (SORA) si sblocca in modo certo, non probabilistico.
- **Scope ridotto Y1** → operatività **EVLOS + VLOS** Y1 (no BVLOS) per "stare in piedi" mentre SORA process si sblocca. Revenue Y1 ridotta del 50-70%.

**Sul 6B Hold del Cap. 10**: formalmente corretto, ma il razionale "Special Condition negoziata caso per caso" è non-realistico (vedi Critica 2). Il Cap. 10 deve dichiarare apertamente che 6B è **R&D speculativo con probabilità path certificativo civile EU < 15%** entro l'orizzonte dello Studio (cioè entro 2032). Phase B 6B è quindi **R&D per opzionalità futura**, non per operatività commerciale a M+48.

---

## 9. Action items regolatori prioritari pre-Gate G3

Lista numerata di azioni che, **se non eseguite entro M+9**, rendono il Gate G3 non difendibile.

1. **PEC formale ENAC DRA UAS** entro M+1 con ConOps draft + dossier operatore + richiesta pre-application meeting. Senza PEC = senza data certa = senza priorità ENAC.
2. **PEC formale Garante Privacy** entro M+1 con notifica intenzione DPIA pubblica + richiesta consultazione informale art. 36 GDPR.
3. **PEC formale AGCOM Direzione Reti e Servizi** entro M+2 con lettera consultazione spettro + manifestazione interesse banda HAPS dedicata.
4. **PEC formale ENAV** entro M+2 con lettera intent + richiesta meeting U-Space + futuro coordinamento FL.
5. **Assunzione Head of Regulatory Affairs** entro M+3 (full-time, profilo senior 10+ anni, esperienza ENAC/EASA). Budget €100-150k/anno + benefits.
6. **Nomina CISO** (anche part-time / fractional) entro M+3 per NIS2 + DO-326A. Budget €40-80k/anno.
7. **Nomina DPO certificato** (esterno o interno) per GDPR + DPIA + Garante. Budget €30-60k/anno.
8. **DPIA preliminare pubblica** submitted al Garante entro M+3 (non M+6 come Cap. 9).
9. **Autovalutazione NIS2** entro M+3 con esito formale "essenziale" / "importante" / "non in scope".
10. **Workshop pubblico Pentema** entro M+3 con notarizzazione verbale; consenso informato comunità prima di ogni engagement Garante.
11. **Verifica vincoli paesaggistici/militari/Soprintendenza** entro M+3 sul rettangolo operazionale Pentema.
12. **Convenzione Comune Torriglia** entro M+3 con ordinanza enabling sorvoli.
13. **Lettera ricognitiva DAGL Golden Power** entro M+6 con qualificazione perimetro tech strategiche.
14. **Engagement formale CIRA** entro M+6 con MOU draft Phase B 6B.
15. **Position paper "Italian Stratospheric Layer"** entro M+6 pubblicato (no oltre M+9 come dichiarato Cap. 5).
16. **Scouting assicurazioni BVLOS** entro M+6 con 3 quotation Generali/Allianz/Lloyd's.
17. **Engagement formale EASA Innovation Network** entro M+9 via ENAC sponsorship (Member State channel, non bilaterale).
18. **Audit AS/EN 9100 preparatorio** entro M+9 con ente certificatore (RINA/DNV); ottenimento entro Y2 obbligatorio per SAIL ≥ III.
19. **Submission contributi consultazione pubblica Regolamento ENAC U-Space** entro aprile 2026 (= M+0-2 reali se Cap. 5 era M+3 di marzo/aprile 2026).
20. **AI Act gap analysis** entro M+6 con classificazione sistemi e roadmap conformità per agosto 2026 e agosto 2027.

**Costo aggregato action items**: €450-800k aggiuntivi su Y1 (non in CapEx Cap. 8). **FTE aggiuntivi**: 3-4 dedicati. **Senza questi, il Gate G3 non è difendibile e il Go Condizionato è una postura, non una decisione.**

---

## 10. Showstopper regolatori NON considerati dal Cap. 5

Cose che il Cap. 5 ha **completamente omesso** e che possono diventare bloccanti.

1. **AI Act (Reg. UE 2024/1689)** — operativo agosto 2026 / agosto 2027 / agosto 2028. Citato solo "AI Act compliance" in §5.6.2 ma:
   - art. 5 (pratiche vietate) può colpire payload IR + biometric
   - Annex III (high-risk) classifica gestione infrastrutture critiche + PA-safety → sistemi Firmamento qualificati high-risk
   - Costo compliance + Notified Body: €100-300k iniziali

2. **EUSPA (EU Agency for the Space Programme)** — citato 0 volte. EUSPA gestisce IRIS² + Galileo + Copernicus. Per qualunque servizio EO commerciale che si interfacci con Copernicus, serve coordinamento EUSPA. Per HAPS che vuole "complementare a IRIS²" (Boundary B2), engagement EUSPA è critico.

3. **EUROCONTROL Network Manager** — citato 0 volte. Per spazio aereo italiano > FL195 e per qualunque test stratosferico, EUROCONTROL ha competenza ATFM. ENAV non basta.

4. **Codice Navigazione + Codice Penale art. 432-bis** ("attentato alla sicurezza dei trasporti") — un incidente UAS può costituire reato penale per il pilota e l'operatore. Cap. 5 non gestisce il rischio penale.

5. **D.Lgs. 81/2008 Sicurezza sul lavoro** — operazioni UAS in area montana con presenza pubblico richiedono valutazione rischio + DUVRI + formazione lavoratori. Cap. 5 non ne parla.

6. **Direttiva Macchine 2006/42/CE + nuovo Reg. UE 2023/1230** — UAS pesanti sono "macchine" ai sensi della direttiva, con obblighi di certificazione CE separati da quelli aeronautici. Operativo gennaio 2027.

7. **Direttiva ATEX 2014/34/UE** — batterie ad alta energia (litio in HALE 6B = 100+ kWh) ricadono in normativa ATEX per stoccaggio + trasporto.

8. **Regolamento RoHS 2011/65/UE** — limiti sostanze pericolose nell'elettronica. Per batterie + payload elettronico serve compliance.

9. **EUSPA — Galileo PRS authorization** — se Firmamento usa Galileo Public Regulated Service (più robusto contro jamming/spoofing), serve autorizzazione MIMIT (PRS authority IT).

10. **WHO IFC INES nuclear materials** — non applicabile probabilmente, ma se HALE 6B include payload sci. con sorgenti radioattive (es. spettrometri) serve autorizzazione ISIN (Ispettorato Nazionale Sicurezza Nucleare).

11. **TLC apparati radio NB-IoT/LoRaWAN** — se cooperative usano sensori IoT comunicanti con HAPS, ogni terminale richiede CE-RED. Volume scale richiede notifica MIMIT.

12. **Modello unico** del processo amministrativo (Codice Amministrazione Digitale + SPID/CIE per accesso piattaforma cooperative). Cap. 4 INT-06 cita SPID ma non gestisce conformità AgID / PSN (Polo Strategico Nazionale) per servizi cloud erogati a PA.

13. **Coabitazione spettro con servizi 5G mmWave** — bande 26/28 GHz (5G) e bande HAPS (27.9-28.2 GHz feeder) sono **adiacenti**. Coordinamento operatori 5G mandatorio per non interferenza. Non considerato.

14. **Codice di condotta UE per HAPS (in elaborazione)** — la Commissione UE sta valutando un codice di condotta volontario HAPS analogo a Long-Term Sustainability of Outer Space. Firmamento dovrebbe **partecipare** all'elaborazione, non attendere passivamente.

15. **EASA Cyber Regulation for Aviation (Part-IS)** — Implementing Regulation 2023/203 obbligo Information Security Management System per operatori UAS specific (applicazione progressiva 2026-2028). Cap. 5.7 non lo cita.

---

## Note finali

Questo audit è prodotto dall'agente `regulatory-adversary` come **stress-test** del Volume 1. La postura è **deliberatamente avversaria** — non per ostilità al progetto, ma per identificare i blocchi che un regolatore reale (lento, conservativo, terrorizzato dal precedente, sotto-staffato, sensibile a lobbying) **userebbe legittimamente** per dire no o sospendere.

**Convergenza con altri Red Team**: l'audit è coerente con red-team-skeptic (sopravvalutazione confidence), competitor-intelligence (Tier 1 lobby contro newcomer), aviation-regulatory-counsel (anti-padre del SÌ). Le critiche sono **complementari**, non sovrapposte.

**Raccomandazione operativa al management Firmamento** (unica concessione consulenziale, in deroga alla regola "no soluzioni"):

> Prima del Gate G3 (M+10/M+11), il Cap. 5 va **integralmente riscritto** con (a) probabilità realistiche delle 12 minacce qui mappate, (b) action items pre-G3 prioritari §9, (c) shifting del verdetto Cap. 10 6A da "Go Condizionato" a "Hold con piano regolatorio rafforzato" come default. Senza questa riscrittura, il documento **non passa due diligence** di un investitore istituzionale o di un RUP esperto su affidamenti aerospace.
