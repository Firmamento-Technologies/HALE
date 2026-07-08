# Limite di accesso: TED (Tenders Electronic Daily) e comunicati ufficiali EMSA/Tekever non fetchabili in questa sessione

**URL:** https://ted.europa.eu (dominio generale) ; https://www.emsa.europa.eu (dominio generale) ; https://www.tekever.com (dominio generale)
**Data accesso:** luglio 2026 — TENTATIVO FALLITO
**Cosa supporta:** dichiarazione di trasparenza sui limiti di questa ricerca, come richiesto dal mandato di rigore avversariale.

## Nota metodologica

In questa sessione di ricerca, il proxy di rete configurato per l'ambiente ha **rifiutato sistematicamente (HTTP 403, "policy denial")** ogni tentativo di connessione diretta (sia via strumento WebFetch sia via `curl`) ai domini:
- `ted.europa.eu` (portale ufficiale UE degli appalti pubblici)
- `www.emsa.europa.eu` (sito ufficiale EMSA)
- `www.tekever.com` (sito ufficiale Tekever)
- `www.unmannedsystemstechnology.com`, `defence-industry.eu`, `skybrary.aero`, `en.wikipedia.org`, e numerosi altri domini esterni

Il blocco è stato confermato a livello di infrastruttura (endpoint diagnostico del proxy, `recentRelayFailures`), non un errore transitorio: **"gateway answered 403 to CONNECT (policy denial or upstream failure)"** per ciascuno di questi host. Le istruzioni operative dell'ambiente indicano esplicitamente di **non ritentare** un blocco di policy 403/407 e di segnalarlo come limite, non di aggirarlo.

**Conseguenza:** tutti i dati di questo pacchetto di ricerca provengono da **sintesi del motore di ricerca (WebSearch)**, che evidentemente opera attraverso un canale infrastrutturale diverso (server-side, non instradato sul proxy locale bloccato) e ha potuto restituire estratti/riassunti di pagine — inclusi TED, EMSA e Tekever — ma **senza la possibilità di verificare il testo integrale e originale della pagina sorgente con un fetch diretto**. Questo introduce un rischio residuo non eliminabile in questa sessione: le sintesi del motore di ricerca potrebbero, in rari casi, mescolare dettagli di articoli diversi restituiti nella stessa query (osservato empiricamente: una sintesi ha inizialmente attribuito erroneamente la piattaforma "AR5" invece di "AR3" al contratto 2021, poi corretto da un incrocio con altre query).

**Raccomandazione per Firmamento:** prima di usare la cifra "€30M/4 anni" in un documento investment-grade (Studio di Fattibilità capitoli 6-8), un membro del team dovrebbe accedere manualmente a `https://ted.europa.eu` con ricerca avanzata (Contracting authority: EMSA; Contractor: Tekever/CLS/REACT; anno 2025) per estrarre il numero di notifica TED e il valore esatto in EUR, che è il dato legalmente vincolante e più preciso disponibile pubblicamente per un appalto UE. Questa verifica NON è stata possibile in questa sessione per limite di rete, non per assenza della fonte (TED è notoriamente il registro pubblico più affidabile per questo tipo di dato).
