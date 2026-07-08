# 02 — Osservazione della Terra (EO): quali servizi, quale piattaforma minima

**Analisi bottom-up per le Aree Interne italiane (focus Liguria montana, caso pilota Pentema — Torriglia, GE)**
Autore: Earth Observation Payload Expert · Data: 2026-07-08 · Progetto HALE / Firmamento Technologies

> **Metodo.** Si parte dal *servizio* (fabbisogno reale del territorio), non dalla piattaforma. Per ciascun servizio si derivano i requisiti EO (GSD, banda spettrale, rivisitazione/persistenza, area), si individua la **piattaforma minima** che li abilita e si confronta bottom-up con i **sostituti dominanti**: satellite Copernicus (gratuito), satellite commerciale (a pagamento), drone COTS a noleggio (<25 kg), infrastruttura fissa a terra. Ogni servizio è sottoposto a **falsificazione**: "esiste già un sostituto che lo fa meglio/più economico?". Solo ciò che sopravvive alla falsificazione giustifica una piattaforma aerea *dedicata*.

---

## 1. Contesto territoriale (fatti)

| Dato | Valore | Fonte | Conf. |
|---|---|---|---|
| Aree Interne Liguria (SNAI 2014-27) | 8 aree, ~118 comuni, ~203.000 ab., ~3.050 km² | `Aree interne/rapporto-istruttoria_regione-liguria.md` (Tab. 2) | alta |
| Area singola (perimetro) | 185–442 km² (es. Fontanabuona 185, Imperiese 442) | ibid. | alta |
| Copertura **forestale** dominante | 77% Imperiese, 80% Fontanabuona, 85% Valle Scrivia, **90% Val Bormida** | ibid. | alta |
| Densità abitativa | 31–82 ab/km² (spopolamento -5…-8% 2011-20) | ibid. | alta |
| Caso pilota | Pentema, frazione di Torriglia, area **Antola-Tigullio** (16 comuni) | CLAUDE.md; rapporto istruttoria | alta |
| Priorità nazionali EO per Aree Interne | **rischio idrogeologico/frane** (PNRR M2C4, €500M) e **incendi boschivi** (fondo dedicato Aree Interne) | `Aree interne/psnai_finale_30072025_clean_ministro.md` (righe 1194, 1470-1490, 5185-5195) | alta |
| Vincoli operativi | orografia complessa, valli strette, elevata copertura nuvolosa invernale | rapporto istruttoria + geografia nota | alta |

**Implicazione di partenza:** il territorio è *piccolo* (aree di poche centinaia di km²), *forestato* (decorrelazione radar e occlusione ottica del suolo) e *frammentato*. Questi tre fattori pesano molto sul confronto tra piattaforme.

---

## 2. Requisiti EO e GSD alle tre quote (calcolo)

Formula: **GSD [m] = (h × pixel_size) / focal_length**. Assunzioni sensore dichiarate in tabella.

| Piattaforma / quota | Sensore RGB (assunzioni) | GSD RGB | Sensore LWIR (12 µm, 640px) | GSD termico | Swath ottico |
|---|---|---|---|---|---|
| **Drone COTS @ 120 m AGL** | 24 MP, pixel 3.3 µm, f=24 mm | **~1,7 cm** | f=13 mm | ~11 cm | ~0,18 km |
| **VTOL @ 1.500 m AGL** | iXM-100, pixel 4.6 µm, f=150 mm | **~4,6 cm** (2–9 cm con 80–300 mm) | f=25 mm | ~0,72 m | ~0,35 km |
| **HALE @ 20 km** | iXM-100, pixel 4.6 µm, f=300 mm | **~31 cm** (0,3–0,5 m) | f=100 mm | ~2,4 m | ~2,9 km |

**Note fisiche (obbligatorie):**
- A **20 km nel visibile** con ottica f=300 mm f/4 (apertura 75 mm) il limite di Rayleigh a λ=0,5 µm dà ~0,16 m a terra: il sistema è **resolution-limited** (sensore), *non* diffraction-limited. La GSD 0,3 m è quindi realizzabile.
- Nel **LWIR a 20 km** (λ=10 µm) il sistema è invece prossimo al **limite di diffrazione**: un'apertura da 100 mm dà ~2,4 m a terra. È il limite fisico, non migliorabile con più pixel.
- **Detection ≠ risoluzione (information resolution).** Un focolaio incipiente di 1 m² è sub-pixel a 2,4 m, ma la sua altissima temperatura satura la radianza dell'intero pixel: la *rilevabilità* di un hotspot non richiede che il fuoco riempia il pixel (stesso principio con cui VIIRS a 375 m rileva incendi molto più piccoli). Questo separa nettamente "vedo la fiamma" da "misuro l'area bruciata".

---

## 3. Matrice servizio → requisiti → piattaforma minima → verdetto

Legenda persistenza: **spot** = una passata; **periodica** = giorni/settimane/mesi; **continua** = loitering h24 su area.

| # | Servizio | GSD target | Banda | Rivisitazione / **persistenza** | Area tipica | **Piattaforma minima** che lo abilita | Sostituto dominante | **Verdetto piattaforma dedicata** | Conf. |
|---|---|---|---|---|---|---|---|---|---|
| 1a | **Frane — deformazione lenta** (mm-cm/anno, wide-area) | ~100 m (punti PS) | **SAR (DInSAR)** | periodica (6-12 gg / annuale) | intera area 200-3.000 km² | *nessuna aerea* | **EGMS Copernicus** (gratis, 100 m, mm/anno, Sentinel-1) + PST-A/IdroGEO ISPRA | **DOMINATO da satellite gratuito.** Scartare. | alta |
| 1b | **Frane — fronte attivo, mappatura di dettaglio** | ≤0,1–0,2 m + DTM | RGB stereo + **LiDAR** | periodica (settimanale in stagione piovosa) | 0,1–10 km² (sito noto) | **Drone COTS** (RGB+LiDAR) | drone a noleggio; GB-InSAR per il singolo fronte | **DOMINATO da drone spot.** Fenomeno lento → persistenza h24 inutile. Scartare la piattaforma dedicata. | alta |
| 1c | **Frane — early-warning collasso imminente** (evento) | qualitativo | RGB/termico + estensimetri | **continua durante l'evento** | singolo versante <1 km² | loitering (MALE/VTOL/aerostato) | **sensori in-situ** (estensimetri, GB-InSAR, pluviometri) — molto più economici e affidabili di notte/nuvole | **DOMINATO da sensoristica a terra.** Nicchia residua marginale. | media |
| 2a | **Incendi — mappatura post-evento** (severità, dNBR) | 10–20 m | **Multispettrale (NBR/SWIR)** | spot post-evento (giorni) | area percorsa | *nessuna aerea* | **Sentinel-2** (gratis, 10-20 m, NBR) + Copernicus EMS | **DOMINATO da satellite gratuito.** Scartare. | alta |
| 2b | **Incendi — early detection su area a rischio** | ≤5 m termico | **RGB + LWIR** | **continua (finestre estive/red-flag)** + latenza ≤5 min | area/valle 50-400 km² | **loitering persistente** (MALE-class, aerostato frenato, o rete di **torri fisse**) | VIIRS/FIRMS gratis ma **375 m, 2×/giorno, latenza ore** → non early; torri camera fisse su crinale (economiche) | **SPAZIO REALE ma conteso.** Persistenza + bassa latenza è il discriminante. Ma torri fisse + standby coprono gran parte del valore a costo minore. | media |
| 3a | **Agricoltura di precisione** (NDVI/NDRE) | 3–10 m (regionale) / ≤0,1 m (plot terrazzati) | **Multispettrale + termico** | periodica (quindicinale) | campi frammentati | **Sentinel-2** (regionale) / **drone COTS** (plot) | Sentinel-2 gratis 5 gg; drone multispettrale a noleggio | **DOMINATO.** Nessun bisogno di persistenza. Scartare. | alta |
| 3b | **Selvicoltura / castanicoltura / carbon** (Parco Aveto) | 10-20 m (stress) / LiDAR (biomassa) | Multispettrale + **LiDAR** | stagionale/annuale | stand forestali | Sentinel-2 + **drone/aereo LiDAR** + dataset nazionali | Sentinel-2 gratis; LiDAR nazionale ISPRA/MASE; drone LiDAR | **DOMINATO.** Fenologia lenta → no persistenza. Scartare. | alta |
| 4a | **Infrastrutture — ispezione ponti/viadotti** | ≤0,01 m | RGB close-range + LiDAR + termico | periodica (trimestrale + post-evento) | singola opera | **Drone COTS** (volo ravvicinato) | drone a noleggio (dettaglio) + Sentinel-1/EGMS (deformazione mm) | **DOMINATO da drone spot.** Scala metrica irraggiungibile dall'alto. Scartare. | alta |
| 4b | **Infrastrutture — corridoi (strade, linee elettriche)** | ≤0,05 m | RGB + LiDAR | periodica | corridoi lineari | **Drone COTS** corridor-mapping | drone/eli a noleggio; servizi utility esistenti | **DOMINATO da drone spot.** Scartare. | alta |
| 5 | **Supporto Protezione Civile in emergenza** (alluvione, incendio, SAR) | 0,1–0,5 m | **RGB + LWIR**, live downlink | **continua per la durata dell'evento** + bassa latenza | teatro d'evento | **loitering** (VTOL ibrido 6-10 h / MALE 12-30 h) | drone tattico VVF/PC (endurance 30-60 min) + Copernicus EMS (mappe in ore) | **SPAZIO REALE.** Persistenza + overwatch continuo. Ma eventi episodici → difficile giustificare asset *always-on* dedicato vs. VTOL in standby. | media |

---

## 4. Falsificazione: dove NON c'è spazio per una piattaforma dedicata

La domanda-chiave del pivot è: *dove il satellite gratuito o il drone a noleggio dominano, rendendo inutile una piattaforma aerea dedicata?* Risposta netta:

1. **Fenomeni lenti su vasta area** (deformazione frane mm/anno, stress vegetazione, biomassa/carbon) → **Copernicus è gratuito e sufficiente**. EGMS dà mm/anno a 100 m aggiornato annualmente; Sentinel-2 dà NDVI/NBR a 10 m ogni ~5 giorni. Una piattaforma persistente non aggiunge nulla: *non c'è niente da "sorvegliare h24" in un processo che si misura in mesi*. **Scartati: 1a, 2a, 3a, 3b.**
2. **Dettaglio spinto su sito puntuale** (fronte di frana, ponte, corridoio, plot terrazzato) → **il drone COTS a noleggio domina**: GSD 1-2 cm e LiDAR sotto-chioma da 120 m, costo di una giornata di rilievo €500-2.000, tecnologia TRL 9. La persistenza è irrilevante perché l'ispezione è point-in-time e programmabile. **Scartati: 1b, 4a, 4b.**
3. **Early-warning di frana** → i **sensori in-situ** (estensimetri, GB-InSAR, pluviometri, wire) sono più economici, funzionano di notte e sotto le nuvole (quando la frana è più probabile) e sono già la prassi normativa PAI. Un occhio aereo non sostituisce la strumentazione a terra. **1c marginale.**

**Il vero discriminante è la PERSISTENZA (loitering continuo su un'area), non la risoluzione né il costo.** Persistenza + bassa latenza è irraggiungibile sia dal satellite (che passa e va: Sentinel ogni 5-6 gg, commerciale su tasking in ore) sia dal drone-spot (endurance 30-60 min, dispiegato solo dopo che l'evento è noto). Ma la persistenza serve **solo a due servizi**: **2b (early detection incendi in finestra estiva)** e **5 (overwatch prolungato in emergenza PC)**. Ed **entrambi hanno sostituti più economici**: torri camera fisse su crinale (2b) e drone tattico in standby (5). Lo spazio è reale ma **stretto e conteso**.

---

## 5. Scala di piattaforma: chi abilita cosa (bottom-up)

| Classe | CapEx indicativo | Endurance | Persistenza su area | Copre i servizi… | Note |
|---|---|---|---|---|---|
| **Satellite Copernicus** (uso) | €0 (gratis) | — | no (5-6 gg) | 1a, 2a, 3a, 3b | Già disponibile, sovrano EU, nessun asset da comprare |
| **Drone COTS <25 kg** (acquisto/noleggio) | €5k-80k / €0,5-2k al giorno | 0,5-1,5 h | no | 1b, 3a(plot), 4a, 4b, 5(spot) | TRL 9, matura, economica, Open/Specific |
| **VTOL / fixed-wing ibrido** | €150k-400k | 6-10 h | parziale (finestra) | 2b, 5 (evento prolungato) | Loitering a mezza giornata; SAIL Specific BVLOS |
| **MALE** | €M (decine) | 12-30 h | sì (giornaliera) | 2b, 5 su scala regionale | Costo/regolatorio pesante per uso civile locale |
| **HALE** | €decine-centinaia M | settimane | sì (continua) | 2b, 5 su scala regionale-continua | **Swath 3 km/area 200 km²: capacità sprecata**; non finanziabile |
| *Alt. non-aerea:* **rete torri camera fisse** | €10k-50k/torre | h24 | sì (fisso) | 2b | Concorrente diretto e più economico dell'aereo per antincendio |

**Conclusione sulla classe minima:** per i pochi servizi che sopravvivono (2b, 5) la piattaforma minima abilitante è una **classe loitering a mezza giornata (VTOL ibrido/fixed-wing, 6-10 h)** — *non* MALE né HALE. HALE è sovradimensionato: uno swath da ~3 km e la capacità di coprire migliaia di km² sono *sprecati* su una valle di 200-400 km², a un costo che il pivot dichiara impossibile (centinaia di M€). Per la sola persistenza antincendio, la soluzione a minor costo è spesso **non aerea** (torri fisse).

---

## 6. Compliance (sintesi)

- **GDPR** (Reg. UE 2016/679): imagery su aree abitate → base giuridica + minimizzazione; Regione Liguria è già Titolare per i dati SNAI (`aree interne.md`, §9). Necessaria DPIA per EO ricorrente su abitato. Conf. alta.
- **Riprese aeree cartografiche** (autorizzazione ex normativa fotografia aerea / nulla-osta per uso commerciale in aree sensibili): da verificare per acquisizioni sistematiche. Conf. media.
- **ENAC/EASA**: drone COTS e VTOL in categoria Specific (SORA/BVLOS montano); MALE/HALE in categoria Certified o quadro HAPS non consolidato. Conf. alta.

---

## 7. Verdetto EO

1. **La maggioranza dei servizi EO utili alle Aree Interne è già coperta, gratis, da Copernicus** (frane wide-area via EGMS, post-incendio via Sentinel-2 NBR, agricoltura/foreste via Sentinel-2) **o, per il dettaglio, da un drone COTS a noleggio** (ispezione ponti/corridoi, plot agricoli, mappatura fronte-frana). Per questi, **una piattaforma aerea dedicata è dominata e va scartata**.
2. **Il solo fattore differenziante di una piattaforma aerea dedicata è la PERSISTENZA** (loitering continuo, bassa latenza), che abilita **(2b) early-detection incendi** e **(5) overwatch in emergenza Protezione Civile**. Non la risoluzione, non il costo.
3. **Anche questi due servizi hanno sostituti più economici** (torri camera fisse; drone tattico in standby), quindi lo spazio è reale ma stretto: giustifica al massimo una **classe VTOL/fixed-wing loitering 6-10 h**, non MALE né HALE.
4. **Raccomandazione EO:** posizionare l'offerta come *servizio* (DaaS) che **orchestra Copernicus (gratis) + drone COTS on-demand**, aggiungendo un layer di **persistenza loitering solo nelle finestre ad alto rischio** (estate antincendio, emergenze). Questo è finanziabile (<€1M per il layer drone/VTOL + software), mentre l'HALE dedicato all'EO locale non lo è.

---

## Fonti
- Territorio/needs: `Aree interne/rapporto-istruttoria_regione-liguria.md`; `Aree interne/psnai_finale_30072025_clean_ministro.md`; `Aree interne/aree interne.md`.
- Satellite (verificati web, lug. 2026): EGMS Copernicus — 100 m, mm/anno, aggiornamento annuale ([land.copernicus.eu](https://land.copernicus.eu/en/products/european-ground-motion-service)); Sentinel-1 revisita 6 gg ripristinata con S1C operativo mag. 2025 ([sentinels.copernicus.eu](https://sentinels.copernicus.eu/-/sentinel-1d-user-data-opening-and-future-plans)); VIIRS/FIRMS 375 m, 2×/giorno, latenza ~3 h ([earthdata.nasa.gov](https://www.earthdata.nasa.gov/data/catalog/lancemodis-vnp14img-nrt-2)).
- GSD/diffrazione: calcoli propri con formule e assunzioni sensore dichiarate (§2).
- Payload/piattaforme: conoscenza di dominio EO (Phase One iXM, MicaSense, Zenmuse L2/H20T, JOUAV CW-30E) + `studio-di-fattibilita/cap-06-analisi-tecnica.md` (letto criticamente, non assunto).

**Livelli di confidenza:** fatti territoriali e specifiche satellitari = **alta** (fonte primaria/verificata); calcoli GSD = **alta** (deterministici date le assunzioni); economia noleggio drone e giudizio sul valore della persistenza = **media** (stima ragionata, non misurata sul caso Pentema). Da falsificare con un pilota reale.
