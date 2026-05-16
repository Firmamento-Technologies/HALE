# 3GPP TR 38.821 — Versioni archiviate

Questa cartella contiene **tutte le release** del 3GPP TR 38.821 *"Solutions for NR to support non-terrestrial networks (NTN) (Release 16)"* in formato `.zip` (ognuno contiene un singolo `.doc`).

## Mappa delle versioni 3GPP (convenzione)

| File | Versione 3GPP | Data | Note |
|---|---|---|---|
| `38821-001.zip` | v0.0.1 | Q3 2018 | Bozza iniziale |
| `38821-010.zip` | v0.1.0 | Q4 2018 | |
| `38821-020.zip` | v0.2.0 | Q1 2019 | |
| `38821-030.zip` | v0.3.0 | Q2 2019 | |
| `38821-040.zip` | v0.4.0 | Q3 2019 | |
| `38821-050.zip` | v0.5.0 | Q4 2019 | |
| `38821-060.zip` | v0.6.0 | Q1 2020 | |
| `38821-070.zip` | v0.7.0 | Q2 2020 | |
| `38821-080.zip` | v0.8.0 | Q3 2020 | |
| `38821-090.zip` | v0.9.0 | Q4 2020 | Pre-approval |
| `38821-100.zip` | v1.0.0 | Q1 2021 | Frozen approval |
| `38821-110.zip` | v1.1.0 | Q2 2021 | Editorial fixes |
| `38821-g00.zip` | **v16.0.0** | Q3 2021 | **Release 16 published** |
| `38821-g10.zip` | v16.1.0 | 2022 | Maintenance |
| `38821-g20.zip` | **v16.2.0** | mar 2023 | **Release 16 latest** ⭐ |

> La convenzione 3GPP: l'ultimo carattere è in base esadecimale. `g` = 16 in hex = Release 16. Le versioni con prefisso numerico (0.X.Y) sono draft pre-approval; quelle con prefisso alfabetico (gXY) sono release stable.

## Versione raccomandata: **v16.2.0** (g20)

È la **release più recente** del TR 38.821 (marzo 2023), e include le ultime correzioni editoriali. Per il progetto HALE è la versione di riferimento.

**Conversione disponibile:**
- ZIP: `38821-g20.zip` (questa cartella)
- DOC estratto: rimosso dopo conversione (era 25 MB, recuperabile con `unzip 38821-g20.zip`)
- **Markdown convertito**: `../3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md` (~350 KB) ← **da usare per consultazione e citazioni**

Convertito con `antiword` (Linux): il `.doc` legacy 3GPP non si converte con pandoc/libreoffice in molti runtime; antiword è il fallback robusto.

## Storico per audit (versioni precedenti)

Le altre versioni sono conservate per **provenance e audit** (es. confronto come è evoluto il framework HAPS in 3GPP), **non per uso operativo**. Da convertire localmente se necessario:

```bash
cd fonti/3GPP\ TR\ 38.821\ /
unzip 38821-XXX.zip
antiword 38821-XXX.doc > ../3GPP_TR_38821_vYYY.md
```
