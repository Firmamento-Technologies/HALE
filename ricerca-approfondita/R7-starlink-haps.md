# R7 — Ancoraggio con fonti reali: Sostituti connettività (Starlink) e capital-intensity HAPS

> **Progetto HALE — Firmamento Technologies**
> **Data:** 8 luglio 2026 · **Autore:** Telecom/NTN Payload Expert (Claude)
> **Mandato:** ricerca iper-approfondita con fonti reali per ancorare (a) i prezzi dei sostituti di connettività e (b) la capital-intensity dei programmi HAPS, a supporto/rettifica dei report `analisi-bottom-up/01-connettivita.md` e `analisi-bottom-up/05-piattaforme-costi.md`.
> **Skill applicate:** `epistemic-rigor` (source provenance, confidence levels, triangolazione).
> **Fonti salvate:** `ricerca-approfondita/fonti/*.md` (10 file, header con Titolo/URL/data/estratto).

---

## 0. Nota di metodo (vincolo dichiarato)

L'ambiente di lavoro instrada l'HTTPS attraverso un **egress proxy con policy restrittiva**: il download integrale delle pagine (WebFetch/curl) è stato **bloccato con 403** su tutti gli host esterni testati (starlink.com, wikipedia.org, cnbc.com, airbus.com, sceye.com, ecc. — verificato via `$HTTPS_PROXY/__agentproxy/status`). Il tool **WebSearch funziona** e restituisce snippet che **citano testualmente** le pagine target. Tutte le cifre qui sotto provengono da questi snippet, con URL della fonte primaria indicato. Dove una cifra non è stata verificabile su fonte primaria (es. costo cumulato di programma non divulgato), è marcata esplicitamente come **inferenza/stima**. Questa è una limitazione di verificabilità di secondo livello, non una fabbricazione: gli URL sono reali e ricercabili.

---

## 1. Sintesi esecutiva (verdetto)

1. **Prezzi Starlink Italia (lug-2026): confermati e più aggressivi del previsto.** Residenziale **29 / 39 / 59 €/mese**, **antenna gratuita** (solo 19 € spedizione, o 10 €/mese noleggio), latenza **25-40 ms**, copertura dichiarata su **Alpi e Appennini**. Il report 01 ("~€40-75/mese") era corretto e semmai **conservativo**: il prezzo di ingresso è sceso a 29 €. → Il verdetto "**Starlink batte l'aereo di 1-3 ordini di grandezza per la sola banda larga**" **si rafforza**.

2. **Starlink Direct-to-Cell: reale, commerciale negli USA, in arrivo in UE, MA non ancora in Italia.** Commerciale con T-Mobile da **lug-2025** (SMS→dati app da ott-2025→voce in beta); in UE **Spagna prima (trial MasOrange, feb-2026)**, **Deutsche Telekom 10 mercati dal 2028**, **nessun deal con operatore italiano a metà 2026**. La minaccia al "D2D di area vasta da HALE" è **credibile ma non ancora concretizzata in Italia** → finestra temporale stretta ma non chiusa.

3. **Capital-intensity HAPS: il "$50M-1B" del report 05 è confermato, con una distinzione chiave.** Un **singolo prototipo** costa **$10-25M**; un **programma fino all'operatività commerciale** costa **centinaia di milioni** (Sceye ~$580M raccolti 2025; Loon ~$100M/anno per ~9 anni ≈ ~$1B; AeroVironment/SoftBank $129M solo di design; Stratospheric Platforms ~£200M target; funding di settore >$1,2B nel 2022-24). **Nessun programma HALE solare è oggi operativo commercialmente.** → Il verdetto "**HALE = centinaia di M€, impossibile per Firmamento standalone**" **si conferma**.

---

## 2. Tabella claim → fonte → verdetto → confidenza

| # | Claim (dai report 01/03/05) | Fonte (URL) | Verdetto | Confidenza (era → ora) |
|---|---|---|---|---|
| 1 | Starlink connette Pentema a ~€40-75/mese oggi | [starlink.com/it kit offer](https://starlink.com/it/residential/kitoffer); [Corriere Comunicazioni](https://www.corrierecomunicazioni.it/spaceconomy/starlink-dalle-aziende-al-residenziale-in-italia-banda-ultralarga-da-29-euro-al-mese/); [HWUpgrade](https://www.hwupgrade.it/news/scienza-tecnologia/offerta-starlink-kit-standard-l-hardware-non-si-paga-rimane-l-abbonamento-mensile-a-partire-da-29-euro_140639.html) | **CONFERMATO e migliorato per l'utente**: 29/39/59 €/mese, antenna gratis (+19 € spedizione o 10 €/mese) | Alta → **Alta** |
| 2 | Latenza Starlink 20-60 ms, copertura montana | [TechPost 2026](https://www.techpost.it/notizie/smart-city/internet-satellitare-in-italia-le-nuove-offerte-starlink-2026-tra-velocita-costi-e-copertura-reale/); [Metropolitan Magazine](https://metropolitanmagazine.it/starlink-nel-2026-come-cambia-la-connessione-internet-dallo-spazio/) | **CONFERMATO**: ~25-40 ms; copertura dichiarata Alpi/Appennini/aree interne | Alta → **Alta** |
| 3 | Starlink batte l'aereo di 1-3 ordini di grandezza (sola banda larga) | Sintesi claim 1-2 + costo marginale costellazione (report 01 §8.2) | **RAFFORZATO** (prezzo ingresso sceso a 29 €, hardware azzerato) | Alta → **Alta ↑** |
| 4 | Starlink D2C erode la nicchia NTN multi-borgo; nessun accordo MNO IT a metà 2026 | [T-Mobile T-Satellite](https://www.t-mobile.com/coverage/satellite-phone-service); [DT/Starlink Europe 2028](https://www.telecoms.com/satellite/dt-signs-european-d2d-deal-with-starlink); [Spagna MasOrange feb-2026](https://www.sahmcapital.com/news/content/starlinks-direct-to-cell-tech-gears-up-for-eu-debut-as-spains-masorange-to-begin-trial-2026-02-04) | **CONFERMATO**: D2C reale e commerciale (USA); UE in arrivo (ES 2026, DT 2028); **IT ancora nessun deal** | Media → **Media-alta** |
| 5 | Airbus Zephyr = leader ma fragile; crash ripetuti | [Wikipedia Zephyr](https://en.wikipedia.org/wiki/Airbus_Zephyr); [AOPA crash 2022](https://www.aopa.org/news-and-media/all-news/2022/august/29/airbus-zephyr-crashes-short-of-endurance-record); [Aerospace America 2025](https://aerospaceamerica.aiaa.org/aalto-maintains-2026-target-for-commercial-operations-despite-aircraft-loss/) | **CONFERMATO**: crash 2022 (dopo 64 gg) + **crash 28-apr-2025** (batteria, Oceano Indiano). Programma dal 2001, non ancora operativo commerciale | n/a → **Alta** |
| 6 | AALTO finanziata/valutata (ordini) | [Airbus PR $100M](https://www.airbus.com/en/newsroom/press-releases/2024-06-ntt-docomo-and-space-compass-partners-with-airbus-on-haps); [DCD](https://www.datacenterdynamics.com/en/news/ntt-and-space-compass-invest-100m-into-airbus-haps-unit/) | **CONFERMATO parzialmente**: $100M da NTT DOCOMO+Space Compass (giu-2024), target entry-into-service 2026. **Nessun order-book commerciale pubblico** (solo demo per NTT) | n/a → **Alta (fondi) / Bassa (ordini reali)** |
| 7 | Facebook Aquila chiuso 2018 (base-rate fallimento) | [TechCrunch 2018](https://techcrunch.com/2018/06/26/facebook-permanently-grounds-its-aquila-solar-powered-internet-plane/); [IEEE Spectrum](https://spectrum.ieee.org/facebook-pulls-out-of-secret-spaceport-internet-drone-tests) | **CONFERMATO**: cancellato giu-2018 dopo ~4 anni; crash 2016. Cifra spesa non divulgata | n/a → **Alta (evento) / n.d. (costo)** |
| 8 | Google Loon chiuso 2021, capitale bruciato | [CNBC 2021](https://www.cnbc.com/2021/01/21/alphabet-cancels-loon-project-to-beam-internet-to-earth-from-balloons.html); [TechCrunch](https://techcrunch.com/2021/01/21/google-alphabet-is-shutting-down-loon-internet/) | **CONFERMATO**: chiuso gen-2021 dopo ~9 anni; **~$100M/anno** di burn; motivo = costi troppo alti | n/a → **Alta (burn/anno); Media (~$1B cumulato, inferito)** |
| 9 | SoftBank HAWK30/Sunglider sospeso/riorganizzato | [Wikipedia HAPSMobile](https://en.wikipedia.org/wiki/HAPSMobile); [DCD dissoluzione](https://www.datacenterdynamics.com/en/news/softbank-to-absorb-hapsmobile-dissolve-unit/) | **RETTIFICATO**: non "chiuso 2023" ma **HAPSMobile assorbita/dissolta in SoftBank il 1-ott-2023**; dev AeroVironment **$65M→$129M**; R&D prosegue | n/a → **Alta** |
| 10 | BAE PHASA-35 programma snello attivo $50-150M | [Aviation Week AFRL](https://aviationweek.com/defense/aircraft-propulsion/bae-built-stratospheric-aircraft-wins-five-year-afrl-contract); [AIAA](https://aiaa.org/2025/12/19/baes-phasa-35-haps-secures-multiyear-afrl-surveillance-contract/) | **CONFERMATO attivo**: contratto AFRL **fino a $10M**, 2025-2030; ancora sperimentazione militare (SAR), non commerciale | Media-alta → **Alta (contratto); Media ($50-150M cumulato)** |
| 11 | Sceye programma airship attivo, ~$100-200M | [AvWeek Series C](https://aviationweek.com/defense/aircraft-propulsion/sceye-haps-airship-startup-raises-series-c-mawarid); [Sceye/PR Newswire SoftBank](https://www.prnewswire.com/news-releases/sceye-receives-investment-from-softbank-corp-to-scale-stratospheric-platform-development-and-launch-pre-commercial-haps-services-in-japan-in-2026-302491626.html) | **RIVISTO AL RIALZO**: **~$580M raccolti (2025)**, Series C SoftBank+Mawarid; pre-commerciale in Giappone 2026 | Low-medium → **Media (cifra da stampa specializzata)** |
| 12 | Stratospheric Platforms attivo (DT-backed) | [Advanced Television £130m](https://www.advanced-television.com/2023/02/21/stratospheric-platforms-wants-130m-for-5g/); [DCD Protelindo](https://www.datacenterdynamics.com/en/news/haps-firm-stratospheric-platforms-gains-investment-from-indonesian-tower-firm-protelindo/) | **CONFERMATO**: **£70M raccolti**, cerca **£130M** per la flotta; idrogeno, copertura 70 km; Protelindo (feb-2026) | n/a → **Alta** |
| 13 | HALE = "$50M-1B per programma" (report 05) | [MarkNtel/PR Newswire](https://www.prnewswire.com/news-releases/high-altitude-pseudo-satellites-haps-market-set-for-rapid-expansion-to-usd-240-million-by-2030--platforms-applications-and-regional-insights-fuel-16-cagr-growth-markntel-advisors-302580736.html); triangolazione claim 8-12 | **CONFERMATO con distinzione**: prototipo singolo **$10-25M**; programma commerciale **centinaia di M€** (Sceye ~$580M, Loon ~$1B, SPL ~£200M) | n/a → **Media-alta** |
| 14 | Funding di settore HAPS | [marketgrowthreports](https://www.marketgrowthreports.com/market-reports/high-altitude-pseudo-satellites-haps-market-112555); [Via Satellite](https://interactive.satellitetoday.com/haps-a-satellite-operators-big-investment-in-the-stratosphere/) | **NUOVO DATO**: funding globale HAPS **>$1,2B (2022-24)**; governativo **>$500M**; ricavi cumulati attesi ~$4B entro 2030 | n/a → **Media (market report)** |
| 15 | Mercato HAPS dimensione/CAGR | [Grand View](https://www.grandviewresearch.com/industry-analysis/high-altitude-platforms-market-report); [Cognitive](https://www.cognitivemarketresearch.com/high-altitude-platform-market-report) | **DEBOLE/DIVERGENTE**: stime 2030 da $240M a $7,2B (forbice ~30×) = mercato pre-commerciale, dato inaffidabile puntualmente | n/a → **Bassa (usare solo O.d.G.)** |

---

## 3. Approfondimento — Sostituti connettività (Starlink)

### 3.1 Prezzi reali Italia (lug-2026)
Dalla nuova struttura tariffaria **dell'11 marzo 2026** ([starlink.com/it](https://starlink.com/it/residential/kitoffer), [Corriere Comunicazioni](https://www.corrierecomunicazioni.it/spaceconomy/starlink-dalle-aziende-al-residenziale-in-italia-banda-ultralarga-da-29-euro-al-mese/)):

| Piano | €/mese | Download | Hardware |
|---|---|---|---|
| Residenziale 100 | **29** | fino 100 Mbps | Mini X, antenna gratis (+19 € sped.) |
| Residenziale 200 | **39** | fino 200 Mbps | Standard, gratis |
| Residenziale Max | **59** | fino 400 Mbps | Standard + router Mini |
| Roaming base | **40** | naz., 50 GB roaming | — |
| Roaming illimitato | **72** | — | — |
| Business | **50 → 4.713** | secondo priorità/volume | fattura P.IVA da 93 € |

Latenza **25-40 ms** ([TechPost](https://www.techpost.it/notizie/smart-city/internet-satellitare-in-italia-le-nuove-offerte-starlink-2026-tra-velocita-costi-e-copertura-reale/)). **Implicazione:** rispetto al report 01, il prezzo di ingresso è **sceso** (da ~€40 a €29) e l'hardware è **azzerato**. Il divario economico con "l'aereo-per-un-borgo" (report 01 §8.2: €100k-1M CapEx) **aumenta**.

### 3.2 Direct-to-Cell — stato reale
- **USA:** commerciale (T-Mobile "T-Satellite") **dal 23 lug-2025**; SMS/MMS/RCS + posizione, **dati per app da ott-2025**, voce in beta fine 2025; >300 sat D2C in orbita a inizio 2026 ([T-Mobile](https://www.t-mobile.com/coverage/satellite-phone-service)).
- **UE:** **Spagna (MasOrange) prima al mondo UE** con trial (feb-2026); **Deutsche Telekom** annuncia lancio in **10 mercati europei dal 2028**; **Ucraina (Kyivstar)** primo operatore europeo live; apertura spettro MSS 2 GHz dalla Commissione UE (mag-2025/26) ([DT/Starlink](https://www.telecoms.com/satellite/dt-signs-european-d2d-deal-with-starlink), [Sahm Capital](https://www.sahmcapital.com/news/content/starlinks-direct-to-cell-tech-gears-up-for-eu-debut-as-spains-masorange-to-begin-trial-2026-02-04)).
- **Italia:** **nessun accordo D2C con TIM/Vodafone/WindTre/Iliad riportato a metà 2026** (evidenza negativa).

**Lettura strategica:** il D2C convalida fisicamente il "direct-to-device dallo spazio" ma le prestazioni sono ancora **SMS/dati-app/voce-narrowband**, non broadband. La finestra per una nicchia NTN italiana da quota esiste finché non firma un MNO IT; storicamente (DT 2028) i lanci europei sono **lenti**. Questo **allunga** la finestra rispetto al timore del report 01, ma non la riapre come business core.

---

## 4. Approfondimento — Capital-intensity HAPS

### 4.1 Programmi falliti/riorganizzati (capitale bruciato)

| Programma | Esito | Capitale / burn | Fonte |
|---|---|---|---|
| **Google Loon** | Chiuso gen-2021 (~9 anni) | **~$100M/anno** → ~$1B cumulato (inferito) | [CNBC](https://www.cnbc.com/2021/01/21/alphabet-cancels-loon-project-to-beam-internet-to-earth-from-balloons.html) |
| **Facebook Aquila** | Cancellato giu-2018 (~4 anni) | Non divulgato; crash 2016 | [TechCrunch](https://techcrunch.com/2018/06/26/facebook-permanently-grounds-its-aquila-solar-powered-internet-plane/) |
| **SoftBank HAPSMobile/Sunglider** | HAPSMobile **dissolta in SoftBank 1-ott-2023**; R&D prosegue | dev AeroVironment **$65M→$129M**; industry $200-500M cumulato | [Wikipedia](https://en.wikipedia.org/wiki/HAPSMobile), [DCD](https://www.datacenterdynamics.com/en/news/softbank-to-absorb-hapsmobile-dissolve-unit/) |
| **Airbus Zephyr/AALTO** | 2 crash (2022 dopo 64 gg; **28-apr-2025** batteria); non operativo commerciale | Programma 20+ anni; stima $200-400M+ (non divulgato) | [AOPA](https://www.aopa.org/news-and-media/all-news/2022/august/29/airbus-zephyr-crashes-short-of-endurance-record), [Aerospace America](https://aerospaceamerica.aiaa.org/aalto-maintains-2026-target-for-commercial-operations-despite-aircraft-loss/) |

**Segnale base-rate:** due dei più capitalizzati attori tech al mondo (Google, Facebook) hanno **rinunciato** — non per mancanza di capitale ma per **impossibilità di chiudere l'economia**. Loon ha esplicitato il motivo: *"we haven't found a way to get the costs low enough to build a long-term, sustainable business."*

### 4.2 Programmi attivi (finanziamenti reali)

| Programma | Capitale documentato | Stato | Fonte |
|---|---|---|---|
| **AALTO (Airbus)** | **$100M** (NTT DOCOMO+Space Compass, giu-2024) + Airbus interno | Demo per NTT; target EIS 2026 | [Airbus](https://www.airbus.com/en/newsroom/press-releases/2024-06-ntt-docomo-and-space-compass-partners-with-airbus-on-haps) |
| **Sceye (airship)** | **~$580M raccolti (2025)**, Series C SoftBank+Mawarid | Pre-commerciale Giappone 2026 | [AvWeek](https://aviationweek.com/defense/aircraft-propulsion/sceye-haps-airship-startup-raises-series-c-mawarid) |
| **Stratospheric Platforms** | **£70M** raccolti + **£130M** richiesti (flotta) | Idrogeno; Protelindo 2026 | [Advanced Television](https://www.advanced-television.com/2023/02/21/stratospheric-platforms-wants-130m-for-5g/) |
| **BAE PHASA-35/Prismatic** | Contratto AFRL **fino $10M** (2025-30); cumulato $50-150M | Sperimentazione SAR militare | [Aviation Week](https://aviationweek.com/defense/aircraft-propulsion/bae-built-stratospheric-aircraft-wins-five-year-afrl-contract) |
| **Skydweller** | ~$48M Series A + EIB loan + contratti Navy | Sviluppo/demo | [Forbes](https://www.forbes.com/sites/davidhambling/2024/10/09/us-navy-eternal-drone-could-signal-the-dawn-of-solar-flight/) |
| **Space42/Mira (UAE)** | Linea produzione sovrana Abu Dhabi (mag-2025) | Test ApusNeo18 2025 | [Space42](https://www.space42.ai/en/press-release/2025/space42-opens-menas-first-high-altitude-platform-stations) |

### 4.3 Il costo di sviluppo di un HALE (rettifica del "$50M-1B")
Il dato più netto trovato: **"un singolo prototipo HAP operativo costa tipicamente USD 10-25 milioni"** ([MarkNtel via PR Newswire](https://www.prnewswire.com/news-releases/high-altitude-pseudo-satellites-haps-market-set-for-rapid-expansion-to-usd-240-million-by-2030--platforms-applications-and-regional-insights-fuel-16-cagr-growth-markntel-advisors-302580736.html)). Ma il **programma completo** fino all'operatività commerciale (flotta, certificazione >400 h di test, ground segment, ridondanza, iterazioni post-crash) è **un ordine di grandezza sopra**:
- Sceye ~$580M · Loon ~$1B · SPL ~£200M target · AeroVironment/SoftBank $129M *solo di design* · funding di settore >$1,2B in 3 anni.

**→ Il range "$50M-1B" del report 05 è corretto**, con una precisazione utile per la governance Firmamento:
- **Dimostratore tecnologico (1 esemplare, non certificato):** plausibilmente **$10-25M / €10-25M** — coerente con la fascia "demonstrator" già identificata nei report interni (05 §3). *Alla portata di un consorzio ben finanziato, NON di Firmamento standalone.*
- **Servizio operativo commerciale persistente:** **centinaia di M€** — fuori portata standalone; unico percorso = **partnership di minoranza** con un prime (AALTO, Sceye, TAS/Leonardo, Space42).

---

## 5. Confidenza aggiornata sui due verdetti-cardine

| Verdetto | Confidenza precedente | Confidenza aggiornata | Motivazione |
|---|---|---|---|
| **"Starlink batte l'aereo di 1-3 ordini di grandezza"** (sola banda larga) | Alta | **Alta ↑ (rafforzata)** | Prezzo ingresso sceso a 29 €, hardware gratis, latenza 25-40 ms, copertura Appennini dichiarata. Il costo marginale della costellazione resta imbattibile per un asset dedicato a un borgo. **Non falsificato.** |
| **"HALE = centinaia di M€, impossibile standalone"** | Alta (base-rate interno) | **Alta (confermata con fonti esterne)** | Loon ~$1B, Sceye ~$580M, SPL ~£200M, Google/Facebook ritirati, 2 crash Zephyr/AALTO, 0 programmi operativi commerciali. Distinzione aggiunta: prototipo $10-25M vs programma centinaia M€. |

### Falsifying observations (cosa cambierebbe il verdetto)
- **Starlink:** raddoppio dei prezzi IT + saturazione cronica cella Liguria, **oppure** un accordo MNO italiano che porta il D2D broadband (non solo SMS) a costo marginale zero prima dell'aereo. Nessuno dei due osservato a lug-2026.
- **HALE:** un attore dimostra un HALE solare **operativo commerciale con revenue >$1M** a latitudine ≥44°N in inverno con budget <€50M. Nessuno l'ha fatto in 20+ anni (base-rate 0%).

---

## 6. Implicazioni per lo Studio di Fattibilità

1. **Connettività broadband come business core: rimane NO** (report 01 confermato e rafforzato). Riposizionare il pilota su **EO + emergenza multi-valle + IoT d'area**, con connettività come funzione secondaria/di emergenza.
2. **D2C non è ancora una minaccia consumata in Italia**, ma la traiettoria è segnata (ES 2026, DT 2028). Qualunque narrativa "NTN da quota per aree interne" va formulata con **orizzonte temporale esplicito** e **de-risking** (partnership MNO neutral-host, non licenza propria).
3. **Percorso 6B (HALE) come sviluppo standalone: fuori portata.** I numeri esterni (Loon ~$1B, Sceye ~$580M) rendono la fascia "centinaia di M€" del report 05 **credibile a una due diligence competente**. Il posizionamento realistico resta **partner di minoranza in un consorzio EU/sovrano** (coerente con la visione 10 anni e il linguaggio "complementare a IRIS²"), non OEM stratosferico.
4. **Un dimostratore tecnologico $10-25M** è l'unico frammento della traiettoria HALE potenzialmente co-finanziabile (EDF/Horizon/PNRR) — ma va tenuto **contabilmente separato** dal procurement di servizio Y1 (coerente con report 05 §11).

---

## 7. Fonti (file salvati in `ricerca-approfondita/fonti/`)

1. `starlink-italia-prezzi.md` — prezzi residenziale/roaming/business + hardware
2. `starlink-italia-prestazioni-copertura.md` — latenza, velocità, copertura montana
3. `starlink-direct-to-cell.md` — D2C USA/UE/Italia, timeline
4. `airbus-zephyr-aalto.md` — crash 2022/2025, rebranding, $100M NTT
5. `google-loon.md` — chiusura 2021, ~$100M/anno
6. `facebook-aquila.md` — cancellazione 2018
7. `hapsmobile-sunglider-aerovironment.md` — $65M→$129M, dissoluzione 2023
8. `bae-phasa35.md` — contratto AFRL fino $10M, 2025-2030
9. `sceye.md` — ~$580M Series C
10. `stratospheric-platforms-skydweller.md` — SPL £70M/£130M; Skydweller ~$48M
11. `haps-mercato-capital-intensity.md` — prototipo $10-25M; funding >$1,2B; market size divergenti

*Ogni file riporta Titolo, URL primari, data accesso (lug-2026), cosa supporta, estratto e confidenza. Vincolo di metodo: estratti da snippet WebSearch (download integrale bloccato da policy egress — §0).*
