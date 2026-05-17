# Volume 3, Riferimenti Bibliografici

> **Studio di Fattibilità, Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes
> Volume 3, Riferimenti
>
> **Versione:** M+3 bozza
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7

## Struttura Volume 3

| Sezione | File | Contenuto |
|---|---|---|
| **R.1** | [`R1-bibliografia-normativa.md`](R1-bibliografia-normativa.md) | Norme UE e IT (Codice Contratti, Reg.UE UAS, EASA AMC/GM, ENAC, AGCOM, GDPR, NIS2, Direttive ATEX/Macchine/RoHS, AI Act) |
| **R.2** | [`R2-bibliografia-tecnica.md`](R2-bibliografia-tecnica.md) | Standard tecnici aerospaziali (NASA SE, INCOSE, ECSS, DO-178C/254/326A, ARP4754A/4761, AS/EN 9100, EUROCAE, STANAG, ITU-R) |
| **R.3** | [`R3-fonti-mercato-competitor.md`](R3-fonti-mercato-competitor.md) | Report di mercato HAPS/UAV (commerciali e istituzionali Eurospace/AIAD/EUSPA), competitor data (Zephyr/Skydweller/PHASA-35/Sunglider/EuroHAPS), fonti finanziarie |
| **R.4** | [`R4-documenti-SNAI-territoriali.md`](R4-documenti-SNAI-territoriali.md) | PSNAI 2025, elenchi aree SNAI 2014-2027, dossier Liguria, Regione Liguria FESR, ENAC AAM Piano Strategico |
| **R.5** | [`R5-studi-accademici.md`](R5-studi-accademici.md) | Studi accademici peer-reviewed (POLITO HELIPLAT/DIMEAS, Polimi/Sapienza/UNIVPM compositi fibra di lino, 3GPP NTN papers, ITU-R papers, NASA Helios mishap report) |

## Convenzioni di citazione

Tutti i riferimenti seguono lo stile **misto Chicago/IEEE adatto a documenti tecnico-regolatori italiani**:

- **Norme**: `[Tipo norma] [Numero]/[Anno], [Titolo abbreviato], [Articolo se rilevante], [Data], [Source URL]`
- **Standard tecnici**: `[Ente] [Identificativo], "[Titolo]", [Edizione/Revisione], [Anno], [URL/DOI]`
- **Peer-reviewed**: `[Autori], "[Titolo]", [Journal/Conference], [Volume/Issue], pp. [pages], [Anno], DOI:[xxx]`
- **Report commerciali**: `[Ente], "[Titolo]", [Anno], [URL]. Confidence: [low/medium]`
- **Documenti istituzionali**: `[Ente], "[Titolo]", [Data], [URL]`

## Note di provenance e confidence

Tutti i riferimenti citati nei capitoli del Volume 1 sono qui consolidati. Per ogni riferimento è indicato un **confidence level** della fonte. Le fonti **commerciali single-source** (MarkNtel, Grand View, ecc.) sono dichiarate `confidence: low` per il loro uso come baseline finanziaria. Le fonti **peer-reviewed o ufficiali normative** sono `confidence: high`. Le fonti **vendor** (datasheet JOUAV, Skydweller, ecc.) sono `confidence: medium` con caveat.

## Cross-reference

I riferimenti citati con `[^N]` nei capitoli del Volume 1 si risolvono qui per categoria:

- Norme e autorità: R.1
- Standard tecnici e metodologia: R.2
- Dati mercato e competitor: R.3
- SNAI, Liguria e AAM: R.4
- Accademici e ricerca: R.5

## Aggiornamento

Versione corrente: **M+3 bozza**. Aggiornamenti previsti:
- M+6: post pre-application ENAC e workshop cooperative
- M+10: completo per gate G3 FEASIBILITY
- M+12+: aggiornamento operativo Y1

## Disciplina epistemica

I riferimenti del Vol. 3 sono **vincolanti** per la skill `epistemic-rigor`: ogni claim del Volume 1 che cita un riferimento di questo Vol. 3 deve essere ricontrollato se la fonte è stata aggiornata o falsificata. Vedi `riferimenti/audit-rigore-epistemico.md` e `DR-research-closure-M3.md` per il debt log.
