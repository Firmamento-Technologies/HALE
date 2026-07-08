# R4 — Regolatorio DELIVERY / BVLOS: ricerca approfondita con fonti reali

> **Firmamento Technologies — Progetto HALE / servizio Aree Interne (caso pilota Pentema, Torriglia GE)**
> **Autore:** Regulatory Counsel (EASA / ENAC / U-Space) · **Data:** 2026-07-08
> **Scopo:** confermare/aggiornare il quadro regolatorio della **consegna medicale BVLOS** con documenti ufficiali e **precedenti reali**, oltre le basi già nel repo (Reg. 947/945/664, SORA 2.5 ED-2025-018-R).
> **Metodo:** WebSearch estensivo (EASA, AESA, ENAC, Osservatorio PoliMi, IATA/ICAO, operatori) + fonte primaria locale SORA 2.5. **Nota d'accesso:** in questa sessione **WebFetch e curl sono bloccati** (origin anti-bot + policy egress); le estrazioni derivano dagli snippet WebSearch (contenuto attribuito con URL) e dal file SORA locale. Fonti salvate in `ricerca-approfondita/fonti/`.

---

## 1. Percorso regolatorio reale della CONSEGNA MEDICALE (sintesi)

La consegna medicale a un borgo montano attraversa **quattro binari autorizzativi**, tutti confermati da fonti ufficiali:

1. **Categoria: sempre Specific (mai Open).** Art. 4 Reg. (UE) 2019/947 vieta in Open sia il trasporto DG sia il rilascio di materiale. Salto in **Certified** solo se: assembramenti / trasporto persone / **DG ad alto rischio** (art. 6). [FATTO, high]
2. **SORA 2.5 (ED Decision 2025/018/R, in vigore 15/09/2025)** per il rischio operazione → SAIL. Le **merci pericolose sono FUORI scope** (§S.1.3(c), verbatim: include "hazardous medical samples") → serve **dimostrazione di contenimento** (rif. GM1 Art. 2(11)). [FATTO PRIMARIO, high]
3. **Autorizzazione merci pericolose ENAC** (Reg. APR Ed.3 §4.5), separata dalla SORA, su carico DG (UN3373). [FATTO, high]
4. **Riduttori d'onere**: **STS-02** (C6, BVLOS controlled ground area) o **PDRA-G01** (BVLOS long-range **cargo**, area scarsamente popolata) **se** la tratta rientra nei loro vincoli — altrimenti **SORA piena**. **Nessuno STS "delivery" su area popolata è adottato** (→ Certified per quel caso). [FATTO, high]

**Classificazione DG del carico (decide il regime):**
| Carico | Classe | Regime |
|---|---|---|
| Farmaci/dispositivi/DPI comuni | Non-DG | Solo SORA + contenimento base |
| **Sangue/campioni diagnostici** | **UN3373 Cat. B, 6.2** | DG basso rischio → **autorizz. ENAC + contenimento (PI650)**; **resta Specific** |
| Ghiaccio secco (refrig.) | UN1845, Cl.9 | DG basso rischio → autorizz. |
| **Patogeni Cat. A** | UN2814/UN2900 | Alto rischio → **possibile Certified (art.6)** → **escludere dal ConOps** |

**SAIL realistico consegna medicale Pentema:** **II** se transito remoto (<5–50 ab/km²) + drop-zone controllata + geofencing stretto + M1(A) sheltering + M2/BRS; **III–IV** se l'approccio finale sorvola stabilmente l'abitato o il buffer tocca Torriglia. **[STIMA, medium]** — sensibilissimo al ConOps, da chiudere in pre-app ENAC.

**Precedente reale che valida la fattibilità in Specific:** **ABzero** — luglio 2024 ENAC autorizza **per la prima volta** una rotta drone per trasporto biomedicale (**37 km, Patti–Eolie**), contenimento **Smart Capsule**, consulente **EuroUSC Italia**. Autorizzazioni **rotta-per-rotta** (non LUC). [FATTO, high]

**Chiave PI650 (novità):** per UN3373 la **Packing Instruction 650** rimuove l'obbligo di conformità a quasi tutte le provisioni IATA-DGR (eccetto PI650: tripla imballatura) e **non richiede NOTOC**. Ma per gli **UAS** l'autorità nazionale **richiede comunque** un'approvazione DG con safety case, e il quadro DG-per-UAS è **novello/incerto** (UPDWG, MDPI). → il contenimento (Smart-Capsule-like) è **necessario e sufficiente in Specific**, ma l'iter DG-ENAC resta un onere non azzerabile.

---

## 2. LUC — costo/tempo reale (verifica stima €150–400k)

- **Cosa concede** (3 privilegi graduali, EASA UAS.LUC.060): (1) STS senza dichiarazione; (2) **auto-autorizzare PDRA**; (3) **auto-autorizzare TUTTE** le operazioni. Concessione graduale sul track-record (~6 mesi). Serve **SMS + Operations Manual + accountable manager + compliance monitoring**; tipicamente **≥3 operazioni Specific approvate** prima di candidarsi.
- **Fee autorità**: **~€3.220** (Cyprus CAA) — sola tassa, variabile per Stato. **Non** è il costo dell'organizzazione.
- **Verifica €150–400k report 13:** la cifra si riferisce al **build organizzativo permanente** (SMS + accountable manager + compliance monitor + OM + registri + personale dedicato), non alla fee. **Plausibile come ordine di grandezza** (base-rate SMS aeronautico) ma **non è un dato pubblicato** → **confidenza medium**.
- **Precedente decisivo:** **Amazon ha RINUNCIATO alla certificazione LUC in Italia** (dic 2025), spostandola in altro Stato UE. Se persino Amazon differisce/abbandona il LUC italiano, la tesi report 13 "**LUC = cerniera di scala Y3+, non porta d'ingresso**" è **rafforzata** → **medium-high**.

---

## 3. Verifica "23 operatori BVLOS" e stato U-Space

- **"23 BVLOS 2023" — VERIFICATO con correzione**: Osservatorio Droni PoliMi: nel 2023 **ENAC ha emesso 23 autorizzazioni operative in categoria Specific per BVLOS** (da **27 nel 2022**). Sono **autorizzazioni**, **non "operatori"** → correggere nei report 20/21. Numero esiguo e **in calo** → l'autorizzazione BVLOS è **asset scarso** (supporta la tesi "wrapper autorizzativo = moat"). Il 51% degli attori indica la **normativa come primo ostacolo**. **[high]**
- **U-Space Italia — AGGIORNATO**: **San Salvo (Abruzzo) operativo dal 1 gen 2026**, **primo in Europa** (~300 km², tetto 120 m AGL, spazio non controllato). **D-Flight** (ENAV+Leonardo) prima in Europa con **doppia certificazione USSP+CISP** (feb 2025). Regolamento ENAC U-Space Ed.1 **in consultazione** (gen 2026). **Amazon**, anchor tenant, **ha sospeso** Prime Air Abruzzo (dic 2025). → per Pentema **U-Space non è prerequisito nel breve** (conferma report 04/13); rilevante solo Y3+ con rotte fisse. **[high]**

---

## 4. TABELLA claim → fonte → verdetto → confidenza aggiornata

| # | Claim (report 12/13) | Fonte reale (URL) | Verdetto | Confidenza (prima → dopo) |
|---|---|---|---|---|
| 1 | Nessuno **STS "delivery"** su area popolata adottato; delivery popolata → Certified | EASA STS + droneregler.dk (`easa-sts-01-02-no-delivery.md`) | **CONFERMATO** | medium → **high** |
| 2 | **STS-02** (C6) vicino al transito rurale ma vincolo "controlled ground area" lo rende inadatto alla rotta di consegna | BCN Drone Center; uasolutions | **CONFERMATO** | medium → **high** |
| 3 | Esistono **PDRA** rilevanti al cargo BVLOS rurale (report 13 incerto su numeri) | AESA ES; Murzilli; BAZL; avtrain (`easa-pdra-lista.md`) | **PRECISATO**: PDRA-G01 = "long range **cargo**" (BVLOS, area scars. popolata, ≤3 m, ≤34 kJ, ≤150 m, ARC-a/spazio segregato, SAIL II); PDRA-S02 = "short range cargo". **Ma** non risolvono drop su borgo né DG | medium (parziale) → **medium-high** |
| 4 | **SORA 2.5** esclude le merci pericolose ("hazardous medical samples") dallo scope → serve **contenimento** | Fonte primaria locale `annex_...2025-018-r_1.md` §S.1.3(c) r.311–315 (`sora25-dg-scope-primaria.md`) | **CONFERMATO (verbatim)** | high → **high** |
| 5 | **UN3373 Cat. B** = DG basso rischio → **Specific** (non Certified); **Cat. A** → possibile Certified | UPDWG; MDPI Drones 10.3390/drones10020113; Sassofia; Intelsius (`un3373-dangerous-goods-uas.md`) | **CONFERMATO** + PI650 alleggerisce ma non azzera l'approvazione DG-UAS (quadro immaturo) | medium-high → **high** |
| 6 | **SAIL** consegna medicale Pentema **II–IV** | SORA 2.5 tabelle (repo `04`); benchmark ABzero/Matternet | **INVARIATO** (stima, dipende dal ConOps) | medium → **medium** |
| 7 | **LUC** dà auto-autorizzazione multi-missione (UAS.LUC.060) | EASA LUC (`easa-luc-costo-tempo.md`) | **CONFERMATO** | high → **high** |
| 8 | **LUC costo €150–400k / 12–24 mesi** | Cyprus CAA fee €3.220; Unmanned Value; eudroneport | **PARZ. CONFERMATO**: fee ~€3–5k; €150–400k = build organizzativo (stima non pubblicata) | medium → **medium** |
| 9 | **LUC solo Y3+, non porta d'ingresso** | Amazon rinuncia LUC IT (dic 2025) — ENAC/IlSole24Ore (`uspace-san-salvo-amazon-2026.md`) | **RAFFORZATO** | medium → **medium-high** |
| 10 | Precedente reale delivery medicale BVLOS in Italia (**ABzero**), in Specific | EuroUSC Italia; Air Cargo Italy; DronEzine (`abzero-enac-eolie-precedente.md`) | **CONFERMATO** (Patti–Eolie, lug 2024, 37 km, Smart Capsule) | media → **high** |
| 11 | **"23 operatori BVLOS Italia 2023"** | Osservatorio Droni PoliMi via automazione-plus/osservatori.net (`osservatorio-droni-23-bvlos-2023.md`) | **CONFERMATO con correzione**: 23 **autorizzazioni** BVLOS (non operatori), da 27 nel 2022 | citato → **high** |
| 12 | **U-Space** non obbligatorio; Italia embrionale | ENAC comunicato; droneoperator.it; Quadricottero (`uspace-san-salvo-amazon-2026.md`) | **AGGIORNATO**: San Salvo operativo 1-1-2026 (1ª zona EU); non obbligatorio salvo designazione; non copre Pentema | medium → **high** |
| 13 | Merci pericolose richiedono **autorizzazione ENAC** (§4.5) | Reg. ENAC APR Ed.3 (repo) + posizione CAA/EASA (Sassofia) | **CONFERMATO** | high → **high** |

---

## 5. Implicazioni e domande da chiudere in pre-application ENAC

**Cosa cambia rispetto ai report 04/13:**
- **Esistono PDRA cargo** (G01 long-range, S02 short-range): valutare se la **tratta rurale** di Pentema vi rientra per **evitare la SORA piena** — ma il **drop sul borgo** e il **DG** restano fuori.
- **U-Space non più "embrionale"** ma con **una zona operativa (San Salvo)**: modello nazionale in consolidamento, non ancora utile all'Appennino ligure.
- **Segnale Amazon** (rinuncia delivery+LUC IT): la scala della delivery-BVLOS in Italia è **più dura del previsto** → prudenza su tempi e sul LUC.
- **ABzero** è insieme **prova di fattibilità** e **competitor incumbent** con track-record ENAC 2024.

**Domande aperte (pre-app M+0–3):**
1. La tratta di consegna Pentema rientra in **PDRA-G01/S02** (evita SORA piena) o serve SORA completa?
2. Quale **dimostrazione di contenimento** ENAC richiede per **UN3373** (Smart-Capsule-like) e quale iter **autorizzazione DG** (§4.5)?
3. Drop-zone controllata tiene **SAIL II–III** o l'approccio sull'abitato spinge a **IV**?
4. Soglia di volumi/varietà oltre cui ENAC vede il **LUC** come via preferenziale; tempi reali in Italia (alla luce del ritiro Amazon).
5. Orizzonte di una **designazione U-Space** utile a rotte di consegna nell'Appennino (post-Regolamento ENAC U-Space Ed.1).

---

### Fonti salvate (`ricerca-approfondita/fonti/`)
`easa-pdra-lista.md` · `easa-sts-01-02-no-delivery.md` · `easa-luc-costo-tempo.md` · `un3373-dangerous-goods-uas.md` · `abzero-enac-eolie-precedente.md` · `osservatorio-droni-23-bvlos-2023.md` · `uspace-san-salvo-amazon-2026.md` · `sora25-dg-scope-primaria.md`
Base repo: `fonti/CELEX_32019R0947_IT_TXT.md`, `fonti/annex_to_ed_decision_2025-018-r_1.md`, `fonti/Regolamento_APR_Ed_3_Emend_1.md`, `fonti/CELEX_32021R0664_IT_TXT.md`.
