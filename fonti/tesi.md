      POLITECNICO DI TORINO
                         Corso di Laurea Magistrale

                          in Ingegneria Gestionale




                     Tesi di Laurea Magistrale
           Sviluppo metodologie Advanced Product Quality
          Planning (APQP) e Product Part Approval Process
          (PPAP) in UmbraGroup S.p.A. operante nel settore
                            aeronautico.




Relatore:                                                      Candidato:
prof. Maurizio Galetto                                Daniele Giammarrusti




                         Anno Accademico 2019/2020
                                                       Indice
INTRODUZIONE .......................................................................................................... 1

CAPITOLO 1: IL CONTESTO AZIENDALE ........................................................... 4

   1.1. L’AZIENDA .......................................................................................................... 4

      1.1.1. LA STORIA .................................................................................................... 5

      1.1.2. STRUTTURA AZIENDALE .......................................................................... 8

      1.1.3. MISSION ........................................................................................................ 9

      1.1.4. VALORI ........................................................................................................ 10

   1.2. I PRODOTTI UMBRAGROUP .......................................................................... 11

      1.2.1. SEGMENTO INDUSTRIALE ...................................................................... 11

      1.2.2. SEGMENTO ENERGIA............................................................................... 14

      1.2.3. SEGMENTO AERONAUTICO ................................................................... 15

   1.3. SERVIZI E PROCESSI ....................................................................................... 19

   1.4. FILOSOFIA LEAN SIX SIGMA ........................................................................ 20

CAPITOLO 2: NORMATIVE .................................................................................... 21

   2.1. IL SISTEMA DI GESTIONE DELLA QUALITA’ ............................................ 21

   2.2. IAQG ................................................................................................................... 23

      2.2.1. AS/EN 9100 .................................................................................................. 24

      2.2.2. AS/EN 9102 .................................................................................................. 25

CAPITOLO 3: MERCATO AERONAUTICO ......................................................... 26

   3.1. PREVISIONI CRESCITA SETTORE AERONAUTICO .................................. 26

   3.2. EFFETTO COVID-19 SULL’ANALISI ............................................................. 29

   3.3. DALLA AS/EN 9102 ALLA AS/EN 9145 ......................................................... 32

CAPITOLO 4: AS/EN 9145 ......................................................................................... 34

   4.1. INTRODUZIONE ALL’APQP ........................................................................... 34

      4.1.1. OBIETTIVI ................................................................................................... 35

      4.1.2. VANTAGGI .................................................................................................. 36

                                                                                                                                  I
  4.2. PRODUCT PART APPROVAL PROCESS (PPAP) .......................................... 37

     4.2.1. DOCUMENTI DI PROGETTAZIONE ........................................................ 38

     4.2.2 ANALISI DEI RISCHI DI PROGETTAZIONE (DRA) ............................... 38

     4.2.3. DESIGN FAILURE MODE & EFFECT ANALYSIS (DFMEA) ............... 39

     4.2.4. DIAGRAMMA DI FLUSSO DEL PROCESSO .......................................... 39

     4.2.5. PROCESS FAILURE MODE & EFFECT ANALYSIS (PFMEA) ............. 40

     4.2.6. PIANO DI CONTROLLO ............................................................................ 41

     4.2.7. MEASURAMENT SYSTEM ANALYSIS (MSA) ...................................... 41

     4.2.8. STUDIO INIZIALE DELLA CAPACITÀ DEL PROCESSO ..................... 42

     4.2.9. APPROVAZIONE IMBALLAGGIO, CONSERVAZIONE ED
     IDENTIFICAZIONE .............................................................................................. 43

     4.2.10. FIRST ARTICLE INSPECTION REPORT (FAIR) ................................... 43

     4.2.11. REQUISITI SPECIFICI DEL CLIENTE ................................................... 44

     4.2.12. PPAP APPROVAL FORM ......................................................................... 44

  4.3. ADVANCED PRODUCT QUALITY PLANNING (APQP) ............................. 46

     4.3.1. I PILASTRI DELL’APQP ............................................................................ 46

     4.3.2. LE FASI DELL’ APQP ................................................................................ 48

     4.3.3. ASPETTI SALIENTI E RIFLESSIONI SU APQP-PPAP ........................... 55

CAPITOLO 5: L’APQP IN UMBRAGROUP ........................................................... 57

  5.1. CASO UMBRAGROUP S.p.A. “AS IS” ............................................................ 57

     5.1.1. MODALITÀ DI SVOLGIMENTO .............................................................. 58

     5.1.2. INCONVENIENTI CORONAVIRUS .......................................................... 59

  5.2. CHECKLIST DELLE 5 FASI APQP .................................................................. 60

  5.3. ASSESSMENT MATRIX ................................................................................... 62

  5.4. RISULTATI ......................................................................................................... 63

CAPITOLO 6: ANALISI DEL SISTEMA DI MISURA (MSA) ............................. 64

  6.1. INTRODUZIONE MSA ...................................................................................... 64


                                                                                                                           II
      6.1.1. TERMINOLOGIA UTILIZZATA NELL’ANALISI DEL SISTEMA DI
      MISURA ................................................................................................................. 66

   6.2. SCOMPOSIZIONE DELLA VARIANZA ......................................................... 68

   6.3. STUDIO GAGE R&R ........................................................................................ 69

      6.3.1. PROGRAMMAZIONE DELL’ESPERIMENTO ........................................ 70

      6.3.2. MODELLO ANOVA (Analysis Of Variance).............................................. 72

   6.4. CASO STUDIO MSA IN UMBRAGROUP S.p.A ............................................. 81

      6.4.1. PROGRAMMAZIONE DEGLI ESPERIMENTI ......................................... 81

      6.4.2. ESECUZIONE DELL’ESPERIMENTO ...................................................... 84

   6.5. RISULTATI ......................................................................................................... 86

      6.5.1. PIN TO PIN – RETRATTO .......................................................................... 90

      6.5.2. PIN TO PIN – ESTESO ................................................................................ 94

      6.5.3. GIOCO ANTIROTAZIONE ......................................................................... 99

      6.5.4. GIOCO RADIALE ...................................................................................... 104

CONCLUSIONI & SVILUPPI FUTURI ................................................................. 108

Bibliografia .................................................................................................................. 111

Sitografia ..................................................................................................................... 111




                                                                                                                                 III
IV
INTRODUZIONE

Il concetto della qualità non è assoluto ed eterno. Nel corso degli anni ha infatti subìto
numerose modifiche dovute all’evoluzione del contesto sociale e legislativo, ma
soprattutto al mutamento delle esigenze dei clienti, i quali rappresentano i destinatari dei
prodotti o servizi forniti e, di conseguenza, i valutatori della qualità in base a come essi
la percepiscono.

Una prima definizione concreta, seppur generale, fu emanata nel 1995 con la
pubblicazione della norma ISO 8402 che recita: “La qualità è l’insieme delle
caratteristiche di un’entità che ne determinano la capacità di soddisfare esigenze
espresse ed implicite”1. La seguente definizione, per quanto possa sembrare esaustiva,
non considera la qualità come una grandezza oggettivamente misurabile. Essa fa
riferimento a come la qualità viene percepita da tutti gli stakeholder, i cui benefici
possono essere differenti e molto spesso contrapposti (si pensi agli enti per il rispetto
dell’ambiente e agli azionisti), per cui assume un significato prettamente soggettivo.

Questo limite venne superato con l’emanazione della norma ISO 9000 del 2000, in cui
la qualità viene definita come “il GRADO in cui un insieme di caratteristiche
intrinseche soddisfa i requisiti”2. Il termine “grado” sottolinea la necessità di
quantificare la qualità attraverso una misurazione della stessa. Alle caratteristiche
qualitative è dunque fondamentale attribuire dei pesi per poter esprimere una
valutazione oggettiva del prodotto/servizio.

Da questa considerazione, l’International Organization for Standardization (ISO) ha
sviluppato una serie di normative volte a guidare le organizzazioni nella mappatura dei
vari processi aziendali al fine di raggiungere livelli qualitativi elevati.

Un’azienda che fornisce un prodotto o servizio di qualità certificata, si distingue dalla
concorrenza. La differenziazione che ne scaturisce incide ed influenza la natura degli
scambi, i quali saranno molto più concentrati per le aziende in possesso di certificazioni
che attestano l’elevata qualità dei propri prodotti.


1
  UNI EN ISO 8402:1995, Quality management and quality assurance – Vocabulary, p. 5. Definizione
revisionata della versione UNI EN ISO 8402:1988 in cui la parola “prodotto” è stata sostituita con
“entità” per poter estendere il campo applicativo del termine.
2
  UNI EN ISO 9000:2000, Quality management systems – Fundamentals and vocabulary, p. 7.
Definizione riproposta anche nella revisione aggiornata UNI EN ISO 9000:2005.
                                                                                                     1
Partendo dalla normativa generale relativa al sistema di gestione della qualità (ISO
9001)3, gli attori operanti nei diversi settori hanno modellato requisiti e procedure in
base alle loro esigenze.

Nel campo aeronautico, l’International Aerospace Quality Group (IAQG)4 ha elaborato
uno standard in grado di guidare le organizzazioni che operano in questo settore nel
processo di sviluppo di un nuovo prodotto/processo, permettendo alle stesse il
raggiungimento di elevati standard qualitativi. La normativa di riferimento è la AS/EN
9145 la quale riprende la metodologia Advanced Product Quality Planning (APQP)5,
ampiamente utilizzata e diffusa nel settore automotive, riadattandola al contesto
aeronautico.

L’APQP è un insieme di procedure e strumenti che hanno lo scopo di supportare
l’organizzazione nella gestione e monitoraggio delle attività da implementare durante le
varie fasi che concorrono al processo di sviluppo di un nuovo prodotto/processo.

L’obiettivo del presente lavoro di tesi è quello di esporre ed analizzare la normativa
AS/EN 9145 adottata nel settore aeronautico e riferita al processo APQP. Inoltre, si è
valutato il grado di implementazione del processo nel sistema di gestione della qualità
dell’organizzazione e, con il coinvolgimento dei responsabili delle varie funzioni
aziendali, sono stati individuati gli aspetti carenti che necessitano di ulteriori
approfondimenti. L’attività di assessment ha evidenziato una lacuna relativa ad uno dei
deliverables dell’APQP ovvero l’analisi del sistema di misura, per cui si è provveduto
ad eseguire uno studio sperimentale sui banchi prova utilizzati per effettuare le misure
delle caratteristiche degli attuatori. Lo studio è stato condotto con l’ausilio di
MINITAB6, un potente software di analisi statistica, coinvolgendo gli addetti della sala
prove, il reparto qualità e il responsabile del collaudo e montaggio degli attuatori.
Questa ultima parte dell’elaborato si pone l’obiettivo di validare il sistema di misura e
rendere ancora più robusto il processo APQP.




3
  UNI EN ISO 9001:2015, Quality management systems requirements.
4
  Link: https://iaqg.org/
5
  AS/EN 9145:2016/2018 Aerospace Standard, Requirements for Advanced Product Quality Planning
and Production Part Approval Process.
6
  Link: https://www.minitab.com/en-us/
                                                                                                2
Il lavoro è stato svolto presso l’azienda UmbraGroup S.p.A.7 con sede a Foligno (PG)
contestualmente ad un periodo di tirocinio della durata di 7 mesi, di cui gli ultimi 3 in
smart-working a causa dell’emergenza Covid-19.

Nel primo capitolo viene presentata l’azienda UmbraGroup S.p.A. facendo riferimento
alla sua storia, all’estensione del gruppo a livello mondiale, alla mission e ai valori
condivisi da tutto il gruppo, nonché al parco prodotti fornito dall’organizzazione ai
clienti operanti nei vari settori di competenza: industriale, aeronautico, energia.

Successivamente, nel secondo capitolo, viene accennato il sistema di gestione della
qualità normato dalla ISO 9001 e vengono trattate le principali normative che l’IAQG
ha sviluppato sulla base di questo standard.

Il terzo capitolo contiene l’analisi della previsione della domanda di velivoli per i
prossimi 20 anni e come essa abbia influenzato l’intera filiera produttiva aeronautica.

La normativa AS/EN 9145 e dunque la metodologia APQP, viene spiegata nel dettaglio
nel capitolo quattro. Oltre alle fasi in cui è scomposto l’intero processo APQP, vengono
anche analizzati i singoli deliverable del processo. Molti di questi deliverables
costituiscono il pacchetto Product Part Approval Process (PPAP)8 che rappresenta
l’output del processo APQP tramite cui il cliente è in grado di effettuare le proprie
considerazioni sul raggiungimento o meno degli obiettivi prefissati.

Nel quinto capitolo viene effettuata una valutazione sul grado di implementazione del
processo APQP in azienda, relativo alla realizzazione di un tipo di attuatore
elettromeccanico. Tale analisi è stata condotta coinvolgendo i responsabili dei vari
reparti aziendali tra cui: Design, Manufacturing, Quality, Procurement, Operations.
Durante i colloqui si è fatto riferimento ad una checklist appositamente studiata
dall’IAQG, in modo tale da non trascurare alcun aspetto nell’analisi.

I risultati dei colloqui hanno evidenziato una particolare carenza del Measurement
System Analysis (MSA)9 e dunque, nel sesto capitolo, viene affrontato lo studio MSA
sui banchi di collaudo degli attuatori.



7
  Link: https://www.umbragroup.com/
8
  Per una panoramica degli elementi del PPAP si rimanda al seguente link:
https://www.sae.org/iaqg/projects/9145_guidance.pdf
9
  Analisi del sistema di misura utilizzato per rilevare le misure delle caratteristiche. Il risultato dell’analisi
permette di quantificare l’incidenza della variabilità imputabile al sistema di misura, rispetto a quella
scaturita dalle effettive differenze tra i componenti misurati.
                                                                                                                 3
CAPITOLO 1: IL CONTESTO AZIENDALE

1.1. L’AZIENDA

L’azienda UmbraGroup S.p.A., capofila del gruppo Umbra, è leader mondiale nella
realizzazione di viti a ricircolo di sfere ed altre tecnologie per applicazioni
aereonautiche ed industriali. Nel business aziendale rientra un sostanziale interesse sia
al settore energetico, attraverso la fornitura di prodotti al mercato dell’energia, sia
all’eco-sostenibilità, con l’impegno nel corso degli anni a dare il proprio contributo
volto a ridurre l’impatto ambientale. Il gruppo è composto da 7 aziende situate in
diverse parti del mondo, condizione strategica che gli ha permesso di interfacciarsi con
un mercato globale. Durante la sua storia, non ha solo migliorato la propria catena di
produzione, ma ha anche curato la formazione del personale e, attraverso investimenti
sostanziali in Ricerca & Sviluppo, è riuscita negli anni ad accrescere la gamma di
prodotti realizzati.

Fondata a Foligno (PG) nel 1972 per la produzione di cuscinetti ad alta precisione, nel
1978 l’azienda inizia la produzione di viti a ricircolo di sfere per applicazioni
aereonautiche, che ben presto divennero il prodotto di punta su cui iniziò a ricadere la
scelta del cliente.

Spinta da un forte desiderio di innovazione e dalla cultura aziendale orientata al
continuous improvement, il gruppo è ad oggi leader mondiale nella realizzazione di viti
a ricircolo di sfere ed è considerato molto all’avanguardia nel settore aeronautico.




                                                                                            4
1.1.1. LA STORIA


La storia di UmbraGroup S.p.A. ha radici molto lontane. Il tutto ebbe inizio con la
nascita nel 1935 dell’Aeronautica Umbra S.A. di proprietà della Macchi. La Macchi
aveva già acquisito esperienza nel settore aeronautico grazie alla Società Anonima
Nieuport-Macchi la quale nel 1913 vinse un concorso per la fornitura di aerei militari
indetto dal ministero della difesa. Durante il periodo della Seconda guerra mondiale
furono costruiti su licenza numerosi aerei Trimotori tra cui molti dei quali presso lo
stabilimento “Aeronautica Umbra S.A.” di Foligno. Lo stabilimento di Foligno produsse
i Savoia-Marchetti S.M.79, S.M.81, S.M.84 e sviluppò il primo caccia monomotore ad
ala bassa (AUSA AUT 18) rimasto, però, allo stadio di prototipo.

L’Aeronautica Umbra S.A. crebbe molto fin dai primi anni della sua nascita, fino ad
impiegare ben 2400 dipendenti allo scoppio della Seconda guerra mondiale.
Rappresentando un fattore strategico, l’azienda venne presa di mira e nel corso della
guerra fu bombardata più volte. Cessato il conflitto fallirono i vari tentativi di rilanciare
l’attività a causa degli ingenti danni riportati per i bombardamenti e la compagnia decise
di interrompere definitivamente la produzione.

Molti dei macchinari, ex dipendenti e dirigenti dell’Aeronautica umbra, azienda ormai
in liquidazione, furono rispettivamente acquistati e assunti dall’ Officina Meccanica
Aeronautica (O.M.A.) nel 1947 e, nel corso degli anni cinquanta, produsse alcuni aerei
leggeri monoposto.

Il punto di svolta per l’attuale UmbraGroup S.p.A. si ha quando negli anni sessanta
Muzio Macchi fallì nel tentativo di riaprire gli stabilimenti di Foligno e nel 1972 la
GEPI (società italiana) e la FAG Kugelfisher Georg Schaffler GmbH (multinazionale
tedesca) acquisirono la proprietà e ciò che restava dell’Aeronautica Umbra, fondando
una nuova società chiamata Umbra Cuscinetti S.p.A., che inizialmente produceva solo
cuscinetti speciali di dimensione medio-grandi per il gruppo FAG.

Nel 1978 la Umbra Cuscinetti, spinta dal desiderio di innovazione e crescita, grazie
anche al ‘Progetto Tornado’, avvia un processo di diversificazione mediante la
produzione di viti a ricircolo di sfere per applicazioni aeronautiche e nel 1982 iniziarono
le attività di progettazione delle viti destinate sia al mercato aeronautico che a quello
industriale.


                                                                                            5
Nel 1983 la FAG Kugelfisher Georg Schaffler GmbH acquisì il totale controllo della
Umbra Cuscinetti, la quale si impegnò nello sviluppo del know how per svolgere
autonomamente la progettazione delle viti ed incrementò sensibilmente il volume
dell’attività legata direttamente al settore aereonautico, ricevendo fiducia e
approvazione da parte dei principali attori del settore.

La FAG detenne il controllo della Umbra Cuscinetti fino al 1993 quando, tramite
un’operazione di management buyout, venne acquisita da managers dell’azienda stessa,
ovvero dall’ Ing. Valter Baldaccini, padre fondatore di UmbraGroup, insieme all’ Ing.
Reno Ortolani, oggi Direttore di Stabilimento, supportati da un gruppo di imprenditori
locali.

Da questo momento sono state effettuate una serie di acquisizioni per garantire
innovazione, miglioramento, crescita ed ampliamento del portafoglio dei prodotti. Di
seguito vengono elencati gli eventi incisivi:

    •     Nel 1996 Umbra Cuscinetti acquisisce l’azienda tedesca Kuhn GmbH,
          specializzata nella progettazione e produzione di viti a ricircolo di sfere per
          applicazioni industriali;
    •     Nel 1998 acquisisce il controllo di FM Elettromeccanica, originariamente con
          sede in provincia di Milano e successivamente trasferita nel nuovo sito di Umbra
          Cuscinetti a Foligno, specializzata nella progettazione e produzione di
          elettromandrini per applicazioni industriali;
    •     Nel 1999 acquisisce l’americana Northwest Gears Inc. di Seattle, operazione
          strategicamente importante data la prossimità dello stabilimento a quello della
          BOEING la quale rappresenta il principale cliente per la fornitura di scatole ad
          ingranaggi, settori e pignoni. Due anni dopo, nel 2001, cambia nome e diventa
          Umbra Cuscinetti Inc.;
    •     Nel 2003 per far fronte ad un significativo incremento della domanda di mercato
          e della propria quota, viene inaugurato il nuovo stabilimento produttivo situato
          nella zona industriale La Paciana di Foligno, consentendole di espandere la
          capacità produttiva;
    •     Avendo da sempre riposto una particolare attenzione anche allo sviluppo sociale,
          nel 2008 Valter Baldaccini realizza l’azionariato diffuso. Questa operazione ha
          permesso ai dipendenti con senso di attaccamento alla società e che negli anni


                                                                                             6
    hanno dimostrato competenze tecniche e umane, di acquistare parte del capitale
    sociale condividendo il rischio di impresa;
•   Nel 2009 Umbra Cuscinetti S.p.A. incorpora per fusione FM Elettromeccanica
    S.r.l.;
•   Nel 2012 viene inaugurato il Centro di Ricerca di Albanella in provincia di
    Salerno per far fronte all’esigenza aziendale di supportare la linea degli attuatori
    elettromeccanici grazie ad un centro completamente funzionale;
•   Nel 2013 venne inaugurato il nuovo stabilimento Umbra Cuscinetti Inc. ad
    Everett, Washington – USA;
•   Nel 2014, a seguito della scomparsa del fondatore Valter Baldaccini, subentrò
    alla guida dell’azienda la seconda generazione con la nomina ad Amministratore
    Delegato del figlio Antonio Baldaccini;
•   Nel 2015 ha inaugurato il nuovo stabilimento produttivo a Foligno interamente
    dedicato alla linea degli attuatori elettromeccanici;
•   Nel 2017 è stata acquisita la società SERMS S.r.l., spin-off dell’Università degli
    Studi di Perugia consentendo lo scambio culturale tra il mondo accademico e
    quello industriale;
•   A gennaio del 2018 Umbra Cuscinetti S.p.A. diventa UmbraGroup S.p.A e,
    nello stesso anno, viene acquisita la Thomson Aerospace & Defense
    appartenente a Linear Motion LLC (Saginaw, Michigan – USA).




                                                                                       7
1.1.2. STRUTTURA AZIENDALE


Come accennato nel precedente paragrafo, UmbraGroup S.p.A., capofila del gruppo, è
composta da 7 aziende che operano a livello mondiale con sedi dislocate tra Italia,
Germania e USA:

• UmbraGroup S.p.A, Foligno, Italia

• UmbraGroup S.p.A, Albanella, Italia

• Serms, Terni, Italia

• Kuhn Gmbh, Freiberg, Germania

• PKE Gmbh, Eltmann, Germania

• Umbra Cuscinetti Inc., Everett, USA

• Thomson Aerospace and Defence, Saginaw, USA




                    Figura 1.1. Struttura aziendale UmbraGroup (fonte: sito aziendale)




                                                                                         8
1.1.3. MISSION


La “mission” di UmbraGroup consiste nel perseguire l’innovazione tecnologica e la
qualità supportando il miglioramento delle performace dei clienti ed offrendo agli stessi
un servizio superiore.



“Affondando le sue radici nella continua tensione che ci contraddistingue verso l’eccellenza,
l’obiettivo è quello di costruire la nostra offerta intorno alle reali esigenze dei nostri clienti ed
essere realmente partner di un progetto comune.”10




"Essere per il Cliente IL fornitore di viti a sfere, cuscinetti, attuatori e componenti
destinati a mercati ad alta tecnologia. Un servizio eccellente sarà alla base di ogni
attività."11




10
     Cit. Valter Baldaccini, Padre Fondatore di UmbraGroup S.p.A.
11
     Mission UmbraGroup S.p.A. , fonte: https://www.umbragroup.com/azienda/881/mission
                                                                                                        9
1.1.4. VALORI


L’azienda si propone di creare un profitto sostenibile nel rispetto e nella valorizzazione
delle persone. L’acronimo FIRST12 racchiude i valori portanti dell’azienda:



• FOCUS SUL CLIENTE: Costruire con il cliente un rapporto di partnership, stima e
serietà. Accompagnare il cliente nello scegliere la soluzione migliore ed
economicamente sostenibile. Valorizzare ciascun cliente e lavorare per soddisfare le sue
esigenze.



• INNOVAZIONE: Creare un ambiente favorevole all’innovazione. Considerare il
cambiamento una forma di ricchezza e opportunità di crescita, accogliendo nuove idee e
mettendole in atto con la massima flessibilità e rapidità.



• RISPETTO: Impegnarsi ad ascoltare e comprendere il cliente e tutti gli stakeholder.
Essere coerenti con gli obiettivi concordati e rispettare le norme e le leggi vigenti



• SVILUPPO SOCIALE: Impegnarsi a realizzare attivamente il bene comune. Sostenere
il benessere e lo sviluppo dei collaboratori dentro e fuori il contesto lavorativo.
Garantire equità avendo a cuore le esigenze di tutti gli stakeholder.



• TUTTI PER UN OBIETTIVO: Operando come una squadra si possono ottenere
risultati che da soli non si riuscirebbero a raggiungere.




12
     Valori condivisi dal gruppo Umbra, fonte: https://www.umbragroup.com/azienda/877/i-valori
                                                                                                 10
1.2. I PRODOTTI UMBRAGROUP

Di seguito vengono elencati i prodotti offerti dall’azienda per il mercato industriale,
quello dell’energia e con maggior focus al mercato aeronautico.

Il parco prodotti Umbra può essere suddiviso in tre macroaree in base al loro campo di
applicazione:

   •   Industriale
   •   Energia
   •   Aeronautico



1.2.1. SEGMENTO INDUSTRIALE


L’ampia gamma di prodotti offerti dall’azienda, l’elevata affidabilità degli stessi e il
soddisfacimento delle più svariate esigenze dei clienti, hanno permesso di affermare il
brand Umbra nella maggior parte delle applicazioni industriali.

Tra i prodotti di maggior rilievo vengono considerati:

   •   Viti a ricircolo di sfere
   •   Cuscinetti
   •   Attuatori elettromeccanici (EMA)



VITI A RICICOLO DI SFERE

Realizzate per far fronte a specifiche richieste applicative quali:

   •   Alta velocità lineare degli assi
   •   Alte accelerazioni
   •   Alti carichi di spinta
   •   Riduzione delle vibrazioni delle viti di elevata lunghezza




                                                                                           11
                                  Figura 1.2. Vite a ricircolo di sfere industriale.




CUSCINETTI

Fin dalla sua fondazione l’azienda si è distinta nella produzione di cuscinetti di medie e
grandi dimensioni, sviluppando e consolidando la capacità progettuale e realizzativa di
cuscinetti a sfere, a rulli cilindrici, a rulli conici e a rulli a botte.




Figura 1.3. Alcune tipologie di cuscinetti fabbricati. Da sinistra a destra: a gola profonda, a doppia corona, combinati
assiali/radiali, a rulli conici.




                                                                                                                     12
ATTUATORI ELETTROMECCANICI (EMA)

La politica di miglioramento continuo e l’incessante attività di ricerca e sviluppo per
proporre soluzioni innovative e performanti, hanno portato alla produzione di sistemi
integrati. L’unione di componenti meccaniche, quali le viti a sfera, con componenti
elettronici aprono nuove sfide produttive e nuove opportunità di business per l’azienda.
L’ EMA è caratterizzato da magneti permanenti legati ad un dado a sfere in modo tale
che lo stesso dado a sfere, magnetizzato, diventi il rotore di un motore. Il vantaggio di
integrare verticalmente la catena cinematica ed eliminare i componenti di innesto e i
dispositivi di trasmissione, riduce sensibilmente la frizione tra i componenti generando
di conseguenza più forza, consumi ridotti e peso inferiore.




                          Figura 1.4. Attuatore elettromeccanico industriale.




                                                                                            13
1.2.2. SEGMENTO ENERGIA


L’attenzione nei confronti dell’ambiente rappresenta un fattore motivante del gruppo
Umbra, infatti è leader globale nella produzione di tecnologie per la generazione di
elettricità e movimento ad alta efficienza energetica. I prodotti fabbricati riducono il
numero di componenti utilizzati, consumano meno energia, generano più forza ed
eliminano l’utilizzo di fluidi pericolosi riducendo in questo modo sia l’impatto
ambientale che l’incidenza sui costi operativi, questi ultimi dovuti al continuo aumento
dei costi per l’energia. Tra questi prodotti rientrano gli EMA, soprattutto quelli
impiegati nella produzione di energia “green” ricavata ad esempio tramite gas
compresso o dal moto delle onde dell’oceano.




      Figura 1.5. Attuatore ad alta velocità di commutazione (a sinistra), generatore di potenza (a destra).




                                                                                                               14
1.2.3. SEGMENTO AERONAUTICO


I prodotti ad alte prestazioni realizzati in ambito aeronautico vantano di un’ottima
reputazione grazie all’efficienza dei processi di lavorazione e ai materiali utilizzati,
come ad esempio il “Cronidur 30”13. Attraverso l’esperienza acquisita nel settore è
infatti riuscita ad eliminare la corrosione, ridurre notevolmente l’usura e allungare
sensibilmente la durata di vita degli articoli. L’insieme di queste caratteristiche e
l’affidabilità dei componenti critici per il volo hanno permesso all’azienda di supportare
con i suoi prodotti molti costruttori di aerei tra cui: Boeing, Airbus, AVIC, Alenia-
Aermacchi, Dassault, Eurofighter, Mitsubishi, Panavia, Pilatius, BAe, Bombardier,
Cessna, Embraer, Fokker, Gulfstream, JDA, Learjet, Lockheed.

Tra i prodotti di maggior rilievo forniti, poiché fungono da cuore meccanico per le
superfici di controllo di volo primarie, secondarie e di sollevamento di alta potenza,
troviamo:

       •   Viti a ricircolo di sfere
       •   Viti acme dei velivoli
       •   Canne di sicurezza per velivoli
       •   Alberi e ingranaggi di precisione per aeromobili
       •   EMA

Una particolare importanza riveste l’attività di ricerca e sviluppo relativa ai componenti
per l’industria aerospaziale, grazie alla quale i prodotti permangono entro le tolleranze
di produzione originali, anche dopo oltre un decennio di servizio, riducendo in questo
modo i costi di manutenzione e di conseguenza i costi relativi al ciclo di vita del
prodotto.



VITI A RICIRCOLO DI SFERE

Utilizzate per applicazioni alquanto delicate, come ad esempio l’attuazione degli
ipersostentatori dell’ala e dello stabilizzatore orizzontale, sistemi di frenatura delle ruote
e inversori di spinta dei motori, le viti a ricircolo di sfere devono essere in grado di
sopportare forti stress di carico e durare a lungo. Per soddisfare questi requisiti, per la


13
     Acciaio inossidabile ad alto contenuto di azoto.
                                                                                              15
loro realizzazione, è stato introdotto il materiale “Cronidur 30”, combinato all’utilizzo
di sfere alternate nella chiocciola (sfera caricata in nitruro di silicio e sfera oziosa in
acciaio). Come risultato, la corrosione e l’usura prematura delle viti è stata praticamente
eliminata.




                            Figura 1.6. Vite a ricircolo di sfere aerospaziale.




VITI ACME

La tecnologia presente in Umbra, le permette di produrre viti ACME di alta qualità,
infatti grazie ai trattamenti termici e galvanici adottati ed agli innovativi processi di
produzione implementati, è in grado di creare un prodotto capace di sostenere carichi
estremamente elevati e quindi adatto ad applicazioni di inversione di spinta del motore.




                                         Figura 1.7. Vite ACME.




ALBERI DI TRASMISSIONE

Gli alberi di trasmissione prodotti dall’azienda sono di diversa tipologia e vengono
suddivisi in base al volume di carico che devono supportare:
                                                                                              16
    •   Basso carico
    •   Carico medio
    •   Alto carico

Questa famiglia di prodotti comprende un’ampia gamma di materiali, processi e
geometrie. Il loro impiego principale risiede nei sistemi di attuazione dei controlli di
volo, del carrello di atterraggio e in applicazioni per porta cargo.




                                Figura 1.8. Albero di trasmissione.




ATTUATORI ELETTROMECCANICI AEROSPAZIALI

La gamma dei prodotti Umbra per il settore aerospaziale si estende anche agli attuatori
elettromeccanici. Un esempio è l’attuatore a staffe per il freno dell’elica che, come tutti
i prodotti, presenta caratteristiche qualitative elevate e risulta essere robusto, affidabile e
ad alta efficienza. La principale funzione consiste nel ridurre dinamicamente la
rotazione dell’elica a velocità costante e fermarsi totalmente dopo lo spegnimento del
motore, anche in condizioni di forte vento.




                                                                                            17
Un’altra tipologia di attuatore elettromeccanico è quello a corsa lunga che sfrutta
l’architettura in-line. Progettato e realizzato nel rispetto dei più severi requisiti di
sicurezza, è in grado di soddisfare le esigenze più particolari dei clienti.




                Figura 1.9. Attuatore a staffe (a sinistra) e attuatore a corsa lunga (a destra).




                                                                                                    18
1.3. SERVIZI E PROCESSI

Per garantire l’efficienza delle proprie lavorazioni e prodotti eccellenti, UmbraGroup ha
internalizzato una serie di trattamenti termici e galvanici complessi. Questa strategia ha
permesso all’azienda di sviluppare competenze elevate per questo tipo di processi,
diventando a sua volta fornitore di un’ampia gamma di trattamenti termici-termochimici
e galvanici per aziende esterne. All’interno dello stabilimento è presente infatti un intero
reparto adibito ai trattamenti termici ed uno all’esecuzione di processi elettrolitici e
chimici di maggior interesse sia per il settore industriale che per quello aeronautico. La
qualifica NADCAP14 conseguita rispettivamente nel 2006 e nel 2007 per le due
tipologie di processo, fornisce un’ulteriore prova dell’elevato standard tecnico-
qualitativo del servizio svolto.

Oltre ai processi sopracitati, UmbraGroup effettua anche prove non distruttive in modo
tale da garantire un servizio qualificato di verifica sia delle proprietà meccaniche che
delle difettosità strutturali dei particolari.

Infine, dal 1996, l’azienda fornisce il servizio Aftermarket attraverso cui è in grado di
offrire al cliente un supporto tecnico eccezionale. La strategia organizzativa è incentrata
sull’adozione di una divisione avente struttura indipendente e dedicata, con lo scopo di
soddisfare i sempre più brevi tempi di turn-around, garantire prezzi competitivi, e
fornire prodotti e servizi di alta qualità.




14
  Programma di cooperazione delle imprese operanti nel settore aeronautico. La sua funzione consiste
nello standardizzare le procedure ed i requisiti di accreditamento dei fornitori, riducendo audit ridondanti
e promuovendo il miglioramento continuo. Link: https://qualitiamo.com/articoli/nadcap.html
                                                                                                          19
1.4. FILOSOFIA LEAN SIX SIGMA

La voglia di migliorarsi sempre più, per fornire dei prodotti di qualità superiore rispetto
alla concorrenza, ha spinto l’azienda a ricercare e successivamente implementare
soluzioni innovative sia a livello organizzativo sia produttivo, come ad esempio la
filosofia Lean Six Sigma.

"In un’azienda di livello internazionale e con un processo produttivo complesso come la
UmbraGroup, il ruolo del miglioramento continuo è fondamentale al fine di permettere al
Gruppo di mantenere il vantaggio competitivo nei mercati in cui opera".15




Tale filosofia trae beneficio da due metodologie. Questo approccio si basa sul concetto
di “Lean Production” combinato e integrato con quello della “Six Sigma”.
Sostanzialmente la Lean Production pone attenzione all’ottimizzazione delle risorse nei
processi produttivi in modo tale da eliminare gli sprechi, incrementando di conseguenza
la velocità e aumentando l’efficienza. La Six Sigma, invece, si focalizza sulla variabilità
e sulla riduzione dei difetti del processo con lo scopo di raggiungere livelli qualitativi
eccellenti. Questo risultato viene raggiunto mediante l’implementazione di un
programma di gestione della qualità basato sul controllo dello scarto quadratico medio
del processo e tutti gli strumenti di supporto.

Dunque, attraverso l’utilizzo della Lean Six Sigma i vantaggi che ne derivano sono:

       •   Riduzione dei costi
       •   Riduzione del lead time
       •   Eliminazione delle fasi prive di valore aggiunto
       •   Riduzione di scarti e rilavorazioni
       •   Riduzione della variabilità dei processi
       •   Miglioramento continuo:
               o Dei processi
               o Dell’apprendimento dell’organizzazione




15
     Cit. Valter Baldaccini, Padre Fondatore di UmbraGroup S.p.A.


                                                                                             20
CAPITOLO 2: NORMATIVE

2.1. IL SISTEMA DI GESTIONE DELLA QUALITA’

Nel corso degli anni, le dinamiche che regolano il mercato concorrenziale hanno subìto
dei cambiamenti radicali, passando dalla competizione sui prezzi (che punta ad offrire
lo stesso prodotto della concorrenza ad un prezzo più basso, anche se di qualità
leggermente inferiore, in modo tale da aggiudicarsi la fetta maggiore del mercato) alla
competizione sulla qualità. Il nuovo gioco a cui partecipano le aziende ha indotto un
meccanismo di sensibilizzazione all’aspetto qualitativo per cui il prodotto che presenta
una qualità elevata è sostanzialmente preferibile, anche se a prezzo maggiore (con il
giusto trade-off). Questo aspetto influisce sia sul cliente finale - utilizzatore del
prodotto/servizio – sia su tutta la filiera produttiva, dunque è molto importante
controllare e monitorare opportunamente la qualità.

Per rendere le aziende sempre più attente alla qualità dei prodotti/servizi che forniscono,
l’Organizzazione Internazionale della Standardizzazione (ISO) ha pubblicato un
documento contenente i requisiti necessari per sviluppare un efficace Sistema di
Gestione della Qualità (SGQ)16. Lo standard a cui fanno riferimento le aziende per
implementare un buon SGQ è la ISO 9001. Questa normativa è divenuta talmente
importante da vincolare la presenza sul mercato delle aziende e tale da selezionare
l’intera filiera produttiva, poiché la valutazione qualitativa delle aziende viene effettuata
da un organismo di certificazione esterno che ha le giuste competenze per attestare la
conformità delle stesse agli standard qualitativi.

Per Sistema di Gestione della Qualità si intende una serie di processi, politiche,
procedure e registrazioni attraverso cui si definiscono le modalità con cui l’azienda crea
e successivamente fornisce il prodotto/servizio al cliente. La ISO 9001 definisce le linee
guida per un corretto sviluppo del SGQ in modo tale da non trascurare nessun aspetto.
Tuttavia, è compito dell’azienda interpretare la norma per costruire un SGQ su misura,
tenendo in considerazione il proprio contesto organizzativo nonché la tipologia di
prodotto che fornisce.



16
   I requisiti di un buon Sistema di Gestione della Qualità sono applicabili ad ogni tipologia di impresa,
operante in ogni settore. Il documento, per essere pubblicato e riconosciuto a livello internazionale, è
stato sottoposto a verifica e approvazione dalla maggioranza degli stati membri.
                                                                                                             21
I requisiti che vertono sul SGQ fanno riferimento a:

   •   Contesto organizzativo
   •   Leadership
   •   Pianificazione
   •   Supporto
   •   Funzionamento
   •   Valutazione delle prestazioni
   •   Miglioramento




                                                       22
2.2. IAQG

L’International Aerospace Quality Group (IAQG) è un’associazione cooperativa no
profit, fondata nel 1998 dai maggiori produttori mondiali operanti nel settore
aeronautico. L’obiettivo del gruppo è quello di instaurare e coltivare la cooperazione tra
aziende per proporre iniziative incentrate sul miglioramento continuo della qualità e
sulla riduzione dei costi.

Il focus principale ricade sui processi implementati nella filiera produttiva. Una corretta
gestione dei processi permette di consegnare prodotti di alta qualità, riducendo le
attività che non producono valore. L’IAQG è composta da circa 50 membri
rappresentativi, suddivisi in tre macro aree: America (AAQG), Europa (EAQG),
Asia/Pacifico (APAQG) e rappresenta l’ente di riferimento in ambito qualitativo
preposto a stabilire, in collaborazione con agenzie governative, standard e requisiti a cui
tutti devono attenersi per operare in questo settore.

Si incontra periodicamente per promuovere nuove iniziative o risolvere i problemi
riscontrati. Il coinvolgimento dei leader del settore rappresenta un forte incentivo al
miglioramento.




                                                                                          23
2.2.1. AS/EN 9100


La normativa che regola il sistema di gestione di qualità nel settore aerospaziale è la
AS/EN 910017, che acquisisce una determinata nomenclatura (AS o EN) in base al
continente considerato, rispettivamente America o Europa. Essa si basa sui requisiti
della ISO 9001, integrandoli ed adattandoli in riferimento alla specificità del settore. In
particolare, è importante tenere in considerazione aspetti qualitativi più restrittivi nel
settore aeronautico, in grado di garantire elevata sicurezza, affidabilità e manutenibilità,
conformi alle specifiche civili e militari imposte.

La normativa standardizza il sistema di gestione della qualità nelle aziende aerospaziali
mondiali. In tal modo, le organizzazioni vengono guidate nel perseguire e soddisfare i
requisiti stabiliti dalle autorità di controllo, adottando metodologie approvate e
riconosciute a livello internazionale. È importante sottolineare che lo strumento di
sorveglianza è rivolto a tutta la catena di fornitura, in modo tale da garantire qualità e
sicurezza in tutto il ciclo produttivo.

I benefici derivanti dall’adozione dello standard sono:

     •   Capacità di fornire costantemente prodotti, servizi e processi che soddisfino i
         requisiti legali e normativi applicabili
     •   Migliorare la soddisfazione del cliente
     •   Dimostrare la conformità ai requisiti specifici del sistema di gestione della
         qualità




17
 AS/EN 9100:2016, Quality Management Systems - Requirements for Aviation, Space and Defense
Organizations.
                                                                                              24
2.2.2. AS/EN 9102


La norma AS/EN 910218 standardizza la documentazione relativa al First Article
Inspection (FAI) per la verifica dei prodotti aeronautici, spaziali e della difesa. Una
buona pianificazione ed esecuzione del FAI fornisce un’evidenza che il processo
produttivo è in grado di produrre prodotti conformi ai requisiti ingegneristici e di
progetto.

Il FAI rappresenta un processo di ispezione pianificata, completa, indipendente e
documentata, finalizzata a garantire che i processi di produzione prescritti abbiano
prodotto un articolo conforme alle specifiche tecniche.

Quindi il FAI deve:

       •   Garantire che i processi di realizzazione del prodotto siano in grado di produrre
           una parte conforme
       •   Dimostrare che i produttori abbiano compreso i requisiti richiesti
       •   Ridurre i potenziali rischi associati all’avvio della produzione e/o modifiche del
           processo
       •   Garantire la conformità del prodotto all’inizio della produzione e dopo le
           modifiche del processo produttivo delineate dalla AS/EN9102
       •   Ridurre i costi totali
       •   Garantire la sicurezza delle parti in volo
       •   Migliorare la qualità e la soddisfazione del cliente
       •   Ridurre i ritardi di produzione associati alle non conformità del prodotto
       •   Ridurre le non conformità di prodotto
       •   Identificare i processi che non sono in grado di produrre un prodotto conforme e
           avviare e/o convalidare azioni correttive




18
     AS/EN 9102:2015, Aerospace First Article Inspection Requirement.
                                                                                           25
CAPITOLO 3: MERCATO AERONAUTICO

3.1. PREVISIONI CRESCITA SETTORE AERONAUTICO

Nel corso degli anni i produttori di velivoli, guidati da un’incessante globalizzazione e
dalla necessità dell’essere umano di voler connettersi ed interfacciarsi sempre più con il
mondo intero nella maniera più rapida possibile, hanno incrementato sensibilmente la
produzione.

Esaminando gli ultimi 40 anni di storia dell’aviazione è possibile osservare che il
traffico aereo risulta essere resiliente a shock economici e geopolitici.




                           Figura 3.1. Trend traffico aereo (fonte: Airbus).




Come si evince dal grafico, il traffico aereo ha avuto un trend crescente, nonostante si
siano verificati eventi che hanno minacciato l’equilibrio economico mondiale. In
corrispondenza di questi eventi si ha solamente una stabilizzazione dell’intensità di
traffico aereo che, nel lungo periodo, è comunque raddoppiato ogni 15 anni circa. I dati
forniscono una previsione dei prossimi 20 anni più che favorevole per il settore, in cui si
assisterà ad una continua crescita della domanda.

Questo effetto si rifletterà di conseguenza anche sulla produzione di velivoli.

Secondo recenti studi, infatti, nei prossimi venti anni è stato stimato un incremento del
fabbisogno di velivoli per il trasporto aereo di passeggeri e di merci che passerà da

                                                                                           26
23000 a circa 48000 aeroplani. Le previsioni mostrano una panoramica di un mercato in
forte espansione, con una crescita annua prevista del 4,3% nel settore19. Le cause di
questo aumento di fabbisogno sono da ricercare nella continua crescita del turismo,
nella disponibilità di nuove rotte, nei nuovi modelli di business sviluppati dalle
compagnie aeree e nella liberalizzazione del settore. La crescente domanda di velivoli è
condizionata non solo dai fattori appena citati, ma anche dalla necessità di ritirare gli
aerei ormai obsoleti che hanno concluso il loro ciclo di vita. Un aereo è considerato
obsoleto quando il costo sostenuto per mantenerlo in funzione eccede il profitto che
potrebbe generare. Mediamente il ciclo di vita di un aereo varia tra i venti e i trenta
anni. Inoltre, la continua innovazione tecnologica permette di sviluppare prodotti
sempre più efficienti dal punto di vista dei consumi, della capacità di carico, nonché
conformi alle restrittive politiche ambientali, cosa che gli aerei datati ma ancora in
grado di esercitare non soddisfano.

Secondo le stime, circa il 40% dei nuovi aerei sarà necessario per rimpiazzare quelli “in
pensionamento”.




                            Figura 3.2. Previsione produzione di velivoli (fonte: Airbus).




Gli effetti descritti si manifesteranno con maggiore incidenza nella regione Asia-
Pacifico, a cui è associato circa il 40% dei nuovi aeromobili (di cui il 19% solo per la
Cina). Le dinamiche che guidano questa crescita di domanda sono intrinseche nello
sviluppo economico del paese, infatti la regione Asia-Pacifico rappresenta una delle


19
     Global Market Forecast, Cities, Airports & Aircraft, 2019-2038, Airbus.
                                                                                             27
principali economie in rapida crescita del mondo. La Cina, in particolare, ha avuto un
tasso di crescita medio di oltre il 7% negli ultimi 10 anni, contribuendo ad estendere il
ceto sociale medio e di conseguenza anche la propensione al consumo e agli
spostamenti tramite mezzi di trasporto via aria.

Seguiranno Nord America ed Europa, entrambe con circa il 20% di nuovi velivoli,
Medio Oriente (7%), America Latina (6,7%), Russia e Asia Centrale (3%) e Africa
(2,6%).


                    Distribuzione previsione di domanda mondiale di velivoli

                                                3%       3%
                                         7%
                                 7%

                                                                               39%



                              20%



                                                         21%
                     Asia-Pacifico             Nord America             Europa
                     Medio Oriente             America Latina           Russia e Asia Centrale
                     Africa

      Figura 3.3. Previsione della distribuzione della domanda mondiale di nuovi velivoli (fonte: Airbus).




                                                                                                             28
3.2. EFFETTO COVID-19 SULL’ANALISI

Purtroppo, ad oggi stiamo sperimentando sulla nostra pelle un evento drammatico, dalle
ingenti conseguenze sociali ed economiche, che non è stato possibile prevedere
nell’analisi e che sta condizionando in maniera aggressiva l’intero assetto economico
mondiale. Durante lo svolgimento del presente lavoro di tesi, il mondo intero è entrato
“in guerra” contro un nemico invisibile. L’emergenza globale dovuta alla comparsa del
Covid-19 avrà un impatto significativo sul settore e si sta assistendo ad una netta
diminuzione del traffico aereo a seguito delle disposizioni emanate dai governi
mondiali. La limitazione delle tratte, la cancellazione dei voli e l’impossibilità di
effettuare spostamenti sia a lungo che a corto raggio è sinonimo di una strategia
indispensabile per evitare una propagazione inarrestabile del contagio. Non è possibile
prevedere con esattezza quando si manifesterà un segnale di ripresa, ma dai dati storici
pervenuti è possibile ipotizzare che nel lungo periodo ci sarà comunque un aumento
della domanda. Tuttavia, è anche vero che una crisi generalizzata di questa entità non si
è mai manifestata. Le epidemie infettive e virali che si sono diffuse nei recenti anni,
sono state in linea di massima concentrate in determinate aree geografiche. Basti
pensare alla SARS, che nei primi anni duemila si diffuse maggiormente nel sud est
asiatico, colpendo solo in minima parte gli altri continenti i quali, con giuste misure
preventive, riuscirono a debellare in pochissimo tempo il virus. Oppure alla diffusione
dell’Ebola nel triennio tra il 2013 ed il 2016 circa, che ebbe una concentrazione
predominante solo in alcuni stati dell’Africa occidentale. Il COVID-19 invece, anche se
meno letale, ha una capacità di propagazione più elevata ed in poco tempo si è diffuso
praticamente in tutto il globo. Le misure adottate per il contenimento del virus hanno un
impatto enorme sull’attività economica mondiale, per cui è lecito aspettarsi una crisi
generalizzata che graverà sulle Nazioni per un periodo di tempo più o meno lungo,
ancora difficile da quantificare.

Alcuni studiosi hanno cercato di analizzare oggettivamente la situazione e dare un senso
a tutto ciò che sta accadendo. Partendo dall’analisi del tasso di mortalità del virus, si
stima che il numero di contagiati sia almeno 10 volte superiore rispetto ai dati ufficiali, i
quali fanno riferimento solo alle persone sottoposte ai controlli con il tampone. Dunque,
i numeri che vediamo rappresentano solo la punta dell’iceberg, per cui si stima che in
realtà la letalità del virus sia dell’ordine dell’1% circa.


                                                                                            29
Le vere problematiche che ci trascineremo negli anni non saranno riferite alla mortalità
del virus, ma riguarderanno la messa in crisi del settore sanitario e in particolar modo
l’economia dei Paesi.

A livello economico, infatti, siamo entrati probabilmente nella recessione più grande
degli ultimi 100 anni. Le cause di tale recessione sono dovute alla completa sospensione
del sistema produttivo per cercare di limitare il contagio. Tale decisione ha portato alla
perdita di posti di lavoro, che a sua volta ha ridotto la capacità economica delle famiglie
le quali hanno una minore propensione al consumo. La minor capacità di spesa, insieme
alla sensazione di incertezza, ha scoraggiato anche gli investimenti, per cui risulta
ancora più difficoltoso far girare l’economia.

Per capire l’entità della recessione, gli studiosi hanno individuato 3 forme di recessione:

       •   Forma a “V”: dopo una caduta improvvisa della ricchezza vi è un’altrettanta
           improvvisa ripresa della crescita. Questo tipo di recessione ha caratterizzato gli
           ultimi 300 anni di storia
       •   Forma a “U”: dopo la caduta, si assiste ad una ripresa molto più lenta e la
           crescita non sarà la stessa di prima
       •   Forma a “L”: la caduta è continua e non sarà possibile riprendere la crescita. È
           l’esempio della Grecia

È importante considerare che ogni nazione potrebbe avere una forma di recessione
diversa. La Cina, ad esempio, potrebbe avere una forma di recessione a “V” e quindi
riprendersi abbastanza velocemente. Per quanto riguarda l’Italia, invece, gli esperti
hanno ipotizzato un tipo di recessione a “U”20. Questo perché si stima una sostanziale
caduta del PIL ed un aumento del debito pubblico dovuto all’ immissione di moneta nel
sistema. Il debito pubblico impatta su tutta la popolazione che inevitabilmente avrà una
minor capacità di spesa. Molte imprese che non saranno in grado di gestire la situazione
subiranno danni strutturali significativi difficili da ripristinare e, nel peggiore dei casi, il
fallimento sarà l’unica via percorribile.

Le aziende sono poste di fronte ad un cambiamento, per cui l’unica soluzione per
sopravvivere è quella di comprendere come sono mutate le esigenze dei clienti e cercare
di adattarsi. Questo evento ha trasformato completamente le abitudini delle persone:



20
     Il Sole 24 ore, Che ripresa sarà quando il Covid-19 sarà un ricordo?
                                                                                              30
vivere a distanza ha avuto un forte impatto nello sviluppo del digitale (ad esempio le
piattaforme per lo smart-working). Dunque, alcuni settori potrebbero esplodere, mentre
altri potrebbero andare in recessione profonda. È necessario re-inventarsi per non
soccombere.

In conclusione, la ripresa economica ci sarà, ma molto probabilmente sarà lenta e ci
vorrà del tempo per tornare ai livelli di prima poiché l’impatto è significativo.




                                                                                         31
3.3. DALLA AS/EN 9102 ALLA AS/EN 9145

Dalle considerazioni effettuate, molto probabilmente nei prossimi anni sarà possibile
assistere al ritorno delle condizioni antecedenti la comparsa del virus, e le previsioni
della domanda di velivoli si presume resteranno pressoché invariate, a meno di una
dilatazione dei tempi.

Sotto tali condizioni, l’approccio attualmente adottato per lo sviluppo di nuovi prodotti
nel settore aeronautico, ai livelli richiesti dal mercato, non risulta essere soddisfacente.
In pratica, ciò che acquisirà un’importanza fondamentale sarà: la rapidità di risposta alle
esigenze del cliente, il rispetto dei requisiti di sicurezza e di qualità imposti dalle
autorità competenti e/o dal cliente, e una capacità produttiva in grado di soddisfare la
continua crescita della domanda analizzata precedentemente. Il tutto deve essere
effettuato minimizzando il più possibile gli scarti di produzione e le rilavorazioni, in
quanto genererebbero:

    •      Slittamento dei tempi di consegna che potrebbero propagarsi lungo tutta la
           filiera produttiva
    •      Costi aggiuntivi

Inoltre, la complessità dei prodotti adottati nel settore aeronautico fa presumere che ci
sia un’elevata probabilità di riscontrare fallimenti, soprattutto nello sviluppo di un
nuovo prodotto innovativo.

Per far fronte alle esigenze appena citate, è stato analizzato il settore dell’automotive
che da tempo sfrutta le metodologie APQP e PPAP, basate su dei principi e delle
tecniche strutturate in grado di permettere ai costruttori di sviluppare nuovi prodotti in
tempi ristretti, rispettando il budget a disposizione e garantendo la soddisfazione del
cliente.

Prendendo come riferimento l’automotive, il team dell’IAQG ha realizzato nel 2016 uno
standard normativo chiamato AS 9145 in cui vengono ripresi i concetti dell’APQP e
PPAP, adattandoli al settore aeronautico che è caratterizzato da:

    •      Bassi volumi
    •      Lunghi cicli di vita dei prodotti
    •      Alto grado di regolamentazione


                                                                                             32
Storicamente, per verificare la conformità di un prodotto aeronautico, si è fatto
affidamento sul First Article Inspection (FAI). Con la metodologia APQP, il FAI viene
incorporato nel pacchetto PPAP e viene esteso il concetto di conformità anche alla
capacità produttiva. Questo risultato viene raggiunto grazie alla verifica del componente
effettuata sulla produzione pianificata al tasso di domanda richiesto dal cliente.




                                                                                       33
CAPITOLO 4: AS/EN 9145

4.1. INTRODUZIONE ALL’APQP

Lo standard AS 9145 definisce i requisiti necessari per implementare un buon processo
APQP21, applicabili a tutti i livelli della catena di fornitura.
L’APQP è un metodo strutturato finalizzato ad assicurare che il processo di sviluppo del
prodotto, implementato dall’organizzazione, sia totalmente integrato. Vengono
sincronizzati i processi che vanno dalla concezione del prodotto e la sua progettazione,
fino alla produzione, all’utilizzo del prodotto, ai servizi post consegna e ai feedback del
cliente.
Sostanzialmente guida nell’implementazione del piano di qualità necessario a garantire
la soddisfazione del cliente e supporta l’identificazione precoce dei possibili
cambiamenti, sia intenzionali che accidentali, relativi al nuovo prodotto o processo da
sviluppare.




21
 Altri dettagli possono essere reperiti su: International Aerospace Quality Group, Supply Chain
Management Handbook. Link: www.sae.org/scmh
                                                                                                  34
4.1.1. OBIETTIVI


Gli obiettivi alla base dell’implementazione del processo APQP sono:

   •   Assicurare un avvio di produzione affidabile rispettando:
          o Livelli qualitativi richiesti
          o Tasso di domanda richiesto dal cliente
   •   Utilizzare approccio di project management per una consegna puntuale del
       prodotto, monitorando le key deliverables del progetto
   •   Servirsi di un team cross-funzionale per una maggiore comunicazione
   •   Promuovere una mentalità proattiva
   •   Mantenere il processo sotto controllo
   •   Miglioramento continuo dei processi
   •   Riduzione dei costi attraverso:
          o Strumenti di prevenzione per la riduzione del rischio
          o Precoce raggiungimento della maturità del prodotto
          o Costruzione di basi solide per efficaci implementazioni di cambiamenti
          o Riduzione dei costi generali inerenti al ciclo di vita del prodotto




                                                                                  35
4.1.2. VANTAGGI


I principali vantaggi derivanti dall’applicazione della metodologia sono:

    •   Dirigere le risorse focalizzando l’attenzione su una selezione di elementi ritenuti
        vitali
    •   Incentivare l’identificazione precoce di cambiamenti intenzionali (utile per
        apportare maggior valore per il cliente) e accidentali
    •   Evitare cambiamenti tardivi anticipando e prevenendo le cause di fallimento
        garantendo poche modifiche di progetto e di processo durante lo sviluppo del
        processo produttivo
    •   Fornire un prodotto di qualità in tempo e ad un costo inferiore
    •   Possibilità di individuare diverse azioni per la riduzione dei rischi poiché
        analizzati anticipatamente
    •   Maggiore possibilità di validazione e approvazione di un cambiamento
    •   Migliore collaborazione tra progettazione del prodotto e processo da
        implementare
    •   Identificazione anticipata della soluzione che presenta il costo più basso
    •   Creazione ed utilizzo di lavori standard efficaci

Il processo APQP è composto da cinque fasi, ognuna delle quali è definita dagli
elementi contenuti in essa. A loro volta ciascuno di questi elementi definisce attività da
svolgere e deliverables, molti dei quali diventano un’evidenza nel pacchetto PPAP.

Per questo motivo il PPAP viene considerato un output dell’APQP e la sua funzione
consiste nel dimostrare che il processo produttivo ha il potenziale di produrre
componenti in grado di soddisfare a pieno i requisiti del cliente al tasso di produzione
richiesto.

Lo scopo del PPAP è dunque quello di analizzare tutti i requisiti inerenti sia al prodotto
che al progetto e determinare se il processo produttivo del fornitore è in grado di
mantenere questi requisiti in una produzione di serie. È composto da una serie di
documenti che fanno capo ad un unico modulo denominato “PPAP Approval Form” il
quale viene consegnato dal fornitore al cliente insieme a tutta la documentazione e alla
campionatura del prodotto. Il cliente, ricevuto il documento, fa tutte le verifiche
necessarie per valutare il raggiungimento o meno degli obiettivi.

                                                                                           36
4.2. PRODUCT PART APPROVAL PROCESS (PPAP)

Di seguito vengono analizzati gli elementi che costituiscono il PPAP in modo da
riuscire a comprendere meglio la loro collocazione all’interno del processo APQP.

Lo standard AS 9145 suddivide il PPAP in 11 punti chiave. Tuttavia, ciò non esclude
che il cliente possa richiedere degli elementi aggiuntivi a seconda delle proprie
esigenze.

Lo standard definisce:

    1. Documenti di progettazione
    2. Analisi dei rischi di progettazione (DRA)
    3. Diagramma di flusso del processo
    4. Process Failure Mode & Effect Analysis (PFMEA)
    5. Piano di controllo
    6. Measurement System Analysis (MSA)
    7. Studio iniziale della capacità del processo
    8. Approvazione imballaggio, conservazione ed identificazione
    9. First Article Inspection Report (FAIR)
    10. Requisiti specifici del cliente
    11. PPAP approval form

È importante sottolineare che la responsabilità dello sviluppo degli elementi del PPAP
ricade solo su quelli che fanno riferimento al business dell’organizzazione. Ad esempio,
se l’azienda non ha alcuna autorità sulla progettazione, essa non sarà responsabile
dell’analisi dei rischi di progettazione.




                                                                                      37
4.2.1. DOCUMENTI DI PROGETTAZIONE


La documentazione inerente alla progettazione deve essere redatta ogni qual volta venga
progettato o riprogettato un prodotto. Lo scopo è quello di verificare che il fornitore
abbia svolto la progettazione del componente e del processo come concordato con il
cliente e nel rispetto dei requisiti imposti dall’organo governativo.

Essa deve contenere:

     •   Dati CAD/CAM
     •   Disegni del prodotto
     •   Specifiche
     •   Lista di tutti i requisiti e caratteristiche



4.2.2 ANALISI DEI RISCHI DI PROGETTAZIONE (DRA)


L’analisi viene effettuata dal responsabile alla progettazione il quale, attraverso tecniche
analitiche, cerca di identificare i potenziali rischi legati alla performance del prodotto,
alla sua durata, alla producibilità e ai costi associati. L’obiettivo di tale attività consiste
nel documentare i rischi, indicando le attenuazioni necessarie, le azioni intraprese ed i
risultati ottenuti. Inoltre, funge da supporto nell’identificazione dei Critical Items
(CI’s)22 e delle Key Characteristics (KC’s)23 del prodotto, rappresentando un input della
DFMEA spiegata di seguito.




22
   Elementi che hanno un significativo impatto sulla realizzazione del prodotto, sulla sicurezza dello
stesso, e che richiedono azioni specifiche affinché vengano trattati adeguatamente.
23
   Caratteristiche del materiale o del prodotto la cui variazione deve essere opportunamente controllata,
poiché una loro piccola variazione ha un’influenza significativa su performance, vita utile, realizzazione e
adattamento del componente.
                                                                                                         38
4.2.3. DESIGN FAILURE MODE & EFFECT ANALYSIS (DFMEA)


La DFMEA è uno strumento che utilizza un approccio strutturato al fine di identificare e
successivamente stabilire l’ordine di priorità dei potenziali rischi che possono
manifestarsi durante lo sviluppo di un nuovo prodotto o di un cambiamento ad esso
associato. Attraverso questo metodo vengono determinate le possibili modalità di
fallimento relative alla fase di progettazione, ne vengono imputati gli effetti, dopodiché
viene assegnato un ordine di priorità alle azioni da intraprendere basandosi su:

   •    Frequenza di accadimento
   •    Impatto
   •    Facilità di individuazione

Il processo appena descritto non è fine a sé stesso, in quanto segue l’intero ciclo di vita
del prodotto ed è opportuno aggiornare continuamente le informazioni contenute nella
DFMEA, poiché saranno utili nel successivo ciclo di sviluppo del prodotto.



4.2.4. DIAGRAMMA DI FLUSSO DEL PROCESSO


Una volta rilasciata la versione preliminare del progetto, bisogna focalizzarsi sul
processo che renderà possibile la realizzazione del prodotto. Il diagramma di flusso del
processo è una rappresentazione grafica della sequenza di operazioni e attività inerenti
al processo da sviluppare.

La sua funzione è quella di:

    •   Facilitare la visione complessiva del processo
    •   Mostrare i collegamenti tra le singole attività
    •   Evidenziare input e output di ogni fase del processo
    •   Individuare le attività non direttamente connesse al processo produttivo
        (misurazioni, ispezioni, movimentazioni)
    •   Distinguere le rilavorazioni pianificate da quelle non pianificate
    •   Fornire supporto nell’identificazione delle risorse necessarie




                                                                                          39
4.2.5. PROCESS FAILURE MODE & EFFECT ANALYSIS (PFMEA)


Come effettuato nella fase di progettazione del prodotto, in cui è stato stilato il
documento DFMEA, anche per lo sviluppo del processo viene adottato un metodo
strutturato per l’identificazione delle possibili modalità di fallimento e il loro impatto
sul processo in esame. In particolare, facendo riferimento al processo produttivo,
vengono analizzate e descritte le possibili non conformità ai requisiti del prodotto che
potrebbero generarsi, cercando di determinare le cause radici e le conseguenze che ne
scaturiscono.

È statisticamente impossibile cercare di individuare ed eliminare completamente tutte le
modalità di fallimento, poiché richiederebbe un impiego illimitato di risorse, una
conoscenza assoluta di ciò che potrebbe accadere (altamente improbabile), nonché
risulterebbe economicamente insostenibile. Per questo motivo viene assegnato un
ordine di priorità alle failure mode caratterizzandole in base a:

     •   Frequenza di accadimento
     •   Impatto
     •   Facilità di individuazione

In questo modo è possibile concentrarsi prima di tutto sugli elementi prioritari, cercando
di individuarne le cause radici e implementando un piano di azione preventivo per
eliminare o ridurre la manifestazione delle failure mode considerate.

La PFMEA rappresenta anche uno strumento incentivante per il miglioramento
continuo, dato che può essere vista come un incubatore di esperienze grazie al quale è
possibile imparare dagli errori commessi24.




24
  Per sviluppare una PFMEA quanto più completa e robusta possibile è necessario il coinvolgimento di
un team cross-funzionale.
                                                                                                   40
4.2.6. PIANO DI CONTROLLO


Il piano di controllo lega le fasi del processo produttivo all’attività ispettiva e di
controllo. L’intento è quello di controllare, attraverso metodi di misurazione, strumenti
e procedure, il rispetto delle caratteristiche di progetto, nonché di valutare la variabilità
del processo affinché venga assicurata la qualità richiesta del prodotto.

Attraverso il piano di controllo è possibile:

    •   Monitorare le Key Characteristics (KC’s) ed i Critical Items (CI’s) definiti sia
        dal cliente che dall’organizzazione
    •   Gestire al meglio il processo per ridurre la variabilità delle caratteristiche del
        prodotto in uscita
    •   Definire le azioni da intraprendere in situazioni di fuori controllo ed assicurare il
        mantenimento dei miglioramenti apportati durante l’intero ciclo di vita del
        prodotto



4.2.7. MEASURAMENT SYSTEM ANALYSIS (MSA)


L’analisi del sistema di misura viene utilizzata per comprendere il grado di precisione e
accuratezza delle misure effettuate sui componenti a monte, a valle e in corrispondenza
delle fasi di ispezione del processo produttivo. Essa viene eseguita utilizzando strumenti
statistico-matematici finalizzati a quantificare la variabilità del processo di misurazione
che, a sua volta, influenza anche la variabilità complessiva del processo di produzione.

I dati raccolti durante il processo di misurazione vengono utilizzati per prendere
decisioni sul processo produttivo ed è fondamentale che siano quanto più accurati
possibile. Un sistema di misura inefficiente e non calibrato alla perfezione conduce ad
una raccolta di dati distorti e contribuirebbe alla manifestazione di errori di prima specie
(rifiutare parti in realtà buone) e di seconda specie (accettare parti in realtà non
conformi), alterando gli interventi correttivi da attuare per migliorare il processo.




                                                                                             41
4.2.8. STUDIO INIZIALE DELLA CAPACITÀ DEL PROCESSO


Durante il primo avvio di produzione al tasso produttivo concordato con il cliente, viene
effettuato il primo studio effettivo relativo alla capacità del processo a regime.

Lo studio consiste nell’analisi dei risultati ottenuti nelle attività svolte nel piano di
controllo, relativi sia all’aspetto dimensionale del prodotto sia alle Key Characteristics
del processo individuate.

Attraverso questa analisi è possibile determinare se l’insieme delle metodologie,
macchine, risorse, materiali e strumenti di misura utilizzati, ha il potenziale di fornire un
prodotto che soddisfa costantemente i requisiti di progetto.

Per dare una valutazione oggettiva sul comportamento del processo viene utilizzato
l’indice di capacità del processo definito come segue (Douglas C. Montgomery, 6th
Edition):

                                   𝐶𝑝𝑘 = min( 𝐶𝑝𝑖 ; 𝐶𝑝𝑠 )

Esplicitando i termini fra parentesi:

                                                𝜇 − 𝐿𝑆𝐿
                                        𝐶𝑝𝑖 =
                                                  3𝜎

                                                𝑈𝑆𝐿 − 𝜇
                                        𝐶𝑝𝑠 =
                                                  3𝜎

Con 𝜇 media del processo, LSL e USL limiti di specifica inferiore e superiore, 𝜎
deviazione standard del processo.

𝐶𝑝𝑖 e 𝐶𝑝𝑠 rappresentano dunque una misura degli indici di capacità del processo relativi
rispettivamente al limite di specifica inferiore e superiore.

A denominatore compare 3𝜎 poiché si assume che il processo segue una distribuzione
normale 𝑁~( 𝜇 , 𝜎 ) e presenta una tolleranza naturale 𝑇𝑁 = ±3𝜎 in cui sono contenuti
il 99,73% dei valori.

Attraverso l’indice 𝐶𝑝𝑘 , applicato ad ogni caratteristica qualitativa da valutare, è
possibile fare delle considerazioni sulla centratura del processo in quanto tiene conto
della posizione effettiva di 𝜇 rispetto ai limiti di specifica. Più l’indice restituisce un



                                                                                              42
valore elevato, più il processo si comporta bene, riducendo la probabilità di produrre dei
pezzi fuori specifica.

Il valore di riferimento che soddisfa il criterio di accettazione risulta essere in generale
𝐶𝑝𝑘 ≥ 1,33 ma questo valore potrebbe variare a seconda delle esigenze del cliente.



4.2.9. APPROVAZIONE IMBALLAGGIO, CONSERVAZIONE ED
IDENTIFICAZIONE


Tra gli elementi contenuti nel PPAP viene presa in considerazione anche la validazione
del processo di consegna, attraverso la richiesta di approvazione delle attività ad esso
inerenti.

Lo scopo è quello di assicurare sia che il prodotto o il materiale da consegnare non
presenti danni strutturali scaturiti da una scorretta conservazione, sia che l’attività di
imballaggio ed impacchettamento sia stata eseguita correttamente e manterrà le stesse
prestazioni durante il trasporto, la consegna e lo stoccaggio.



4.2.10. FIRST ARTICLE INSPECTION REPORT (FAIR)


Il FAI, come discusso nel capitolo §2 relativo alle normative, è un processo di ispezione
completa ed indipendente volto a verificare che il processo produttivo ha realizzato un
pezzo conforme alle specifiche ingegneristiche, ai disegni, all’ordine di acquisto e ad
ogni altro documento di progetto.

Lo scopo del FAI è di fornire un’evidenza pragmatica, basata sulla valutazione del
primo articolo prodotto durante l’avvio della produzione, che tutti i requisiti sono stati
compresi in maniera chiara dall’organizzazione, verificati e documentati.

È bene ricordare che il FAI è un elemento del PPAP ma potrebbe essere approvato
prima della consegna del suddetto. Inoltre, è opportuno specificare che il FAI è un
documento che attesta la conformità ai requisiti di progetto del primo pezzo prodotto,
mentre tramite il PPAP si ha una validazione del processo produttivo anche in termini di
capacità e ripetibilità del processo, garantendo il corretto avvio di una produzione
futura.

                                                                                             43
4.2.11. REQUISITI SPECIFICI DEL CLIENTE


Potrebbe accadere che, nel commissionare un determinato lavoro, il cliente abbia la
necessità di specificare altri elementi non inclusi in quelli richiesti dallo standard
aeronautico AS 9145. In queste circostanze è opportuno identificare i requisiti
aggiuntivi durante la fase di project-planning, definendo le tempistiche e le appropriate
funzioni organizzative coinvolte.

Il documento “requisiti specifici del cliente” è parte integrante del pacchetto PPAP e
certifica il rispetto dei requisiti aggiuntivi richiesti secondo le modalità definite dal
cliente.



4.2.12. PPAP APPROVAL FORM


Una volta completati gli elementi del PPAP, le informazioni vengono sintetizzate in un
unico documento ed inviato, insieme al pacchetto PPAP, al cliente. Il PPAP Approval
Form contiene, oltre alle informazioni identificative di prodotto, disegno e ordine di
produzione, una checklist dei punti sviluppati dall’organizzazione sui quali il cliente
effettuerà le proprie valutazioni e stabilirà il proprio grado di soddisfazione, con relativi
commenti, accettando o meno i singoli elementi.

Fatte le dovute considerazioni, il cliente ha la facoltà di scegliere tra 3 stati di
approvazione:

    •      Approvazione completa
    •      Approvazione provvisoria
    •      Rifiutato



Approvazione completa

Il prodotto e la relativa documentazione soddisfano tutti i requisiti ed il fornitore ha
l’autorizzazione per fornire il prodotto.

Approvazione provvisoria

Lo stato di approvazione provvisoria si verifica nel caso in cui:

                                                                                            44
   •   Non tutti i requisiti del cliente risultano soddisfatti
   •   Le cause principali di non conformità ai requisiti è stata individuata dal
       fornitore, il quale ha predisposto un piano d’azione provvisorio a sua volta
       approvato dal cliente
   •   Il cliente potrebbe accettare la fornitura per uno specifico lasso di tempo o in
       quantità diversa da quella concordata
   •   È richiesta un’integrazione degli elementi che risultano essere incompleti

Rifiutato

Lo stato di rifiuto implica che il prodotto e la relativa documentazione non soddisfano le
aspettative del cliente, per cui il fornitore non è autorizzato a spedire il prodotto e deve
inviare un nuovo PPAP al cliente, contenente gli elementi mancanti o incongruenti.




                                                                                           45
4.3. ADVANCED PRODUCT QUALITY PLANNING (APQP)

Spiegati gli elementi caratterizzanti della documentazione PPAP, di seguito viene
analizzato nel dettaglio il processo APQP relativo allo standard AS/EN 9145.



4.3.1. I PILASTRI DELL’APQP


Il processo APQP non è semplice da implementare, richiede impegno, organizzazione e
capacità di adattamento da parte di tutti gli attori coinvolti. Esso si fonda su dei concetti
base in assenza dei quali sarebbe impossibile raggiungere i risultati sperati.
Questi concetti assumono infatti la denominazione di “pilastri”, per meglio rendere
l’idea che, la mancanza di anche solo uno di essi, farebbe collassare l’intera struttura.

I pilastri del processo APQP sono:

   •   Impegno organizzativo e supporto del Management
   •   Team cross-funzionale
   •   Pianificazione efficace




                       Figura 4.1 Pilastri dell'APQP (fonte: ASQ, Quality Progress).


                                                                                            46
IMPEGNO ORGANIZZATIVO E SUPPORTO DEL MANAGEMENT

Per implementare un buon processo APQP è indispensabile l’impegno del top
management, il quale ha il compito di assicurarsi che:

    •   Tutti gli attori coinvolti predispongano di una formazione adeguata
    •   Le risorse siano correttamente allocate
    •   Il programma venga rispettato

Il supporto del management guida l’organizzazione al raggiungimento degli obiettivi
nel rispetto di: tempi, budget e livello qualitativo.



TEAM CROSS FUNZIONALE

La costituzione di un team cross-funzionale funge da mezzo di comunicazione tra le
diverse funzioni organizzative ed incentiva la predisposizione ad impegnarsi per un
obiettivo comune, consentendo un più rapido sviluppo del prodotto.



PIANIFICAZIONE DI PROGETTO EFFICACE

Compresi i bisogni del cliente è importante sviluppare un project plan efficace a cui fare
riferimento. Bisogna programmare le attività, assegnare le responsabilità ed effettuare
un monitoraggio continuo al fine di completare in tempo il progetto.




                                                                                          47
4.3.2. LE FASI DELL’ APQP


Come accennato precedentemente, l’APQP è composto da 5 fasi interconnesse che
coprono l’intero ciclo di vita del prodotto, dalla sua concezione ai servizi post consegna.

La parola “fase” non deve essere interpretata come un susseguirsi di attività che iniziano
e finiscono seguendo una sequenza temporale predefinita, bensì come identificativo di
una determinata parte del processo APQP, in quanto attività appartenenti a fasi diverse
hanno la necessità di essere sviluppate in concomitanza, scambiando informazioni e
cercando di essere quanto più integrate possibili.

Durante lo sviluppo dell’APQP vengono generate una serie di attività che forniranno
deliverables ed outputs, guidando l’organizzazione al raggiungimento delle milestones e
dell’obiettivo finale.

Prima di spiegare come sono strutturate le varie fasi del processo APQP, è opportuno
specificare le differenze tra deliverables, outputs e milestones.

Deliverable: Prodotto o servizio tangibile, misurabile e specifico che viene fornito al
cliente. Il cliente può essere sia esterno che interno all’organizzazione. I deliverables
rientrano nel campo di applicazione del progetto ed hanno un ruolo preciso nel
realizzare l’obiettivo del progetto. Un deliverable può essere sia massiccio come ad
esempio un palazzo, sia piccolo come un documento di una pagina.

Output: Risultato derivante da una serie di attività svolte. Rappresenta per lo più un
elemento immateriale.

Milestones: Rappresentano dei punti di controllo e servono per tenere traccia
dell’avanzamento del progetto. Esse contrassegnano il completamento di un’attività
importante e sono pensate per il team interno di progetto.




                                                                                            48
                                 Figura 4.2. Fasi del processo APQP (fonte: IAQG).

FASE 1: Pianificazione

La fase della pianificazione è quella più importante, poiché ha delle ripercussioni
sull’intero processo APQP, dunque è opportuno attribuirle il giusto peso onde evitare
spiacevoli inconvenienti futuri.

Il processo inizia con lo studio del mercato di riferimento e l’analisi delle esperienze
pregresse. L’aspetto più importante consiste nel comprendere in maniera esaustiva la
“voce del cliente” (VoC), accertandosi che i suoi bisogni siano chiaramente identificati,
riconosciuti e colti dall’organizzazione. Successivamente, raccolte tutte le informazioni
relative alle caratteristiche tecniche, agli input associati al prodotto e ai requisiti
richiesti, è necessario sviluppare un project plan a cui faranno riferimento tutti gli
stakeholder per assicurare un corretto coordinamento.

DELIVERABLES:

     •   Requisiti di progettazione del prodotto
     •   Target di progetto (sicurezza, qualità, affidabilità, manutenibilità, durata, costo)
     •   Elenco preliminare dei Critical Items (CI’s) e delle Key Characteristics (KC’s)
     •   Distinta base preliminare (BOM)25
     •   Diagramma di flusso preliminare del processo
     •   Review dello Statement of Work (SoW)26
     •   Piano preliminare di approvvigionamento
     •   Project plan


25
  Documento contenente tutti gli item che concorrono alla realizzazione del prodotto.
26
  Documento in cui viene esposto il progetto, le attività ad esso connesse, i risultati attesi e i tempi di
consegna stabiliti.
                                                                                                              49
OUTPUT:

    •   Viene finalizzato il concetto del prodotto ed è disponibile una pre-progettazione



FASE 2: Progettazione e sviluppo del prodotto

Durante la fase 2, le caratteristiche e le specifiche individuate nella fase di
pianificazione assumono una forma più robusta e vengono assimilate in una
progettazione del prodotto controllata, verificata e validata. Molto spesso, è opportuno
sviluppare un ambiente di test attraverso cui poter individuare le fasi produttive previste
ed i potenziali fornitori per realizzare il prodotto nel rispetto dei requisiti. Inoltre,
bisogna identificare gli input della progettazione del processo produttivo che includono:

    •    Documentazione del prodotto progettato
    •    Target di produttività, capacità del processo, qualità e costi
    •    Requisiti del cliente e dell’ente governativo, compreso il tasso di domanda
         richiesto dal cliente

Infine, viene condotto uno studio di fattibilità per garantire che la produzione sia
supportata da un corretto piano di approvvigionamento.

DERIVERABLES:

I risultati attesi di questa fase sono:

    •   Identificazione di requisiti speciali, oltre alla lista delle KC’s e CI’s del prodotto
    •   Analisi preliminare dei rischi inerenti al piano di approvvigionamento
    •   Fornire le specifiche di imballaggio
    •   Rapporto di revisione del progetto
    •   Piano di sviluppo del prodotto
    •   Piani di verifica e validazione del progetto e risultati associati
    •   Rilascio dello studio di fattibilità

OUTPUT:

    •   Rilascio dei documenti di progettazione e BOM
    •   Completamento del piano di verifica e validazione del progetto



                                                                                            50
   •   Completamento dei test specifici di prototipazione, come simulazioni e test
       funzionali
   •   Iniziazione dell’analisi dei rischi del piano di approvvigionamento

ELEMENTI PPAP APPLICABILI – FASE 2

Durante la fase di progettazione e sviluppo del prodotto prendono forma i seguenti
elementi del PPAP, descritti nello specifico nel paragrafo precedente §4.2.:

   •   Documenti di progettazione
   •   Analisi dei rischi di progettazione e relativa DFMEA



Fase 3: Progettazione e sviluppo del processo

La fase 3 dell’APQP è incentrata sullo sviluppo di un consistente processo produttivo
che garantisca il soddisfacimento dei bisogni e delle aspettative del cliente.

Per la progettazione completa del sistema di produzione è importante interagire con la
fase precedente. In particolare, risulta necessario assumere come input le informazioni
generate dalla fase 2 e processarle in maniera adeguata.

Sviluppato il processo, avendo tenuto conto di:

   •   Requisiti da soddisfare
   •   Key Characteristics (KC’s) di processo
   •   Rischi associati al processo ed incorporati nella PFMEA
   •   Piano di gestione dei rischi relativi alla catena di fornitura

viene stilata la relativa documentazione, con annesse istruzioni operative e valutato lo
stato di preparazione alla produzione.

DELIVERABLES:

Le attività svolte nella terza fase producono i seguenti risultati:

   •   Layout di stabilimento
   •   Piano di preparazione alla produzione
   •   Piano di formazione ed indottrinamento delle risorse
   •   KCs del processo
   •   Valutazione preliminare della capacità produttiva
                                                                                           51
    •   Documentazione delle stazioni di lavoro
    •   Piano preliminare MSA
    •   Piano di gestione dei rischi relativi alla catena di fornitura
    •   Risultati delle revisioni effettuate sulla prontezza del processo alla produzione

OUTPUT:

    •   Viene definito e verificato il processo, pronto per essere validato
    •   Completamento di attività per rendere il processo pronto alla produzione

ELEMENTI PPAP APPLICABILI – FASE 3

Durante la terza fase vengono generati i seguenti punti del PPAP:

    •   Diagramma di flusso del processo
    •   Process Failure Mode & Effect Analysis (PFMEA)
    •   Piano di controllo
    •   Approvazione imballaggio, conservazione ed identificazione



Fase 4: Validazione del prodotto e del processo

Dopo aver sviluppato il processo inerente al prodotto, è necessario validare il suo
corretto funzionamento. Lo strumento attraverso cui è possibile effettuare tutte le
opportune verifiche è rappresentato dal primo avvio significativo della produzione
(definito come production run).

Durante la prima production run, viene determinato se sono stati rispettati: il piano di
controllo, il diagramma di flusso del processo e la conformità dei pezzi prodotti. La
minima quantità di pezzi da produrre durante questo avvio di produzione viene definita
dal cliente, tuttavia non è esclusa la possibilità di eccedere la quantità stabilita per
effettuare valutazioni più approfondite richieste dal team qualità dell’organizzazione.

DERIVERABLES:

Gli elementi risultanti dalla quarta fase sono:

    •   Prodotto derivante dalla production run
    •   Verifica della capacità produttiva
    •   Risultati relativi al processo di validazione del prodotto
                                                                                            52
OUTPUT:

    •   Validazione del processo produttivo, il quale è in grado di fornire prodotti
        conformi ai requisiti
    •   Completamento e approvazione del FAI
    •   Completamento e approvazione del PPAP

ELEMENTI DEL PPAP APPLICABILI – FASE 4

Con la fase 4 si ha il completamento del pacchetto PPAP, che successivamente verrà
inviato al cliente per permettergli di effettuare le verifiche che ritiene opportuno.
I punti sviluppati in questa fase:

    •   Measurament System Analysis (MSA)
    •   Studi iniziali della capacità del processo (grazie ai dati registrati durante la
        production run)
    •   Piano di controllo
    •   First Article Inspection Report (FAIR)
    •   Requisiti specifici del cliente
    •   PPAP approval form



Fase 5: Produzione di serie, Utilizzo e Servizio post-consegna

Il processo APQP non termina con la validazione del processo produttivo e
l’approvazione da parte del cliente. La metodologia ha come obiettivo generale il
miglioramento continuo della qualità, per cui l’organizzazione è impegnata nel
perseguire questo scopo anche una volta partita la produzione di serie.

Durante la quinta fase, infatti, assume fondamentale importanza l’attività di
monitoraggio sia del processo sia del prodotto fornito, confrontando i risultati ottenuti
con quelli target, definiti in fase di pianificazione. L’attenzione si riversa sulle
caratteristiche di affidabilità e qualità che concorrono alla soddisfazione del cliente,
sulla performance del servizio post-consegna, e sulle operazioni di manutenzione,
riparazione e revisione (MRO).
Inoltre, per incentivare il miglioramento continuo vengono utilizzati strumenti statistici,
come ad esempio le carte di controllo, per cercare di ridurre la variabilità del prodotto e
del processo.
                                                                                            53
L’esperienza acquisita nello sviluppo di un prodotto tramite l’APQP può essere utile in
altre attività di progettazione, seppur integrando in maniera appropriata il processo.

In conclusione, è opportuno specificare che tutti i documenti contenenti informazioni
modificabili devono essere continuamente aggiornati. Rientrano in questa tipologia di
documenti soprattutto la DFMEA, PFMEA e i piani di controllo.




                                                                                         54
4.3.3. ASPETTI SALIENTI E RIFLESSIONI SU APQP-PPAP


L’impiego di risorse dedicate e l’elevato impegno richiesto per lo sviluppo di un buon
APQP potrebbe essere inteso come un fattore di costo aggiuntivo e scoraggiare le
organizzazioni all’adozione del metodo. Tuttavia, l’esperienza insegna che vi è
un’effettiva riduzione di costo che scaturisce da un minor numero di ispezioni da
effettuare ed una ridotta probabilità di fallimento dovuta non solo a fattori interni ma
anche esterni l’organizzazione.


                       EFFETTO DELLA PREVENZIONE SUI COSTI
         100%
          90%
          80%
          70%
          60%
          50%
          40%
          30%
          20%
          10%
           0%
                                 PRIMA                                         DOPO

                    Prevenzione        Ispezioni      Fallimenti interni     Fallimenti esterni


            Figura 4.3. Effetto della prevenzione sui fattori di costo (fonte: ASQ, Quality Progress).




Dal grafico è possibile osservare che l’aumento di costo generato da una maggiore
attività di prevenzione ha un’influenza positiva sulla riduzione degli altri fattori di
costo.



Facendo riferimento all’intero ciclo di vita del prodotto, possiamo avere un’idea di
come varia l’andamento dei costi della qualità (CoQ) nel caso di sviluppo di un prodotto
con e senza APQP-PPAP.

Il confronto dei due casi è rappresentato nella seguente figura:




                                                                                                         55
 Figura 4.4 Confronto del CoQ nello sviluppo di un prodotto con e senza APQP-PPAP (fonte: ASQ, Quality Progress).




Se vengono comprese subito le aspettative del cliente e viene sviluppato un piano
dettagliato per soddisfare i requisiti individuati, è possibile gestire in maniera opportuna
e proattiva i potenziali rischi associati. Questo comporta una spesa maggiore durante la
fase di sviluppo, che viene compensata durante la fase di produzione. Dunque,
applicando la metodologia APQP si ha un più rapido raggiungimento della maturità del
prodotto, evitando modifiche tardive che risultano sempre più incisive sui costi con
l’avanzare del tempo.




                                                                                                               56
CAPITOLO 5: L’APQP IN UMBRAGROUP

5.1. CASO UMBRAGROUP S.p.A. “AS IS”

Nel seguente capitolo viene analizzata l’implementazione del processo APQP nel
sistema di gestione della qualità di UmbraGroup S.p.A.

Il primo programma in cui viene richiesto un modello di sviluppo di prodotto secondo la
metodologia APQP è stato commissionato dalla compagnia Airbus.

L’azienda ha colto al volo questa sfida, tramutandola in opportunità. Trovarsi nella
condizione di riprogettare e riprogrammare i propri processi cercando di attenersi a
quanto richiesto dallo standard AS/EN 9145, nel contesto di un settore ancora molto
lontano dall’applicazione sistematica della metodologia, pone le basi per essere sempre
più competitiva e all’avanguardia.

Lo svolgimento del lavoro è stato effettuato coinvolgendo le varie funzioni aziendali tra
cui: Design Engineering, Manufacturing Engineering, Quality, Procurement,
Operations.




                                                                                       57
5.1.1. MODALITÀ DI SVOLGIMENTO


Per analizzare il grado di maturità ed esperienza raggiunto dall’azienda
nell’implementazione del processo APQP, sono state condotte delle interviste rivolte ai
principali attori coinvolti. Durante i colloqui sono stati considerati dei documenti stilati
dall’ IAQG e confrontati con la procedura sviluppata internamente dall’organizzazione,
in modo tale da valutare l’adeguatezza della procedura interna allo standard AS/EN
9145.

I documenti del gruppo IAQG presi in considerazione per svolgere questa attività sono:

   1. Checklist delle 5 fasi APQP
   2. Assessment Matrix

Come accennato nell’introduzione di questo capitolo, l’attività di assessment viene
condotta sul programma Airbus. Tuttavia, è importante sottolineare che tale programma
ha preso il via circa tre anni fa e inizialmente la normativa non era ancora entrata in
vigore (in Europa infatti la EN9145 è stata rilasciata nel 2018). Il cliente ha quindi
modellato i termini contrattuali e le attività da svolgere secondo le proprie esigenze,
prendendo spunto dall’APQP utilizzato nel settore automotive. Con l’avanzamento del
progetto e la formalizzazione dello standard, sono stati successivamente aggiornati i
termini tra cui il riferimento esplicito alla AS/EN9145, seppure in parte.

In queste circostanze, la UmbraGroup ha iniziato a sviluppare delle procedure per
allineare i propri processi con quanto richiesto dalla normativa. Quanto sviluppato fin’
ora non è ancora in versione definitiva, necessita di revisioni e alcune modifiche. Lo
scopo della presente attività, dunque, è anche quello di dare un’evidenza concreta di ciò
che è stato svolto ed implementato sul programma Airbus, circoscrivendo i punti su cui
non si ha piena consapevolezza e per i quali le competenze attuali non risultano essere
adeguate. Questo approccio fungerà da guida nella determinazione ed attuazione delle
modifiche da apportare, in modo tale da avere un processo più robusto da poter
implementare nella sua totalità su un programma futuro, in cui il cliente ha imposto
come requisito contrattuale l’applicazione completa dell’APQP secondo la AS/EN9145.

I primi colloqui effettuati sono serviti perlopiù a trasferire in maniera chiara i concetti
dell’APQP a tutto il team che concorre al processo di sviluppo del prodotto, nonché ad
illustrare la procedura interna sviluppata a livello teorico. In questo modo, è stato

                                                                                              58
possibile condurre l’assessment utilizzando un linguaggio comune e procedere in
maniera sincrona.



5.1.2. INCONVENIENTI CORONAVIRUS


Dopo i primi incontri effettuati in azienda, in cui è stato esposto il progetto e sono state
programmate le attività da svolgere, si è presentata l’emergenza da coronavirus.
In questa particolare circostanza l’azienda ha attivato tutte le procedure necessarie per
una corretta gestione dell’imprevisto, cercando di mitigare il più possibile l’impatto
sulla produzione e sulla sicurezza dei propri dipendenti. Tutte le attività non
direttamente coinvolte nella realizzazione dei prodotti sono state affidate in smart-
working e coordinate tramite Microsoft Teams27, mentre gli addetti alla produzione
sono stati attrezzati con adeguati dispositivi di protezione individuali e formati in
maniera consona alle misure precauzionali da adottare.

Parte dell’attività del presente lavoro di tesi è stata, dunque, eseguita da remoto,
interagendo con i vari stakeholder tramite Microsoft Teams. La particolarità di Teams
consiste nella possibilità di partecipare a delle riunioni virtuali con un numero elevato di
utenti, condividendo schermate e documenti. Inoltre, tramite Teams è possibile
permettere agli utenti in contatto di poter controllare il dispositivo degli altri
partecipanti e il sistema è in grado di sincronizzare in tempo reale le modifiche e gli
aggiornamenti apportati.




27
  Piattaforma di comunicazione e collaborazione unificata per teleconferenze, condivisione di contenuti e
integrazione delle applicazioni.
                                                                                                      59
5.2. CHECKLIST DELLE 5 FASI APQP

L’ingente lavoro svolto dall’IAQG permette di fare un’analisi approfondita delle attività
e deliverables da sviluppare nel processo APQP, guidando l’organizzazione nel
considerare tutti gli aspetti, senza tralasciarne alcuno.

A questo scopo sono stati redatti dei documenti contenenti una Checklist per ognuna
delle 5 fasi dell’APQP.

Le Checklist sono sostanzialmente dei file Excel in cui vengono presi in considerazione
tutti gli aspetti del processo.

Ciascun file fa riferimento ad una delle fasi dell’APQP e presenta tanti fogli di calcolo
quanti sono i deliverables associati a quella determinata fase. Per ogni deliverables
(quindi per ogni foglio di calcolo) compare un elenco di domande riferite a:

    •   Aspetti qualitativi
    •   Disponibilità degli input necessari alla realizzazione del deliverable
    •   Utilizzo di un approccio cross-funzionale nell’esecuzione delle attività
    •   Conformità agli standard, se applicabili o, nel caso non lo siano, se è stata
        seguita la migliore prassi
    •   Controllo del risultato del deliverable

Le domande sono appositamente studiate per far riflettere sulle modalità con cui sono
state condotte e gestite le attività, guidando l’organizzazione all’individuazione degli
aspetti più carenti.



Per ciascuna domanda è possibile dare 4 risposte:

    •   (Y) se quanto espresso nella domanda è possibile confermarlo
    •   (N) se non sono state eseguite le attività richieste
    •   (IP) se l’attività è in corso come programmato
    •   (N/A) se è stato concordato con il cliente la non applicabilità dei concetti
        espressi nella domanda

Oltre a fornire una risposta immediata, viene anche richiesto di indicare lo “stato” di
ciascuna domanda tramite l’indicatore RYG (Red, Yellow, Green).

                                                                                           60
Alle risposte negative (N) è possibile associare due stati (Red, Yellow), in base alla
presenza o meno di un piano d’azione in grado di mitigare l’impatto su tempistica e
qualità. Nel caso non sia possibile implementare un piano d’azione efficace, molto
probabilmente vi sarà un impatto sui tempi e la domanda sarà contrassegnata con “Red”.
Se invece è previsto un piano d’azione robusto in grado di ripristinare la situazione e
fare in modo che non ci siano ripercussioni sui tempi, allora la domanda sarà
contrassegnata con “Yellow”.

Tutte le risposte positive (Y) vengono contrassegnate con “Green” e seguono il normale
svolgimento del programma.

Nella colonna successiva (“Evidence”) del foglio Excel, adiacente alla colonna
dell’indicatore RYG, bisogna giustificare la risposta alle domande, fornendo
un’evidenza oggettiva come, ad esempio, un riferimento ai documenti disponibili. Per le
risposte negative (N) è importante descrivere il problema ed includere la causa radice da
cui esso scaturisce.

Le restanti colonne del foglio di calcolo fanno riferimento alle attività di Program
Management. In corrispondenza delle domande contrassegnate con “Red” o “Yellow”
bisogna descrivere i provvedimenti da prendere basandosi sulla causa radice individuata
nella colonna precedente (“Evidence”), associare un responsabile, la data di inizio del
provvedimento, la data di fine prevista e lo stato di avanzamento dell’azione intrapresa.

Per una maggiore comprensione di come è strutturata la Checklist, di seguito ne viene
riportato un esempio:




                            Figura 5.1. Checklist fasi APQP (fonte: IAQG)




                                                                                          61
5.3. ASSESSMENT MATRIX

L’assessment matrix è stata utilizzata per avere una visione generale del modo in cui
l’azienda percepisce ed ha internalizzato l’APQP.

Essa prende in considerazione:

    •   La filosofia aziendale relativa ad aspetti organizzativi e manageriali
    •   L’esperienza nella gestione dei progetti e dei rischi ad essi associati
    •   La conoscenza e l’utilizzo adeguato dei tool dell’APQP (come ad esempio:
        FMEA, piani di controllo, diagramma di flusso del processo, analisi del sistema
        di misura, ecc..)
    •   Il grado di conoscenza dell’APQP di terze parti che interagiscono con l’azienda
        e come essa incentiva i propri fornitori ad adeguarsi allo standard

Ad ognuna di queste categorie vengono associati 5 livelli di “maturità”. Il primo livello
corrisponde ad una conoscenza scarsa o addirittura nulla dell’aspetto considerato,
mentre il quinto livello è sinonimo di una comprensione dettagliata e completa. Nella
determinazione del livello di appartenenza, è fondamentale che l’organizzazione
certifichi la conformità a tutto ciò che è specificato in quel determinato livello, fornendo
un’evidenza oggettiva in grado di giustificare tale scelta. Dopo aver completato la
matrice, viene stabilito un punteggio basato sulla media ponderata ottenuta nelle varie
categorie. Il punteggio risultante indica il posizionamento dell’azienda, la sua maturità
in riferimento agli elementi chiave dell’APQP.

L’assessment matrix è utile non solo ad analizzare lo stato attuale, ma anche a
comprendere quale direzione intraprendere per migliorare gli aspetti più carenti.

Di seguito viene riportata a scopo esemplificativo una parte della matrice.




                               Figura 5.2. Assessment Matrix (Fonte: IAQG).

                                                                                          62
5.4. RISULTATI

Una delle principali lacune riscontrate dal team durante i colloqui è riferita all’analisi
del sistema di misura. La documentazione relativa al sistema di misura e ad una sua
completa analisi, come richiesto dalla normativa AS9145, risulta essere incompleta. In
particolare, i prodotti realizzati dall’azienda per il cliente Airbus sono degli attuatori
elettromeccanici. Le caratteristiche degli attuatori vengono verificate attraverso la loro
misurazione su dei banchi prova automatici, i quali sono collaudati e calibrati da una
società terza. Le misure sono molto attendibili in quanto i banchi possiedono una
certificazione che attesta il loro corretto funzionamento, ma non è stato effettuato uno
studio approfondito sulla determinazione della variabilità del sistema di misura e di
quanto questa variabilità incide sulla variabilità totale osservata in uscita dal processo.

Con il team, è stato allora deciso di effettuare una completa analisi del sistema di misura
degli attuatori elettromeccanici, in modo tale da avere un’evidenza oggettiva sulla
determinazione della variabilità e fornire al cliente un’ulteriore conferma della massima
attenzione dell’azienda all’aspetto qualitativo.




                                                                                              63
CAPITOLO 6: ANALISI DEL SISTEMA DI MISURA
(MSA)

6.1. INTRODUZIONE MSA

L’attività di misurazione ricopre un aspetto fondamentale nella valutazione delle
caratteristiche qualitative del prodotto. È attraverso i dati raccolti durante il processo di
misurazione che viene stabilita la conformità del prodotto ai requisiti di progetto.
Inoltre, sulla base di questi dati, è possibile individuare eventuali inefficienze del
processo produttivo e risalire alla fonte che ha generato il problema, in modo tale da
stabilire un adeguato piano d’azione finalizzato ad apportare miglioramenti.

Da questo presupposto, è intuitivo trarre la conclusione che il processo di misurazione
deve essere in grado di fornire dati estremamente affidabili e attendibili, i quali saranno
utilizzati per effettuare analisi più approfondite sul processo di produzione.

Tuttavia, è ampiamente condivisa l’idea che il sistema di misura influenza in qualche
modo la variabilità totale in uscita osservata.

In particolare, la variabilità totale del processo è condizionata dalla somma di due
contributi:

    •      La variabilità effettiva del prodotto, sul quale agiscono diversi fattori
    •      La variabilità risultante dal sistema di misura impiegato




        Figura 6.1. Contributo del sistema di misura alla variabilità totale osservata (fonte: Six Sigma Institute).




L’obiettivo dell’analisi del sistema di misura consiste, dunque, nella valutazione della
bontà e dell’adeguatezza del sistema di misura. I dati raccolti durante questa attività
vengono processati utilizzando un approccio statistico-matematico per la

                                                                                                                       64
determinazione della variabilità del processo di misurazione e stabilire il suo impatto
sulla variabilità totale. Qualora i risultati ottenuti non fossero soddisfacenti, è
fondamentale individuare, circoscrivere e successivamente eliminare le fonti di
eccessiva variabilità poiché fornirebbero dei risultati fuorvianti, che renderebbero
inapplicabili e spesso controproducenti le azioni di miglioramento.

Il sistema di misura è un insieme articolato di elementi che va ben oltre il solo
strumento utilizzato per effettuare la misura.
Esso è composto da:

    •   Strumento di misura
    •   Ambiente in cui esso opera
    •   Operatori che eseguono le misurazioni
    •   Metodi e procedure definite per l’esecuzione della misurazione
    •   Materiale del componente
    •   Supporto hardware e software

L’interazione di tutti questi elementi contribuisce alla determinazione della variabilità
del sistema.




                                                                                            65
6.1.1. TERMINOLOGIA UTILIZZATA NELL’ANALISI DEL SISTEMA DI
MISURA


La capacità del sistema di misura viene valutata analizzando alcune proprietà che
incidono ognuna in maniera differente nella determinazione della variabilità.

Le proprietà28 che vengono prese in considerazione nell’analisi sono:

Ripetibilità: fa riferimento alla variabilità risultante dalla misurazione ripetuta di un
singolo componente, sulla stessa caratteristica in esame, dallo stesso operatore, alle
stesse condizioni. Il concetto di ripetibilità è strettamente legato allo strumento di
misura utilizzato.

Riproducibilità: rappresenta la variabilità dovuta al valore medio registrato dai diversi
operatori che effettuano la misura su un gruppo omogeneo di oggetti, utilizzando il
medesimo sistema di misura, sotto le stesse condizioni. Talvolta, la riproducibilità è
valutata anche rispetto ad una diversa strumentazione, diversi set-up del sistema, diversi
momenti temporali o condizioni di misurazione.

Errore: evidenzia la differenza tra il valore medio rilevato dalle varie misurazioni
effettuate sotto le stesse condizioni, ed il valore target di riferimento, definito “master
value”. Attraverso l’errore, si percepisce la precisione della misura.

Linearità: valuta l’evoluzione dell’errore sull’intero range operativo del sistema di
misura. In altre parole, si cerca di capire se la correlazione tra la risposta dello
strumento e la caratteristica misurata è di tipo lineare. Se, ad esempio, l’errore di misura
rilevato su una determinata caratteristica varia in funzione della dimensione dell’oggetto
misurato, allora il sistema risulta essere non lineare.

Stabilità & Consistenza: definiscono l’impatto del tempo sul sistema. Il tempo riveste
un ruolo importante nell’analisi, poiché molto spesso incide sulle cause di instabilità ed
inconsistenza come ad esempio: il deterioramento della componentistica elettrica e
meccanica, l’affaticamento degli operatori, l’aggiornamento delle procedure, il
cambiamento delle condizioni ambientali. Nello specifico, la stabilità osserva il
mutamento nel tempo della variabilità relativa all’errore, mentre la consistenza può
essere vista come l’evoluzione nel tempo della ripetibilità. Un sistema stabile e


28
 Per informazioni aggiuntive, consultare la normativa ASTM E2782-17, Standard Guide for
Measurement System Analysis (MSA).
                                                                                              66
consistente risulta essere sotto controllo statistico, quindi è possibile prevedere il suo
comportamento entro un determinato lasso di tempo.

Risoluzione: determina il potere discriminatorio del sistema di misura, cioè la sua
capacità di distinguere elementi diversi. Tanto più alta sarà la risoluzione, più il sistema
sarà sensibile a variazioni impercettibili dei componenti misurati. Il grado di risoluzione
del sistema è strettamente legato alla riproducibilità, poiché una risoluzione adeguata
permette di ricavare dati di misurazione affidabili per poter effettuare un corretto studio
di riproducibilità del sistema.




                                                                                             67
6.2. SCOMPOSIZIONE DELLA VARIANZA

Lo scopo ultimo dello studio MSA può essere racchiuso in 3 concetti chiave:

   1. Determinare quanto della variabilità totale è imputabile allo strumento
   2. Isolare le componenti di variabilità del sistema di misura
   3. Valutare l’adeguatezza dello strumento nello svolgere il compito assegnato

I risultati derivanti dalla procedura di misurazione sono affetti da una variabilità che in
parte è dovuta all’effettiva differenza dei componenti prodotti ed in parte è associabile
al sistema di misura impiegato. Dunque, è possibile esprimere le componenti di
variabilità secondo la seguente equazione (Douglas C. Montgomery, 6th Edition):

                   2         2           2
                  𝜎𝑇𝑜𝑡𝑎𝑙𝑒 = 𝜎𝑃𝑟𝑜𝑑𝑜𝑡𝑡𝑜 + 𝜎𝑆𝑖𝑠𝑡𝑒𝑚𝑎 𝑑𝑖 𝑚𝑖𝑠𝑢𝑟𝑎                            (6.1)
      2                                                                2
dove 𝜎𝑇𝑜𝑡𝑎𝑙𝑒 rappresenta la varianza complessiva osservata in uscita, 𝜎𝑃𝑟𝑜𝑑𝑜𝑡𝑡𝑜 è la
                                                           2
quota di varianza totale imputabile al componente, mentre 𝜎𝑆𝑖𝑠𝑡𝑒𝑚𝑎 𝑑𝑖 𝑚𝑖𝑠𝑢𝑟𝑎 si
riferisce alla varianza derivante dal sistema di misura.

In una condizione ipotetica, ideale, si vorrebbe una varianza del sistema di misura nulla,
in modo tale che esso non abbia alcuna influenza nella determinazione della variabilità
dei prodotti provenienti dal processo produttivo. Tuttavia, è una situazione alquanto
irreale. Vi sarà sempre una componente di variabilità, seppur piccola, associata al
sistema di misura, per cui è importante assicurare un’adeguata capacità del sistema al
fine di limitare il più possibile il suo impatto nella determinazione della variabilità totale
osservata.




                                                                                           68
6.3. STUDIO GAGE R&R

La validazione del sistema di misura viene effettuato utilizzando degli strumenti di
analisi statistica. Uno degli strumenti più utilizzati è lo studio Gage R&R.

Lo studio Gage R&R consiste in un esperimento programmato utile a determinare la
precisione del sistema di misura attraverso l’analisi di due proprietà, ovvero la
Ripetibilità e la Riproducibilità. In questo modo viene considerata, rispettivamente, la
variabilità prettamente imputabile allo strumento (Ripetibilità) e quella derivante
dall’interazione di altri fattori come, ad esempio, l’esecuzione della misura da parte di
diversi operatori o stazioni di misura (Riproducibilità).

La variabilità totale osservata può essere, quindi, ulteriormente scomposta come segue
(Douglas C. Montgomery, 6th Edition):

       2         2           2               2
      𝜎𝑇𝑜𝑡𝑎𝑙𝑒 = 𝜎𝑃𝑟𝑜𝑑𝑜𝑡𝑡𝑜 + 𝜎𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à + 𝜎𝑅𝑖𝑝𝑟𝑜𝑑𝑢𝑐𝑖𝑏𝑖𝑙𝑖𝑡à                          (6.2)

Una rappresentazione grafica della scomposizione della variabilità totale osservata in
uscita è illustrata dalla seguente figura.




                            Figura 6.2. Scomposizione della varianza totale.




                                                                                            69
6.3.1. PROGRAMMAZIONE DELL’ESPERIMENTO


Nella maggior parte delle analisi dei sistemi di misura, l’incremento della variabilità
totale osservata in uscita è imputabile all’operatore che esegue la misurazione, oltre a
quella intrinseca al sistema di misura impiegato.

Tuttavia, come vedremo nel paragrafo §6.4. , relativo all’applicazione sperimentale del
metodo, in cui l’analisi viene condotta su banchi ATE (Automatic Test Equipment), ci
sono casi in cui l’incidenza dell’operatore è pressoché irrilevante e, in queste
circostanze, la riproducibilità viene analizzata considerando altri fattori.

Nel presente capitolo, a scopo illustrativo e teorico, è stato considerato l’operatore come
causa di variabilità aggiuntiva, ma le stesse considerazioni possono essere fatte per altre
cause.

Essendo un esperimento programmato, è buona prassi seguire alcune indicazioni per
una corretta pianificazione dello studio Gage R&R. A tal proposito è stata presa come
riferimento la normativa ASTM E 278229.

Il primo passo da effettuare prima di eseguire le misurazioni consiste nel determinare la
dimensione dell’esperimento come segue:

       •   Decidere il numero di oggetti da misurare (n), selezionati in maniera casuale
           dalla popolazione di oggetti a cui appartengono
       •   Individuare il numero di operatori (p) che dovranno effettuare le misure,
           selezionati anch’essi in modo casuale dalla popolazione degli addetti alle
           misurazioni. Nel caso il numero di operatori sia esiguo (2 o al massimo 3
           operatori) allora è opportuno sceglierli tutti, in modo tale da rappresentare
           l’intera popolazione
       •   Scegliere il numero di misurazioni che ogni operatore deve effettuare su ogni
           oggetto di studio (m)

La dimensione dell’esperimento sarà data dal prodotto dei 3 parametri (n × p × m).

Durante l’esecuzione delle misure, per evitare distorsione dei dati, è necessario che
ciascun operatore esegua la misurazione senza conoscere i risultati ottenuti dagli altri


29
     ASTM E2782-17, Standard Guide for Measurement System Analysis (MSA).

                                                                                           70
operatori, per non esserne condizionato. Inoltre, durante tutta la durata dell’esperimento
bisogna preservare le condizioni del sistema di misura, evitando ricalibrazioni,
cambiamenti nel settaggio, revisioni delle procedure, o modifiche software e hardware.




                                                                                        71
6.3.2. MODELLO ANOVA (Analysis Of Variance)


Dopo aver determinato la dimensione dell’esperimento e aver eseguito le misurazioni è
necessario analizzare i dati raccolti. Il metodo statistico utilizzato per valutare la
Ripetibilità e la Riproducibilità del sistema di misura è il Two Ways ANOVA.

Questo metodo statistico permette di considerare più fattori di variabilità e, oltre a
valutare gli effetti dei singoli fattori nella determinazione della variabilità totale, viene
analizzata anche l’incidenza dell’interazione tra essi.

Nel caso in esame, i fattori di interesse sono rappresentati da: “componente” e
“operatore”.

Di seguito viene riportato il modello descrittivo dell’analisi (Douglas C. Montgomery,
6th Edition):

 𝒚𝒊𝒋𝒌 = 𝝁 + 𝑪𝒐𝒎𝒑𝒐𝒏𝒆𝒏𝒕𝒆𝒊 + 𝑶𝒑𝒆𝒓𝒂𝒕𝒐𝒓𝒆𝒋 + (𝑪𝒐𝒎𝒑𝒐𝒏𝒆𝒏𝒕𝒆 × 𝑶𝒑𝒆𝒓𝒂𝒕𝒐𝒓𝒆)𝒊𝒋 + 𝜺𝒊𝒋𝒌
                                 (𝟔. 𝟑)

Con:

𝑖 = 1,2, … , 𝑛           indice relativo al componente misurato
𝑗 = 1,2, … , 𝑝           indice relativo all’operatore che sta eseguendo la misura
𝑘 = 1,2, … , 𝑚           indice relativo alla misurazione effettuata sul componente

ASSUNZIONI DEL MODELLO:

    •   Le variabili sono indipendenti ed identicamente distribuite (casualità e
        indipendenza);
    •   Le varianze delle sottopopolazioni da cui sono tratti i gruppi devono essere
        omogenee (omoschedasticità)
    •   La popolazione da cui sono estratti i campioni deve essere distribuita
        normalmente (normalità)

I parametri del modello sono tutti delle variabili aleatorie indipendenti che
rappresentano rispettivamente l’effetto del componente, dell’operatore, dell’interazione
tra essi, e dell’errore casuale. Si assume che le variabili aleatorie siano distribuite
normalmente con media nulla e varianza rispettivamente:

    •   𝑽(𝑪𝒐𝒎𝒑𝒐𝒏𝒆𝒏𝒕𝒆𝒊 ) = 𝝈𝟐𝑪

                                                                                            72
    •     𝑽(𝑶𝒑𝒆𝒓𝒂𝒕𝒐𝒓𝒆𝒋 ) = 𝝈𝟐𝑶𝒑
    •     𝑽[(𝑪𝒐𝒎𝒑𝒐𝒏𝒆𝒏𝒕𝒆 × 𝑶𝒑𝒆𝒓𝒂𝒕𝒐𝒓𝒆)𝒊𝒋 ] = 𝝈𝟐𝑪×𝑶𝒑

    •     𝑽(𝜺𝒊𝒋𝒌 ) = 𝝈𝟐𝜺

Dunque, la varianza del modello (6.3), relativa ad ogni singola osservazione, risulta
essere:

                             𝑽(𝒚𝒊𝒋𝒌 ) = 𝝈𝟐𝑪 + 𝝈𝟐𝑶𝒑 + 𝝈𝟐𝑪×𝑶𝒑 + 𝝈𝟐𝜺                        (𝟔. 𝟒)

Raggruppando in maniera opportuna gli elementi della (6.4) è possibile distinguere la
variabilità introdotta dal sistema di misura da quella scaturita dalle effettive differenze
dei componenti misurati:

                                  𝝈𝟐𝑪 = Part-to-Part Variation                           (𝟔. 𝟓)

                               𝝈𝟐𝑶𝒑 + 𝝈𝟐𝑪×𝑶𝒑 = 𝝈𝟐𝑹𝒊𝒑𝒓𝒐𝒅𝒖𝒄𝒊𝒃𝒊𝒍𝒊𝒕à                         (𝟔. 𝟔)

                                      𝝈𝟐𝜺 = 𝝈𝟐𝑹𝒊𝒑𝒆𝒕𝒊𝒃𝒊𝒍𝒊𝒕à                               (𝟔. 𝟕)




Per cui:

                           𝝈𝟐𝑺𝒊𝒔𝒕𝒆𝒎𝒂 𝒅𝒊 𝒎𝒊𝒔𝒖𝒓𝒂 = 𝝈𝟐𝑶𝒑 + 𝝈𝟐𝑪×𝑶𝒑 + 𝝈𝟐𝜺                     (𝟔. 𝟖)

Attraverso il metodo ANOVA, è possibile ottenere una stima delle componenti della
varianza totale. A tal proposito, per l’analisi delle varianze a due fattori vengono
calcolate le somme dei quadrati degli scarti dalle medie (o “devianze”) di ogni fattore
coinvolto nell’analisi. Successivamente, bisogna depurare le somme per i relativi gradi
di libertà in modo tale da ottenere le medie quadratiche per la costruzione delle
statistiche F, adoperate per verificare le ipotesi di significatività dell’effetto dei singoli
fattori, nonché della loro interazione.
Infine, dal calcolo del valore atteso delle medie quadratiche, sarà possibile ottenere una
stima delle varianze delle varie componenti dello studio.

Nel modello ANOVA a due fattori con replicazione, la devianza totale può essere
scomposta in 4 componenti:

                           𝑺𝑺𝒕𝒐𝒕𝒂𝒍𝒆 = 𝑺𝑺𝑪 + 𝑺𝑺𝑶𝒑 + 𝑺𝑺𝑪×𝑶𝒑 + 𝑺𝑺𝜺                          (𝟔. 𝟗)



                                                                                             73
Le formule per il calcolo delle somme dei quadrati degli scarti dalle medie (devianze) e
delle medie quadratiche sono presentate di seguito (ASTM E 2782-17):

Con:

𝒏 = Numero degli oggetti selezionati per lo studio;
𝒑 = Numero di operatori coinvolti;
𝒎 = Numero di misurazioni effettuate per ciascun oggetto.

   •   Somma dei quadrati degli scarti totale. Viene considerata ogni singola
       osservazione e valutata rispetto alla media complessiva:

                                        𝑛   𝑝        𝑚
                                                                 2
                           𝑆𝑆𝑡𝑜𝑡𝑎𝑙𝑒 = ∑ ∑ ∑(𝑥𝑖𝑗𝑘 − 𝑥̿… )                              (6.10)
                                        𝑖=1 𝑗=1 𝑘=1


Dove 𝑥̿… rappresenta la media calcolata rispetto a tutte le osservazioni, in tutti i gruppi:

                                             𝑛       𝑝       𝑚
                                       1
                                𝑥̿… =     ∑ ∑ ∑ 𝑥𝑖𝑗𝑘                                  (6.11)
                                      𝑛𝑝𝑚
                                            𝑖=1 𝑗=1 𝑘=1


Il numero di gradi di libertà (GDL) della devianza totale è pari al numero totale di
osservazioni meno uno: 𝐺𝐷𝐿(𝑆𝑆𝑡𝑜𝑡𝑎𝑙𝑒 ) = 𝑛𝑝𝑚 − 1

   •   Somma dei quadrati degli scarti delle medie del fattore “componente” dalla
       media complessiva:
                                             𝑛

                                𝑆𝑆𝐶 = 𝑝𝑚 ∑(𝑥̅𝑖.. − 𝑥̿… )2                             (6.12)
                                            𝑖=1


Dove 𝑥̅𝑖.. rappresenta la media aritmetica delle misurazioni effettate sull’i-esimo
componente:
                                                 𝑝       𝑚
                                            1
                                   𝑥̅𝑖.. =    ∑ ∑ 𝑥𝑖𝑗𝑘                                (6.13)
                                           𝑝𝑚
                                             𝑗=1 𝑘=1


Il numero di gradi di libertà della devianza del fattore “componente” è pari al numero di
componenti considerati (n) meno uno: 𝐺𝐷𝐿(𝑆𝑆𝐶 ) = 𝑛 − 1




                                                                                           74
   •   Somma dei quadrati degli scarti delle medie del fattore “operatore” dalla media
       complessiva:
                                             𝑝
                                                             2
                               𝑆𝑆𝑂𝑝 = 𝑛𝑚 ∑(𝑥̅ .𝑗. − 𝑥̿… )                             (6.14)
                                            𝑖=1


Dove 𝑥̅.𝑗. rappresenta la media aritmetica delle misurazioni effettuate dal j-esimo
operatore:
                                             𝑛       𝑚
                                           1
                                  𝑥̅.𝑗. =    ∑ ∑ 𝑥𝑖𝑗𝑘                                 (6.15)
                                          𝑛𝑚
                                             𝑖=1 𝑘=1


Il numero di gradi di libertà della devianza del fattore “operatore” è pari al numero di
operatori coinvolti (p) meno uno: 𝐺𝐷𝐿(𝑆𝑆𝐶 ) = 𝑝 − 1



   •   Somma dei quadrati degli scarti di ogni singola osservazione dalla sua media “di
       casella”. Fa riferimento alla misura ripetuta dallo stesso operatore sul medesimo
       componente, dunque alla ripetibilità:

                                             𝑛       𝑝   𝑚
                                                                    2
                     𝑆𝑆𝜀 = 𝑆𝑆𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à = ∑ ∑ ∑(𝑥𝑖𝑗𝑘 − 𝑥̅𝑖𝑗. )                      (6.16)
                                            𝑖=1 𝑗=1 𝑘=1


Dove 𝑥̅𝑖𝑗. Rappresenta la media aritmetica delle osservazioni che il j-esimo operatore fa
sull’i-esimo componente:
                                                 𝑚
                                           1
                                    𝑥̅𝑖𝑗. = ∑ 𝑥𝑖𝑗𝑘                                    (6.17)
                                           𝑚
                                                 𝑘=1


Il numero di gradi di libertà della devianza dell’errore è pari al prodotto del numero di
componenti e operatori coinvolti (np) per il numero di ripetizioni della misura sul
singolo componente meno uno (m – 1): 𝐺𝐷𝐿(𝑆𝑆𝜀 ) = 𝑛𝑝(𝑚 − 1)

Per una maggiore comprensione del metodo, di seguito viene riportata la tabella
incrociata dei due fattori “componente” ed “operatore”:




                                                                                            75
                         Tabella 6.1. Tabella incrociata metodo ANOVA.




Come accennato precedentemente nella (6.6), la riproducibilità del sistema di misura
viene valutata considerando sia la variabilità dell’operatore che l’interazione tra
componente e operatore che esegue la misura:
                                2     2       2
                               𝜎𝑂𝑝 + 𝜎𝐶×𝑂𝑝 = 𝜎𝑅𝑖𝑝𝑟𝑜𝑑𝑢𝑐𝑖𝑏𝑖𝑙𝑖𝑡à

Passando alle somme dei quadrati degli scarti dalle medie, possiamo scrivere la
precedente equazione come:

                            𝑺𝑺𝑹𝒊𝒑𝒓𝒐𝒅𝒖𝒄𝒊𝒃𝒊𝒍𝒊𝒕à = 𝑺𝑺𝑶𝒑 + 𝑺𝑺𝑪×𝑶𝒑                         (𝟔. 𝟏𝟖)

Tale quantità rappresenta la variazione risultante dalle misurazioni effettuate dai diversi
operatori sul medesimo componente, utilizzando lo stesso strumento di misura.

Tuttavia, per il calcolo della riproducibilità è possibile notare che abbiamo ancora un
termine ignoto e cioè la devianza dell’interazione tra “componente” e “operatore”
(𝑆𝑆𝐶×𝑂𝑝 ).

Attraverso il metodo ANOVA, in cui le devianze godono della proprietà additiva, è
possibile ricavare l’ultima devianza incognita, relativa all’interazione tra i due fattori, a
partire dai restanti 4 elementi.

Riprendendo la (6.9), è possibile esplicitarla secondo la devianza 𝑆𝑆𝐶×𝑂𝑝 come segue:

                         𝑆𝑆𝑡𝑜𝑡𝑎𝑙𝑒 = 𝑆𝑆𝐶 + 𝑆𝑆𝑂𝑝 + 𝑆𝑆𝐶×𝑂𝑝 + 𝑆𝑆𝜀

da cui:

                         𝑺𝑺𝑪×𝑶𝒑 = 𝑺𝑺𝒕𝒐𝒕𝒂𝒍𝒆 − 𝑺𝑺𝑪 − 𝑺𝑺𝑶𝒑 − 𝑺𝑺𝜺                         (𝟑. 𝟏𝟗)


                                                                                           76
Il numero di gradi di libertà inerenti all’interazione dei due fattori è dato dal prodotto
del numero di operatori coinvolti (p) meno uno, per il numero dei componenti
considerati (n) meno uno: 𝐺𝐷𝐿(𝑆𝑆𝐶×𝑂𝑝 ) = (𝑝 − 1)(𝑛 − 1)

A questo punto, abbiamo tutti gli elementi per il calcolo delle medie quadratiche,
dividendo semplicemente le singole somme dei quadrati degli scarti per i rispettivi
GDL:

              𝑆𝑆𝐶
    •   𝑀𝑆𝐶 = 𝑛−1                                                                         (6.20)
               𝑆𝑆𝑂𝑝
    •   𝑀𝑆𝑂𝑝 = 𝑝−1                                                                         (6.21)

                   𝑆𝑆𝐶×𝑂𝑝
    •   𝑀𝑆𝐶×𝑂𝑝 = (𝑝−1)(𝑛−1)                                                                (6.22)

                                 𝑆𝑆𝜀
    •   𝑀𝑆𝜀 ≡ 𝑀𝑆𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à = 𝑛𝑝(𝑚−1)
                                                                                          (6.23)

L’ANOVA a due fattori permette di testare la significatività dei fattori sulle misure
rilevate tramite la statistica F. Il test può essere effettuato sia rispetto ai singoli fattori,
che all’effetto combinato di entrambi.

I tre test per la verifica delle ipotesi sono spiegati di seguito:

    1. Si verifica l’ipotesi nulla di “nessuna differenza tra le medie del fattore
        ‘componente’ ” contro l’ipotesi alternativa in cui non tutte le medie sono
        uguali.


                              𝐻0 : 𝜇1 = 𝜇2 = ⋯ = 𝜇𝑛
                              𝐻1 : almeno una μ è diversa dalle altre


        La verifica dell’ipotesi viene effettuata tramite la statistica F così costruita:
                                                       𝑀𝑆𝐶
                                     𝐹𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡𝑒 =                                         (6.24)
                                                       𝑀𝑆𝜀
        e confrontata con 𝑭(𝒏−𝟏) ,𝒏𝒑(𝒎−𝟏) , dove i pedici rappresentano appunto i gradi

        di libertà rispettivamente del numeratore e del denominatore della statistica test.
        L’ipotesi nulla viene respinta se il rapporto supera il valore critico alla
        significatività α scelta.



                                                                                                   77
   2. Si verifica l’ipotesi nulla di “nessuna differenza tra le medie del fattore
       ‘operatore’ ” contro l’ipotesi alternativa in cui non tutte le medie sono uguali.


                             𝐻0 : 𝜇1 = 𝜇2 = ⋯ = 𝜇𝑝
                             𝐻1 : almeno una μ è diversa dalle altre


       La verifica dell’ipotesi viene effettuata tramite la statistica F così costruita:
                                                  𝑀𝑆𝑂𝑝
                                   𝐹𝑂𝑝𝑒𝑟𝑎𝑡𝑜𝑟𝑒 =                                        (6.25)
                                                  𝑀𝑆𝜀
       e confrontata con 𝑭(𝒑−𝟏) ,𝒏𝒑(𝒎−𝟏) .

       L’ipotesi nulla viene respinta se il rapporto supera il valore critico alla
       significatività α scelta.



   3. Si verifica l’ipotesi nulla di “nessuna interazione tra i fattori ‘componente’ e
       ‘operatore’ ” ai vari livelli, contro l’ipotesi alternativa in cui vi è interazione in
       almeno un livello.


                 𝐻0 : (𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡𝑒 × 𝑂𝑝𝑒𝑟𝑎𝑡𝑜𝑟𝑒)𝑖𝑗 = 0             ∀ 𝑖, 𝑗
                 𝐻1 : (𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡𝑒 × 𝑂𝑝𝑒𝑟𝑎𝑡𝑜𝑟𝑒)𝑖𝑗 ≠ 0             per almeno un 𝑖𝑗


       La verifica dell’ipotesi viene effettuata tramite la statistica F così costruita:
                                                       𝑀𝑆𝐶×𝑂𝑝
                            𝐹𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡𝑒×𝑂𝑝𝑒𝑟𝑎𝑡𝑜𝑟𝑒 =                                    (6.26)
                                                        𝑀𝑆𝜀
       e confrontata con 𝑭(𝒏−𝟏)(𝒑−𝟏) ,𝒏𝒑(𝒎−𝟏) .

       L’ipotesi nulla viene respinta se il rapporto supera il valore critico alla
       significatività α scelta.

I risultati dell’ANOVA forniscono le basi per la stima delle varianze di ogni singola
componente del modello (6.3). Le stime delle varianze vengono ottenute dal calcolo dei
valori attesi delle medie quadratiche come segue (Douglas C. Montgomery, 6th
Edition):

   •                     2
       𝐸(𝑀𝑆𝐶 ) = 𝜎𝜀2 + 𝑚𝜎𝐶×𝑂𝑝 + 𝑝𝑚𝜎𝐶2                                                 (6.27)

   •                      2
       𝐸(𝑀𝑆𝑂𝑝 ) = 𝜎𝜀2 + 𝑚𝜎𝐶×𝑂𝑝      2
                               + 𝑛𝑚𝜎𝑂𝑝                                                 (6.28)
                                                                                           78
    •                        2
        𝐸(𝑀𝑆𝐶×𝑂𝑝 ) = 𝜎𝜀2 + 𝑚𝜎𝐶×𝑂𝑝                                                   (6.29)
    •   𝐸(𝑀𝑆𝜀 ) = 𝜎𝜀2                                                               (6.30)

Da cui, procedendo per sostituzione, si ha:

    •   𝜎̂𝜀2 = 𝑀𝑆𝜀                                                                  (6.31)
                  𝑀𝑆𝐶×𝑂𝑝 −𝑀𝑆𝜀
    •     2
        𝜎̂𝐶×𝑂𝑝 =                                                                    (6.32)
                        𝑚
                 𝑀𝑆𝑂𝑝 −𝑀𝑆
                            𝐶×𝑂𝑝
    •     2
        𝜎̂𝑂𝑝 =                                                                      (6.33)
                    𝑛𝑚
               𝑀𝑆𝐶−𝑀𝑆𝐶×𝑂𝑝
    •   𝜎̂𝐶2 =                                                                      (6.34)
                   𝑝𝑚

A questo punto, è possibile stimare la percentuale di incidenza dei singoli elementi
rispetto alla varianza totale, che è proprio lo scopo dello studio GAGE R&R.

Di seguito vengono elencate le percentuali di composizione della varianza totale.

    •   % di variazione dovuta allo STRUMENTO:
                                         2
                                       𝜎̂𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à
                                           2
                                                                                    (6.35)
                                         𝜎̂𝑇𝑜𝑡𝑎𝑙𝑒
      2
Con 𝜎̂𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à ≡ 𝜎̂𝜀2

    •   % di variazione dovuta all’OPERATORE
                                        2
                                      𝜎̂𝑅𝑖𝑝𝑟𝑜𝑑𝑢𝑐𝑖𝑏𝑖𝑡à
                                           2
                                                                                    (6.36)
                                         𝜎̂𝑇𝑜𝑡𝑎𝑙𝑒
      2                 2      2
Con 𝜎̂𝑅𝑖𝑝𝑟𝑜𝑑𝑢𝑐𝑖𝑏𝑖𝑡à = 𝜎̂𝑂𝑝 + 𝜎̂𝐶×𝑂𝑝

    •   % di variazione complessiva del SISTEMA DI MISURA (Gage R&R):
                               2                2
                             𝜎̂𝑅𝑖𝑝𝑒𝑡𝑖𝑏𝑖𝑙𝑖𝑡à + 𝜎̂𝑅𝑖𝑝𝑟𝑜𝑑𝑢𝑐𝑖𝑏𝑖𝑡à
                                           2
                                                                                    (6.37)
                                         𝜎̂𝑇𝑜𝑡𝑎𝑙𝑒


    •   % di variazione dovuta al COMPONENTE:
                                            𝜎̂𝐶2
                                           2
                                                                                    (6.38)
                                         𝜎̂𝑇𝑜𝑡𝑎𝑙𝑒



                                                                                        79
Tramite il metodo ANOVA a due vie è stato dunque possibile risalire all’incidenza del
sistema di misura sulla variabilità totale osservata.




                                                                                    80
6.4. CASO STUDIO MSA IN UMBRAGROUP S.p.A

Dopo aver appurato con il team Qualità dell’azienda la necessità di effettuare uno studio
del sistema di misura, poiché richiesto come deliverable dell’APQP relativo al
programma Airbus, è stato costituito un team dedicato per svolgere le inerenti attività.

Le responsabilità del sottoscritto nello studio sono state relative al processamento dei
dati ottenuti dalle misurazioni, all’offrire supporto per le attività di coordinazione del
team, nonché a fornire, insieme agli specialisti, una valutazione del sistema di misura e
all’individuazione di azioni correttive.

Il contesto di questa sezione della tesi è focalizzato sullo studio GAGE R&R eseguito
su dei banchi prova automatici per uno specifico tipo di attuatore elettromeccanico
prodotto dall’azienda.



6.4.1. PROGRAMMAZIONE DEGLI ESPERIMENTI


Lo svolgimento del progetto è stato portato avanti in smart-working a causa
dell’emergenza COVID-19, per cui non mi è stato possibile essere fisicamente presente
in azienda ed eseguire personalmente le misurazioni. In queste circostanze è stato
fondamentale l’utilizzo del software Microsoft Teams il quale ha permesso il corretto
coordinamento degli attori coinvolti.

Il primo passo effettuato è stato quello di creare un’apposita sezione di MS Teams
dedicata esclusivamente al progetto, in cui sono stati caricati i documenti e aggiunti i
membri del team. Nella sezione dedicata, tutti gli utenti che ne fanno parte, hanno la
possibilità di leggere, caricare, modificare ed aggiornare i file.

Il team è composto dal personale dei reparti Qualità e Sala Prove (direttamente a
contatto con i banchi di collaudo), nonché dal responsabile Montaggio & Collaudo degli
attuatori.

Durante il primo colloquio con il team sono stati analizzati i banchi prova su cui
eseguire lo studio. Trattandosi di banchi di collaudo automatici, utilizzati per testare e
raccogliere dati inerenti al corretto funzionamento degli attuatori elettromeccanici, è
stata ampiamente condivisa da tutto il team l’idea che l’impatto dell’operatore è
pressoché inesistente nella rilevazione delle misure. L’attuatore, infatti, viene caricato
                                                                                             81
sul banco, fissato ai supporti dedicati, successivamente vengono collegati i cavi di
alimentazione dell’attuatore e infine il banco esegue automaticamente tutti i test
necessari, sotto la guida del programma del software di test. I risultati del test vengono
visualizzati sul display e l’operatore provvede alla compilazione della documentazione
digitale.

Data la poca rilevanza dell’operatore, l’analisi del sistema di misura ed in particolare lo
studio GAGE R&R è stato condotto prendendo come riferimento i due banchi prova
disponibili. La proprietà della riproducibilità del sistema è stata dunque valutata rispetto
ai due banchi prova piuttosto che rispetto ai diversi operatori che eseguono le
misurazioni.

Dopo aver assodato che lo studio GAGE R&R sarà condotto considerando i seguenti
fattori:

    •      Attuatori elettromeccanici (componenti)
    •      Banchi prova (prendono il posto degli operatori nella procedura standard)

sono state analizzate le caratteristiche degli attuatori elettromeccanici che risultano
essere più critiche. In sostanza è stato esaminato il documento “Acceptance Test
Procedure” (ATP), il quale contiene l’elenco di tutte le misurazioni da effettuare, con le
relative tolleranze, utili alla validazione del prodotto. La scelta è ricaduta sulle
caratteristiche che presentano un range di tolleranza ristretto e per le quali un’eventuale
‘fuori specifica’ potrebbe compromettere seriamente la funzionalità dell’attuatore.

Le caratteristiche di studio selezionate sono:

    1. Lunghezza Pin to Pin – RETRATTO
    2. Lunghezza Pin to Pin – ESTESO
    3. Gioco Antirotazione
    4. Gioco Radiale

I due banchi utilizzati per effettuare i test degli attuatori permettono di simulare le
condizioni applicative reali, dunque, viene rigorosamente effettuata una calibrazione
periodica della strumentazione.

Ciascun banco è suddiviso a sua volta in due sezioni:




                                                                                          82
     •   la prima sezione è stata progettata per la valutazione di caratteristiche relative
         all’attuazione dell’attuatore, come ad esempio: la lunghezza raggiunta dal
         braccio dell’attuatore, il tempo di attuazione, i valori di corrente e tensione, la
         corretta segnalazione di malfunzionamenti dell’attuatore quando esso viene
         sottoposto a condizioni di lavoro improprie, e molto altro.
     •   la seconda sezione è dedicata alla valutazione dei giochi.

Le caratteristiche Pin-To-Pin sia in posizione retratta sia estesa, vengono misurate sulla
prima sezione dei banchi. Per lunghezza Pin-To-Pin si intende la distanza che intercorre
tra i due attacchi estremi dell’attuatore, uno alla base di esso e l’altro in testa al braccio
scorrevole. Per effettuare questo test, il componente viene montato sull’apposito
supporto e fissato in maniera univoca, dunque, non vi è la possibilità che l’operatore
abbia una qualche influenza sul posizionamento del componente. Successivamente,
vengono collegati i cavi di alimentazione dell’attuatore e grazie ad una cella di carico è
possibile settare la forza necessaria per la chiusura dei giochi. Tale forza viene
impostata su 500N rispettivamente in compressione, nel caso della valutazione della
distanza Pin-To-Pin retratto e, in trazione, per valutare la lunghezza tra i due pin in
estensione. La misura viene rilevata tramite un encoder lineare assoluto30 e stampata sul
display.

Le caratteristiche dei giochi, come detto, vengono invece rilevate sulla seconda sezione
dei banchi in cui è presente tutta la strumentazione necessaria per la valutazione sia del
gioco antirotazione che del gioco radiale. Anche in questo caso è presente un apposito
supporto su cui viene fissato il componente. Nel caso del gioco antirotazione, la
strumentazione è composta da un mandrino oscillante che applica una coppia di 12,4
Nm al pin esterno dell’attuatore, prima in senso orario e successivamente in senso
antiorario. La posizione angolare viene rilevata da un encoder rotativo monogiro31
posizionato sul pin dell’attuatore. Il gioco radiale viene invece misurato tramite due
stantuffi posizionati rispettivamente sopra e sotto il pin dell’attuatore, i quali applicano
una forza di circa 20 N prima in un verso e poi in quello opposto. L’entità del gioco,


30
   Trasduttore di posizione lineare opportunamente collegato all’oggetto di cui si vuole conoscere
suddetta informazione. I dati vengono raccolti, sotto forma di impulsi elettrici, durante il moto traslatorio
dell’oggetto e, una volta elaborati, ne determinano la posizione.
31
   Trasduttore di posizione angolare che converte la posizione angolare del proprio albero di rotazione in
impulsi elettrici i quali, appositamente elaborati, forniscono informazioni su posizione, velocità ed
accelerazione angolare.

                                                                                                           83
data dalla differenza tra gli spostamenti ottenuti nelle due direzioni, viene rilevato da un
sensore a contatto con il pin stesso e visualizzato sul display.




La dimensione dell’esperimento è data da:

    •   n=5 (numero di attuatori utilizzati per lo studio);
    •   p=2 (numero di stazioni su cui effettuare le misure ripetute);
    •   m=5 (numero di ripetizioni della misurazione su ogni attutatore);

per un totale di (𝑛𝑝𝑚) = (5 × 2 × 5) = 50 misurazioni per ogni caratteristica
selezionata.

Il numero di attuatori disponibili è esiguo, poiché derivano da una prima fase produttiva
preliminare. Il programma Airbus relativo alla fornitura di attuatori elettromeccanici è
stato sviluppato seguendo il processo APQP e attualmente si è giunti a cavallo tra la
fase 3 e la fase 4 della metodologia, in cui bisogna validare il prodotto e il processo
produttivo. Prima di procedere con la first production run, uno degli aspetti da tenere in
considerazione in questa fase è proprio lo sviluppo di un’analisi del sistema di misura.
Questa attività è di fondamentale importanza per poter effettuare una corretta analisi
della capacità del processo quando si procederà con la prima produzione a regime.
Infatti, grazie ad una corretta analisi del sistema di misura, sarà possibile tenere sotto
controllo la variabilità del prodotto in uscita con dei dati più attendibili ed affidabili.



6.4.2. ESECUZIONE DELL’ESPERIMENTO


Definito il team, le variabili di studio e la dimensione del test, si è deciso di procedere
con l’esperimento. I successivi incontri con il team sono serviti a:

    •   Monitorare le attività
    •   Ricevere aggiornamenti continui sullo stato di avanzamento delle misurazioni
    •   Esporre le eventuali problematiche riscontrate
    •   Essere certi del corretto adempimento delle procedure



                                                                                              84
    •   Avere la conferma da parte degli operatori che le condizioni del sistema di
        misura sono rimaste invariate durante tutto il periodo dell’esperimento

La prima problematica riscontrata è stata la diversa configurazione dei banchi prova.
Essendo uno dei due banchi molto più recente, non era ancora stata effettuata
un’adeguata calibrazione. Si è subito provveduto alla risoluzione del problema mediante
il coinvolgimento di una società terza specializzata nella calibrazione e messa a punto di
banchi prova automatici complessi. Tuttavia, per abbattere i tempi di durata
dell’esperimento, è stato comunque richiesto agli addetti della sala prove di iniziare
l’attività di misurazione sul banco “maturo”, nell’attesa che il secondo banco venisse
configurato.

Per comodità di trattamento dati è stato generato un foglio di calcolo Excel,
appositamente studiato, sul quale gli operatori registrano solo i risultati inerenti alle
caratteristiche in esame. La motivazione di questa scelta risiede nella maggior facilità di
estrarre i risultati per inserirli successivamente nel software MINITAB, utilizzato per il
processamento dati.

MINITAB è un software di analisi statistica molto completo, tramite cui è possibile
effettuare studi complessi di controllo qualità e, nel caso specifico, rientra anche
l’analisi del sistema di misura. L’output che fornisce il software per lo studio GAGE
R&R è quello descritto nel paragrafo §6.3.2., in cui viene dimostrato il metodo
ANOVA. Oltre ai risultati numerici, MINITAB genera automaticamente una serie di
grafici che permettono di avere un’analisi più completa e trarre ulteriori conclusioni.

Gli operatori del reparto sala prove hanno eseguito 5 misurazioni ripetute per ognuno
dei 5 attuatori su entrambi i banchi prova. Essendo una procedura automatica, una volta
avviato il banco prova vengono effettuati tutti i test necessari. Gli operatori hanno
dunque selezionato le misure relative alle caratteristiche individuate per lo studio e
hanno provveduto alla compilazione dell’apposito file Excel.

I report delle misurazioni effettuate sono stati condivisi su Microsoft Teams in modo
tale da poter essere accessibili da tutto il team.




                                                                                            85
6.5. RISULTATI

Come anticipato, il processamento dei dati pervenuti è stato effettuato con MINITAB. Il
primo step per eseguire lo studio GAGE R&R consiste nell’impostazione del workspace
del programma. Vengono selezionati: il numero di componenti da misurare (n=5), il
numero di stazioni di misura (p=2) e il numero di misure ripetute su ogni componente
(m=5). A questo punto, è possibile inserire le misure effettuate nelle apposite caselle,
generate in modo automatico dal software.
Tramite il comando “gage run chart” il software genera l’omonimo grafico, il quale
mostra tutte le osservazioni in funzione del componente e della stazione. Il grafico
permette di fare una rapida valutazione su eventuali differenze nelle misure tra i diversi
attuatori o tra le stazioni di misura utilizzate. Le varie osservazioni sono suddivise in
riquadri che rappresentano i singoli componenti misurati. All’interno di ogni riquadro
sono riportate le 5 misure effettuate dai due banchi prova per quel determinato
componente, contrassegnate da: cerchio nero per la stazione 1 e quadrato rosso per la
stazione 2. La media di tutte le osservazioni è raffigurata dalla linea centrale
tratteggiata.
Dopo una prima analisi generale, è possibile entrare nel dettaglio. Lo studio delle
componenti di variabilità che agiscono sulla variabilità totale osservata è sintetizzato
dalle tre tabelle a doppia entrata che il comando Gage R&R Study (Crossed) di
MINITAB restituisce come output.
Esse sono:

    •   Two-way ANOVA Table With Interaction:
        la tabella espone i risultati relativi alla significatività dei fattori caratterizzanti lo
        studio: “Componente”, “Baco” e la loro interazione. Il procedimento analitico
        dello studio è spiegato nel paragrafo §6.3.
        La tabella presenta sulle righe le varie componenti di variabilità del modello:
        “Componente”, “Banco”, “Componente*Banco”, “Repeatability”, “Total”. Sulle
        colonne è invece indicato:
             o “DF” rappresenta i gradi di libertà di ogni componente di variabilità
             o “SS” fa riferimento alla somma dei quadrati degli scarti dalle medie
             o “MS” sono le medie quadratiche
             o “F” è il valore della statistica F
             o “P” è il p-value
                                                                                                86
    •   Gage R&R per le componenti di variazione:
        in questa tabella sono riportate le stime delle componenti di variazione che
        formano la varianza complessiva (VarComp), ottenute analiticamente
        applicando le relazioni da (6.31) a (6.34). MINITAB suddivide la varianza totale
        nelle diverse cause di variabilità, ed in particolare in:
            o Total Gage R&R, il quale si riferisce allo strumento di misura, che a sua
                  volta viene ulteriormente scomposto in Repeatibility e Reproducibility
            o Part-To-Part, che rappresenta la stima della variabilità tra i componenti
        L’ultima colonna della tabella, contrassegnata con %Contribution, contiene
        inoltre le percentuali di incidenza di ogni fattore come indicato nelle relazioni da
        (6.35) a (6.38).


    •   Gage R&R per le deviazioni standard:
        la tabella restituisce, per ogni componente di variabilità di cui sopra, i seguenti
        output:
            o StdDev (SD): deviazioni standard delle varie componenti
            o Study Var (6*SD): 6 volte il valore delle deviazioni standard utile a
                  coprire il 99,73% del totale delle osservazioni
            o % Study Var (%SV): rapporto percentuale tra la deviazione standard di
                  ogni singolo elemento e la deviazione standard totale
        Il vantaggio nell’utilizzare la deviazione standard è dovuto al fatto che i risultati
        dello studio presentano la stessa unità di misura della caratteristica analizzata,
        permettendo un confronto diretto.

Oltre alle tabelle, MINITAB fornisce anche un supporto grafico dei risultati, tali da
completare l’analisi.
I grafici generati dal software sono (dall’alto verso il basso e da sinistra a destra):

    •   Components of Variation:
        è la rappresentazione grafica della tabella Gage R&R. Il grafico permette di
        confrontare la %Contribution con la %Study Var (%SV) per i quattro elementi:
            o Repeatability: percentuale di variabilità dovuta allo strumento di misura
            o Reproducibility: percentuale di variabilità dovuta alla stazione su cui
                  vengono effettuate le misure


                                                                                              87
        o Gage R&R: rappresenta la somma dei due contributi Repeatability e
            Reproducibility
        o Part-to-Part: percentuale di variabilità dovuta all’effettiva diversità dei
            componenti misurati
    Gli istogrammi offrono un supporto visivo della distribuzione della varianza
    complessiva evidenziata dalle tabelle Gage R&R.


•   R Chart by Banco:
    mostra il grado di ripetibilità del sistema attraverso la valutazione della coerenza
    delle misure effettuate dalla singola stazione sui vari attuatori. Questo grafico è
    proprio la carta di controllo dei Range, i cui punti sono ottenuti come differenza
    tra il valore massimo ed il valore minimo del gruppo di misure effettuate sul
    determinato componente. La carta dei Range è suddivisa in due gruppi, ognuno
    dei quali corrisponde ai valori ottenuti dalle misurazioni sul primo e sul secondo
    banco prova. Per la determinazione dei limiti di controllo viene utilizzata la
    varianza within group e se tutti i punti sono compresi tra i limiti di controllo, il
    sistema di misura può essere considerato ripetibile, dunque le due stazioni non
    presentano problemi nell’effettuare le misure dei componenti.


•   Xbar chart by Banco:
    è la carta di controllo delle medie e mostra le misurazioni in relazione alla media
    complessiva. La carta di controllo delle medie nello studio Gage R&R assume
    un significato diverso rispetto al suo consueto utilizzo. I limiti di controllo della
    carta sono infatti calcolati sulla base della varianza dello strumento di misura, e
    quindi fanno riferimento alla ripetibilità. Ciò significa che la presenza di punti
    fuori controllo implica che il sistema di misura è in grado di discriminare
    correttamente le parti. In altre parole, se almeno il 50% dei punti cade fuori i
    limiti di controllo è possibile affermare che la varianza introdotta dallo
    strumento di misura è inferiore alla variabilità dovuta all’effettiva differenza tra
    le parti misurate.


•   “Caratteristica” by Componente:
    il grafico raccoglie tutte le misurazioni effettuate sui componenti senza
    considerare la distinzione delle misure effettuate su un banco prova piuttosto che
                                                                                           88
       l’altro. Viene valutata la dispersione delle misure rilevate su ogni componente,
       escludendo la stazione che ha effettivamente eseguito la misura. In questo modo
       è possibile fare delle considerazioni sull’influenza delle stazioni di misura, in
       quanto una concentrazione dei dati in prossimità del valor medio implica che le
       due stazioni misurano allo stesso modo.


   •   “Caratteristica” by Banco:
       situazione opposta rispetto al grafico precedente. In questo caso vengono
       considerate le misure effettuate sulle due stazioni, escludendo la distinzione tra i
       componenti misurati. È una rappresentazione del modo in cui misurano le due
       stazioni. Quanto più la linea che unisce i valori medi dei due gruppi di misure è
       approssimabile ad un segmento orizzontale, tanto più le due stazioni misurano in
       ugual modo.


   •   Componente*Banco Interaction:
       in questo grafico viene rappresentata l’interazione tra le stazioni di misura ed i
       componenti misurati. I punti del grafico si riferiscono alle medie delle misure
       ottenute su ogni stazione, per ognuno dei componenti misurati. Le stazioni di
       misura sono rappresentate dalle due linee spezzate e contrassegnate con cerchio
       nero e quadrato rosso rispettivamente per la stazione 1 e la stazione 2. Se le due
       linee che congiungono la media delle misure seguono lo stesso andamento,
       allora le due stazioni misurano allo stesso modo. Viceversa, nel caso in cui le
       due linee si intersecano o divergono, significa che vi è una qualche dipendenza
       tra le misure che una data stazione rileva su un determinato componente.



Di seguito vengono riportati i risultati dell’analisi suddivisi per caratteristica. Vengono
analizzate prima le caratteristiche misurate sulla sezione 1 dei banchi e successivamente
quelle rilevate sulla sezione 2.

La descrizione delle due sezioni dei banchi prova e del loro funzionamento è riportata
nel paragrafo §6.4.1.




                                                                                            89
6.5.1. PIN TO PIN – RETRATTO


Il grafico GAGE RUN CHART permette di effettuare delle considerazioni su eventuali
trend delle misure effettuate dalle stazioni sui diversi componenti. Nel caso in esame è
possibile notare una bassa variazione tra le misure rilevate dalle due stazioni sui singoli




                         Figura 6.3. Gage Run Chart per Pin-To-Pin Retratto.

componenti, che suggerisce una buona ripetibilità. Tuttavia, entrambe le stazioni
tendono a sovrastimare di poco le misure con l’avanzare delle ripetizioni, infatti dal
grafico si evidenzia un leggero trend crescente delle misure rilevate sullo stesso
componente. La variazione “between groups” che mette in relazione le misure effettuate
dalle due stazioni sui medesimi componenti sembra essere poco rilevante, ma è
possibile notare un valore delle misure rilevate dal secondo banco sui componenti 3 e
15 leggermente inferiori rispetto a quelle rilevate sul primo banco, e viceversa
leggermente maggiori sui componenti 1 e 16.




                                                                                         90
Dalla tabella ANOVA with interaction notiamo un valore del P-value relativo al termine
di interazione tra Banco e Componente prossimo a zero, il che lascia intendere che
potrebbe esserci una qualche dipendenza tra la misura rilevata da una determinata
stazione di misura su un dato componente.




                              Tabella 6.1. Tabella ANOVA per Pin-To-Pin retratto.




      Tabella 6.2. Tabella ANOVA (sopra) e Gage R&R della varianza stimata per Pin-To-Pin retratto (sotto).

La tabella GAGE R&R relativa alla varianza complessiva stimata mostra un’incidenza
della variabilità dovuta allo strumento molto bassa, dell’ordine dello 0,93%. Questo
dato è molto confortante in quanto la maggior parte della variabilità risultante
dall’analisi è imputabile all’effettiva differenza dei pezzi misurati, per una quota del
99,07%.

Nella tabella GAGE R&R delle deviazioni standard, il risultato è confermato, anche se
di poco superiore rispetto alla tabella precedente. Infatti, la percentuale della Study Var
riferita al sistema di misura è pari al 9,64%. Il risultato è anche in questo caso ottimo.

La metrica di valutazione per affermare che lo strumento è adatto alla rilevazione delle
misure, come suggerisce l’IAQG, è la seguente:

•      %Contribution della voce Total Gage R&R ≤ 10%

•      %Study Var della voce Total Gage R&R ≤ 30%




                                                                                                              91
Se ciò si verifica, allora non è indispensabile approfondire lo studio in quanto il sistema
di misura si comporta in maniera ottimale.




              Tabella 6.3. Tabella Gage R&R delle deviazioni standard per Pin-To-Pin retratto

Un’informazione utile a completare la valutazione del sistema di misura è il “number of
dinstinct categories” che rappresenta il potere discriminatorio del sistema di misura. In
pratica è una stima di quanti gruppi separati di parti il sistema saprebbe distinguere. Un
buon sistema di misura dovrebbe saper distinguere almeno 5 gruppi separati. Nel caso
in esame tale numero è pari a 14, quindi è possibile concludere che il sistema di misura
ha un buon potere discriminatorio.

Per completezza si riportano anche i risultati forniti dai grafici generati da MINITAB.




                           Figura 6.4. Grafici MINITAB per Pin-To-Pin retratto.



                                                                                                92
Il primo grafico intitolato “Componetns of Variation” evidenzia un contributo della
variabilità part-to-part molto più accentuata rispetto a quella Gage R&R, a conferma di
quanto espresso numericamente nella tabella Gage R&R in riferimento alla
%Contribution e %Study Var.

La carta R presenta tutti i punti all’interno dei limiti, il che è positivo, però si nota una
differenza di variabilità tra le misure effettuate dai due banchi sui componenti
identificati dai serial number 1, 3 e 16. In particolare, le misure dei tre componenti
rilevate sul banco 2 presentano una variabilità maggiore. Tuttavia, essendo tutti i punti
all’interno dei limiti di controllo, si può dedurre che la ripetibilità del sistema di misura
è molto buona.

La carta Xbar ha tutti i punti fuori dai limiti di controllo. È opportuno ricordare che la
carta mette a confronto la reale differenza tra le parti misurate, con la ripetibilità del
sistema. In pratica i limiti di controllo della carta Xbar rappresentano la variabilità dello
strumento di misura calcolata sulla base della carta R. La variabilità tra le parti è
sensibilmente maggiore della variabilità dello strumento, confermato dalla totalità dei
punti al di fuori dei limiti di controllo, dunque, la riproducibilità del sistema di misura
risulta essere affidabile.

Il grafico “Pin-To-Pin RETR. by Componente”, il quale mostra le misure rilevate da
entrambe le stazioni su ogni singolo componente, evidenzia una piccola dispersione dei
punti attorno al valore medio delle misure. Ciò implica che il sistema di misura si
comporta molto bene e possono essere escluse cause di variabilità imputabili alla
stazione di misura.

Il grafico “Pin-To-Pin RETR. by Banco” mette in relazione la totalità delle misure
rilevate dalle due stazioni di misura. Essendo la linea che congiunge le medie delle
misure rilevate sui due banchi parallela all’asse x, e quindi orizzontale, è possibile
affermare che le due stazioni misurano in modo omogeneo.

Il grafico che rappresenta l’interazione tra “Componente” e “Banco” non presenta
significative differenze tra le medie delle misure rilevate dai due banchi su ogni
componente, a patto una leggera discordanza per i componenti identificati con il serial
number 3 e 16. Questa considerazione è visibile anche dal grafico “Pin-To-Pin RETR.
by Componente”, in cui i due serial number presentano una dispersione dei valori


                                                                                                93
attorno alla media leggermente maggiore degli altri. Tuttavia, non è tale da suggerire
ulteriori approfondimenti del caso.

6.5.2. PIN TO PIN – ESTESO


La lunghezza rilevata sulla corsa massima raggiunta dall’attuatore presenta dei valori
che si comportano in maniera più o meno simile a quelli rilevati sull’attuatore
completamente retratto, ma si possono fare delle considerazioni aggiuntive.




                           Figura 6.5. Gage Run Chart per Pin-To-Pin esteso.




Esaminando il GAGE RUN CHART, si nota che le misure rilevate sul banco 2
presentano delle oscillazioni per i componenti 1, 15 e 16. Questa situazione potrebbe
essere dovuta al fatto che le misure sono state rilevate in momenti temporali diversi,
oppure potrebbe essere una caratteristica intrinseca degli elementi selezionati, i quali
durante l’estensione potrebbero aver presentato dei piccoli problemi. Quest’ultima
considerazione è plausibile poiché tutti gli attuatori considerati sono in fase di test.
Un’ultima causa potrebbe essere dovuta al banco prova, anche se sarebbe da escludere




                                                                                           94
poiché sia le misure rilevate sugli altri componenti (3 e 13), sia quelle effettuate per la
caratteristica “Pin-To-Pin retratto”, non presentano tale andamento.




                            Tabella 6.4. Tabella ANOVA per Pin-To-Pin esteso.




La tabella ANOVA suggerisce che anche per questa caratteristica vi è una possibile
interazione tra “Componente” misurato e “Banco”, poiché il P-value è prossimo a zero.
Inoltre, il P-value del fattore “Banco” è di molto superiore alla significatività alpha
scelta di 0.05, dunque possiamo dedurre che non vi è sostanziale differenza tra le medie
delle misure rilevate dai banchi, le quali sono statisticamente simili.




                Tabella 6.5. Tabella Gage R&R della varianza stimata per Pin-To-Pin esteso.

Analizzando la tabella Gage R&R della varianza complessiva, la variazione dovuta allo
strumento di misura risulta essere molto bassa, ed il contributo maggiore di tale
variazione è rappresentato dalla riproducibilità del sistema. La componente di
variabilità dovuta alle effettive differenze tra le parti è del 98,58%, quindi questo dato
presuppone una buona capacità del sistema di misura.




                                                                                              95
              Tabella 6.6. Tabella Gage R&R delle deviazioni standard per Pin-To-Pin esteso.

Passando alla sezione della tabella GAGE R&R relativa alle deviazioni standard, la
%Study Var relativa allo strumento risulta essere dell’11,90%. Anche in questo caso il
risultato è molto al di sotto della soglia limite del 30%, per cui è confermato il corretto
funzionamento del sistema di misura nello svolgere il compito assegnatogli.

Il potere discriminatorio del sistema di misura, per questa caratteristica, risulta essere
ancora molto buona, poiché il sistema è in grado di distinguere 11 gruppi distinti di
parti.

L’output grafico di MINITAB restituisce i seguenti risultati.




                             Figura 6.6. Grafici MINITAB per Pin-To-Pin esteso.




                                                                                               96
Dal grafico “Components of Variation” si può osservare che il contributo maggiore
della variabilità totale è dovuta alle effettive differenze tra i componenti, e la proprietà
del sistema di misura che incide di più nella determinazione della sua variabilità è la
riproducibilità.

La carta R presenta tutti i punti all’interno dei limiti di controllo tranne il punto relativo
al componente 1 misurato dal banco 2, il quale giace proprio sul limite. Questo
comportamento del banco 2 è evidenziato anche dal grafico “Gage Run Chart”
esaminato precedentemente, in cui si era notata una variazione maggiore per i
componenti 1, 15 e 16. D'altronde, si può concludere che la ripetibilità dello strumento
di misura è tutto sommato buona vista l’assenza di punti al di fuori dei limiti di
controllo.

La carta Xbar ha tutti i punti al di fuori dei limiti di controllo, perciò, la variabilità tra le
parti è molto maggiore di quella del sistema di misura, il che auspica una buona
riproducibilità del sistema.

Il grafico “Pin-To-Pin EXT. by Componente” non lascia presagire alcun
comportamento anomalo dei due banchi prova, poiché non vi è elevata dispersione dei
punti attorno al loro valor medio tranne che per il componente 16, le cui misure rilevate
da entrambi i banchi risultano essere leggermente più disperse.

Per quanto riguarda il modo in cui misurano i due banchi, il grafico “Pin-To-Pin EXT.
by Banco” evidenzia una leggera sovrastima della media delle misure rilevate dal banco
2, che molto probabilmente è dovuta ai componenti 1, 15 e 16. Ad ogni modo, il
segmento che congiunge le due medie, è alquanto parallelo all’asse x, dunque, non c’è
motivo di escludere che i due banchi misurano in maniera simile la caratteristica in
esame.

Il grafico dell’interazione tra “Componente” e “Banco” evidenzia lo stesso andamento
delle due linee spezzate che congiungono i valori medi delle misure rilevate dai due
banchi, tranne che un leggero scostamento per il componente 3 ed il componente 16.
Questa situazione è analoga alla caratteristica “Pin-To-Pin retratto”, il che fa presagire
che in realtà vi è una qualche dipendenza tra le misure che la stazione 2 rileva sui
componenti 3 e 16.

Il comportamento della sezione 1 dei banchi, dalle analisi effettuate, non presenta
problemi nel rilevare le misure. La variabilità imputabile al sistema di misura è molto
                                                                                               97
bassa rispetto a quella dovuta alle effettive differenze dei componenti, per cui è
possibile validare il sistema di misura ed utilizzarlo senza problemi per determinare
successivamente la capacità del processo produttivo in relazione alle due caratteristiche
analizzate.

A questo punto si passa alla valutazione della sezione 2 dei banchi prova, sui quali
vengono rilevati i giochi degli attuatori.




                                                                                        98
6.5.3. GIOCO ANTIROTAZIONE


I risultati dell’analisi riferita alla valutazione del gioco antirotazione non sono molto
soddisfacenti.




                          Figura 6.7. Gage Run Chart per Gioco Antirotazione.




Dal grafico “Gage Run Chart” è possibile osservare un comportamento anomalo dei due
banchi nella rilevazione delle misure, infatti sono presenti dei trend alquanto strani. In
particolare, il set di misure rilevate dal banco 1 sul componente 3, presenta un evidente
trend decrescente mentre il banco 2, sul medesimo componente, rileva misure molto
simili tra loro. Per gli altri componenti, invece, sembra esserci un problema nella
rilevazione della prima misura soprattutto per il banco 2, la quale risulta essere sempre
molto diversa rispetto alle restanti 4 misurazioni.




                                                                                             99
                          Tabella 6.7. Tabella ANOVA per Gioco Antirotazione.




Analizzando la tabella ANOVA, i P-value relativi al componente e all’interazione
Componente*Banco risultano essere molto bassi e quindi significativi, mentre il P-value
del fattore banco è molto maggiore di 0,05.




              Tabella 6.8. Tabella Gage R&R della varianza stimata per Gioco Antirotazione.




La tabella GAGE R&R relativa alla scomposizione della varianza totale stimata
restituisce un valore della percentuale di incidenza del sistema di misura molto
superiore alla soglia fissata del 10%. Infatti, la %Contribution della voce “Total Gage
R&R” è del 23,40%, il cui 21,24% è imputato alla riproducibilità.




                                                                                              100
              Tabella 6.9. Tabella Gage R&R delle deviazioni standard per Gioco Antirotazione.

Tale risultato viene ampiamente confermato nella seconda sezione della tabella Gage
R&R, relativa alle percentuali di incidenza delle deviazioni standard. La %Study Var
della voce “Total Gage R&R” è del 48,37%; percentuale molto al di sopra del limite di
accettabilità del 30%. Anche in questo caso, come ovvio che sia, è la riproducibilità ad
avere maggior incidenza (46,08%). Il numero di gruppi distinti di parti che lo strumento
di misura è in grado di distinguere è esiguo, per cui il suo potere discriminatorio non è
accettabile. Questa prima analisi suggerisce che lo strumento di misura adottato non
svolge bene la sua mansione nella rilevazione dei giochi degli attuatori.
A tal proposito, analizzando i grafici generati dal software, si cerca di risalire ad
eventuali cause che hanno portato a risultati insoddisfacenti.




                            Figura 6.8. Grafici MINITAB per Gioco Antirotazione.

                                                                                                 101
I grafici confermano quanto riportato nelle tabelle. Dal grafico “Components of
Variation”, la quota di variabilità totale dovuta allo strumento di misura è molto
rilevante.

La carta R non risulta essere in controllo poiché il componente 3 misurato dal banco 1
presenta un valore del range molto elevato, tale da posizionarlo fuori dai limiti di
controllo. Il comportamento anomalo nella rilevazione delle misure del componente 3
sul banco 1 è stato osservato anche nel grafico “Gage Run Chart”, in cui si nota un
significativo trend decrescente delle misure. Questa situazione impatta sulla ripetibilità
dello strumento.

Nella carta Xbar, nonostante la maggior parte dei punti sia al di fuori dei limiti di
controllo, le due linee spezzate non seguono lo stesso andamento. In particolare, vi sono
3 punti su 5 che differiscono tra loro (1, 15, 16), dunque lo strumento non gode di una
buona riproducibilità delle misure.

Il grafico “Gioco Antirotazione by Componente” evidenzia una maggiore dispersione
delle misure rilevate dai 2 banchi sui componenti 1 e 16, per cui potrebbero esserci dei
problemi relativi a questi 2 elementi specifici del campione. Inoltre, è possibile
osservare i due punti isolati sul componente 3 e 13, che fanno riferimento alla prima
misura rilevata rispettivamente sul banco 1 e sul banco 2, come mostrato dal grafico
“Gage Run Chart”.

Il modo in cui la caratteristica in esame viene misurata dai due banchi non è totalmente
speculare in quanto il segmento che collega le due medie non è perfettamente
orizzontale. Inoltre, è presente un punto isolato sul banco 1 che suggerisce una qualche
difficoltà del banco nel rilevare la misura su qualche componente, probabilmente fa
riferimento al componente contrassegnato dal serial number 1.

Per la valutazione dell’interazione, raffigurata nell’ultimo grafico, si nota che le due
linee spezzate non seguono lo stesso andamento e divergono in corrispondenza dei
componenti 1, 15 e 16. Questa situazione fa presagire che ci sia una qualche dipendenza
tra le misure rilevate da uno specifico banco sui componenti appena citati.

Da quanto analizzato, l’eccessiva incidenza della variabilità dello strumento di misura
lascia intendere che esso non sia propriamente adatto alla corretta determinazione del

                                                                                           102
gioco antirotazione. La scarsa riproducibilità del sistema di misura potrebbe tuttavia
essere dovuta anche ad un fattore intrinseco agli attuatori. In particolare, si è cercato di
circoscrivere le cause di tale variabilità coinvolgendo i tecnici del montaggio attuatori.
Dal brainstorming è emerso che una possibile spiegazione al fatto che le misure rilevate
siano visibilmente differenti tra loro, risiede nel tipo di materiale con cui è stata
realizzata la boccola ellittica antirotazione degli attuatori. Essa è composta di materiale
plastico, per cui ogni attuatore potrebbe essere stato sottoposto a un numero diverso di
cicli di attuazione, il che potrebbe aver inciso in maniera differente sul degradamento
delle singole boccole. Di conseguenza, boccole più o meno usurate, portano ad una
rilevazione del valore gioco più o meno accentuato. Lo studio di questa caratteristica
richiede maggiori approfondimenti per poter validare lo strumento di misura utilizzato.
Una possibile strada da intraprendere consiste nel ripetere l’esperimento dopo aver
fissato un numero univoco di cicli di attuazione per tutti gli attuatori, in modo tale che
essi siano rodati alla stessa maniera. L’alternativa, leggermente più dispendiosa ma che
sembra essere maggiormente condivisa, consiste nella sostituzione dell’attuale boccola
ellittica in plastica con una realizzata in materiale metallico. Anche in questo caso,
tuttavia, converrebbe effettuare un rodaggio comune prima di ripetere l’esperimento.

Per avere una valutazione più completa si procede anche con l’analisi del gioco radiale,
in modo tale da capire come si comporta complessivamente l’intera sezione dei banchi
prova destina alla determinazione dei giochi.




                                                                                          103
6.5.4. GIOCO RADIALE

Quanto emerso dall’analisi del gioco antirotazione si ripropone in maniera più
accentuata per il gioco radiale.




                            Figura 6.9. Gage Run Chart per Gioco Radiale.




Dal “Gage Run Chart” è evidente che i due banchi rilevano misure totalmente differenti
sui singoli componenti. In particolare, le misure effettuate dal banco 1 giacciono tutte al
di sopra della linea media, mentre quelle del banco 2 tutte al di sotto.




                                                                                        104
                             Tabella 6.10. Tabella ANOVA per Gioco Radiale.

Dalla tabella ANOVA risulta che i fattori “Componente”, “Banco”, nonché la loro
interazione, presentano un P-value prossimo a zero, dunque sono tutti statisticamente
significativi. A differenza delle precedenti analisi, in questo caso è presente anche la
significatività del fattore “Banco”, per cui si ha la conferma che le medie delle misure
rilevate dai due banchi sono statisticamente differenti.




                 Tabella 6.11. Tabella Gage R&R della varianza stimata per Gioco Radiale.




                Tabella 6.12. Tabella Gage R&R delle deviazioni standard per Gioco Radiale.




La tabella “Gage R&R” del gioco radiale restituisce un risultato molto allarmante. La
%Contribution della varianza complessiva inerente allo strumento di misura è del
97,12%, mentre %Study Var, sempre relativo alla voce Total Gage R&R risulta essere
                                                                                              105
del 98,55%. In entrambi i casi, la fonte maggiore di variabilità, è associata alla
riproducibilità del sistema. Questi valori sono estremamente elevati, per cui è
necessario approfondire lo studio in quanto lo strumento non è per niente in grado di
svolgere il proprio compito.




                            Figura 6.10. Grafici MINITAB per Gioco Radiale.




La carta R mostra una ripetibilità del banco 1 tale da sembrare più scadente di quella del
banco 2. Da questa considerazione si potrebbe pensare che il banco 2 sia quello più
affidabile e che potrebbe fungere da “golden unit”. Tuttavia, non è da escludere che vi
sia stato un problema nella rilevazione delle misure su entrambi i banchi.

La carta Xbar conferma la pessima riproducibilità del sistema poiché nonostante tutti i
punti della carta giacciano al di fuori dei limiti di controllo, le linee spezzate che
congiungono i punti non sono per niente comparabili tra i due banchi. A causa del modo
diverso di misurare dei due banchi, ampiamente confermato dal grafico “Gioco Radiale
by Banco”, anche la dispersione dei punti attorno al valor medio nel grafico “Gioco
Radiale by Componente” è eccessiva.

Per quanto riguarda l’interazione tra banco e componente, è superfluo cercare di capire
se vi è una qualche dipendenza tra le misure rilevate da uno specifico banco su un

                                                                                         106
determinato componente, poiché è abbastanza visibile una differenza sostanziale nel
modo in cui misurano i due banchi.

La strumentazione impiegata per la valutazione dei giochi presenta delle problematiche
soprattutto per quanto riguarda il gioco radiale. È opportuno ripetere l’esperimento in
quanto ci potrebbe essere stato anche un problema nella trascrizione dei dati, oppure
potrebbe esserci un problema hardware o software su uno dei due banchi, o addirittura
su entrambi. Infine, non è da escludere che anche sulla valutazione del gioco radiale,
come in quello antirotazione, incida la boccola ellittica in materiale plastico. Prima di
dare conclusioni affrettate è utile ripetere l’esperimento dopo aver sostituito la boccola
ellittica in plastica con quella in metallo, ed aver rodato in maniera opportuna gli
attuatori.

In conclusione, non è possibile validare la seconda sezione dei banchi prova nelle
condizioni di funzionamento attuali. Per quanto possa essere influente la composizione
della boccola ellittica degli attuatori, i risultati derivanti dall’analisi del gioco radiale
evidenziano delle misure rilevate dai due banchi troppo discordanti tra loro. È
necessario approfondire lo studio per risalire ad eventuali cause ed agire in maniera
adeguata per cercare di ridurre la variabilità imputabile al sistema di misura.




                                                                                                107
CONCLUSIONI & SVILUPPI FUTURI

L’APQP è un processo articolato che presuppone grande impegno da parte
dell’organizzazione. La sua implementazione può richiedere addirittura anni di lavoro
come nel caso esaminato in azienda, il cui programma ha alle spalle 3 anni di sviluppo.
Nonostante l’elevato impiego di risorse per ottenere dei risultati soddisfacenti, la
metodologia APQP rende lo sviluppo di un nuovo prodotto/processo meno incerto,
evitando cambiamenti tardivi e promuovendo un approccio proattivo nella risoluzione
dei problemi.

I clienti del settore aeronautico, in particolare i produttori di velivoli, stanno diventando
sempre più esigenti nel voler ricevere, dai propri fornitori, prodotti innovativi ad alto
contenuto tecnologico in tempi sempre più ristretti e che non necessitano modifiche
aggiuntive già dal primo lotto di fornitura.

Per questo motivo, dopo la consolidazione nel settore automotive, anche nel settore
aeronautico negli ultimi anni si sta diffondendo la mentalità APQP nel processo di
sviluppo di un nuovo prodotto/processo.

Durante il tirocinio svolto in azienda, è stata riscontrata l’assenza di una piena e
completa consapevolezza della metodologia quindi, il presente lavoro, è servito anche a
divulgare e ad incentivare una mentalità APQP oriented. A questo scopo sono state
coinvolte le varie funzioni aziendali e sono stati condotti dei meeting, sulla base di una
checklist, per rafforzare la comprensione della metodologia ed individuare i punti in cui
il processo presenta delle lacune.
Durante gli incontri è stato preso in considerazione quanto sviluppato internamente
dall’azienda in termini di procedure e la loro corrispondenza alla normativa AS/EN
9145. È stata analizzata la procedura interna “P11”, la quale spiega come dovrebbe
essere implementato il processo APQP in UmbraGroup. Per la valutazione è stato preso
come riferimento il programma Airbus che rappresenta il pioniere dell’implementazione
dell’APQP in azienda. Come accennato nell’introduzione, ci si è voluti focalizzare su
una parte del processo ed in particolare sull’analisi del sistema di misura (MSA), in
quanto contrassegnato come aspetto carente. Suddetta scelta ha anche una valenza
operativa, poiché l’avanzamento del programma Airbus, al tempo di stesura del presente
elaborato di tesi, è giunto a cavallo tra la fase 3 e la fase 4 del processo APQP e l’MSA
è uno dei deliverables da sviluppare in questa parte del processo. Lo studio MSA
                                                                                            108
permette di validare i banchi prova degli attuatori e di procedere con la prima
production run, nonché con la successiva produzione di serie definitiva.

In letteratura non vi è molta chiarezza riguardo le modalità con cui eseguire l’analisi del
sistema di misura su una tipologia di banco prova automatico. L’idea è stata quella di
condurre uno studio Gage R&R utilizzando come fattore di variabilità, per la
determinazione della riproducibilità del sistema, i due banchi prova disponibili in
azienda piuttosto che i diversi operatori che eseguono le misure.

Analizzando la Ripetibilità e la Riproducibilità del sistema di misura è stato possibile
quantificare la variabilità ad esso associata e quanto essa incida sulla variabilità totale
osservata in uscita dal processo.

Nel presente lavoro sono state considerate in totale quattro caratteristiche degli attuatori.
La scelta è ricaduta sulle caratteristiche più critiche e tali per cui una loro analisi
permette di avere una prima valutazione generale dell’intero sistema di misura. Ciò
deriva dal fatto che le rilevazioni dei giochi degli attuatori vengono effettuate su una
sezione differente del banco prova rispetto a quella utilizzata per effettuare tutti gli altri
test.
Lo studio ha prodotto risultati abbastanza soddisfacenti per la determinazione delle
lunghezze Pin-To-Pin dell’attuatore effettuate sulla sezione 1 dei banchi. La
strumentazione gode di una bassa variabilità rispetto a quella derivante dall’effettiva
differenza dei componenti. Il risultato è incoraggiante, tuttavia, per avere un’evidenza
oggettiva e validare il sistema di misura correttamente, è opportuno condurre l’analisi
sulla totalità delle caratteristiche degli attuatori presenti nel documento ATP
(Acceptance Test Procedure).
Per quanto riguarda la sezione 2 dei banchi prova, dedicata alla misurazione dei giochi
degli attuatori, l’analisi ha evidenziato una variabilità eccessiva imputabile allo
strumento di misura. Nelle condizioni di lavoro attuali non è possibile validare la
strumentazione ed è necessario approfondire lo studio per cercare di ridurre
drasticamente la variabilità risultante dall’esperimento. Una delle possibili cause che si
pensa abbia contribuito a fornire questi risultati insoddisfacenti, è attribuibile ad un
componente strutturale degli attuatori. In particolare, il componente che ha la funzione
di contrastare i giochi, è la boccola ellittica. Essa è stata realizzata in materiale plastico
e, in quanto tale, è soggetta a deformazioni più o meno accentuate in base al numero di
attuazioni effettuate dall’attuatore. Non essendo rodati tutti allo stesso modo, ogni
                                                                                            109
attuatore potrebbe aver effettuato cicli diversi di attuazione, dunque, i risultati
dell’analisi potrebbero essere influenzati da questo fattore. Si propone di ripetere
l’esperimento sostituendo il componente in questione con uno in materiale metallico,
tenendo comunque traccia delle attuazioni, in modo tale che ogni componente venga
sottoposto allo stesso rodaggio.

Una critica costruttiva riguarda la gestione della documentazione inerente alle attività
svolte nel processo APQP. Durante gli incontri con i vari responsabili delle diverse
funzioni aziendali, nel compilare la checklist stilata dall’International Aerospace
Quality Group (IAQG), sono state riscontrate delle difficoltà nel reperire la
documentazione utile a fornire l’evidenza oggettiva di quanto sviluppato nelle varie fasi
del processo. Questa problematica ha reso l’attività di assessment poco efficiente, con
incontri che spesso duravano più del dovuto.
La soluzione proposta per efficientare la gestione del processo e della relativa
documentazione consiste nell’adozione di un software che integra tutti gli elementi da
sviluppare nel processo APQP.
Il software consigliato è “VISUAL PPAP”, sviluppato da “IPI Solutions”, il quale
presenta un’interfaccia grafica molto semplice ed intuitiva.
Visual PPAP permette di creare, gestire e monitorare tutti gli elementi del PPAP riferiti
ad ogni singola commessa dell’azienda. La sua versatilità permette di personalizzare
facilmente gli elementi in base alle diverse esigenze dei clienti. Essendo una soluzione
integrata, le varie funzioni aziendali hanno la possibilità di avere una comprensione
globale e completa di quanto sviluppato, agevolando il flusso informativo e
promuovendo la comunicazione cross-funzionale.

Il business aziendale si sta indirizzando sempre più verso la realizzazione di attuatori
elettromeccanici, considerati uno dei “core product” dell’insieme di parti complesse
che compongono i velivoli. Si auspica che il procedimento utilizzato per la validazione
dei banchi prova automatici, esposto nel presente lavoro di tesi, fungerà da base solida
per successive analisi finalizzate a ridurre continuamente la variabilità introdotta dal
sistema di misura, nonché a garantire una soddisfazione del cliente sempre maggiore.




                                                                                           110
Bibliografia

Enzo Belluco (2013), Guida allo Statistical Process Control per Minitab, FrancoAngeli.
Douglas C. Montgomery (2009), Introduction to Statistical Quality Control, 6th Edition,
John Wiley & Sons, Inc.


Normative consultate:
AS/EN 9100:2016, Aerospace Quality Management, SAE International.
AS/EN 9102:2015, First Article Inspection, SAE International.
AS/EN 9145:2016/2018, Advanced Product Quality Planning and Production Part
Approval Process, SAE International.
ASTM E2782-17, Standard Guide for Measurement System Analysis (MSA), American
Society for Testing and Materials.
SAE AS 13003:2015, Measurement System Analysis Requirements for the Aero Engine
Supply Chain, SAI Global.




Sitografia

https://www.sae.org/iaqg/

https://asq.org/

https://www.umbragroup.com/

https://www.airbus.com/aircraft/market/global-market-forecast.html

http://www.gmsl.it/getting-started-with-minitab-17/

https://www.minitab.com/en-us/




                                                                                    111
RINGRAZIAMENTI

Sono tante le persone che hanno contribuito a rendere speciale questo breve ma intenso
percorso di vita e che vorrei ringraziare.

Ringrazio innanzitutto il prof. Maurizio Galetto per avermi proposto di svolgere il
lavoro di tesi presso la UmbraGroup S.p.A., e per essersi dimostrato sempre gentile e
disponibile nel fornirmi le indicazioni necessarie nel momento del bisogno.

Un sentito grazie al mio tutor aziendale, l’Ing. Marco Ceccarelli, per avermi dato la
possibilità di intraprendere un’esperienza formativa in una grande Azienda, trovando
costantemente il modo di seguirmi nello svolgimento del progetto nonostante le
difficoltà riscontrate, dovute all’emergenza COVID-19. Il supporto fornitomi è stato
fondamentale per il compimento del lavoro.

Desidero ringraziare tutti i ragazzi del reparto Dimensionale e l’intero team Qualità, in
particolare Andrea Ceccarelli, Fabrizio D’Andrea e Jacopo Bracco, con i quali ho
trascorso la maggior parte del tempo instaurando, oltre che un buon rapporto
professionale, anche un bel rapporto di amicizia. Sono stato accolto nel migliore dei
modi, ricevendo consigli validi sul lavoro e non solo. Ringrazio per la disponibilità
mostratami, per avermi insegnato con entusiasmo molte cose nuove e per avermi fatto
sentire parte di un team.

Ringrazio anche tutte le stupende persone che ho avuto modo di conoscere in Azienda e
che hanno contribuito ad introdurmi nel mondo lavorativo, trasferendomi le loro
conoscenze e consigliandomi dall’alto della loro esperienza.

Un ringraziamento speciale e inestimabile va alla mia famiglia. Dedico questo traguardo
ai miei genitori che, con il loro supporto, mi hanno dato la forza necessaria per non
arrendermi mai. Sono stati un punto di riferimento cui poter fare affidamento in
qualsiasi momento, soprattutto in quelli più difficili. Sono grato per tutti i sacrifici fatti,
per essermi stati vicini anche se fisicamente lontani, per aver costantemente creduto in
me e per avermi dato la possibilità di frequentare gli studi universitari. Se non fosse per
loro non avrei potuto vivere questa magnifica esperienza formativa. Grazie, vi voglio un
bene immenso.



                                                                                            112
Un grazie di cuore ai coinquilini di Foligno, nonché seconda famiglia, Laura e Valerio.
Insieme abbiamo affrontato una delle esperienze più brutte di questo 2020. Con il loro
calore, l’umanità e la saggezza hanno contribuito a rendere meno traumatico il periodo
di quarantena obbligatoria. Grazie per il sostegno offertomi, per le risate, i consigli di
vita e le mangiate improvvisate, ma soprattutto grazie per aver fatto parte della mia vita.

A questo punto, è giunto il momento di ringraziare gli amici hanno avuto un ruolo
fondamentale durante il percorso di studi al Politecnico.

Parto col ringraziare Graziano per avermi scelto come coinquilino e con cui si è subito
instaurato un bellissimo rapporto di amicizia fraterna. Abbiamo condiviso tanto, gioie e
dolori, divertimento e nottate intere di studio, rendendo indimenticabile il mio primo
anno nella città di Torino. L’apice è stato raggiunto con l’arrivo di Mercurio, che reputo
come un fratello e con cui ho avuto la fortuna di condividere l’appartamento fino
all’ultimo giorno della mia permanenza a Torino. Il trio così composto era un qualcosa
di stupendo. Mi fermo qui altrimenti non mi basterebbe lo spazio.

Ringrazio Michele per la sua sincera amicizia, le suonate al parco del valentino, le risate
a crepa pelle, le serate alternative e le lunghe chiacchierate filosofiche e riflessive.
Grazie per aver influenzato positivamente questo mio periodo di vita.

Un grazie allo “zaparone” Pietro che, con il suo modo di fare stravagante, rallegra le
giornate e rende l’animo più leggero. Grazie per avermi dimostrato che siamo noi a
decidere da quale tipo di emozioni farci condizionare.

Ringrazio il mio amico e fratello acquisito Pasquale che, insieme alla ragazza Teresa,
mi ha sempre ascoltato ed accolto a braccia aperte. Grazie per le giornate passate al
lago, le mangiate rustiche, le serate gradevoli e spensierate. Nonostante parecchi
chilometri ci abbiano diviso per circa una decade, il tempo sembra non aver avuto
alcuna influenza sul nostro rapporto.

A proposito di rapporti che permangono nel tempo e nello spazio, vorrei dedicare un
pensiero ed esprimere la mia gratitudine a tutti gli amici conosciuti durante la laurea
triennale a Salerno e che continuano ad avere un “posto fisso” (Cit. Checco) nel mio
cuore. È bello sapere che, nonostante il trascorrere del tempo e l’aver intrapreso strade
diverse, si trova sempre il modo e l’occasione giusta per rincontrarsi, mantenendo
quello stesso rapporto di amicizia sincera di un tempo. Grazie di cuore a tutti voi,
specialmente a chi mi è stato vicino in quest’ultimo periodo.
                                                                                           113
Un grazie ai colleghi di studio del Politecnico che ho avuto il piacere di conoscere e con
cui ho affrontato nel migliore dei modi progetti ed esami universitari.

Colgo l’occasione per ringraziare anche gli amici del mio paese d’origine con i quali, a
distanza di anni, continua ad esserci un bel rapporto e ci si ritrova costantemente
durante le celebrazioni festive.

Infine, ringrazio gli intramontabili Lucia, Gerry e Monte. I veri amici si vedono nel
momento del bisogno, e voi, in tutti questi anni, ci siete sempre stati. Grazie davvero.



Mi auguro che questo sia solo uno dei tanti traguardi che, con impegno e dedizione,
sacrificio e costanza, la vita futura sarà in grado di regalarmi.




                                                                                        114
