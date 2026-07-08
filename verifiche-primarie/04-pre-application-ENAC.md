# Pre-application ENAC — traccia ConOps + lista domande (SAIL e consegna medicale)

**Scopo:** ottenere da ENAC (fonte primaria) la stima realistica del **SAIL** e del percorso autorizzativo per operazioni BVLOS a Pentema, incluse missioni di **consegna medicale** — chiudendo il debito di rigore DR-004. Da usare per un **pre-application meeting** e per impostare la domanda di autorizzazione.

> Ancoraggi dalla ricerca (da confermare con ENAC): consegna = **sempre categoria Specific** (art. 4 Reg. 947); **SORA 2.5** (ED Decision 2025/018/R); merci pericolose **fuori scope SORA** → servono contenimento + **autorizzazione DG ENAC**; esiste **PDRA-G01 "long-range cargo"** (BVLOS zona poco popolata, target **SAIL II**); precedente reale **ABzero – rotta biomedicale Patti/Eolie (lug 2024)**, autorizzata rotta-per-rotta; densità Pentema **< 5 ab/km²** (banda "Remote/sparsely populated").

## 1. Sintesi ConOps (bozza da allegare)
| Voce | Descrizione (bozza) |
|---|---|
| **Operatore** | Firmamento Technologies S.r.l. (+ rete cooperativa) |
| **Area operativa** | Appennino ligure, comune di Torriglia – frazione Pentema (GE) e valli limitrofe; terreno montano, densità **< 5 ab/km²** |
| **Tipo operazioni** | BVLOS in categoria Specific |
| **Missioni** | (a) EO/monitoraggio persistente (frane, incendi, sorveglianza ambientale); (b) **consegna medicale/biomedicale** (campioni, farmaci) tra presidio a valle e borgo/e; (c) relay/IoT d'emergenza |
| **Piattaforma** | UAS ala fissa+VTOL, MTOM _[25–150] kg_ (classe da definire post-RFQ), payload ≤ _[15] kg_ |
| **Quota / volume** | VLL, ≤ _[120–500] m_ AGL, spazio aereo Classe G non controllato (da confermare) |
| **Rotte** | corridoi predefiniti valle→borgo; drop-zone controllate (non sorvolo diretto dell'abitato) |
| **Carico pericoloso** | biomedicale **UN3373 Cat. B** (basso rischio); **esclusione Cat. A** dal ConOps; contenimento con capsula dedicata |
| **Mitigazioni** | geofencing, FTS/paracadute balistico, C2 ridondante, DAA, procedure meteo/vento montano |

## 2. Domande sul percorso SORA / SAIL
1. Confermate la classificazione della **densità del footprint** operativo a Pentema come "**sparsely populated / controlled ground area**"? Con quale banda si entra (< 5 / < 50 ab/km²) e quale **iGRC** ne consegue per la nostra classe di UAS?
2. Con le mitigazioni previste (M1 riduzione popolazione a rischio, M2 contenimento), quale **GRC finale** e quale **SAIL** stimate per (a) la missione **EO** e (b) la missione **consegna**?
3. Per l'**Air Risk Class (ARC)**: confermate ARC-b in Classe G a bassa quota per l'area? Quali condizioni la alzerebbero (prossimità a spazi controllati, rotte VFR, elisuperfici HEMS)?
4. Il nostro caso rientra in un **PDRA** (in particolare **PDRA-G01 long-range cargo**) o richiede **SORA piena**? Quali limiti di PDRA-G01 rischiamo di superare (dimensione caratteristica, energia d'impatto)?

## 3. Domande sulla consegna medicale / merci pericolose
5. Per **UN3373 Cat. B** trasportato da UAS: quale **autorizzazione merci pericolose** ENAC serve, e come si dimostra il **contenimento** (dato che la SORA esclude le DG dal proprio scope)?
6. Esistono **prescrizioni specifiche** ereditabili dal precedente **ABzero** (rotta biomedicale autorizzata) che possiamo prendere a riferimento?
7. Il **rilascio/sgancio** del carico e l'avvicinamento alla drop-zone in prossimità di un borgo: quali condizioni evitano il salto in **categoria Certified** (art. 6, sorvolo di assembramenti)?

## 4. Domande su spazio aereo, U-Space, coordinamento
8. Serve coordinamento con **ENAV** per l'area? Esistono restrizioni (aree vietate/riservate, HEMS, antincendio boschivo Canadair) da gestire, specie in stagione incendi?
9. **U-Space**: per l'Appennino ligure non risultano zone U-Space designate (prima zona IT a San Salvo, 2026) — confermate che **non è un prerequisito** per la nostra operazione a breve?
10. Come gestire la **condivisione dello spazio aereo con i mezzi antincendio** durante gli eventi (priorità, NOTAM, sospensione operazioni)?

## 5. Domande su processo, tempi, documentazione
11. Quali **documenti** attendete per la domanda (ConOps, OM, Risk Assessment SORA, evidenze OSO, manuali)? Esiste un **template** ENAC aggiornato alla SORA 2.5?
12. **Tempi** indicativi tra domanda e autorizzazione per un SAIL II e per un SAIL III?
13. L'autorizzazione è **rotta-per-rotta** (come ABzero) o è ottenibile un'**autorizzazione d'area/di operazione** più ampia? Cosa serve per quest'ultima?
14. In prospettiva multi-missione/multi-rotta, quando conviene puntare a un **LUC** e quali sono i prerequisiti (SMS, accountable manager) che ENAC valuta?
15. È attivabile una **fase sperimentale / progetto pilota** con ENAC (o ENAC + Regione/Protezione Civile) che semplifichi l'avvio?

## 6. Esito atteso del meeting
- [ ] SAIL stimato per EO e per consegna (con banda di densità confermata)
- [ ] Applicabilità PDRA-G01 sì/no
- [ ] Percorso DG medicale chiarito
- [ ] Lista documenti + tempi
- [ ] Rotta-per-rotta vs autorizzazione d'area
- [ ] Eventuale canale "pilota" con Regione/PC

---
*Bozza di lavoro. Personalizzare la sezione ConOps con i dati della piattaforma scelta (post-RFQ) prima del meeting ENAC. Richiedere il pre-application meeting via i canali ufficiali ENAC (Direzione Operazioni / UAS).*
