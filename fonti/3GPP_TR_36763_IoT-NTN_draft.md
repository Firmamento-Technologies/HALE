
|3GPP TR 36.763 V0.0.12 (2021-012)                                               |
|Technical Report                                                                |
|3rd Generation Partnership Project;                                             |
|Technical Specification Group Radio Access Network;                             |
|Study on Narrow-Band Internet of Things (NB-IoT) / enhanced Machine Type        |
|Communication (eMTC) support for Non-Terrestrial Networks (NTN) (Release 17)    |
|                                                                                |
|[pic]                                |[pic]                                     |
|                                                                                |
|The present document has been developed within the 3rd Generation Partnership   |
|Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.       |
|The present document has not been subject to any approval process by the 3GPP   |
|Organizational Partners and shall not be implemented.                           |
|This Specification is provided for future development work within 3GPP only. The|
|Organizational Partners accept no liability for any use of this Specification.  |
|Specifications and Reports for implementation of the 3GPP TM system should be   |
|obtained via the 3GPP Organizational Partners' Publications Offices.            |
|                                                                                |

|                                                                                |
|3GPP                                                                            |
|Postal address                                                                  |
|                                                                                |
|3GPP support office address                                                     |
|650 Route des Lucioles - Sophia Antipolis                                       |
|Valbonne - FRANCE                                                               |
|Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16                                  |
|Internet                                                                        |
|http://www.3gpp.org                                                             |
|Copyright Notification                                                          |
|No part may be reproduced except as authorized by written permission.           |
|The copyright and the foregoing restriction extend to reproduction in all media.|
|                                                                                |
|                                                                                |
|© 2019, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). |
|All rights reserved.                                                            |
|                                                                                |
|UMTS is a Trade Mark of ETSI registered for the benefit of its members          |
|3GPP is a Trade Mark of ETSI registered for the benefit of its Members and of   |
|the 3GPP Organizational Partners                                                |
|LTE is a Trade Mark of ETSI registered for the benefit of its Members and of the|
|3GPP Organizational Partners                                                    |
|GSM® and the GSM logo are registered and owned by the GSM Association           |

         Contents


Foreword 4

1  Scope 6

2  References 6

3  Definitions of terms, symbols and abbreviations  6
3.1  Terms  6
3.2  Symbols  8
3.3  Abbreviations  8

4  IoT Non-Terrestrial Networks overview and scenarios  9
4.1  IoT Non-Terrestrial Networks overview 9
4.2  IoT Non-Terrestrial Networks reference scenarios 10

5  IoT-NTN Architecture and Capabilities   10
5.1  IoT-NTN Architecture  10
5.2  IoT-NTN UE Capabilities 11

6  Radio Layer 1 issues and related solutions  11
6.1  IoT NTN Reference Parameters 11
6.2  Link Budget Analysis  13
6.2.1  Link Budget Parameters   13
6.3  Timing Relationships  16
6.4  Time and Frequency Synchronization 17
6.5  HARQ   18

7  Radio Protocol Issues and Solutions  18
7.1  Requirements and key issues  18
7.1.1  Delay  18
7.2  User plane enhancements 19
7.2.1  MAC  19
7.2.2  RLC  21
7.2.3  PDCP 21
7.3  Control plane enhancements 22
7.3.1  Idle mode mobility enhancements  22
7.3.2  Connected mode mobility enhancements  24

8  Recommendations on the way forward 24
8.1  Recommendations from RAN1  24
8.2  Recommendations from RAN2  24

Annex A: Satellite ephemeris 25

B.1  Key Performance Indicators 26

B.2  Performance targets for evaluation purposes 26

Annex C (Informative): Change history 27




         Foreword

This Technical Report has been produced by the 3rd Generation Partnership
Project (3GPP).

The contents of the present document are subject to continuing work within
the TSG and may change following formal TSG approval. Should the TSG modify
the contents of the present document, it will be re-released by the TSG
with an identifying change of release date and an increase in version
number as follows:

  Version x.y.z

  where:

    x  the first digit:

       1  presented to TSG for information;

       2  presented to TSG for approval;

       3  or greater indicates TSG approved document under change control.

    y  the second digit is incremented for all changes of substance, i.e.
       technical enhancements, corrections, updates, etc.

    z  the third digit is incremented when editorial only changes have been
       incorporated in the document.

In the present document, modal verbs have the following meanings:

  shall  indicates a mandatory requirement to do something

  shall not   indicates an interdiction (prohibition) to do something

The constructions "shall" and "shall not" are confined to the context of
normative provisions, and do not appear in Technical Reports.

The constructions "must" and "must not" are not used as substitutes for
"shall" and "shall not". Their use is avoided insofar as possible, and they
are not used in a normative context except in a direct citation from an
external, referenced, non-3GPP document, or so as to maintain continuity of
style when extending or modifying the provisions of such a referenced
document.

  should indicates a recommendation to do something

  should not  indicates a recommendation not to do something

  may  indicates permission to do something

  need not indicates permission not to do something

The construction "may not" is ambiguous and is not used in normative
elements. The unambiguous constructions "might not" or "shall not" are used
instead, depending upon the meaning intended.

  can  indicates that something is possible

  cannot indicates that something is impossible

The constructions "can" and "cannot" are not substitutes for "may" and
"need not".

  will indicates that something is certain or expected to happen as a
             result of action taken by an agency the behaviour of which is
             outside the scope of the present document

  will not indicates that something is certain or expected not to happen as
             a result of action taken by an agency the behaviour of which
             is outside the scope of the present document

  might  indicates a likelihood that something will happen as a result of
             action taken by some agency the behaviour of which is outside
             the scope of the present document

  might not   indicates a likelihood that something will not happen as a
             result of action taken by some agency the behaviour of which
             is outside the scope of the present document

In addition:

  is (or any other verb in the indicative mood) indicates a statement of
             fact

  is not (or any other negative verb in the indicative mood) indicates a
             statement of fact

The constructions "is" and "is not" do not indicate requirements.



         1  Scope

TBA


2  References

The following documents contain provisions, which, through reference in
this text, constitute provisions of the present document.

  -  References are either specific (identified by date of publication,
    edition number, version number, etc.) or non-specific.

  -  For a specific reference, subsequent revisions do not apply.

  -  For a non-specific reference, the latest version applies. In the case
    of a reference to a 3GPP document (including a GSM document), a non-
    specific reference implicitly refers to the latest version of that
    document in the same Release as the present document.

  [1]  3GPP TR 21.905: "Vocabulary for 3GPP Specifications"

  [2]  3GPP TR 38.811 v15.2.0: "Study on New Radio (NR) to support non-
             terrestrial networks (Release 15)"

  [3]  3GPP TRTS 38.821 v16.0.0: " Solutions for NR to support non-
             terrestrial networks (NTN) (Release 16)"

  [4]  3GPP TR 45.820 v13.1.0: "Cellular system support for ultra-low
             complexity and low throughput Internet of Things (CIoT)
             (Release 13)"

  [5]  3GPP TS 22.261: "Service requirements for the 5G system; Stage 1
             (Release 16)"

  [6]  R2-1901404: "IoT Device Density Models for Various Environments",
             Vodafone, RAN2 #105

  [7]  3GPP TS 36.331: "E-UTRA Radio Resource Control (RRC) protocol
             specification (Release 16)"

  [8]  3GPP TS 36.322: "E-UTRA Radio Link Control (RLC) protocol
             specification (Release 16)"

  [9]  3GPP TS 36.323: "E-UTRA Packet Data Convergence Protocol (PDCP)
             specification (Release 16)"

  [10] R2-2011275: "[IoT-NTN] Applicability of TR 38.821 (MediaTek)"

  [11] 3GPP TS 36.304: "Evolved Universal Terrestrial Radio Access (E-
             UTRA); UE Procedures in Idle Mode (Release 16)"

  [12] 3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-
             UTRA); Medium Access Control (MAC) protocol specification
             (Release 16)"








3  Definitions of terms, symbols and abbreviations


3.1  Terms

For the purposes of the present document, the terms and definitions given
in TR 21.905 [1] and the following apply. A term defined in the present
document takes precedence over the definition of the same term, if any, in
TR 21.905 [1].

Availability: % of time during which the RAN is available for the targeted
communication. Unavailable communication for shorter period than [Y] ms
shall not be counted. The RAN may contain several access network components
among which an NTN to achieve multi-connectivity or link aggregation.

Feeder link: Wireless link between NTN Gateway and satellite

Geostationary Earth orbit: Circular orbit at 35,786 km above the Earth's
equator and following the direction of the Earth's rotation. An object in
such an orbit has an orbital period equal to the Earth's rotational period
and thus appears motionless, at a fixed position in the sky, to ground
observers.

Low Earth Orbit: Orbit around the Earth with an altitude between 300 km,
and 1500 km.

Medium Earth Orbit: region of space around the Earth above low Earth orbit
and below geostationary Earth Orbit.

Minimum Elevation angle: minimum angle under which the satellite or UAS
platform can be seen by a terminal.

Mobile Services: a radio-communication service between mobile and land
stations, or between mobile stations

Mobile Satellite Services: A radio-communication service between mobile
earth stations and one or more space stations, or between space stations
used by this service; or between mobile earth stations by means of one or
more space stations

Non-Geostationary Satellites: Satellites (LEO and MEO) orbiting around the
Earth with a period that varies approximately between 1.5 hour and 10
hours. It is necessary to have a constellation of several Non-Geostationary
satellites associated with handover mechanisms to ensure a service
continuity.

Non-terrestrial networks: Networks, or segments of networks, using an
airborne or space-borne vehicle to embark a transmission equipment relay
node or base station.

NTN-gateway: an earth station or gateway is located at the surface of
Earth, and providing sufficient RF power and RF sensitivity for accessing
to the satellite. NTN Gateway is a transport network layer (TNL) node.

On Board processing: digital processing carried out on uplink RF signals
aboard a satellite or an aerial.

On board NTN eNB: eNB implemented in the regenerative payload on board a
satellite.

On ground NTN eNB: eNB of a transparent satellite payload implemented on
ground.

One-way latency: time required to propagate through a telecommunication
system from a terminal to the public data network or from the public data
network to the terminal. This is especially used for voice and video
conference applications.

Regenerative payload: payload that transforms and amplifies an uplink RF
signal before transmitting it on the downlink. The transformation of the
signal refers to digital processing that may include demodulation,
decoding, re-encoding, re-modulation and/or filtering.

Round Trip Delay: time required for a signal to travel from a terminal to
the sat-gateway or from the sat-gateway to the terminal and back. This is
especially used for web-based applications.

Satellite: a space-borne vehicle embarking a bent pipe payload or a
regenerative payload telecommunication transmitter, placed into Low-Earth
Orbit (LEO), Medium-Earth Orbit (MEO), or Geostationary Earth Orbit (GEO).

Satellite beam: A beam generated by an antenna on-board a satellite

Service link: Radio link between satellite and UE

Transparent payload: payload that changes the frequency carrier of the
uplink RF signal, filters and amplifies it before transmitting it on the
downlink

User Connectivity: capability to establish and maintain data / voice /
video transfer between networks and Terminals

User Throughput: data rate provided to a terminal


3.2  Symbols

Void


3.3  Abbreviations

For the purposes of the present document, the abbreviations given in
TR 21.905 [1] and the following apply. An abbreviation defined in the
present document takes precedence over the definition of the same
abbreviation, if any, in TR 21.905 [1].



  ECEF Earth-Centered, Earth-Fixed
  EIRP Equivalent Isotropic Radiated Power
  GEO  Geostationary Earth Orbiting
  eNB  4G Node B
  GW Gateway
  LEO  Low Earth Orbiting
  Mbps Mega bit per second
  MS Mobile Services
  MSS  Mobile Satellite Services
  NGEO Non-Geostationary Earth Orbiting
  NTN  Non-Terrestrial Network
  RAN  Radio Access Network
  RTD  Round Trip Delay
  SNR  Signal-to-Noise Ratio
  TLE  Two-Line Element
  Rx Receiver
  UE User Equipment

         4  IoT Non-Terrestrial Networks overview and scenarios


4.1  IoT Non-Terrestrial Networks overview



A non-terrestrial network refers to a network, or segment of networks using
RF resources on board a satellite.

The typical scenario of a non-terrestrial network providing access to user
equipment is depicted below:



















 Figure 4.1-1: Non-terrestrial network typical scenario based on transparent
                                   payload



Non-Terrestrial Network typically features the following elements:

  -  One or several sat-gateways that connect the Non-Terrestrial Network
    to a public data network

    -  a GEO satellite is fed by one or several sat-gateways which are to
       enable satellite coverage over the targeted area (e.g. regional or
       even continental coverage). It is assumed that UE in a cell are
       served by only one sat-gateway

    -  A Non-GEO satellite served successively by one or several sat-
       gateways at a time. The system ensures service and feeder link
       continuity between the successive serving sat-gateways with
       sufficient time duration to proceed with mobility anchoring and hand-
       over

  -  A Feeder link or radio link between a sat-gateway and the satellite

  -  A service link or radio link between the user equipment and the
    satellite.

  -  A satellite which implements a transparent payload. The satellite
    typically generate several beams over a given service area bounded by
    its field of view. The beam could be either earth fixed beam or earth
    moving beam for LEO. The footprints of the beams are typically of
    elliptic shape. The field of view of a satellite depends on the on
    board antenna design and minimum elevation angle.

    -  A transparent payload: Radio Frequency filtering, Frequency
       conversion and amplification. Hence, the waveform signal repeated by
       the payload is un-changed;

  -  User Equipment are served by the satellite within the targeted service
    area.




  There may be different types of satellites listed here under:

                     Table 4.1-1: Types of NTN platforms

|Platforms       |Altitude range      |Orbit                     |Typical    |
|                |                    |                          |beam       |
|                |                    |                          |footprint  |
|                |                    |                          |size       |
|Low-Earth Orbit |300 - 1500 km       |Circular around the earth |100 - 1000 |
|(LEO) satellite |                    |                          |km         |
|Geostationary   |35 786 km           |notional station keeping  |200 - 3500 |
|Earth Orbit     |                    |position fixed in terms of|km         |
|(GEO) satellite |                    |elevation/azimuth with    |           |
|                |                    |respect to a given earth  |           |
|                |                    |point                     |           |


Typically

  -  GEO satellites are used to provide continental, regional or local
    service.

  -  A constellation of LEO satellites is used to provide services in both
    Northern and Southern hemispheres. In some case, the constellation can
    even provide global coverage including polar regions. For the later,
    this requires appropriate orbit inclination, sufficient beams generated
    and inter-satellite links.




4.2  IoT Non-Terrestrial Networks reference scenarios

The study captured in this Technical Report considers non-terrestrial
networks for IoT service providing access to NB-IoT/eMTC user equipment in
reference scenarios including:

  -  GEO and LEO orbiting scenarios

  -  No inter-satellite link

  -  Transparent payload

  -  Fixed or steerable beams resulting respectively in moving or fixed
    beam footprint on the ground

  -  Sub 6 GHz bands of interest.

IoT NTN scenarios A, B, and C are included in the study as shown in Table
4.2-1 below:



                  Table 4.2-1: IoT NTN reference scenarios

|NTN Configurations                          |Transparent satellite          |
|GEO based non-terrestrial access network    |Scenario A                     |
|LEO based non-terrestrial access network    |Scenario B                     |
|generating steerable beams (altitude 1200 km|                               |
|and 600km)                                  |                               |
|LEO based non-terrestrial access network    |Scenario C                     |
|generating fixed beams whose footprints move|                               |
|with the satellite (altitude 1200 km and    |                               |
|600km)                                      |                               |



5  IoT-NTN Architecture and Capabilities


5.1  IoT-NTN Architecture

IoT NTN connectivity via EPC is supported.

  Editor's Note: Support for IoT NTN connectivity via 5GCN is under
         discussion.




5.2  IoT-NTN UE Capabilities

GNSS capability in the UE is taken as a working assumption in this study
for both NB-IoT and eMTC devices.

   Editor's Note: UE can estimate and pre-compensate timing and frequency
         offset with sufficient accuracy for UL transmission - FFS pending
         RAN1 decision.

Simultaneous GNSS and NTN NB-IoT/eMTC operation is not assumed.

TBA




6  Radio Layer 1 issues and related solutions


6.1  IoT NTN Reference Parameters

The IoT NTN reference scenario parameters are listed in Table 5.1-1 6.1-1
below:

             Table 6.1-1: IoT NTN reference scenario parameters

|Scenarios           |GEO based non-terrestrial    |LEO based               |
|                    |access network - scenario A  |non-terrestrial access  |
|                    |                             |network -Scenario B & C |
|Orbit type          |station keeping a nominally  |circular orbiting at low|
|                    |fixed position in terms of   |altitude around the     |
|                    |elevation/azimuth with       |earth                   |
|                    |respect to a given earth     |                        |
|                    |point                        |                        |
|Altitude            |35,786 km                    |600 km                  |
|                    |                             |1,200 km                |
|Frequency Range     |< 6 GHz (e.g. 2 GHz in S band)                        |
|(service link)      |                                                      |
|Device channel      |- NB-IoT 180 kHz (DL), Up to 180 kHz with all         |
|Bandwidth  (service |permissible smaller resource allocations 12*15 kHz,   |
|link) (NOTE 7)      |6*15 kHz, 3*15 kHz, 1*15 kHz, 1*3.75 kHz (UL)         |
|                    |- eMTC: 1080 kHz (DL), Up to 1080 kHz with all        |
|                    |permissible smaller resource allocations , including  |
|                    |2*180 kHz, 180 kHz, 2*15 kHz or 3*15 kHz or 6*15 kHz  |
|                    |(UL)                                                  |
|Payload             |Transparent type             |Transparent Type        |
|Earth-fixed beams   |Yes                          |Scenario B: Yes         |
|                    |                             |(steerable beams), see  |
|                    |                             |NOTE 1                  |
|                    |                             |Scenario C: No (the     |
|                    |                             |beams move with the     |
|                    |                             |satellite)              |
|Max beam foot print |3500 km (NOTE 3)             |1000 km  (NOTE 2)       |
|size (edge to edge) |                             |                        |
|regardless of the   |                             |                        |
|elevation angle     |                             |                        |
|Min Elevation angle |10° for service link and 10° |10° for service link and|
|for both sat-gateway|for feeder link              |10° for feeder link     |
|and C-IoT device    |                             |                        |
|Max distance between|40,581 km                    |1,932 km (600 km        |
|satellite and C-IoT |                             |altitude)               |
|device at min       |                             |3,131 km (1,200 km      |
|elevation angle     |                             |altitude)               |
|Max Round Trip Delay|541.46ms (service and feeder |25.77 ms (600km)        |
|(propagation delay  |links)                       |(service and feeder     |
|only)               |                             |links)                  |
|                    |                             |41.77 ms (1200km)       |
|                    |                             |(service and feeder     |
|                    |                             |links)                  |
|Max differential    |10.3 ms                      |3.12 ms and 3.18 ms for |
|delay within a cell |                             |respectively 600km and  |
|                    |                             |1200km                  |
|Max Doppler shift   |0.93 ppm                     |24 ppm (600km)          |
|(earth fixed user   |                             |21ppm(1200km)           |
|equipment) (NOTE 6) |                             |                        |
|Max Doppler shift   |0.000 045 ppm/s              |0.27 ppm/s (600km)      |
|variation (earth    |                             |0.13 ppm/s (1200km)     |
|fixed user          |                             |                        |
|equipment)  (NOTE 6)|                             |                        |
|C-IoT device motion |Min 0 km/s (stationary       |Min 0 km/s (stationary  |
|on the earth        |device), max 120 km/h        |device), max 120 km/h   |
|C-IoT device antenna|Omnidirectional antenna with 0 dBi TX antenna gain and|
|types               |0 dBi RX antenna gain (NOTE 4)                        |
|C-IoT device max Tx |UE power class 3 with up to 200 mW (23dBm), UE power  |
|power               |class 5 with up to 100 mW (20 dBm)                    |
|C-IoT device Noise  |Omnidirectional antenna: 7 dB or 9 dB  (NOTE 5)       |
|Figure              |                                                      |
|Service link        |3GPP defined Narrow Band IoT and eMTC                 |
|NOTE 1: Each satellite has the capability to steer beams towards fixed     |
|points on earth using beamforming techniques. This is applicable for a     |
|period of time corresponding to the visibility time of the satellite.      |
|NOTE 2: This beam size refers to the Nadir pointing of the satellite.      |
|NOTE 3: The Maximum beam footprint size for GEO is based on current state  |
|of the art GEO High Throughput systems, assuming either spot beams at the  |
|edge of coverage (low elevation) or a single wide-beam.                    |
|NOTE 4: The use of a Circular polarized antenna is optional.               |
|NOTE 5: Same Noise Figure of 7 dB as in Release 16 TR 38.821 or 9 dB as in |
|Release 12 TR 36.888 for device can be assumed for link budget. The noise  |
|figure is device vendor implementation specific.                           |
|NOTE 6: Max Doppler shift and Max Doppler shift variation in the absence of|
|any device pre-compensation of satellite Doppler shift on the service link.|
|                                                                           |
|NOTE 7: System bandwidth is FFS                                            |










6.2  Link Budget Analysis


6.2.1  Link Budget Parameters


The following assumptions are agreed for a common set of link budget
parameters:

  -  UE power class (PC5=20 dBm)

  -  UE Noise Figure (NF=9 dB)

  -  Channel Bandwidth for NB-IoT and eMTC as was included in IoT NTN
    reference scenario parameters agreed in RAN1#103e:

    -  NB-IoT 180 kHz (DL), Up to 180 kHz with all permissible smaller
       resource allocations 12*15 kHz, 6*15 kHz, 3*15 kHz, 1*15 kHz, 1*3.75
       kHz (UL)

    -  eMTC: 1080 kHz (DL), Up to 1080 kHz with all permissible smaller
       resource allocations, including 2*180 kHz, 180 kHz, 2*15 kHz or 3*15
       kHz or 6*15 kHz (UL)

  -  Other losses:

                          Table 6.2-1: Other losses

|Other Losses      |GEO (35786  |LEO (1200  |LEO (600 km)|
|                  |km)         |km)        |            |
|Scintillation     |2.2         |2.2        |2.2         |
|losses            |            |           |            |
|Atmospheric losses|0.2         |0.1        |0.1         |
|Polarization loss |3           |3          |3           |
|Shadow margin     |3           |3          |3           |

  NOTE 1:  With PC3 (23 dBm) there is a 3dB gain compared to the PC5 (20
         dBm) assumption on UL.

  NOTE 2:  With NF=7 dB, there is a 2 dB improvement compare to NF=9 dB on
         DL.

  NOTE 3:  Link budgets with other link budget parameters are not excluded
         from being captured in the TR.

  NOTE 4:  These parameters are only for the purpose of link budget
         calculations.

  NOTE 5:  Atmospheric losses are a function of elevation angle.

Link budget analysis assumes 3 dB polarization loss for DL and 3 dB
polarization loss on UL for satellite parameters Set 1, Set 2, Set 3, and
Set 4

For the satellite parameter sets Set-3 and Set-4, the 3 dB beam width
(HPBW), central beam center elevation and central beam edge elevation in
the satellite parameter set(s) to be used in link budget calculations are
given in Tables 6.2-2 and 6.2-3. These parameters correspond to the
satellite parameter Set 3 and Set 4 given in Tables 6.2-6 and 6.2-7
respectively.

           Table 6.2-2: Set-3 parameters for link budget analysis

|SET 3                      |GEO 35786 km  |LEO-600 km |LEO-1200 km  |
|3 dB Beam width (HPBW)     |0.735 degree  |22.0631    |22.0631      |
|                           |              |degree     |degree       |
|Central beam center        |20.88 degree  |43.78      |46.05 degree |
|elevation                  |              |degree     |             |
|Central beam edge elevation|12.5 degree   |30 degree  |30 degree    |
|Central beam edge          |40316 km      |1074 km    |1998 km      |
|satellite-UE distance      |              |           |             |


           Table 6.2-3: Set-4 parameters for link budget analysis

|SET 4                              |LEO-600 km             |
|3 dB Beam width (HPBW)             |104.7 degree           |
|Central beam center elevation      |90 degree              |
|Central beam edge elevation        |30 degree              |
|Central beam edge satellite-UE     |1076 km                |
|distance                           |                       |


  NOTE 1:  The 3 dB beam width (HPBW) is already included in satellite
         parameter set 1 and Set 2 in TR 38.821 Table 6.1.1.1-1 and Table
         6.1.1.1-2 respectively. The central beam center elevation for Set-1
         and Set-2 is defined as the target elevation angle that is included
         in in TR 38.821 Table 6.1.3.2-1. The central beam edge satellite-UE
         distance can be derived from the central beam edge elevation and
         does not need to be included.

  NOTE 2:  Central beam center elevation is the beam center elevation of
         the central beam in the beam layout.

  NOTE 3:  Central beam edge elevation is the minimum beam edge elevation
         of the central beam in the beam layout.

  NOTE 4:  In SLS evaluation with a multiple beam layout, the central beam
         is the serving beam for UEs. The outer beams have beam center
         elevation that is different from the central beam center
         elevation.  For the interference modelling, the interference due to
         the outer beams is determined by using their respective beam center
         elevations.

  NOTE 5:   For the multiple-beam satellite cell, the longest beam edge
         distance will correspond to the minimum beam edge elevation of the
         most outer beam as illustrated in figure below.



                                    [pic]
  Figure 6.2-1 Illustration of beam layout and elevation angles for IoT NTN


The following satellite set parameters Set-1, Set-2, Set-3, and Set-4 given
in Tables 6.2-4, 6.2-5, 6.2-6 and 6.2-7, respectively, can be used for the
for the system level simulator calibration.:

 Table 6.2-4: Set 1 satellite parameters (based on TR 38.821, Table 6.1.1.1-
                                     1)




 Table 6.2-5: Set 2 satellite parameters (based on TR 38.821, Table 6.1.1.1-
                                     2)



     Table 6.2-6: Set-3 satellite parameters for system level simulator
                                 calibration
                      (based on R1-2101146 - Eutelsat)

|Satellite orbit                 |GEO       |LEO-1200  |LEO-600   |
|Satellite altitude              |35786 km  |1200 km   |600 km    |
|Central beam edge elevation     |12.5      |30 degree |30 degree |
|                                |degree    |          |          |
|Central beam center elevation   |20.9      |46.05     |43.8      |
|                                |degree    |degree    |degree    |
|Payload characteristics for DL transmissions                      |
|Equivalent satellite   |S-band  |12 m      |0.4m      |0.4 m     |
|antenna aperture (NOTE |(i.e. 2 |          |          |          |
|1)                     |GHz)    |          |          |          |
|Satellite EIRP density |        |59.8      |33.7      |28.3      |
|                       |        |dBW/MHz   |dBW/MHz   |dBW/MHz   |
|Satellite Tx max Gain  |        |45.7 dBi  |16.2 dBi  |16.2 dBi  |
|3dB beam width (HPBW)  |        |0.7353    |22.1      |22.1      |
|                       |        |degree    |degree    |degree    |
|Satellite beam diameter|        |459km     |470 km    |234 km    |
|(NOTE 2)               |        |          |          |          |
|Payload characteristics for UL transmissions                      |
|Equivalent satellite   |S-band  |12 m      |0.4 m     |0.4 m     |
|antenna aperture (NOTE |(i.e. 2 |          |          |          |
|1)                     |GHz)    |          |          |          |
|G/T                    |        |16.7dB K-1|-12.8 dB  |-12.8 dB  |
|                       |        |          |K-1       |K-1       |
|Satellite Rx max Gain  |        |45.7 dBi  |16.2 dBi  |16.2 dBi  |
|NOTE 1: This value is equivalent to the antenna diameter in Sec.  |
|6.4.1 of TR 38.811                                                |
|NOTE 2: Satellite beam diameter is at Nadir point                 |
|NOTE 3: Central beam center elevation is referred to as central   |
|beam elevation in TR 38.821                                       |
|NOTE 4: Central beam edge elevation is the minimum beam edge      |
|elevation of the central beam in the beam layout.                 |


    .

     Table 6.2-7: Set-4 satellite parameters for system level simulator
                                 calibration
            (based on R1-2101019 - Thales, Sateliot, Gatehouse):

|Satellite orbit                         |LEO-600     |
|Satellite altitude                      |600 km      |
|Central beam edge elevation             |30 degree   |
|Central beam center elevation           |90 degree   |
|Payload characteristics for DL transmissions         |
|Equivalent satellite antenna   |S-band   |0.097 m     |
|aperture (NOTE 1)              |(i.e. 2  |            |
|                               |GHz)     |            |
|Satellite EIRP density         |         |21.45       |
|                               |         |dBW/MHz     |
|Satellite Tx max Gain          |         |11 dBi      |
|3dB beam width (HPBW)          |         |104.7 degree|
|Satellite beam diameter (Note  |         |1700 km     |
|2)                             |         |            |
|Payload characteristics for UL transmissions         |
|Equivalent satellite antenna   |S-band   |0.097 m     |
|aperture (NOTE 1)              |(i.e. 2  |            |
|                               |GHz)     |            |
|G/T                            |         |- 18.6      |
|                               |         |dB·K-1      |
|Satellite Rx max Gain          |         |11 dBi      |
|NOTE 1: This value is equivalent to the antenna      |
|diameter in Sec. 6.4.1 of TR 38.811                  |
|NOTE 2: Satellite beam diameter is at Nadir point    |
|NOTE 3: Central beam center elevation is referred to |
|as central beam elevation in TR 38.821               |
|NOTE 4: Central beam edge elevation is the minimum   |
|beam edge elevation of the central beam in the beam  |
|layout.                                              |





6.3  Timing Relationships

The following aspects related to timing relationships enhancements will be
studied to check whether enhancement is necessary and beneficial:

  -  For NB-IoT:

    -  NPDCCH to NPUSCH format 1

    -  RAR grant to NPUSCH format 1

    -  NPDSCH to HARQ-ACK on NPUSCH format 2

    -  NPDCCH order to NPRACH

    -  Timing advance command activation

    -  FFS: Other NB-IoT timing relationships



  -  For eMTC:

    -  MPDCCH to PUSCH

    -  RAR grant to PUSCH

    -  PDCCH order to PRACH

    -  MPDCCH to scheduled uplink SPS

    -  PUSCH to HARQ-ACK on PUCCH

    -  CSI reference resource timing

    -  MPDCCH to aperiodic SRS

    -  Timing advance command activation

    -  FFS: Other eMTC timing relationships



  -  Impact of large RTD (which impacts TA) on HD-FDD UL-DL timing
    relationships.



The study will identify IoT-NTN configurations needing activation/de-
activation via MAC CE and their timing relationships.




6.4  Time and Frequency UL Synchronization

The following aspects related to enhancements to time and frequency
synchronization will be studied:

  -  GNSS measurement window for initial access

  -  Potential impact of GNSS Position fix on UE power consumption
    considering at least the following parameters:

    -  GNSS power consumption value

    -  GNSS position Time To First Fix

  -  Potential impact of NTN SIB carrying the satellite ephemeris on:

    -  UE power consumption in NB-IoT and eMTC

    -  Accuracy of satellite location tracking

    -  RACH congestion

  -  UE pre-compensation of satellite delay and satellite Doppler shift
    during long UL transmission on (N-)PUSCH and PRACH in NB-IoT and eMTC.




6.5  HARQ

For NTN IoT, potential HARQ enhancements need to consider the main
characteristics of an IoT device, which are low complexity, low cost, low
power consumption and low throughput, and key requirements of IoT services
which are extended coverage, delay-tolerant and infrequent data
transmissions, and support of massive communications.

The peak throughput of IoT UEs operating over NTN is not expected to be
higher than the peak throughput of IoT UEs operating over TN.

The following aspects related to HARQ enhancements will be studied:

  -  Potential benefits and/or drawbacks of:

    -  Increasing the number of HARQ processes on throughput, latency,
       power consumption and complexity

    -  Disabling HARQ feedback for NB-IoT

    -  Disabling HARQ feedback for eMTC



  -  Necessity, potential benefits and/or drawbacks relation to HARQ
    operation in IoT NTN:

    -  Any other potential HARQ feedback mechanisms

    -  Reduced PDCCH monitoring

    -  Coverage enhancements

    -  Uplink transmission gaps with multiple HARQ processes

    -  Maintaining HARQ process continuity in serving cell change

    -  Multiple Transport Blocks scheduling

    -  Throughput enhancements



The study will identify whether HARQ stalling happens at least in the GEO
satellite scenario.




7  User Plane Aspects


7.1  Random Access Procedure

TBA




7.2  MAC Timers

TBA




7.3  HARQ

TBA


7  Radio Protocol Issues and Solutions


7.1  Requirements and key issues


7.1.1  Delay

The table below is amended from TR 38.821 [3] to identify the worst case
IoT-NTN scenarios to be considered.

       Table 7.1-1: NTN scenarios versus delay constraints, Source [3]

|NTN scenarios                       |GEO transparent     |LEO transparent   |
|                                    |payload             |payload           |
|Satellite altitude                  |35786 km            |600 km            |
|Relative speed of Satellite with    |negligible          |7.56 km per second|
|respect to earth                    |                    |                  |
|Min elevation for both feeder and   |10° for service link and 10° for feeder|
|service links                       |link                                   |
|Typical Min / Max NTN beam footprint|100 km / 3500 km    |50 km / 1000 km   |
|diameter (Note 2)                   |                    |                  |
|Maximum propagation delay           |541.46ms (Worst     |25.77ms           |
|contribution to the Round Trip Delay|case)               |                  |
|on the radio interface between the  |                    |                  |
|gNB and the UE                      |                    |                  |
|Minimum propagation delay           |477.48ms            |8ms               |
|contribution to the Round Trip Delay|                    |                  |
|on the radio interface between the  |                    |                  |
|gNB and the UE                      |                    |                  |
|Maximum Delay variation seen by the |Negligible          |Up to +/- 40      |
|UE (Note 3)                         |                    |µs/sec (Worst     |
|                                    |                    |case)             |
|NOTE 1: The beam footprint diameter is indicative. The diameter depends on   |
|the orbit, earth latitude, antenna design, and radio resource management     |
|strategy in a given system.                                                  |
|NOTE 2: The delay variation measures how fast the round trip delay (function |
|of UE-satellite-NTN gateway distance) varies over time when the satellite    |
|moves towards/away from the UE. It is expressed in µs/s and is negligible for|
|GEO scenario.                                                                |
|NOTE 3: Speed of light used for delay calculation is 299792458 m/s.          |


When several non-terrestrial network scenarios feature a maximum in terms
of delay constraints, it is sufficient to study only one of these
scenarios.

  -  NTN Scenario based on GEO with transparent payload for RTT and delay
    difference constraints

  -  NTN Scenario based on LEO with transparent payload and moving beams
    for the delay variation related constraint.





7.2  User plane enhancements


7.2.1  MAC

The challenges associated with the expiry of MAC timers in NR-NTN remain
the same in IoT-NTN and high RTT of NTN is the primary cause of this [10].
The following sections are adopted from TR 38.821 [3] with suitable
amendments for IoT operation.




7.2.1.1  Random Access

Enhancement to random access (RA) response window

Problem Statement

After transmitting the Random Access Preamble (Msg1), the UE monitors the
PDCCH for the Random Access Response (RAR) message (Msg2). The RA Response
window starts at a determined time interval after the preamble
transmission. If no valid response is received during the RA Response
window, a new preamble is transmitted. If more than a certain number of
preambles have been transmitted with no valid response during the RA
Response window, a random access problem is indicated to upper layers.

In NTN the propagation delay is much larger and therefore, RAR message
cannot be received by the UE within the time interval specified for
terrestrial communications. Therefore, the starting time of RA Response
window should be modified to support IoT-NTN.

Solution Overview

Similar to NR-NTN [3], the offset can be adjusted to delay the start of the
RA Response window for IoT-NTN [10]. If the start of the ra-ResponseWindow
is accurately compensated and no extension of repetition is required, there
is no need to extend the ra-ResponseWindowSize for IoT NTN.



Enhancement to contention resolution timer

Problem Statement

When the UE sends an RRC Connection Request (Msg3), it will monitor for
Msg4 in order to resolve a possible random-access contention. The mac-
ContentionResolutionTimer starts after Msg3 transmission. The maximum
configurable value of mac-ContentionResolutionTimer is large enough to
cover the Round Trip Delay in NTN. However, to save UE power, the behavior
of mac-ContentionResolutionTimer should be modified to support NTN.

Solution Overview

Similar to NR-NTN [3], introduce an offset to delay the start of the mac-
ContentionResolutionTimer for IoT-NTN [10].




7.2.1.2  Discontinuous Reception (DRX)

Problem Statement

The Discontinuous Reception (DRX) supports UE battery saving by reducing
the PDCCH monitoring time. Several RRC configurable parameters are used to
configure DRX. [7, TS36.331]

HARQ RTT Timer is the minimum duration before a downlink assignment for
HARQ retransmission is expected by the MAC entity. UL HARQ RTT Timer is the
same as DL HARQ RTT Timer, just for the uplink. If HARQ is supported by IoT-
NTN, the handling of DL HARQ RTT Timer and UL HARQ RTT Timer, should be
modified to support IoT-NTN.

Modification of the remaining timers related to DRX is not needed to
support IoT-NTN, similar to NR-NTN [3].

Solution Overview

As the challenges associated with the expiry of MAC timers in NR-NTN [3]
remain the same in IoT-NTN, it is assumed that the same solutions as NR-NTN
for the start of DL HARQ RTT Timer and UL HARQ RTT Timer can be reused as a
baseline to support IoT-NTN [10].




7.2.1.3  Scheduling Request

Problem Statement

A UE can use a Scheduling Request (SR) to request UL-SCH resources from the
eNB for a new transmission or a transmission with a higher priority. SR
transmission is configured by RRC. While the prohibit timer (sr-
ProhibitTimer) is active, no further SR is initiated. The sr-ProhibitTimer
will at latest expire after 560ms for eMTC or after 8 NPRACH opportunities
for NB-IoT [7] and initiate a SR. For GEO systems the value range may not
be sufficient because of the large RTT. The sr-ProhibitTimer may have to be
modified to support IoT-NTN.

Solution Overview

  Editor's Note: The value range of sr-ProhibitTimer for IoT-NTN  needs  to
         be decided.




7.2.1.4  HARQ

  Editor's Note: This section will be updated based on further agreements
         on HARQ, e.g., whether to disable HARQ feedback.




7.2.1.5  Uplink scheduling

The typical procedure when data arrives in the buffer is to trigger a
Buffer Status Report and if the UE does not have any uplink resources for
transmitting the BSR, the UE will go on to do a Scheduling Request to ask
for resources. Since the scheduling request is only an indication telling
the network that the UE requires scheduling, the network will not know the
full extent of the resources required to schedule the UE, thus first the
network may typically schedule the UE with a grant large enough to send a
BSR so that the network may schedule the UE more accurately.

In non-terrestrial networks the drawback of this procedure is that it would
take at least 2 round-trip times from data arriving in the buffer at the UE
side until it can be properly scheduled with resources that would fit the
data. Due to the large propagation delays this may become prohibitively
large.

Based on these reasons, some enhancements for UL scheduling are discussed
for NR-NTN. However, unlike NR-NTN, UL scheduling enhancements for delay
reduction is not needed for NB-IoT over NTN as latency is not a critical
performance requirement for IoT devices [10].

  Editor's Note: UL scheduling enhancements for delay reduction might be
         needed for LTE-M UEs over NTN.




7.2.2  RLC


7.2.2.1  Reordering timer

Problem Statement

Both AM and UM modes use the t-Reordering timer to control the RLC wait
interval for out-of-order MAC data before considering the missing data as
lost and handing any received data off to the PDCP layer. The t-Reordering
timer can be configured with fixed values between 0 and 1600ms [7]. Large
propagation delay might have impacts on t-Reordering timer.

Solution Overview

  Editor's Note: It needs to be checked if there is a need to extend RLC t-
         Reordering timer in IoT-NTN.




7.2.2.2  RLC Sequence Numbers

In NB-IoT, the RLC sequence number (SN) size is 7 bits for AM and 5 bits
for UM. In eMTC, 10bit and 16bit are specified as the maximum possible UM
and AM SN field lengths [8]. The sequence number space needed for a radio
bearer depends on the data rate that is to be supported, the retransmission
time (i.e. the RTT, the number of retransmissions and the scheduling delay)
as well as the average size of the RLC SDUs. As the data rates for IoT-NTN
are significantly lower than NR-NTN, there is no need to extend the RLC SN
length for IoT-NTN.




7.2.3  PDCP


7.2.3.1  Discard timer

The transmitting PDCP entity shall discard the PDCP SDU when the
discardTimer expires for a PDCP SDU or when a status report confirms the
successful delivery [9]. The discardTimer can be configured up to 1500ms
for eMTC and up to 81920ms for NB-IoT, or can be switched off by choosing
infinity. The discardTimer mainly reflects the QoS requirements of the
packets belonging to a service.

  Editor's Note: It is FFS if there is a need to extend  PDCP  discardTimer
         in IoT-NTN.




7.2.3.2  PDCP Sequence Numbers

In NB-IoT, the PDCP sequence number (SN) size is 7 bits. In eMTC, the
maximum possible PDCP SN field length is 18bits [9]. As the data rates for
IoT-NTN are significantly lower than NR-NTN, there is no need to extend the
PDCP SN length for IoT-NTN.




7.3  Control plane enhancements

  Editor's Note: RAN2 should wait for RAN1's input on supporting multiple
         beams per cell for IoT-NTN.


7.3.1  Idle mode mobility enhancements


7.3.1.1  Tracking Area

Problem Statement

As outlined in 38.821 [3], satellites may provide very large cells,
covering hundreds of kilometres, and consequently would lead to large
tracking areas. In this scenario the tracking area updates (TAUs) are
minimal, however the paging load could be high because it then relates to
the number of devices in the tracking area.

Moving cells and consequently moving tracking areas would be difficult to
manage in the network as the contrast between the TAU and the paging
signalling load would be too extreme to find a practical compromise.

On one hand, small tracking areas would lead to massive TAU signalling for
UE at the boundary between 2 TAs as illustrated in figure 7.3.1.1-2.

                                    [pic]

 Figure 7.3.1.1-1: Moving Cells and Small tracking areas leading to massive
                               TAU signalling



On the other hand, wide tracking areas would lead to high paging load in
the satellite beams as illustrated in figure 7.3.1.1-2.

                                    [pic]

  Figure 7.3.1.1-2: Moving Cells and wide tracking areas leading to higher
                                 Paging load

However, tracking areas must be dimensioned to minimise the TAUs as this is
more signalling-intensive than paging on the network.

In practical tracking area design, one of the criteria affecting the
performance and capacity is the limiting capabilities of MME/AMF platforms
and the radio channel capacity.

Ping-pong effect generating excessive TAU, and it can be minimised by
ensuring 10-20% overlaps between the adjacent cells and appropriate
allocation of TAI List to UEs especially at the edge of cells/TAs.



Solution Overview

In order not to have TAU performed frequently by the UE triggered by the
satellite motion, the tracking area should be designed to be fixed on
ground (i.e. earth-fixes TA similar to NR-NTN). For NTN LEO, this implies
that while the cells sweep on the ground, the tracking area code (i.e. TAC)
broadcasted is changed, when the cell arrives to the area of next planned
earth fixed tracking area location. The TAC broadcasted by the eNB needs to
be updated as the eNB enters to the area of next planned tracking area.
When the UE detects entering a tracking area that is not in the list of
tracking areas that the UE previously registered in the network, a mobility
registration update procedure will be triggered.



                                    [pic]

  Figure 7.3.1.1-3: An example of updating TAC and PLMN ID in real-time for
                            LEO with moving beams

As shown in Figure 7.3.1.1-3, network updates the broadcast TAC in real
time according to the ephemeris and confirms that the broadcast TAC is
associated with the geographical area covered by the satellite beam. UE
listens to TAI = PLMN ID + TAC and determines to trigger registration area
update procedure based on the broadcast TAC and PLMN ID when it moves out
of the registration area.

  Editor's Note: Two possible options: (1) soft-switch broadcasting a  list
         of TACs per cell and (2) hard-switch based on a single TAC per cell
         are currently considered in NR-NTN. The same solution as NR-NTN can
         be reused for IoT-NTN, if applicable.




7.3.1.2  Using ephemeris information and UE location information

Ephemeris information and UE location information can be used to help UEs
perform measurement and cell selection/reselection, in addition to PCI and
frequency information included in the broadcast system information [3]
[10].

  Editor's Note: Provisioning of satellite ephemeris data and other
         information using System Information (SI) message for IoT-NTN is
         FFS.




7.3.1.3  Enhancements to UE mobility procedure

Cell selection/reselection for NR-NTN can be reused as a baseline [3] [10].

  Editor's Note: Detailed solutions of cell selection/reselection in
         eMTC/NB-IoT NTN need further discussion.




7.3.2  Connected mode mobility enhancements

Similar to NR-NTN [3], for LEO NTN, mobility management procedures should
take satellite movement into account, while for GEO NTN, the large
propagation delay needs to be accommodated.




7.3.2.1  Connected Mode Mobility for NB-IoT in NTN

There are no Connected Mode mobility procedures defined for NB-IoT. When an
NB-IoT UE goes out of service coverage of the source cell, it experiences a
Radio Link Failure (RLF). This triggers the UE to perform RRC connection re-
establishment.




7.3.2.2  Connected Mode Mobility for eMTC in NTN

Challenges in connected mode mobility for eMTC based NTN are similar to the
connected mode mobility issues in NR-NTN. These include (1) high latency
associated with handover signalling, (2) measurement validity, (3) frequent
handovers, (4) dynamic neighbour cell list, (4) handover of a large number
of UEs and (5) impact of propagation delay difference in measurements [3]
[10].

  Editor's  Note:  Agreements  regarding  handover  (including  Conditional
         Handover) for NR-NTN, will be discussed for  possible  adoption  in
         eMTC based IoT-NTN, if beneficial.




8  Control Plane Aspects




8.1  System Information Enhancements

TBA


8.2  Idle Mobility Enhancements

TBA




8.3  Radio Link Failure Enhancements (NB-IoT Only)

TBA




8.4  Connected Mobility Enhancements (eMTC only)

TBA




8.5  Tracking Area Update Enhancements

TBA




98 Recommendations on the way forward


98.1 Recommendations from RAN1

TBA


98.2 Recommendations from RAN2

TBA





         Annex A: Satellite ephemeris







Annex B: KPI and evaluation assumptions




B.1  Key Performance Indicators

KPIs defined in TR38.913 are considered.




B.2  Performance targets for evaluation purposes

Based on RAN2#105 conclusion on contribution R2-1901404 and SA1
specification requirements, the Non-Terrestrial network target performances
per usage scenario for IoT connectivity (low power wide area service
capability) was recommended in TR 38.821 as shown in Table B.2-1:

     Table B.2-1: Non-Terrestrial network target performances per usage
                        scenarios [source: TR 38.821]

|Usage scenarios                                                        |




         Annex C (Informative):
         Change history

|Change history                                                            |


 Date |Meeting |TDoc |CR |Rev |Cat |Subject/Comment |New version | |2020-11
   |RAN#90e |R3-185304 | | | |Skeleton TR |0.0.0 | |2021-01 |R2-113e |R2-
            2101455 | | | |Skeleton TR |0.0.1 | |2021-02 |R1#104e
                             R2#113e |R1-2101139
R2-2102492 | | | |- Text proposal for TR 36.763 chapter related to RAN1
 - Text proposal for TR 36.763 related to RAN2 |0.0.2 | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | |[pic][pic][pic]

