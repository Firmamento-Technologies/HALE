# R6 — Box-wing / Joined-wing / PrandtlPlane: verifica della letteratura reale ai claim del report 22

> **Volume:** Ricerca approfondita (fonti accademiche scaricate/verificate) a supporto di `analisi-bottom-up/22-boxwing-vantaggio-tecnico.md`
> **Data:** 8 luglio 2026
> **Autore:** Aerodynamics & Structures Engineer
> **Metodo:** WebSearch su Google Scholar/AIAA/ScienceDirect/Springer/arXiv/IOP + estrazione di numeri e citazioni. **Limite di ambiente:** WebFetch/curl bloccati dall'egress policy sui domini editoriali (arxiv, springer, icas, purdue, wiley): i full-text non sono stati scaricati in locale; le evidenze provengono dagli **abstract/estratti indicizzati** e dai metadati (autori/DOI/venue verificati). Fidelity delle fonti: **peer-reviewed L1-L2 teorico/computazionale; nessuna galleria/volo su box-wing UAV C3.**
> **Fonti salvate:** `ricerca-approfondita/fonti/*.md` (12 schede)

---

## 0. Sintesi in una riga

La letteratura reale **conferma il report 22** su tutti e sei i claim, con **una precisazione che rende il verdetto aerodinamico ancora più netto per la nicchia** e **due raffinamenti** (il crossover Reynolds coincide con la crociera C3 → è genuinamente marginale e CD0-sensibile; l'aeroelasticità joined-wing è un rischio metodologico reale ma scala con la deformabilità → basso a C3, dominante su HALE). **Nessun claim del report 22 è falsificato.**

---

## 1. Tabella claim → fonte → verdetto → confidenza aggiornata

| # | Claim del report 22 | Fonte(i) reale(i) — DOI/URL | Cosa dice la fonte | Verdetto | Confidenza (era → ora) |
|---|---|---|---|---|---|
| **1a** | Prandtl best wing system: box a pari apertura minimizza l'indotta; e_box ≈ 1.46 a h/b=0.2; riduzione indotta 22–40% al crescere di h/b | Kroo, *Nonplanar wing concepts* (VKI 2005); Demasi, *J. Aircraft* 44(1):81–99 (2007), **10.2514/1.21884** | Box "outperformed all others, e ≈ **1.46**" a **h/b=0.2**; monoplano ideale e=1.0. Teoria variazionale conferma il minimo di Prandtl. | **CONFERMATO (teoria)** | media → **alta** |
| **1b** | Il ~30–40% "da brochure" è reale ma **solo sull'indotta, a pari apertura**, non sul drag totale | Abu Salem, Palaia, **Frediani**, Carrera, *Progress in Aerospace Sciences* 157:101108 (2025), **10.1016/j.paerosci.2025.101108** | "up to **43% less induced drag**" ma su **airliner transonico** ottimizzato a h/b≈0.2, vs tube-and-wing, **sull'indotta** | **CONFERMATO** — anche la fonte pro-PrandtlPlane colloca il guadagno nel regime indotta-dominato (transonico/alto CL), non nella crociera lenta | media → **alta** |
| **2** | Il guadagno **svanisce** per un VTOL cargo C3 in crociera lenta attrito-dominata; box vince solo se indotta > attrito | Box-wing vs mono UAV, arXiv 2112.02872 / **AIAA 2025-0256** (**10.2514/6.2025-0256**); *J. Phys. Conf. Ser.* 2235:012070 (**10.1088/1742-6596/2235/1/012070**) | "advantageous **when induced drag is higher than friction drag**"; "**higher total drag due to higher parasitic drag**… lower total L/D than conventional at lower total lift"; crossover a **Re ≈ 4×10⁵** | **CONFERMATO** (vedi §2 per la precisazione critica sul Re) | media → **alta** |
| **3a** | Vantaggio strutturale bracing reale ma **conteso/piccolo** a scala C3 | Wolkovitch, *J. Aircraft* 23(3):161–178 (1986), **10.2514/3.45285** | Rigidezza alta (torsione di un'ala resistita dalla flessione dell'altra), **ma join tip-to-tip può essere più pesante** di un'ala convenzionale di pari apertura | **CONFERMATO** — proprio il box tip-to-tip (caso BOXY) è il topologicamente peggiore per il peso | media → **medio-alta** |
| **3b** | Buckling della membratura compressa ri-aggiunge massa; gap aero peggiora il peso | *Review of Structural Issues in the Design of a Box Wing Aircraft* (JAEM 2019); *HALE joined-wing structural*, **10.1155/ijae/9931529** | Buckling dell'ala posteriore è requisito dimensionante ("additional weight necessary"); **tail height** (gap) è il driver #1 del peso; risparmio 24.1% **vs flying wing** (non vs monoplano) e sotto vincolo 10% deflessione | **CONFERMATO** — il risparmio di massa citato in letteratura è vs flying wing high-AR, **non trasferibile** al C3 | media → **medio-alta** |
| **4** | Aeroelasticità joined-wing (flutter accoppiato/buckling/snap) = rischio reale ma gestibile a C3, **da dimostrare** | Cavallaro & Demasi, *Progress in Aerospace Sciences* 87:1–93 (2016), **10.1016/j.paerosci.2016.07.002**; snap-divergence *J. Fluids & Structures* 2015, **10.1016/j.jfluidstructs.2015.01.006** | Layout **iperstatico**; **snap-buckling/snap-divergence**; la divergenza da eigenvalue lineare può essere "**unreliable and even nonconservative**"; LCO/flutter. Fenomeni studiati per config **"highly deformable"** | **CONFERMATO + raffinato**: è un rischio **metodologico** (il check lineare non basta) che **scala con la deformabilità** → basso a C3 rigido, **dominante su HALE high-AR** | media → **alta** (sul fatto che sia rischio reale) |
| **5** | Esistono UAV/PrandtlPlane box-wing reali (IDINTOS ecc.) | Frediani et al., IDINTOS, *AMS* 2015 **10.1007/BF03404701**; final design **10.1007/BF03404721** | Prototipo PrandtlPlane full-scale **costruito e volato** (in scala); manned VLA | **CONFERMATO** — ma i casi maturi sono **manned ultraleggeri**, non UAV cargo C3 | alta → **alta** |
| **6** | Config box-wing = arte nota, nessun moat IP forte | US 3,834,654 (Lockheed 1974, **scaduto**); Wolkovitch 1986; brevetti PrandtlPlane Frediani su implementazioni specifiche; Prandtl 1924 | Concetto pubblico da 100 anni; boxplane fondativo scaduto; solo implementazioni specifiche brevettabili | **CONFERMATO** | alta → **alta** |

---

## 2. Il punto che merita attenzione: il crossover Reynolds coincide con la crociera C3

La scoperta più rilevante della ricerca è **quantitativa**. Lo studio su piccoli UAV (*J. Phys. Conf. Ser.* 2235:012070) trova che il box-wing **inizia a superare il mono-wing oltre Re ≈ 4×10⁵**, perché lì il guadagno sull'indotta supera l'incremento di attrito. Il report 22 aveva calcolato per la baseline C3 una **crociera a Re ≈ 4.7×10⁵**.

**I due numeri quasi coincidono.** Ne segue una lettura più precisa di quella del report 22:

- Il verdetto aerodinamico **non è "il box perde"**, ma **"è genuinamente marginale e il segno dipende dal CD0 dell'airframe"**. Questo è esattamente ciò che il report 22 dichiara nella banda −5%…+8% e nella caveat #3 ("airframe pulito"). La letteratura **conferma il framework e ne indica il fulcro**: la pulizia aerodinamica.
- Per un UAV box-wing **pulito** (come quello dello studio IOP — ala liscia, senza rotori esposti) il box può **già pareggiare/vincere** a Re≈4–5×10⁵.
- Per il **VTOL delivery C3 reale** (rotori lift+cruise esposti, CD0≈0.040, penalità di download in hover) l'airframe è "sporco": il crossover si sposta a CL più alti e **il mono resta avanti in crociera**, mentre la penalità di superficie bagnata delle paratie (confermata da entrambe le fonti UAV) e il download in hover lavorano contro il box.

**Conseguenza per il verdetto:** l'affermazione del report 22 "≈0% netto, probabile leggera penalità" è **corretta e ben calibrata per il caso VTOL sporco**, ma la letteratura suggerisce che la stima centrale potrebbe essere **leggermente pessimista per un airframe pulito**. Il segno esatto è **indecidibile a L0/L1**: va risolto con **CFD RANS transizionale (γ-Reθ) a L2**, esattamente la porta d'ingresso obbligata indicata dal report 22. Il messaggio strategico non cambia: **nessun edge aerodinamico decisivo per la nicchia C3.**

---

## 3. La verità sull'aeroelasticità joined-wing (claim 4)

La letteratura Cavallaro-Demasi è **la più autorevole** sul tema e va letta con precisione:

1. **Il fenomeno è reale e peculiare**, non FUD: layout iperstatico, **snap-buckling** e **snap-divergence**, LCO, biforcazioni non-lineari. La configurazione è genuinamente più complessa di un monoplano.
2. **Il rischio metodologico è il vero costo:** la previsione di divergenza con **eigenvalue lineare** può essere **non-conservativa**. Non ci si può fidare di una clearance flutter/divergenza "classica"; serve **analisi non-lineare geometricamente esatta + GVT**. Questo **aggiunge effort a L3** (coerente con lo showstopper S4 e i costi §5 del report 22).
3. **Scala con la deformabilità.** Gli studi parlano di joined-wing **"highly deformable"**. Un box-wing C3 (apertura ≤3 m, rigido, V≈20–30 m/s) ha Vf verosimilmente ben sopra Vd → **rischio basso ma da dimostrare**, mai da assumere. Il report 22 lo inquadra correttamente.

**Implicazione trasversale per Firmamento (fuori mandato C3 ma rilevante):** lo **stesso** fenomeno aeroelastico che è benigno a scala C3 diventa **dominante e potenzialmente fatale** su un'ala **HALE high-AR** (il Percorso 6B). Diversi dei paper trovati sono infatti su **joined-wing/closed-wing HAPS** (J. Aircraft 10.2514/1.C038477; AIAA 2025-0461; CIRA). Se Firmamento cercasse un differenziatore box-wing, il terreno tecnicamente coerente è l'**HALE**, non il VTOL C3 — ma lì l'aeroelasticità non-lineare è un rischio di primo ordine e c'è già un precedente nazionale (CIRA) → da girare a `competitor-intelligence` e all'analisi 6B.

---

## 4. Verdetto: il report 22 è CONFERMATO

**Il report `22-boxwing-vantaggio-tecnico.md` è confermato dalla letteratura reale, e va rafforzato — non rivisto — su tre punti.** Nessuna conclusione è falsificata.

- **Aerodinamica (§1 report 22): confermato.** Il 22–43% di riduzione dell'indotta è reale (Kroo, Demasi 2007, Frediani 2025) ma **solo sull'indotta, a pari apertura, in regime indotta-dominato** (transonico/alto CL). In crociera lenta C3 attrito-dominata il netto sul drag totale è marginale e, per un airframe VTOL sporco, tendenzialmente sfavorevole (arXiv 2112.02872/AIAA 2025-0256; IOP 2235:012070). **Raffinamento:** il crossover Re≈4×10⁵ ≈ crociera C3 → è un pareggio CD0-sensibile, da risolvere a L2, non un edge.
- **Struttura (§2): confermato.** Il risparmio di massa da bracing è reale ma (a) misurato **vs flying wing high-AR**, non vs monoplano; (b) eroso dal buckling della membratura compressa e dal peso del gap; (c) **≤2% MTOM = trascurabile a scala C3**. Il join **tip-to-tip** (caso BOXY) è il peggiore per il peso (Wolkovitch).
- **Aeroelasticità (§3/§5): confermato e precisato.** Rischio reale (snap-divergence, check lineare non-conservativo → effort L3), ma **gestibile a C3 perché scala con la deformabilità**. Non showstopper fisico a C3; showstopper potenziale su HALE.
- **IP (§4): confermato.** Arte nota (Prandtl 1924, Lockheed 1974 scaduto, Wolkovitch 1986, PrandtlPlane Frediani su implementazioni). **Nessun moat.**

### Confidenza aggregata
- Report 22 dichiarava **LOW-MEDIUM**.
- Dopo triangolazione con ≥12 fonti peer-reviewed (di cui una review 93-pagine e una review 2025 a firma Frediani, cioè **non ostili** alla configurazione): **la confidenza sulla direzione del verdetto sale a MEDIO-ALTA.**
- **Resta L1/L2-limitata sul numero esatto del Δ crociera** (segno −5%…+8%): nessuna fonte fornisce CFD transizionale o galleria su un box-wing **VTOL cargo C3 sporco** specifico. Quel numero richiede L2 dedicato.

### Raccomandazione invariata
Per la nicchia delivery C3, **adattare un fixed-wing VTOL COTS** batte lo sviluppo box-wing proprietario. Il box-wing va tenuto come **eventuale dimostratore/vetrina IP**, non come base di prodotto. Se mai si vorrà un differenziatore box-wing, **il contesto tecnicamente sensato è l'HALE 6B** (regime indotta-dominato high-AR), dove però l'aeroelasticità non-lineare è un rischio di primo ordine e il CIRA è già un precedente.

---

## 5. Gap di evidenza (onestà epistemica)

1. **Nessun full-text scaricato in locale** (egress policy blocca i domini editoriali): evidenze da abstract/estratti indicizzati + metadati verificati (DOI/venue/autori). Confidence sui *numeri puntuali* interni ai paper: media; sui *metadati e conclusioni qualitative*: alta.
2. **Nessuna galleria del vento né CFD transizionale su un box-wing VTOL cargo C3 sporco specifico** esiste in letteratura → il segno del Δ crociera resta L1-aperto.
3. **Download in hover del box-wing VTOL** (showstopper S2 del report 22) **non è coperto** da nessuna delle fonti trovate → resta la stima a confidence più bassa; richiede URANS/attuatore-disco (L2).
4. La penalità di novità in **certificazione C3** (Notified Body) non è un tema aerodinamico e non è verificabile con letteratura tecnica.

---

## 6. Elenco fonti (12 schede in `fonti/`)

1. `crossover-boxwing-vs-monowing-uav-scitech2025.md` — arXiv 2112.02872 / AIAA 2025-0256 (**10.2514/6.2025-0256**)
2. `boxwing-uav-iop-conf-2022-crossover-Re.md` — J. Phys. Conf. Ser. 2235:012070 (**10.1088/1742-6596/2235/1/012070**)
3. `demasi-2007-min-induced-drag-closed-wings.md` — J. Aircraft 44(1):81–99 (**10.2514/1.21884**)
4. `abu-salem-frediani-boxwing-critical-review-2025.md` — Prog. Aero. Sci. 157:101108 (**10.1016/j.paerosci.2025.101108**)
5. `kroo-nonplanar-wing-concepts.md` — Kroo, VKI 2005 (e≈1.46 @ h/b=0.2)
6. `cavallaro-demasi-joinedwing-review-2016.md` — Prog. Aero. Sci. 87:1–93 (**10.1016/j.paerosci.2016.07.002**)
7. `cavallaro-demasi-snap-divergence-2015.md` — J. Fluids & Struct. (**10.1016/j.jfluidstructs.2015.01.006**)
8. `wolkovitch-joined-wing-overview-1986.md` — J. Aircraft 23(3):161–178 (**10.2514/3.45285**)
9. `review-structural-issues-boxwing-buckling.md` — JAEM 2019 (buckling rear wing)
10. `joined-wing-hale-structural-mass-24pct.md` — IJAE 2025 (**10.1155/ijae/9931529**) + CJA hi-fidelity
11. `idintos-prandtlplane-prototype-frediani.md` — AMS 2015/2016 (**10.1007/BF03404701**, **/BF03404721**)
12. `patents-boxplane-prandtlplane-prior-art.md` — US 3,834,654 (Lockheed 1974, scaduto) + Frediani/Wolkovitch
13. `closed-wing-HAPS-jaircraft-CIRA.md` — J. Aircraft **10.2514/1.C038477**, AIAA **2025-0461** (rilevanza HALE 6B/competitor CIRA)
