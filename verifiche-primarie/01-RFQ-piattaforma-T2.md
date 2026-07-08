# RFQ — Richiesta di Quotazione: Piattaforma UAS multi-missione (fascia T2)

**Firmamento Technologies S.r.l.** — Progetto piattaforma aerea per le Aree Interne
**Rif. RFQ:** FT-T2-2026-01 · **Data:** _[da compilare]_ · **Scadenza risposta richiesta:** _[gg giorni, es. 30]_
**Referente:** _[nome, email, tel]_

> **Scopo.** Ancorare a **quotazioni reali** la fascia di costo "T2" (mid-VTOL), oggi l'unica non verificata della nostra analisi (stima €0,8–1,8M non confermata). Questo documento è un **RFQ non vincolante** a scopo di budgetary quotation per uno studio di fattibilità; non costituisce ordine.

## 1. Chi siamo e contesto
Firmamento Technologies è un operatore di servizi (non OEM) che sta valutando una flotta UAS **multi-missione a payload intercambiabile** per servizi territoriali (osservazione, monitoraggio, logistica leggera/medicale, resilienza in emergenza) nelle aree interne italiane, con pilota in Liguria (Appennino, comune di Torriglia/frazione Pentema). Operazioni previste in **categoria Specific (BVLOS)**.

## 2. Requisito di missione (target — indicare conformità e alternative)
| # | Parametro | Target | Vostro valore |
|---|---|---|---|
| R1 | Configurazione | VTOL o fixed-wing+VTOL ibrido (decollo/atterraggio verticale, no pista) | |
| R2 | MTOM | 25–150 kg (indicare classe) | |
| R3 | Payload utile | ≥ 5 kg (obiettivo 5–15 kg) | |
| R4 | **Vano payload modulare** | interfaccia standard mecc./elettr./dati per **cambio rapido** tra: (a) gimbal EO (RGB+termico/multispettrale), (b) relay comunicazioni/IoT, (c) **pod cargo** | |
| R5 | Autonomia | ≥ 6 h (obiettivo 10–16 h); indicare con quale payload | |
| R6 | Raggio operativo / range | ≥ 50 km dal ground segment | |
| R7 | Quota operativa | fino a ≥ 3.000 m AMSL (operazioni in terreno montano) | |
| R8 | Vento operativo / meteo | vento sostenuto ≥ 12 m/s, resistenza pioggia leggera | |
| R9 | Propulsione | elettrica o ibrida (indicare); rumore | |
| R10 | Link C2 | BVLOS: portata, ridondanza, banda, opzione SATCOM | |
| R11 | Detect-And-Avoid | opzioni cooperative (ADS-B/FLARM) e non-cooperative | |
| R12 | Ground Control Station | comune a più payload; multi-aircraft; interfaccia U-Space | |

## 3. Requisiti regolatori e di conformità (critici)
| # | Requisito | Richiesta |
|---|---|---|
| C1 | **Marcatura di classe UAS (Reg. UE 2019/945)** | stato: classe C_ ottenuta / in corso / assente. Se assente, percorso previsto |
| C2 | **Idoneità categoria Specific / SORA 2.5** | disponibilità di documentazione a supporto SORA (M2/OSO), track record di autorizzazioni BVLOS in UE |
| C3 | **PDRA-G01 (long-range cargo)** | la piattaforma rientra nei limiti (≤3 m dimensione o ≤34 kJ, ecc.)? |
| C4 | **Consegna / merci pericolose medicali (UN3373 Cat. B)** | compatibilità con pod di contenimento certificabile; esperienze pregresse (es. trasporto biomedicale) |
| C5 | **Origine e catena di fornitura** | **paese di produzione dei componenti critici (airframe, autopilota, datalink, sensori).** Requisito preferenziale: **origine UE/NATO, esclusione fornitori soggetti a restrizioni (es. lista USA DoD 1260H)** — motivo: sovranità e ammissibilità a fondi UE/dual-use |
| C6 | Cybersecurity / sovranità dati | dove risiedono i dati; opzione on-premise |

## 4. Informazioni commerciali richieste
1. **Prezzo unitario** (budgetary) del sistema base (airframe + 1 GCS) e configurazioni.
2. **Prezzo dei moduli payload** (gimbal EO, relay, pod cargo) singolarmente.
3. **Sconti a volume** (1 / 2–3 / 4–6 unità).
4. **Costo operativo indicativo per ora di volo** (manutenzione, ricambi, consumabili).
5. **Spares & consumabili** raccomandati per servizio continuo (lista + costo).
6. **Formazione equipaggi e manutentori** (durata, costo, sede).
7. **Supporto e SLA** (garanzia, tempi di riparazione, disponibilità ricambi, MTBF).
8. **Lead time** dall'ordine alla consegna.
9. **Modello di offerta**: vendita, leasing, o "as-a-service" (indicare se disponibile).
10. **Referenze**: operatori UE con missioni analoghe (EO-persistenza, delivery, sorveglianza).

## 5. Destinatari suggeriti (fornitori europei / non a rischio-ban)
_Da contattare (verificare listino reale — nessun prezzo pubblico affidabile in ricerca):_
- **Wingtra AG** (CH) — WingtraOne GEN II [prezzo tender UK ~€35–37k: fascia inferiore]
- **Quantum-Systems** (DE) — Trinity Pro / Vector
- **Threod Systems** (EE) — Stream C
- **Tekever** (PT) — AR3/AR5 (fascia alta/MALE, per confronto)
- **Delair** (FR), **Alta/Altavian**, **UMS Skeldar** (CH/SE), **Schiebel** (AT, S-100)
- Operatori italiani/EU per **as-a-service** (es. per pod cargo medicale: interlocuzione con integratori tipo ABzero-model)

> ⚠️ **Escludere/segnalare** fornitori soggetti a restrizioni di procurement (es. **JOUAV** e altri in lista USA DoD 1260H) — rischio di analoghe misure UE e incompatibilità con la narrativa di sovranità.

## 6. Modalità di risposta
Inviare la quotazione (anche solo budgetary) a _[email]_ entro _[data]_. Gradita la compilazione delle tabelle §2–§4. Per NDA, indicare la vostra procedura.

---
*Documento di lavoro Firmamento Technologies — RFQ non vincolante a fini di studio di fattibilità.*
