# WingtraOne GEN II — appalto pubblico reale UK (Find a Tender, equivalente UK di TED), aggiudicato a Korec, settembre 2025

**URL:** https://www.find-tender.service.gov.uk/Notice/060190-2025/PDF (notice UKRI-5251, "Wingtra One UAV", 2025/S 000-060190)
**Data accesso:** luglio 2026 (recuperato via sintesi WebSearch — vedi nota metodologica sotto; fetch diretto del PDF non riuscito, WebFetch bloccato 403 a livello di ambiente per l'intera sessione, confermato anche su `ted-emsa-access-limitation.md` di sessioni precedenti)
**Cosa supporta:** aggiorna/conferma con un dato di appalto pubblico REALE il claim "WingtraOne GEN II — kit base $29.000 (~€27k), fonte: Robotomated (blog terzo)" in `05-piattaforme-costi.md` §2 e `10-fasce-engineering.md` §1.

## Estratto rilevante

Da sintesi WebSearch del notice UK (portale ufficiale "Find a Tender", il sistema britannico post-Brexit strutturalmente equivalente a TED per soglie sopra £139.688 — non è TED/EU in senso stretto, ma stessa categoria di fonte: notifica di aggiudicazione di appalto pubblico governativo, legalmente vincolante):

> "The contract is for the purchase of a fixed-wing UAV with VTOL capability for survey and mapping of ice fronts in hazardous areas, with reference UKRI-5251. **Supplier: Korec. Contract value: £30,947.64 excluding VAT / £37,137.17 including VAT. Date signed: 24 September 2025.** Contract dates: 25 September 2025 to 1 November 2025. Notice identifier: 2025/S 000-060190. This is a below-threshold contract for goods procurement under the Procurement Act 2023."

Contraente: UKRI (UK Research and Innovation) — verosimilmente per un ente di ricerca polare (survey di fronti glaciali, "ice fronts in hazardous areas" — compatibile con British Antarctic Survey o simile).

Conversione indicativa (non verificata in tempo reale): £30.947,64 ≈ **€35.500-36.200** (IVA esclusa) al cambio GBP/EUR ~1,15-1,17 di luglio 2026.

**Secondo riscontro indipendente trovato nella stessa ricerca:** tender separato, Ulster Wildlife Trust, "Wingtra One Gen II UAV and Associated Equipment", valore stimato **£35.000 GBP** (fonte: bidstats.uk / D3 Tenders / The Construction Index — notice pubblicato 2025, settimana W03). Questo è un valore di **stima di gara**, non necessariamente l'importo finale aggiudicato, ma converge nello stesso ordine di grandezza del contratto Korec/UKRI.

## Lettura

Il claim originale ($29.000 / ~€27k, fonte unica "Robotomated", un blog ROI-calculator di terze parti, dichiarato "medium confidence" nel report interno) è ora **confermato in ordine di grandezza da due notizie di appalto pubblico indipendenti**, entrambe più alte di circa il 20-30% (€35-37k IVA esclusa vs €27k stimato) — plausibile per via di configurazione/accessori inclusi nel bundle "Associated Equipment" o differenza di cambio. **Non è un dato TED/UE**, ma un dato di appalto pubblico britannico della stessa categoria evidenziale (notifica ufficiale di aggiudicazione, importo legalmente vincolante).

**Nota rilevante sul ciclo di vita prodotto:** dalla stessa ricerca risulta che WingtraOne GEN II è stato il prodotto di punta Wingtra dal 2017 al 2025; dal 2025 il nuovo modello di punta è **WingtraRAY**, che lo sostituisce (supporto/ricambi per GEN II garantiti ≥24 mesi, payload/accessori ancora in vendita ≥12 mesi dal lancio di RAY). Il contratto Korec di settembre 2025 dimostra che GEN II era ancora acquistabile e attivamente fornito a quella data, ma il prodotto è in fase di uscita di listino — va verificato prima di ogni RFQ Firmamento se GEN II è ancora ordinabile nel 2026 o se il fornitore indirizzerà automaticamente verso WingtraRAY (prezzo non pubblico, "request a quote" su tutti i rivenditori controllati).

## Nota metodologica (limite di sessione)

Come già documentato in `ted-emsa-access-limitation.md`, il proxy di rete di questo ambiente blocca sistematicamente (403 "policy denial") ogni fetch diretto (WebFetch e curl) verso domini esterni, inclusi ted.europa.eu, find-tender.service.gov.uk, wikipedia, ecc. — confermato anche in questa sessione con test su https://example.com (403). Tutti i dati qui riportati provengono da **sintesi del motore WebSearch**, che evidentemente opera su un canale diverso e riesce a restituire estratti di pagina, ma senza possibilità di verifica diretta del testo integrale/originale del PDF del notice. Confidence upgrade a "medium-alta" e non "alta piena" per questo motivo.
