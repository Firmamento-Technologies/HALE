# 24 — BOXTILT (box-wing 4 tilt-rotor): verdetto integrato aero + economia

> **Cosa è.** Chiusura del filone aperto dall'utente sul concept **box-wing con 4 tilt-rotor** (2 anteriori traenti + 2 posteriori spingenti, entrambe le ali portanti). Integra la simulazione bottom-up (`sim_boxwing_tiltrotor.py`), la validazione aero-strutturale (`20`) e l'analisi economico-critica (`19`, la parte principale in ottica studio di fattibilità). Aggiorna la decisione **D3** di `17`.
> **Confidenza:** aero MEDIA (L0/L1, da riverificare con VLM/RANS), economia MEDIA sulle direzioni, BASSA sui valori assoluti (nessun dato reale di prezzo/volume). **Onestà preliminare:** il concept è preso sul serio e modellato, non liquidato.

---

## 1. Il responso in una riga

> **Aerodinamicamente il concept funziona ed è onesto** — vola, e a scala C3 è un **pareggio genuino** con un monoplano pulito pur restando VTOL (non la penalità del lift+cruise). **Ma la decisione di fattibilità è economica, e lì il concept perde:** il vantaggio non ripaga lo sviluppo bespoke, esiste un concorrente italiano già brevettato (SUPAIR) con un approccio più semplice, e per un operatore-di-servizi l'airframe non crea valore d'impresa. **Resta una linea dimostratore R&D/IP finanziata da grant, non un prodotto.**

---

## 2. Aerodinamica — cosa regge e cosa no (da `sim` + `20`)

**L'utente ha ragione su un punto sostanziale:** poiché qui **nessun rotore è morto in crociera** (i 4 tilt-rotor diventano tutti traenti/spingenti), **non** si applica il CD0 "sporco" del lift+cruise (i cui 0,040 venivano proprio dai dischi rotore fermi, `22` §1.3). Quindi il concept **non eredita la penalità del lift+cruise**: l'aerodinamica è un **pareggio (≈0%)** con un monoplano pulito — coerente col verdetto consolidato (vantaggio d'ala ≈0% a C3), **non in contraddizione**.

**Ma la sim prendeva il corner ottimistico.** Rifatto il conto con banda onesta (`20`):

| Metrica | Worst | Base | Best (sim originale) |
|---|---|---|---|
| **L/D** | 12,9 | 14,4 | 16,6 |
| **Range vs COTS lift+cruise** | −9% | +13% | +44% |
| **Range vs retrattile (SUPAIR)** | −28% | −10% | +15% |

→ Il **+44% è il corner, non l'atteso**. Contro il **retrattile** (che ottiene crociera pulita con **un** meccanismo invece di quattro) l'edge esiste **solo nel best case**. Le tre leve ottimistiche insieme (e=1,05; CD0=0,034; penalità massa 15%) sono difendibili singolarmente ma improbabili tutte assieme; la massa dei tilt è probabilmente **sottostimata** (un tilt-rotor pesa più di un lift-rotor fisso).

**Il vero collo di bottiglia NON è aerodinamico** (`20`):
1. **Controllo di transizione** — 4 tilt opposti sincronizzati, safety-critical; **jam di un singolo attuatore a metà transizione = stato non recuperabile a bassa quota** su una valle come Pentema → **rischio SORA di primo ordine**.
2. **Massa dei 4 meccanismi di tilt** — erode il range rivendicato e il payload sul tetto duro 25 kg.
3. **Whirl flutter** — modo aeroelastico nuovo (rotore su gondola cedevole) che il "box rigido C3" di `18`/`R6` **non** copre.

---

## 3. Economia — il filtro decisivo (da `19`, parte principale)

- **Il +44% (best case) vale poco in un modello-servizio:** ~€20-70k/anno lordi, **~€10-30k/anno incrementali** sulla migliore alternativa acquistabile, per una flotta SNAI di 3 piattaforme. Il grosso del vantaggio **non viene dall'ala chiusa** ma dall'eliminazione dei rotori morti — che il **retrattile SUPAIR cattura con un meccanismo, ed è già brevettato**.
- **Sensitivity spietata:** il "valore del +44%" muove l'NPV di ±€0,2M; il **costo di sviluppo di ±€3M (15×)**. *L'aerodinamica dell'idea è rumore; il suo sviluppo è il segnale.*
- **Tre strade (TCO 5y, flotta 3, NPV@12%):**

| Strada | TCO 5y | NPV | Payback | TRL/tempi |
|---|---|---|---|---|
| **(A) BUY COTS lift+cruise** | ~€6,4M | ~−€1,9M | — | 9 / subito ← default |
| **(B) BUILD BOXTILT** | ~€9-12M | **−€4,5/−€8M** | **mai** | 3-4 / 24-48 mesi |
| **(C) PARTNER/LICENSE SUPAIR** | ~€6,3M | dipende | — | pre-prodotto altrui, brevettato |

- **Nessun moat IP:** box-wing e tilt-rotor sono arte nota (Prandtl 1924); per un operatore-di-servizi l'airframe non aggiunge valore d'impresa, e aggirare il brevetto SUPAIR col 4-tilt porta alla variante **più costosa e meno difendibile**.

---

## 4. Verdetto di fattibilità e aggiornamento della decisione D3

**Condizione UNICA sotto cui costruire BOXTILT ha senso:** come **linea R&D/IP finanziata ≥70% da grant a fondo perduto** (Coopfond/FESR Poli/PNRR-Aero, con cumulazione de minimis/GBER verificata), con valore di **vetrina-sovranità e trasferimento tecnologico verso l'HALE** — **mai come prodotto o asset di servizio autofinanziato**, perché il servizio si eroga meglio, prima e a minor rischio comprando COTS.

Questo **conferma e ora quantifica** l'opzione **(A)** di **D3** (`17`): il box-wing — anche nella variante 4-tilt più sofisticata dell'utente — è un **dimostratore R&D**, non il prodotto. La novità rispetto a `18`: ora è **caratterizzato con numeri** (aero = pareggio non penalità; +44% solo nel best case; NPV negativo come prodotto; collo di bottiglia = controllo/massa/flutter, non aero) e con il **contesto competitivo** (SUPAIR brevettato).

> **D3 aggiornata.** *Confermo BOXTILT (box-wing 4-tilt) come **dimostratore R&D/IP finanziato da grant**, scorporato dal P&L del prodotto (opzione A) — con il valore reale di vetrina-sovranità verso l'HALE. L'opzione (B) "BOXTILT come prodotto" è **economicamente esclusa** salvo copertura grant ≥70%. Il prodotto di servizio resta il COTS lift+cruise (D2, `17`).*

---

## 5. Se si vuole comunque de-riscare il concept: le 2 simulazioni

Costo ~nullo, in-house (`20` §piano L2):
1. **Sim 1 — polare VLM→RANS** del box-wing 4-tilt a C3: falsifica/conferma la banda L/D 12,9–16,6 e il CD0 reale delle 4 nacelle di tilt.
2. **Sim 2 — transizione + jam (la più importante):** dinamica dei 4 tilt opposti e **scenario di attuatore inceppato a metà** → dice se il modo di guasto è mitigabile (BRS/logica) o showstopper SORA. **Pesa più della polare.**

Se anche solo la Sim 2 mostra il jam non mitigabile a bassa quota, il concept resta vetrina, non prodotto, **indipendentemente** dall'aerodinamica.

---

## 6. Falsifying observations (integrate da `19` e `20`)

1. Una **VLM/RANS** che dia L/D reale >16 **e** CD0 nacelle <0,006 → riaprirebbe (parzialmente) l'edge aero vs retrattile.
2. Una **logica di mitigazione del jam** (ridondanza attuatori, BRS dedicato) dimostrata sicura a bassa quota → toglierebbe il collo di bottiglia n.1.
3. Un **grant a fondo perduto ≥70%** su €3-5M R&D aerospazio (PNRR/FESR/EDF) effettivamente ottenibile → renderebbe (B) sostenibile **come R&D**, non come prodotto.
4. Una **FTO professionale** che mostri il 4-tilt libero dal brevetto SUPAIR **e** difendibile → darebbe un (piccolo) valore IP.
5. Un **prezzo/volume reale** (LoI operatori) che ripaghi un airframe proprietario > COTS → oggi assente; se emergesse, cambierebbe l'NPV.
6. Un **fallimento/ritardo di SUPAIR** che liberi la nicchia italiana → cambierebbe il contesto competitivo (ma non l'economia bespoke).
7. Una **massa reale dei 4 tilt** ≤12% MTOM (non 15-20%) → recupererebbe range e payload.

---

### Riga di fondo

> Il concept dell'utente **non era campato in aria**: a scala C3, non avendo rotori morti in crociera, è aerodinamicamente un **pareggio onesto** con un monoplano pulito pur restando VTOL — meglio del lift+cruise COTS, alla pari (o poco sopra, solo nel best case) del retrattile. **Ma lo studio di fattibilità decide sull'economia, ed è lì che si ferma:** il vantaggio vale €10-30k/anno, lo sviluppo costa €3-10M, l'NPV da prodotto è −€4,5/−€8M con payback mai, non c'è moat IP e c'è già un concorrente italiano brevettato (SUPAIR). Il vero rischio non è l'aria, è il **controllo di transizione** (jam = rischio SORA) e la **massa**. Conclusione, coerente e ora quantificata: **BOXTILT è un dimostratore R&D/IP da finanziare con grant e da usare come vetrina-sovranità verso l'HALE — non il prodotto.** Il prodotto di servizio resta il lift+cruise COTS. Le 2 simulazioni (soprattutto quella di transizione+jam) sono la prossima prova a costo quasi nullo, se si vuole portare avanti il dimostratore.
