# 04 — Gradiente di attrito regolatorio per classe di piattaforma (Pentema)

> **Analisi bottom-up — Percorso "servizio-first"**
> Firmamento Technologies, Progetto HALE / servizio Aree Interne (caso pilota: Pentema, Torriglia, GE)
> **Autore:** Regulatory Counsel (EASA / ENAC / U-Space)
> **Data:** 2026-07-08
> **Metodo:** ripartenza da zero. Le conclusioni SORA/SAIL pregresse del repo (`cap-05`, `A11-Safety-Case-SORA`) sono state lette **criticamente**, non assunte.
> **Domanda guida:** qual è il percorso regolatorio **più economico e veloce** che abilita comunque un servizio utile (anche parziale) a Pentema?

---

## 0. Disclaimer epistemico (fatto normativo vs stima)

- **[FATTO]** = testo di regolamento/AMC in vigore, citato con articolo/tabella e fonte nel repo.
- **[STIMA]** = valutazione di chi scrive (iGRC/SAIL preliminari, costi, tempi). Le stime di costo e tempo hanno **confidenza medium-low**: derivano da base-rate italiani + figure dello Studio esistente, **non** da un pre-application ENAC concluso.
- Regola dura: **nessuna classificazione SORA è definitiva finché ENAC non la conferma in pre-application** (art. 11 Reg. (UE) 2019/947). Tutti i valori qui sono *preliminary-grade*.

---

## 1. La macchina che decide il costo: i tre "cancelli" EASA

Il costo/tempo regolatorio non dipende dalla piattaforma in sé, ma da **in quale categoria la missione cade** e **quale SAIL genera la SORA**. Fatti normativi:

### 1.1 Open / Specific / Certified — i trigger [FATTO]
- **Open** (basso rischio): UAS < 25 kg, **VLOS**, **≤ 120 m AGL**, non sopra persone non coinvolte, classi C0–C4. Riferimenti: art. 4 Reg. (UE) 2019/947 (`CELEX_32019R0947` righe 297–305); sotto-categoria **A3** = `UAS.OPEN.040`: **≥ 150 m orizzontali** da zone residenziali/commerciali/industriali/ricreative, nessuna persona non coinvolta sorvolata (righe 1030–1046).
- **Specific** (medio rischio): tutto ciò che eccede Open → **autorizzazione operativa** ENAC previa **SORA** (art. 5 e art. 11 Reg. 947; recepimento ENAC Reg. APR Ed.3 art. 10–11, art. 26 BVLOS).
- **Certified** (alto rischio): scatta **solo se** (art. 6 Reg. 947, righe 347–392): (i) sorvolo di **assembramenti di persone**, (ii) **trasporto di persone**, (iii) **merci pericolose** ad alto rischio; **oppure** se l'autorità, sulla base della SORA, determina che il rischio **non è mitigabile adeguatamente senza certificazione** (art. 6.2). Inoltre la SORA stessa spinge in Certified quando **GRC finale > 7** o si finisce nelle **celle grigie** della tabella iGRC (Annex ED Decision 2025/018/R righe 1018, 1084–1086, 1664).

> **Conseguenza-chiave:** superare 25 kg **NON** butta automaticamente in Certified. Ciò che butta in Certified è: sorvolare assembramenti, salire in quota/spazio controllato tanto da alzare l'ARC oltre soglia, o generare un GRC > 7. Questo è il perno di tutto il gradiente.

### 1.2 iGRC — la tabella che premia il "piccolo e lento" [FATTO]
`Table 1` dell'Annex a ED Decision 2025/018/R (righe 997–1028). iGRC = f(dimensione caratteristica × velocità max, densità popolazione):

| Densità pop. (ab/km²) \ Dim.max·vel.max | **1 m / 25 m/s** | **3 m / 35 m/s** | **8 m / 75 m/s** | **20 m / 120 m/s** | **40 m / 200 m/s** |
|---|---|---|---|---|---|
| Controlled ground area | 1 | 1 | 2 | 3 | 3 |
| **< 5** (Remote) | **2** | **3** | 4 | 5 | 6 |
| < 50 (Lightly pop.) | 3 | 4 | 5 | 6 | 7 |
| < 500 (Sparsely pop.) | 4 | 5 | 6 | 7 | 8 |
| < 5 000 | 5 | 6 | 7 | 8 | 9 |
| < 50 000 | 6 | 7 | 8 | 9 | 10 |
| > 50 000 (assemblies) | 7 | 8 | **fuori SORA → Certified** | | |

Note [FATTO]: ≤ 250 g → iGRC = 1 sempre (riga 1020). Dim. > 40 m → calcolo via Annex F (riga 1030).

### 1.3 Mitigazioni GRC — quanto si può scendere [FATTO]
`Table 5` (righe 1261–1273):
- **M1(A) Sheltering** −1 (low) / −2 (medium): applicabile se l'UA "non penetra un edificio standard" e i sorvolati sono protetti da strutture (riga 1023). Facile da rivendicare in un borgo con case in pietra.
- **M1(B) Restrizioni operative** −1 (medium) / −2 (high).
- **M1(C) Ground observation** −1 (low).
- **M2 Riduzione energia d'impatto** (es. paracadute/BRS) −1 (medium) / −2 (high).
- Limite: il GRC non scende sotto il valore "controlled ground area" della colonna (riga 1313).

### 1.4 SAIL — il moltiplicatore di costo [FATTO]
`Table 3` (righe 1655–1666): SAIL = f(GRC finale, ARC residuo). Estratto rilevante per valle montana (ARC-a/b):

| GRC finale \ ARC | **a** | **b** | c | d |
|---|---|---|---|---|
| ≤ 2 | **I** | **II** | IV | VI |
| 3 | **II** | **II** | IV | VI |
| 4 | III | III | IV | VI |
| 5 | IV | IV | IV | VI |
| 6 | V | V | V | VI |
| 7 | VI | VI | VI | VI |
| > 7 | → **Certified** | | | |

Il SAIL determina **quanti OSO** e a quale robustezza (Table 14 dell'Annex): SAIL I ≈ pochi OSO "low/optional"; SAIL VI ≈ 24 OSO tutti "high". **Ogni gradino di SAIL è un salto di costo di compliance e di tempo.**

### 1.5 ARC — l'effetto quota/spazio aereo [FATTO/STIMA]
- Valle appenninica, spazio **Classe G non controllato**, VLL, traffico GA sporadico (parapendio/alianti) → **iARC-b** [STIMA plausibile, coerente con `A11`].
- Salire in **spazio controllato** (TMA, aerovie, Classe A/C) → iARC-c/d → SAIL IV–VI anche con GRC basso. È il meccanismo per cui **la quota è un cancello di costo indipendente dal peso**.
- Sopra **FL195** lo spazio è tipicamente controllato (Classe C→A); **HALE perennial a ~FL650** attraversa in salita/discesa spazio controllato → coordinamento ENAV obbligatorio +, di fatto, Certified.

---

## 2. TABELLA GRADIENTE (deliverable principale)

Ipotesi comune: missione reale sopra/vicino Pentema, terreno montano, densità locale **< 5 ab/km²** ("Remote") ma con *iGRC footprint* che può intercettare SS45/edifici sparsi (→ banda **< 50**) e, se il buffer è ampio, sfiorare Torriglia (~1500 ab, banda **< 500/5000**). Perciò per ogni riga do il **range iGRC** (footprint stretto → footprint largo).

| # | Piattaforma | Categoria | iGRC (Pentema)¹ | GRC finale² | ARC | **SAIL** | Iter regolatorio | Tempo³ | Costo compliance³ | ABILITA | NON PUÒ FARE |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | Nano/micro < 250 g (o C0) | **Open A1** | n/a (iGRC 1) | — | — | — | Registrazione operatore + patentino A1/A3 online | **giorni–settimane** | **< €0.5k** | Riprese ravvicinate VLOS spot | Payload utile nullo; VLOS; no servizio |
| **1** | **Drone C3 < 25 kg, < 3 m** (multirotore o fixed/box-wing) | **Open A3** | n/a (Open, no SORA) | — | — | — | Registrazione operatore (art.14) + attestato A3 + marcatura C3 (Reg. 945) + RC base | **settimane** | **€1–5k** + polizza | EO/mapping **VLOS** su versanti **disabitati** (frane, incendi su terreno non sorvolato da persone), demo | **BVLOS**; sorvolo borgo/persone; loiter persistente; > 120 m AGL; **niente connettività al borgo** |
| **2a** | **Stesso C3, ma ~1 m e lento (< 25 m/s)** BVLOS | **Specific** | 2 → 3 | **1–2** (M1A −1) | b | **I–II** | Pre-app ENAC → SORA 2.5 → autorizzazione + OM/MM | **9–18 mesi** | **€25–70k** | **BVLOS** EO su valle sparsa, monitoraggio frane/incendi area vasta, qualche loiter | Sorvolo assembramenti; quota controllata; connettività dedicata |
| **2b** | **C3 < 25 kg, ~3 m** BVLOS (box-wing ~3 m del concept) | **Specific** | 3 → 4 (fino 5 se footprint largo) | **2–3** (M1A + M2) | b | **II (–III)** | come 2a, con DAA + C2 robusto (art. 26 ENAC) | **9–24 mesi** | **€40–120k** | BVLOS EO valle, endurance media, relay locale sperimentale | Sorvolo borgo/persone; spazio controllato; H24 continuo |
| **3** | **Fixed-wing/VTOL > 25 kg** (es. CW-30E ~38 kg, 3–4 m) BVLOS | **Specific** | 4 → 6 | **3–5** | b (c se sale) | **III–IV** | SORA "pesante": OSO robusti, M2 certificato, insurance ×3–5 | **12–30 mesi** | **€80–250k+** | Payload EO pesante, endurance lunga, esperimenti telecom | Certified-trigger se sorvola assembramenti; se sale in TMA → SAIL IV+ |
| **4** | **MALE** (> 150 kg, span > 10 m, FL200+) | **Specific SAIL alto → di fatto Certified** | 5 → 7+ (col. 20 m) | 5–7+ | **c/d** (spazio controllato) | **IV–VI → Certified** | SORA al limite + art. 6.2 (autorità); spesso Type Certificate | **2–4+ anni** | **€1–5M+** | Sorveglianza persistente area vasta, alta quota | Sproporzione assurda per Pentema; entra in spazio controllato; framework maturo assente |
| **5** | **HALE** (~20 km/FL650, span 25–40 m, perennial) | **Certified** (Type Certificate) | col. 40 m (celle alte / calcolo Annex F) | — | **c/d in salita/discesa** | **Certified** — no SAIL | **Special Condition negoziata** + TC + Operating Cert + ENAV | **5–8+ anni** | **€5–15M+ (sola cert.)** | Connettività regionale persistente + EO wide-area, "layer stratosferico" | **Nessun framework HAPS civile EASA/ENAC**; ENAV FL195+; spettro HAPS non licenziato → **non abilita servizio a breve** |

¹ [STIMA] range footprint stretto→largo, banda densità <5 → <50 (<500 se il buffer tocca Torriglia). ² [STIMA] dopo M1(A) sheltering e/o M2. ³ [STIMA] confidenza medium-low; costi = consulenza SORA + documentazione + polizza + attestati, **esclusa** la piattaforma.

---

## 3. Le SOGLIE che fanno esplodere costo e tempo (i "cliff")

Ordinate per impatto sul rapporto costo/beneficio del servizio Pentema:

### SOGLIA 1 — VLOS → BVLOS (Open → Specific). **Il primo e più universale salto.** [FATTO]
Passare da Open A3 a Specific è il salto da **"settimane, €1–5k, zero SORA"** a **"9–24 mesi, €25–120k, SORA completa + Operations/Maintenance Manual + DAA + C2 fade-margin + attestato pilota BVLOS + assicurazione BVLOS (×3–5)"**. È il cancello che, da solo, cambia l'ordine di grandezza. Base normativa: art. 5/11 Reg. 947; art. 26 ENAC Ed.3. **Rischio prassi:** integrazioni ripetute ENAC (art. 12.5 Reg. 947; art. 6 L. 241/1990) allungano di 6–15 mesi (cfr. `AUDIT-REGULATORY` RA-02, P 75–85%).

### SOGLIA 2 — Dimensione caratteristica × velocità × densità (la scala della piattaforma). [FATTO]
Ogni **colonna** della tabella iGRC (1 m→3 m→8 m→20 m→40 m) e ogni **banda di densità** salgono l'iGRC di 1–2 punti; ~2 punti di GRC = ~1–2 gradini di SAIL = raddoppio/triplicazione degli OSO robusti. Concretamente: **1 m/lento a <5 ab/km² = iGRC 2 (SAIL I–II); 3 m = iGRC 3 (SAIL II); 8 m = iGRC 4 (SAIL III); 20 m = iGRC 5 (SAIL IV).** Il **peso** (25 kg) non entra direttamente nella SORA, ma è: (a) confine Open/Specific [FATTO], (b) proxy di energia d'impatto → M2 più difficile, (c) driver del premio assicurativo. **Sotto-soglia dura:** **sorvolo di assembramenti/persone** → art. 6.1(a) → **Certified** immediato, a qualunque peso.

### SOGLIA 3 — Quota / ingresso in spazio aereo controllato → Certified. **Il cliff finale.** [FATTO/STIMA]
Finché si resta VLL in Classe G, ARC-b e SAIL ≤ III sono raggiungibili. Salire in **spazio controllato** (TMA Genova a ~15 km, aerovie, Classe A/C) porta iARC a c/d → **SAIL IV–VI** anche con GRC basso. **FL195+ e operazione perennial (HALE)** = coordinamento ENAV obbligatorio + assenza di framework → **Certified / Type Certificate**: da €decine-di-migliaia a **€5–15M solo per la certificazione**, da mesi a **5–8+ anni**, con **showstopper** documentato (nessuna Certification Specification HAPS EASA; cfr. `cap-05` §5.10.1, RSK-REG-001).

---

## 4. Path spettro/autorizzazioni per la connettività (AGCOM · ENAC · ENAV · U-Space)

Il servizio "connettività" ha **due catene autorizzative parallele e indipendenti**: (A) far **volare** la piattaforma (ENAC/ENAV, §1–3) e (B) **trasmettere** legalmente (spettro).

### 4.1 Chi fa cosa [FATTO]
- **AGCOM + MIMIT:** licenze/diritti d'uso spettro per servizio commerciale (D.Lgs. 259/2003 Codice Comunicazioni Elettroniche; PNRF gestito da MIMIT che recepisce le WRC-ITU).
- **ITU Radio Regulations (ed. 2024, WRC-23):** bande HAPS riconosciute — gateway 6.4–6.7 / 27.9–28.2 / 31–31.3 GHz; service link 38–39.5 / 47 GHz; NTN S-band ~2 GHz (3GPP n255/n256).
- **ENAC/ENAV:** aeronavigabilità + integrazione spazio aereo (indipendente dallo spettro).
- **U-Space (Reg. (UE) 2021/664):** applicabile **solo** dove ENAC **designa** un volume U-Space; **non è obbligatorio** in generale. Stato Italia: embrionale (prima area R100 San Salvo attiva dal 28/11/2025; Regolamento U-Space Ed.1 in consultazione gen–apr 2026). **Per Pentema, nel breve, non è un prerequisito**: la via è autorizzazione Specific + **NOTAM/coordinamento ENAV** puntuale.

### 4.2 Gradiente di attrito spettro (dal più al meno economico) [FATTO normativo / STIMA tempi]
1. **Banda esente da licenza (ISM 2.4/5.8 GHz)** per link locale/backhaul corto → **nessuna licenza**, ma potenza/portata limitate: connettività "di prossimità" only. **Giorni.**
2. **Spettro di un MNO ospitante (accordo MVNO/hosting con TIM/Vodafone/Iliad/WindTre)** → si usa lo spettro già licenziato dell'operatore; nessuna nuova allocazione AGCOM. È **la via realistica per erogare connettività "utile" al borgo nel breve.** **Settimane–mesi** (negoziazione commerciale, non regolatoria).
3. **Licenza individuale AGCOM su banda HAPS dedicata / NTN** → richiede allocazione PNRF + parere MIMIT + coordinamento ITU + assenza di opposizione operatori terrestri → **12–36 mesi, esito incerto**, dipendenza da **WRC-27** (cfr. `AUDIT-REGULATORY` RA-03, P 70–80% per banda dedicata). **Non percorribile come base del servizio a breve.**

> **[FATTO] 3GPP:** HAPS è scenario NTN supportato senza modifiche UE (`38811` §6.1.5), quindi tecnicamente un payload gNB è standard; **il collo di bottiglia è il diritto d'uso dello spettro, non lo standard.**

---

## 5. Lettura critica delle conclusioni pregresse (SORA SAIL III)

Il repo (`A11-Safety-Case-SORA` §A.11.1) fissa per Pentema **iGRC 5 → GRC 3 → SAIL III** classificando Pentema "sparsely populated" (banda **< 500**). **Critica:**
- La densità dichiarata è **< 5 ab/km²** (14 residenti) = banda **"Remote" (< 5)** nella tassonomia SORA 2.5 (Annex righe 1113–1141), **non** "< 500". Sembra una carry-over dalla terminologia SORA 2.0 ("sparsely populated" = fascia alta).
- Per un UAS a **3 m**, banda **< 5** → **iGRC 3**, non 5. Con **M1(A) −1** → **GRC 2 → SAIL II** (ARC-b). Anche in banda **< 50** (footprint che include SS45) → iGRC 4 → GRC 3 → **SAIL II**.
- **iGRC 5 è difendibile solo se** il footprint (operational volume + ground risk buffer, che per un fixed-wing veloce è ampio) intercetta stabilmente Torriglia o zone a densità < 500. Con **piattaforma più piccola/lenta e geofencing stretto**, il buffer si riduce e **SAIL II diventa il target realistico**.
- **Implicazione strategica:** la scelta di piattaforma **grande (CW-30E ~38 kg, 3–4 m, veloce)** è ciò che spinge verso iGRC 5 / SAIL III. **Scendere di piattaforma abbassa il SAIL di un gradino** → meno OSO robusti → meno costo/tempo. Questo conferma la tesi bottom-up: **il minimo attrito spinge in basso nella scala.**
- Nota terminologica: `A11` chiama il CW-30E "Class III" — nomenclatura NATO/STANAG, **non** una classe Reg. (UE) 2019/945 (C0–C6). Irrilevante ai fini SORA (che usa dimensione/velocità), ma da correggere per pulizia.

---

## 6. VERDETTO — percorso minimo-attrito

**Scala a gradini (ciascun gradino sblocca servizio incrementale al minimo costo regolatorio marginale):**

- **G0 — Subito (settimane, €1–5k): C3 < 25 kg in Open A3, VLOS.** EO/mapping dei **versanti disabitati** (frane, ricognizione incendi) tenendosi ≥ 150 m da edifici e senza sorvolo persone. Servizio **parziale ma reale e immediato**, zero SORA. Serve anche come track-record per ENAC.
- **G1 — 9–18 mesi (€25–70k): piccolo UAS (≤ 25 kg, dim. ~1–3 m, lento) in Specific BVLOS, target SAIL II.** Sblocca **BVLOS EO area-vasta** sulla valle sparsa. Progettare la ConOps per **restare GRC ≤ 3 × ARC-b**: geofencing stretto (no Torriglia nel footprint), **no sorvolo del borgo/assembramenti** (evita art. 6 → Certified), VLL Classe G (evita ARC-c/d), M1(A) sheltering + M2 recovery.
- **G2 — connettività: via MNO-hosting o ISM locale**, **non** via banda HAPS dedicata (che è 12–36 mesi, incerta, WRC-27-dipendente).

**Cosa NON fare a breve:** MALE e soprattutto **HALE**. HALE è categoria **Certified**, senza framework HAPS civile, con ENAV FL195+ e spettro non licenziato: **5–8+ anni e €5–15M solo di certificazione**, **showstopper** già registrato (RSK-REG-001). **Non abilita alcun servizio a Pentema nell'orizzonte finanziabile**; resta vettore strategico Y6+, non leva di servizio.

**Sintesi del gradiente:** il costo/tempo regolatorio **non cresce con continuità, cresce a scalini**, e i tre scalini sono **(1) VLOS→BVLOS, (2) scala/dimensione della piattaforma + sorvolo persone, (3) quota/spazio controllato→Certified**. Poiché ogni scalino moltiplica costo e tempo, **il vincolo di "minimo attrito" spinge deterministicamente verso il basso nella scala di piattaforma**: la configurazione che massimizza servizio-utile per euro-di-compliance è il **piccolo UAS (≤ 25 kg) usato prima in Open A3 e poi escalato a Specific BVLOS al SAIL più basso ottenibile (II)**, con connettività via spettro di terzi.

---

## 7. Confidenza e domande aperte

| Elemento | Confidenza | Nota |
|---|---|---|
| Trigger Open/Specific/Certified, tabelle iGRC/SAIL/Table 5 | **high** [FATTO] | Reg. 947, Annex ED Decision 2025/018/R citati per riga |
| iGRC/GRC/SAIL preliminari Pentema per piattaforma | **medium-low** [STIMA] | Dipende dalla banda densità del *footprint* e da M1/M2 accettate da ENAC |
| Costi/tempi di compliance | **medium-low** [STIMA] | Base-rate + Studio esistente; non validati da pre-app |
| ARC-b in valle Classe G | **medium** [STIMA] | Da confermare vs TMA Genova / R-71 Brugneto / parapendio |
| Path spettro (MNO-hosting via realistica) | **medium-high** | Fatto normativo chiaro; tempi negoziali commerciali |
| HALE = Certified senza framework | **high** [FATTO] | Assenza CS HAPS EASA confermata; showstopper documentato |

**Domande aperte da chiudere in pre-application ENAC (M+0–3):**
1. **OQ-1** — banda densità del footprint Pentema: "<5/<50" (nostra tesi, SAIL II) vs "<500" (tesi conservativa `A11`, SAIL III)? *È il singolo driver di costo più pesante.*
2. **OQ-2** — M1(A) sheltering accettata in borgo montano in pietra? M2 (BRS) come tactical robust?
3. **OQ-3** — ARC-b confermato con TMPR Standard nonostante prossimità TMA Genova / R-71?
4. **OQ-4** — soglia dimensione: fino a che span/velocità ENAC tiene SAIL II prima di scattare a III?
5. **OQ-5** — connettività: preferenza ENAC/AGCOM tra ISM locale, MNO-hosting e domanda banda dedicata?

---

### Fonti (repo)
- `fonti/CELEX_32019R0947_IT_TXT.md` — Reg. (UE) 2019/947 (Operations): art. 4 (Open), art. 5/11 (Specific/autorizzazione), art. 6 (Certified triggers), `UAS.OPEN.040` (A3).
- `fonti/CELEX_32019R0945_IT_TXT.md` — Reg. (UE) 2019/945 (classi C0–C6): requisiti classe **C3** (MTOM < 25 kg, dim. < 3 m, righe 1795–1874).
- `fonti/ed_decision_2025-018-r.md` + `fonti/annex_to_ed_decision_2025-018-r_1.md` — SORA 2.5 (in vigore 15/09/2025): Table 1 iGRC (r.997–1028), Table 5 mitigazioni (r.1261–1273), Table 3 SAIL (r.1655–1666), Certified via GRC>7/celle grigie (r.1018, 1664).
- `fonti/Regolamento_APR_Ed_3_Emend_1.md` — ENAC APR Ed.3+Em.1: art. 10–11 (critiche/autorizzazione), art. 26 (BVLOS), art. 31 (data link), art. 34 (privacy).
- `fonti/CELEX_32021R0664_IT_TXT.md` + `fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md` — U-Space (designazione ENAC, non obbligatorio; Italia embrionale).
- `fonti/38811.md` — 3GPP TR 38.811 (HAPS come scenario NTN).
- Letture critiche: `studio-di-fattibilita/cap-05-quadro-normativo.md`, `studio-di-fattibilita/allegati/A11-Safety-Case-SORA/`, `studio-di-fattibilita/AUDIT-REGULATORY-VOLUME-1.md`.
