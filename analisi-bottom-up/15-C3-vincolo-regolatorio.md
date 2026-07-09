# 15 — La classe C3 è un vincolo troppo stringente per il drone di servizio-consegna T1? Restarci o uscirne?

> **Analisi bottom-up — Percorso "servizio-first / famiglia modulare"**
> Firmamento Technologies — piattaforma T1 (VTOL/box-wing, "BOXY", ≤25 kg, ~3 m) e missioni EO / consegna medicale / relay / sorveglianza.
> **Autore:** Aviation Regulatory Counsel (EASA / ENAC / U-Space)
> **Data:** 2026-07-09
> **Base:** estende e chiude un punto lasciato aperto da `13-fasce-regolatorio-missione.md` (matrice missione×fascia), `04-regolatorio.md` (gradiente per classe di piattaforma), `10-fasce-engineering.md` §3 (T1/BOXY).
> **Domanda guida:** la marcatura di classe **C3** (e il suo tetto ≤25 kg / <3 m) limita indebitamente il drone di servizio-consegna, o è in gran parte **irrilevante** per la missione perché la consegna vive comunque in **Specific**? Conviene progettare il T1 "C3-bound" o "Specific-native"?

---

## 0. Disclaimer epistemico (fatto normativo vs stima)

- **[FATTO]** = testo di regolamento/AMC/GM in vigore, citato con articolo/riga e fonte nel repo.
- **[STIMA]** = valutazione di chi scrive (iGRC/SAIL, costi, tempi, robustezza SORA). Confidenza dichiarata caso per caso.
- **Regola dura del progetto:** nessuna classificazione SORA/SAIL è definitiva finché ENAC non la conferma in **pre-application** (art. 11 Reg. (UE) 2019/947). Tutti i valori qui sono *preliminary-grade*.
- **Riserva sulle fonti:** le classi **C5/C6** e gli **STS-01/STS-02** in versione consolidata **non sono nel file di repo** `CELEX_32019R0945_IT_TXT.md` (fermo all'edizione 2019, prima degli emendamenti Reg. delegato (UE) 2020/1058 per C5/C6 e Reg. esecuzione (UE) 2020/639 per gli STS). Il repo contiene però la **descrizione degli scenari standard** all'Allegato Parte B §1 (righe 1182–1202) che è quanto serve. Dove cito C5/C6 in dettaglio tecnico lo marco **[FATTO con riserva — da verificare edizione in pre-app]**.

---

## 1. Il fraintendimento da sciogliere per primo: **classe C-marking (C3) ≠ categoria operativa (Open/Specific/Certified)**

È l'errore concettuale che rende la domanda "C3 è troppo stringente?" mal posta. Sono **due assi ortogonali**:

- **La classe C0–C6** è una **etichetta di prodotto** apposta dal *fabbricante* sul velivolo (marcatura CE + etichetta di classe) attestante conformità a un set di requisiti tecnici del **Reg. (UE) 2019/945** (design & manufacture). È una **proprietà dell'oggetto**. Per C3: MTOM < 25 kg, dimensione caratteristica < 3 m, altezza limitabile a 120 m, RID (identificazione remota diretta), geo-awareness, datalink protetto, 48 V max, ecc. **[FATTO]** — `CELEX_32019R0945` Parte 4, righe 1795–1936 (in particolare punto 1, riga 1804: «MTOM inferiore a 25 kg… dimensione caratteristica massima inferiore a 3 m»).
- **La categoria Open/Specific/Certified** è una **proprietà dell'operazione** (rischio del volo), decisa dagli artt. 4/5/6 del **Reg. (UE) 2019/947** (operations). **[FATTO]** — `CELEX_32019R0947` righe 293–367.

**Il nesso tra i due assi è a senso unico e debole:** la classe C-marking serve **solo** come *biglietto d'ingresso a una sotto-categoria della Open* (e come pre-requisito di alcuni STS della Specific). Una volta che l'operazione **esce dalla Open**, la classe C-marking del velivolo diventa **quasi ininfluente** ai fini della SORA: la SORA 2.5 non "legge" l'etichetta C3, legge **dimensione caratteristica × velocità × densità di popolazione** (Tabella iGRC) e la classe di spazio aereo (ARC). **[FATTO]** — `annex_to_ed_decision_2025-018-r_1` Table 1 (iGRC), Table 3 (SAIL); coerente con `04-regolatorio.md` §1.2 e §5.

> **Corollario-chiave n.1:** chiedersi "il C3 è troppo stringente per la consegna" equivale, per il ~90% dei suoi effetti, a chiedersi "la sotto-categoria **Open A3** è troppo stringente per la consegna". E la risposta a *questa* domanda è già nel repo: **per la consegna la Open è preclusa a monte, a qualunque peso** (§2). Quindi il C3, come *lasciapassare-Open*, per la consegna **non compra nulla**.

### 1.1 Cosa "compra" davvero la marcatura C3 [FATTO]

| Ciò che C3 **abilita** | Base | Ciò che C3 **NON abilita / impone come tetto** |
|---|---|---|
| Operare in **Open sotto-categoria A3** («far from people»): VLOS, ≤120 m AGL, ≥150 m orizzontali da aree residenziali/commerciali/industriali/ricreative, **nessuna persona non coinvolta sorvolata**. **[FATTO]** `UAS.OPEN.040` (rif. `04` §1.1, righe 1030–1046) | Reg. 947 art. 4 + Allegato Parte A | **No BVLOS** in Open; **no sorvolo persone**; **no rilascio materiale**; **no trasporto merci pericolose** (art. 4 lett. f, riga 305) |
| Fungere da **pre-requisito di prodotto** per alcuni scenari standard (via kit di conversione a classe C5/C6) | Reg. 947 App. 1 (STS) | Il **tetto fisico**: MTOM < 25 kg **e** dimensione < 3 m (`945` riga 1804). Superarli = **non sei più C3** (e nemmeno più Open) |
| Requisiti di sicurezza "gratuiti" già a bordo utili anche in Specific: RID, geo-awareness/geo-fencing, datalink protetto, RTH/flight-termination su perdita link, low-battery warning, luci notturne | `945` righe 1806–1895 (punti 2, 5, 9, 10, 12, 13, 14) | Nessuna abilitazione BVLOS o su-persone: sono *igiene di base*, non *robustezza SORA* certificata |

**Lettura:** ciò che C3 realmente "compra" è **(a) l'accesso a Open A3 per l'EO VLOS lontano dalle persone** e **(b) un pacchetto di funzioni di sicurezza che, pur non essendo prova di conformità agli OSO, riducono il lavoro di argomentazione in SORA** (la geo-awareness e il datalink protetto sono capitalizzabili come mitigazioni tecniche). Il **prezzo** è il tetto rigido dei 25 kg / 3 m. Il punto è che quel prezzo lo paghi **solo se ti serve il biglietto Open A3**; per tutto ciò che è BVLOS/consegna/su-abitato quel biglietto non lo usi.

---

## 2. Il vincolo ≤25 kg / ~3 m è "troppo stringente"? Il "cliff dei 25 kg" analizzato

### 2.1 Il confine dei 25 kg è un **cliff netto SOLO in Open** [FATTO]

- In **Open** i 25 kg sono un muro binario: art. 4 lett. b, riga 297 — «massa massima al decollo **inferiore a 25 kg**». A 25,0 kg **esci dalla Open, punto**, indipendentemente da tutto il resto. È il classico *cliff*.
- In **Specific** i 25 kg **non sono un cliff**: non compaiono come soglia negli artt. 5/6 né nella SORA. Il peso entra **indirettamente e con continuità**, per tre vie (già in `04` §3, SOGLIA 2):
  1. come **proxy di dimensione/velocità** nella Tabella iGRC — ma la SORA usa *dimensione caratteristica × velocità*, non la massa (`annex` Table 1, righe 997–1028);
  2. come **proxy di energia d'impatto** → rende più difficile rivendicare la mitigazione **M2** (riduzione energia d'impatto, paracadute/BRS) alla robustezza voluta (`annex` Table 5, righe 1261–1273);
  3. come **driver del premio assicurativo** e della robustezza attesa degli OSO tecnici.

> **Corollario-chiave n.2:** superare i 25 kg **non** fa scattare la Certified (lo fanno solo assembramenti/trasporto persone/DG ad alto rischio o GRC>7 — art. 6, righe 351–367; `04` §1.1). Superarli significa **perdere l'opzione Open** (che per la consegna **hai già perso comunque**) e pagare, in Specific, **frazioni di SAIL** — non un salto di categoria. Il "cliff" a 25 kg, per una missione già-Specific, si **appiattisce in una rampa**.

### 2.2 Quindi: superare i 25 kg conviene per la consegna?

**[STIMA, confidenza medium-high]** Sì, *condizionatamente*, **se e solo se la missione lo richiede** (payload cargo + BRS + ridondanza + endurance). Ragionamento:

- Per la consegna sei **già in Specific** (§3). Il beneficio-Open del restare ≤25 kg è **nullo**.
- Il payload di consegna medicale utile (capsula termica sangue/campioni + defibrillatore + margine) più il **contenimento certificato del carico** richiesto fuori-SORA (`annex` §S.1.3(c), righe 311–315) più un **BRS/paracadute** più **ridondanza** (per tenere gli OSO tecnici a SAIL III) sono voci che **erodono rapidamente il budget di massa** di un ≤25 kg. `10-fasce-engineering.md` §3.2 stima per BOXY un payload utile di soli **3–5 kg** a 25 kg MTOM: risicato per cargo + BRS + contenimento insieme.
- Il **costo regolatorio marginale** di stare a, poniamo, 30–40 kg (fascia T2) rispetto a 24 kg **non è il salto Open→Specific** (già pagato) ma **+1 gradino di SAIL al più** (iGRC che sale di ~1 per l'aumento di dimensione/velocità, e M2 più difficile): da SAIL II a SAIL III (`04` tabella §2, righe 84–86). È un **incremento marginale gestibile**, non un muro.

**Conclusione §2:** per la **consegna**, il tetto C3/25 kg è un **vincolo di *ingegneria* travestito da vincolo *regolatorio***. Regolatoriamente non ti dà quasi nulla (il biglietto Open non lo spendi) e ti costa un tetto di massa che il payload di consegna fatica a rispettare. **Non è "troppo stringente" nel senso di alzare la categoria — è "gratuito e inutile" per questa missione, e potenzialmente controproducente se ti costringe a comprimere payload/BRS/contenimento sotto la soglia di sicurezza.**

---

## 3. Per ciascuna missione: C3 è vincolante o irrilevante?

Sintesi missione-per-missione del *valore reale* della marcatura C3. (Basata su `13` matrice §2 e `04` §2.)

| Missione | C3 è vincolante o irrilevante? | Dove il tetto C3 **costa capacità senza dare beneficio regolatorio** |
|---|---|---|
| **EO / sensing** | **Rilevante — l'unico caso in cui C3 vale.** È l'unica missione che può *davvero* partire in **Open A3 VLOS** (nessun trigger di missione, `13` §1.4) sfruttando il biglietto C3. Qui il C3 è una **scorciatoia legittima** per il collaudo e i primi servizi EO su versanti disabitati (`04` G0). | Poco: l'EO VLOS ci sta comodo nel tetto. Il costo appare **solo** quando l'EO scala a **BVLOS area-vasta** (Specific SAIL II) e vorresti più endurance/payload di quanto 25 kg concedano — lì il C3 diventa una gabbia autoimposta. |
| **Consegna medicale** | **Irrilevante (anzi controproducente).** Open esclusa a monte (art. 4 lett. f: né trasporto DG né *rilascio di materiale*; `13` §1.1, riga 305). Sei **sempre Specific**, a qualunque peso. Il biglietto Open del C3 **non si spende mai**. | Alto: il tetto 25 kg comprime payload cargo + **contenimento** (`annex` §S.1.3(c)) + **BRS/M2** + ridondanza, che per la consegna servono *tutti insieme*. C3 qui **costa capacità e non compra categoria**. |
| **Connettività / relay** | **Irrilevante ai fini SORA** (il payload radio è massa+antenna, non alza il SAIL — `13` §1.3). Il C3 conta solo se il relay gira *come payload sulla base EO Open/Specific*. Il collo di bottiglia è lo **spettro** (AGCOM/MNO-hosting), non la classe (`04` §4). | Medio: il tetto 25 kg limita antenna/potenza/endurance del nodo relay; ma il vero vincolo è spettro, non C3. |
| **Sorveglianza** | **Irrilevante come classe; vincolante come *overlay privacy*.** Il loiter persistente su abitato alza l'iGRC (Specific SAIL II–III) e attiva **DPIA + art. 34 ENAC + Garante** (`13` §1.2). Nessuno di questi oneri dipende dal C3. | Il C3 non tocca il binario privacy; il tetto 25 kg limita solo il gimbal/endurance. |

> **Corollario-chiave n.3:** la marcatura C3 dà valore regolatorio reale **in una sola delle quattro missioni** — l'**EO in fase VLOS iniziale**. Per le altre tre è, ai fini di categoria, **irrilevante**, e per la **consegna** è **attivamente controproducente** (comprime la massa dove serve di più senza regalare alcuna abilitazione).

---

## 4. Percorsi alternativi: se si esce da C3, dove si va?

Se il T1-consegna non deve essere C3, **cosa diventa**? Tre opzioni, non mutuamente esclusive nel tempo.

### 4.1 Opzione A — **Specific-native, "dimenticando" la marcatura C3** [FATTO/STIMA]
Progettare il velivolo per **soddisfare gli OSO del SAIL target (II–III)**, non per superare l'esame di tipo C3. In Specific la **conformità è all'operazione** (SORA + OSO), non a un'etichetta di prodotto: l'autorità valuta il **safety case**, non la marcatura CE-classe (art. 5, righe 314–323). Il velivolo può essere **>25 kg** e **>3 m** se serve; deve solo dimostrare gli OSO alla robustezza richiesta. È il regime in cui operano i comparabili delivery (ABzero, Matternet+Swiss Post, Everdrone — `13` §3.6): **nessuno di loro è "un C3"**; sono operatori Specific con safety case dedicato.

- **Pro:** libera il progetto dal tetto 25 kg/3 m; dimensiona payload/BRS/contenimento sul fabbisogno reale; è **la via dei comparabili**.
- **Contro:** perde il biglietto Open A3 → **niente collaudo/EO "facile" in Open**; ogni volo richiede autorizzazione Specific fin dal test.

### 4.2 Opzione B — **Specific via STS / classi C5–C6** [FATTO con riserva]
Gli **scenari standard** riducono l'onere (dichiarazione al posto della SORA piena). Il repo descrive gli STS all'Allegato Parte B §1 (righe 1182–1202):
- **STS-01**: VLOS su **area a terra controllata**, UA fino a **3 m**, ≤120 m, spazio non controllato (righe 1188, 1197–1199). Richiede **classe C5** (C3 + kit di conversione a bassa velocità/terminazione) **[FATTO con riserva]**.
- **STS-02**: **BVLOS** su **area a terra controllata** in ambiente scarsamente popolato, UA fino a **3 m**, ≤120 m (righe 1193–1195), con osservatori dello spazio aereo. Richiede **classe C6** **[FATTO con riserva]**.

**Applicabilità alla consegna:** **debole**. Entrambi gli STS vincolano a una **«area a terra controllata»** lungo l'operazione (righe 1188, 1195): la rotta di consegna che **attraversa terreno con edifici sparsi** e **consegna al borgo** non è "area controllata" per tutta la sua estensione (`13` §3.4). L'STS-02 è *vicino* al profilo di **transito EO rurale**, non a quello di consegna su abitato. Utile quindi per **EO/relay rurale**, marginale per la consegna.
> Nota: le classi **C5/C6** sono di fatto **un C3 "vestito" con kit di conversione** (low-speed mode, terminazione, tethering per C5). Quindi "uscire da C3 verso C5/C6" **non** è abbandonare il tetto 25 kg/3 m — è **restare dentro lo stesso inviluppo fisico** aggiungendo funzioni per accedere agli STS. È un *lateral move*, non un *escape*.

### 4.3 Opzione C — **PDRA (S01/G01/G03)** [FATTO parziale]
I **PDRA** (AMC EASA all'art. 11) coprono profili BVLOS ricorrenti (tipicamente SAIL II, UA fino a ~3 m) su ambiente scarsamente popolato/controllato, evitando la SORA piena **se il ConOps vi rientra** (`13` §3.4). **Il testo integrale non è nel repo** — numero/edizione **da verificare in pre-app** [FATTO con riserva]. Nessun PDRA/STS "delivery su area popolata" risulta adottato al cutoff. Per la **rotta rurale** possono ridurre l'onere; per l'**approccio al borgo con sorvolo di non-coinvolti** si torna alla **SORA piena**.

### 4.4 Verdetto §4 — "C3-bound" per il collaudo/EO, "Specific-native" per la consegna [STIMA, confidenza medium-high]

La domanda "il drone di consegna dovrebbe essere C3 o Specific-native?" ha una risposta **a doppio binario**, perché il *velivolo di collaudo/EO* e il *velivolo di consegna* possono e dovrebbero essere trattati come **due configurazioni**:

- La marcatura **C3 conserva un valore reale solo come "scorciatoia Open A3" per il collaudo iniziale e i primi servizi EO VLOS** (`04` G0): permette di volare **subito, settimane, €1–5k, zero SORA**. È un **acceleratore di time-to-first-flight e di track-record ENAC**, non una scelta di architettura di servizio.
- Il **velivolo di consegna va progettato Specific-native fin dall'inizio**, **ignorando il tetto C3** come vincolo di missione: dimensionare payload cargo + contenimento + BRS + ridondanza sul fabbisogno del SAIL II–III, anche a costo di superare 25 kg/3 m (il che, ribadito, **non** alza la categoria — §2.1).

> **In una frase:** *il C3 è una porta d'ingresso per l'EO, non una gabbia per la consegna. Tienilo per far volare presto il dimostratore EO; buttalo via quando dimensioni il cargo.*

---

## 5. Implicazioni regolatorie delle architetture VTOL (tilt-rotor/tilt-wing vs quadplane) [STIMA, confidenza medium]

La domanda è: **la complessità meccanica del VTOL ha un costo regolatorio?** In SORA 2.5 la categoria (Open/Specific) **non cambia** con l'architettura, ma il **peso della dimostrazione OSO** sì. Analisi qualitativa:

- **Dove la complessità NON conta (direttamente):** la SORA non premia né penalizza tilt vs quadplane *di per sé*. iGRC e ARC sono funzione di dimensione/velocità/densità/spazio aereo, non del meccanismo di transizione (`annex` Table 1/Table 3).
- **Dove la complessità conta (indirettamente, e parecchio):** gli **OSO tecnici** che scalano col SAIL — in particolare quelli su **affidabilità/robustezza tecnica del velivolo**, **containment** e **gestione del failure in transizione**. Un **tilt-rotor/tilt-wing** ha un **modo di guasto critico aggiuntivo** (fallimento della transizione hover↔crociera: attuatori di tilt, sincronizzazione, stallo asimmetrico) che un **quadplane** (lift+cruise, rotori di sostentamento e di crociera separati e sempre nella stessa configurazione) **non ha**. Questo si traduce, a parità di SAIL, in:
  - **più assunzioni da dimostrare** negli OSO di design/affidabilità (più analisi FMECA/FTA, più prove) → più tempo e costo di compliance;
  - **M2/containment più difficile da argomentare**: un guasto in transizione a bassa quota degrada l'efficacia del **BRS** (paracadute inefficace sotto una certa quota/assetto), indebolendo la mitigazione dell'energia d'impatto;
  - **maggiore superficie di attacco per il regolatore avversariale** (§6): più meccanismi = più "dimostrami che è sicuro".
- **Quadplane (lift+cruise):** meccanicamente ridondante e "boring" — più massa/drag, ma **una storia di sicurezza più semplice da raccontare in SORA**: nessuna transizione meccanica critica, failure modes più segregati, BRS più facilmente efficace.

> **Corollario-chiave n.4:** a parità di missione/SAIL, **la complessità meccanica non alza la categoria ma alza il costo e il rischio di *dimostrazione*** (OSO tecnici, containment, tempi ENAC). Per un operatore che deve **massimizzare la probabilità e la velocità di autorizzazione** su una missione ad alta sensibilità (consegna medicale su borgo), **l'architettura più semplice difendibile (quadplane) è regolatoriamente preferibile** al tilt-rotor/tilt-wing, salvo che le prestazioni lo impongano. Coerente con lo spirito bottom-up "minimo attrito" di `04`/`13`.

---

## 6. Prospettiva avversariale: come ENAC/EASA userebbe classe e complessità per dire NO/rallentare [STIMA, confidenza medium]

(Incorpora la logica `regulatory-adversary`.) Un regolatore che voglia legittimamente rallentare troverebbe questi appigli:

1. **"Il vostro velivolo di consegna non è marcato C3 (è >25 kg): dimostratemi tutto in SORA piena."** — Non è un blocco (è corretto: sei in Specific), ma può essere usato per **negare qualsiasi scorciatoia** (STS/PDRA) e imporre la SORA completa con OSO ad alta robustezza. **Mitigazione:** ConOps chirurgico + safety case pre-costruito sui comparabili (ABzero/Matternet); non contare su STS.
2. **"Il velivolo è C3 ma lo usate per consegnare: la marcatura non copre l'operazione."** — Trappola inversa: se si *insistesse* sul C3 per la consegna, ENAC osserverebbe che la classe C3 **non autorizza alcun rilascio** (art. 4 lett. f). **Mitigazione:** non presentare mai la consegna come "operazione C3"; presentarla come Specific pura.
3. **Complessità del tilt-rotor come leva OSO.** — «La transizione è un single point of failure non adeguatamente mitigato per il SAIL richiesto»: richiesta di prove di affidabilità aggiuntive, allungamento istruttoria (art. 12.5 Reg. 947; art. 6 L. 241/1990 → integrazioni ripetute, `04` RA-02). **Mitigazione:** architettura semplice difendibile (§5) o dossier di affidabilità della transizione robusto *prima* della domanda.
4. **Rischio-precedente sul contenimento merci pericolose.** — Per la consegna medicale (UN3373/UN1845) ENAC può alzare l'asticella del **contenimento** (`annex` §S.1.3(c)) chiedendo una dimostrazione quasi-certificativa, perché **non esiste precedente italiano consolidato** e teme di "fare giurisprudenza". **Mitigazione:** escludere dal ConOps Cat. A e assembramenti (evita Certified, `13` §3.2); proporre un protocollo di contenimento mutuato da comparabili EASA-associati (Matternet/FOCA).
5. **Uso del "no framework HAPS/MALE" come alone di sospetto.** — Se il T1 viene presentato dentro una narrativa "famiglia fino a HALE", il regolatore può **contaminare** la valutazione del T1 con la diffidenza verso il T4. **Mitigazione:** **scorporare nettamente** la domanda T1 (Specific, maturo) da qualsiasi riferimento HALE/MALE (Certified, fuori orizzonte — `04`/`13` invariato).

---

## 7. Raccomandazione netta e sequenza a gradini

**Restare dentro C3? Uscirne? Progettare Specific-native ignorando C3?** → **La risposta corretta è "tutte e tre, ma su oggetti diversi e in tempi diversi".** Non c'è un solo velivolo la cui unica scelta è C3 sì/no; ci sono **una configurazione di collaudo/EO** (per cui C3 vale) e **una configurazione di consegna** (per cui C3 è irrilevante/dannoso). Sequenza coerente con `13` §7:

- **S0 — Subito (settimane, €1–5k): dimostratore EO in Open A3, *sfruttando* la marcatura C3.** VLOS su versanti disabitati. Qui il C3 **compra** il time-to-first-flight e il track-record ENAC. **Tienilo.** *(È l'unico punto in cui C3 è un asset.)*
- **S1 — 9–18 mesi (€25–70k): EO BVLOS in Specific, SAIL II.** Da qui in avanti la marcatura C3 **smette di dare valore di categoria**: conta il ConOps + gli OSO. Il velivolo può restare fisicamente C3-compatibile (comodo, ma non necessario). Base autorizzativa madre riusabile.
- **S3 — 12–24 mesi (€50–150k): consegna medicale in Specific, velivolo *Specific-native*.** **Qui si "esce" da C3 come vincolo di progetto:** dimensionare payload cargo + **contenimento** (`annex` §S.1.3(c)) + **BRS** + ridondanza sul fabbisogno del **SAIL II–III**, anche superando 25 kg/3 m se serve (non alza la categoria — §2). **Architettura VTOL la più semplice difendibile** (quadplane preferito al tilt, §5). Escludere Cat. A/assembramenti (evita Certified). Modellare su ABzero/Matternet.
- **S4 — solo Y3+ (volumi/varietà alti): LUC come leva di scala**, **non** porta d'ingresso (`13` §6). Auto-autorizzazione multi-missione una volta maturi SMS e track-record.
- **Fuori orizzonte finanziabile:** MALE (T3) e **HALE (T4)** — Certified, framework HAPS assente, ENAV FL195+, spettro non licenziato (showstopper RSK-REG-001, invariato).

### 7.1 Riga di fondo

**La classe C3 NON è "troppo stringente" per il drone di consegna — è in gran parte *irrilevante*, e per la sola parte in cui morde (il tetto 25 kg/3 m) è un vincolo di *ingegneria autoimposto*, non un vincolo *regolatorio*.** Il ragionamento: (1) C3 è una marcatura di prodotto il cui unico vero potere è aprire la **Open A3**; (2) per la **consegna la Open è preclusa a monte** (art. 4 lett. f), quindi quel potere **non si spende mai**; (3) restare ≤25 kg per rispettare il C3 **non abbassa la categoria** (resti Specific comunque) ma **comprime payload/BRS/contenimento** dove servono di più. **Raccomandazione netta:** **tenere la marcatura C3 come "scorciatoia Open A3" per il solo dimostratore/EO iniziale** (dove è un genuino acceleratore), e **progettare il velivolo di consegna "Specific-native", ignorando il tetto C3**, con l'**architettura VTOL più semplice difendibile** per minimizzare l'onere OSO. Non "restare in C3" né "uscirne" come scelta binaria su un unico velivolo: **usare C3 dove serve, dimenticarlo dove pesa.** Nulla di ciò è definitivo finché ENAC non conferma la classificazione in **pre-application** (art. 11).

---

## 8. Falsifying observations e domande da chiudere in pre-application ENAC (M+0–3)

Almeno cinque osservazioni **falsificanti** / domande aperte. Se una di queste risultasse vera nel senso "sfavorevole", parte della tesi di questo documento cadrebbe.

1. **FO-1 (falsifica §2 e §4):** *esiste un vincolo assicurativo o di bando* (Coopfond/PA) *che impone la marcatura C3 come requisito di ammissibilità*? Se sì, "uscire da C3" ha un costo commerciale che l'analisi regolatoria da sola non cattura. → **Da verificare nei capitolati.**
2. **FO-2 (falsifica §2.2):** *un velivolo di consegna a 30–40 kg tiene davvero SAIL III, o l'aumento di dimensione/velocità + M2 più difficile lo spinge a SAIL IV*? Se salta a IV, il "cliff appiattito" torna ripido e il ≤25 kg riacquista valore. → **Pre-app: soglia dimensione/velocità oltre cui ENAC scatta da III a IV** (cfr. `04` OQ-4).
3. **FO-3 (falsifica §4.2):** *ENAC/EASA considera applicabile un STS-02/PDRA-G03 alla rotta di consegna rurale* (drop-zone come "area a terra controllata")? Se sì, esiste una scorciatoia che rivaluta le classi C6 e il restare nel tetto 3 m. → **Pre-app: perimetro "area a terra controllata" per una consegna a punto fisso.**
4. **FO-4 (falsifica §5):** *ENAC penalizza effettivamente in SORA la complessità della transizione VTOL* (OSO affidabilità/containment più severi per tilt vs quadplane), o la tratta come neutra? Se neutra, il vantaggio regolatorio del quadplane svanisce. → **Pre-app: peso degli OSO tecnici sull'architettura di transizione.**
5. **FO-5 (falsifica §2/§4):** *quale dimostrazione di contenimento del carico* (`annex` §S.1.3(c)) *ENAC richiede per UN3373/UN1845, e questa dipende dalla massa/architettura*? Se il contenimento richiesto è pesante, il budget di massa esplode e conferma l'inadeguatezza del tetto 25 kg (rafforza la tesi, ma va quantificato). → **Pre-app: standard di contenimento accettato** (cfr. `13` OQ-B2).
6. **FO-6 (falsifica §1):** *la marcatura C3 richiede un Notified Body* (Modulo B/C EU-type examination — Modulo A non disponibile per C1-C3, `10` §3.4): *il costo/tempo di ottenere la marcatura C3 è tale da renderla non conveniente anche per il solo EO*? Se il C3-marking costa più del beneficio Open A3, anche S0 va ripensato (dimostratore auto-costruito ex art. 20 in Open A3 senza marcatura). → **Verificare costo/tempo Notified Body.**

---

## 9. Confidenza e domande aperte

| Elemento | Confidenza | Nota |
|---|---|---|
| C-marking (C3) ≠ categoria operativa; C3 apre solo Open A3 | **high** [FATTO] | `945` Parte 4 r.1795–1936; `947` art. 4 r.293–307 |
| Requisiti tecnici C3 (≤25 kg, <3 m, RID, geo-awareness…) | **high** [FATTO] | `945` r.1804–1895 |
| Consegna = sempre Specific (Open preclusa, art. 4 lett. f) | **high** [FATTO] | `947` r.305; `13` §1.1 |
| 25 kg = cliff netto in Open, rampa continua in Specific | **high** [FATTO] | art. 4 r.297; art. 6 r.351–367; SORA usa dim×vel non massa |
| Superare 25 kg non alza la categoria (solo assembramenti/DG-alto/GRC>7 lo fanno) | **high** [FATTO] | art. 6 r.351–367; `annex` GRC>7 |
| C3 irrilevante per consegna/relay/sorveglianza, rilevante solo per EO VLOS | **medium-high** [STIMA] | Deriva dai fatti sopra; conclusione di sintesi |
| Superare 25 kg conviene per la consegna (payload/BRS/contenimento) | **medium-high** [STIMA] | Dipende da budget di massa reale (`10` §3.2) e da FO-2/FO-5 |
| STS-01/STS-02 e classi C5/C6 (dettaglio tecnico) | **medium** [FATTO con riserva] | Non nel repo (post-emendamento); descrizione STS in `947` r.1182–1202 |
| STS/PDRA scarsa applicabilità alla consegna su borgo | **medium** [STIMA] | Vincolo "area a terra controllata"; `13` §3.4; FO-3 |
| Complessità VTOL alza costo OSO/containment, non la categoria | **medium** [STIMA] | Analisi qualitativa; da confermare FO-4 |
| Raccomandazione "C3 per EO, Specific-native per consegna" | **medium-high** [STIMA] | Robusta salvo FO-1/FO-6 (vincoli di bando/costo Notified Body) |

### Fonti (repo)
- `fonti/CELEX_32019R0945_IT_TXT.md` — Reg. (UE) 2019/945: **Parte 4 requisiti classe C3** (r.1795–1936; MTOM<25 kg e dim.<3 m r.1804; RID r.1841; geo-awareness r.1863; datalink protetto r.1881; 48 V r.1832); classi C0–C4 (r.1450–1936). **C5/C6 non presenti** (edizione pre-2020/1058).
- `fonti/CELEX_32019R0947_IT_TXT.md` — Reg. (UE) 2019/947: **art. 4 Open** (r.293–307; divieto DG/drop lett. f r.305; soglia 25 kg lett. b r.297); **art. 5 Specific** (r.310–345; dichiarazione STS §5 r.333–337; esenzione LUC §6 r.339–344); **art. 6 Certified** (r.347–367; trigger assembramenti/persone/DG-alto r.358–362; art. 6.2 autorità r.364–367); **A3** `UAS.OPEN.040` (rif. `04` r.1030–1046); **descrizione STS/dichiarazione** Allegato Parte B §1 (r.1182–1202).
- `fonti/annex_to_ed_decision_2025-018-r_1.md` — SORA 2.5: Table 1 iGRC (r.997–1028), Table 5 mitigazioni M1/M2 (r.1261–1273), Table 3 SAIL (r.1655–1666); **esclusione merci pericolose + contenimento §S.1.3(c)** (r.311–315); GRC>7→Certified.
- `fonti/Regolamento_APR_Ed_3_Emend_1.md` — ENAC APR Ed.3+Em.1: §4.5 autorizzazione merci pericolose (r.424); art. 26 BVLOS; art. 34 privacy.
- Base interna: `analisi-bottom-up/04-regolatorio.md`, `analisi-bottom-up/13-fasce-regolatorio-missione.md`, `analisi-bottom-up/10-fasce-engineering.md` §3.
- Comparabili esterni (pubblici, non nel repo — confidenza media): ABzero (IT), Matternet+Swiss Post (CH), Everdrone (SE), Wingcopter (DE).
