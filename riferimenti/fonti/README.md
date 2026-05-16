# Fonti esterne da scaricare manualmente

**Perché manualmente:** il runtime cloud di Claude Code on the web ha una network policy restrittiva (`x-deny-reason: host_not_allowed`) che blocca i domini italiani ufficiali (`enac.gov.it`, `mimit.gov.it`, `dtascarl.org`, `politichecoesione.governo.it`, `agcom.it`, ecc.) e diversi domini europei e di standard tecnici. Lo script `download.sh` di questa cartella va eseguito **dalla tua macchina locale**, non dal runtime cloud.

**Cosa farà:** scarica 40 fonti in 8 sotto-cartelle tematiche e prova a convertire i PDF in `.md` se hai `pdftotext` installato. Continua su errore (URL non più disponibili sono segnalati nel log, ma non bloccano il resto).

**Come usarlo:**
```bash
cd riferimenti/fonti/
chmod +x download.sh
./download.sh
# verifica log
cat download.log
# committa quello che è arrivato
git add -A
git commit -m "Add downloaded reference sources"
git push
```

**Stima dimensione:** ~100-300 MB di PDF + qualche tesi pesante (5-30 MB ciascuna). Tempo: 5-15 min in funzione della banda.

---

## Priorità

I file sono organizzati in **3 tier**:

| Tier | Priorità | Quante fonti | Uso |
|---|---|---|---|
| **T1** | Must-have | 12 | Chiusura debito di rigore critico (DR-001..DR-006), capitoli Studio 3-5-8-9 |
| **T2** | Should-have | 15 | Triangulation, capitoli 6-7-11, Allegati |
| **T3** | Nice-to-have | 13 | Completezza bibliografica Vol. 3 |

Se hai poco tempo, scarica almeno **T1** (12 documenti, 30 min totali).

---

## Indice dettagliato

### 📁 `01-normativa-italia/` — D.Lgs. 36/2023 e Codice Contratti

| # | Tier | File | URL | Uso nel progetto |
|---|---|---|---|---|
| 1 | T1 | `01-DLgs-36-2023-testo-integrale.htm` | https://www.bosettiegatti.eu/info/norme/statali/2023_0036.htm | Cap. 5 (normativo) — testo art. 41 PFTE |
| 2 | T1 | `02-DLgs-36-2023-allegati.pdf` | https://www.bosettiegatti.eu/public/2023_0036_Allegati.pdf | Cap. 5 — testo Allegato I.7 (contenuti PFTE/QE/DOCFAP/DIP) |
| 3 | T1 | `03-art-41-codiceappalti.htm` | https://www.codiceappalti.it/DLGS_36_2023/Articolo_41__Livelli_e_contenuti_della_progettazione_/12647 | Cap. 5 — interpretazione consolidata |
| 4 | T2 | `04-allegato-I7-codiceappalti.htm` | https://www.codiceappalti.it/DLGS_36_2023/Allegato_I_7_Contenuti_minimi_del_quadro_esigenziale,_del_documento_di_fattibilit%C3%A0_delle_alternative_progettuali,_del_documento_di_indirizzo_della_progettazione,_del_progetto_di_fattibilit%C3%A0_tecnica_ed_economica_e_del_progetto_esecutivo_/12883 | Cap. 5 — riferimento per QE/DOCFAP/DIP |
| 5 | T2 | `05-biblus-PFTE-elaborati.htm` | https://biblus.acca.it/progetto-fattibilita-tecnico-economica-elaborati/ | Cap. 5 — checklist elaborati PFTE |
| 6 | T2 | `06-PFTE-elenco-documenti-esempio.pdf` | https://www.scuoleapertemilano.it/documents/20126/470457961/3_Elenco+documenti+PFTE_REV1.pdf | Cap. 5 — template di riferimento |

### 📁 `02-fac-simili-aero/` — DTA, ENAC AAM, MIMIT

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 7 | T1 | `07-DTA-Grottaglie-studio-fattibilita-2020.pdf` | https://www.dtascarl.org/wp-content/uploads/2024/05/GROTTAGLIE-studio-fattibilita.pdf | **Template fac-simile aerospaziale principale.** Cap. 0-11 calibrazione struttura. |
| 8 | T1 | `08-ENAC-AAM-Piano-Strategico-Nazionale.pdf` | https://www.enac.gov.it/app/uploads/2024/04/01_Piano-Strategico-Nazionale-AAM_ENAC_web-en-GB.pdf | Cap. 5 + Cap. 7 (visione policy) |
| 9 | T1 | `09-ENAC-AAM-Roadmap-Allegato1.pdf` | https://www.enac.gov.it/app/uploads/2024/04/02_AAM-Italian-Ecosystem-%E2%80%93-Project-overview-and-Roadmap_web-1.pdf | Cap. 9 (cronoprogramma policy) |
| 10 | T1 | `10-ENAC-AAM-Business-Plan-Allegato2.pdf` | https://www.enac.gov.it/app/uploads/2024/04/03_AAM-Business-Plan_web-1.pdf | **Template BP aeronautico italiano.** Cap. 7-8. |
| 11 | T2 | `11-MIMIT-prefattibilita-aero.pdf` | https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf | Cap. 5+7 (template MIMIT prefatt.) |
| 12 | T2 | `12-aeropolis-analisi-costi-BP.pdf` | http://www.aeropolis.it/workshop2014/workshop-24-5-2014/AnalisiCostiBusinessPlan24_05_14.pdf | Cap. 8 (struttura costing aerospace) |
| 13 | T3 | `13-camp-otranto-ABMT.pdf` | https://camp-otranto.com/wp-content/uploads/2024/04/04-WEB-ABMT-IT.pdf | Cap. 5 (esempio studio aeroportuale) |
| 14 | T3 | `14-TE2C-sogaer-presentazione.pdf` | https://www.sogaer.it/sites/default/files/legacy/images/stories/societa/consulenti/presentazione_TE2C.pdf | Cap. 6 (struttura tecnica aeroportuale) |
| 15 | T3 | `15-aeronautica-difesa-regolamento.pdf` | https://www.aeronautica.difesa.it/wp-content/uploads/2024/02/Regolamento-amministrativo-ex-art.-15-D.Lgs_.-36.2023-POP-AMM-001_Ed.-20.pdf | Cap. 5 (interpretazione D.Lgs.36 in ambito Difesa) |

### 📁 `03-enac-easa-uspace/` — Regolamenti UAS e U-Space

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 16 | T1 | `16-Reg-UE-2019-947-operations-UAS.pdf` | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0947 | Cap. 5 — Operations UAS (Open/Specific/Certified) |
| 17 | T2 | `17-Reg-UE-2019-945-design-UAS.pdf` | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0945 | Cap. 5 — Design UAS (classi C0-C6) |
| 18 | T2 | `18-Reg-UE-2021-664-uspace-framework.pdf` | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0664 | Cap. 5 — U-Space regulatory framework |
| 19 | T3 | `19-Reg-UE-2021-665-atm-ans-uspace.pdf` | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0665 | Cap. 5 — U-Space ATM/ANS |
| 20 | T3 | `20-Reg-UE-2021-666-sera-uspace.pdf` | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0666 | Cap. 5 — U-Space SERA |
| 21 | T1 | `21-ENAC-LG-2023-006-uspace.pdf` | https://www.enac.gov.it/app/uploads/2023/12/LG-2023_006-UAS-Linee-Guida-U-Space.pdf | Cap. 5 — Linee Guida ENAC U-Space |

### 📁 `04-standard-tecnici/` — NASA SE, 3GPP, ITU

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 22 | T1 | `22-NASA-SE-Handbook-Rev2.pdf` | https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf | **Metodologia di base progetto.** Riferimento normativo NASA SE. |
| 23 | T1 | `23-3GPP-TR-38811-NTN-channel-models.pdf` | https://hscc.csie.ncu.edu.tw/38811.pdf | Cap. 6.2 + skill `link-budget-calculator` — NTN channel HAPS |
| 24 | T2 | `24-3GPP-TR-38821-NTN-solutions.pdf` | https://www.atis.org/wp-content/uploads/3gpp-documents/Rel16/ATIS.3GPP.38.821.V1600.pdf | Cap. 6.2 — NR-NTN solutions |
| 25 | T2 | `25-ITU-R-P618-rain-fade.pdf` | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.618-13-201712-S!!PDF-E.pdf | skill `link-budget-calculator` — modello rain fade |
| 26 | T3 | `26-ITU-R-P676-atmospheric-attenuation.pdf` | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.676-13-202208-S!!PDF-E.pdf | skill `link-budget-calculator` — atmospheric losses |

### 📁 `05-snai-territorial/` — SNAI, Liguria, Pentema

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 27 | T1 | `27-PSNAI-finale-2025.pdf` | https://politichecoesione.governo.it/media/k0unx2d3/psnai_finale_30072025_clean_ministro.pdf | Cap. 1 + 2 — razionale pubblico aree interne |
| 28 | T2 | `28-elenco-aree-snai-2014-2027.pdf` | https://politichecoesione.governo.it/media/rpipea3z/elenco_aree_snai_14-20-e-21-27_20231012.pdf | Cap. 2 — elenco aree IT |
| 29 | T2 | `29-snai-dossier-regionale-liguria.pdf` | https://politichecoesione.governo.it/media/3171/snai-dossier-regionale-liguria.pdf | Cap. 1 — dossier Liguria specifica |
| 30 | T3 | `30-elenco-aree-snai-2021-2027-aggiornato.pdf` | https://politichecoesione.governo.it/media/3111/elenco-aree-snai-2021-2027.pdf | Cap. 2 — aree 2021-2027 |

### 📁 `06-tesi-accademiche/` — Politecnico Torino, Polimi, UniBO, UniNa

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 31 | T2 | `31-polito-tesi-aeroportuale-28852.pdf` | https://webthesis.biblio.polito.it/28852/1/tesi.pdf | Cap. 6 — esempio analisi tecnica aero |
| 32 | T2 | `32-polito-tesi-aerospace-14893.pdf` | https://webthesis.biblio.polito.it/14893/1/tesi.pdf | Cap. 6 — riferimenti tecnici aerospace |
| 33 | T2 | `33-polimi-tesi-flax-crashworthiness.pdf` | https://www.politesi.polimi.it/retrieve/a81cb05b-7d29-616b-e053-1605fe0a889c/2020_07_Veneruso.pdf | Cap. 6.1 + agente `aerodynamics-structures-engineer` — fibra lino |
| 34 | T3 | `34-unina-fedoa-1003-tesi-gravina.pdf` | http://www.fedoa.unina.it/1003/1/Tesi_Gravina_Francesco.pdf | Cap. 6 — riferimenti accademici |
| 35 | T3 | `35-unibo-amslaurea-9491-tesi-cuoccio.pdf` | https://amslaurea.unibo.it/id/eprint/9491/1/cuoccio_davide_tesi.pdf | Cap. 6 — riferimenti accademici |

### 📁 `07-compositi-lino/` — Fibra di lino aerospace

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 36 | T3 | `36-univpm-tesi-flax-invecchiamento.htm` | https://tesi.univpm.it/handle/20.500.12075/16766 | agente `aerodynamics-structures-engineer` — durabilità lino |
| 37 | T3 | `37-compositesworld-biogear-flax.htm` | https://www.compositesworld.com/articles/carbon-fiberflax-landing-gear-achieves-54-weight-reduction-via-tailored-layup-optimization | Caso Biogear (Fuko+Turtle) |

### 📁 `08-mercato-competitor/` — HAPS market e competitor

| # | Tier | File | URL | Uso |
|---|---|---|---|---|
| 38 | T3 | `38-MarkNtel-HAPS-summary.htm` | https://www.marknteladvisors.com/research-library/high-altitude-pseudo-satellites-market.html | Cap. 7 (abstract pubblico) |
| 39 | T3 | `39-airbus-zephyr-product-page.htm` | https://www.airbus.com/en/products-services/defence/uas/zephyr | Cap. 7 — competitor data |
| 40 | T3 | `40-skydweller-perpetual-flight.htm` | https://www.skydweller.aero/news/skydweller-aero-successfully-demonstrates-perpetual-flight/ | Cap. 7 — competitor data |

---

## Note importanti

### Verifica della freschezza degli URL

Alcuni URL pubblici cambiano nel tempo (specialmente file PDF su CMS). Se uno script restituisce errore 404 su qualcuna delle fonti T1, **segnalalo e proverò a trovare l'URL aggiornato via search**.

### URL incerti (T3)

Le tesi UniNa Federico II (#34) e UniBO (#35) sono state citate nelle fonti originali ma l'URL di download diretto potrebbe essere ricostruito o aver subito redirect. Sono **T3 (nice-to-have)**, non bloccanti.

### Fonti che voglio anche, ma URL da cercare

Queste sono utili ma non ho l'URL diretto certificato. Le aggiungerò allo script di download successivo dopo che cercheremo l'URL preciso:

- **ENAC Regolamento "Mezzi Aerei a Pilotaggio Remoto" Ed. 3** (2021) — disponibile su enac.gov.it ma URL specifico da identificare
- **EASA SORA AMC/GM** (rev. corrente) — disponibile su easa.europa.eu
- **EASA Special Condition for Light UAS (SC-Light-UAS)** — disponibile su easa.europa.eu
- **ITU Radio Regulations 2024** — disponibile su itu.int (pubblicazione, può richiedere accesso)
- **AGCOM PNRF aggiornato** — pubblicato da MIMIT, URL esatto da identificare
- **Coopfond bando Cooding 2026** — non ancora pubblicato (verifica diretta con Coopfond)

### Convertire i PDF in markdown dopo il download

Lo script `download.sh` prova a fare anche la conversione `.pdf → .md` se `pdftotext` è installato sulla tua macchina:
```bash
# macOS
brew install poppler

# Ubuntu/Debian
sudo apt-get install -y poppler-utils

# Windows (via choco)
choco install xpdf-utils
```

I `.md` generati vanno accanto ai `.pdf` originali nelle stesse sottocartelle.

### Dopo il download

Una volta committati i file:
1. Io potrò **leggerli direttamente** via Read tool (sono ora in repo locale)
2. Potrò applicare la conversione markdown agli HTML come ho fatto con i `.docx` iniziali
3. Potrò chiudere progressivamente il debito di rigore (DR-001..DR-015) usando le fonti come triangulation

---

## Generated `download.sh` — usage

```bash
cd riferimenti/fonti/
chmod +x download.sh
./download.sh         # scarica tutto
./download.sh tier1   # solo T1 (12 fonti must-have)
./download.sh tier2   # T1 + T2
```
