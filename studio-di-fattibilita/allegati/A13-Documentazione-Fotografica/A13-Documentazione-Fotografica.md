# Allegato A.13: Documentazione Fotografica del Contesto

> Volume 2, Allegato A.13
> Conformità D.Lgs. 36/2023 art. 41 + Allegato I.7 (Documentazione fotografica obbligatoria PFTE)

## A.13.0 Premessa

Il presente allegato consolida la documentazione fotografica del contesto operativo del progetto HALE/VTOL Firmamento Technologies. Le fotografie hanno valore di:
- Documentazione visuale del sito pilota Pentema
- Riferimento operativo per progettazione GS + hangar
- Comunicazione a stakeholder + finanziatori
- Compliance art. 41 PFTE

**Status M+3**: documentazione fotografica del sito Pentema **da acquisire** durante sopralluogo Y0 (M+3-6). Il presente file è **placeholder con indice di acquisizione fotografica raccomandata**.

## A.13.1 Categorie fotografiche raccomandate

### A.13.1.1 Sito pilota Pentema (Torriglia, GE)

| Foto ID | Soggetto | Scopo |
|---|---|---|
| F-PENT-001 | Panoramica generale frazione Pentema dall'alto | Inquadramento territoriale |
| F-PENT-002 | Borgo storico vista frontale | Contesto comunità |
| F-PENT-003 | Edifici comunità (case + chiesa + piazza) | Aree residenziali da geofence |
| F-PENT-004 | Area possibile sede hangar (terreno candidato) | Pianificazione infrastruttura |
| F-PENT-005 | Area possibile GS fissa (posizione antenne) | Pianificazione GS |
| F-PENT-006 | Strade di accesso (logistica) | Pianificazione logistica |
| F-PENT-007 | Vista valle Trebbia/Pentemina (rischio frane) | Use case UC-001 |
| F-PENT-008 | Aree boschive circostanti (rischio incendio) | Use case UC-002 |
| F-PENT-009 | Condizioni meteo tipiche (4 stagioni) | Operational planning |
| F-PENT-010 | Connettività mobile (test cell coverage) | Use case UC-003 |

### A.13.1.2 Area operativa estesa (Valli Antola-Tigullio)

| Foto ID | Soggetto | Scopo |
|---|---|---|
| F-AREA-001 | Vista Parco Antola | Vigilanza ambientale |
| F-AREA-002 | Aree dissesto idrogeologico noto | Use case UC-001 |
| F-AREA-003 | Infrastrutture strade comunali (state of repair) | Use case UC-004 |
| F-AREA-004 | Cooperative agricole partner (terreni) | Use case UC-005 |
| F-AREA-005 | Centro operativo Protezione Civile Liguria | Engagement |
| F-AREA-006 | Stazione ARPA monitoraggio | Engagement |

### A.13.1.3 Piattaforme candidate (vendor materials)

| Foto ID | Soggetto | Source |
|---|---|---|
| F-VEND-001 | JOUAV CW-30E in volo | JOUAV media kit |
| F-VEND-002 | JOUAV CW-30E ground operations | JOUAV media kit |
| F-VEND-003 | Tekever AR3 in volo | Tekever media kit |
| F-VEND-004 | Tekever AR3 dimensioni vs operatore | Tekever media kit |
| F-VEND-005 | Quantum Trinity F90+ | Quantum media |
| F-VEND-006 | FlyingBasket FB3 | FlyingBasket media |

### A.13.1.4 Concept HALE Firmamento (CAD + render)

| Foto ID | Soggetto | Source |
|---|---|---|
| F-HALE-001 | Render concept HALE high-AR T-tail | CAD Firmamento (cartella `cad/`) |
| F-HALE-002 | Vista 3D ala high-AR (b ~25-30 m) | CAD |
| F-HALE-003 | Three Lifting Surface alternative (analisi XFLR5) | XFLR5 output |
| F-HALE-004 | Configurazione fibra di lino skin (rendering) | CAD + materiali |

### A.13.1.5 Casi d'uso (reference operativi)

| Foto ID | Soggetto | Source |
|---|---|---|
| F-UC-001 | Monitoraggio frane simulato (drone capture) | Reference operatori IT |
| F-UC-002 | Antincendio boschivo (IR thermal imagery) | Sample IR sensor |
| F-UC-003 | Connettività emergenza setup | Reference Protezione Civile |
| F-UC-004 | Mapping infrastrutture (RGB ortomosaico) | Reference e-GEOS/Planetek |
| F-UC-005 | Agricoltura precisione (NDVI map) | Reference MicaSense |

### A.13.1.6 Stakeholder engagement (workshop + meeting)

| Foto ID | Soggetto | Quando |
|---|---|---|
| F-STAKE-001 | Workshop pubblico comunità Pentema | M+3-6 (da fare) |
| F-STAKE-002 | Workshop cooperative Legacoop (Fabrica capofila) | M+3-6 (da fare) |
| F-STAKE-003 | Meeting Regione Liguria | M+3 (da fare) |
| F-STAKE-004 | Meeting Protezione Civile + ARPA | M+3-6 (da fare) |
| F-STAKE-005 | Meeting ENAC pre-application | M+3-6 (da fare) |

## A.13.2 Specifiche tecniche fotografiche

Per garantire **uso professionale** in documenti formali, le fotografie devono rispettare:

- **Risoluzione**: minimo 12 MP (3000×4000 px), preferito 24 MP
- **Formato**: RAW + JPEG; per pubblicazione: JPEG quality 95+
- **Color profile**: sRGB per web/print
- **Metadata EXIF**: data, coordinate GPS, timestamp
- **Geolocalizzazione**: tutte le foto sito pilota devono avere coordinate GPS
- **Licenze**: chiarire licenze per foto vendor materials (uso interno vs pubblico)

## A.13.3 Logistica acquisizione fotografica

### Sopralluogo Pentema (M+3-6)
- Durata sopralluogo: 1-2 giorni
- Team: founder + ingegnere + fotografo (eventuale)
- Equipaggiamento: DSLR 24 MP + drone amatoriale per panoramiche aeree (no BVLOS)
- Permessi: comunicazione preventiva Comune Torriglia
- Stagionalità: preferito sopralluogo in 2 stagioni (estate, autunno/inverno) per documentare condizioni operative reali

### Workshop documentazione (M+6+)
- Foto in workshop con consenso esplicito partecipanti (GDPR)
- Foto formali per pubblicazione: liberatoria firmata
- Privacy: blur volti se necessario

### Vendor materials
- Richiesta formale a vendor (JOUAV, Tekever, Quantum, FlyingBasket) per uso autorizzato foto in documenti business

## A.13.4 Cartelle file (struttura raccomandata)

```
A13-Documentazione-Fotografica/
├── 01-Pentema/ (F-PENT-001..010)
│ ├── panoramiche/
│ ├── borgo-storico/
│ ├── aree-operative/
│ └── condizioni-meteo/
├── 02-Area-Operativa/ (F-AREA-001..006)
├── 03-Piattaforme-Vendor/ (F-VEND-001..006)
├── 04-Concept-HALE/ (F-HALE-001..004)
├── 05-Casi-Uso/ (F-UC-001..005)
└── 06-Stakeholder-Workshop/ (F-STAKE-001..005)
```

## A.13.5 Status M+3 + roadmap

- ⏳ Sopralluogo Pentema con acquisizione fotografica (M+3-6)
- ⏳ Workshop pubblico Pentema + documentazione foto (M+3-6)
- ⏳ Richiesta materials vendor (M+3-6)
- ⏳ Acquisizione foto stagionali (M+6 + M+9)
- ⏳ Workshop cooperative + meeting istituzionali (M+3-9)

## A.13.6 Falsifying observations

- Se al sopralluogo Pentema il sito candidato per hangar GS risulta inadeguato (es. accesso impossibile, esposizione meteo, proprietà non disponibile), re-baseline sito operativo
- Se comunità Pentema rifiuta documentazione fotografica per privacy, il borgo storico va escluso dalle foto pubbliche

## A.13.7 Riferimenti

- Cap. 1 §1.2.3 (Pentema caso pilota)
- Cap. 5 §5.6 (Privacy + GDPR consenso)
- Vol. 3 R.4 (Documenti territoriali Liguria + SNAI)
- Allegato A.6 (CAD del concept HALE)
- Allegato A.11 (PSC + SORA, engagement comunità OQ-009)
- Allegato A.9 (CME, sito hangar Pentema)
