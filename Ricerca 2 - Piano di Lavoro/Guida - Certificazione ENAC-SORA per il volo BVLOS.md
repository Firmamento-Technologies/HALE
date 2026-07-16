# Guida alla Certificazione ENAC–SORA per il volo BVLOS
## Spiegata in modo semplice, anche per chi non conosce il mondo dei droni

| | |
|---|---|
| **Documento** | Guida chiara al percorso di certificazione per far volare un drone "oltre la vista del pilota" (BVLOS) in Italia. |
| **A chi serve** | A chiunque debba capire **cosa serve, quanto tempo, quanto costa e in che ordine** procedere — senza competenze tecniche pregresse. |
| **Versione / Data** | 0.1 — 2026-07-14 |
| **Collegato a** | `Nota Strategica - Alternativa Superiore a HALE` (di cui questo documento è l'approfondimento certificativo). |
| **Nota** | Quadro EASA/ENAC aggiornato a metà 2026 (Reg. UE 2019/947 e 2019/945; metodo SORA versione 2.5). Tempi e costi delle singole autorizzazioni italiane **non sono pubblici**: dove indicati sono **stime**. |

---

## In una frase

> Per far volare un drone **oltre la distanza a cui il pilota lo vede a occhio nudo** (BVLOS), in Italia **non basta comprare il drone**: serve un **permesso dell'ENAC** che si ottiene superando un'**analisi del rischio chiamata SORA**. Il percorso intelligente è: **iniziare a lavorare (e a incassare) volando "a vista" con permessi semplici, e nel frattempo preparare il permesso per il volo "oltre la vista".**

---

## Glossario — tutte le sigle, in parole semplici

*(Leggi questa tabella prima di tutto: il resto del documento diventa facile.)*

| Sigla | Cosa significa (per esteso) | In parole semplici |
|---|---|---|
| **ENAC** | Ente Nazionale per l'Aviazione Civile | L'**autorità italiana** che concede i permessi di volo ai droni. |
| **EASA** | European Union Aviation Safety Agency | L'**autorità europea** che scrive le regole (l'ENAC le applica in Italia). |
| **VLOS** | *Visual Line of Sight* | Il drone vola **a vista**: il pilota lo vede a occhio nudo. |
| **BVLOS** | *Beyond Visual Line of Sight* | Il drone vola **oltre la vista** del pilota (es. dietro una collina). |
| **EVLOS** | *Extended VLOS* | Vista **estesa** grazie a osservatori a terra che "passano" il drone di vista in vista. |
| **UAS / SAPR** | *Unmanned Aircraft System* / Sistema Aeromobile a Pilotaggio Remoto | Il modo tecnico di dire "**drone**" (velivolo + stazione di controllo). |
| **MTOM** | *Maximum Take-Off Mass* | Il **peso massimo al decollo** del drone. |
| **Classi C0–C6** | Etichette di classe (Reg. UE 2019/945) | "**Cartellini**" che dicono in quale fascia rientra il drone (peso, dimensioni, dotazioni). |
| **Categoria Open / Specific / Certified** | Le tre categorie operative (Reg. UE 2019/947) | Le tre "**corsie**" di rischio in cui può ricadere un'operazione (vedi §1). |
| **SORA** | *Specific Operations Risk Assessment* | Il **metodo di analisi del rischio** che si deve superare per ottenere il permesso di volo in categoria Specific. |
| **ConOps** | *Concept of Operations* | La **descrizione dell'operazione**: cosa fa il drone, dove, a che quota, con quale missione. |
| **GRC** | *Ground Risk Class* | Il **rischio per le persone a terra** (se il drone cade). |
| **ARC** | *Air Risk Class* | Il **rischio di collisione in aria** con altri velivoli. |
| **iGRC** | *intrinsic GRC* | Il rischio a terra "**di partenza**", prima di applicare le contromisure. |
| **SAIL** | *Specific Assurance and Integrity Level* | Il **livello di robustezza/serietà** richiesto all'operazione: da **I** (facile) a **VI** (severissimo). |
| **OSO** | *Operational Safety Objective* | La **lista di obiettivi di sicurezza** da dimostrare (una "checklist" che si allunga col salire del SAIL). |
| **STS** | *Standard Scenario* | Scenari **già pronti e approvati**: se la tua operazione ci rientra, basta una **dichiarazione** (percorso rapido). |
| **PDRA** | *Predefined Risk Assessment* | Un'analisi del rischio **già pre-compilata dall'autorità**: percorso **semi-rapido**, più leggero del SORA completo. |
| **LUC** | *Light UAS Operator Certificate* | Una sorta di "**patente da operatore esperto**" che permette di **auto-autorizzarsi** le operazioni. |
| **DAA** | *Detect And Avoid* | Il sistema che dà al drone la capacità di "**vedere ed evitare**" altri velivoli (fondamentale nel BVLOS). |
| **FTS** | *Flight Termination System* | L'"**interruttore di emergenza**" che ferma il volo in modo sicuro (es. paracadute). |
| **C2 (link)** | *Command and Control link* | Il **collegamento radio** tra pilota e drone (il "telecomando"). |
| **DOP** | *Drone Operation Plan* | Il **piano di volo** da presentare prima di operare. |
| **D-Flight** | Piattaforma nazionale italiana | Il **portale online** dove si registrano drone, operatore e piani di volo. |
| **Remote ID** | *Remote Identification* | La "**targa elettronica**" che identifica il drone mentre vola. |
| **U-space** | Spazio aereo per droni | Il futuro "**sistema di controllo del traffico**" dedicato ai droni (in costruzione). |

---

## 1. Le tre "corsie" del volo: Open, Specific, Certified

Ogni volo di drone ricade in una di **tre categorie**, in base al **rischio**. Pensa a tre corsie:

| Categoria | Quando ci si rientra | Serve un permesso? | Ci si può volare "oltre la vista" (BVLOS)? |
|---|---|---|---|
| 🟢 **Open** (libera) | Basso rischio: drone < 25 kg, **solo volo a vista**, sotto i 120 m, lontano dalle persone | **No** (basta registrarsi e avere il patentino) | ❌ **No, mai** |
| 🟡 **Specific** (a permesso) | Rischio medio: **volo oltre la vista (BVLOS)**, oltre i 120 m, sopra le persone, drone > 25 kg… | **Sì**: autorizzazione ENAC tramite **SORA** (o scorciatoie STS/PDRA/LUC) | ✅ **Sì — è qui che vive il BVLOS** |
| 🔴 **Certified** (come un aereo) | Rischio alto: sopra la folla con drone grande, trasporto persone, casi estremi | Sì, come l'aviazione di linea | (Non è il nostro caso) |

> **La regola d'oro n.1:** la categoria **Open è solo "a vista"**. **Appena vuoi volare oltre la vista (BVLOS), sei automaticamente in categoria Specific e ti serve il SORA** — a prescindere dal peso o dalla classe del drone.

---

## 2. La classe del drone e la "regola dei 3 metri"

Un drone può ricevere un "**cartellino di classe**" (C0…C6). Per la nostra fascia conta la **classe C3**, che richiede **due** condizioni insieme:

- **peso < 25 kg**, **e**
- **dimensione massima < 3 metri** (per un aereo ad ala fissa, la dimensione massima è l'**apertura alare**).

**Perché i 3 metri contano moltissimo?** Perché cambiano il percorso:

| | Drone **C3 pieno** (< 25 kg **e** < 3 m) | Drone < 25 kg **ma con apertura > 3 m** |
|---|---|---|
| Ottiene il cartellino di classe? | ✅ Sì (C3) | ❌ **No** (nessuna classe C: sono tutte sotto i 3 m) |
| Volo **a vista** commerciale | ✅ **Libero, senza permesso** (categoria Open) | ⚠️ **Serve comunque un'autorizzazione** (categoria Specific) |
| Scorciatoie per il BVLOS (STS/PDRA) | ✅ Disponibili come opzione | ❌ **Escluse** (richiedono < 3 m) |
| BVLOS con SORA completo | ✅ Come alternativa | ✅ **Unica strada** |
| Difficoltà/costo del permesso | Più basso | **Più alto** (più documenti da produrre) |

> **La regola d'oro n.2:** superare i **3 metri di apertura alare** non è *vietato*, ma **fa perdere tutte le scorciatoie**: il drone dovrà passare **sempre** per il permesso completo (SORA), anche per volare a vista, e il permesso sarà **più laborioso e costoso**.
>
> **Conseguenza pratica:** tenere il drone **compatto (sotto i 3 m)** e **leggero (sotto i 25 kg)** **riduce tempi e costi di certificazione**. È uno dei motivi per cui un'ala "compatta" (es. box-wing) ha un vantaggio anche *burocratico*, non solo tecnico.

---

## 3. Il SORA spiegato semplice (l'"esame" per ottenere il permesso)

Il **SORA** è il **metodo con cui si dimostra all'ENAC che l'operazione è sicura**. Funziona come un esame a tappe:

1. **ConOps** — *descrivi cosa fai*: che missione, dove, a che quota, su quale zona.
2. **Rischio a terra (GRC)** — *quanto è pericoloso se cade*? Dipende da peso/dimensione del drone e da **quante persone ci sono sotto**. Si abbassa con contromisure (volare su zone spopolate, montare un **paracadute/FTS**).
3. **Rischio in aria (ARC)** — *quanto è probabile scontrarsi con altri velivoli*? Il volo oltre la vista (BVLOS) **lo alza**. Si abbassa scegliendo spazi aerei tranquilli o **segregati**, oppure con sistemi che "**vedono ed evitano**" (DAA).
4. **SAIL (livello di severità)** — dai due rischi sopra esce il **livello di robustezza** richiesto, da **I** (semplice) a **VI** (severissimo). Un tipico volo BVLOS di un drone ~25 kg su zona poco abitata è **SAIL II–IV**.
5. **OSO (la checklist di sicurezza)** — a ogni livello SAIL corrisponde una **lista di obiettivi da dimostrare** (affidabilità del collegamento radio, procedure, addestramento del pilota, qualità di progetto…). Più alto è il SAIL, **più lunga e severa** è la lista.

> In sintesi: **più persone sotto + più traffico in aria + drone più grande = SAIL più alto = più cose da dimostrare = più tempo e più costi.** Il mestiere sta nel **scegliere missioni e aree** che tengano il SAIL **basso**.

---

## 4. Il workflow operativo — dal drone costruito al servizio pagato

Questo è il **percorso consigliato**, passo per passo. L'idea centrale: **si inizia a lavorare e a incassare volando "a vista", mentre si prepara in parallelo il permesso per il volo "oltre la vista".**

| Fase | Cosa si fa | Stato del permesso | Si guadagna? |
|---|---|---|---|
| **0. Progetto della missione** | Si decide *cosa farà* il drone (aree, quote, servizi) → questo determina la difficoltà del permesso | — | — |
| **1. Costruzione del drone** | Si costruisce **già con le dotazioni di sicurezza a bordo** (paracadute/FTS, doppio collegamento radio, "recinto elettronico" geofencing, targa elettronica Remote ID) — aggiungerle dopo costa di più | — | — |
| **2. Cartellino di classe** | Se < 3 m: si dichiara la conformità **C3**. Se > 3 m: niente cartellino → si prepara direttamente il **SORA** | Classe o preparazione SORA | — |
| **3. Collaudo in volo** | Prove in **area riservata** o con **permesso sperimentale** dell'ENAC | Test | — |
| **4. Avvio dei servizi "a vista" (VLOS)** | Con un **permesso semplice**, si iniziano a **vendere servizi** (ispezioni, sorveglianza, monitoraggio). L'azienda mette **il pilota abilitato**, l'operatore registrato, il manuale operativo, il piano di volo su D-Flight | Permesso Specific (a vista) | ✅ **SÌ — qui iniziano i ricavi** |
| **5. Preparazione del permesso BVLOS (in parallelo)** | Si prepara il **SORA completo** per il volo oltre la vista, **usando i dati raccolti volando a vista** come prova di affidabilità | Domanda in corso | ✅ si continua a incassare "a vista" |
| **6. Ottenimento del permesso BVLOS** | Spesso **prima su un corridoio/spazio riservato** (più facile), poi esteso. Si scalano i servizi a **lungo raggio, oltre l'orizzonte** | Permesso Specific (oltre la vista) | ✅ ricavi maggiori |
| **7. (Facoltativo) Patente da operatore (LUC)** | Con esperienza, l'ENAC può concedere la "**patente da operatore esperto**" che permette di **auto-autorizzarsi** le operazioni successive | LUC | ✅ massima libertà operativa |

> **Il cuore del metodo:** le **fasi 4 e 5 avvengono insieme**. Si **fattura da subito** volando a vista (fase 4), mentre il permesso per il volo oltre la vista matura in parallelo (fase 5). I dati di affidabilità raccolti lavorando a vista **sono la prova** che rafforza la domanda BVLOS. Questo modello si chiama **"prima a vista, prima i ricavi"** ed è quello realmente usato dalle aziende italiane (§9).

---

## 5. Quanto tempo e quanto costa

- **Tempo:** l'ENAC **non pubblica** i tempi delle singole autorizzazioni. Come riferimento europeo, un permesso BVLOS richiede in genere **circa 7–18 mesi** (di più se il livello SAIL è alto). Il ritardo più frequente sono le **domande incomplete**, che fanno ripartire il conteggio.
- **Costo:** la **tariffa ufficiale dell'ENAC è di circa 355 €** — cioè **quasi nulla**: è solo la "marca da bollo". Il **costo vero** sta altrove: le **dotazioni di sicurezza** (paracadute/FTS, doppio radiocomando, sistemi anticollisione), la **consulenza specializzata**, la **documentazione** e le **prove di volo**. Nessuna azienda italiana ha reso pubbliche queste cifre → **vanno considerate stime**.

> **Attenzione a non farsi ingannare:** i 355 € del permesso sono un **falso indizio**. Il conto vero è ingegneria + consulenza + test, ed è **riservato** presso tutti gli operatori.

---

## 6. Come ci si mantiene mentre si aspetta il permesso BVLOS

Ci si mantiene **vendendo servizi "a vista" (VLOS)**, che **non richiedono il permesso BVLOS**:

- Esiste un **mercato consolidato di servizi con drone** (ispezioni, rilievi, sorveglianza) in cui l'azienda **fornisce il pilota e il servizio**. È attivo da anni e paga.
- **Esempio reale:** **E-Distribuzione (gruppo Enel)** ha fatto **prima** una grande operazione **a vista** (centinaia di piloti e droni per ispezionare le linee elettriche) e **solo dopo** ha ottenuto il volo oltre la vista: per lei il BVLOS è stato un **miglioramento su ricavi che già esistevano**.
- Le startup (es. **ABzero**, consegne mediche) si mantengono con **dimostrazioni, progetti pilota in aree sperimentali ("sandbox"), partnership e fondi pubblici** finché il servizio a regime non parte.

---

## 7. Cosa bisogna aggiungere al drone per ottenere il permesso

> 📄 **Per prezzi, prodotti (Italia/estero) e stima costi** di ognuna di queste dotazioni, più il workflow di equipaggiamento, vedi il documento **`Guida - Tecnologie e Costi per la Certificazione BVLOS (superare gli OSO)`**.

Le **modifiche tecniche** più richieste dall'ENAC (per superare gli "obiettivi di sicurezza" OSO):

- **Paracadute / sistema di arresto del volo (FTS)** — la contromisura più citata: ferma il drone in sicurezza in caso di guasto.
- **Doppio collegamento radio (C2 ridondante)** — se un canale si perde, ce n'è un altro.
- **Sistema anticollisione (DAA)** — oppure, in alternativa, **volare in uno spazio aereo riservato** dove non c'è altro traffico (è la scorciatoia più usata oggi).
- **"Recinto elettronico" (geofencing) e targa elettronica (Remote ID)** — il drone non esce dall'area consentita ed è sempre identificabile.
- **Piano di volo su D-Flight** per ogni operazione, e **pilota con corso avanzato** (gestione delle emergenze + SORA).
- **Prove di robustezza di progetto e produzione** — richieste quando il livello SAIL è alto (III o superiore), vicine a quelle di un vero aeromobile.

---

## 8. Gli ostacoli veri (perché costruire il drone è la parte facile)

Molte aziende italiane **hanno il drone ma non il permesso BVLOS**. I motivi ricorrenti:

1. **Il "vedere ed evitare" (DAA) è ancora immaturo.** Oltre la vista, il pilota non può schivare gli ostacoli a occhio: servirebbe un sistema automatico affidabile, che a questa scala **non esiste ancora maturo ed economico**. La soluzione pratica è **volare in spazi aerei riservati** (aggirando il problema, non risolvendolo).
2. **L'ENAC considera il BVLOS "a rischio alto"** e ancora in gran parte **sperimentale** (poche aree "sandbox" attive).
3. **I livelli SAIL alti richiedono prove di progetto quasi da aeromobile** — care e lunghe.
4. **Lo spazio aereo per droni (U-space) è ancora in costruzione**, e non è chiaro chi ne paghi i costi.
5. **Ostacoli non aeronautici:** anche col permesso di volo, le **basi/piazzole di decollo possono richiedere permessi edilizi comunali**; certi trasporti (es. sangue) attivano le regole sulle **merci pericolose**.

> **Il messaggio:** costruire un drone dimostra la **macchina**. Il permesso BVLOS richiede invece di dimostrare la **sicurezza dell'intera operazione come sistema** (rischi a terra e in aria, radiocomando, procedure, spazio aereo, permessi locali). È un problema **di sistema e di regole**, non di sola meccanica.

---

## 9. Chi in Italia ha già ottenuto il volo BVLOS (la concorrenza e i progetti pubblici)

Chi è arrivato al volo oltre la vista in Italia sono soprattutto **utility, grandi gruppi aerospaziali e poche startup ben assistite** — quasi sempre con una **consulenza specializzata** e spesso **confinati a corridoi o spazi riservati**.

| Chi | Cosa fa | Che permesso ha ottenuto | Anno | In parole semplici |
|---|---|---|---|---|
| **E-Distribuzione** (Enel) | Ispezione linee elettriche | **1° volo BVLOS "non geografico" d'Italia** (percorso semi-rapido IT-PDRA-01) | **2022** | Ha fatto **prima i ricavi a vista**, poi il BVLOS |
| **Telespazio** (Leonardo/Thales) | Infrastrutture, agricoltura, consegne mediche | Permesso BVLOS **come operatore** (piattaforma propria) | **2024** | Permesso "di azienda", non di singola rotta |
| **FlyingBasket** (Bolzano) | Trasporto merci pesanti in montagna | **1ª "patente da operatore" (LUC) d'Italia** | **2024** | La posizione più forte: **si auto-autorizza** |
| **ABzero** (Pisa) | Consegne mediche (sangue, organi) | **1ª rotta medica BVLOS di 37 km** (Isole Eolie) | **2024** | Opera in area sperimentale ("sandbox") |
| **UrbanV + Speedbird** | Consegne in città | **1° permesso di livello SAIL III d'Italia** (città, sopra autostrada e ferrovia) | **2026** | Il caso più complesso mai autorizzato in Italia |
| **Horus Technologies + Hangar 84** | Drone **ad ala fissa con decollo verticale** (il più simile al nostro) | Permesso operativo ENAC, ma **BVLOS dentro uno spazio aereo riservato (R315)** | **2024–25** | Ha risolto il rischio-aria **con lo spazio riservato**, non col "vedere ed evitare" |
| **Aermatica3D** | Agricoltura + **fornitore di paracadute/FTS** | Permesso in categoria Specific; **vende il "kit autorizzazione ENAC"** ad altri | 2022–24 | Ha fatto del **paracadute di sicurezza** un prodotto |
| **Polizia Locale "Colline Moreniche"** | Sorveglianza pubblica | **1° permesso BVLOS con scenario PDRA-G03** (ente pubblico) | **2025** | Anche un ente pubblico ci è riuscito |

> **Cosa ci insegna questa tabella:**
> - Il caso **più vicino a noi** (Horus, ala fissa a decollo verticale) ha ottenuto il BVLOS **solo dentro uno spazio aereo riservato** → per iniziare conviene puntare su **corridoi o spazi riservati**, non sul volo libero.
> - **Tutti** hanno iniziato **generando ricavi a vista** o con progetti dimostrativi, **prima** di avere il BVLOS a pieno regime.
> - **Nessuno** ha reso pubblici **tempi e costi**: vanno chiesti a una **consulenza specializzata** (in Italia la più presente nei casi-simbolo è **EuroUSC Italia**).

---

## 10. In sintesi (per chi ha fretta)

1. **BVLOS = categoria Specific = serve il permesso ENAC** ottenuto col metodo **SORA**. Punto.
2. **Sotto i 3 metri e sotto i 25 kg** = percorso **più semplice ed economico**. Sopra i 3 metri = **sempre permesso completo**.
3. **Si va a mercato subito volando "a vista"** (con pilota e servizio nostro) e **si prepara il BVLOS in parallelo**: si incassa mentre il permesso matura.
4. **Il primo BVLOS conviene farlo in spazio riservato** (aggira il problema del "vedere ed evitare", ancora immaturo).
5. **Il costo vero non è la tariffa ENAC (355 €)**, ma dotazioni di sicurezza + consulenza + test (cifre riservate → stime).
6. **Servono una consulenza specializzata presto** e **un progetto di drone compatto e leggero** per abbassare tempi e costi.

---

## Fonti principali
- **Regole europee:** Reg. UE 2019/947 (categorie di volo) e 2019/945 (classi di drone); metodo **SORA 2.5** (EASA, ED Decision 2025/018/R, in vigore dal 29/09/2025).
- **ENAC:** categoria Specific, PDRA nazionali IT-PDRA-01…09, piattaforma D-Flight — https://www.enac.gov.it/sicurezza-aerea/droni/categoria-specifica-specific-category/
- **Casi italiani BVLOS:** E-Distribuzione (EuroUSC Italia), Telespazio (T-DROMES), FlyingBasket (LUC), ABzero (Eolie 37 km), UrbanV/Speedbird (SAIL III 2026), Horus Songbird (R315), Aermatica3D (FTS) — dettaglio fonti in `Nota Strategica - Alternativa Superiore a HALE`, §Fonti esterne.
- **Consulenza SORA in Italia:** EuroUSC Italia (la più presente nei casi-simbolo), Murzilli Consulting (europea).

> ⚠️ **Onestà:** i **tempi e i costi** delle singole autorizzazioni italiane **non sono pubblici** (consulenza e ingegneria riservate). I riferimenti temporali/economici qui riportati sono **stime** o **benchmark europei**, da confermare con una consulenza specializzata e con l'ENAC (incluse la scadenza di transizione al SORA 2.5 e l'eventuale PDRA nazionale applicabile al nostro caso).
