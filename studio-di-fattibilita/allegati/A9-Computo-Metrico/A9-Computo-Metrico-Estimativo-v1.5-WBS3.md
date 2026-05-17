# Allegato A.9. Computo Metrico Estimativo v1.5 (WBS 3)

> Volume 2, Allegato A.9. **Versione 1.5 (WBS livello 3)**
> Computo Metrico Estimativo Ground Segment Pentema + OpEx correlati
> Conformità: D.Lgs. 36/2023 art. 41 + Allegato I.7 (elaborato PFTE obbligatorio)
> Versione: v1.5, Maggio 2026. Granularità WBS 3 (sub-component livello operativo)
> Sostituisce: v1.0 (WBS 2 preliminary) per la sola componente Ground Segment Pentema Percorso 6A
> Confidence aggregato: **MEDIUM** (preliminary investment-grade richiede 200-400 h Cost Estimator certificato + revisione RUP Regione Liguria)

---

## Indice

1. Inquadramento normativo e metodologia
2. WBS 3 Computo Metrico per categoria (10 macro-categorie)
3. Quadro Economico riepilogativo (sub-totali, scenario worst/base/best)
4. Voci OPEX correlate (manutenzione, utenze, run-rate)
5. Tariffario FTE (prestazioni professionali)
6. Caveat epistemici e gap residui
7. Cronoprogramma spese Y1 (M+0 al M+12)
8. Linkage cross-volume

---

## Sezione 1. Inquadramento normativo e metodologia

### 1.1 Quadro normativo di riferimento

Il presente Computo Metrico Estimativo (CME) v1.5 è elaborato in conformità a:

| Riferimento | Ambito | Applicazione al CME |
|---|---|---|
| **D.Lgs. 36/2023 art. 41** | Codice dei Contratti Pubblici, PFTE | Obbligo di CME per progetti pubblici/cofinanziati |
| **Allegato I.7 D.Lgs. 36/2023** | Contenuti minimi PFTE | CME tra elaborati obbligatori (lett. l) |
| **D.M. LL.PP. 14/01/2008** | Norme Tecniche Costruzioni (NTC 2018 aggiornamento) | Verifica strutturale opere edili (hangar) |
| **Prezzario Regione Liguria 2025** | Tariffario lavori pubblici regionali | Base prezzi unitari opere edili e impianti |
| **DEI Tipografia del Genio Civile 2025** | Prezzi informativi infrastrutture | Cross-check voci speciali (data center, RF) |
| **Linee Guida ANAC n. 1/2016** | Servizi di architettura e ingegneria | Calcolo spese tecniche (3-10% lavori) |
| **Reg. UE 651/2014 GBER** | Aiuti di Stato compatibili | Vincoli intensità aiuto su CapEx grant-financed |

`[fonte: testi normativi vigenti maggio 2026 | confidence: high]`

### 1.2 Granularità WBS adottata

Adottiamo **WBS livello 3** (sub-component operativo) per il Ground Segment Pentema (Percorso 6A), come compromesso ragionevole rispetto all'investment-grade:

- **WBS 1**: macro-area (es. "Ground Segment Pentema")
- **WBS 2**: sistema (es. "Hangar", "GCS fissa")
- **WBS 3**: sub-component operativo (es. "Hangar, pavimentazione cemento industriale", "GCS fissa, UPS online 5 kVA")
- WBS 4 (componente fisica e capitolato tecnico dettagliato) e WBS 5 (singolo articolo prezzario): richiesti per investment-grade ma fuori scope per studio di fattibilità.

**Codifica WBS 3**: `GS.[macro-categoria 2 digit].[sub-sistema 2 digit].[item 3 digit]`

Esempio: `GS.01.01.001` = Ground Segment, Hangar, Strutture, Item 001 (pavimentazione cemento).

### 1.3 Convenzioni di calcolo

| Convenzione | Valore | Note |
|---|---|---|
| **Valuta** | Euro (€) | Riferimento 2026 Q1-Q2 |
| **IVA** | Esclusa nei totali parziali; aggiunta 22% in quadro riepilogativo | Riferimento ordinario; eventuali agevolazioni cooperativo Coopfond da verificare |
| **Contingency** | 15% raccomandato sul totale opere | Allineato benchmark aerospace baseline 10-30% (lower bound prudenziale) |
| **Spese tecniche** | 8-12% lavori (Linee Guida ANAC n. 1/2016) | Include progettazione, DL, CSP, RUP |
| **Imprevisti** | 5% lavori | Riferimento art. 41 c. 12 D.Lgs. 36/2023 |
| **Tariffe FTE** | €/g lordo azienda + onnicomprensivo benefit | Riferimento mercato aerospace IT 2025-2026 |
| **Tasso di sconto** | Non applicato a CapEx (anno 0); applicato in Cap. 8 §8.6 NPV con WACC 11% | Coerenza con scenario base |

### 1.4 Fonti prezzo gerarchia

In ordine di preferenza:
1. **Prezzario Regione Liguria 2025** (autorità regionale, voci pubblicate)
2. **DEI 2025** (riferimento nazionale tecnico)
3. **Offerte vendor formali** (per attrezzature aerospace specifiche; da formalizzare RFQ M+3)
4. **Benchmark mercato comparabili** (e-GEOS, Planetek, Leonardo UAS service)
5. **Stima parametrica** (ultima ratio, confidence ridotta a LOW)

Ogni voce in tabella riporta colonna "Fonte" e "Confidence".

`[fonte: metodologia consolidata da Linee Guida MIT 2018 + ANAC n. 1/2016 + best practice Cost Estimator IFAC | confidence: high]`

---

## Sezione 2. WBS 3 Computo Metrico per categoria

> **Nota di lettura**: ogni macro-categoria riporta tabella WBS 3 con sub-totale categoria. Le 10 macro-categorie sono allineate al perimetro Ground Segment Pentema dal briefing operativo di progetto.

### 2.1 Categoria 1. Hangar Pentema (riuso edificio esistente + adeguamento minimo)

**Ipotesi base**: scenario A, affitto immobile rurale esistente 80-150 m² coperto + 30-60 m² scoperto pavimentato + adeguamento leggero. Lo scenario B (light build prefabbricato) è in tabella alternative §2.1-B.

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| **GS.01. Strutture coperte (riuso + adeguamento)** | | | | | | | |
| GS.01.01.001 | Indagine strutturale preliminare (verifica capacità portante solaio + tetto) | a corpo | 1 | 2.500 | 2.500 | Tariffa OING Liguria 2025 | M |
| GS.01.01.002 | Pratiche urbanistiche (SCIA edilizia, comunicazione cambio destinazione) | a corpo | 1 | 1.800 | 1.800 | Tariffa OAPPC Liguria | H |
| GS.01.01.003 | Pavimentazione cemento industriale levigato 80 m² (resistenza UAV + batterie) | m² | 80 | 65 | 5.200 | Prezzario Liguria 2025 art. E.05.010 | H |
| GS.01.01.004 | Trattamento antipolvere + segnaletica gialla parking UAV | m² | 80 | 18 | 1.440 | Prezzario Liguria 2025 art. E.07.150 | H |
| GS.01.01.005 | Porta scorrevole industriale 3x3 m motorizzata | cad | 1 | 4.800 | 4.800 | DEI 2025 sez. NP.07 | H |
| GS.01.01.006 | Manto copertura, verifica e ripristino impermeabilizzazione (50 m²) | m² | 50 | 45 | 2.250 | Prezzario Liguria 2025 art. C.03.220 | H |
| GS.01.01.007 | Tinteggiatura pareti interne lavabile (200 m² superficie) | m² | 200 | 12 | 2.400 | Prezzario Liguria 2025 art. F.01.080 | H |
| GS.01.01.008 | Coibentazione termica leggera pareti (lana roccia 80 mm) | m² | 100 | 38 | 3.800 | Prezzario Liguria 2025 art. C.07.040 | H |
| **GS.02. Aree esterne pavimentate** | | | | | | | |
| GS.01.02.001 | Pavimentazione esterna in cls drenante 40 m² (piazzola decollo) | m² | 40 | 78 | 3.120 | Prezzario Liguria 2025 art. E.05.040 | H |
| GS.01.02.002 | Pavimentazione asfaltata viabilità accesso (riassetto 50 m²) | m² | 50 | 42 | 2.100 | Prezzario Liguria 2025 art. E.04.010 | H |
| GS.01.02.003 | Segnaletica orizzontale piazzola (T, H, area sicurezza ENAC) | a corpo | 1 | 850 | 850 | Stima parametrica | M |
| GS.01.02.004 | Dissuasori automatici accesso veicolare | cad | 2 | 1.200 | 2.400 | DEI 2025 sez. SC.02 | M |
| **GS.03. Locazione annua (Y1)** | | | | | | | |
| GS.01.03.001 | Canone locazione immobile 80-150 m² Pentema 12 mesi | mese | 12 | 1.000 | 12.000 | Benchmark Borsino OMI Liguria 2025 | M |
| GS.01.03.002 | Deposito cauzionale (3 mensilità) | a corpo | 1 | 3.000 | 3.000 | Prassi commerciale | H |
| GS.01.03.003 | Spese notarili registrazione contratto + bolli | a corpo | 1 | 650 | 650 | Tariffa notarile 2025 | H |
| | **Sub-totale Categoria 1. Hangar (scenario A riuso)** | | | | **48.310** | | M |

**Alternativa GS.01-B. Light build prefabbricato (se riuso non praticabile)**:

| WBS 3 | Descrizione | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Conf. |
|---|---|---|---|---|---|---|
| GS.01.B.001 | Permesso costruire + oneri urbanistici | a corpo | 1 | 5.500 | 5.500 | H |
| GS.01.B.002 | Fondazioni + platea cls armato 100 m² | m² | 100 | 95 | 9.500 | H |
| GS.01.B.003 | Struttura prefabbricata leggera (parete sandwich + tetto) | m² | 100 | 285 | 28.500 | H |
| GS.01.B.004 | Porta scorrevole 4x4 m + accessori | cad | 1 | 5.200 | 5.200 | H |
| GS.01.B.005 | Sistema antincendio FM-200 + ATEX storage LiPo | sistema | 1 | 7.500 | 7.500 | M |
| GS.01.B.006 | Allacciamenti impianti generali | a corpo | 1 | 4.000 | 4.000 | M |
| | **Sub-totale Alternativa B (light build)** | | | | **60.200** | M |

`[Decision gate G2 M+6: scelta A vs B subordinata a sopralluogo e offerta locazione vincolante]`

### 2.2 Categoria 2. GCS fissa (Ground Control Station)

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| **GS.02.01. Rack + computing** | | | | | | | |
| GS.02.01.001 | Rack 19" 24U + porta vetro + ventilazione attiva + PDU intelligente | cad | 1 | 1.450 | 1.450 | APC/Vertiv listino 2025 | H |
| GS.02.01.002 | Server mission control 1U (Dell PowerEdge R660 o eq., 64 GB RAM, 2x SSD 1TB) | cad | 1 | 6.800 | 6.800 | Dell listino EDU 2025 | H |
| GS.02.01.003 | Server payload processing 2U (GPU NVIDIA A4000, 128 GB RAM) | cad | 1 | 9.500 | 9.500 | Dell/Supermicro listino 2025 | H |
| GS.02.01.004 | Switch managed L3 24 porte gigabit + 4 SFP+ | cad | 1 | 1.850 | 1.850 | Cisco/Aruba listino 2025 | H |
| GS.02.01.005 | Firewall UTM hardware (Fortinet 80F o eq.) | cad | 1 | 2.200 | 2.200 | Fortinet listino 2025 | H |
| **GS.02.02. Workstation operatore** | | | | | | | |
| GS.02.02.001 | Workstation pilota BVLOS (PC desktop Dell Precision 3680, 32GB, RTX A2000) | cad | 1 | 2.400 | 2.400 | Dell listino PRO 2025 | H |
| GS.02.02.002 | Workstation analista dati (PC desktop Dell Precision 3680, 64GB, RTX A4000) | cad | 1 | 3.800 | 3.800 | Dell listino PRO 2025 | H |
| GS.02.02.003 | Monitor 32" 4K IPS calibrati (per mission control) | cad | 2 | 850 | 1.700 | Dell/LG listino 2025 | H |
| GS.02.02.004 | Monitor 27" secondari (telemetria) | cad | 2 | 380 | 760 | Dell listino 2025 | H |
| GS.02.02.005 | KVM IP 4 porte enterprise (Raritan/Vertiv) | cad | 1 | 1.650 | 1.650 | Raritan listino 2025 | H |
| GS.02.02.006 | Cuffie professionali aviation (Bose A30) | cad | 2 | 1.200 | 2.400 | Bose listino 2025 | H |
| GS.02.02.007 | Joystick + throttle quadrant professionale (CH Products/Brunner) | set | 2 | 1.450 | 2.900 | Brunner listino 2025 | H |
| **GS.02.03. UPS + power conditioning** | | | | | | | |
| GS.02.03.001 | UPS online doppia conversione 5 kVA (4h autonomia carico nominale) | cad | 1 | 4.800 | 4.800 | APC/Vertiv listino 2025 | H |
| GS.02.03.002 | Pacco batterie esteso (raddoppio autonomia 8h) | cad | 1 | 2.200 | 2.200 | APC/Vertiv listino 2025 | H |
| GS.02.03.003 | Stabilizzatore tensione 6 kVA (zona rurale fluttuazioni) | cad | 1 | 1.350 | 1.350 | DEI 2025 sez. EI.04 | M |
| GS.02.03.004 | Generatore diesel backup 8 kVA insonorizzato (avvio automatico) | cad | 1 | 6.500 | 6.500 | DEI 2025 sez. EI.06 | M |
| **GS.02.04. Software mission planning** | | | | | | | |
| GS.02.04.001 | Licenza UgCS PRO mission planning (perpetua + 1 anno support) | cad | 2 | 2.800 | 5.600 | UgCS listino 2025 | H |
| GS.02.04.002 | Licenza Pix4D Mapper Enterprise (annuale) | anno | 1 | 4.500 | 4.500 | Pix4D listino 2025 | H |
| GS.02.04.003 | Licenza QGIS + plugin enterprise + setup | a corpo | 1 | 1.500 | 1.500 | Servizio + plugin commerciali | M |
| GS.02.04.004 | Suite anonimizzazione GDPR (es. Brighter AI + setup) | anno | 1 | 6.500 | 6.500 | Brighter AI listino 2025 | M |
| GS.02.04.005 | SIEM aziendale (Wazuh enterprise support 1 anno) | anno | 1 | 2.800 | 2.800 | Wazuh support 2025 | M |
| | **Sub-totale Categoria 2. GCS fissa** | | | | **73.160** | | H-M |

### 2.3 Categoria 3. GCS mobile (van adattato)

**Opzione Y1: differita a Y2**. Per Y1 si include solo l'allestimento leggero rapido (kit removibile da furgone esistente). Il van dedicato resta posticipato a Y2 post-MVP success.

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.03.01.001 | Console removibile portatile (ruggedized case + Pelican 1620) | cad | 1 | 1.800 | 1.800 | Pelican listino 2025 | H |
| GS.03.01.002 | Laptop ruggedized mission control (Dell Latitude 5430 Rugged) | cad | 1 | 4.500 | 4.500 | Dell listino 2025 | H |
| GS.03.01.003 | Antenna tracking mast telescopico 4 m portatile | cad | 1 | 6.800 | 6.800 | Microhard/Doodle listino 2025 | M |
| GS.03.01.004 | Modem C2 portatile (Microhard pDDL/Doodle Labs) | cad | 1 | 3.200 | 3.200 | Microhard listino 2025 | H |
| GS.03.01.005 | UPS portatile 2 kVA + batterie esterne | cad | 1 | 1.450 | 1.450 | EcoFlow listino 2025 | H |
| GS.03.01.006 | Generatore inverter portatile 3 kW (Honda EU30is) | cad | 1 | 2.800 | 2.800 | Honda listino 2025 | H |
| GS.03.01.007 | Kit antenne portable VHF/UHF + LMR400 cablaggio | set | 1 | 1.850 | 1.850 | Mercato vendor RF 2025 | M |
| GS.03.01.008 | Radio TETRA portatile (Sepura SC21) | cad | 2 | 1.600 | 3.200 | Sepura listino 2025 | H |
| GS.03.01.009 | Modem 4G/5G industriale dual-SIM ruggedized | cad | 1 | 950 | 950 | Teltonika listino 2025 | H |
| GS.03.01.010 | Tavolo pieghevole + sedia ergonomica ruggedized + tenda parasole | set | 1 | 1.200 | 1.200 | Mercato outdoor PRO | M |
| | **Sub-totale Categoria 3. GCS mobile (kit Y1 leggero)** | | | | **27.750** | | M |

> Van dedicato (Iveco Daily 4x4 allestito) differito a Y2: stima preliminare €60-80k allestimento completo + €30-45k veicolo.

### 2.4 Categoria 4. Antenne RF + sistema comunicazione

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.04.01.001 | Antenna omnidirezionale C2 link 900 MHz (gain 8 dBi, IP67) | cad | 1 | 1.450 | 1.450 | Mercato vendor RF 2025 | H |
| GS.04.01.002 | Antenna direzionale Yagi 2.4/5 GHz (gain 18 dBi, IP67) | cad | 1 | 2.200 | 2.200 | Mercato vendor RF 2025 | H |
| GS.04.01.003 | Antenna backup omnidirezionale diversità (900 MHz) | cad | 1 | 1.450 | 1.450 | Mercato vendor RF 2025 | H |
| GS.04.01.004 | Antenna SATCOM L-band Iridium Certus fissa | cad | 1 | 8.500 | 8.500 | Iridium partner listino 2025 | H |
| GS.04.01.005 | Modem SATCOM Iridium Certus 700 + abbonamento setup | cad | 1 | 4.800 | 4.800 | Iridium partner listino 2025 | H |
| GS.04.01.006 | Palo antenne tubolare zincato H=8 m + tirantatura | cad | 1 | 2.800 | 2.800 | DEI 2025 sez. ER.02 | H |
| GS.04.01.007 | Cavo coassiale LMR-400 (set 50 m + connettori N) | set | 3 | 480 | 1.440 | Times Microwave listino 2025 | H |
| GS.04.01.008 | Lightning arrestor antenne + sistema messa terra dedicato | cad | 3 | 320 | 960 | PolyPhaser listino 2025 | H |
| GS.04.01.009 | Misurazione + calibrazione VSWR + analisi spettro | a corpo | 1 | 1.800 | 1.800 | Servizio specialistico vendor | M |
| GS.04.01.010 | Pratiche AGCOM/MISE autorizzazione frequenze sperimentali | a corpo | 1 | 2.500 | 2.500 | Studio legale specializzato | M |
| | **Sub-totale Categoria 4. Antenne RF** | | | | **27.900** | | H-M |

### 2.5 Categoria 5. Storage + processing

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.05.01.001 | NAS enterprise 40 TB RAID6 (Synology RS3621xs+ o eq.) | cad | 1 | 8.500 | 8.500 | Synology partner listino 2025 | H |
| GS.05.01.002 | Disk extension bay (12 bay aggiuntivi) | cad | 1 | 3.200 | 3.200 | Synology partner listino 2025 | H |
| GS.05.01.003 | Hard disk enterprise 8 TB (Seagate Exos x12) | cad | 12 | 290 | 3.480 | Seagate distributore 2025 | H |
| GS.05.01.004 | NAS secondario backup 20 TB (offsite-ready) | cad | 1 | 4.800 | 4.800 | Synology partner listino 2025 | H |
| GS.05.01.005 | Jetson Orin AGX Developer Kit (cluster 3 nodi processing edge) | cad | 3 | 2.100 | 6.300 | NVIDIA listino 2025 | H |
| GS.05.01.006 | Cluster orchestrator (mini-server K3s + cabling) | a corpo | 1 | 2.800 | 2.800 | Stima parametrica | M |
| GS.05.01.007 | Sottoscrizione cloud sync (AWS S3 IA / Wasabi 100 TB anno 1) | anno | 1 | 3.600 | 3.600 | AWS/Wasabi listino 2025 | H |
| GS.05.01.008 | Software backup enterprise (Veeam Community + licenza estesa) | anno | 1 | 1.800 | 1.800 | Veeam listino 2025 | H |
| GS.05.01.009 | Setup + configurazione iniziale storage + processing | h | 40 | 85 | 3.400 | Tariffa system integrator | M |
| | **Sub-totale Categoria 5. Storage + processing** | | | | **37.880** | | H-M |

### 2.6 Categoria 6. Connettività

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.06.01.001 | Indagine fattibilità fibra dedicata Pentema (Open Fiber/TIM/Fastweb) | a corpo | 1 | 800 | 800 | Tariffa indagine operatore | M |
| GS.06.01.002 | Allacciamento fibra business 100/100 Mbps (canone setup) | a corpo | 1 | 4.500 | 4.500 | Listino TIM Business 2025 (zona rurale) | M |
| GS.06.01.003 | Canone fibra annuale 100/100 Mbps SLA business | anno | 1 | 3.600 | 3.600 | Listino TIM Business 2025 | M |
| GS.06.01.004 | Router CPE business + apparati attivi | cad | 1 | 950 | 950 | TIM o terzi | H |
| GS.06.01.005 | Backup 4G/5G professional con SIM M2M dual-carrier | a corpo | 1 | 1.200 | 1.200 | Teltonika + abbonamento | H |
| GS.06.01.006 | Canone 4G/5G backup annuale (50 GB/mese, 2 carrier) | anno | 1 | 1.440 | 1.440 | Vodafone/TIM M2M 2025 | H |
| GS.06.01.007 | VPN appliance + certificati (Wireguard enterprise) | a corpo | 1 | 1.500 | 1.500 | Setup + licenza | M |
| | **Sub-totale Categoria 6. Connettività (Y1 capex+opex Y1)** | | | | **13.990** | | M |

### 2.7 Categoria 7. Sicurezza fisica

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.07.01.001 | Cancello motorizzato scorrevole 4 m + automazione | cad | 1 | 3.800 | 3.800 | DEI 2025 sez. SC.04 | H |
| GS.07.01.002 | Telecamere CCTV IP fisse 4K (Axis P3265 o eq.) | cad | 4 | 580 | 2.320 | Axis listino 2025 | H |
| GS.07.01.003 | Telecamera PTZ 360° (Axis Q6135-LE) | cad | 1 | 2.200 | 2.200 | Axis listino 2025 | H |
| GS.07.01.004 | NVR 16 canali + storage 8 TB (Synology DVA3221) | cad | 1 | 2.800 | 2.800 | Synology partner listino 2025 | H |
| GS.07.01.005 | Sistema antintrusione (centrale + 6 sensori PIR + 4 magnetici + sirena) | sistema | 1 | 2.450 | 2.450 | Bentel/Inim listino 2025 | H |
| GS.07.01.006 | Sensori movimento esterni perimetrali (Optex) | cad | 4 | 280 | 1.120 | Optex listino 2025 | H |
| GS.07.01.007 | Lettore RFID controllo accessi + tessere | sistema | 1 | 1.450 | 1.450 | HID listino 2025 | H |
| GS.07.01.008 | Cablaggio + posa segnale debole + canalizzazioni | a corpo | 1 | 3.500 | 3.500 | Prezzario Liguria art. EI.07 | H |
| GS.07.01.009 | Allacciamento istituto vigilanza (chiamata + ronda) anno 1 | anno | 1 | 1.800 | 1.800 | Mercato Liguria 2025 | M |
| GS.07.01.010 | Certificazione impianto + cert. CEI 79 | a corpo | 1 | 850 | 850 | Tariffa professionista | H |
| | **Sub-totale Categoria 7. Sicurezza fisica** | | | | **22.290** | | H |

### 2.8 Categoria 8. Impianti (HVAC + elettrico + UPS + groundbond + safety)

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| **GS.08.01. Impianto elettrico** | | | | | | | |
| GS.08.01.001 | Allacciamento ENEL trifase 15 kW dedicato (escluso oneri ENEL) | a corpo | 1 | 1.800 | 1.800 | Tariffa Enel 2025 (zona rurale C) | H |
| GS.08.01.002 | Quadro elettrico generale + sub-quadri (server room + uffici) | a corpo | 1 | 3.500 | 3.500 | Prezzario Liguria art. EI.02 | H |
| GS.08.01.003 | Cavidotti + cablaggio dorsale 3F+N+T 35 mmq (50 m posa) | m | 50 | 28 | 1.400 | Prezzario Liguria art. EI.05 | H |
| GS.08.01.004 | Punti luce LED industriali (24 punti hangar + uffici) | cad | 24 | 95 | 2.280 | Prezzario Liguria art. EI.10 | H |
| GS.08.01.005 | Prese FM 16A + UPS dedicate (12 punti) | cad | 12 | 65 | 780 | Prezzario Liguria art. EI.11 | H |
| GS.08.01.006 | DPI + cassette pronto soccorso elettrico + segnaletica | a corpo | 1 | 450 | 450 | Mercato sicurezza lavoro | H |
| GS.08.01.007 | Certificazione impianto DM 37/08 + dichiarazione conformità | a corpo | 1 | 1.200 | 1.200 | Tariffa professionista | H |
| **GS.08.02. Impianto HVAC** | | | | | | | |
| GS.08.02.001 | Climatizzatore split inverter 18.000 BTU (server room) | cad | 1 | 2.200 | 2.200 | Daikin/Mitsubishi listino 2025 | H |
| GS.08.02.002 | Climatizzatore split inverter 12.000 BTU (uffici) | cad | 2 | 1.500 | 3.000 | Daikin/Mitsubishi listino 2025 | H |
| GS.08.02.003 | Ventilazione meccanica controllata hangar (estrattore industriale) | cad | 1 | 1.800 | 1.800 | DEI 2025 sez. IT.04 | H |
| GS.08.02.004 | Sistema umidificazione/deumidificazione server room | cad | 1 | 1.450 | 1.450 | DEI 2025 sez. IT.05 | M |
| GS.08.02.005 | Riscaldamento pompa calore (zona montana, inverno -10°C) | cad | 1 | 4.500 | 4.500 | Daikin/Mitsubishi listino 2025 | H |
| **GS.08.03. Ground bond + safety** | | | | | | | |
| GS.08.03.001 | Impianto messa terra dedicato (picchetti + cordone Cu nudo 50 mmq) | a corpo | 1 | 2.800 | 2.800 | Prezzario Liguria art. EI.13 | H |
| GS.08.03.002 | Impianto scariche atmosferiche (palo + collettori) | a corpo | 1 | 3.500 | 3.500 | Prezzario Liguria art. EI.14 | H |
| GS.08.03.003 | Verifica resistenza terra + cert. periodica DPR 462/01 | a corpo | 1 | 600 | 600 | Tariffa professionista | H |
| GS.08.03.004 | Sistema antincendio FM-200 server room (oppure aerosol Stat-X) | sistema | 1 | 4.500 | 4.500 | DEI 2025 sez. SA.02 | H |
| GS.08.03.005 | Estintori CO2 + polvere + carrelli (12 unità) + segnaletica | a corpo | 1 | 1.800 | 1.800 | Prezzario Liguria art. SA.01 | H |
| GS.08.03.006 | Armadio ATEX per stoccaggio batterie LiPo (vincolo VVF) | cad | 1 | 3.500 | 3.500 | Mercato chemical storage | M |
| GS.08.03.007 | Centrale rilevazione fumo + sensori (8 sensori cablati EN54) | sistema | 1 | 2.200 | 2.200 | Inim/Bentel listino 2025 | H |
| | **Sub-totale Categoria 8. Impianti** | | | | **43.260** | | H-M |

### 2.9 Categoria 9. Cartellonistica e segnaletica (ENAC + ambientale)

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.09.01.001 | Pannello identificativo aerodromo ENAC (operatore + categoria SORA) | cad | 1 | 450 | 450 | Mercato segnaletica aviation | H |
| GS.09.01.002 | Cartellonistica accesso area sicurezza (divieto + rischio elettrico + UAV) | cad | 6 | 85 | 510 | Prezzario Liguria art. SE.01 | H |
| GS.09.01.003 | Segnaletica orizzontale piazzola decollo (vernice gialla ENAC) | a corpo | 1 | 650 | 650 | Mercato segnaletica aviation | M |
| GS.09.01.004 | Cartellonistica ambientale Parco Antola (vincolo VIA) | cad | 4 | 150 | 600 | Ente Parco Antola 2025 | M |
| GS.09.01.005 | Targa GDPR videosorveglianza + privacy | cad | 4 | 35 | 140 | Mercato segnaletica GDPR | H |
| GS.09.01.006 | Cartellonistica antincendio + vie fuga (EN ISO 7010) | sistema | 1 | 380 | 380 | Mercato segnaletica safety | H |
| GS.09.01.007 | Targa identificativa impianto trasmettente (AGCOM) | cad | 1 | 120 | 120 | Mercato segnaletica RF | H |
| GS.09.01.008 | NOTAM Origination service (anno 1, gestione publicazioni) | anno | 1 | 1.800 | 1.800 | Tariffa ENAV/ENAC | M |
| | **Sub-totale Categoria 9. Cartellonistica** | | | | **4.650** | | H-M |

### 2.10 Categoria 10. Allestimenti ufficio operations

| WBS 3 | Descrizione item | UM | Q.tà | Prezzo unit. (€) | Totale (€) | Fonte | Conf. |
|---|---|---|---|---|---|---|---|
| GS.10.01.001 | Scrivanie regolabili motorizzate (1600x800) | cad | 2 | 580 | 1.160 | IKEA/Herman Miller 2025 | H |
| GS.10.01.002 | Sedie ergonomiche operative (uso 8 h/g, conformità UNI EN 1335) | cad | 2 | 420 | 840 | Mercato office IT 2025 | H |
| GS.10.01.003 | Armadio ufficio per documentazione + ignifugo per backup | cad | 2 | 380 | 760 | Mercato ufficio IT 2025 | H |
| GS.10.01.004 | Sala riunioni: tavolo 6 posti + sedie + monitor 65" smart display | a corpo | 1 | 3.800 | 3.800 | Mercato office 2025 | H |
| GS.10.01.005 | Cassaforte ignifuga per documenti sensibili (DPIA, certificazioni) | cad | 1 | 950 | 950 | Mercato safe 2025 | H |
| GS.10.01.006 | Stampante multifunzione laser A3 (Brother MFC L9670CDN) | cad | 1 | 1.200 | 1.200 | Brother listino 2025 | H |
| GS.10.01.007 | Distributore acqua + frigo break room + microonde | a corpo | 1 | 650 | 650 | Mercato office 2025 | H |
| GS.10.01.008 | Cassetta pronto soccorso conforme DM 388/03 | cad | 2 | 80 | 160 | Mercato safety 2025 | H |
| GS.10.01.009 | Materiale ufficio start-up (cancelleria, etichette, raccoglitori) | a corpo | 1 | 600 | 600 | Stima parametrica | M |
| GS.10.01.010 | Lavagna interattiva planning operativo | cad | 1 | 1.800 | 1.800 | Mercato office 2025 | M |
| | **Sub-totale Categoria 10. Allestimenti ufficio** | | | | **11.920** | | H |

---

## Sezione 3. Quadro Economico riepilogativo

### 3.1 Sub-totali per categoria (scenario base, IVA esclusa)

| # | Categoria | Sub-totale (€) | Note |
|---|---|---|---|
| 1 | Hangar Pentema (scenario A riuso + adeguamento) | 48.310 | Alternativa B light build: 60.200 |
| 2 | GCS fissa | 73.160 | |
| 3 | GCS mobile (kit Y1 leggero) | 27.750 | Van dedicato differito Y2 |
| 4 | Antenne RF + comunicazione | 27.900 | |
| 5 | Storage + processing | 37.880 | |
| 6 | Connettività (CapEx + Y1 OpEx) | 13.990 | |
| 7 | Sicurezza fisica | 22.290 | |
| 8 | Impianti (HVAC + elettrico + safety) | 43.260 | |
| 9 | Cartellonistica + segnaletica | 4.650 | |
| 10 | Allestimenti ufficio operations | 11.920 | |
| | **A. TOTALE LAVORI + FORNITURE (no IVA)** | **311.110** | Base scenario A hangar riuso |

### 3.2 Somme a disposizione (formato art. 41)

```
QUADRO ECONOMICO. Ground Segment Pentema Y1 (Percorso 6A)
Riferimento art. 41 D.Lgs. 36/2023 + Allegato I.7
─────────────────────────────────────────────────────────────────
A) IMPORTO LAVORI E FORNITURE €
 A.1 Hangar Pentema (riuso + adeguamento) 48.310
 A.2 GCS fissa 73.160
 A.3 GCS mobile (kit Y1 leggero) 27.750
 A.4 Antenne RF + comunicazione 27.900
 A.5 Storage + processing 37.880
 A.6 Connettività (CapEx + Y1 OpEx) 13.990
 A.7 Sicurezza fisica 22.290
 A.8 Impianti HVAC + elettrico + safety 43.260
 A.9 Cartellonistica + segnaletica 4.650
 A.10 Allestimenti ufficio operations 11.920
 TOTALE A 311.110

B) SOMME A DISPOSIZIONE €
 B.1 Spese tecniche (progett. + DL + CSP + RUP)
 10% di A (Linee Guida ANAC n. 1/2016) 31.111
 B.2 Imprevisti (5% di A, art. 41 c. 12) 15.556
 B.3 Contingency aerospace (15% di A) 46.667
 B.4 Spese pubblicità bandi (eventuali) 1.500
 B.5 Allacciamenti + autorizzazioni (esclusi A) 4.800
 (ENAC SORA, AGCOM, oneri ENEL, VVF)
 B.6 Spese collaudo + verifiche di conformità 3.500
 B.7 Indagini integrative + sopralluoghi 2.800
 TOTALE B 105.934

C) IVA + ONERI FISCALI €
 C.1 IVA 22% su A 68.444
 C.2 IVA 22% su B (su voci imponibili) 19.605
 TOTALE C 88.049

─────────────────────────────────────────────────────────────────
TOTALE GENERALE (A + B + C), scenario BASE € 505.093
─────────────────────────────────────────────────────────────────
```

### 3.3 Scenario worst / base / best

| Scenario | A (lavori) | B (somme disp.) | C (IVA) | Totale (€) | Note |
|---|---|---|---|---|---|
| **Best** (-15% / contingency 10%) | 264.444 | 79.333 | 75.652 | **419.428** | Hangar riuso ottimale + offerte vendor competitive |
| **Base** | 311.110 | 105.934 | 88.049 | **505.093** | Scenario nominale + contingency standard 15% |
| **Worst** (+25% / contingency 20% + hangar B) | 416.638 | 162.489 | 127.408 | **706.535** | Light build hangar B + overrun vendor + extra opere |

### 3.4 Cross-check vs Cap. 8 §8.3 CapEx Y1

| Item | A.9 v1.5 base (€k) | Cap. 8 §8.3 baseline range (€k) | Δ | Coerenza |
|---|---|---|---|---|
| Ground Segment Pentema totale | 505 | 350-700 (segmento infrastructure) | -50/+200 | OK (entro range; conservativo) |
| Quota su CapEx totale Y1 (€700k-2M) | 25-30% | 20-35% atteso | -- | OK (allineato benchmark UAS ops) |

`[fonte: cross-check vs Cap. 8 §8.3.1 Quadro Economico Y1 | confidence: medium]`

**Falsifying observation**: se al M+6 le offerte vendor vincolanti riportano A > €420k (vs 311k base), si attiva la revisione di scope (es. cluster Jetson da 3 a 1 nodo, GCS mobile differita Y3) oppure il rinforzo del grant pubblico a copertura del delta.

---

## Sezione 4. Voci OPEX correlate (run-rate annuale Ground Segment)

> Coerenza con Cap. 8 §8.5.1.A (baseline OpEx) + §8.5.1.B (regulatory team).

### 4.1 OpEx Manutenzione Ground Segment Y2+ (€/anno)

| WBS 3 OpEx | Descrizione | UM | Q.tà | Costo unit. (€) | Totale (€/anno) | Conf. |
|---|---|---|---|---|---|---|
| OPEX.GS.01.001 | Manutenzione ordinaria hangar (pulizia + verifiche periodiche) | a corpo | 1 | 2.400 | 2.400 | H |
| OPEX.GS.01.002 | Manutenzione straordinaria hangar (5% valore opere) | anno | 1 | 1.500 | 1.500 | M |
| OPEX.GS.02.001 | Manutenzione GCS hardware (server + workstation, contratto Dell PRO) | anno | 1 | 4.800 | 4.800 | H |
| OPEX.GS.02.002 | Rinnovo licenze software (UgCS, Pix4D, anonim, SIEM) | anno | 1 | 18.500 | 18.500 | H |
| OPEX.GS.02.003 | Sostituzione batterie UPS (ciclo 3 anni, ammortamento annuale) | anno | 1 | 1.500 | 1.500 | H |
| OPEX.GS.04.001 | Canone abbonamento SATCOM Iridium Certus 700 (data plan) | anno | 1 | 6.500 | 6.500 | H |
| OPEX.GS.04.002 | Manutenzione antenne RF + ricalibrazione VSWR annuale | anno | 1 | 1.800 | 1.800 | M |
| OPEX.GS.05.001 | Sottoscrizione cloud sync (AWS S3 IA / Wasabi 100 TB) | anno | 1 | 3.600 | 3.600 | H |
| OPEX.GS.05.002 | Hard disk replacement (rotazione preventiva 25% disk/anno) | anno | 1 | 1.200 | 1.200 | H |
| OPEX.GS.06.001 | Canone fibra 100/100 Mbps SLA business | anno | 1 | 3.600 | 3.600 | H |
| OPEX.GS.06.002 | Canone 4G/5G backup dual-carrier | anno | 1 | 1.440 | 1.440 | H |
| OPEX.GS.07.001 | Canone istituto vigilanza + ronda | anno | 1 | 1.800 | 1.800 | M |
| OPEX.GS.07.002 | Manutenzione antintrusione + CCTV (contratto vendor) | anno | 1 | 1.200 | 1.200 | H |
| OPEX.GS.08.001 | Manutenzione HVAC + ricariche refrigerante | anno | 1 | 1.500 | 1.500 | H |
| OPEX.GS.08.002 | Verifica annuale impianto elettrico + messa terra DPR 462/01 | anno | 1 | 800 | 800 | H |
| OPEX.GS.08.003 | Verifica + ricarica estintori + sistema FM-200 | anno | 1 | 600 | 600 | H |
| OPEX.GS.10.001 | Materiale ufficio + cancelleria | anno | 1 | 1.200 | 1.200 | H |
| | **Totale OPEX Ground Segment Y2+ (€/anno)** | | | | **53.940** | H-M |

### 4.2 OpEx Utenze (€/anno)

| WBS 3 OpEx | Descrizione | UM | Q.tà | Costo unit. (€) | Totale (€/anno) | Conf. |
|---|---|---|---|---|---|---|
| OPEX.UT.01.001 | Energia elettrica (15 kW × 4500 h equivalenti × 0,25 €/kWh) | kWh | 16.875 | 0,25 | 4.218 | H |
| OPEX.UT.01.002 | Acqua + scarico (utenza domestica) | anno | 1 | 480 | 480 | H |
| OPEX.UT.01.003 | Smaltimento rifiuti speciali (batterie LiPo dismesse, eco-fee) | anno | 1 | 850 | 850 | M |
| OPEX.UT.01.004 | Canone locazione hangar Y2+ (scenario A) | anno | 1 | 12.000 | 12.000 | M |
| OPEX.UT.01.005 | Tassa rifiuti TARI + IMU (utenza non residenziale) | anno | 1 | 1.450 | 1.450 | M |
| | **Totale Utenze Y2+ (€/anno)** | | | | **18.998** | H-M |

### 4.3 Totale OpEx Ground Segment Pentema (run-rate Y2+)

| Voce | €/anno |
|---|---|
| Manutenzione + licenze | 53.940 |
| Utenze | 18.998 |
| **TOTALE OPEX Ground Segment (no FTE)** | **72.938** |

> Cross-check Cap. 8 §8.5.1.A: voce "Costi sede / utilities Pentema" range €15-30k + voci manutenzione/licenze distribuite. Il totale GS di €73k/anno resta coerente con il baseline (margine -10% rispetto a stima conservativa €80k).

---

## Sezione 5. Tariffario FTE (prestazioni professionali)

> Riferimento mercato aerospace IT 2025-2026. Tariffe lorde azienda (costo per il datore di lavoro), inclusive di retribuzione, contributi, TFR, welfare e assicurazioni.

### 5.1 Tariffe €/giorno e €/mese FTE

| Ruolo | RAL ord. (€/anno) | Costo aziendale (€/anno) | €/mese (12 mensilità) | €/giorno (218 g lavorabili) | Note |
|---|---|---|---|---|---|
| **Pilota BVLOS senior** | 48.000-58.000 | 62.400-75.400 | 5.200-6.283 | 286-346 | Brevetto SORA + esperienza ≥ 5 anni |
| **Pilota BVLOS junior** | 38.000-45.000 | 49.400-58.500 | 4.117-4.875 | 227-268 | Brevetto SORA + 2 anni exp |
| **Ingegnere ops aerospace** | 42.000-52.000 | 54.600-67.600 | 4.550-5.633 | 250-310 | Laurea ing. + 3-5 anni exp |
| **Ingegnere senior systems** | 55.000-72.000 | 71.500-93.600 | 5.958-7.800 | 328-429 | Laurea ing. + 7+ anni exp |
| **Analista dati / GIS specialist** | 36.000-46.000 | 46.800-59.800 | 3.900-4.983 | 215-274 | Competenze QGIS/Python/AI/ML |
| **Project Manager certificato** | 50.000-68.000 | 65.000-88.400 | 5.417-7.367 | 298-405 | PMP/Prince2 + esperienza aerospace |
| **CISO (Chief Information Security Officer)** | 70.000-95.000 | 91.000-123.500 | 7.583-10.292 | 417-566 | Cybersecurity + ISO 27001 + NIS2 |
| **DPO (Data Protection Officer)** | 45.000-65.000 | 58.500-84.500 | 4.875-7.042 | 268-388 | GDPR cert. + 3+ anni exp |
| **Head of Regulatory** | 65.000-90.000 | 84.500-117.000 | 7.042-9.750 | 387-537 | Esperienza ENAC/EASA/AGCOM |
| **RUP / Responsabile procedimento** | 55.000-75.000 | 71.500-97.500 | 5.958-8.125 | 328-447 | PA o consulente esterno |
| **Cost Estimator certificato** | 50.000-70.000 | 65.000-91.000 | 5.417-7.583 | 298-417 | AACE/ICCM cert., per CME investment-grade |

`[fonte: indagini retributive Page Personnel 2025, Hays Aerospace 2025, Robert Half Tech 2025, mercato IT Milano/Torino/Roma | confidence: medium-high]`

### 5.2 Tariffe consulenza esterna (€/giorno)

| Servizio | €/giorno | Note |
|---|---|---|
| Studio legale specializzato aerospace/AGCOM | 1.200-2.500 | Tariffa partner senior |
| Consulente certificazione SORA | 850-1.500 | Specialista ENAC PDRA |
| Consulente VIA / studio ambientale | 600-1.200 | Per pratiche Parco Antola |
| Engineering specialistico (avionica, RF) | 750-1.400 | Consulenza occasionale |
| Audit cybersecurity / pen-test | 950-1.800 | Tariffa progetto |
| Architetto/ingegnere edile (DL ground segment) | 480-750 | Tariffa OAPPC Liguria 2025 |
| Direttore lavori operativo (DL) | 550-850 | Tariffa OING Liguria 2025 |
| CSP/CSE Coordinatore Sicurezza | 450-700 | D.Lgs. 81/08 ambito cantiere |
| Notaio (registrazioni contratti) | a tariffa | Tariffario notarile 2025 |

### 5.3 Cross-check totale FTE Y1 vs Cap. 8 §8.5.1

| Ruolo Y1 (FTE allocazione %) | Costo Y1 (€k) | Note |
|---|---|---|
| Pilota BVLOS senior (100% FTE) | 75 | Posizione critica |
| Ingegnere ops aerospace (100%) | 67 | Mission planning + procedures |
| Analista dati (100%) | 59 | Processing + cliente delivery |
| PM (50%) | 38 | Part-time fino M+12 |
| DPO (10% retainer esterno) | 8 | Consulenza GDPR |
| Head Regulatory (20% retainer) | 22 | Engagement ENAC/AGCOM |
| Total FTE Y1 baseline | 269 | Coerente con Cap. 8 §8.5.1.A range €250-300k |

---

## Sezione 6. Caveat epistemici e gap residui

### 6.1 Confidence aggregato

**Confidence aggregato CME v1.5: MEDIUM**

Razionale:
- **HIGH** sulle voci edili standard (prezzario Liguria 2025 ufficiale): cat. 1-Hangar, cat. 8-Impianti, cat. 10-Allestimenti
- **MEDIUM-HIGH** sulle voci IT/RF (listini vendor 2025 ma non offerte vincolanti): cat. 2-GCS, cat. 3-Mobile, cat. 4-Antenne, cat. 5-Storage, cat. 7-Sicurezza
- **MEDIUM** sulle voci specialistiche aerospace (tariffe parametriche e benchmark): allacciamento RF, AGCOM, NOTAM, ATEX LiPo, ATEX storage
- **LOW** sulle 3 voci stimate parametricamente: cluster orchestrator (GS.05.01.006), cartellonistica orizzontale piazzola (GS.01.02.003), materiale ufficio start-up (GS.10.01.009)

`[fonte: metodologia AACE Cost Estimate Classification System, Classe 4 "Study or Feasibility" tipica per PFTE pre-execution | confidence: high]`

**Per investment-grade (Classe 2-3 AACE)** è richiesta integrazione obbligatoria (vedi gap 6.3).

### 6.2 Limiti dichiarati v1.5

1. **WBS 3 vs WBS 4-5 investment-grade**: il presente CME è WBS 3 (sub-component operativo); l'investment-grade richiede WBS 4 (componente fisica + capitolato dettagliato) e WBS 5 (singolo articolo prezzario), tipicamente 200-400 h Cost Estimator certificato.
2. **Assenza sopralluogo sito**: nessuna indagine fisica condotta su immobile Pentema target (privato o pubblico). La stima dimensioni 80-150 m² resta parametrica.
3. **Assenza offerte vendor vincolanti**: tutte le voci IT/RF si basano su listini pubblici 2025 e benchmark. La RFQ formale è prevista M+3.
4. **Assenza indagine strutturale**: il riuso hangar assume conformità statica solaio/copertura per carichi UAV e batterie, da verificare M+1.
5. **Prezzario Liguria 2025**: utilizzato in edizione corrente; un eventuale aggiornamento 2026 può modificare le voci edili del ±3-5%.
6. **Scenario A vs B hangar**: scelta finale subordinata a sopralluogo + offerta locazione vincolante (decision gate G2 M+6).
7. **Vincoli Parco Antola**: assunta compatibilità autorizzativa baseline; VIA preliminare A.12 da finalizzare.
8. **Tariffe FTE**: derivate da indagini retributive 2025; il mercato aerospace IT in espansione lascia possibile un incremento del 5-8% nel 2026-2027.

### 6.3 Gap residui per investment-grade (M+9 target)

| Gap | Azione richiesta | Owner | Deadline |
|---|---|---|---|
| Sopralluogo sito Pentema | Sopralluogo tecnico + rilievo metrico | Engineering | M+1 |
| Indagine strutturale hangar | Tecnico abilitato verifica solaio + copertura | Strutturista esterno | M+2 |
| Offerta vincolante locazione hangar | Trattativa con proprietà + contratto preliminare | Legal + PM | M+4 |
| RFQ vendor GCS (≥ 3 offerte) | Dell + HPE + Lenovo + integratori IT | Procurement | M+3 |
| RFQ vendor antenne/RF (≥ 3 offerte) | Microhard, Doodle Labs, integratori RF | Procurement | M+3 |
| RFQ vendor SATCOM Iridium | Iridium partner Italia (es. Marlink, Telespazio) | Procurement | M+3 |
| Pratica autorizzazione AGCOM frequenze | Consulente specialista | Regulatory | M+5 |
| Pratica ENAC SORA + PSC | Consulente certificazione + SME | Regulatory | M+6 |
| Indagine fattibilità fibra Open Fiber/TIM Pentema | Operatore TLC + comune Torriglia | Procurement | M+2 |
| Prezzario Liguria 2026 aggiornamento (se rilasciato) | Verifica voci edili modificate | Cost Estimator | M+9 |
| Revisione RUP Regione Liguria (per cofinanziamento FESR) | Engagement + presentazione CME | PM + Head Regulatory | M+9 |
| Cost Estimator certificato AACE per validazione | Incarico esterno (200-400 h) | CFO + Engineering | M+8 |

### 6.4 Falsifying observations attivanti revisione

| Trigger | Azione |
|---|---|
| Offerte vendor GCS > €100k (vs €73k base) | Revisione scope: cluster Jetson 1 nodo, monitor singolo, no SIEM enterprise |
| Locazione hangar > €18k/anno (vs €12k base) | Attivare scenario B light build |
| Indagine strutturale hangar = negativa | Forzare scenario B light build (+€15k delta) |
| AGCOM tempi autorizzazione > M+9 | Ritardo go-live, attivare M+12 timeline |
| Fibra Pentema non disponibile a 100 Mbps | Downgrade a 30/30 Mbps + 4G primario (vincoli SLA) |
| ATEX LiPo classificazione VVF Zona 1 (vs Zona 2) | +€20-40k armadio + ventilazione (RSK-REG-022) |

---

## Sezione 7. Cronoprogramma spese Y1

### 7.1 Allocazione mese-per-mese (CapEx + OpEx Y1)

| Mese | Fase | Voci principali | CapEx (€) | OpEx (€) | Cumulato (€) |
|---|---|---|---|---|---|
| M+0 | Pre-execution | Spese tecniche progettazione iniziale + indagini | 8.000 | 0 | 8.000 |
| M+1 | Design | Sopralluogo + indagine strutturale + ICD detailed | 6.500 | 0 | 14.500 |
| M+2 | Design | Pratiche urbanistiche + indagine fibra | 5.500 | 0 | 20.000 |
| M+3 | Procurement | RFQ vendor + contratti preliminari + cauzione locazione | 15.000 | 1.000 | 36.000 |
| M+4 | Procurement | Ordini GCS + storage + antenne (acconto 40%) | 55.000 | 1.000 | 92.000 |
| M+5 | Procurement | Ordini impianti elettrici/HVAC + sicurezza (acconto 40%) | 28.000 | 1.000 | 121.000 |
| M+6 | Installazione | Lavori hangar + pavimentazione + impianti base | 42.000 | 2.500 | 165.500 |
| M+7 | Installazione | Installazione GCS + cablaggio + antenne (saldo 60% ordini) | 78.000 | 2.500 | 246.000 |
| M+8 | Installazione | Setup storage + processing + connettività | 35.000 | 3.000 | 284.000 |
| M+9 | Commissioning | Collaudo + cert. CE + verifiche elettriche/RF | 18.000 | 4.000 | 306.000 |
| M+10 | Commissioning | Test integrato + acceptance test + training | 8.000 | 5.000 | 319.000 |
| M+11 | Ramp-up | Test operativi + procedure + dry-run mission | 4.000 | 6.000 | 329.000 |
| M+12 | Operativo | Inizio servizio + manutenzione ordinaria | 2.000 | 8.000 | 339.000 |
| | **TOTALI Y1 (CapEx + OpEx parziale)** | | **305.000** | **34.000** | **339.000** |

> Nota: il totale Y1 €339k rappresenta il flusso di cassa effettivo Y1 al netto di spese tecniche, IVA e contingency (che ricadono in B+C). Il Quadro Economico totale base di €505k include tutte le voci (vedi §3.2).

### 7.2 Curva spese cumulate (S-curve)

```
% Cumulato CapEx Y1
100% | ████
 90% | ████
 80% | ████
 70% | ████
 60% | ████
 50% | ████
 40% | ███
 30% | ███
 20% | ██
 10% | █
 0% |__________________________________________
 M0 M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 M11 M12
 Design | Procurement | Install. | Commiss.| Ramp
```

Picco esborso CapEx: M+7 (saldo 60% ordini GCS + lavori installazione).

### 7.3 Vincoli cassa + finanziamento

| Tranche | Mese | Fonte | Importo (€k) | Note |
|---|---|---|---|---|
| T0 | M-1 | Equity fondatori | 50 | Capitale circolante iniziale |
| T1 | M+1 | Coopfond Cooding Prototypes | 50 | Erogazione anticipo 50% |
| T2 | M+3 | Coopfond Cooding-Invest | 100 | Tranche 1 |
| T3 | M+5 | Regione Liguria FESR (anticipo 30%) | 60 | Acconto pratica deliberata |
| T4 | M+8 | Coopfond Cooding-Invest | 100 | Tranche 2 al milestone |
| T5 | M+10 | R&D tax credit Y1 | 30 | Anticipo compensazione |
| T6 | M+12 | Regione Liguria FESR (SAL 1) | 80 | A rendicontazione SAL 50% |
| | **Totale finanziamento Y1** | | **470** | Copre €339k CapEx+OpEx Y1 + buffer |

`[fonte: scenario funding mix Cap. 8 §8.7 | confidence: medium, subordinato a esito bandi]`

---

## Sezione 8. Linkage cross-volume

### 8.1 Riferimenti normativi e standard

- **D.Lgs. 36/2023 art. 41**: Codice dei Contratti Pubblici, PFTE
- **D.Lgs. 36/2023 Allegato I.7**: Contenuti minimi PFTE (CME tra obbligatori lett. l)
- **D.M. LL.PP. 14/01/2008**: Norme Tecniche Costruzioni (NTC 2018 vigenti)
- **Linee Guida ANAC n. 1/2016**: Servizi di architettura e ingegneria
- **Prezzario Regione Liguria 2025**: Tariffario lavori pubblici regionali
- **DEI Tipografia del Genio Civile 2025**: Prezzi informativi nazionale
- **Reg. UE 651/2014 GBER**: Aiuti di Stato compatibili (intensità aiuto)
- **AACE International**: Cost Estimate Classification System (Classe 4 "Study/Feasibility")
- **DPR 462/01**: Verifiche periodiche impianti messa terra
- **DM 37/08**: Sicurezza impianti elettrici
- **CEI 79**: Sicurezza antintrusione
- **EN ISO 7010**: Segnaletica antincendio
- **DM 388/03**: Pronto soccorso aziendale
- **D.Lgs. 81/08**: Sicurezza lavoro (CSP/CSE)

### 8.2 Linkage con capitoli Studio di Fattibilità

| Riferimento | Linkage |
|---|---|
| **Cap. 4. Perimetro e scope** | DEL-PFTE-12 Quadro Economico + Computo Metrico (il presente A.9 v1.5 è il deliverable) |
| **Cap. 8 §8.3. CapEx baseline** | Cross-check tabella §3.4 (range CapEx Y1 €700k-2M, di cui infrastructure 25-30%) |
| **Cap. 8 §8.5.1.A. OpEx baseline** | Cross-check §4.3 (OpEx GS €73k/anno coerente con voce "Costi sede / utilities") |
| **Cap. 8 §8.5.1.B. Regulatory team** | Cross-check §5.3 (FTE Head Regulatory 20% retainer + DPO 10%) |
| **Cap. 8 §8.7. Mix funding** | Cross-check §7.3 (tranche finanziamento Y1 €470k coerente con mix Coopfond + FESR + R&D) |
| **A.4. ICD interfaces ground segment** | Voci GCS + antenne + storage coerenti con ICD GS-UAV link e GS-Cliente data delivery |
| **A.11. Safety Case SORA** | Vincoli operational requirements impattano dimensionamento GCS (workstation pilota, ridondanza) e cartellonistica |
| **A.12. VIA preliminare** | Vincoli edilizi area Parco Antola: limita alterazioni esterne, favorisce scenario A riuso |
| **A.10. Piano Manutenzione preliminare** | Correlato OpEx §4.1: piano manutenzione GS coerente con cicli e budget |
| **A.6. CAD** | Hangar dimensionamento richiede layout UAV + batterie (decisione M+1) |
| **A.7. Link Budget** | Dimensionamento antenne RF (§2.4) deriva da link budget HAPS/VTOL |
| **A.2. Risk Register** | Voci ATEX, ENAC, AGCOM linkate a RSK-REG-022, RSK-OPS-008, RSK-REG-014 |
| **A.5. V&V Plan** | Collaudo e verifica (§3.2 voce B.6) linkati a test acceptance |

### 8.3 Riferimenti esterni operativi

- **ENAC**: Linee Guida Regolamento UAS 2024; PDRA per BVLOS
- **AGCOM**: Autorizzazione frequenze sperimentali (CEPT/ECC Decision 17-04)
- **ENAV**: NOTAM Origination services
- **Regione Liguria**: PSR + PR FESR 2021-2027 (cofinanziamento)
- **Coopfond**: Bando Cooding Prototypes + Cooding-Invest
- **Open Fiber/TIM**: BUL Liguria mappa copertura
- **Borsino Immobiliare OMI**: zona Torriglia / Pentema valore locazione
- **VVF Genova**: classificazione ATEX storage LiPo (consultazione preventiva)
- **Ente Parco Antola**: nulla osta interventi area protetta

### 8.4 Versioning + history

| Versione | Data | Granularità | Autore | Note |
|---|---|---|---|---|
| v1.0 | M+3 (precedente) | WBS 2 preliminary | CFO Analyst | Skeleton iniziale, 9 KB |
| **v1.5** | **M+5 (presente)** | **WBS 3 (sub-component)** | **CFO Analyst** | **Granularità per ground segment Pentema, review critica Cap. 4 §4.8** |
| v2.0 (prevista) | M+10 | WBS 4-5 investment-grade | Cost Estimator certificato + RUP Liguria | CME definitivo gate G3 |

---

## Disclaimer

Il presente Computo Metrico Estimativo v1.5 è elaborato in conformità a D.Lgs. 36/2023 art. 41 + Allegato I.7 con granularità WBS 3 (livello AACE Classe 4 "Study/Feasibility"). I valori unitari e quantitativi sono stime parametriche basate su prezzari pubblici 2025, listini vendor 2025 e benchmark mercato; **non costituiscono offerta vincolante**. Per l'utilizzo del presente CME ai fini di:

- partecipazione a bandi pubblici (Coopfond, FESR Liguria, PNRR)
- rendicontazione SAL a finanziatori
- procurement contratti definitivi

è obbligatoria la validazione da Cost Estimator certificato AACE/ICCM, la revisione RUP Regione Liguria e le offerte vendor vincolanti (gap M+8-M+9 da §6.3). I range scenario worst/base/best vanno comunicati integralmente, evitando di citare il solo scenario base con pretesa di precisione superiore alla classe AACE 4.

*Documento elaborato dall'agente analisi finanziaria CFO del progetto HALE Firmamento Technologies. Maggio 2026.*
