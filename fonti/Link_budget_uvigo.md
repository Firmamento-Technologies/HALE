  Small Satellite Link Budget
          Calculation

       Marcos Arias (Universidade de Vigo)
Fernando Aguado (Universidade de Vigo and CINAE)
             marcos@com.uvigo.es



        Santiago de Chile. November 2016

                                                   1/46
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Table of Contents
     1    Critical points in a Satellite Link
     2    Received power
            Friis formula
            Antennas
            Polarization
            Propagation
     3    Noise
           Radio Noise
           Antenna Noise
     4    Signal to noise ratio
            Rate carrier / noise
            Doppler effect
            Eb /N0
            Receiver sensitivity
            Interference
     5    Conclusions
                                                                  2/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Critical points in a Satellite Link



       Critical points in a Satellite Link
            Available power at the Ground Station
               Available power at the satellite
               Sensitivity of the Receiver
               SNR at the Receiver
               Reception level at the Earth to avoid interferences




                                                                     3/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Radio link chain




                                                                  4/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 RECOMMENDATION ITU-R P.525-2


       RECOMMENDATION ITU-R P.525-2
          Friis formula was first published in 1946: H. T. Friis, ’A note
          on a simple transmission formula,’ Proc. IRE 34, 254–256
          (1946)
                                          λ
                                              2 1
          pr = pt · (1 − |Γt |2 ) · gt · 4π·d   · am · gr · (1 − |Γr |2 ), where Γt
          and Γr are the reflection coefficients of the antennas and gt
          and gr the gain of the antennas
                                                1       1
               pr = pt · (1 − |Γt |2 ) · gt · 4π·d                           2
                                                   2 · am · Aeff · (1 − |Γr | ), where
                      λ      2
               Aeff = 4π gr is the effective area of recepction


                                                                                         5/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Free-space basic transmission loss


       Free-space basic transmission loss
            If the distance d between the antennas is much greater than
            the wavelength λ, the free-space attenuation (free-space basic
            transmission loss) in decibels will be: Lbf = 20 · log10 4π·d
                                                                          
                                                                      λ
               With a low-orbit satellite with elliptical orbit, the distance
               must be calculated using the worst case, that means when the
               satellite is with the lowest elevation angle and in the direction
               of the major axis of the ellipse



                                                                                   6/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Maximum distance
       Maximum distance
           The maximum distance with a satellite with maximum height
           H and minimum elevation
                             q     angle α is:
               dmax = −RE sin α +                      (RE sin α)2 + H 2 + 2 · RE · H

       Satellite distance
                                                         d
                                          α
                                              RE + H
                     RE


                                                                                        7/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 HUMSAT: Distance and time


                          Orbit                  Elevation        Maximum link      Link
                     altitude (Km)                 angle          distance (Km)   time (s)
                                                    40                  598          60
                           400                      50                  512          43
                                                    60                  457          30
                                                    40                  882          90
                           600                      50                  761          65
                                                    60                  683          45
                                                    40                 1159         119
                           800                      50                 1006          87
                                                    60                  907          61


                                                                                             8/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 RECOMMENDATION ITU-R P.341-5
       RECOMMENDATION ITU-R P.341-5
          The basic transmission loss of a radio link (Lb ) is the addition
          between the free-space basic transmission loss (Lbf ) and the
          loss relative to free space (Am ): Lb = Lbf + Am
          Main types of losses for satellite communications:
                      absorption loss (ionospheric, atmospheric gases or
                      precipitation)
                      effective reflection or scattering loss as in the ionospheric case
                      including the results of any focusing or defocusing due to
                      curvature of a reflecting layer
                      polarization coupling loss from any polarization mismatch
                      between the antennas for the particular ray path considered
                      effect of wave interference between the direct and reflected
                      rays from the ground, other obstacles or atmospheric layers
                                                                                           9/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Antenna Gain and Beamwidth


       Antenna Gain and Beamwidth
           The Beamwidth of a pattern is defined as the angular
           separation between two identical points on opposite side of
           the pattern maximum
               One of the most widely used beamwidths is the Half-Power
               Beamwidth (HPBW) that can vary with the azimuth angle
               An approximate relation between the antenna gain and its
               HPBW is gmax = HPBWE4π  ·HPBWH




                                                                                  10/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Polarization


       Polarization
            The polarization in the link can be Lineal, Horizontal or
            Vertical, or Circular, Left Hand (LHCP) or Right Hand
            (RHCP)
               Both antennas (satellite and earth station) should have the
               same polarization.
               Theoretically, using two orthogonal polarizations, radio-link
               capacity can be the double, but a crosspolarization
               interference can appear in the reception


                                                                                  11/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Recommendation ITU-R P.618-12

       Propagation data and prediction methods required for the design
       of Earth-space telecommunication systems
            In the design of Earth-space links for communication systems,
            several effects must be considered:
                      absorption in atmospheric gases; absorption, scattering and
                      depolarization by hydrometeors and emission noise from
                      absorbing media and they are especially important at
                      frequencies above about 10 GHz
                      loss of signal due to beam-divergence of the earth-station
                      antenna, due to the normal refraction in the atmosphere
                      a decrease in effective antenna gain, due to phase decorrelation
                      across the antenna aperture, caused by irregularities in the
                      refractive-index structure
                                                                                         12/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Recommendation ITU-R P.618-12 (II)
       Propagation data and prediction methods required for the design
       of Earth-space telecommunication systems
            Continue:
                      relatively slow fading due to beam-bending caused by
                      large-scale changes in refractive index; more rapid fading
                      (scintillation) and variations in angle of arrival, due to
                      small-scale variations in refractive index
                      possible limitations in bandwidth due to multiple scattering or
                      multipath effects, especially in high-capacity digital systems
                      attenuation by the local environment of the ground terminal
                      short-term variations of the ratio of attenuations at the up-
                      and down-link frequencies, which may affect the accuracy of
                      adaptive fade countermeasures
                      for non-geostationary satellite (non-GSO) systems, the effect
                      of varying elevation angle to the satellite                       13/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Recommendation ITU-R P.618-12 (III)

       Ionospheric effects (see Recommendation ITU-R P.531)
               Effects of the non-ionized atmosphere become critical above
               about 1 GHz and for low elevation angles
               These effects are:
                      Faraday rotation: a linearly polarized wave propagating
                      through the ionosphere undergoes a progressive rotation of the
                      plane of polarization;
                      dispersion, which results in a differential time delay across the
                      bandwidth of the transmitted signal;
                      excess time delay;
                      ionospheric scintillation: inhomogeneities of electron density in
                      the ionosphere cause refractive focusing or defocusing of radio
                      waves and lead to amplitude and phase fluctuations termed
                      scintillations
                                                                                          14/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Attenuation by atmospheric gases. Recommendation
 ITU-R P.676-10




                                                                                  15/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Attenuation by rain


       Attenuation by rain
           The attenuation by rain is calculated using the Specific
           attenuation (dB/Km) and the Effective rain path (Km)
               Specific attenuation γR is computed with the rainfall rate Rp
               (mm/h) exceeded for % of an average year, typically p = 0.01
               that provides a QoS of 99.99%.
               The effective path length Le is computed including the effect
               of the height of the terrain, elevation angle, longitude and
               latitude.


                                                                                  16/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Rainfall Rate




                                                                                  17/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Attenuation by rain p 6= 0.01

       Attenuation by rain p 6= 0.01
               The rain attenuation for different availability of 99.99%
               (p = 0.01%) can be computed using the following graph:




                                                                                  18/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Rain, fog and clouds

       Cross polarization due to the rain
           The rain drop shape is elongated
               This implies that the rain can be considered as an isotropic
               media for the electromagnetic wave propagation.
               Crossing the wave through a rain area, a cross polarization
               effect appears due to this effect.

       Attenuation due to clouds and fog. Recommendation ITU-R
       P.840-5
           It is quite equivalent to the rain attenuation method
               The attenuation values are smaller
                                                                                  19/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Estimated ionospheric effects for elevation angles of about
 30o

       Estimated ionospheric effects for elevation angles of about 30o
            The effects at 500 MHz are:
                      Faraday rotation 1.2 rotations
                      Propagation delay 1µs
                      Refraction < 2.40
                      Variation in the direction of arrival (r.m.s.) 48”
                      Absorption (auroral and/or polar cap) 0.2dB
                      Absorption (mid-latitude) < 0.04dB
                      Dispersion 0.0032 ps/Hz
                      Scintillation up to 27.5 dB


                                                                                  20/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Faraday rotation

       Faraday rotation
           When propagating through the ionosphere, a linearly polarized
           wave will suffer a gradual rotation of its plane of polarization
           due to the presence of the geomagnetic field and the
           anisotropy of the plasma medium




                                                                                  21/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 Scintillation

       Scintillation
            Scintillations are created by fluctuations of the refractive
            index, which are caused by inhomogeneities in the medium
               It is important for signals below 3 GHz but the effects may be
               observed occasionally up to 10 GHz
               Geographically, there are two intense zones of scintillation,
               one at high latitudes and the other centered within 20o of the
               magnetic equator. In the middle latitudes scintillation occurs
               exceptionally, such as during geomagnetic storms. In the
               equatorial sector, there is a pronounced night-time maximum
               of activity

                                                                                  22/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                                                  Friis formula
                                               Received power
                                                                  Antennas
                                                          Noise
                                                                  Polarization
                                         Signal to noise ratio
                                                                  Propagation
                                                  Conclusions


 HUMSAT-D: Atmospheric losses at 437 MHz




                                    Minimum              Maximum           Minimum     Maximum
                 Elevation          Latm (dB)            Latm (dB)         Lsci (dB)   Lsci (dB)
                     5                 0.02                 0.22             0.02        0.37
                    10                 0.02                 0.11             0.02        0.16
                    15                 0.02                 0.08             0.02         0.1




                                                                                                   23/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Recommendation ITU-R P.372-12


       Radio Noise
           The noise can be produced by:
                      Radiation from lightning discharges
                      Aggregated unintended radiation from electrical machinery,
                      electrical and electronic equipments, power transmission lines,
                      or from internal combustion engine ignition (man-made noise)
                      Emissions from atmospheric gases and hydrometeors
                      The ground or other obstructions within the antenna beam
                      Radiation from celestial radio sources



                                                                                        24/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Noise model



       Noise model
           Additive Gaussian White Noise
               Noise power spectral density of n0 constant
               Noise Power n = n0 · b where b is the bandwidth
               Effective noise temperature (Kelvin) at a reference point of
               the circuit t = nk0 where k = 1.379 · 10−23 W · Hz −1 · K −1
               So, n = k · b · t



                                                                                  25/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Internal effective noise temperature

       Internal effective noise temperature
               Effective noise temperature tef of a two port circuit (for
               example, an amplifier) referred at the entrance:
               nout = (nin + nef ) · g = k · b · (tin + tef ) · g = k · b · tout ⇒
               tout = (tin + tef ) · g
               Internal noise factor: fn = 1 + tTef0 where the reference
               temperature T0 = 290K
               External noise factor: fa = Ttin0
               System noise factor: f = tinT+t0 ef
               Noise Figure F = 10 · log10 f

                                                                                     26/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Effective Noise Temperature of a transmission Line



       Effective Noise Temperature of a transmission Line
            The effective noise temperature for a resistive attenuator
            (with attenuation a) at physical temperature tphy temperature
            is tef = tphy · (a − 1)
               This model is applied for any attenuator including
               transmission lines for both transmission and reception chains




                                                                                  27/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 HUMSAT-D: Ground Station Receiver Chain



                                          Transm.             Transm.             Pre-           Transm.
                                           Line 1              Line 2          amplifier          Line 3
             Gain (dB)                      -0.9               -0.11               20             -1.53
               Gain                        0.813               0.975              100             0.703
         Noise Figure (dB)                  0.9                 0.11               0.9             1.53
         Noise Temp. (K)                    66.8                 7.4              66.8            122.5
                                                                     7.4               66.8
            Total noise                                     66.8 + 0.813      75.9 + 0.793    160.14 + 122.5
                                                                                                         79.3
          temp. at input                     66.8             = 75.9           = 160.14         = 161.68




                                                                                                            28/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Antenna Noise



       Antenna Noise
           The antenna noise is modelled by an equivalent temperature
           tA
               The antenna noise picks up an average of the brightness
               temperature of the radiation bodies around the antenna,
               weightedR by
                          R the antenna pattern radiation:
                     1
               tA = 4π      tB · gr (θ, φ) sin θdθdφ




                                                                                  29/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 Noise temperature of a satellite antenna

       Noise temperature of a satellite antenna
           For the uplink, satellites with attitude control and a directive
           antenna that points to the Earth, the antenna temperature
           can be considered as T0 = 290K , but this value is considered
           as default if we don’t have further information
               For the downlink, the antenna noise sources are the
               temperature of clear sky tCS , the temperature due to radiation
               sources tFR (Sun, Moon), the temperature of the ground
               tGROUND (by side lobes), the additional temperature when it
               is raining tRAIN with a hydrometeor temperature tm and
                                                   m ·(aRAIN −1)
               attenuation aRAIN : tA = tCS +tFR +t
                                                 aRAIN           + tGROUND

                                                                                  30/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 RECOMMENDATION ITU-R P.372-12




                                                                                  31/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                                  Radio Noise
                                                          Noise
                                                                  Antenna Noise
                                         Signal to noise ratio
                                                  Conclusions


 HUMSAT-D: Total Noise



                                                  Antenna           System          Receiver
                                                   Noise             Noise           Noise
                       Gain                                          55.75
                    Gain (dB)                                         17.5
                 Noise Temp. (K)                      400            161.8            2400
                                                                                           2400
                    Total noise                                   400 + 161.8     561.8 + 55.75
                  temp. at input                      400           = 561.8         = 604.8




                                                                                                  32/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link   Rate carrier / noise
                                               Received power     Doppler effect
                                                          Noise   Eb /N0
                                         Signal to noise ratio    Receiver sensitivity
                                                  Conclusions     Interference


 Rate carrier / noise


       Rate carrier / noise
               C /N: Relation between the power of the modulated carrier C
               and the noise power
               C /N0 : Relation between the power of the modulated carrier C
               and the noise power spectral density N0 = k · t. It can
               characterize the channel without the final information about
               the bandwidth
                         EIRP
                              gr        gr  1
                                 = EIRP
                          Lb
               C /N0 = k·t          Lb  t k




                                                                                         33/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link   Rate carrier / noise
                                               Received power     Doppler effect
                                                          Noise   Eb /N0
                                         Signal to noise ratio    Receiver sensitivity
                                                  Conclusions     Interference


 Doppler effect

       Doppler effect
           The Doppler effect is the change in frequency of a wave for an
           observer moving relative to its source
               All non-geostationary satellite moves relative to the
               Earth-Station, so a Doppler effect appears.
               The change in frequency can be calculated as ∆f = ∆v
                                                                  c f0
               This shift increases with the frequency of the carrier f0 and in
               LEO. At 800 Km and 435 MHz, the doppler shift can be
               ±9.76KHz at low elevation angles
               The receiver must compensate this shift estimating the
               position of the satellite or it must increase the bandwith and
               the noise
                                                                                         34/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link   Rate carrier / noise
                                               Received power     Doppler effect
                                                          Noise   Eb /N0
                                         Signal to noise ratio    Receiver sensitivity
                                                  Conclusions     Interference


 Eb /N0


       Eb /N0
               For the purposes of link budget analysis, the most important
               aspect of a given modulation technique is the Signal-to-Noise
               Ratio (SNR) necessary for a receiver to achieve a specified
               level of reliability in terms of BER
               Eb /N0 = SNR · Rbb where Rb is the system data rate and Eb is
               the energy per bit of information
               In general, the modulation technique dictates the required
               system bandwidth


                                                                                         35/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link   Rate carrier / noise
                                               Received power     Doppler effect
                                                          Noise   Eb /N0
                                         Signal to noise ratio    Receiver sensitivity
                                                  Conclusions     Interference


 Receiver sensitivity


       Receiver sensitivity
           The first step in performing the link budget is determining the
           required signal strength at the receiver input. This is referred
           to as receiver sensitivity
               As described previously, this is a function of the Modulation
               Technique and the desired BER
               As an example, PSK modulation requires Eb /N0 = 9.5dB to
               achive a BER = 10−5 . Then its sensitivity will be the internal
               noise plus 9.5 dB.


                                                                                         36/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link     Rate carrier / noise
                                               Received power       Doppler effect
                                                          Noise     Eb /N0
                                         Signal to noise ratio      Receiver sensitivity
                                                  Conclusions       Interference


 HUMSAT-D: Receiver noise




                         Sensitivity (dBm)                                        -118
                         Sensitivity (dBW)                                        -148
                             SNR (dB)                                              13
                         Bandwidth (kHz)                                           2.4
                                                                           10−14.8
                       Noise Temperature (K)                      101.3 ·2400·1.379·10−23 = 2400




                                                                                                   37/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link   Rate carrier / noise
                                               Received power     Doppler effect
                                                          Noise   Eb /N0
                                         Signal to noise ratio    Receiver sensitivity
                                                  Conclusions     Interference


 Interference




                                                                                         38/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Summary for computation of the Link Budget


       Summary for computation of the Link Budget
          Compute the received power at the entrance of the receiver.
          It must be higher than the sensitivity
               Compute the noise received by the antenna
               Define the reference point to compute the performance of the
               Link Budget. Typically at the entrance of the receiver or at
               the entrance of the LNA
               Use the SNR and/or Eb /N0 methods to determine if we have
               achieved the required margins


                                                                              39/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Methods for computation of the Link Budget


       Methods for computation of the Link Budget
               Method 1 : SNR Method (More realistic). Usually, the Link
               budget is computed to provide a SNR greater than minimum
               SNR at the entrance of the LNA of the receiver. For this
               method it is necessary to know the bandwidth used by the
               receiver
               Method 2 : Eb /N0 Method (less realistic). It is assumed that
               the receiver uses the minimum possible bandwidth



                                                                               40/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 HUMSAT-D: Link budget

                   Transmitter power                                          0.5 W
                   Transmitter power                                         27 dBm
                   TTC antenna gain                                           -6 dBi
                  Transmission Losses                                         0.1 dB
               Tx Impedance mismatch                                          0.5 dB
                          EIRP                                    27 − 6 − 0.1 − 0.5 = 20.4dBm
                 Distance (H=800 Km,
                 α = 15o , f=437 MHz)                                      2030 Km
           Free-space basic transmission loss                              151.4 dB
                    Atmospheric loss                                        0.18 dB
                    Polarization loss                                        3 dBi
                Basic transmission loss                                    154.58 dB

                                                                                                 41/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 HUMSAT-D: Link budget II


             GS Antenna Gain                                              18.95 dBi
              Unpointing loss                                                1 dB
          Rx Impedance mismatch                                            0.51 dB
              Received power                            20.4-154.58+18.95-1-0.51 = -116.74 dBm
         Received power at receiver                             -116.74+17.5 = -99.24 dBm
           Margin with sensitivity                                -99.24-(-118) = 18.76 dB
                Bandwidth                                                   5 KHz
                   Noise                                604.8 · 1.379 · 10−23 · 5000 = 4.2 · 10−17 W
                   Noise                                                 -133.8 dBm
                   SNR                                          -116.74-(-133.8) = 17.06 dB
              SNR Minimum                                                   13 dB
                  Margin                                             17.06-13 = 4.06 dB
                                                                                                       42/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Low elevation angle



       Low elevation angle effects
           Greatest distance with the satellite
               Maximum Doppler shift
               Maximum atmospheric losses
               Greater noise (man-made and Earth noise)
               Ground reflection




                                                                  43/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 Difference between small and large satellites


       Difference between small and large satellites
            The antenna gain at the satellite is smaller
               The transmitted power from the satellite is also smaller
               If the satellite doesn’t have attitude control, the gain and the
               polarization can change over time. The worst case must be
               calculated
               It is useful to implement a dual receiver with two orthogonal
               polarizations



                                                                                  44/46
Small Satellite Link Budget Calculation
                            Critical points in a Satellite Link
                                               Received power
                                                          Noise
                                         Signal to noise ratio
                                                  Conclusions


 More information




       More information
           AMSAT-IARU Link Budget
               For non comercial purposes




                                                                  45/46
Small Satellite Link Budget Calculation
       Universidade    Centro de Innovación
         de Vigo      Aeroespacial de Galicia




  Small Satellite Link Budget
          Calculation

       Marcos Arias (Universidade de Vigo)
Fernando Aguado (Universidade de Vigo and CINAE)
             marcos@com.uvigo.es



        Santiago de Chile. November 2016




                                                   46/46
