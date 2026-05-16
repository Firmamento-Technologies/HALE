                                                  AMC & GM
                                         to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3


                        Acceptable Means of Compliance and Guidance Material
                         to Regulation (EU) 2019/947 — Issue 1, Amendment 3


                                   Annex to ED Decision 2025/018/R
                 ‘AMC and GM to Regulation (EU) 2019/947 — Issue 1, Amendment 3’


This document shows deleted, new or amended text as follows:
—      deleted text is struck through;
—      new or amended text is highlighted in blue;
—      an ellipsis ‘[…]’ indicates that the rest of the text is unchanged.




Note to the reader
In amended, and in particular in existing (that is, unchanged) text, ‘Agency’ is used interchangeably
with ‘EASA’. The interchangeable use of these two terms is more apparent in the consolidated versions.
Therefore, please note that both terms refer to the ‘European Union Aviation Safety Agency (EASA)’.




Annex to ED Decision 2025/018/R                                                           Page 1 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


The Annex to Decision 2019/021/R of the Executive Director of the Agency of 9 October 2019 is
amended as follows:


                                         List of abbreviations
[…]
 ATZ                  aerodrome traffic zone
 CAA                  civil aviation authority
 COTS                 commercial off-the-shelf
 CSP                  comprehensive safety portfolio
 CTR                  controlled traffic region
 CTA                  controlled aerospace
 FIZ                  flight information zone
 FTB                  functional test-based
 FTS                  flight termination system
 HF                   human factors
 iARC                 initial air risk class
 iGRC                 intrinsic ground risk class
 MSO                  multiple simultaneous operations
 RCM                  remote crew member
 RMZ                  radio mandatory zone
 SLA                  service level agreement
 SMS                  safety management system
 S&A                  see and avoid
 TLOS                 target level of safety
 TMZ                  transponder mandatory zone
 UTM                  UAS traffic management
 VHL                  very-high-level airspace
[…]


GM1 AMC1 Article 11 Rules for conducting an operational risk
  assessment
GENERAL
[…]
For the purposes of the SORA, the following definitions should apply:
— ‘populated area’ should be understood as ‘congested area’, as defined in Regulation (EU) No
965/2012 (the ‘Air Operations Regulation’): ‘in relation to a city, town or settlement, any area which
is substantially used for residential, commercial or recreational purposes’; and
— ‘rural area’ is used in the context of the air risk and it means the volume outside a populated area
and not within the aerodrome traffic zone (ATZ) of an aerodrome.
[…]



Annex to ED Decision 2025/018/R                                                           Page 2 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3



AMC1 Article 11 Rules for conducting an operational risk assessment
SPECIFIC OPERATIONS RISK ASSESSMENT (SORA) (SOURCE: JARUS SORA V2.5)
Edition: September 2025

Section 0 Executive summary

S0.1       The SORA approach
The SORA process is intended to provide a risk-proportionate method for determining the evidence
and assurance required for an unmanned aircraft system (UAS) to be acceptably safe when operating
in the ‘specific’ category of UAS operations as defined in Article 3(b) of Implementing Regulation (EU)
2019/947.
The SORA process provides structure and guidance for both the competent authority and the applicant
to support an application to operate a UAS in a given operational environment. The benefit of this
process is that both the competent authority and the applicant can allocate their available resources
and time proportionally to the risk of the intended UAS operation. After receiving an operational
authorisation, the applicant becomes the UAS operator. For the sake of simplicity, the term ‘UAS
operator’ is used throughout the rest of this AMC.
The SORA is a holistic safety risk management process used to evaluate the risks related to a given UAS
operation and then establish proportionate requirements a UAS operation should comply with to
ensure that a target level of safety (TLOS) is met. This TLOS is defined for people and aircraft that are
not involved in the UAS operation and is commensurate with the existing level of safety for manned
aviation. The TLOS-related values were chosen to ensure that the risk posed by UAS operations to third
parties will not be greater than that posed by manned aviation, which are seen as socially acceptable
values (see Section 5(f) of the Scoping Paper to AMC RPAS 1309 Issue 21 and Section 1.2.1 of Annex F2
Edition 2.5):
i.       for ground risk — fewer than one fatality per million hours (10–6 fatalities per flight hour)
         (for more details, see Annex F Edition 2.52 Section 1.2.1);
ii.      for air risk — fewer than one mid-air collision per 10 million flight hours (10–7 mid-air collisions
         per flight hour) for operations that are primarily conducted under self-separation and see-and-
         avoid (primarily in uncontrolled airspace); for operations that are conducted with separation
         provided by an air navigation service provider (primarily in controlled airspace), the TLOS is one
         mid-air collision per billion flight hours (10–9 mid-air collisions per flight hour).
The SORA has been developed using assumptions expected to be both credible and conservative
across a wide range of UAS operations.
Under the ‘specific’ category, different UAS operations will have different levels of inherent risk and,
thus, varying levels of the ability to maintain control of the operation to meet the TLOS will need to
be demonstrated. To do this, the SORA has developed the specific assurance and integrity levels (SAIL),
which map the maximum allowable loss-of-control rate to operational, organisational, personnel,
design and production risk controls that, when implemented correctly at the required level, ensures

1     jar_04_doc_amc_rpas_1309_issue_2_2.pdf (jarus-rpas.org)
2     http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf



Annex to ED Decision 2025/018/R                                                                      Page 3 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


that an operation meets the TLOS. This means that for a UAS operation conducted in a high-risk
environment (e.g. over a large city near an airport) more evidence would need to be provided to the
competent authority demonstrating that the operation is safe than for the same UAS operated in a
low-risk environment (e.g. at a protected test range and below 30 m).

S0.2     The SORA methodology




                                    Figure 1 — The SORA process


Note: If UAS operations are conducted across different environments, some steps may need to be
      repeated for each particular environment (e.g. the operation includes a flight path partially in
      controlled and partially in uncontrolled airspace; in this case, steps #4 and #5 should be
      repeated for the two environments).




Annex to ED Decision 2025/018/R                                                           Page 4 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3


The SORA methodology consists of ten systematic steps:

Step #1: Documentation of the proposed operation
This is a preparatory step which is intended to ensure the UAS operator has sufficient information to
complete Steps #2 to #9 of the SORA process. This information should enable the subsequent steps of
the SORA process to be completed successfully.

Step #2: Determination of the intrinsic ground risk class (iGRC)
The iGRC (scaled from 1 to 10) is determined by the UA characteristics (maximum characteristic
dimension and maximum speed) as well as the population density at risk in the operational volume
and ground risk buffer.

Step #3: Determination of the final ground risk class (GRC) (optional)
The final GRC is determined based on any mitigations put in place, as described in Annex B to this AMC,
which may have a significant effect on the likelihood of a fatality after the loss of control of the
operation, including:
(i)     strategic mitigations intended to reduce the risk before the flight;
(ii)    tactical mitigations intended to reduce the risk during the flight;
(iii)   mitigations intended to reduce the effect of a ground impact.
A final GRC higher than 7 is outside the scope of the SORA and should be handled in the ‘certified’
category of UAS operations, as defined in Article 6 of Implementing Regulation (EU) 2019/947.

Step #4: Determination of the initial air risk class (iARC)
The determination of the ARC is done in Steps #4 and #5. In Step #4, the iARC is assessed based on an
expected generalised encounter rate in the airspace identified in Step #1. The parameters that define
the four categories of ARC (a, b, c, d) are the following: whether the airspace is atypical (e.g.
segregated), altitude, controlled by air traffic versus uncontrolled, airport versus non-airport
environment, and airspace over urban versus rural environments.

Step #5: Application of strategic mitigations to determine the residual air risk class (ARC)
The residual ARC is obtained after applying any relevant strategic mitigations in order to lower the
iARC. Two types of strategic mitigations, as described in Annex C, exist in the SORA. Air risk mitigations
are either operational restrictions (e.g. boundaries, time of operation) which are controlled by the
UAS operators, or by the structure and associated rules of the airspace which is controlled by the
relevant authorities (e.g. U-space airspace).

Step #6: Tactical mitigation performance requirements (TMPRs) and robustness levels
Tactical mitigations for the operation are then applied in Step #6 to mitigate any remaining
unacceptable residual risk of a mid-air collision with manned air traffic after the strategic mitigations
have been applied.
TMPRs address the functions of detect, decide, command, execute and feedback loop (see Annex D
to this AMC) for each residual ARC.


Annex to ED Decision 2025/018/R                                                               Page 5 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


Step #7: Determination of the SAIL
A SAIL (scaled from I to VI) is then assigned to the operation described in Step #1 based on the final
GRC and residual ARC.

Step #8: Determination of containment requirements
The containment requirements aim to ensure that the TLOS can be met for both ground and air risk
in the adjacent ground area.
There are three possible levels of robustness for containment: low, medium and high; each level with
a set of safety requirements described in Annex E to this AMC as a function of the UA characteristics,
SAIL, average population density in the defined adjacent ground area and the presence of an outdoor
assembly of people within 1 km of the outer limit of the operational volume.

Step #9: Identification of operational safety objectives (OSOs)
The SAILs define the level of integrity and assurance (low, medium, high) to be met for each OSO
according to the criteria provided in Annex E to this AMC.
For the assigned SAIL, the UAS operator is required to show compliance with each of the 17 OSOs, at
the defined robustness level (for lower SAILs, it may not be required to show compliance for some
OSOs to the competent authority). The OSOs cover but are not limited to: the UAS designer, UAS
operator or other organisations involved in maintenance, related services and training, UAS technical
aspects, deterioration of external systems supporting UAS operations, human–machine interface,
human error, adverse operating conditions.

Step #10: Comprehensive safety portfolio (CSP)
The CSP is a suite of documents showing compliance with the requirements resulting from the SORA
steps for the proposed operation. If the CSP does not provide appropriate evidence as determined by
the SORA process at a given SAIL, changes to the proposed operation (e.g. reduction of the intrinsic
risk of the operation), additional mitigations, possible UAS design changes, or further
analysis/evidence may be needed.
Annex A to this AMC provides guidance and templates on how to provide relevant information to the
competent authority as part of the SORA process.




Annex to ED Decision 2025/018/R                                                           Page 6 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3


Section 1 Introduction

S.1.1    Preface
The SORA methodology guides both the UAS operator and the competent authority towards the
determination of whether a UAS operation can be conducted safely. The document should not be used
as a checklist, nor be expected to provide answers to all the potential challenges related to the UAS
operation. The SORA is a guide that allows an operator to identify the risk and, if needed, reduce it to
an acceptable level by tailoring their mitigations to the intended UAS operation. This involves meeting
or exceeding the target level of safety (TLOS) regardless of the complexity of the UAS operation, UA
size, or area of operation. The TLOS of operations conducted under the ‘specific’ category covered by
the SORA is equivalent to that of the ‘open’ and ‘certified’ categories. For this reason, it does not
contain prescriptive requirements but rather safety objectives to be met at various levels of
robustness commensurate with the risk of a given operation.

S.1.2    Purpose of the document
(a)     The purpose of the SORA is to propose a methodology of risk assessment to support an
        application for authorisation to operate a UAS in the ‘specific’ category.
(b)     Due to the operational differences and expected increase in level of risk of the operating
        environment, the ‘specific’ category cannot automatically take credit for the safety and
        performance data demonstrated with the large number of UAS operating in the ‘open’ category.
        Therefore, the SORA provides a consistent approach to assess the additional risks associated
        with the expanded operations not covered by the ‘open’ category.
(c)     This methodology is proposed as an acceptable means to evaluate the safety risks and
        determine the acceptability of a proposed UAS operation in the ‘specific’ category.
(d)     This methodology may be applied where the traditional approach to aircraft certification
        (approving the design, issuing an airworthiness approval and a type certificate) may not be
        appropriate and proportionate to the safety risk presented for the intended operation. This
        methodology may also support activities necessary to determine the associated airworthiness
        requirements.
(e)     The methodology is based on the principle of a holistic safety risk-based assessment model used
        to evaluate the risks of a given operation. The model considers the most common safety threats
        associated with a specified hazard, the relevant design, and the proposed operational
        mitigations for a specific UAS operation. The SORA then helps to evaluate the risks
        systematically and determine any operational limitation required for its safe operation. This
        method allows the UAS operator to determine acceptable risk levels and validate that those
        levels are complied with by the proposed operations. The competent authority may also apply
        this methodology to gain confidence that the UAS operator can conduct the operation safely.
(f)     The methodology, the related processes, and the values proposed in this document are
        intended to guide a UAS operator when performing a risk assessment of an intended operation
        to obtain an operational authorisation by the competent authority. At the same time, this
        material is intended to support the competent authority when assessing the completeness and
        acceptability of an application for a UAS to be operated in the ‘specific’ category.




Annex to ED Decision 2025/018/R                                                             Page 7 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3


S.1.3       Applicability
(a)      The methodology presented in this document is aimed at evaluating the safety risks involved in
         the operation of one or multiple UAS3 of any class and size. In the case of multiple simultaneous
         UA operating relative to each other, such as displays for entertainment, it is recommended to
         examine common mode failures and adapt the application of the SORA as needed in
         consultation with the competent authority.
(b)      Safety risks associated with collisions between UA and manned aircraft are in the scope of the
         methodology. The risk of collision between two UA will be addressed in future revisions of the
         document. It is expected that multiple simultaneous UAS operations and concurrent high-
         volume operators have a deconfliction strategy for their own UA.
(c)      The carriage of people is outside the scope of the SORA. The carriage of dangerous goods (e.g.
         weapons, munitions of war, explosives, hazardous medical samples) on board the UAS that
         present additional hazards is excluded from the scope of this methodology and might require
         additional safety considerations (e.g. demonstration of the ability to contain the dangerous
         goods). For more information, please refer to GM1 Article 2(11).
(d)      Privacy, data protection, liability, insurance, security and environmental protection are
         excluded from the scope of applicability of this methodology.
(e)      In addition to performing the SORA process, the UAS operator should also ensure compliance
         with all other regulatory frameworks applicable to UAS operations that are not necessarily
         addressed by the SORA, i.e. the SORA does not preclude any additional regulatory requirements
         implemented by the competent authority.
(f)      The SORA can be used to obtain operational authorisation for UAS operations conducted in
         multiple locations. In that situation, the UAS operator needs to provide a SORA that is applicable
         to all these areas to show that the SORA requirements will be met for all flights performed under
         the operational authorisation obtained. If a UAS operator can demonstrate to have sufficient
         procedures in place to correctly allocate operational volumes, buffers, adjacent ground areas
         and airspace volumes, a generic location authorisation could be considered as described in
         GM2 UAS.SPEC.030(2).

S.1.4       SORA documents
The SORA consists of the following parts:
(a)      Main Body (AMC1 to Article 11): describing the SORA risk assessment process;
(b)      Annex A to AMC1 to Article 11: guidelines for the UAS operator on collecting and presenting
         system and operation information for a specific UAS operation to the competent authority;
(c)      Annex B to AMC1 to Article 11: integrity and assurance levels for the mitigations used to reduce
         the intrinsic ground risk class (iGRC);
(d)      Annex C to AMC1 to Article 11: air risk strategic mitigations;
(e)      Annex D to AMC1 to Article 11: air risk tactical mitigations;



3     Refer to definition I.94 ‘Multiple simultaneous UAS operations’.



Annex to ED Decision 2025/018/R                                                                Page 8 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3


(f)      Annex E to AMC1 to Article 11: integrity and assurance levels for the operational safety
         objectives (OSOs);
(g)      Annex F Edition 2.54: theoretical basis for ground risk classification and containment
         requirements;
(h)      Annex I to AMC1 to Article 11: glossary.

Section 2 Key concepts and definitions

S.2.1       ‘Risk’ in the context of the SORA
(a)      The definition of ‘risk’ used in the SORA is the combination of the frequency (probability) of an
         occurrence and its associated level of severity.
(b)      The consequence of an occurrence will be designated as a harm of some type.
(c)      Many different categories of harm can arise from any given occurrence. This document will
         focus on occurrences of harm (e.g. UAS crash) that are short-lived and usually give rise to the
         potential loss of life. Chronic events (e.g. toxic emissions over a period of time) are explicitly
         excluded from this assessment. The categories of harm in this document involve the potential
         for:
         (i)     fatal injuries to third parties on the ground5;
         (ii)    fatal injuries to third parties in the air.
(d)      As the SORA only addresses safety risks, it is acknowledged that the competent authorities,
         when appropriate, may consider additional categories of harm (e.g. cybersecurity, privacy,
         disruption of a community, environmental damage, financial loss, etc.) as defined in point 2(c)
         of Article 12 of Implementing Regulation (EU) 2019/947.
(e)      Fatal injury is a well-defined condition and known by competent authorities. Therefore, the risk
         of under-reporting fatalities is almost non-existent. The quantification of the associated risk of
         fatality is straightforward. The usual means to measure fatalities are by the number of deaths
         within a particular operating time interval (e.g. fatal accident rate per million flight hours) or
         the number of deaths for a specified circumstance (e.g. fatal accident rate per number of take-
         offs).
(f)      Damage to critical infrastructure is a more complex condition and different countries may have
         differing sensitivities to this harm. Therefore, the quantification of the associated risks may be
         difficult and subject to national specificities, thus it is not addressed within the SORA and should
         be subject to a separate risk assessment. This should be done in cooperation with organisations
         responsible for the infrastructure, as they are most knowledgeable of the threats.




4     http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf
5     The risks to involved persons should be mitigated appropriately (e.g. through appropriate procedures). Involved persons
      should accept the risk of the UAS operation by informed consent and by explicitly agreeing to participate. For additional
      information, please refer to GM1 Article 2(18).



Annex to ED Decision 2025/018/R                                                                                 Page 9 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3


S.2.2      The SORA semantic model
(a)      The semantic model is a key aspect to understanding the SORA and introduces concepts and
         common terms for all users of the SORA.
(b)      To facilitate effective communication of all aspects of the SORA, the methodology requires
         standardised use of terminology for phases of operation6, procedures and operational volumes.
         The semantic model shown in Figure 2 provides a consistent use of terms for all SORA users.
         Figure 3 provides a graphical representation of the model and a visual reference to further aid
         the reader in understanding the SORA terminology.




                                        Figure 2 — The SORA semantic model




6     An operation may be a single flight or multiple sequential and/or simultaneous flights that are assessed under a single
      SORA process.



Annex to ED Decision 2025/018/R                                                                               Page 10 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3




                   Figure 3 — Graphical representation of the SORA semantic model
(c)    The SORA considers two states of the operation: ‘in control’ and ‘loss of control’. The SAIL score
       of the operation is inversely proportional to the acceptable loss-of-control rate of the operation
       to meet the OSOs. The higher the SAIL score, the higher the level of integrity and assurance of
       the OSOs becomes, which should result in a decreased loss-of-control rate for the operation.

S.2.2.1 The operational volume
(a)    Operational volume is defined as the volume in which the operation is intended to take place
       safely.
(b)    It is made up of the flight geography and the contingency volume.
(c)    The operational volume is the basis to determine the air risk class (ARC) of an operation.
(d)    The main SORA process is applied to the operational volume and ground risk buffer. To protect
       the adjacent ground area and airspace, the UAS operation should be contained within the
       operational volume.

S.2.2.2 The flight geography
(a)    The flight geography is the volume where the UAS operates in normal operations.
(b)    Depending on the type of the operation, the flight geography can be defined as a flight corridor
       for each planned trajectory, a larger volume to allow for a multitude of similar flights with
       changing flight paths or a set of different flight volumes fulfilling some specific conditions.
(c)    Whenever a particular flight requires the UA to traverse or loiter/hold at a specific point of
       interest, this point shall be included inside the flight geography. Refer to Chapter A.5 of Annex A
       to this AMC for additional information.

S.2.2.3 The contingency volume
(a)    The contingency volume surrounds the flight geography. The outer limit of the contingency
       volume is equivalent to the outer limit of the operational volume.
(b)    Entry into this volume is always considered an abnormal situation and requires the execution
       of appropriate contingency procedures to return the UA to the flight geography or perform a


Annex to ED Decision 2025/018/R                                                              Page 11 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3


        safe contingency landing. The size of the contingency volume should be determined based on
        the appropriate contingency procedures.
(c)     The outer limit of the contingency volume should include sufficient margins for system and
        operational errors (refer to the definition of ‘total system error’ in I.139 of Annex I to this AMC).
(d)     It should be noted that an abnormal situation may also occur inside the flight geography.

S.2.2.4 The ground risk buffer
(a)     The ground risk buffer is an area on the ground that surrounds the footprint of the contingency
        volume.
(b)     If the UA exits the contingency volume during a loss of control of the operation, it is expected
        to end its flight without exceeding the ground risk buffer.
(c)     The appropriate size of the ground risk buffer is based on the individual risk of an operation and
        is driven by the flight characteristics of the UA and the identified containment requirements of
        the SORA.
(d)     The footprint of the operational volume plus the ground risk buffer is the area used to
        determine the ground risk class (GRC).

S.2.2.5 The adjacent ground area
(a)     The adjacent ground area represents the ground area adjacent to the ground risk buffer where
        it is reasonably expected that a UA may crash following a loss-of-control situation resulting in a
        fly-away.
(b)     The lateral inner limit of the adjacent ground area is the outer limit of the ground risk buffer.
        The lateral outer limit of the adjacent ground area is computed starting from the outer limit of
        the contingency volume (see Figure 7).
(c)     The size of the adjacent ground area depends on the UA performance. UAS operators should
        not design operational volume areas which are not intended for use but are only there for
        manipulation of the composition of the adjacent ground area.

S.2.2.6 The adjacent airspace
(a)     The adjacent airspace corresponds to the airspace where it is reasonably expected that a UA
        may fly following a loss-of-control situation resulting in a fly-away.
(b)     The adjacent airspace is the airspace adjacent to the operational volume.
(c)     The lateral outer limit of the adjacent airspace is defined by the lateral outer limit of the
        adjacent ground area as described in point S.4.8.3(b).

S.2.3    States of the operation

S.2.3.1 Operation in control
(a)     An operation is considered in control when the remote crew can manage the current flight
        situation, such that no persons on the ground or in the air onboard manned aircraft are put in
        immediate danger.



Annex to ED Decision 2025/018/R                                                                Page 12 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3


(b)    This holds true for both normal and abnormal situations; however, the safety margins in the
       abnormal situation are reduced. In the abnormal state, it is the remote crew’s duty to try to
       return the operation back to normal state by executing contingency procedures as soon as
       practically possible.
(c)    Normal operation
       The UAS operator utilises standard operational procedures consisting of a set of instructions
       covering policies, procedures and responsibilities set out by the UAS operator that support
       operational personnel in ground and flight UAS operations safely and consistently.
(d)    Abnormal situation
       (i)    An abnormal situation is an undesired state where it is no longer possible to continue the
              flight using standard operational procedures, but the safety of the aircraft and of the
              persons on the ground or in the air is not in immediate danger. In this case, contingency
              procedures should be applied. Abnormal situations require attention and corrective
              actions (e.g. reduced engine performance, a system failure that can be managed with the
              backup or redundant system, issues that do not require an immediate descent, tolerable
              minor flight control malfunction or navigation equipment malfunction described handled
              by the UAS flight manual). Abnormal situations should not be confused with emergency
              situations.
       (ii)   Contingency procedures are designed to prevent a significant event (e.g. loss of control
              of the operation) that has an increased likelihood to occur in the future due to the current
              abnormal state of the operation. These procedures should return the operation to normal
              state and allow the return to using standard operational procedures or allow the safe
              cessation of the flight.

S.2.3.2 Loss of control of the operation
(a)    The loss of control of the operation is a state that corresponds to situations:
       (i)    whose outcome highly relies on providence; or
       (ii)   which cannot be handled by a contingency procedure.
(b)    In the context of the semantic model, this includes situations where a UA exits the operational
       volume and potentially operates over or in an area that may be characterised by a different
       level of ground or air risk.
(c)    The loss-of-control state is also entered if a UA does not follow the predefined route and the
       remote pilot is unable to control it and it crashes, or if an unplanned flight termination sequence
       is executed, even if this happens inside the operational volume.
(d)    Emergency procedures are executed in case of a loss of control of the operation. They are
       executed by the remote crew and may be supported by automated features of the UAS (or vice
       versa) and are intended to mitigate the effect of failures that cause or lead to an emergency
       condition (e.g. flight termination system). Emergency procedures should be activated as soon
       as the UA reaches the boundaries of the operational volume. However, as soon as the remote
       crew identifies a failure condition where the control of the UA cannot be recovered through
       contingency procedures (e.g. loss of propulsion), the remote crew may initiate the emergency


Annex to ED Decision 2025/018/R                                                              Page 13 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3


        procedures when the UAS is in the operation volume. Emergency procedures deal with affecting
        the UA to either:
        (i)     return to a state where the operation is ‘in control’; or
        (ii)    minimise hazards until the flight has ended.
(e)     Emergency response plan (ERP)
        (i)     The ERP deals with the potential hazardous secondary or escalating effects after a loss of
                control of the operation (e.g. timely intervention of emergency services).
        (ii)    The ERP is different from the emergency procedures, as it does not deal with the control
                of the UA.
        (iii)   The ERP is used for coordinating all the activities needed to respond to incidents and
                accidents.
(f)     Containment is a function that consists of technical and operational mitigations that are meant
        to contain the flight of the UA within the defined operational volume and ground risk buffer and
        reduce the likelihood of a loss of control of the operation resulting in a fly-away.

S.2.4     Robustness
(a)     To properly understand the SORA process, it is important to introduce the key concept of
        robustness.
(b)     Robustness is the term used to describe the combination of two key characteristics of a risk
        mitigation or operational safety objective: the level of integrity (i.e. how good the
        mitigation/objective is at reducing the risk), and the level of assurance (i.e. the degree of
        certainty with which the level of integrity is ensured).
(c)     The activities used to substantiate the level of integrity and assurance are detailed in
        Annexes B, C, D and E to this AMC. These annexes provide either guidance material or reference
        industry standards and practices where applicable.
(d)     Table 1 provides guidance to determine the level of robustness based on the level of integrity
        and the level of assurance.

                                  Low assurance           Medium assurance         High assurance
 Low integrity                    Low robustness           Low robustness          Low robustness
 Medium integrity                 Low robustness          Medium robustness       Medium robustness
 High integrity                   Low robustness          Medium robustness        High robustness

                          Table 1 — Robustness, integrity and assurance matrix
(e)     For example, if an applicant demonstrates a medium level of integrity with a low level of
        assurance, the overall robustness will be considered low as the robustness is equal to the lowest
        level of either integrity or assurance.
(f)     Any given risk mitigation or operational safety objective will have different requirements for the
        different levels of robustness. The SORA has three levels of robustness commensurate with the
        risk: low, medium and high.




Annex to ED Decision 2025/018/R                                                              Page 14 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3


(g)      Guidance for the level of assurance is provided below. An applicant is required in all cases to
         achieve the required level of integrity and produce or obtain any necessary evidence required.
         (i)     For low-level assurance, the applicant declares that the required level of integrity has
                 been achieved. The competent authority may request relevant evidence for review (e.g.
                 during oversight).
         (ii)    For medium-level assurance, the applicant declares that the required level of integrity
                 has been achieved. The declaration should include a reference to the evidence and the
                 evidence should be provided to the competent authority, unless the applicant uses a
                 means of compliance7 published by EASA. In this case, the applicant may not be required
                 to submit evidence during the application process. However, the competent authority
                 may request relevant evidence for review (e.g. during oversight).
         (iii)   For high-level assurance, the achievement of the required level of integrity is verified8 to
                 be acceptable by the competent authority or by an entity that is designated9 by the
                 competent authority.
(h)      The specific criteria defined in the SORA annexes take precedence over the criteria defined in
         point (g).
(i)      To accommodate national specificities, competent authorities may require different activities
         to substantiate the level of robustness. National specificities could include nationally sensitive
         infrastructure, protection of environmental areas, etc., and they are published by MSs as
         geographical zones according to Article 15 of Implementing Regulation (EU) 2019/947.

S.2.5      Roles and responsibilities
While performing an assessment using the SORA process, several key actors might be required to
interact in different phases of the process. The key actors to whom SORA is applicable are described
in this section.
(a)      Applicant — The applicant is the party that produces evidence for compliance with the
         operational safety objectives or mitigations. It may be the future UAS operator that seeks to
         obtain an operational authorisation or the organisation that designs or produces the UAS or a
         training organisation. Supporting material for the assessment may be provided by third parties
         (e.g. the designer of the UAS or the equipment, U-space service providers, etc.).
(b)      UAS operator — The UAS operator is an applicant that has obtained an operational
         authorisation from the competent authority. The operational authorisation allows the UAS
         operator to perform a series of flights provided they are performed in accordance with the
         scope and limitations of the operational authorisation, based on at least the SORA compliance
         demonstration. The UAS operator is responsible for the safe operation of the UAS. Therefore,
         the compliant execution of the procedures, training and other applicable programmes as well



7     For example, an acceptable means of compliance (AMC).
8     Refer to definition I.154 ‘Verified’ of Annex I to AMC1 to Article 11.
9     An entity designated by the competent authority should be understood in the meaning of a qualified entity as described
      in Article 69 of Regulation (EU) 2018/1139. The competent authority may grant to the designated entity the privilege to
      issue a certificate or an operational authorisation.



Annex to ED Decision 2025/018/R                                                                               Page 15 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3


         as the observation of the limitations and other requirements of the applicable concept of
         operations are the UAS operator’s obligation.
(c)      UAS designer and UAS production organisation — The UAS designer and the UAS production
         organisation is the party that designs and produces the UAS. In some cases, a UAS may be
         equipped with one or more components (e.g. parachute) designed and produced by an entity
         other than the UAS designer and installed by a UAS component integrator (that may also be the
         same entity designing the component or a different entity or the UAS operator itself). It may be
         expected that sometimes the design and production of the UAS or of the components is carried
         out by two different organisations. The design and production organisation has unique design
         evidence (e.g. system performance, system architecture, software/hardware development
         documentation, test/analysis documentation, etc.) it may choose to share with one or more
         UAS operators or with the competent authority or with EASA to help substantiate the operator’s
         SORA safety case. Alternatively, a design and production organisation may use the SORA process
         to target design objectives for specific or generic operations, tailored to the relevant SAIL.
         To obtain airworthiness approval(s), these design objectives could be complemented by the use
         of Light UAS certification specifications (CSs)10 or industry consensus standards if they are found
         acceptable by EASA. The UAS designer or the UAS production organisation may also be a UAS
         operator (for example, during a test flight campaign).
(d)      Competent authority — The competent authority that is referred to throughout this AMC is the
         authority designated by the Member State in accordance with Article 17 of Implementing
         Regulation (EU) 2019/947 to assess the safety case of UAS operations and to issue the
         operational authorisation in accordance with Article 12 of that Regulation. The competent
         authority may accept a UAS operator’s submission of an operations manual with an associated
         SORA-based risk assessment. Through the SORA process, the UAS operator may need to consult
         with the competent authority to ensure consistent application or interpretation of individual
         steps. The competent authority should also oversee the UAS operator in accordance with point
         (h) of Article 18 of Implementing Regulation (EU) 2019/947. When required, the competent
         authority may decide to make use of ‘recognised entities’ for reviewing supporting evidence for
         mitigations and operational safety objectives of an application. In this case, the competent
         authority defines the process and the conditions on how to appoint the ‘recognised entity’ and
         the competent authority has responsibility when issuing an operational authorisation based on
         the recommendation provided by the ‘recognised entity’. Alternatively, a competent authority
         may use a ‘designated entity’, also referred to as ‘qualified entity’, in accordance with Article 69
         of Regulation (EU) 2018/1139. In this case, the ‘designated entity’ may be granted the privilege
         to issue the operational authorisation.
         According to Article 77(1) of Regulation (EU) 2018/1139, EASA is the competent authority in the
         European Union to verify compliance of the UAS design and its components with the applicable
         rules, while the authority that is designated by the Member State is the competent authority to
         verify compliance with the operational requirements and compliance of the personnel’s
         competency with those rules. The following elements are related to UAS design:




10    For light UAS, please refer to Special Condition Light UAS at Special Condition Light UAS | EASA.



Annex to ED Decision 2025/018/R                                                                           Page 16 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3


         —       the OSOs marked in Table 14 as those for which the UAS designer is expected to develop
                 evidence;
         —       M2 mitigation: criterion #1;
         —       TMPR (design aspects);
         —       verification of the system to contain the UAS to avoid infringement of the adjacent areas
                 on the ground and/or adjacent airspace in accordance with Step #8 of the SORA process.
         If the UAS operation is classified as SAIL V and VI, compliance with the design requirements
         defined by the SORA (i.e. design-related OSOs, mitigations linked with the design and
         containment function) should be demonstrated through a type certificate (TC) issued by EASA
         according to Annex I (Part 21) to Regulation (EU) No 748/201211, as defined in Article 40(1)(d)
         of Implementing Regulation (EU) 2019/94512. For the OSOs and mitigations, the competent
         authority may verify their compliance.
         If the UAS operation is classified as SAIL IV, compliance with the design-related SORA
         requirements (i.e. design-related OSOs, mitigations linked with the design and containment
         function) should be demonstrated through a design verification report (DVR)13 issued by EASA.
         Evidence of compliance with non-design-related OSOs and mitigations will be provided to the
         competent authority according to the level of robustness of the OSOs, which will assess them
         as part of the application for the operational authorisation.
         If the UAS operation is classified as SAIL I, II or III, the competent authority may accept, as part
         of the operational authorisation process, a statement of compliance provided by the designer
         of the UAS or of a component with all OSOs and mitigations related to design.
         Regardless of the SAIL defined at the end of the SORA process, when the claimed level of
         robustness of the mitigation M2 or of the containment is high, the competent authority should
         require the UAS operator to use a UAS with a DVR issued by EASA limited to compliance with
         mitigation M2 and/or the containment requirements14.
(e)      Air navigation service provider (ANSP) — The ANSP is the designated provider of air traffic
         service in a specific area of operation (airspace). The ANSP assesses and/or should be consulted
         by the UAS operator whether the proposed operation can be safely conducted in the particular
         airspace the ANSP covers. Whether an ANSP approval would be required may depend on
         whether the particular proposed operation may be considered as being compliant with the rules
         of the air (thus being integrated in the airspace), national rules, or should be managed as a
         contained hazard (for example, through segregation according to the airspace policy of the
         Member State of operation)15.

11    Commission Regulation (EU) No 748/2012 of 3 August 2012 laying down implementing rules for the
      airworthiness and environmental certification of aircraft and related products, parts and appliances, as well
      as for the certification of design and production organisations (https://eur-lex.europa.eu/legal-
      content/EN/TXT/?uri=CELEX%3A32012R0748&qid=1753894524265).
12    Commission Delegated Regulation (EU) 2019/945 of 12 March 2019 on unmanned aircraft systems and on third-country
      operators of unmanned aircraft systems (OJ L 152, 11.6.2019, p. 1) (https://eur-lex.europa.eu/legal-
      content/EN/TXT/?uri=CELEX:32019R0945).
13    Design verification report | EASA
14    If the UAS has a DVR that covers the full design, this may cover also the mitigations.
15    The role of the ANSP as a function is distinct from that of the aviation regulator or the function of safety oversight.



Annex to ED Decision 2025/018/R                                                                               Page 17 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3


(f)      U-space service provider (USSP) — USSPs are entities certified according to Implementing
         Regulation (EU) 2021/66416 that provide services to support the efficient use of airspace as well
         as the safety of UAS operations. These services may support an operator’s compliance with their
         safety obligation and risk analysis.
(g)      Remote pilot-in-command (RPIC) — The remote pilot that is designated by the UAS operator
         as being in command of and charged with the safe conduct of the flight. Some UAS operations
         may require employing more than one remote pilot with different tasks; however, in this case,
         only one pilot is responsible as RPIC.
         UAS designed with a high level of automation may reduce the remote pilot’s workload to the
         point that operations can be conducted without allowing the intervention of a remote pilot.
(h)      Remote crew — The remote crew includes all UAS operator personnel involved in the operation
         of the UAS, with duties essential to the safe operation of the UAS. The RPIC is part of the remote
         crew.
(i)      Maintenance staff — Ground personnel in charge of maintaining the UAS before and after the
         flight in accordance with the UAS maintenance instructions.




16    Commission Implementing Regulation (EU) 2021/664 of 22 April 2021 on a regulatory framework for the U-space (OJ L
      139, 23.4.2021, p. 161) ( http://data.europa.eu/eli/reg_impl/2021/664/oj).



Annex to ED Decision 2025/018/R                                                                         Page 18 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3


Section 3 The SORA walk-through
This section provides a description for UAS operators of whether the SORA process applies to their
operations and how to complete the required SORA steps.

S.3.1 Introduction to the SORA walk-through
(a)      This section relates to how the SORA process is described in the document. The intent is to
         provide both the UAS operators and the competent authorities with clear guidance in terms of
         what is expected from the SORA process.
(b)      The following headers are applied:
         (i)     Outcome: is the result achieved when the task has been completed. All outcomes are
                 summarised in the comprehensive safety portfolio (CSP).
         (ii)    Task description: is a recommendation to be followed by UAS operators when
                 completing the SORA process.
         (iii)   Instructions: is material provided to UAS operators to better identify and understand the
                 steps contained in the task description.

S.3.2 Before starting the SORA process

S.3.2.1 Outcome
UAS operators will determine whether they should carry out the SORA process.

S.3.2.2 Task description
(a)      Before starting the SORA process, the following should be verified:
         (i)     whether the UAS operator uses a tethered aircraft for which Implementing Regulation
                 (EU) 2019/947 does not apply17;
         (ii)    whether the intended UAS operation falls under the ‘open’ category;
         (iii)   whether the intended UAS operation is covered by a standard scenario (STS) as defined
                 by Appendix 1 to Implementing Regulation (EU) 2019/947 and the UAS bears an
                 appropriate class identification label;
         (iv)    whether the UAS operation is covered by one of the PDRAs published by EASA as AMC to
                 Article 11 to Implementing Regulation (EU) 2019/947;




17    According to Annex I to Regulation (EU) 2018/1139, Implementing Regulation (EU) 2019/947 does not apply when the
      UAS operator uses a tethered aircraft with
      (a) no propulsion system, where the maximum length of the tether is 50 m, and where
          (i) the MTOM of the aircraft, including its payload, is less than 25 kg, or
          (ii) in the case of a lighter-than-air aircraft, the maximum design volume of the aircraft is less than 40 m3;
      (b) an MTOM of not more than 1 kg.
      In this case, national regulations apply.

Annex to ED Decision 2025/018/R                                                                          Page 19 of 204
                                      AMC & GM to Regulation (EU) 2019/947
                                             Issue 1, Amendment 3

         (v)    whether the operation involves the transport of people or the transport of dangerous
                goods posing a high risk to third parties18; in these cases, the operation falls under the
                ‘certified’ category;
         (vi)   whether the operation is subject to any local no-go criteria established by the competent
                authority (e.g. local conditions published by the competent authority of the State of
                operation).
(b)      If none of the above applies, the SORA process should be applied.

S.3.3 The phases of the SORA process
(a)      As part of the SORA process, it is critical to review the steps and validate the assumptions and
         derivations made throughout this process. The SORA process can be split into two phases (see
         Figure 4):
         (i)    Phase 1 (Step #1 to Step #9) focuses on the derivation of safety requirements and
                proposed means of compliance; and
         (ii)   Phase 2 (Step #10) focuses on compliance with the derived safety requirements from
                Phase 1.
(b)      Upon completing Phase 1, it is advisable for the UAS operator to obtain confirmation from the
         competent authority regarding the correctness of the process conducted thus far. The phases
         ensure there is a review of the first-phase outputs for the UAS operator to determine whether
         any adjustments to the proposed operation are required before undertaking the second phase.
         This approach should minimise unnecessary iterations in the operational procedures, remote
         crew requirements, and system(s) design in the proposed operations and mitigations19.
(c)      An additional benefit of the two phases is that they provide an opportunity for the UAS operator
         to engage with the competent authority. This is intended to support reaching a preliminary
         agreement that Phase 1 has been undertaken correctly, and that the derived requirements and
         proposed means of compliance for Phase 2 are appropriate.




18    Refer to GM1 Article 6 for additional information.
19    EASA created an automated platform in the IAM HUB to support UAS operators in conducting the SORA Phase 1.
      The platform may be reached at https://www.easa.europa.eu/en/domains/civil-drones.

Annex to ED Decision 2025/018/R                                                                   Page 20 of 204
                                      AMC & GM to Regulation (EU) 2019/947
                                             Issue 1, Amendment 3




                                  Figure 4 — The phases of the SORA process



S.3.3.1 Phase 1 (Derivation of requirements)
(a)    The purpose of Phase 1 is to derive all relevant safety requirements based on the proposed
       operation(s) which should result in a document suite that sufficiently describes the proposed
       operation(s). This should include the relevant information, safety claims and derived
       requirements of Step #1 to Step #9. The UAS operator should collect explanations, but not the
       entire justification, of the means by which the UAS operator will demonstrate compliance with
       any safety claims. This can assist both the UAS operator and the competent authority in
       ensuring that any means of compliance proposed is/are valid and will result in satisfying the
       safety claims. This may take the form of an initial compliance matrix (an example is provided in
       Chapter A.4 of Annex A to this AMC).
(b)    The results of Phase 1 may be the basis for the competent authority to conduct a preliminary
       evaluation. The competent authority may or may not be able to provide its formal agreement
       until final compliance evidence (covered in Phase 2) is submitted and reviewed.


Annex to ED Decision 2025/018/R                                                           Page 21 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3

(c) It is recommended that the UAS operator contact the competent authority as early as possible in
    order to present the available information and reach a common initial understanding and in-
    principle agreement on the safety claims, in particular the final GRC, residual ARC, and SAIL.

S.3.3.2 Phase 2 (Compliance with requirements)
(a)     Phase 2 occurs after the completion of Step #9. This phase is a final set of iterations to complete
        the SORA process. This should result in a SORA comprehensive safety portfolio (CSP), which
        collects the work done in all previous steps of the SORA into a comprehensive, including
        evidence showing compliance with the SORA requirements.
(b)     If the SORA process is completed correctly, the CSP should provide all the necessary claims,
        arguments and evidence to support the assessment and approval of the proposed operation(s).


Section 4 The SORA process

S.4.1     Step #1 — Documentation of the proposed operation

S.4.1.1 Introduction
Step #1 provides an opportunity for the UAS operator to collect and present contextual information
about the proposed operation and the intended safety claims made during Phase 1 of the SORA
process.

S.4.1.2 Outcome
A sufficiently detailed operational concept that allows the UAS operator to continue through the SORA
process.

S.4.1.3 Task description
(a)     Compilation of operational, technical and organisational information. Such information may
        include:
        (i)    maps, figures, diagrams and other information detailing the operational volume, the
               ground risk buffers, the adjacent ground area and the adjacent airspace to facilitate the
               determination of:
               (A)   the intrinsic GRC (i.e. population density maps, information on land use),
               (B)   the initial ARC (i.e. information on airspace use, aerodromes, and airspace charts),
                     and
               (C)   the adjacent ground areas;
        (ii)   information about the operational, technical and organisational elements of:
               (A)   the intended operation and functions during flight, including intended flight
                     profiles, states and modes that provide for safety throughout the nominal,
                     contingency and emergency phases of flight,
               (B)   any ground and air risk mitigations (strategic and tactical) used to reduce the
                     intrinsic ground risk or the initial air risk.


Annex to ED Decision 2025/018/R                                                               Page 22 of 204
                                      AMC & GM to Regulation (EU) 2019/947
                                             Issue 1, Amendment 3

(b)      A description of the contingency volume and ground risk buffers, and how they were
         determined.
(c)      The UAS operator may use Chapter A.3 of Annex A to this AMC to gain an understanding of the
         type of data that needs to be presented, and any other information that supports the risk
         assessment, to the competent authority.

S.4.2      Step #2 — Determination of the intrinsic ground risk class (iGRC)

S.4.2.1 Introduction
(a)      In this step, the UAS operator is required to assess the intrinsic ground risk of the operational
         volume and the ground risk buffer.
(b)      No ground risk mitigations will be applied at this step; this may be completed in Step #3.

S.4.2.2 Outcome
Calculation and documentation of the iGRC.

S.4.2.3 Task description
iGRC footprint
(a)      Identify the maximum characteristic dimension and the maximum speed of the UA.
(b)      Identify the iGRC footprint:
         (i)     identify the flight geography;
         (ii)    calculate the contingency volume;
         (iii)   calculate the initial ground risk buffer (the final ground risk buffer calculation will be
                 completed in Step #8).
(c)      Identify the highest population density within the iGRC footprint.
(d)      Identify the iGRC of the footprint using Table 2 for fixed-wing aircraft, rotorcraft-helicopters,
         rotorcraft-gyroplanes, VTOL-capable aircraft (including multirotors)20.




20    For lighter-than-air configurations, the UAS operator may propose a GRC based on the model defined
      in Annex F Edition 2.5, available at http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-
      Release.JAR_doc_29pdf.pdf.

Annex to ED Decision 2025/018/R                                                                  Page 23 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3


                                                       UAS iGRC

 Maximum UA characteristic
                                               1m             3m             8m            20 m            40 m
 dimension
            and
 Maximum speed                               25 m/s         35 m/s         75 m/s        120 m/s         200 m/s

                        Controlled
                                                1              1              2              3               3
                        ground area

                        <5                      2              3              4              5               6
 Maximum iGRC < 50                              3              4              5              6               7
 population
 density      < 500                             4              5              6              7               8
 (people/km2)
              < 5 000                           5              6              7              8               9

                        < 50 000                6              7              8              9               10

                        > 50 000                7              8                     Not part of SORA

 — A single UA with a take-off mass less than or equal to 250 g and having a maximum speed less
   than or equal to 25 m/s is considered to have an iGRC of 1 regardless of population density,
   unless operating over assemblies of people21.
 — A UA that is not expected to penetrate a standard dwelling will get a –1 GRC reduction in
   Step #3 from the M1(A) sheltering mitigation when not flying over large outdoor assemblies of
   people and most of the people overflown are protected by adequate structures; see Annex B of
   this AMC for additional details.

                           Table 1 — Intrinsic ground risk class (GRC) determination

(e)      For UA with a maximum characteristic dimension greater than 40 m, the iGRC should be
         calculated following the guidance in Appendices A and B to Annex F Edition 2.522.

S.4.2.4 Instructions

UA characteristics
(a)      For maximum UA characteristic dimension examples, refer to the definition of ‘UA characteristic
         dimensions’ in I.141 of Annex I to this AMC.
(b)      Maximum speed
         (i)    The maximum speed is conservatively defined as the maximum possible commanded
                airspeed of the UA, as defined by the UAS designer.


21    Additional information may be found in Appendix II to NPA 2017-05 (B) ‘Introduction of a regulatory framework for
      the operation of drones — Unmanned aircraft system operations in the open and specific category’
      (https://www.easa.europa.eu/en/downloads/22496/en).
22    http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf

Annex to ED Decision 2025/018/R                                                                         Page 24 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3

         (ii)   This is not the flight-specific maximum commanded airspeed of the UA as reducing the
                flight airspeed may not necessarily reduce the impact area23. Mitigations that limit
                airspeed below the maximum speed value during an impact can be considered in Step #3,
                referring to Annex B to AMC1 Article 11.

iGRC Footprint




                                 Figure 5 — Visualisation of the iGRC footprint


(c)      The UAS operator should have defined the area at risk when conducting the operation. This is
         defined as the iGRC footprint. It is composed of the operational volume plus the ground risk
         buffer as shown in Figure 5 above.
(d)      The operational volume is composed of the flight geography and the contingency volume (refer
         to Sections S.2.2.1, S.2.2.2 and S.2.2.3 respectively for additional information). To determine
         the operational volume, the UAS operator should consider the position-keeping capabilities of
         the UAS in 4D space (latitude, longitude, height and time). In particular, the accuracy of the
         navigation solution, the flight technical error of the UAS, the path definition error (e.g. map
         error) and latencies should be considered when determining the operational volume.
(e)      The iGRC footprint is used to determine the population density. It is expected that for many
         flights the iGRC footprint may cover segments with different population densities. The segment
         with the highest population density should be used when determining the iGRC.

Identification of the iGRC
(a)      The iGRC is found at the intersection of the applicable maximum population density and the
         rightmost column matching both criteria, the maximum UA characteristic dimension and the
         maximum speed in Table 2.
(b)      The UAS operator may provide substantiation to the competent authority for a different iGRC.
         See Appendix A of Annex F Edition 2.524 for further guidance.
(c)      UAS operations that do not have a corresponding iGRC (i.e. grey cells on the table) are outside
         the scope of the SORA methodology. In this case, UAS operators should consider the ‘certified’
         category.




23    The reduction may not be guaranteed in case of a loss of control of the UA.
24    http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf

Annex to ED Decision 2025/018/R                                                                      Page 25 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3

(d)      If population density values are not available or not accurate, the UAS operator may use
         qualitative descriptors for the iGRC table; the following approximations may be used as
         guidance:



 Quantitative
  population                Qualitative
                                                                              Area description
     value                  descriptors
 (people/km2)
                                     Areas that are controlled where uninvolved people are not
      Controlled Controlled ground / allowed to enter.
     ground area Extremely remote    Refer to point (21) of Article 2 of Implementing Regulation
                                     (EU) 2019/947 and related GM1.
                                                  Areas where people may be, such as forests, deserts, large
                                                  farm parcels, etc.
          <5           Remote
                                                  Areas where there is approximately one small building every
                                                  km2.
                                                  Areas of small farms.
         < 50          Lightly populated
                                                  Residential areas with very large lots (~ 4 acres or 16 000 m2).
                       Sparsely populated /
                                            Areas comprised of homes and small businesses with large lot
        < 500          Residential lightly
                                            sizes (~1 acre or 4 000 m2).
                       populated
                                                  Areas of single-family homes on small lots, apartment
                       Suburban /
                                                  complexes, commercial buildings, etc.
       < 5 000         Low-density
                                                  Can contain multistorey buildings, but generally most should
                       metropolitan
                                                  be below 3–4 stories.
                                                  Areas of mostly large multistorey buildings.
                       High-density
      < 50 000                                    The downtown area of most cities.
                       metropolitan
                                                  Areas of dense skyscrapers.
                       Assemblies of              Refer to point (3) of Article 2 of Implementing Regulation (EU)
      > 50 000
                       people                     2019/947 and related GM1.
        Table 2 — Correspondence between quantitative and qualitative assessment of the iGRC


Ground risk buffer
(a)      An appropriate initial ground risk buffer should be defined considering the principles outlined
         in criterion #3 of Section E.4 of Annex E of this AMC:
         (i)     with the 1-to-1 principle25; or
         (ii)    a different ground risk buffer value may be proposed by the UAS operator using the
                 principles outlined in Section 4, criterion #3 of Annex E of this AMC.
(b)      Cases where the final ground risk buffer may be different than the initial one could include:




25
      For the evaluation of the size of the ground risk buffer based on the 1:1 principle, see Section A.5.2.4 of Annex A.

Annex to ED Decision 2025/018/R                                                                                  Page 26 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3

         (i)    medium and high level of containment26;
         (ii)   use of ground risk mitigations, such as a parachute.

Controlled ground area
(a)      A controlled ground area is defined as the intended UAS operational area where only involved
         persons (if any) are present.
(b)      Controlled ground areas are a way to strategically mitigate the ground risk; the assurance that
         there will be no uninvolved persons in the iGRC footprint is under the full responsibility of the
         UAS operator. The competent authority may request evidence of how the UAS operator will
         ensure control of the ground area during operation.

Non-typical cases
(a)      There are certain cases, for example aircraft whose maximum characteristic dimension and
         maximum speed differ significantly from the selected column, which may have a significant
         effect on the iGRC. Such cases may not be well represented in the iGRC table and may lead to
         an increase or decrease in the iGRC. See Section 1.8 of Annex F Edition 2.527 for further
         guidance.
(b)      A UAS operator may consider that the iGRC is too conservative for its UA. Therefore, a UAS
         operator may decide to calculate the iGRC by applying the mathematical model defined in
         Section 1.8 of Annex F Edition 2.526. The UAS operator should choose the column that matches
         the critical area calculated for the UA that is used, as identified in Table B.8 of Annex B to this
         AMC. An automatic tool to calculate the critical area of a UA is available on the EASA website28.

Information on population density
(a)      Determining the population density to calculate the iGRC in Step #2 should be done using maps
         with appropriate grid size based on the intended operation. Competent authorities should
         designate specific maps to be used for determining population densities.
(b)      If there are no available population density maps acceptable to the competent authority, the
         qualitative population density descriptors (see Table 3) may be used to estimate the population
         density band in the operational volume and the ground risk buffer. Alternatively, the competent
         authority may require, or permit, UAS operators to provide appropriate population density
         maps. Table 4 below presents the suggested optimal grid size for different maximum heights of
         the operational volume.




26
      For additional information, refer to criterion #3 in Chapter E.4 of Annex E.
27    http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf
28    https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/critical-area-assessment-tool-caat

Annex to ED Decision 2025/018/R                                                                         Page 27 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3


                               Max. height (AGL) of
                                the operational            Suggested optimal grid
                                     volume                         size
                                                              (metre × metre)
                                  Feet       Metres
                                  500         152                  200 × 200
                                1 000          305                 400 × 400
                                2 500          762               1 000 × 1 000
                                5 000         1 524              2 000 × 2 000
                               10 000         3 048              4 000 × 4 000
                               20 000         6 096              5 000 × 5 000
                               60 000         18 288           10 000 × 10 000
                         Table 4 — Suggested grid size for population density maps
(c)      The authority-designated map should be at the suggested optimal grid size. If mapping products
         do not exist at the suggested optimal grid size, the competent authority should use the closest
         grid size available. If the closest grid size available is smaller than the suggested optimal grid
         size, then the map should be smoothed to the suggested optimal grid size.
(d)      If the UAS operator identifies inaccuracies in the designated static population density map, it
         can provide alternative data (for example, by using other mapping products, satellite imagery,
         on-site inspections, local knowledge of the area, etc.) that demonstrates the correction in the
         estimated average population density of the area. If accepted by the competent authority, the
         UAS operator may use the alternative data to determine the iGRC. Use of time-based restriction
         arguments (e.g. flying at night) for the reduction of the number of people at risk on the ground
         are addressed in SORA Step #3.
(e)      Additional information may be found in Section 3.2 of Annex F Edition 2.529.

S.4.3      Step #3 — Final ground risk class (GRC) determination (optional)

S.4.3.1 Introduction
(a)      The intrinsic risk of a person being struck by a UA during the loss of control of the operation can
         be reduced by means of acceptable mitigations.
(b)      In this step, the UAS operator may identify ground risk mitigations and reduce the GRC of the
         operation.

S.4.3.2 Outcome
(a)      Identification of the mitigations applied to reduce the iGRC for the iGRC footprint.
(b)       Identification of the applicable mitigations.
(c)      Determination of the final GRC by subtracting the credit derived by the mitigations from the
         iGRC.
(d)      Collection of information and references used to substantiate the application of the ground risk
         mitigation(s).

29    http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf

Annex to ED Decision 2025/018/R                                                                      Page 28 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3

S.4.3.3 Task description
(a)      Identify the applicable mitigations listed in Table 5 that could lower the iGRC of the iGRC
         footprint. All mitigations should be applied in numerical sequence.

                                                                                         Level of robustness

           Mitigations for ground risk                                                Low      Medium         High

           M1(A) — Strategic mitigations — Sheltering                                  –1          –2         n/a

           M1(B) — Strategic mitigations — Operational restrictions                   n/a          –1         –230

           M1(C) — Tactical mitigations — Ground observation                           –1         n/a         n/a

           M2 — Effects of UA impact dynamics are reduced                             n/a          –1          –2

                               Table 5 — Mitigations for the determination of the final GRC
(b)      Identify in Annex B to AMC1 Article 11 the requirements to be complied with in order to receive
         appropriate credit for the mitigation.
(c)      If an M2 mitigation that affects the UA’s descent behaviour is used, assess whether the size of
         the ground risk buffer defined in Step #2 is still valid.
(d)      Determine the final GRC by applying the appropriate correction to the iGRC.

S.4.3.4 Instructions
Ground risk mitigations
(a)      Step #3 is optional.
(b)      The mitigations used to modify the iGRC have a direct effect on the safety objectives associated
         with an operation. Therefore, it is important to ensure their robustness. This has particular
         relevance for technical mitigations (e.g. parachute).
(c)      The final GRC determination is based on the availability and correct application of the
         mitigations to the operation. Table 5 provides a list of potential mitigations and the associated
         relative correction factor. All mitigations should be applied in numeric sequence to perform the
         assessment. Annex B to this AMC provides additional details on the robustness of each
         mitigation. Competent authorities may define or accept additional mitigations and the relative
         correction factors.
(d)      A quantitative approach to mitigations allows a reduction in the iGRC by 1 point if the mitigation
         reduces the population at risk to the next lowest iGRC population band. This is in most cases
         approximately a factor of 10 (90 % reduction) compared to the risk that is assessed before




30    The competent authority may decide to require UAS operators to use static population density maps augmented with
      the identification of the areas where the population density data is most probably incorrect and provide a corrective
      value (e.g. static population density maps may use as source census data where typically commercial, recreational,
      industrial and other areas are defined as unpopulated even if during some part of the day they may have a high
      population density value). In this case, the UAS operator may be allowed to claim a reduction of the iGRC higher than 2.

Annex to ED Decision 2025/018/R                                                                                Page 29 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3

         mitigations are applied. Such quantitative criteria should be used to validate the risk reduction
         that is claimed when applying Annex B to this AMC.
(e)      In rare situations, iGRC reductions greater than the ones shown in Table 5 may be possible.
         Refer to Annex B to this AMC for further guidance.
(f)      When applying all the M1 mitigations, the final GRC cannot be reduced to a value lower than
         the lowest value in the applicable column in Table 2. This is because it is not possible to reduce
         the number of people at risk below that of a controlled ground area.
(g)      If the mitigation influences the descent behaviour of the UA, for example by using a parachute,
         the ground risk buffer size should be redefined using the updated assumptions including the
         effects of the mitigations.
(h)      Additional information may be found in Chapter A.3 of Annex A to this AMC regarding guidance
         on presenting the data that supplements the risk assessment to the competent authority.
What if the final GRC is greater than 7?
If the final GRC is greater than 7, the operation is considered to pose a greater risk than the SORA is
designed to support. The UAS operator may consider other options such as using the ‘certified’
category or changing the characteristics of the UAS operation in Step #1 (as stated in Figure 1).

S.4.4 Step #4 — Determination of the initial air risk class (iARC)

S.4.4.1 Introduction to the air risk assessment process
(a)      The SORA uses the operational airspace defined in Step #1 as the baseline to evaluate the
         intrinsic risk of mid-air collision with manned aircraft and for determining the iARC. The iARC
         may be modified (lowered) by applying strategic and tactical mitigations. An example of
         strategic mitigations to reduce mid-air collision risk may be by operating during certain times or
         within certain boundaries. After applying strategic mitigations, any residual mid-air collision risk
         is addressed by means of tactical mitigations.
(b)      Tactical mitigations take the form of detect-and-avoid systems or alternative collaborative
         means, such as ADS-B, systems transmitting on the SRD 860 frequency band, U-space services31
         or operational procedures. Depending on the residual mid-air collision risk, the tactical
         mitigation performance requirement(s) may vary.
(c)      As part of the SORA process, the UAS operator should cooperate with the relevant service
         provider (e.g. ANSP or U-space service provider) for the airspace it intends to operate and obtain
         the necessary authorisations. Additionally, generic local authorisations or local procedures
         allowing access to a certain portion of airspace may be used if available. The competent
         authority or the ANSP may impose additional strategic or tactical mitigations on airspace
         authorisations, taking into account uncertainties relating to UA reliability, conspicuity, and
         other factors.
(d)      The SORA recommends that, irrespective of the results of the risk assessment, the operator pay
         particular attention to all features that may increase the detectability of the UA in airspace.



31    Some U-space services could also be used as strategic mitigations.

Annex to ED Decision 2025/018/R                                                                 Page 30 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3

       Therefore, technical solutions that improve the electronic conspicuousness or detectability of
       the UAS are recommended.

S.4.4.2 Outcome
(a)    Identification of the risk of mid-air collision between the UA and a manned aircraft.
(b)    Documentation of information and references used to determine the iARC of the operational
       volume.

S.4.4.3 Task description
Operational volume
(a)    Identify the vertical limit of the operational volume:
       (i)     identify the vertical limit of the flight geography;
       (ii)    identify and document the contingency procedures in case the UA exceeds the height of
               the flight geography;
       (iii)   evaluate the maximum height the UA will travel above the limit of the flight geography
               when applying the contingency procedures before it enters again in the flight geography.
(b)    Check whether there are official airspace collision risk maps available. The competent authority
       or the ANSP may elect to directly map the airspace collision risks using airspace characterisation
       studies. These maps would directly show the initial/residual air risk class (ARC) for a particular
       airspace. If the competent authority, the ANSP or the U-space service provider provides an air
       collision risk map (static or dynamic), the UAS operator should use that service to determine
       the initial/residual ARC and go directly to Section S.4.5 ‘Application of strategic mitigations’ to
       reduce the iARC, provided that a further reduction is still possible.
(c)    If point (b) is not applicable, identify the iARC of the operational volume using the decision tree
       in Figure 6.




Annex to ED Decision 2025/018/R                                                              Page 31 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3




                                  Figure 6 — ARC assignment process

S.4.4.4 Instructions

Identification of the iARC
(a)    As seen in Figure 6, the airspace is categorised into 12 aggregated collision risk categories.
       These categories are characterised by altitude, controlled versus uncontrolled airspace,
       airport/heliport versus non-airport/non-heliport environments, airspace over urban versus
       rural areas, and lastly atypical (e.g. segregated) versus typical airspace. The categories
       correspond to the airspace encounter classes (AECs), which provide a further qualitative
       delineation of non-mitigated collision risk that is elaborated in Annex C to this AMC.
(b)    During a UAS operation, the operational volume may span many different airspace
       environments. The UAS operator should conduct an air risk assessment for the entire range of
       the operational volume. An example scenario of operations in multiple airspace environments
       is provided at the end of Annex C to this AMC.
(c)    The ARC is a qualitative classification of the rate at which a UAS would typically encounter a
       manned aircraft within that volume of airspace. The ARC is an initial assignment of the


Annex to ED Decision 2025/018/R                                                         Page 32 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3

          aggregated collision risk for the airspace before mitigations are applied. The actual collision risk
          for a specific local operational volume could be much different and can be addressed in the
          application of strategic mitigations to reduce the ARC section (this step is optional; see Step #5
          in Section S.4.5).
(d)       Although the non-mitigated risk captured by the initial ARC is conservative, there may be
          situations where that conservative assessment may not suffice. It is important that both the
          competent authority and the operator take great care to understand the operational volume
          and under what circumstances the definitions in Figure 6 could be invalidated. In some
          situations, the competent authority may raise the operational volume’s initial ARC to a level
          which is higher than that indicated in Figure 6. The ANSP should be consulted to assure that the
          assumptions related to the operational volume are accurate.
(e)       The competent authority may designate parts of its airspace as atypical. ARC-b, ARC-c and
          ARC-d generally define airspace with an increasing risk of collision between a UAS and manned
          aircraft.

Identification of the vertical limit of the operational volume
(a)       The vertical limit of the flight geography is the maximum height where the UA is planned to
          operate in normal conditions.
(b)       On top of the flight geography, the UAS operator should identify the extent of the contingency
          volume as the maximum height the UA will travel when applying the contingency procedures.

Atypical air environment
(a)       An atypical air environment (leading to ARC-a classification) is defined as airspace where the
          risk of collision between a UAS and manned aircraft is acceptably low without the application
          of any tactical mitigations. This is usually the case when it can be generally expected that no
          manned aircraft use the airspace volume that is intended for the operation.
(b)       Examples may include operation in reserved or restricted airspace (e.g. by means of a temporary
          segregated airspace), or operation at very low altitudes (including in close proximity to
          obstacles) in those areas where manned aircraft generally do not operate32.

S.4.5       Step #5 — Application of strategic mitigations to determine residual ARC (optional)

S.4.5.1 Introduction
(a)       The ARC is a qualitative classification of the rate at which a UA would encounter a manned
          aircraft in a given airspace environment. However, it is recognised that the operational volume
          may have a collision risk that differs from the iARC assigned.
(b)       If the UAS operator considers that the iARC assigned is too high for the condition in the local
          operational volume, then refer to Annex C to this AMC for the ARC reduction process.
(c)       If the UAS operator considers that the iARC assignment is correct for the condition in the local
          operational volume, then that iARC becomes the residual ARC.


32    Refer to definition I.19 ‘Authority’ in Annex I to AMC1 to Article 11.

Annex to ED Decision 2025/018/R                                                                  Page 33 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3

S.4.5.2 Outcome
(a)       Identification of the strategic mitigations applied to reduce the iARC of the operational volume.
(b)       Identification of the residual ARC.
(c)       Documentation of information and references used to support the application of strategic
          mitigations.

S.4.5.3 Task description
(a)       Identify the applicable strategic mitigations listed in Section 5 of Annex C to this AMC.
(b)       Identify the residual ARC of the operational volume following the process listed in Section 6 of
          Annex C to this AMC.
(c)       Refer to Chapter A.3 of Annex A to this AMC for further guidance on how to present the data
          that supplements the risk assessment to the authority.
(d)       If flying in VLOS, consider the additional guidance below.

S.4.5.4 Instructions

Application of strategic mitigations
For VLOS operations, or for BVLOS operations where the remote pilot is supported by one or multiple
airspace observers (located in a way that the UA is always at a VLOS distance from the remote pilot or
from one airspace observer that is able to scan the sky and communicate in real time with the remote
pilot informing them of possible other manned or unmanned aircraft flying in the area of operation33),
the initial ARC can be reduced by one class. In these conditions, the crew is assumed to have the ability
to assess other aircraft activity in the airspace concerned and therefore is able to lower the encounter
rate by applying this mitigation both before and during the operation. The mitigation cannot be used
to reduce the ARC to ARC-a. In ARC-d environments, agreement with ATC may be required34.

S.4.6       Step #6 — Tactical mitigation performance requirement (TMPR) and robustness levels

S.4.6.1 Introduction
Tactical mitigations are applied to mitigate any residual risk of a mid-air collision in order to achieve
the applicable airspace safety objective.

S.4.6.2 Outcome
(a)       Identification of the applicable TMPR and corresponding level of robustness.
(b)       Collection of information and references to be used to support compliance with the TMPR.

S.4.6.3 Task description
Identify whether flying in VLOS, BVLOS or BVLOS with AOs.



33    This type of operations is sometimes referred to as ‘EVLOS’.
34    This information will be reflected in a future version of Annex C.

Annex to ED Decision 2025/018/R                                                                Page 34 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

VLOS operations or BVLOS with airspace observers (AOs)
(a)    Develop and document a VLOS deconfliction scheme, in which it is explained which methods
       will be used for detection; and
(b)    Define the associated criteria applied for the decision to avoid incoming traffic. If the remote
       pilot relies on AOs for detection, the use of phraseology will have to be described as well.
BVLOS operations
(a)    Identify the applicable TMPR level deriving it from the residual ARC using Table 6.
(b)    Identify the applicable TMPR according to Section 5 of Annex D to this AMC.
Refer to Chapter A.3 of Annex A to this AMC for further guidance on how to present the data that
supplements the risk assessment to the authority.

           Residual ARC                       TMPR and corresponding level of robustness

               ARC-d                                                High

               ARC-c                                              Medium

               ARC-b                                                 Low

               ARC-a                                          No requirement

  Table 6 — Tactical mitigation performance requirements (TMPR) and assignment of the TMPR
                                       level of robustness

S.4.6.4 Instructions
Application of tactical mitigations
Tactical mitigations will take the form of either ‘see and avoid’ (i.e. operations in VLOS) or may require
a system which provides an alternate means of achieving the applicable airspace safety objective
(operation using a detect-and-avoid (DAA) system or multiple DAA systems). Annex D to AMC1
Article 11 provides the method for applying tactical mitigations.
VLOS operations or BVLOS with airspace observers (AOs)
(a)    VLOS operations or BVLOS with AOs are considered an acceptable tactical mitigation for
       collision risk for all ARC levels.
(b)    Notwithstanding the above, the operator is advised to consider additional means to increase
       situational awareness with regard to air traffic operating in the vicinity of the operational
       volume.
(c)    In the case of multiple flight segments, those segments flown in VLOS or in BVLOS with AOs do
       not have to meet the TMPR nor the TMPR robustness requirements, whereas those flown in
       BVLOS do need to meet the TMPR and the TMPR robustness requirements.
(d)    In general, the VLOS requirements are applicable when one or more airspace observers are
       employed. In this case, additional requirements beyond VLOS should be proposed, including the



Annex to ED Decision 2025/018/R                                                              Page 35 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

       definition of procedures and phraseology. The communication latency between the remote
       pilot and the airspace observer(s) should be less than 15 seconds.
(e)    For BVLOS operations with AOs, it is assumed that an airspace observer is not able to detect
       traffic beyond 2 NM (approximately 3,7 km). (Note that the 2 NM range is not a fixed value and
       may largely depend on atmospheric conditions, aircraft size, geometry, closing rate, etc.)
       Therefore, the operator may have to adjust the operation and/or the procedures accordingly.

Tactical mitigation performance requirement (TMPR) levels
(a)    High TMPR (ARC-d): The ARC-d level is assigned to airspace where either the manned aircraft
       encounter rate is high and/or the available strategic mitigations are low. Therefore, the
       resulting residual collision risk is high and the TMPR level is also high. In such airspace, the UA
       may be operating in integrated airspace (e.g. integrated with manned aircraft) and will have to
       comply with the operating rules and procedures applicable to that airspace, without reducing
       existing capacity, decreasing safety, negatively impacting current operations with manned
       aircraft, or increasing the risk to airspace users or persons and property on the ground. These
       are the same requirements as for the integration of comparable new and novel technologies in
       manned aviation. The performance level(s) of those tactical mitigations and/or the required
       variety of tactical mitigations is generally higher than for the other ARCs. If operations in this
       airspace are conducted more routinely, the competent authority is expected to require the
       operator to comply with the recognised DAA system standards (e.g. those developed by RTCA
       SC-228 and/or EUROCAE WG-105).
(b)    Medium TMPR (ARC-c): A medium TMPR will be required for operations in airspace with a
       moderate likelihood of encountering manned aircraft and/or where the available strategic
       mitigations have medium robustness. Operations with a medium TMPR will likely be supported
       by systems currently used in aviation to aid the remote pilot in detecting other manned aircraft
       or by systems which are designed to support aviation and which are built to a corresponding
       level of robustness. Traffic avoidance manoeuvres for a medium TMPR could be more advanced
       than for a low TMPR.
(c)    Low TMPR (ARC-b): A low TMPR will be required for operations in airspace where the likelihood
       of encountering a manned aircraft is low but not negligible and/or where strategic mitigations
       address most of the risk and the resulting residual collision risk is low. Operations with a low
       TMPR are supported by technologies that are designed to aid the remote pilot in detecting other
       traffic, but which may be built to lesser standards. For example, for operations below 500 ft
       AGL, the traffic avoidance manoeuvres are expected to mostly be based on a rapid descent to
       an altitude where manned aircraft are not expected to ever operate.
(d)    No TMPR (ARC-a): This is airspace where the manned aircraft encounter rate is expected to be
       extremely low and, therefore, there is no need for a TMPR. It is defined as airspace where the
       risk of collision between a UA and manned aircraft is acceptable without the addition of any
       tactical mitigation. An example of this may be UAS flight operations in some parts of northern
       Sweden where the manned aircraft density is so low that the airspace safety threshold could be
       met without any tactical mitigation.
(e)    Annex D to this AMC provides information on how to satisfy the TMPR based on the available
       tactical mitigations and the TMPR level of robustness.
Annex to ED Decision 2025/018/R                                                              Page 36 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

Guidance on airspace/operational requirements
(a)     Modifications to the initial and subsequent approvals may be required by the competent
        authority or the ANSP should safety and operational issues arise.
(b)     The operator and the competent authority need to be aware that ARCs are a generalised
        qualitative classification of collision risks. Local circumstances could invalidate the aircraft
        density assumptions of the SORA, for example with special events. It is important that both the
        competent authority and the operator fully understand the airspace and air traffic flows, and
        develop a system which can alert operators to changes to the airspace on a local level. This will
        allow the operator to safely address the increased risks associated with these events.
(c)     There are many airspace, operational and equipment requirements which have a direct impact
        on the collision risk of all aircraft that operate in a particular airspace volume. Some of these
        requirements are general and apply to all airspace volumes, while some are local and are
        required only for a particular airspace volume. The SORA cannot possibly cover all the possible
        requirements required by the competent authority for all conditions in which the operator may
        wish to operate. The UAS operator and the competent authority need to work closely together
        to define and address these additional requirements.
(d)     The SORA process should not be used to support UAS operations in a given airspace volume
        without the UAS being equipped with the required equipment for operations in that airspace
        volume (e.g. equipment required to ensure interoperability with other airspace users). In these
        cases, specific exemptions may be granted by the competent authority. Those exemptions are
        outside the scope of the SORA.
(e)     Operations in controlled airspace, in an airport/heliport environment or in a Transponder
        Mandatory Zone (TMZ) will likely require prior approval from the ANSP. The UAS operator
        should ensure that it coordinates with the relevant ANSP/authority prior to commencing
        operations in these environments.

S.4.7    Step #7 — Determination of the specific assurance and integrity level (SAIL)

S.4.7.1 Introduction
(a)     The SAIL parameter consolidates the ground and air risk analyses and drives the required
        activities.
(b)     The SAIL represents the level of confidence that the UAS operation will remain in control.

S.4.7.2 Outcome
Identification of the SAIL.

S.4.7.3 Task description
Identify the SAIL associated with the proposed operation deriving it from the final GRC and the residual
ARC using Table 7.




Annex to ED Decision 2025/018/R                                                             Page 37 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3


                                              SAIL determination
                                                      Residual ARC
                        Final GRC        a            b          c             d
                           ≤2            I            II           IV          VI
                            3            II           II           IV          VI
                            4           III           III          IV          VI
                            5           IV            IV           IV          VI
                            6            V            V            V           VI
                            7          VI           VI            VI            VI
                           >7        Operation classified in the ‘certified’ category

                                      Table 3 — SAIL determination

S.4.7.4 Instructions
(a)     The level of confidence that the UAS operation will remain in control is represented by the SAIL.
(b)     The SAIL is not quantitative but instead corresponds to:
        (i)     the level of the OSO robustness to be complied with (see Table 14);
        (ii)    the description of activities that might support compliance with the OSOs; and
        (iii)   the evidence that indicates the OSOs have been satisfied.

S.4.8     Step #8 — Determination of the containment requirements

S.4.8.1 Introduction
(a)     The containment requirements ensure that the target level of safety can be met for both ground
        and air risk in the adjacent ground area.
(b)     The containment requirements are derived from the difference between the final ground risk
        level in the operational volume plus the ground risk buffer and the final ground risk level in the
        adjacent ground area.
(c)     There are three possible levels of robustness for containment: ‘low’, ‘medium’ and ‘high’,
        each with a set of safety requirements described in Annex E to this AMC.

S.4.8.2 Outcome
(a)     A set of operational limitations for the population in the adjacent ground area.
(b)     A derived level of robustness for containment.

S.4.8.3 Task description
(a)     If the UA has a take-off mass of less than 250 g, apply low containment with no required
        operational limitations for the population in the adjacent ground area and go to Step #9.
        Otherwise, apply point (b).
(b)     Determine the size and the population characteristics of the adjacent ground area:



Annex to ED Decision 2025/018/R                                                              Page 38 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3

         (i)     calculate the size of the adjacent ground area for the operation; the lateral outer limit of
                 the adjacent ground area is calculated from the operational volume as the distance flown
                 by the UA in 3 minutes at maximum speed:
                 (A)     if the distance is less than 5 km, use 5 km;
                 (B)     if the distance is between 5 and 35 km, use the distance calculated;
                 (C)     if the distance is greater than 35 km, use 35 km;
         (ii)    calculate the average population density between the outer limit of the ground risk buffer
                 and the outer limit of the adjacent ground area;
         (iii)   develop procedures to assess the potential presence of outdoor assemblies of people,
                 during the time when the flight takes place, within 1 km of the outer limit of the
                 operational volume.
(c)      Determine a set of operational limitations appropriate for the UAS operation using the columns
         in Tables 8 to 13.
         (i)     Choose an operational limitation for the acceptable average population density in the
                 established adjacent ground area.
         (ii)    Choose an operational limitation for the acceptable size of assemblies of people within
                 1 km surrounding the operational volume.
(d)      Use Tables 8 to 13 to identify the required containment robustness level based on the
         characteristic dimension of the UA and the SAIL of the operation, considering the most stringent
         between the value of the average population density and the outdoor assembly of people.

                                           1 m UA (< 25 m/s)
                  Sheltering assumed applicable for the UA in the adjacent ground area35
      Average population density                                                         < 50 000
                                                     No upper limit
                allowed                                                                people/km2
      Outdoor assemblies allowed
                                                              Assemblies of 40k to    Assemblies of
     within 1 km of the operational          > 400k
                                                                      400k                 < 40k
                 volume
                   SAIL
                  I & II                      High                  Medium                  Low
                    III                     Medium                    Low                   Low
               IV, V -& VI                    Low                     Low                   Low
          Table 8 — Containment requirements for a UA up to 1 m UA with shelter assumption




35
      Refer to Table B.2 ‘Level of integrity assessment criteria for M1(A) mitigation’ of Annex B to AMC1 Article 11 for guidance
      on how to evaluate the applicability of the sheltering effect.

Annex to ED Decision 2025/018/R                                                                                  Page 39 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3


                                         3 m UA (< 35 m/s)
                 Shelter assumed applicable for the UA in the adjacent ground area32
  Average population density                                            < 50 000         < 5 000
                                           No upper limit                        2
            allowed                                                   people/km        people/km2
  Outdoor assemblies allowed
                                                    Assemblies of
 within 1 km of the operational       > 400k                           Assemblies of < 40k people
                                                     40k to 400k
            volume
              SAIL
              I & II               Out of scope          High           Medium             Low
                III                Out of scope       Medium              Low              Low
                IV                   Medium              Low              Low              Low
             V & VI                    Low               Low              Low              Low
          Table 9 — Containment requirements for a UA up to 3 m with shelter assumption

                                         3 m UA (< 35 m/s)
                Shelter assumed not applicable for the UA in the adjacent ground area
     Average population                               < 50 000          < 5 000           < 500
                               No upper limit
      density allowed                               people/km2        people/km2       people/km2
     Outdoor assemblies
                                                   Assemblies of
 allowed within 1 km of the       > 400k                               Assemblies of < 40k people
                                                    40k to 400k
     operational volume
            SAIL
            I & II              Out of scope            High            Medium             Low
              III               Out of scope          Medium              Low              Low
              IV                  Medium                Low               Low              Low
           V & VI                   Low                 Low               Low              Low
       Table 10 — Containment requirements for a UA up to 3 m without shelter assumption

                                         8 m UA (< 75 m/s)
               Sheltering assumed not applicable for the UA in the adjacent ground area
     Average population           No upper      < 50 000         < 5 000       < 500          < 50
      density allowed               limit      people/km2      people/km2    people/km2    people/km2
     Outdoor assemblies                  Assemblies
 allowed within 1 km of the   > 400k      of 40k to                       Assemblies of < 40k
     operational volume                     400k
            SAIL
            I & II          Out of scope Out of scope            High          Medium           Low
              III           Out of scope Out of scope           Medium          Low             Low
              IV            Out of scope Medium                  Low            Low             Low
               V             Medium          Low                 Low            Low             Low
              VI                Low          Low                 Low            Low             Low
                       Table 11 — Containment requirements for a UA up to 8 m




Annex to ED Decision 2025/018/R                                                             Page 40 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3


                                        20 m UA (< 120 m/s)
               Sheltering assumed not applicable for the UA in the adjacent ground area
      Average population           No upper       < 50 000        < 5 000        < 500          < 50
       density allowed               limit       people/km2     people/km2     people/km2    people/km2
     Outdoor assemblies                          Assemblies
 allowed within 1 km of the         > 400k        of 40k to                 Assemblies of < 40k
     operational volume                             400k
            SAIL
            I & II                Out of scope Out of scope Out of scope          High            Medium
              III                 Out of scope Out of scope Out of scope         Medium            Low
              IV                  Out of scope Out of scope  Medium               Low              Low
               V                  Out of scope Medium           Low               Low              Low
              VI                   Medium          Low          Low               Low              Low
                       Table 12 — Containment requirements for a UA up to 20 m

                                       < 40 m UA (< 200 m/s)
               Sheltering assumed not applicable for the UA in the adjacent ground area
 Average population density         No upper       < 50 000    < 5 000            < 500       < 50
          allowed                     limit       people/km2 people/km2         people/km2 people/km2
      Outdoor assemblies                          Assemblies
  allowed within 1 km of the         > 400k        of 40k to                Assemblies of < 40k
      operational volume                             400k
             SAIL
             I & II               Out of scope Out of scope Out of scope Out of scope              High
               III                Out of scope Out of scope Out of scope Out of scope             Medium
               IV                 Out of scope Out of scope Out of scope  Medium                   Low
                V                 Out of scope Out of scope Medium           Low                   Low
               VI                 Out of scope Medium           Low          Low                   Low
                       Table 13 — Containment requirements for a UA up to 40 m

(e)    Ensure the operation complies with the containment requirements listed in Annex E Section 4.

S.4.8.4 Instructions
Refer to Chapter A.3 of Annex A to this AMC for further guidance on how to present the data that
supplements the risk assessment to the competent authority.

Adjacent ground area
(a)    The adjacent ground area represents the ground area adjacent to the ground risk buffer where
       it is reasonably expected that a UA may crash after a loss-of-control situation resulting in a fly-
       away.
(b)    The operator is not approved to plan flights in this area, and it should only be overflown
       unintentionally in the event of a loss of control that results in a fly-away.




Annex to ED Decision 2025/018/R                                                               Page 41 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3

(c)      As regards the situation in point (b), the direction and duration of the fly-away is assumed to be
         random, thus the average population density of the adjacent ground area is used, instead of the
         maximum as is done in Step #2.
(d)      Conservative simplifications for calculating the average population density may be used by the
         operator when compliance with the operational limitations can be assured.

Calculating the size of the adjacent ground area
The diagram below in Figure 7 depicts how to determine the size of the adjacent ground area.




                              Figure 7 — Lateral limits — Adjacent ground area

If the ground risk buffer is larger than the adjacent ground area, then the assessment of the adjacent
ground area is not required.

Adjacent ground area containment requirements
(a)      When using Tables 8 to 13 to identify the required containment robustness level of the
         operation:
         (i)     select the correct table based on the maximum characteristic dimensions of the UA used
                 in Step #2;
                 (A)   for a 3 m UA determine whether sheltering can be applied in the adjacent ground
                       area, using similar considerations applied in Step #3;
                 (B)   if sheltering applies for a UA greater than 3 m, the operator may use Annex F
                       Edition 2.536 to apply the credit and determine the appropriate containment
                       requirements;
         (ii)    identify the correct row based on the SAIL found in Step #7;
         (iii)   identify the appropriate column to derive the containment level of robustness based on
                 the adjacent ground area population density;




36    http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf

Annex to ED Decision 2025/018/R                                                                      Page 42 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

       (iv)   if the results are ‘out of scope’, the operation cannot be conducted in the ‘specific’
              category; in this case, adjusting the location of the operation or an increase of the SAIL of
              the operation could be considered.
(b)    Example: An operation uses a SAIL III 2.5 m UA with a maximum speed of 30 m/s, sheltering is
       applicable, the outer limit of the adjacent ground area is 5.4 km from the boundary of the
       operational volume. An assessment of the adjacent ground area shows no large outdoor
       assemblies of people within 1 km and such area spans mostly rural and suburban areas,
       expecting an average population density between 1–4k people/km2. This results in low
       containment requirements. If the UAS operator decides to use a UA with low containment, the
       operator should document the operational limitations for the low containment SAIL III UA:
       (i)    no assemblies of people > 40k within 1 km of the operational volume;
       (ii)   the adjacent ground area (5.4 km from the operational volume) average population
              density should not exceed 50 000 people/km2.

Operational limitations regarding adjacent ground area
(a)    The UAS operator should define operational limitations that have to be adhered to when
       planning the operational volume for a flight operation.
(b)    The UAS operator should have a procedure to identify and take into account scheduled outdoor
       assemblies of people in excess of the operational limitations within 1 km of the outer limit of
       the operational volume. The values for the size of assemblies of people are to be understood as
       rough order of magnitude guidelines since measuring the actual values is not practical.
(c)    If the ground risk buffer size exceeds 1 km, the adjacent ground area consideration for all
       assemblies of people is not applicable.

Inclusion of the containment feedback loop into the definition of the ground risk buffer and
operational volume
(a)    If the UAS operator determines that a medium or high robustness containment is required for
       its operational objectives, there might be a recursive effect. If a high level of containment is
       required, the calculation of the ground risk buffer size may need to be repeated using the
       requirements defined in criterion #3 of Chapter E.4 of Annex E to this AMC. It is possible that
       this results in a bigger ground risk buffer size compared to the one defined by the UAS operator
       in Step #1.
(b)    If this is the case, the UAS operator needs to go back to Step #2 and re-evaluate the GRC.
(c)    Alternatively, the UAS operator may choose to reduce the size of the operational volume
       described in Step #1 to allow for a greater ground risk buffer.

Containment requirements for adjacent airspace
By containing the flight within the operational volume and assuring the immediate cessation of the
flight in case of an unlikely breach of the operational volume, low robustness containment is generally
considered sufficient to allow operations to be conducted adjacent to all airspace volumes.



Annex to ED Decision 2025/018/R                                                               Page 43 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3

  S.4.9      Step #9 — Identification of the operational safety objectives (OSOs)

  S.4.9.1 Introduction
  This step of the SORA process is to map the operation’s SAIL score to the required levels of robustness
  of the OSOs.

  S.4.9.2 Outcome
  (a) Identification of the required robustness levels of the individual OSOs.
  (b) Collection of information and references to be used to show compliance with the OSO
      requirements.

  S.4.9.3 Task description
  (a)      Identify the level of robustness of each OSO, deriving it from the SAIL of the proposed operation
           using Table 14.

                                                                                                      Dependencies
OSO ID                                                                       SAIL         (Criteria references as per Annex E)
                                                                                                        Training
                                                                  I     II    III IV V VI Operator                    Designer
                                                                                                      organisation
        Ensure that the UAS operator is a competent
OSO #01                                             NR L M H H H                                  x
        and/or proven organisation
        UAS designed and produced by a competent
OSO #02                                             NR NR L M H H                                                        x37
        and/or proven organisation
                                                                                           Crit. #2
OSO #03 UAS maintenance                                           L     L     M MH H                                  Crit. #1
                                                                                           Crit. #3
        UAS components essential to safe
OSO #04 operations are designed to an airworthiness NR NR NR M H H                                                        x
        design standard
        UAS is designed considering system safety
OSO #05                                             NR NR L M H H                                                         x
        and reliability
        C3 link characteristics (e.g. performance
OSO #06 spectrum use) are appropriate for the UAS NR L L M H H Crit. #1                                               Crit. #2
        operation

OSO #07 Conformity check of the UAS configuration                 L     L     M MH H              x

                                                                                      Crit. #2
           Operational procedures             are     defined,
OSO #08                                                           L    M      H H H H Crit. #3                        Crit. #1
           validated and adhered to
                                                                                      Crit. #4
OSO #09 Remote crew trained and current             L                   L     M MH H     x                 x
        External services supporting UAS operations
OSO #13                                             L                   L     M H H H             x
        are adequate for the UAS operation
                                                                                     Crit. #1
OSO #16 Multi-crew coordination                                   L     L     M MH H                   Crit. #2
                                                                                     Crit. #3
OSO #17 Remote crew is fit to operate                             L     L     M MH H    x



  37    Annex E of this AMC includes requirements for both design and production organisations.

  Annex to ED Decision 2025/018/R                                                                              Page 44 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3


          Automatic protection of the flight envelope
OSO #18                                               NR NR L M H H                                        x
          from human errors

OSO #19 Safe recovery from human error                    NR NR L M M H                                    x

        A human factors evaluation has been
OSO #20 performed and the HMI found appropriate NR L L M M H                                               x
        for the intended UAS operation
        Environmental     conditions   for  safe
OSO #23                                           L  L M MH H                                              x
        operations defined and measurable
        UAS designed and qualified to operate in
OSO #24                                          NR NR M H H H                                             x
        adverse environmental conditions
                       Table 14 — Recommended operational safety objectives (OSOs)
  (b)     Refer to Annex E to this AMC for the integrity and assurance requirements of each OSO based
          on its level of robustness:
          (i)     identify the requirements for procedures and document them accordingly;
          (ii)    identify the technical requirements for the UAS and document them accordingly;
          (iii)   identify the training requirements for the personnel essential for the safety of the
                  operation and document them accordingly.
   (c) For OSO #5, see further guidance in Annex E to this AMC regarding UAS designs that employ novel
       or complex features for which very limited operational experience is available and are intended
       to be operated in SAIL II.

  S.4.9.4. Instructions
  (a)     Table 14 is a consolidated list of common OSOs that historically have been used to ensure safe
          UAS operations. It represents the gained experience of many experts and is, therefore, a solid
          starting point to determine the required safety objectives for a specific operation.
  (b)      While the operator is the organisation responsible for showing compliance with all OSOs, some
          of the evidence may be developed by other organisations such as the UAS designer or the
          training organisation, as identified in Table 14.
  (c)     Table 14 indicates the corresponding OSOs. In this table:
          (i)     ‘NR’ stands for ‘not required’ to show compliance to the competent authority; however,
                  the applicant is encouraged to consider the operational safety objective at a low integrity
                  level;
          (ii)    ‘L’ stands for ‘low’ robustness;
          (iii)   ‘M’ stands for ‘medium’ robustness;
          (iv)    ‘H’ stands for ‘high’ robustness.

  S.4.10 Step #10 — Comprehensive safety portfolio (CSP)

  S.4.10.1 Introduction
  (a)     The final step of the SORA involves the compilation of the CSP.

  Annex to ED Decision 2025/018/R                                                               Page 45 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3

(b)    The CSP is a structured argument using the SORA process that is supported by a body of
       evidence which provides a robust safety case. This demonstrates that the proposed operation
       has been assessed correctly and meets its SORA objectives.

S.4.10.2 Outcome
(a)    A completed CSP should be provided to the competent authority for the application for the
       issue of an operational authorisation.
(b)    By documenting all the elements of the SORA, the competent authority can assess a
       standardised document suite that provides assurance that the SORA process has been
       completed correctly and the operation can be conducted safely.

S.4.10.3 Task description
(a)    Finalise and present all the documentation that needs to be included in the CSP. This should
       include the following:
       (i)     The finalised detailed operational description from Step #1 that details the proposed
               operation(s), providing the air and ground risk information necessary to validate the
               safety claims within the proposed operational context.
       (ii)    All safety claims, and their robustness, made through Steps #2 (iGRC), #3 (M1(A), M1(B),
               M1(C), M2), #4 (initial ARC), #5 (Strategic Mitigations for Air Risk), updated (if required)
               from Phase 1 to reflect the finalised operation.
       (iii)   All derived requirements based on the safety claims; the final GRC, the residual ARC,
               TMPRs, the OSOs associated with the SAIL, and the containment requirements.
       (iv)    Compliance evidence, which comprises of data, facts and information that provide the
               necessary justification for each of the safety claims and derived requirements made
               through the SORA process at the robustness level required. The CSP covers operational,
               technical, personnel and organisational compliance evidence.
       (v)     The necessary linkages and references between documents that ensure the CSP makes a
               justified safety case that demonstrates the operation has satisfied all required SORA
               safety claims and derived requirements.
       (vi)    It is expected that a finalised compliance matrix (based on the initial compliance matrix,
               if developed in Phase 1) will be used to map the safety claims and derived requirements
               to the compliance evidence.
(b)    Refer to Annex A to this AMC for more guidance on how to structure documentation as part of
       the CSP.

S.4.10.4 Instructions
(a)    The UAS operator should only put information into the CSP as required by the items mentioned
       in paragraph S.4.10.3. If a requirement has a low robustness (refer to Section S.2.4), it is mostly
       sufficient to self-declare the compliance by a statement in the CSP. The SORA requirements for
       self-declaration in no way prevent the competent authority from requesting further documents
       to validate the declaration, if considered necessary for the given operation.


Annex to ED Decision 2025/018/R                                                               Page 46 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

(b)    The CSP is expected to be a collection of documents specific to the UAS operation(s). It can be
       modularised and can consist of multiple documents and subsections to accommodate the need
       to perform the UAS operation(s).
(c)    Appropriate references and version/configuration control apply to all documents in the CSP,
       including subsections and other documents. Chapter A4 of Annex A to this AMC provides a
       template that could be used for developing the CSP that is in line with the requirements of this
       AMC. The competent authority may require a separate process for any change to be made. The
       management of any change should follow the relevant competent authority’s requirements.
(d)    A completed and valid CSP forms the basis for the issue of an operational authorisation.
(e)    If the operator uses external service(s), reference(s) to the service level agreement(s) (SLA(s))
       providing a delineation of responsibilities between the service provider(s) and the operator
       should be included in the CSP. It should also detail the functionality, limitations and
       performance of the external service(s).




Annex to ED Decision 2025/018/R                                                            Page 47 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


Annex A to AMC1 Article 11
GUIDELINES ON COLLECTING AND PRESENTING INFORMATION ON SYSTEMS AND OPERATIONS
REGARDING UAS OPERATIONS CONDUCTED IN THE ‘SPECIFIC’ CATEGORY
The purpose of this Annex is to provide guidance to UAS operators for collecting and presenting
evidence and data required when compiling an application to obtain operational authorisation for UAS
operations in the ‘specific’ category.
This document does not replace civil regulations but provides recommendations and guidance as to
how UAS operators can comply with those regulations using the SORA process.
This document is composed of the following five chapters:

—      A.1: Key principles for completing the application documents for UAS operations to be
       conducted in the ‘specific’ category
       It explains the different documents and how to use them to compile an application.

—      A.2: SORA risk assessment template
       It is intended to support UAS operators in compiling all the information necessary to perform a
       risk assessment.

—      A.3: Structure of the operations manual
       It provides an operations manual model structure for UAS operators to follow in order to
       present their operations manual in an appropriate manner.

—      A.4: Compliance matrix
       It provides a template for UAS operators on how to present the reference between the SORA-
       driven requirements and the operations manual.

—      A.5: How to document and present a flight area
       It contains guidance for UAS operators on how to create and include a flight area into the
       operations manual.

A.1 Key principles for completing the application documents for UAS operations to be conducted in
the ‘specific’ category

How does an application generally work?
The operations manual serves as the basis for an operational authorisation for UAS operations to be
conducted in the ‘specific’ category. When the competent authority issues the operational
authorisation, it accepts the related operations manual.

General workflow
Before starting collecting information and describing procedures, the UAS operator should outline a
preliminary operational concept (refer to Section S.4.1 of this AMC). This preliminary operational


Annex to ED Decision 2025/018/R                                                          Page 48 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

concept ensures that the UAS operator can effectively explore all available options, and select the
most suitable approach for its specific needs.
Key considerations for this initial plan include the following:
—      the intended flight location(s);
—      the maximum operational flight altitude and speed;
—      the flight mode: either VLOS or BVLOS with or without AOs;
—      the type of UAS to be used;
—      environmental limitations (time of day, weather).
In the next step, the UAS operator assesses the risk for the operation and develops a high-level
overview of the SORA requirements. For this, the UAS operator should apply the requirements of
Section A.2 and follow each step of the SORA process.
When SORA phase 1 (see Figure A.1) is completed, it is considered best practice for a UAS operator to
liaise with the competent authority before moving to the data collection and procedure description
(refer to Section S.3.3 of this AMC) to share its preliminary operational information and initial risk
assessment. The competent authority and the UAS operator evaluate the alignment of the risk
assessment with the operational information and check the correct application of the SORA steps. The
competent authority may provide feedback to the UAS operator on its expectations on how to achieve
an operational authorisation considering the resulting SAIL.
Once the risk assessment (i.e. the outcome of SORA Phase 1) has been validated and the UAS operator
has secured confirmation from the competent authority, the next step involves identifying the specific
requirements that arise from the risk assessment (i.e. conduct SORA phase 2 and develop the evidence
in support of compliance with the applicable OSOs, mitigations and containment). Following this
identification, the UAS operator should then collect the relevant evidence and information, as well as
describe the procedures that will be implemented. The UAS operator should ensure that all integrity
and corresponding assurance requirements are met. These can be found in Annexes B to E to this
AMC. It is recommended to use the operations manual structure provided in Chapter A.3 for this
purpose.
The UAS operator should use the template provided in Chapter A.4 (Compliance matrix) once all
procedures are described and evidence is collected. This is done by providing the corresponding
reference to the integrity and/or assurance evidence for each requirement. This document serves as
a checklist for the UAS operator to review before submitting an application. The competent authority
may use this document as a reference to assist the review process.
The competent authority reviews the application in accordance with the requirements arising from
the risk assessment and the respective SAIL. In this process, the implementation of all technical and
operational requirements is checked based on the descriptions in the operations manual, or other
associated documents as required. The competent authority has the option to request the UAS
operator to revise the documents and resubmit them, or ask for additional supporting documentation.
For the UAS operator to address the additional requests effectively, the competent authority may also
provide guidance on how the UAS operator can proceed to close any outstanding issues.



Annex to ED Decision 2025/018/R                                                          Page 49 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3

Figure A.1 graphically depicts the process described above and thus serves as an additional illustration
of the general workflow.

                       UAS operator
                Prepares general operational
                        information


                                                        A.2




                                                                                                                        PHASE 1 — Identification of requirements
                        UAS operator
      Performs an initial risk assessment and identifies
                   specific requirements
                       (SORA steps 2-9)
                                                     optional
                        UAS operator
          Consults the competent authority on risk
            assessment and intended operation




         No
                        Confirmation
                         received?
                              ?

                        Yes
                                         A.2 A.3 A.4
                       UAS operator
       Prepares required documents according to risk
            assessment and intended operation
                      (SORA step #10)


                       UAS operator



                                                                                                                         PHASE 2 — Compliance with requirements
                                                                             Competent authority
               Submits the application with all
                                                                            Assesses the application
                  supporting documents



                                                                          Competent authority
                                                                 Prepares feedback for the UAS operator




                      Competent authority                        No
            Informs the UAS operator on the reason(s)                          All requirements
                   for rejecting the application                                     met?

                                                                                Yes


                                                                           Competent authority
                                                                   Issues the operational authorisation

   Figure A.1 — Recommended level of detail and use of supporting documents and references

Annex to ED Decision 2025/018/R                                                                        Page 50 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

The operations manual and its associated annexes should enable the UAS operator to describe how
to conduct the operation safely for the benefit of its staff. It should include the identification of the
flight area, all normal, contingency and emergency procedures and additional information derived by
the compliance with the required OSOs, mitigations and containment requirements.
Supporting documents serving as evidence for the compliance with the required OSOs, mitigations
and containment requirements may be referenced in the operations manual and can be linked in the
compliance matrix (see Section A4) and be included in a separate document. Evidence developed in
support of requirements having a low level of robustness (related to the OSOs, based on the SAIL of
the operation or to the level of mitigation and or to the containment chosen by the UAS operator)
may be kept internal to the UAS operator’s organisation. The same applies in case the level of
robustness of the requirements is medium and the UAS operators decided to use AMC published by
EASA. The competent authority may require those evidence during the oversight audit or anytime. In
case the level of robustness of the requirements is high or it is medium and the UAS operators decided
not to use AMC published by EASA, then the evidence should be provided with the application of the
operational authorisation.
The competent authority may request further documents if considered necessary by the competent
for the given operation.

Document set-up for additional flight areas, UAS or UAS operations
When a UAS operator seeks to expand its approved operations manual(s) to include a new flight area,
a UAS or a UAS operation, the primary question is whether the underlying risk assessment covers
these additions. If it does, the new information can be incorporated into existing parts (see
Chapter A.3 of this Annex — Part A to T) of the operations manual(s). Otherwise, it is considered best
practice to establish new parts for such information.
When dealing with complex UAS operations (e.g. multiple types of UAS operations and multiple UAS
employed), the UAS operator may find it useful to use a different structure of the operations manual
compared to that proposed by this Annex. In this case, it is recommended to discuss the proposed
manual’s structure with the competent authority to ensure it meets both national and industry
standards.
Operation-specific details should typically be organised into separate parts for clarity during approval
and ease of use. Conversely, general or related information can be consolidated into a common
segment. An example would be adding an additional UAS with the same characteristic dimensions,




Annex to ED Decision 2025/018/R                                                             Page 51 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

but a different set of procedures. This could be added to existing Part B; for illustration purposes, see
Figure A.2.




         Figure A.2 — Common scenarios and how they may impact the operations manual




Annex to ED Decision 2025/018/R                                                             Page 52 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3


A.2 SORA risk assessment template
Introduction
This chapter serves as a guide to assist UAS operators in compiling all the necessary information for
conducting a risk assessment. UAS operators should submit an application for an operational
authorisation using the form provided in AMC1 UAS.SPEC.030(2). By providing this questionnaire-style
template for documenting the risk assessment, UAS operators are encouraged to focus on the
essential information required and to avoid unnecessary lengthy explanations about their operational
procedures.
The ‘remarks’ section is optional and is designed for UAS operators to provide additional information
when needed, helping to prevent misunderstandings. At this stage, no evidence is required as the
requirements are determined by the risk analysis process.
Once the application form is completed, both the UAS operator and the competent authority will have
all the necessary information to complete Phase 1 assessment (for reference, see Figure A.1).
Note that for Phase 1 the fields 2.9 (OM references) and 2.10 (compliance evidence file reference) of
the application form (AMC1 UAS.SPEC.030(2)) may not be filled in yet.
In situations involving the use of multiple UA or flight areas with varying ground or air risk classes, it
is advisable to consult with the competent authority. This practice helps ensuring alignment with
competent authority expectations and adherence to national standards. In certain cases, it may be
possible to include multiple UA or flight areas into one form.
Evidence should not be included in the application form. Instead, it should be incorporated into the
operations manual (Chapter A.3 ‘Structure of the operations manual’) and referenced in the CSP
(Chapter A.4 ‘Compliance matrix’).




Annex to ED Decision 2025/018/R                                                              Page 53 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3

A.3 Structure of the operations manual
Introduction
The intention of this chapter is to provide a standardised framework for documenting essential
information that relates to a specific operation. It serves only as an example structure for UAS
operators to create a comprehensive document that outlines the procedures and relevant details
necessary for the safe and efficient execution of a UAS operation38.
In the example structure, the operations manual is divided into logical subject parts, which in turn
offer a structure as regards where to include specific topics that are crucial for creating a standardised
manual for the safe operation of UAS.
While the structure is not inherently mandatory, the topics it contains should be incorporated into the
operations manual as needed for the specific operation(s) to provide the relevant information and
evidence required for the safe operation of UAS. It is advisable to adhere to the provided structure,
as it aligns with the expectations and practices of most competent authorities. An example of an
operations manual may be found on the EASA website39.
In general, any information that does not have direct operational relevance to the UAS operator or its
staff should be placed in the relevant annex to ensure the document remains concise and reader-
friendly.
The main purpose of this structure is the following:
1.      Standardisation: It ensures that all critical aspects of the UAS operation are documented
        consistently, following applicable industry standards and regulations, and best practices.
2.      Compliance: It helps operators meet regulatory requirements by specifying the information and
        procedures needed to obtain necessary approvals and certification.
3.      Clarity: It provides a clear and organised structure for conveying operational procedures, safety
        protocols and other essential information, thus reducing the risk of misunderstandings and
        errors.
4.      Safety: It emphasises safety measures, emergency procedures and risk-mitigation strategies to
        enhance the overall safety during the operation.
5.      Efficiency: It streamlines the process of creating an operations manual by providing predefined
        sections and guidelines, helping UAS operators save time and effort.
6.      Consistency: It ensures that all UAS operators that are involved in the operation of the same
        UAS type follow the same documented procedures, promoting uniformity and reducing the
        potential for confusion.
7.      Reference: It serves as a valuable reference document for UAS operators, remote crew
        members, competent authorities and other stakeholders involved in, or overseeing, the UAS
        operation.


38   An example of an operations manual and modules providing dedicated procedures may be found on the EASA website
     at https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-
     drones/predefined-risk-assessment-pdra#group-easa-downloads.
39   https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-drones#group-
     easa-downloads

Annex to ED Decision 2025/018/R                                                                       Page 54 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3

8.      Documentation: It aids in the systematic recording of operational details, making it easier to
        track changes, updates, and compliance with evolving regulatory requirements.


Recommended structure for the operations manual

Cover page
Document control
Other applicable documents
Purpose and scope of this document
List of contents
List of definitions and abbreviations
1         Part A — General Part
     1.1 Opening statement
     1.2 Security and privacy statement
     1.3 Environmental statement
     1.4 The operating organisation
       1.4.1   Structure / organisation chart
       1.4.2   Duties and responsibilities of the personal
     1.5 Change management
     1.6 Retention periods
     1.7 Document control
     1.8 Requirements and qualifications for personnel
       1.8.1   Remote pilot
       1.8.2   Maintenance personnel
       1.8.3   Ground staff
       1.8.4   Training, examination and supervision personnel
     1.9 Crew member is ‘fit for the operation’
       1.9.1   Preventive health care
       1.9.2   Duty hours and rest periods
2         Procedures (Part B)
     2.1 Multi-crew coordination
     2.2 Flight planning
       2.2.1   Use of up-to-date information
       2.2.2   Geographical zones
     2.3 External services and systems
       2.3.1   Services
       2.3.2   Systems
     2.4 Procedures for obtaining information about and evaluating weather conditions

Annex to ED Decision 2025/018/R                                                          Page 55 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

    2.5 Procedures for responding to unexpected adverse weather conditions
    2.6 Procedures for tactical mitigation performance requirements (TMPRs)
    2.7 Occurrence reporting
      2.7.1   What must be reported?
      2.7.2   Who must report?
      2.7.3   What must be observed after reporting?
    2.8 Procedures specifically for UAS 1
      2.8.1   Normal procedures
      2.8.2   Contingency procedures
      2.8.3   Emergency procedures
    2.9 Procedures specifically for UAS 2
      2.9.1   Normal procedures
      2.9.2   Contingency procedures
      2.9.3   Emergency procedures
3        Part C — Flight areas
    3.1 General operational limitations
      3.1.1   Environmental conditions
      3.1.2   Technical operational limitations
    3.2 Flight area 1
      3.2.1   Description
      3.2.2   Calculation of the contingency volume (CV) / ground risk buffer (GRB)
      3.2.3   Specific procedures for flight area 1
      3.2.4   Emergency response plan (ERP) — Local information
    3.3 Flight area 2
      3.3.1   Description
      3.3.2   Calculation of the contingency volume (CV) / ground risk buffer (GRB)
      3.3.3   Specific procedures for flight are 2
      3.3.4   Emergency response plan (ERP) — Local information
    3.4 Flight area 3
      3.4.1   Description
      3.4.2   Calculation of the contingency volume (CV) / ground risk buffer (GRB)
      3.4.3   Specific procedures for flight area 3
      3.4.4   Emergency response plan (ERP) — Local information
4        Part D — Training
5        Part E — Emergency response plan (ERP)
    5.1 General
    5.2 Creation of the ERP
    5.3 ERP template
    5.4 Preparation and briefing
    5.5 Reporting procedures and obligations after an emergency

Annex to ED Decision 2025/018/R                                                       Page 56 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

6        Part T — Technical part of the UAS
    6.1 UAS 1 [Model/Type]
      6.1.1 Description
      6.1.2 Image/graphic
      6.1.3 C3 link
      6.1.4 Parachute (M2)
      6.1.5 TMPRs
      6.1.6 Containment
      6.1.7 Human–machine interface (HMI)
      6.1.8 Payload
      6.1.9 Automatic protection of the flight envelope
      6.1.10 Designed and qualified to operate in adverse environmental conditions
    6.2 UAS 2 [Model/Type]
      6.2.1 Description
      6.2.2 Image/graphic
      6.2.3 C3 link
      6.2.4 Parachute (M2)
      6.2.5 TMPRs
      6.2.6 Containment
      6.2.7 Human–machine interface (HMI)
      6.2.8 Payload
      6.2.9 Automatic protection of the flight envelope
      6.2.10 Designed and qualified to operate in adverse environmental conditions
7        Part M — Maintenance
    7.1 General
    7.2 Software updates
    7.3 Maintenance of UAS 1 [Model/Type]
    7.4 Maintenance of UAS 2 [Model/Type]
8        Annex
    8.1 Evidence
      8.1.1 Organisational evidence
      8.1.1.1 Organisational operating certificate
      8.1.1.2 Maintenance programme / organisation certificate
      8.1.2 Operational evidence
      8.1.2.1 Operational agreements (e.g. with ATC)
      8.1.2.2 M1
      8.1.2.3 Flight tests
      8.1.2.4 Performance of external services and systems
      8.1.3 Technical evidence
      8.1.3.1 Design (DVR, TC)
      8.1.3.2 M2
      8.1.3.3 Manufacturer competence
    8.2 Printed forms

Annex to ED Decision 2025/018/R                                                      Page 57 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

     8.2.1    List of maintenance personnel
     8.2.2    List of personnel authorised to conduct pre-flight and post-flight inspections
     8.2.3    List of the training/experience level of personnel
     8.2.4    List of authorised remote pilots
     8.2.5    List of personnel trained in the emergency response plan (ERP)
     8.2.6    Operator flight logbook
     8.2.7    Technical logbook
  8.3 Checklists
     8.3.1    ERP template
     8.3.2    Pre-flight inspection — Checklist
     8.3.3    Post-flight inspection — Checklist
  8.4 Manuals
     8.4.1    Maintenance manual for UAS 1
     8.4.2    Maintenance manual for UAS 1




Annex to ED Decision 2025/018/R                                                            Page 58 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

Reference table for the requirements specified in the annexes to AMC1 (SORA)
The following table offers a comprehensive overview of the suitable locations within the operations
manual where the requirements specified in the annexes to AMC1 (SORA) can be sensibly
incorporated.

                  Integrity (I) /
OSOs ↓                            Criterion                                  OM
                  Assurance (A)

                                                                            Part A
                          I          —
OSO #01                                                                     Part D
                         A           —                                   Annex 8.1.1.1
                          I          —                                      Part T
OSO #02
                         A           —                                   Annex 8.1.3.3
                                                                   Part M Chapter 7.1
                          I          —
                                                                     Annex 8.1.1.2
                                                                   Part A Chapter 1.7
                                     #1
                                                                     Annex 8.1.1.2
OSO #03                                                            Part A Chapter 1.7
                                     #2
                         A                                           Annex 8.1.1.2
                                                                   Part A Chapter 1.6
                                     #3                            Part A Chapter 1.7
                                                                     Annex 8.1.1.2
                          I          —                                      Part T
OSO #04
                         A           —                                   Annex 8.1.3.1
                          I          —                                      Part T
OSO #05
                         A           —                                   Annex 8.1.3.1
                          I          —                            Part T Chapter 6.1.3
OSO #06
                         A           —                                   Annex 8.1.3.1
                                                                  Part B Chapter 2.8.1
                          I          —                                   Part D
OSO #07                                                                  Annex 8.2.6
                                     #1                            Part A Chapter 1.7
                         A
                                     #2                            Part A Chapter 1.7
                                                                            Part B
                                     #1                                     Part D
                                                                          Annex 8.3
                          I
                                                                            Part B
OSO #08                              #2
                                                                            Part D
                                     #3                                     Part E
                                                                            Part B
                         A           —
                                                                            Part D
Annex to ED Decision 2025/018/R                                                          Page 59 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


                                                                         Annex 8.1.2.3
                                                                            Part E
                                                                         Annex 8.3.1
                          I         —                              Part A Chapter 1.7
OSO #09
                         A          —                                       Part D
                          I         —                              Part B Chapter 2.3
OSO #13                                                            Part B Chapter 2.3
                         A          —
                                                                         Annex 8.1.2.4
                                    #1                             Part B Chapter 2.1
                          I
                                    #2                                      Part D
                                                                   Part B Chapter 2.1
OSO #16                             #1
                                                                         Annex 8.1.2.3
                         A
                                    #2                                      Part D
                                    #3                                   Annex 8.1.2.4
                          I         —                              Part A Chapter 1.9
OSO #17
                         A          —                              Part A Chapter 1.9
                          I         —                                       Part T
OSO #18
                         A          —                                    Annex 8.1.3.1
                          I         —                              Part B Chapter 2.8
OSO #19
                         A          —                                    Annex 8.1.3.1
                          I         —                             Part T Chapter 6.1.7
OSO #20
                         A          —                                    Annex 8.1.3.1
                                                                   Part B Chapter 2.4
                          I         —                             Part C Chapter 3.1.1
                                                                            Part D
OSO #23                                                            Part C Chapter 3.1
                                                                   Part B Chapter 2.4
                         A          —
                                                                         Annex 8.1.2.3
                                                                            Part D
                          I         —                                       Part T
OSO #24
                         A          —                                    Annex 8.1.3.1
                          I         —                            Part C Chapter 3.2.3.2
M1
                         A          —                                    Annex 8.1.2.2
                          I         —                                       Part T
M2
                         A          —                                    Annex 8.1.3.2
ARC                       I         —                            Part C Chapter 3.2.3.3
mitigation               A          —                                Annex 8.1.2.1




Annex to ED Decision 2025/018/R                                                           Page 60 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


                                                                 Part B Chapter 2.8.3.4
                          I         —                            Part B Chapter 2.8.3.5
TMPRs
                                                                  Part T Chapter 6.1.5
                         A          —                                    Annex 8.1.3.1
                          I         —                             Part T Chapter 6.1.6
Containment
                         A          —                                    Annex 8.1.3.1
                          I         —                             Part T Chapter 6.1.8
Payload
                         A          —                                    Annex 8.1.3.1




Annex to ED Decision 2025/018/R                                                           Page 61 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

A.4 Compliance matrix
Introduction
This chapter provides a template for UAS operators on how to present the reference between the
SORA-driven requirements and the operations manual from Chapter A.3 of Annex A to this AMC to
the competent authority.
For all the requirements that should be fulfilled in order to conduct a safe UAS operation, the UAS
operator should put the specific reference into the compliance matrix table where it can be found.
This is not a list of evidence, but the reference where it can be found.
Example:

 …
 Requirement                               Level of                Reference to documentation
                                           robustness

 OSO #08                                   ☒ Low                   Document name:

                                           ☐ Medium                 MyOperationsManual.pdf

                                           ☐ High                  Chapter or page number:
                                                                   Chapter B, pp. 42–47
                                                                   Chapter Annex, p. 815

 …

(The level of robustness in this case is SAIL dependent, and should be checked accordingly (e.g. ‘low’
for SAIL II.))




Annex to ED Decision 2025/018/R                                                            Page 62 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3



                                          Compliance matrix


 Requirement                              Level of robustness      Reference to documentation


                                       Ground risk mitigations


 M1(A) Strategic mitigations               ☐ None                  Document name:
 — Sheltering                              ☐ Low                   _____________________________

                                           ☐ Medium                Chapter or page number:
                                                                   _____________________________


 M1(B) Strategic mitigations               ☐ None                  Document name:
 — Operational restrictions                ☐ Medium                _____________________________

                                           ☐ High                  Chapter or page number:
                                                                   _____________________________


 M1(C) Tactical mitigations                ☐ None                  Document name:
 — Ground observation                      ☐ Low                   _____________________________
                                                                   Chapter or page number:
                                                                   _____________________________


 M2 — Effects of UA impact dynamics        ☐ None                  Document name:
 are reduced
                                           ☐ Medium                _____________________________

                                           ☐ High                  Chapter or page number:
                                                                   _____________________________




Annex to ED Decision 2025/018/R                                                          Page 63 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3



                                          Strategic air risk mitigations


 Air risk class (ARC)             ☐ ARC-d (AEC 1 or 2) → ARC-c          Document name:
 mitigation
                                  ☐ ARC-d (AEC 1 or 2) → ARC-b          _____________________________

                                  ☐ ARC-d (AEC 3) → ARC-c
                                                                        Chapter or page number:
                                  ☐ ARC-d (AEC 3) → ARC-b
                                                                        _____________________________
                                  ☐ ARC-c (AEC 4) → ARC-b

                                  ☐ ARC-c (AEC 5) → ARC-b

                                  ☐ ARC-c (AEC 6,7,8) → ARC-b

                                  ☐ ARC-c (AEC 9) → ARC-b




                         Tactical mitigation performance requirements (TMPRs)


 TMPR level             ☐ VLOS (deconfliction scheme)                   Document name:

                        ☐ BVLOS                                         _____________________________

                          ☐ No requirement (ARC-a)                      Chapter or page number:
                          ☐ Low requirement (ARC-b)                     _____________________________
                          ☐ Medium requirement (ARC-c)
                          ☐ High requirement (ARC-d)


                        Detect                                          Document name:
                                                                        _____________________________
                                                                        Chapter or page number:
                                                                        _____________________________


                        Decide                                          Document name:
 TMPR function                                                          _____________________________
                                                                        Chapter or page number:
                                                                        _____________________________


                        Command                                         Document name:
                                                                        _____________________________
                                                                        Chapter or page number:

Annex to ED Decision 2025/018/R                                                               Page 64 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3


                                                                      _____________________________


                        Execute                                       Document name:
                                                                      _____________________________
                                                                      Chapter or page number:
                                                                      _____________________________


                        Feedback loop                                 Document name:
                                                                      _____________________________
                                                                      Chapter or page number:
                                                                      _____________________________


 TMPR robustness        TMPR integrity and assurance                  Document name:
                        objectives                                    _____________________________
                                                                      Chapter or page number:
                                                                      _____________________________




                                        Containment requirements


 Containment                                      ☐ Low               Document name:

                                                  ☐ Medium            _____________________________

                                                  ☐ High              Chapter or page number:
                                                                      _____________________________
                                                  ☐ Tethered




Annex to ED Decision 2025/018/R                                                             Page 65 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3


                                  Operational safety objectives (OSOs)

 OSO #01                                       ☐ NR                 Document name:
 Ensure that the UAS operator is a
                                               ☐ Low                _____________________________
 competent and/or proven organisation
                                               ☐ Medium             Chapter or page number:
                                                                    _____________________________
                                               ☐ High

 OSO #02                                       ☐ NR                 Document name:
 UAS designed and produced by a
                                               ☐ Low                _____________________________
 competent and/or proven organisation
                                               ☐ Medium             Chapter or page number:
                                                                    _____________________________
                                               ☐ High

 OSO #03                                       ☐ Low                Document name:
 Maintenance of the UAS
                                               ☐ Medium             _____________________________

                                               ☐ High               Chapter or page number:
                                                                    _____________________________

 OSO #04                                       ☐ NR                 Document name:
 UAS components essential for its safe
                                               ☐ Low
 operation are designed to an
 Airworthiness Design Standard (ADS)           ☐ Medium             Chapter or page number:

                                               ☐ High               _____________________________


 OSO #05                                       ☐ NR                 Document name:
 UAS is designed considering system
                                               ☐ Low                _____________________________
 safety and reliability
                                               ☐ Medium             Chapter or page number:
                                                                    _____________________________
                                               ☐ High

 OSO #06                                       ☐ NR                 Document name:
 C3 link characteristics (e.g. performance
                                               ☐ Low                _____________________________
 spectrum use) are appropriate for the
 UAS operation                                 ☐ Medium             Chapter or page number:
                                                                    _____________________________
                                               ☐ High




Annex to ED Decision 2025/018/R                                                           Page 66 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3



 OSO #07                                      ☐ Low                Document name:
 Conformity check of the UAS
                                              ☐ Medium             _____________________________
 configuration
                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #08                                      ☐ Low                Document name:
 Operational procedures are defined,          ☐ Medium             _____________________________
 validated and adhered to
                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #09                                      ☐ Low                Document name:
 Remote crew trained and current
                                              ☐ Medium             _____________________________

                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #13                                      ☐ Low                Document name:
 External services supporting UAS
                                              ☐ Medium             _____________________________
 operations are adequate for the UAS
 operation                                    ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #16                                      ☐ Low                Document name:
 Multi-crew coordination
                                              ☐ Medium             _____________________________

                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #17                                      ☐ Low                Document name:
 Remote crew is fit to operate
                                              ☐ Medium             _____________________________

                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #18                                      ☐ NR                 Document name:
 Automatic protection of the flight
                                              ☐ Low                _____________________________
 envelope from human errors
                                              ☐ Medium             Chapter or page number:
                                                                   _____________________________
                                              ☐ High


Annex to ED Decision 2025/018/R                                                          Page 67 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3



 OSO #19                                      ☐ NR                 Document name:
 Safe recovery from human error
                                              ☐ Low                _____________________________

                                              ☐ Medium             Chapter or page number:

                                              ☐ High

 OSO #20                                      ☐ NR                 Document name:
 A human factors evaluation has been
                                              ☐ Low                _____________________________
 performed and the human–machine
 interface (HMI) has been found               ☐ Medium             Chapter or page number:
 appropriate for the intended UAS                                  _____________________________
                                              ☐ High
 operation

 OSO #23                                      ☐ Low                Document name:
 Environmental conditions for safe
                                              ☐ Medium             _____________________________
 operations are defined and measurable
                                              ☐ High               Chapter or page number:
                                                                   _____________________________

 OSO #24                                      ☐ NR                 Document name:
 The UAS is designed and qualified to
                                              ☐ Medium             _____________________________
 operate in adverse environmental
 conditions                                   ☐ High               Chapter or page number:
                                                                   _____________________________




                                             Confirmation

 Have all safety requirements been described and met?             ☐Yes

                                                                  ☐No

 Place, date                                        Name and signature




Annex to ED Decision 2025/018/R                                                          Page 68 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

A.5 How to document and present a flight area
Introduction
This chapter provides guidelines, typically located under Part C ‘Flight areas’ of the operations manual,
on how to prepare and present a flight area. The goal is to present the proposed flight area in a way
that is both straightforward and easy to understand. This is crucial not only for the competent
authority reviewing this section, but especially for all staff that participate in the flight operation and
consult the operations manual.
It is worth noting that this section is also relevant for operators that have the privilege to analyse,
approve and document flight areas independently, such as those approved under a generic
operational authorisation.
For better usability, Chapter A.5 is divided into two sections:
—      Section A.5.1 provides a comprehensive guide on creating a *.kml file, which is a file format for
       displaying information in a geographic context. It also specifies the basic necessities for the
       illustration and delves into the methods of depicting the flight area, as well as explaining the
       underlying reasons for these representations in the operations manual.
—      Section A.5.2 provides a sample computation for determining the minimum dimensions of the
       contingency volume and the ground risk buffer. These examples are intended solely as
       illustrative calculations. For a more in-depth analysis, one may also employ sophisticated flight-
       mechanics-based computations. These calculations can be incorporated into the operations
       manual annex. UAS operations covered by standard scenarios (STS) or predefined risk
       assessments (PDRAs) should use at least the values defined in the STS or the PDRA.
While adhering to these guidelines, it is important to cite the source used for the calculations.
If the UAS operator chooses to use alternative calculations, it is important to provide clear explanation
and supporting documentation that outline the methodology and its safety assurances.

A.5.1 Presentation
The provided graphical representation of the flight area should contain as a minimum:
—      an area: flight geography in transparent green colour;
—      an area: contingency volume in transparent yellow colour;
—      an area: ground risk buffer in transparent red colour;
—      a position: remote pilots’ position (for VLOS operations);
—      a position: remote pilots’ position and AO position (for BVLOS operations with AOs);
—      a position: take-off / landing position (optional).
The UAS operator should provide the flight area to the competent authority when required.
This should be in the format of a *.kml file or a similar format suitable for visualisation, accompanied
by the operations manual or a referenced document that includes all pertinent flight area details.
There are two methods for delineating the flight area: ‘inside out’ or ‘reverse’. The choice between
them largely depends on the constraining factor. For many applications, the ‘inside out’ method will
provide the desired areas based on the specific flight geography.
However, there may be situations where it is preferable to utilise the maximum available ground risk
Annex to ED Decision 2025/018/R                                                               Page 69 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3

buffer (e.g. controlled ground) and then determine the maximum possible flight geography from that.
This is called ‘reverse’ computation of the flight area.


            Inside out:                                            Reverse:




                Figure 9 — ‘Inside out’ versus ‘reverse’ computation of the flight area


Areas within the flight geography that need to be excluded for any reason (e.g. higher ground risk)
should be addressed in the same way as to surround them with a contingency volume and a ground
risk buffer.
A screenshot of the flight area, accompanied by a concise description, all input values, and the
calculations for contingency volume (CV) and ground risk buffer (GRB) should be documented. For
instance, in Part C of the operations manual according to Chapter A.3.
The content should be presented in a manner that is easily comprehensible to all parties involved in
the operation, enabling swift access to all pertinent data during routine operations. It is also crucial
for the competent authority to understand the calculation process. If the derivation of the calculation
or the overall rationale is unusually extensive, it is advisable to relocate the sections not directly
pertinent to daily operations to the operations manual annex.


Example:
Detailed information for each flight area is typically located under Part C, following the recommended
format outlined in Chapter A.3 ‘Structure of the operations manual’.
In a structured chapter layout, this may appear as follows:
    3 Part C — Flight Areas
                  3.2 Flight area [project name]
Description
The flight area, along with its precise coordinates, is delineated in the accompanying *.kml file
‘[project name.kml]’.




Annex to ED Decision 2025/018/R                                                            Page 70 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3




                           Figure 8 — Graphical representation of a flight area


The centre of the figure is located at [N53.1234567 E11.1234567].
The remote pilot’s position is located at [N53.1434567 E11.1434567].
General comment: [The flight area is an area used for agricultural purposes, etc.]
Special procedures/mitigations: [CTR Clearance for airport XY is required, as per OM 2.2]

Calculation of the contingency volume (CV) and the ground risk buffer (GRB)
The CV and the GRB were determined using the formulas described in paragraph A.5.2 of this annex.
UA characteristics:
—      type: [rotary wing without parachute];
—      altitude measurement: [barometric];
—      maximum speed in operation V0: [10,0 m/s];
—      maximum permissible wind speed VWind: [3,0 m/s];
—      characteristic dimension CD: [1,50 m];
—      maximum pitch angle Θmax: [45°].
The following parameters were used:
—      height of the flight geography HFG: [100,0 m];
—      calculation method: [from inside];
—      manoeuvre on entering into the contingency volume (horizontal): [stopping];
—      manoeuvre on entering the contingency volume (vertical): [kinetic into potential];
—      manoeuvre on entering the ground risk buffer: [power off].



Annex to ED Decision 2025/018/R                                                             Page 71 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3

Assumptions:
—      GNSS accuracy SGNSS: [0,5 m];
—      position holding error SPos: [3,0 m];
—      map error SK: [1,0 m];
—      reaction time tR: [1,0 s];
—      altitude measurement error HAM: [HBaro = 1,0 m];
—      additional distance (horizontal) SAdd: [0,0 m];
—      additional distance (vertical) HAdd: [0,0 m].
Reasons for deviations from the standard values:
—      SGNSS ([0,5 m] instead of [3,0 m]): [The UA is equipped with …];
—      …;
—      HCM ([3,0 m] instead of [5,1 m]): [The assumption based on …].

Results
Flight altitude:
—      Altitude of the flight geography HFG: [100,0 m].
Contingency volume:
—      Horizontal SCV: [34,5 m];
—      Vertical HCV: [113,1 m].
Ground risk buffer:
—      Horizontal SGRB: [113,8 m].
Adjacent ground area:
—      Horizontal SAA: [5000 m].




Annex to ED Decision 2025/018/R                                             Page 72 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3




                                              contingency volume                      … or
                   either
                                                                                      ballistic
                1:1-rule…                      flight geography
                                                                                      approach
                            𝑆𝐺𝑅𝐵                                                                  𝑆𝐺𝑅𝐵
                                                                                𝑆𝐶𝑉
                            𝑆𝐴𝐺𝐴        𝑆𝐹𝐺                                                       𝑆𝐴𝐺𝐴




                                        𝑆𝐴𝐺𝐴       adjacent ground area



                                                                     𝑆𝐺𝑅𝐵

                                                                          ground risk buffer



                                               contingency volume 𝑆𝐶𝑉

                                                  flight geography




       Figure 9 — Schematic representation of the flight geography, the contingency volume
                                   and the ground risk buffer




Annex to ED Decision 2025/018/R                                                                          Page 73 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3

A.5.2 Calculations used in the example case in the paragraph above
A.5.2.1 Information required for the calculations

                  Maximum operational speed that is flown. This corresponds to the information in
                  point 3.6 in the operational authorisation application form provided in
    𝑉0 , m/s      AMC1 UAS.SPEC.030(2).
                  Note: A speed below 3 m/s for multirotor and 1.25 ∙ 𝑉Stall,clean for fixed-wing aircraft
                  is not considered realistic.

                  For the ‘maximum UA characteristic dimension (CD)’, please refer to definition
                  I.141 ‘UA characteristic dimensions’ in Annex I to this AMC. Propellers and rotors
     CD, m        are part of the geometry, whereby their most unfavourable position is considered.
                  This corresponds to the information in point 3.4 of the operational authorisation
                  application form provided in AMC1 UAS.SPEC.030(2).

                  Maximum wind speed specified in the operations manual up to which the UA may
  𝑉Wind, m/s
                  be operated.

       FG         Flight geography

       CV         Contingency volume

      GRB         Ground risk buffer



A.5.2.2 Computation of the flight geography
Variant 1 (‘inside out’)
The size of the flight geography usually results from the operator’s desired flight geography.
The contingency volume and the ground risk buffer just add up to this area.
Variant 2 (‘reverse’)
Determination of the maximum flight geography available, e.g. when operating over a controlled
ground area.
In this example (controlled ground), the ground projection of the flight geography, the contingency
volume and the ground risk buffer should be completely contained in the controlled ground area.
A calculation in reverse is recommended.
The outer limit of the ground risk buffer corresponds to the topology of the controlled ground area.
In the first step, the horizontal extent (width) of the ground risk buffer is subtracted from the topology
of the controlled ground area. This gives the boundary between the contingency volume and the
ground risk buffer.
In the second step, the horizontal extent (width) of the contingency volume is then subtracted from
this limit. This results in the maximum possible expansion of the flight geography as the remaining
area.

Annex to ED Decision 2025/018/R                                                               Page 74 of 204
                                   AMC & GM to Regulation (EU) 2019/947
                                          Issue 1, Amendment 3

Notes on the realistic definition of particularly small flight geographies:

 Flight geography (FG) horizontal

 Width of the flight geography: 𝑆FG                                       𝑆FG ≥ 3 CD

 Flight geography (FG) vertical

 Height of the flight geography: 𝐻FG                                      𝐻FG ≥ 3 CD

 Note: Values smaller than 𝐻FG = 3 CD and 𝑆FG = 3 CD are considered unrealistic, also for automated
 waypoint flights.


A.5.2.3 Computation of the contingency volume
Notes on the realistic dimensioning of the contingency volume. Assumptions can be substituted with
real values if evidence is available:

 Contingency volume horizontal

 GNSS accuracy: 𝑆GNSS                                                 𝑆GNSS = 3 m

 Position holding error: 𝑆Pos                                             𝑆Pos = 3 m

 Map error: 𝑆K                                                            𝑆K = 1 m

                                          Manual initiation of measures
                                          Reaction time: 𝑡R = 1 s, with 𝑉0 results in
 Reaction distance: 𝑆R                                                    𝑆R = 𝑉0 𝑡𝑅
                                          Note: 𝑡R may also be smaller in fully automatic systems (e.g.
                                          geofence).




Annex to ED Decision 2025/018/R                                                         Page 75 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3



                                         Multirotor — stopping
                                                            1
                                         Based on 𝑆CM = 2 𝑎 𝑡R 2 + 𝑉0 𝑡R follows for a

                                         thrust to weight ratio of at least 2
                                                                    thrust ≥ 2 𝑚 𝑔
                                         and a maximum pitch angle of less than 45 degrees
                                                                         Θmax ≤ 45°

 Contingency manoeuvres: 𝑆CM             The minimum distance for stopping to hovering mode is:

                                                                            1    𝑉0 2
                                                                  𝑆CM =
                                                                            2 𝑔 tan(Θ)
                                         Fixed-wing aircraft –180° turn:
                                         Assumption: roll angle Φmax ≤ 30°
                                         The radius for the turn is:

                                                                            𝑉0 2
                                                                   𝑆CM =
                                                                         𝑔 tan(Φ)

                                         Flight terminated with parachute triggered when leaving the
 Alternative contingency manoeuvre       FG 𝑡P = Time to open the parachute
 parachute: 𝑆CM
                                                                         𝑆CM = 𝑉0 𝑡P

 Horizontal extension of the
                                                        𝑆CV = 𝑆GPS + 𝑆Pos + 𝑆K + 𝑆R + 𝑆CM
 contingency volume: 𝑆CV




 Examples

 Example: multirotors
           m                                                                    m 2
 𝑉0 = 10 s , Θ = 45° , [tan(45°) =                                       1 (10 s )
                                           SCV = 3 m + 3 m + 1 m + 10 m + ∙           = 22,1 m
 1]                                                                      2 9,81 m ∙ 1
                                                                                s2


 Example: fixed-wing aircraft                                                          m 2
                                                                                  (30 s )
           m
 𝑉0 = 30 s , Φ = 30°                           SCV = 3 m + 3 m + 1 m + 30 m +      m
                                                                              9,81 2 ∙ tan(30°)
                                                                                   s
                                                         = 195,9 m

 Contingency volume vertical

 Altitude measurement error: 𝐻AM         𝐻AM = 𝐻Baro = 1 m for barometric altitude measurement


Annex to ED Decision 2025/018/R                                                          Page 76 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


                                         or
                                         𝐻AM = 𝐻GNSS = 4 m for GNSS-based altitude measurement.
                                         Note: When operating close to large buildings or between
                                         buildings in narrow streets, the altitude information provided by
                                         GNSS may not be reliable.

                                         Manual initiation of measures
                                         Reaction time: 𝑡R = 1 s, with 45° pitch angle

 Reaction distance: 𝐻R                                             𝐻R = 𝑉0 ∙ 0,7 ∙ 𝑡R
                                         Note: 𝑡R may also be smaller in fully automatic systems (e.g.
                                         geofence). If external services are used for command and control,
                                         their system latency should be taken into consideration.

                                         For multirotor
                                         The forward kinetic energy is completely converted into
                                         potential energy.
                                         This results in

                                                                           1 𝑉0 2
                                                                     𝐻CM =
                                                                           2 𝑔
                                         For fixed-wing aircraft

 Contingency manoeuvres: 𝐻CM             Exit the FG upwards with a 45° pitch angle, then fly on a constant
                                         circular path with V0 and radius r until level flight is achieved.
                                         With

                                                                              𝑉0 2
                                                                         𝑟=
                                                                               𝑔
                                         results in the        contingency       manoeuvre    height    being
                                         approximately

                                                                          𝑉0 2
                                                                    𝐻CM =      ∙ 0,3
                                                                           𝑔
                                         Flight terminated with parachute triggered when leaving the FG

 Alternate contingency manoeuvre         Exit FG with 45° pitch angle
 parachute: 𝐻CM                          𝑡P = Time to open the parachute
                                                                   𝐻CM = 𝑉0 ∙ 𝑡P ∙ 0,7

 Contingency volume: 𝐻CV                                   𝐻CV = 𝐻FG + 𝐻AM + 𝐻R + 𝐻CM




Annex to ED Decision 2025/018/R                                                              Page 77 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


 Examples

 Height of the flight geography                                      𝐻FG = 100 m

                                                                             m 2
                                                                       1 (10 s )
                                              𝐻CV = 100 m + 1 m + 7 m + ∙         = 113,1 m
 Example: multirotor: 𝑉0 = 10 s
                                  m
                                                                       2 9,81 m
                                                                              s 2


                                                                            m 2
                                                                       (30 s )
                                      m     𝐻CV = 100 m + 1 m + 21 m +       m ∙ 0,3 = 149,52 m
 Example: fixed-wing a/c: 𝑉0 = 30 s                                     9,81 2
                                                                             s

A.5.2.4 Computation of the ground risk buffer

 Ground risk buffer horizontal

                                                                                 1
 Simplified approach: 1:1 rule: 𝑆GRB                             𝑆GRB = 𝐻CV +      CD
                                                                                 2

 Ballistic approach: 𝑆GRB
                                                        2 𝐻CV  1
 Note: Only permitted for rotorcraft      𝑆GRB = 𝑉0 √         + CD
                                                          𝑔    2
 and multirotors!

                                          𝑡P = Time to open the parachute
 Termination with parachute: 𝑆GRB
                                   From the rate of descent with the parachute open (𝑉z ) and the
                             m
 Note: Values below 𝑉Wind = 3 are  maximum permissible wind speed for operation (𝑉Wind) results
                             s
 not considered realistic for this in
 computation.                                                             𝐻CV
                                                    𝑆GRB = 𝑉0 𝑡P + 𝑉Wind
                                                                           𝑉z

                                          • Power is switched off:
                                                                         1   𝐶
                                                  A glide ratio of 𝐸 = 𝜀 = 𝐶L results in
                                                                             D

 Termination with fixed-wing                                         𝑆GRB = 𝐸 𝐻CV
 aircraft: 𝑆GRB
                                          • Power is switched off and the flight control surfaces are
                                            permanently set in a way that no gliding is possible:
                                                  The simplified approach can be chosen (1:1 rule).




 Examples

                                                                      1
 Simplified approach:                                 𝑆GRB = 113,1 m + ∙ 1,5 m = 113,85 m
                                                                      2


Annex to ED Decision 2025/018/R                                                            Page 78 of 204
                                      AMC & GM to Regulation (EU) 2019/947
                                             Issue 1, Amendment 3

                         m
 Multirotor: 𝑉0 = 10 s , CD = 1,5 m,
 𝐻CV = 113,1 m

 Ballistic approach:
                                                                 m 2 ∙ 113,1 m 1
                     m                              𝑆GRB = 10                 + ∙ 1,5 m = 48,77 m
 Multirotor: 𝑉0 = 10 s , CD = 1,5 m,                             s √ 9,81 m    2
                                                                           s2
 𝐻CV = 113,1 m

 Fixed-wing aircraft if only power is
                             m                                𝑆GRB = 149,52 m ∙ 20 = 2990,4 m
 switched off: 𝑉0 = 30 s , CD = 3 m,
 𝐻CV = 149,52 m , E=20

 Fixed-wing aircraft if power is
 switched off and flight control
 surfaces set so that no gliding is                                        1
                                                          𝑆GRB = 149,52 m + ∙ 3 m = 151,02 m
                         m                                                 2
 possible:    𝑉0 = 30 s ,        CD = 3 m,
 𝐻CV = 149,52 m

 GRB vertical                                         — not applicable —


A.5.2.5 Examples of computation of maximum distance(s) for VLOS / BVLOS with AOs
When determining the operating range for VLOS or BVLOS with AO operations, care should be taken
to ensure that the remote pilot can actually operate the UAS within their visual range or within the
visual range of the AOs.
To check whether the described UAS operation is in VLOS or in BVLOS, the following calculations may
be used.




 VLOS / BVLOS with           In VLOS or in BVLOS with AOs the air risk is mitigated by having the UA in sight of
 AO limit                    the remote pilot or of the AO. The maximum possible distance between the
                             remote pilot or the AO and the UA results from the smaller value of ALOS and
                             DLOS. Anything beyond that is considered BVLOS.

                             Attitude line of sight (ALOS)
                             The ALOS defines the maximum distance up to which a remote pilot can detect
 ALOS                        the position and orientation of the UA. Up to this limit, the remote pilot is able
                             to control the flight path of the UA and is able to determine the attitude and
                             position of the UA. This distance was determined in practical tests.

                             Detection line of sight (DLOS)
 DLOS
                             The DLOS defines the distance up to which the UA could theoretically fly while at
                             the same time other aircraft in the same direction can be visually detected, and



Annex to ED Decision 2025/018/R                                                                Page 79 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3


                              sufficient time is available for an avoidance manoeuvre. The ground visibility is
                              crucial for this.

                              Ground visibility (GV)
                              The GV depends on the operational area and the meteorological conditions, and
                              should be determined at the respective time of operation. The procedure for
                              precisely determining GV should be described in a section of the OM related to
 GV
                              procedures (e.g. Section 2.4 of the OM structure provided in A.3 of this annex).
                              The use of landmarks or the use of a transmissometer is possible.
                              The maximum ground visibility to be assumed is 5 km, analogue to the visibility
                              according to the VFR rules in airspace G40.




 ALOS limit                   For rotorcraft and multirotors:
                              ALOSmax = 327 ∙ CD + 20 m


                              For fixed-wing aircraft:
                              ALOSmax = 490 ∙ CD + 30 m

 DLOS limit                                                       DLOSmax = 0,3 ∙ GV
                              The GV depends on the actual ground visibility at site and time of operation.
                              However, the following always applies:
                                                                     GVmax = 5 km



If the largest possible distance between the remote pilot’s location and the outer side of the CV
(boundary between CV and GRB) is greater than the VLOS distance, no VLOS operation may take place.
UAS operations should then take place in BVLOS.




40   As any larger GV value is not deemed possible to extend the bare eye DLOS beyond the 1.5 km, provided that sufficient
     time for avoidance is still available.

Annex to ED Decision 2025/018/R                                                                            Page 80 of 204
                                       AMC & GM to Regulation (EU) 2019/947
                                              Issue 1, Amendment 3

A.5.2.6 Examples for maximum VLOS distances
The following table is valid for a ground visibility of 5 km or more.

 Characteristic dimension               Maximum VLOS distance

 (CD)                                   Rotary wing                           Fixed wing

                                  1m                               347 m                        520 m

                                  2m                               674 m                      1 010 m

                                  3m                             1 000 m                      1 500 m

                              3,5 m                            1 164,5 m                      1 500 m

                                  4m                             1 328 m                      1 500 m

                             4,53 m                              1 500 m                      1 500 m

                           > 4,53 m                              1 500 m                      1 500 m




                                   Figure 10 — Multirotor VLOS range




Annex to ED Decision 2025/018/R                                                            Page 81 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3




                                  Figure 11 — Fixed-wing VLOS range




Annex to ED Decision 2025/018/R                                          Page 82 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3


    Annex B to AMC1 Article 11
    INTEGRITY AND ASSURANCE LEVELS FOR THE MITGATIONS USED TO REDUCE THE INTRINSIC
    GROUND RISK CLASS (iGRC)

    B.1 How to use Annex B
    The following table provides the basic principles to consider when using the SORA Annex B.

#         Principle description                                                                    Additional information

#1        Annex B provides the assessment criteria for the integrity (i.e. safety gain) and        The identification       and
          assurance (i.e. method of proof) of the applicant’s proposed mitigations.                implementation            of
          The proposed mitigations are intended to reduce the iGRC associated with a               mitigations    is        the
          given operation.                                                                         responsibility  of       the
                                                                                                   applicant.

#2        A proposed mitigation should have a positive effect on reducing the ground
          risk associated with defined operational limitations. In the case where a
          mitigation is available but does not reduce the ground risk, its level of integrity
          should be considered equivalent to ‘None’.

#3        To achieve a given level of integrity/assurance, when more than one criterion If a criterion for a mitigation
          exists for that level of integrity/assurance, all applicable criteria need to be is not applicable, it can be
          met, unless specified otherwise.                                                 ignored      (e.g.    passive
                                                                                           mitigations do not require
                                                                                           training or activation).

#4        Annex B intentionally uses non-prescriptive terms (e.g. suitable, reasonably
          practicable) to provide flexibility to both applicants and competent
          authorities. This does not constrain the applicant in proposing mitigations,
          nor the competent authority in evaluating what is needed on a case-by-case
          basis.

#5        Annex B in its entirety also applies to single-person organisations.

#6        Annex B mitigations are applied to the operational volume and ground risk                Details    of    mitigation
          buffer. Annex B mitigations may be applied to the adjacent ground area.                  application to adjacent
                                                                                                   ground area can be found in
                                                                                                   Annex F Edition 2.541.

#7        All bullet points within all tables in this Annex are meant to be fulfilled unless
          followed by ‘or’.




    41   http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf

    Annex to ED Decision 2025/018/R                                                                     Page 83 of 204
                                    AMC & GM to Regulation (EU) 2019/947
                                           Issue 1, Amendment 3


#8    The GRC cannot be lowered to a value less than the equivalent for controlled
      ground area.

#9    Any criterion labelled ‘technical design’ will most likely require the support of
      the UAS or component designer for providing statements of compliance and,
      if applicable, gathering the required evidence.

#10   The applicant may claim more points of GRC reduction than indicated in
      Table 11 (Table 5 in this AMC (SORA Main Body)) when the appropriate orders
      of magnitude reduction of the risk to uninvolved people can be
      demonstrated. Any of these claims should be fulfilled to ‘high’ robustness
      level.


                                       Table B.1 — Basic principles




 Annex to ED Decision 2025/018/R                                                          Page 84 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3

   B.2 M1(A) — Strategic mitigations — Sheltering
   The M1(A) mitigation is linked to the fact that people spend on average a very small amount of time
   outdoors unprotected by a structure. Therefore, operators that use sufficiently small UAS can expect
   to have a large percentage of the population sheltered from an impact. This assumption may also
   apply to larger UAS; in these cases, the sheltering effectiveness should be demonstrated.
   Time-based arguments such as ‘I fly at night and there are less people outdoors in my iGRC footprint’
   do not belong to M1(A) low robustness. At medium robustness, time-based arguments are included.
   Sheltering at low robustness is to be understood as a generally applicable mitigation given by the
   characteristics of the environment being flown, with no operational restrictions added.
   To prevent double-counting time-based restrictions, M1(A) medium robustness mitigation cannot be
   combined with any M1(B) mitigations. However, M1(A) low robustness has no operational restrictions
   and can be combined with M1(B) mitigations.



                                                                   LEVEL of INTEGRITY
                                                         Low                                 Medium
                                     If the UAS operator claims a reduction due Same as low. In addition, the
                                     to a sheltered operational environment, the UAS       operator     restricts
                                     UAS operator:                                operating times (e.g. during
                                                                                  night-time) and demonstrates
                                     a) flies over operational environments
                                                                                  that    an    even     greater
                                          generally consisting of structures
                                                                                  proportion of uninvolved
             Criterion #1                 providing shelter (e.g. buildings);
M1(A) —                                                                           people are sheltered.
             (Evaluation of          b) it is reasonable to expect that on
Sheltering
             people at risk)              average a vast majority of the
                                          uninvolved people will be located under
                                          a structure1.
                                     This mitigation cannot be claimed when
                                     flying over outdoor assemblies of people or
                                     over areas with no shelter.




   Annex to ED Decision 2025/018/R                                                               Page 85 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3


                                  1
                                   The consideration of this mitigation may vary based on local conditions.
                                  A metastudy of time-activity pattern studies shows that people generally
                                  spend at most 10% of their time outside. Diffey, B. (2010). An overview analysis
                                  of the time people spend outdoors. The British journal of dermatology. 164.
                                  848-54. 10.1111/j.1365-2133.2010.10165.x.
                                  The intention is to estimate the proportion of people outside on average and
                                  not at a specific time of day or year. There will be times when at specific
          Comments                locations temporarily there are more people exposed, but it should be
                                  sufficient to expect that on average the proportion of people exposed outside
                                  is below 10%. However, assemblies of people should be avoided. UAS
                                  operators and/or competent authorities may consider adapting this ratio
                                  based on other evidence.
                                  Please, see GM2 UAS.SPEC.030(2) to identify whether the application of M1
                                  triggers the need to apply for an operational authorisation with precise or
                                  generic locations.

          Criterion #2
          (Evaluation of          The UAS operator uses a UA that is not expected to penetrate structures and
          penetration             fatally injure people under the shelter2.
          hazard)

                                  2
                                    Guidance on how to evaluate the sheltering effect can be found in the
                                  following:

                                      •     ASSURE UAS Ground Collision Severity Evaluation A4 report section
                                            ‘4.12. Structural Standards for Sheltering (KU)’, pp. 103–111, or

          Comments                    •     MITRE presentation given during the UAS Technical Analysis and
                                            Applications Center (TAAC) conference in 2016 titled ‘UAS EXCOM
                                            Science and Research Panel (SARP) 2016 TAAC Update’ - PR 16-3979.
                                  In general, it can be expected that UAS with a take-off mass of less than 25 kg
                                  are not able to penetrate into buildings except in cases where the UAS speed
                                  or building materials are unusual (e.g. tents, glass roofs, etc).

                Table B.2 — Level of integrity assessment criteria for M1(A) mitigation




Annex to ED Decision 2025/018/R                                                                  Page 86 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3


                                                                 LEVEL of ASSURANCE
                                                         Low                                  Medium
               Criterion #1         The UAS operator declares that the             Same as ‘low’. In addition, the
               (Evaluation of       operation is in an environment that has        UAS operator has time-based
               people at risk)      structures1 providing shelter where the        restrictions in place and
                                    vast majority of people are generally          evidence to support that a
                                    expected to be, and the UA does not fly        higher proportion of people
                                    over large outdoor assemblies of people.       are sheltered.
                                                                                   Medium robustness M1(A)
                                                                                   mitigation   cannot   be
                                                                                   combined     with   M1(B)
                                                                                   mitigations.

                                    1
               Comments                For example, a city or town consists generally of structures providing
M1(A) —
                                    shelter. While it may also include areas that are not sheltered, the mitigation
Sheltering
                                    is expected to be provided in most of such cases.

               Criterion #2         The applicant declares that the UA used has a take-off mass of less than
               (Evaluation of       25 kg.
               penetration
                                    OR
               hazard)
                                    For UA with a take-off mass higher than 25 kg1, the UAS operator has
                                    supporting evidence that the required level of integrity is achieved. This is
                                    typically done by means of testing, analysis, simulation, inspection, design
                                    review or through operational experience.

                                    1
                                     UA technical information needed for the evaluation may require support
               Comments
                                    from the UAS designer.

                        Table B.3 — Level of assurance criteria for M1(A) mitigation




  Annex to ED Decision 2025/018/R                                                                 Page 87 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3

  B.3 M1(B) — Strategic mitigations — Operational restrictions
  M1(B) mitigations are intended to reduce the number of people at risk on the ground independently
  of sheltering. These mitigations are applied before the flight.
  Improvements in the data included in the static data population density maps are not part of M1(B)
  mitigations and should be already used in the intrinsic ground risk assessment at Step #2. Use of best
  available data is encouraged to be used already for the iGRC determination.
  A competent authority may on a case-by-case basis accept pure time exposure arguments for ground
  risk reduction but should consider how this affects the cumulative risk. M1(B) mitigations are
  combinations of limitations on time and location of the operation to reduce the number of people at
  risk at a set time and location.



                                                                LEVEL of INTEGRITY
                                                    Medium                                     High
                                    The UAS operator provides space-time-based restrictions (e.g. flying over
                                    a market square when it is not crowded) to substantiate that the actual
                                    density of people during the operation is lower than that in Step #2.

                 Criterion #1       This can be done by means of:
                 (Evaluation of     a) an analysis or appraisal of the characteristics of the location1 and the
                 people at risk)       time2 of operation; AND/OR
                                    b) the use of temporal density data (e.g. data from a supplemental data
                                       service provider) relevant for the proposed area; this can incorporate
                                       real-time or historical data.

                                    1
                                     The characteristics of the location should be understood as land use that
 M1(B) —                            relates to the presence of people, e.g. industrial area, urban park or
Operational                         shopping centres.
restrictions     Comments
                                    2
                                      Time should be understood as time of day or day of the week that would
                                    influence the presence of people, e.g. weekend for industrial plants,
                                    night-time, time after opening hours of shops.

                                                                                 The population at risk is
                                    The population at risk is lowered by at
                 Criterion #2                                                    lowered by at least 2 iGRC
                                    least 1 iGRC population band3 (~90 %)
                 (Impact on                                                      population bands3 (~99 %)
                                    using one or more methods described
                 population at                                                   using one or more methods
                                    in the level of integrity for criterion #1
                 risk)                                                           described in the level of
                                    above.
                                                                                 integrity for criterion #1 above.

                                    3
                                     The iGRC population band is described in ‘4.2.3 Step #2’ of the SORA
                 Comments
                                    Main Body.

                  Table B.4 — Level of integrity assessment criteria for M1(B) mitigation


  Annex to ED Decision 2025/018/R                                                               Page 88 of 204
                                     AMC & GM to Regulation (EU) 2019/947
                                            Issue 1, Amendment 3




                                                               LEVEL of ASSURANCE
                                                   Medium                                   High
                 Criterion #1        All mapping products, data sources and processes used to claim
                 (Evaluation of     lowering the density of population at risk are accepted by the competent
                 people at risk)    authority.

                 Comments           N/A

                                                                               The claimed level of integrity is
                                                                               validated by the competent
                                                                               authority of the Member State
 M1(B) —                            The UAS operator has supporting
                 Criterion #2                                                  or by an entity that is designated
Operational                         evidence that the required level of
                 (Impact on                                                    by the competent authority
restrictions                        integrity is achieved. This is typically
                 population at                                                 against a standard considered
                                    done by means of analyses, surveys
                 risk)                                                         adequate by the competent
                                    or through operational experience.
                                                                               authority and/or in accordance
                                                                               with means of compliance
                                                                               acceptable to that authority.

                                    Quantitative and qualitative mitigations can in combination meet the
                 Comments           target reductions of populations at risk set in ‘medium’ and ‘high’
                                    integrity levels.

                        Table B.5 — Level of assurance criteria for M1(b) mitigation




  Annex to ED Decision 2025/018/R                                                               Page 89 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3

 B.4 M1(C) — Tactical mitigations — Ground observation
 The M1(C) mitigation is a tactical mitigation where the remote crew or the system can observe most
 of the overflown area(s), allowing the detection of uninvolved people in the operational area and
 manoeuvring the UA so that the number of uninvolved people overflown during the operation is
 significantly reduced42.
                                                                         LEVEL of INTEGRITY
                                                                                Low
                                         To achieve a reduction of the number of people at risk:
                                         a) the remote crew members observe the vast majority of the
                                            overflown areas during the operation and identify area(s) of lower
                                            risk on the ground (e.g. presence of uninvolved people and
                  Criterion #1
                                            obstacles);
                  (Procedures)
                                         b) the remote pilot reduces the number of people at risk by adjusting
                                            the flight path while the operation is in progress (e.g. flying away from
                                            the area with a higher risk on the ground or overflying only the
 M1(C) —                                    identified area(s) of lower risk on the ground).
  Ground
                                         1
observation                               The iGRC population band is described in Chapter 4.2.3 Step #2 of this
                  Comments
                                         AMC (SORA Main Body).

                                         If the mitigation is achieved through the use of technical means1 (e.g.
                  Criterion #2
                                         camera(s) mounted on the UA or visual observers on the ground with
                  (Technical
                                         radios/phones), these should provide data of reliable quality allowing the
                  means)
                                         reliable detection of uninvolved people on the ground.

                                         1
                                          Criterion #2 may require support from the UAS or the component
                  Comments
                                         designer to gather the required evidence.

                    Table B. 6 - Level of integrity assessment criteria for M1(C) mitigation

                                                                        LEVEL of ASSURANCE
                                                                                Low
                                         The operational procedures for the mitigation are documented.
                  Criterion #1
                  (Procedures)           The UAS operator declares that the required level of integrity has been
                                         achieved.
 M1(C) —
  Ground          Comments               N/A
observation
                  Criterion #2
                                         Competent authorities may allow the use of technical means1 for ground
                  (Technical
                                         observation with assurance criteria acceptable to them.
                  means)


 42
      The size of the area where the remote crew is required to have ground observation should cover at least the projection
      on ground of the VLOS distance defined in Section A.5.2.5.

 Annex to ED Decision 2025/018/R                                                                             Page 90 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3


                                        1
                                         Criterion #2 may require support from the UAS or the component
                 Comments
                                        designer to gather the required evidence.

                 Table B. 7 — Level of assurance assessment criteria for M1(C) mitigation

B.5 M2 Effects of UA impact dynamics are reduced
M2 mitigations are intended to reduce the effect of ground impact once the control of the operation
is lost. This is done by either reducing the probability of lethality of a UA impact (i.e. energy, impulse,
transfer of energy dynamics, etc.) and/or by reducing the size of the expected critical area (see
Table B.8 below). Examples include but are not limited to parachutes, autorotation, frangibility,
stalling the aircraft to slow the descent and increase the impact angle. UAS designers should
demonstrate the required total amount of reduction (see integrity criteria) in either or for both
factors.
The base assumption in the SORA for UAS impact lethality before mitigation M2 is applied is that most
impacts are lethal43. Based on the characteristic dimensions of a UA, the related critical areas are
displayed in Table B.8 below. Depending on whether the mitigation is passive, manually activated or
automatically activated, UAS designers should provide correspondingly adequate evidence and
procedures for a given level of robustness. The reduction of the inherent critical area of a UA by way
of analysis should be conducted already in Step #2 of the SORA and is not part of mitigation M2.
Critical area calculations are defined in Annex F Edition 2.544 Chapter 1.845. The table provided in
Section S.4.2 of this AMC (SORA Main Body) assumes the following critical areas for each characteristic
dimension.




Maximum characteristic dimension (m)                    1              3             8         20            40


Critical area (m2)                                     6.5            65            650      6 500         65 000


 Table B.8 — Critical areas associated with the maximum characteristic dimension (non-mitigated)

UAS designers that claim a mitigation by reducing the critical area shall use the values above as the
baseline for comparison to show the appropriate mitigation.
If a UAS operator or a UAS designer has used the modifications according to Annex F Edition 2.545 in
Step #2, or has used the automatic critical area assessment tool available on the EASA website46, to


43   Most UA impacts are assumed to be lethal in the SORA ground risk model except:
     • impacts during slide of UA with characteristic dimension less or equal to 1 metre;
     • any impacts during slide of UA with total kinetic energy below 290 joules.
     See      Annex      F     Edition    2.5     (http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-
     Release.JAR_doc_29pdf.pdf) for more details on calculation.
44   http://jarus-rpas.org/wp-content/uploads/2024/06/SORA-v2.5-Annex-F-Release.JAR_doc_29pdf.pdf
45   Additional     guidelines    on   the    assessment       of     the   critical  area    may    be    found    at
     https://www.easa.europa.eu/en/downloads/139781/en.
46   https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/critical-area-assessment-tool-caat

Annex to ED Decision 2025/018/R                                                                        Page 91 of 204
                                      AMC & GM to Regulation (EU) 2019/947
                                             Issue 1, Amendment 3

 show a corrected critical area for its UAS and matched the corrected critical area to a column in
 Table B.8, then this table value is used as the baseline against which the mitigation is assessed.
 If a UAS operator or a UAS designer has used the modifications according to Annex F Edition 2.545 in
 Step #2 to show both a corrected critical area and a matching population density, then this custom
 critical area value is used as the baseline against which the mitigation is assessed, and the custom
 population density value should be used as a limitation in the UAS operation.



                                                                   LEVEL of INTEGRITY
                                                              1
                                                      Medium                                       High
                                   (a) The effects of impact dynamics and           Same as ‘medium’.
                                       immediate post-impact hazards2, the          In addition:
                                       critical area or the combination of these   (a) When        applicable,     the
                                       are reduced such that the risk to                activation of the mitigation is
                                       population is reduced by an                      automated4,5,6.
                                       approximate 1 order of magnitude
                                                                                   (b) The effects of impact
M2 —                                   (90 %)3.
                                                                                        dynamics and immediate post-
Effects of UA   Criterion #1       (b) When       applicable,    in    case   of        impact hazards2, the critical
impact          (Technical             malfunctions, failures or a combination          area or the combination of
dynamics        design)                of these that could lead to a crash, the         these are reduced such that
are reduced                            UAS contains all the elements required           the risk to the population is
                                       for the activation of the mitigation4.           reduced by an approximate 2
                                   (c) When applicable, any failure or                  orders of magnitude (99 %)3.
                                       malfunction of the proposed mitigation
                                       itself (e.g. inadvertent activation) does
                                       not adversely affect the safety of the
                                       operation.




 Annex to ED Decision 2025/018/R                                                                Page 92 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3

                                   1
                 Comments            MoC to Light-UAS.251247 is an acceptable means to comply with the ‘medium’
                                      level of robustness for M2. Moreover, it provides additional explanation of the
                                      M2 criteria.
                                   2
                                     Examples of immediate post-impact hazards include fires and release of high-
                                      energy debris.
                                   3
                                     Latest research on UAS impacts estimates injuries using the Abbreviated Injury
                                      Scale (AIS) developed for automotive impact tests and test dummies. An impact
                                      that has a 30 % chance of causing injury of AIS level 3 injury or greater is
                                      estimated to have a 10 % probability of death. Note that the SORA methodology
                                      only considers fatalities. It does not provide guidance on the injury levels /
                                      thresholds beyond which an injury should be considered as a fatality. Further
                                      guidance on how to evaluate impact severity measurement may be found for
                                      example in Ranges of Injury Risk Associated with Impact from Unmanned
                                      Aircraft Systems DOI: 10.1007/s10439-017-1921-6, ASSURE UAS reports A14
                                      and A4 on UAS Ground Collision Severity Evaluation.
                                   4
                                     For ‘medium’ robustness, the UAS designer is expected to address only probable
                                      malfunctions, failures and their combinations. No single failure should lead
                                      simultaneously to a loss of control of the operation and a reduction of the
                                      effectiveness of the M2 mitigation.
                                   5
                                     An automated activation may be required when reaction time is critical or when
                                      the operator cannot determine the need for activation.
                                   6
                                     The UAS designer may nevertheless implement an additional manual activation
                                      function.
                 Criterion #2      Any piece of equipment used to reduce the effect of the UA impact dynamics is
                 (Procedures)      installed, operated and maintained in accordance with the UAS/mitigation
                                   designer instructions.
                 Comments          N/A
                 Criterion #3      When the use of the mitigation requires action from the remote crew, then the
                 (Training)        UAS operator should provide appropriate training to the remote crew.
                                   The UAS operator should ensure that the personnel (internal or external)
                                   responsible for the installation and maintenance of the mitigations are qualified
                                   for the task.
                 Comments          N/A

                   Table B.4 — Level of integrity assessment criteria for M2 mitigation




47   https://www.easa.europa.eu/en/document-library/product-certification-consultations/means-compliance-mitigation-
     means-m2-ref-amc

Annex to ED Decision 2025/018/R                                                                        Page 93 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


                                                                LEVEL of ASSURANCE
                                                      Medium                                       High
                                  The UAS designer has supporting evidence to          The UAS operator should use
                                  claim that the required level of integrity and       a UAS for which EASA has
                                  reliability is achieved. This is typically done by   verified the claimed integrity
                                  means of testing, analysis, simulation1,             through a design verification
                                  inspection, design review or through                 report (DVR) issued following
                                  operational experience.                              an application from the UAS
                   Criterion #1                                                        designer.
                                  A UAS with a C0 or C1 class mark or with an
                   (Technical
                                  MTOM lower or equal to 900 g and a
                   design)
                                  maximum speed of 19 m/s fulfils the
                                  assurance criterion 1.
                                  The UAS designer may provide a statement of
                                  compliance with MoC to Light-UAS.25122 by
                                  providing the supporting evidence defined in
                                  it.

                                  1
                   Comments         When simulation is used, the validity of the targeted environment used in the
                                  simulation needs to be justified.
                                  2
                                   https://www.easa.europa.eu/en/document-library/product-certification-
M2 — Effects                      consultations/means-compliance-mitigation-means-m2-ref-amc
of UA impact
dynamics are       Criterion #2   (a) Procedures are validated against standards (a) the DVR covers the
reduced            (Procedures)       that are considered adequate by the            operating instructions
                                      competent authority of the Member State        of the mitigations;
                                      and/or in accordance with means of
                                                                                 (b) the            competent
                                      compliance acceptable to that authority.
                                                                                     authority       of    the
                                  (b) The adequacy of the operator’s procedures      Member State or an
                                      is justified through:                          entity that is designated
                                                                                     by    the competent
                                       (i) dedicated flight tests; or
                                                                                     authority verifies that
                                       (ii) simulation,    provided that     the     the           procedures
                                            representativeness of the simulation     developed by the UAS
                                            means is proven for the intended         operator              are
                                            purpose with positive results;           acceptable.
                                      (iii) any other means acceptable to the
                                            competent authority of the MS.
                                  (c) The UAS/mitigation designer provides the
                                      instructions necessary for the correct
                                      operation of the mitigations.




Annex to ED Decision 2025/018/R                                                                Page 94 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3


                   Comments       UAS operators may directly use the procedures provided by the
                                  UAS/mitigation designer and rely on the adequacy verification performed by
                                  them.
                                  AMC2 UAS.SPEC.030(3)(e) ‘Operational procedures for medium and high
                                  levels of robustness’ is considered an acceptable means of compliance.

                   Criterion #3   (a) Training syllabus is available.            Same as ‘medium’.
                   (Training)
                                  (b) The UAS operator provides theoretical and In addition, the competent
                                      practical training for the remote crew.    authority of the Member
                                                                                 State or an entity that is
                                  (c) Personnel responsible for installation and
                                                                                 designated      by     the
                                      maintenance of the mitigations have
                                                                                 competent authority:
                                      completed relevant training.
                                                                                 (a) validates the training
                                                                                     syllabus;
                                                                                 (b) verifies the remote
                                                                                     crew competencies.

                   Comments       N/A

                Table B.10 — Level of assurance assessment criteria for M2 mitigation




Annex to ED Decision 2025/018/R                                                         Page 95 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3



Annex E to AMC1 to Article 11
INTEGRITY AND ASSURANCE LEVELS FOR THE OPERATIONAL SAFETY OBJECTIVES (OSOs)

E.1. How to use SORA Annex E
       The following Table E.1 provides the basic principles to consider when using SORA Annex E.
       Principle description                                                                                     Additional information
 #1    Annex E provides assessment criteria for the integrity (i.e. safety gain) and assurance (i.e. method of   The identification of OSOs for a given operation is the
       proof) of the OSOs proposed by an applicant.                                                              responsibility of the applicant UAS operator.
                                                                                                                 The relationship between the SAIL and the low/medium/high
                                                                                                                 level of robustness of an OSO can be found in Step #9, see
                                                                                                                 Section S.4.9 of this AMC (SORA Main Body).
 #2    Annex E does not cover the LoI of the competent authority. The Lol is based on the competent
       authority’s assessment of the applicant ’s ability to perform the given operation.
 #3    To achieve a given level of integrity/assurance, wWhen more than one criterion exists for a given
       that level of integrity/assurance in an OSO, all the applicable criteria need to be met at the required
       integrity/assurance level to satisfy the given OSO.
 #4    ‘Optional’ ‘Not required (NR)’ cases defined in Section S.4.9.3 of this AMC (SORA mMain bBody)            All robustness levels are acceptable for OSOs for which an
       Table 14 6 do not need to be defined in terms of integrity and assurance levels in Annex E.               ‘optional’ level of robustness is defined in Table 6
                                                                                                                 ‘Recommended OSOs’ of the SORA main body.
                                                                                                                 UAS operators are encouraged to consider also the OSOs
                                                                                                                 classified as ‘NR’, at least with ‘low’ level of integrity and
                                                                                                                 assurance.
 #5    When the criteria to assess the level of integrity or assurance of an OSO rely on ‘standards’ that are
       not yet available, the OSO needs to be developed in a manner acceptable to the competent
       authority.
 #6    Annex E intentionally uses non-prescriptive terms (e.g. suitable, reasonably practicable) to provide
       flexibility to both the applicant and the competent authorities. This does not constrain the applicant
       fromin proposing mitigations, nor the competent authority fromin evaluating what is needed on a
       case-by-case basis.
 #7    This annex in its entirety also applies to single-person organisations.
       Some of the OSOs refer to the functional-test-based (FTB) approach which is described in detail in
 #8
       Section E.3.



Annex to ED Decision 2025/018/R                                                                                                                                Page 96 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3




Table E.1 – Basic principles to consider when using SORA Annex E

E.2    Operational safety objectives (OSOs) related to technical issues with the UAS

OSO #01 — Ensure that the UAS operator is a competent and/or proven organisation
                                                                                        Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                             Low                                                 Medium                                        High
                                                        (SAIL II)                                             (SAIL III)                               (SAIL IV to VI)
                                                                                       Same as L‘low’. In addition, the applicant UAS operator
                                                                                       has set up an organiszation appropriate13 for the
                                                                                       intended UAS operation, with at least the following in
                                                                                       place: Also, the applicant has a method to identify,
                                                                                       assess, and mitigate the risks associated with flight
                                      The      applicant     UAS     operator     is
                                      knowledgeable of the UAS1 being used and         operations. These should be consistent with the nature
                                      as a minimum has the following relevant          and extent of the operations specified.                   Same as medium
 OSO #01                              operational procedures2:
                 Criteria Criterion                                                    (a) a method to continuously evaluate whether the         The UAS operator has an
 Ensure that                          (a) checklists,
                                                                                           operator is operating according to the terms of the   adequate    organisational
 the UAS                              (b) maintenance,
                                                                                           operational authorisation and check whether the       management system.
 operator is a                        (c) training,
 competent                            (d) responsibilities, and associated duties.         mitigations proposed as part of the operational
 and/or                                                                                    authorisation are still appropriate;
 proven
 organisation                                                                          (b) occurrence analysis procedures and reporting to
                                                                                           the UAS designer in case of design-related in-
                                                                                           service events.

                                      N/A
                                                                                       13
                                      1                                                   For the purpose of this assessment, ‘appropriate’
                                       Including monitoring of any related
                                                                                       should    be     interpreted     as     commensurate
                 Comments             airworthiness        directives    or                                                                      N/A
                                                                                       with/proportionate to the size of the organisation and
                                      recommendations issued by national               the complexity of the operation.
                                      aviation authorities and UAS designer




Annex to ED Decision 2025/018/R                                                                                                                               Page 97 of 204
                                                                         AMC & GM to Regulation (EU) 2019/947
                                                                                Issue 1, Amendment 3


                                        recommendations (service bulletins, service
                                        information letters, etc.).
                                        2
                                          Operational     procedures      (checklists,
                                        maintenance, training, etc.) can be justified
                                        in the context of other applicable OSOs.

                                                                                           Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                                  Low                                          Medium                                          High
                                                             (SAIL II)                                      (SAIL III)                                 (SAIL IV to VI)
                                                                                                                                         The applicantUAS operator holds a light
                                                                                                                                         UAS operator certificate (LUC)
                                                                                                                                         according to PART C of Implementing
                                                                                                                                         Regulation (EU) 2019/947 or an air
                                                                                                                                         operator certificate (AOC) according to
                                                                                                                                         Regulation (EU) No 965/2012 or
                                                                                           Prior to the first operation, the competent   equivalent or, if the applicant is a
 OSO #01                                    The elements delineated in the level of        authority of the Member State or an entity    design or production organisation,
 Ensure that       Criteria Criterion       integrity are available and addressed in the   that is designated by the competent           holds an approval according to Subpart
 the UAS                                    operations manual ConOps.                      authority performs an audit of the            J or P of Annex I (Part 21) to Regulation
 operator is a                                                                             organisation.                                 (EU) No 748/2012. an organisational
 competent                                                                                                                               operating certificate (e.g LUC) or has a
 and/or proven                                                                                                                           recognised flight test organisation.
 organisation                                                                                                                            In addition, the competent authority of
                                                                                                                                         the MS or an entity that is designated
                                                                                                                                         by the competent authority verifies the
                                                                                                                                         UAS operator’s competencies.
                                                                                           N/A
                                                                                           Audits should be adapted to the size and scope of the organisation and focus on items
                   Comments                 N/A
                                                                                           that can be connected to the applicable OSOs and their robustness depending on the
                                                                                           SAIL of the operation. Audits can take the form of desk reviews, if deemed appropriate.




Annex to ED Decision 2025/018/R                                                                                                                                    Page 98 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


OSO #02 — UAS designed and produced by a competent and/or proven organisation entity
                                                                                       Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                                 Low                                      Medium                                        High
                                                           (SAIL III)                                  (SAIL IV)                                 (SAIL V & VI)
                                         As a minimum, design documentation
                                         covers:                                      Same as ‘low’.
                                                                                                                                     The UAS designer organisation
                            Criteria     (a) the specification of the materials;      In addition, design documentation also
                                                                                                                                     complies with Subpart J of Annex I
                            Criterion        and                                      covers:
                                                                                                                                     (Part 21)   to   Regulation   (EU)
                            for design   (b) the suitability and durability of the    (a) the configuration control; and
                                                                                                                                     No 748/2012.
                                             materials used; and                      (b) identification and traceability.
                                         (c) configuration control.
                                                                                      Same as ‘low’.
 OSO #02
                                                                                      In addition, production procedures also
 UAS designed and
                                                                                      cover:
 produced by a
                                          As a minimum, production procedures         (a) the configuration control;
 competent and/or
                                          cover:                                      (b)(a) the verification of incoming
 proven organisation        Criteria                                                                                                 The production organisation complies
                                         (a) the configuration control;,                  products, parts, materials, and
 entity                     Criterion                                                                                                with the organisational requirements
                                         (b) the processes necessary to allow for         equipment;
                            for                                                                                                      that are defined in Subpart F or G of
                                         repeatability in manufacturing;, and         (c)(b) identification and traceability;
                            production                                                                                               Annex I (Part 21) to Regulation (EU)
                                         (c) conformity      within      acceptable   (d)(c) in-process and final inspections
                                                                                                                                     No 748/2012.
                                         tolerances.                                      and& testing;
                                                                                      (e)(d) the control and calibration of tools;
                                                                                      (f)(e) handling and storage; and
                                                                                      (g)(f) the control of non-conforming items.
                            Comments     N/A                                          N/A                                            N/A




Annex to ED Decision 2025/018/R                                                                                                                             Page 99 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


                                                                                        Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS
                                                                Low                                           Medium                                     High
                                                              (SAIL III)                                      (SAIL IV)                              (SAIL V & VI)
                                                                                               Same as low. In addition, evidence is      Same as medium.
                                           The specifications, suitability and durability of
                                                                                               available that the UAS has been
                                           the materials are declared against a standard                                                  In addition:
                                                                                               designed in accordance with design
                                           recognised by the competent authority
                                                                                               procedures.                                In addition, the competent
                                           and/or in accordance with means of
                           Criteria                                                                                                       authority should request the
                                           compliance acceptable to the competent              The competent authority should
                           Criterion for                                                                                                  applicant The UAS operator should
                                           authority.                                          request the applicant UAS operator
                           design                                                                                                         to operate a UAS designed by an
                                                                                               should use a UAS for which EASA has
                                           The UAS operator should use a UAS for which                                                    organisation approved by EASA
                                                                                               verified the claimed integrity through a
                                           the UAS designer has issued a statement of                                                     according to Subpart J of Annex I
                                                                                               design verification report (DVR) issued
                                           compliance with MoC to OSO #021 using the                                                      (Part 21) to Regulation (EU)
                                                                                               following an application from the UAS
                                           form attached to the MoC.                                                                      No 748/2012       following     an
                                                                                               designer.
                                                                                                                                          application from the UAS designer.
 OSO #02
                                           1
                                             https://www.easa.europa.eu/en/document-
 UAS designed and
                                           library/product-certification-
 produced by a
                                           consultations/means-compliance-moc-
 competent and/or
                                           design-uas-operated-sail
 proven organisation       Comments
 entity                                    Note: EASA is in the process of developing the
                                           means of compliance for all OSOs. Once
                                           developed, they will be made available at the
                                           link above.
                                                                                                                                          Same as ‘medium’. In addition:, the
                                           The declared production procedures are                                                         competent authority of the
                                           developed to a standard that is considered          Same as ‘low’. In addition, evidence is    Member State or an entity that is
                           Criterion for   adequate by the competent authority that            available that the UAS has been            designated by the competent
                           production      issues the operational authorisation and/or in      produced in conformityance with its        authority validates compliance
                                           accordance with a means of compliance               design.                                    with the production organisational
                                           acceptable to the that competent authority.                                                    requirements that are defined in
                                                                                                                                          Subpart F or G of Annex I (Part 21)
                                                                                                                                          to Regulation (EU) No 748/2012




Annex to ED Decision 2025/018/R                                                                                                                               Page 100 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


                                                                                                                                      following an application from the
                                                                                                                                      UAS production organisation.
                                            N/A                                               N/A                                     N/A
                           Comments




OSO #03 — UAS maintained by competent and/or proven entityMaintenance of UAS
                                                                                      Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                            Low                                             Medium                                     High
                                                      (SAIL I & II)                                    (SAIL III & IV)                          (SAIL V & VI)

                                      The     UAS     designer’s  maintenance
                   Criterion #1                                                      Same as ‘low’.
                                      instructions and requirements to ensure a
                   (Design)                                                          In addition, the UAS designer’s scheduled maintenance requirements are defined.
                                      safe operation are defined.

                                                                                     Same as ‘low’.
                                                                                     In addition:
                                                                                                                                      Same as ‘medium’.
 OSO #03                                                                             (a) Preventive/sScheduled         maintenance/
                                      (a)      The UAS operator’s1 maintenance                                                        In addition, the maintenance staff
 Maintenance                                                                         inspection of each UAS is organised and in
                                      instructions2 and requirements3 are                                                             work in accordance with a
 of UAS                                                                              accordance with a the UAS operator’s
                                      defined, and, when applicable, covering the                                                     maintenance procedures manual
 maintained by                                                                       maintenance programme, established on the
                                      applicable UAS designer’s instructions and                                                      that provides information and
 a competent                                                                         basis of the UAS designer’s scheduled
                                      requirements4,5, and are adhered to.                                                            procedures relevant to the
 and/or proven     Criteria                                                          maintenance requirements4 and adapted to the
                                      (b)      The     maintenance     staff    is                                                    maintenance facility, records,
 entity (e.g.      Criterion #2                                                      specificities of the intended UAS operations.
                                      competent and has received an                                                                   maintenance instructions, release,
 industry          (Procedure)                                                       (b) Upon completion, the maintenance log
                                      authorisation by the UAS operator to carry                                                      tools, materials, components,
 standards)                                                                          system is used to record all the maintenance
                                      out UAS maintenance.                                                                            defect deferral, etc.
                                                                                     conducted on the UAS, including releases.
                                      (c)      The maintenance staff use the UAS
                                                                                     A maintenance release can only be
                                      maintenance instructions while performing                                                       The UAS operator complies with
                                                                                     accomplished by a staff member that who has
                                      maintenance.                                                                                    Delegated   Regulation    (EU)
                                                                                     received by the UAS operator a maintenance
                                                                                                                                      2024/1107.
                                                                                     release authorisation for athat particular UAS
                                                                                     model/family.
                   Comments           N/A




Annex to ED Decision 2025/018/R                                                                                                                          Page 101 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3



                                  1
                                      The maintenance may be carried out by an organisation other than the UAS operator (e.g. use of a third party).
                                  2
                                   The UAS operator’s maintenance instructions are the information establishing how to carry out the required maintenance/repairs.
                                  These instructions are used by maintenance staff while performing maintenance.
                                  3
                                   The UAS operator’s maintenance requirements are the needs for maintenance of the UAS (e.g. inspection after hard landing, regular
                                  check of lighting system). The UAS operator ensures these requirements are covered in the UAS maintenance instructions.
                                  4
                                      The UAS operator may just reuse the UAS designer’s instructions and requirements for maintenance.
                                  5
                                   The UAS designer’s instructions and requirements for maintenance are sometimes referred to as ‘ICAs’ (Instructions for Continuing
                                  Airworthiness).




Annex to ED Decision 2025/018/R                                                                                                                        Page 102 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


                                                                               Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                          Low                                             Medium                                         High
                                                    (SAIL I & II)                                   (SAIL III & IV)                               (SAIL V & VI)
                                                                               Same as ‘low’.
                                                                               In addition, the UAS designer’s scheduled maintenance requirements are developed
                                                                               and documented in accordance with standards considered adequate by the
                                                                               competent authority of the Member State and/or in accordance with means of
                                                                               compliance acceptable to that authority.
                                                                               If the operation is classified as SAIL III, the UAS operator should use a UAS for which
                                     The UAS designer’s maintenance the UAS designer has issued a statement of compliance with MoC to OSO #03 and
                     Criterion #1
                                     instructions and requirements to ensure a Light-UAS.26251 using the form attached to the MoC.
                     (Design)
                                     safe operation are documented.            If the operation is classified as SAIL IV, the UAS operator should use a UAS for which
                                                                               EASA has issued a design verification report (DVR) issued following an application
                                                                               from the UAS designer.
                                                                               If the operation is classified as SAIL V and VI, the UAS operator should use a UAS for
 OSO #03                                                                       which EASA has issued a type certificate or a restricted type certificate in accordance
 Maintenance of                                                                with Annex I (Part 21) to Regulation (EU) No 748/2012, following an application from
 UAS maintained                                                                the UAS designer.
 by a competent                                                                     1
                                                                                      https://www.easa.europa.eu/en/document-library/product-certification-
 and/or proven       Comments        N/A
                                                                                    consultations/means-compliance-moc-design-uas-operated-sail
 entity (e.g.
                                                                                    Same as ‘low’.
 industry
                                                                                    In addition:                                             Same as ‘medium’.
 standards)
                                                                                    (a) The UAS operator’s maintenance programme In addition, the maintenance
                                                                                    covers the UAS designer’s scheduled maintenance programme               and     the
                                     (a) The UAS operator’s maintenance
                                                                                    requirements and is developed in accordance with maintenance             procedures
                                     instructions are documented1.
                                                                                    standards considered adequate by the competent manual are validated by the
                                     (b) The    maintenance      carried out
                                                                                    authority of the Member State and/or in accordance competent authority of the
                     Criterion #12   conducted on the UAS is recorded in a
                                                                                    with a means of compliance acceptable to that Member State or by an entity
                     (Procedure)     maintenance log system2,31/2.
                                                                                    authority. In addition, if the UAS has a DVR or a (R)TC, that is designated by the
                                     (c) A list of the maintenance staff
                                                                                    the maintenance programme includes the scheduled competent authority.
                                     authorised to carry out maintenance is
                                                                                    maintenance requirements developed as part of the
                                     established and kept up to date.
                                                                                    design.                                                  The UAS operator complies
                                                                                    (b) A list of the maintenance staff with maintenance with Delegated Regulation
                                                                                    release authorisation is established and kept up to (EU) 2024/1107.
                                                                                    date.



Annex to ED Decision 2025/018/R                                                                                                                         Page 103 of 204
                                                                  AMC & GM to Regulation (EU) 2019/947
                                                                         Issue 1, Amendment 3



                                     1
                                      The UAS operator may just reuse the UAS
                                     designer’s instructions and requirements
                                     for maintenance.
                                     21
                                         The objective is to record all the
                                     maintenance       performed     on     the
                     Comments        UAaircraft, and why it is performed            N/A                                                         N/A
                                     (rectification of defects or malfunctions,
                                     modifications, scheduled maintenance,
                                     etc.).
                                     32
                                       The maintenance log may be requested
                                     for inspection/audit by the approving
                                     authority or an authorised representative.
                                                                                                                                                Same as ‘medium’.
                                                                                                                                                In addition:
                                                                                                                                                (a) A a programme for the
                                                                                    Same as ‘low’.
                                                                                                                                                recurrent training of staff
                                                                                    In addition:
                                                                                                                                                holding      a   maintenance
                                                                                    (a) The initial training syllabus and training standard,
                                                                                                                                                release    authorisation   is
                                                                                    including theoretical/practical elements, duration,
                                     A record of all the relevant qualifications,                                                               established; and
                                                                                    etc., is defined and is commensurate with the
                     Criterion #23   experience and/or training completed by                                                                    (b) This that programme is
                                                                                    authorisation held by the maintenance staff.
                     (Training)      the maintenance staff is established and                                                                   validated by the Member
                                                                                    (b) For staff that hold a maintenance release
                                     kept up to date.                                                                                           State or by an entity that is
                                                                                    authoriszation, the initial training is specific to athat
                                                                                                                                                designated by the competent
                                                                                    particular UAS model/family.
                                                                                                                                                authority.
                                                                                    (c) All maintenance staff have undergone initial
                                                                                    training.
                                                                                                                                                The UAS operator complies
                                                                                                                                                with Delegated Regulation
                                                                                                                                                (EU) 2024/1107.
                     Comments        N/A                                            N/A                                                         N/A




Annex to ED Decision 2025/018/R                                                                                                                               Page 104 of 204
                                                                 AMC & GM to Regulation (EU) 2019/947
                                                                        Issue 1, Amendment 3


OSO #04 — UAS components essential to safe operations are designed to an airworthiness design standard developed to authority recognized design
      standards
(a)    Within the scope of OSO #4, UAS components essential to safe operations are those whose failure would significantly impair the capability of the
       operator to meet the required target level of safety in terms of loss of control of the operation. The term ‘component’ is meant as including any element
       of the UAS.
(b)    Starting at SAIL IV, it is considered that the safety objective associated to the SAIL of an operation (e.g. probability of loss of control of the operation
       below 10-–4/FH for a SAIL IV operation) should be achieved with a UAS designed to be compliant with SC Light UAS verified by EASA.
       The list of airworthiness design standards (ADSs) to be complied with through OSO #04 is not intended to duplicate the requirements already covered
       by other design-related OSOs. While OSO #04 aims at ensuring that the UAS as a whole is designed according to an ADS (for example, the design and
       construction, structure, and flight performance is part of the ADS, but not of other OSOs), other design-related OSOs focus on particular
       systems/functionalities of the UAS and or technical disciplines (e.g. safety):
       —      OSO #05 (system safety related),
       —      OSO #06 (C3 link),
       —      OSO #07 (conformity check),
       —      OSO #13 (external services),
       —      OSO #18 (automatic protection of envelope),
       —      OSO #20 (HMI),
       —      OSO #23/#24 (adverse environmental conditions).




Annex to ED Decision 2025/018/R                                                                                                                    Page 105 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3




                                                                                     Level of integrity LEVEL of INTEGRITY
  TECHNICAL ISSUE WITH THE UAS                      Low Medium                                                            High
                                                      (SAIL IV)                                   (SAIL V)                                   (SAIL VI)
                                                                                 The UAS components that are essential to The UAS components that are essential
                                   The UAS components that are essential to
                                                                                 safe operations are is designed to an to safe operations are is designed to an
                                   safe operations are is designed to an
                                                                    1            airworthiness      design      standards1 airworthiness       design      standards1
                                   airworthiness design standards considered
  OSO #04                                                                        considered adequate by EASA the considered adequate by EASA the
                                   adequate by EASA the competent authority
  UAS                                                                            competent      authority     and/or     in competent       authority    and/or     in
                                   and/or in accordance with a means of
  components                                                                     accordance with a means of compliance accordance with a means of compliance
                      Criteria     compliance acceptable to EASA that
  essential to safe                                                              acceptable to EASA that authority to acceptable to EASA that authority to
                      Criterion    authority to contribute to the overall safety
  operations are                                                                 contribute to the overall safety objective contribute to the overall safety objective
                                   objective of 10–4/FH for the loss of control
  designed to an                                                                 of 10–5/FH for the loss of control of the of 10–6/FH for the loss of control of the
                                   of the operation. The standards and/or the
  airworthiness                                                                  operation. The standards and/or the operation. The standards and/or the
                                   means of compliance should be applicable
  design                                                                         means of compliance should be applicable means of compliance should be
                                   to a low level of integrity and the intended
  developed to                                                                   to a medium level of integrity and the applicable to a high level of integrity and
                                   operation.
  authority                                                                      intended operation.                          the intended operation.
  recognised                       In case of experimental flights that investigate new technical solutions, the competent authority may accept that recognised
  design                           standards are not met.
  standards                        1
                      Comments         EASA Special Condition Light-UAS is the recommended airworthiness design standard.

                                   When aspects of an airworthiness design standard are covered by an OSO (for instance, OSO #05), the OSO requirement takes
                                   precedence.


                                                                                    Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                      Low Medium                                                              MediumHigh
                                                     (SAIL IV)                                                              (SAIL V & VI)
 OSO #04                           The competent authority should request the         The competent authority should request the applicant to use a UAS for which EASA
 UAS components                    applicant UAS operator should to use a UAS         has issued a type certificate or restricted type certificate in accordance with Annex I
 essential to safe                 for which EASA has verified the claimed            (Part 21) to Regulation (EU) No 748/2012.
 operations are        Criteria    integrity through a design verification report
 designed to an        Criterion   (DVR) issued following an application from         The competent authority should request the UAS operator should use a UAS for
 airworthiness                     the UAS designer.                                  which EASA has issued a type certificate or restricted type certificate in accordance
 design developed                                                                     with Annex I (Part 21) to Regulation (EU) No 748/2012, following an application from
 to authority                                                                         the UAS designer.



Annex to ED Decision 2025/018/R                                                                                                                              Page 106 of 204
                                                                AMC & GM to Regulation (EU) 2019/947
                                                                       Issue 1, Amendment 3


 recognised design
 standards             Comments     N/A                                          N/A                                     N/A

                                    In case the UAS designer decides to apply
                                    OSO #4 for UAS operated in SAIL I to III,
                                    MoC Light UAS.FTB may be used
                                    (https://www.easa.europa.eu/en/document-     N/A
                       Comment
                                    library/product-certification-
                                    consultations/final-means-compliance-
                                    special-condition-light).


OSO #05 — The UAS is designed considering system safety and reliability
       This OSO complements:
       (a)    the safety requirements for containment defined in the main body; and
       (b)    OSO #10 and OSO #12, which only address the risk of a fatality while operating over populated areas or assemblies of people.
       (a)    OSO #05 ensures that the contribution of the UAS, or of any external system supporting the operation, to the loss of control of the operation
              inside the operational volume is commensurate with the acceptable level of risk associated with each SAIL. The OSO #05 safety objectives are to
              be considered in conjunction with the containment safety requirements (Step #8 and Section 4 of this Annex) and, when applicable, the ground
              risk mitigation requirements (Annex B, in particular M2 Criterion #1 requirements). In combination, these three sets of safety objectives ensure
              that whatever the SAIL of the operation, the target level of safety is met and no single failure is expected to lead to a catastrophic event.
       (b)    Note on SAIL II operations: some UAS designs may employ novel or complex features with which the UAS designer has very limited operational
              experience. If such features are identified by the competent authority or the UAS designer, the UAS designer should assure that the equipment,
              systems and installations are designed to minimise hazards in the event of a probable failure of the UAS or of any external system supporting the
              operation. This should be done through a statement of compliance with a simple written justification from the UAS designer including functional
              diagrams and a description of how the system functions.




Annex to ED Decision 2025/018/R                                                                                                                Page 107 of 204
                                                                     AMC & GM to Regulation (EU) 2019/947
                                                                            Issue 1, Amendment 3


                                                                                    Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE
                                                   Low                                          Medium                                          High
 UAS
                                                 (SAIL III)                                     (SAIL IV)                                  (SAIL V & VI)
                                                                                                                            Same as medium. In addition:
                                                                                                                            (a) Major failure conditions are not more
                                                                                                                                 frequent than remote;
                                                                                                                            (b) Hazardous failure conditions are not
                                                                                                                                 more frequent than extremely remote3;
                                                                                                                            (c) Catastrophic failure conditions are not
                                  The equipment, systems, and                                                                    more frequent than extremely
                                                                              Same as ‘low’.
                                  installations are designed to minimise1                                                        improbable;
                                                                              In addition, the strategy for detection,
                    Criteria      hazards21 in the event of a probable32                                                    (d) No single failure can lead to a
                                                                              alerting and management of any malfunction,
                    Criterion     malfunction or failure of the UAS or of                                                        catastrophic failure condition; and
                                                                              failure or combination thereof, which would
                                  any external system supporting the                                                        (ed) SW and AEH whose development
                                                                              lead to a hazard, is available.
                                  operation.                                                                                     error(s) may cause or contribute to
                                                                                                                                 hazardous or catastrophic failure
 OSO #05
                                                                                                                                 conditions are developed to an industry
 The UAS is
                                                                                                                                 standard or a methodology considered
 designed                                                                                                                        adequate by EASA and/or in accordance
 considering
                                                                                                                                 with means of compliance acceptable
 system safety
                                                                                                                                 to EASA.
 and reliability
                                  1
                                     The minimisation of the hazard
                                  criterion correlates to the contribution
                                  of the UAS, and of any external system
                                  supporting the operation, to the loss of    N/A UAS designers may achieve compliance
                                  control of the operation rate, thus the     by using MoC Light UAS.2510
                    Comments      SAIL of the operation. As an example,       (https://www.easa.europa.eu/en/document-
                                  at SAIL III, the contribution of the UAS,   library/product-certification-
                                                                              consultations/means-compliance-moc-
                                  and of any external system supporting
                                                                              design-uas-operated-sai).
                                  the operation, to the loss of control of
                                  the operation rate could be 10–4/FH
                                  assuming        a    traditional     10 %




Annex to ED Decision 2025/018/R                                                                                                                          Page 108 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


                                  contribution of the technical aspects to
                                  the safety of an operation.


                                  21
                                     For the purpose of this assessment,
                                  the term ‘hazard’ should be
                                  interpreted as a failure condition that
                                  relates to major, and hazardous, or
                                  catastrophic consequences (the term
                                  ‘catastrophic’ is intentionally not
                                  included since the TLOS is considered
                                  met for SAIL I to IV operations with the
                                  provision of Note 1 above and, if
                                  applicable, M2 requirements in Annex
                                  B).
                                  32
                                     For the purpose of this assessment,
                                  the term ‘probable’ should be
                                  interpreted in a qualitative way as
                                  ‘anticipated to occur one or more
                                  times       during       the      entire
                                  system/operational life of a UAS’.


                                                                                    Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                              Low                                              Medium                                          High
                                                         (SAIL III)                                         (SAIL IV)                                   (SAIL V & VI)
                                                                                      Same   as SAIL III.                                      The competent authority
                                       A functional hazard assessment1,2 and a
                                                                                      In addition:                                             should request the applicant
 OSO #05                               design and installation appraisal3 that show
                                                                                      (a) The Ssafety analyses assessment is conducted         UAS operator should to use a
 The UAS is                            that hazards are minimised, are available.
                                                                                      in line with standards considered adequate by EASA       UAS for which EASA has
 designed          Criteria
                                                                                      the competent authority and/or in accordance with        issued a type certificate or
 considering       Criterion           The UAS operator should use a UAS for which
                                                                                      a means of compliance acceptable to EASA that            restricted type certificate in
 system safety                         the UAS designer has issued a statement of
                                                                                      authority.                                               accordance with Annex I (Part
 and reliability                       compliance with MoC to OSO #054 using the
                                                                                      (b) A strategy for the detection of single failures of   21) to Regulation (EU) No
                                       form attached to the MoC.                                                                               748/2012       following    an
                                                                                      concern includes pre-flight checks.



Annex to ED Decision 2025/018/R                                                                                                                              Page 109 of 204
                                                                  AMC & GM to Regulation (EU) 2019/947
                                                                         Issue 1, Amendment 3


                                                                                    Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                          Low                                                  Medium                                       High
                                                     (SAIL III)                                             (SAIL IV)                                (SAIL V & VI)
                                                                                      The competent authority should request the            application from the UAS
                                                                                      applicantUAS operator should to use a UAS for         designer.
                                                                                      which EASA has validated the claimed integrity
                                                                                      through a design verification report (DVR) issued
                                                                                      following an application from the UAS designer.
                                  1
                                   The severity of failure conditions (no safety
                                  effect, minor, major, hazardous and
                                  catastrophic) should be determined according
                                  to the definitions provided in JARUS AMC
                                  RPAS.1309 Issue 2.
                                  2
                                   EUROCAE ED-280 ‘Guidelines for UAS safety
                                  analysis for the specific category (low and
                                  medium levels of robustness)’ may be
                                  considered to support compliance with this          N/A
                                  criterion (through a functional hazard analysis     EUROCAE ED-280 ‘Guidelines for UAS safety analysis
                   Comments                                                           for the specific category (low and medium levels of   N/A
                                  (FHA)).
                                                                                      robustness)’ may be considered acceptable to
                                  3
                                   A simple written justification from the UAS        support compliance with this criterion.
                                  designer including functional diagrams and a
                                  description of how the system works
                                  explaining why the integrity claim is met is an
                                  acceptable means of compliance.
                                  4
                                    https://www.easa.europa.eu/en/document-
                                  library/product-certification-
                                  consultations/means-compliance-moc-
                                  design-uas-operated-sail




Annex to ED Decision 2025/018/R                                                                                                                        Page 110 of 204
                                                                 AMC & GM to Regulation (EU) 2019/947
                                                                        Issue 1, Amendment 3


OSO #06 — C3 link characteristics (e.g. performance, spectrum use) are appropriate for the UAS operation
       (a)    For the purpose of the SORA and this specific OSO, the term ‘C3 link’ encompasses:
              (1)    the C2 link; and
              (2)    any communication link required for the safety of the flight.
       (b)    To correctly assess the integrity of this OSO, the applicant UAS operator or the UAS designer, as described in the table below, should identify the
              following:
              (1)    The performance requirements for the C3 links necessary for the intended UAS operation.
              (2)    All the C3 links, together with their actual performance and RF spectrum useusage.
                     Note 1: The specification of the performance and the RF spectrum for a C2 Llink is typically documented by the UAS designer in the UAS
                     flight manual.
                     Note 2: The main parameters associated with the performance of a C2 link (RLP) and the performance parameters for other communication
                     links (e.g. RCP for communication with ATC) include, but are not limited to, the following:
                     (i)     the transaction expiration time;
                     (ii)    the availability;
                     (iii)   the continuity; and
                     (iv)    the integrity.
                     Refer to the ICAO references for definitions.
              (3)    The RF spectrum usage requirements for the intended UAS operation (including the need for authorisation if required).
                     Note: Usually, countries publish the allocation of RF spectrum bands applicable in their territories. This allocation stems mostly from the
                     International Communication Union (ITU) Radio Regulations. However, the applicantUAS operator should check the local requirements
                     and request authorisation when needed since there may be national differences and specific allocations (e.g. national sub-subdivisions of
                     ITU allocations). Some aeronautical bands (e.g. AM(R)S, AMS(R)S 5030-5091 MHz) were allocated for potential use in UAS operations under
                     within the ICAO scope for UAS operations classified as category. C (‘certified’), but their use may be authorised for operations inunder the
                     ‘specific’ category. It is expected that the use of other licensed bands (e.g. those allocated to mobile networks) may also be authorised


Annex to ED Decision 2025/018/R                                                                                                                  Page 111 of 204
                                                                     AMC & GM to Regulation (EU) 2019/947
                                                                            Issue 1, Amendment 3


                     inunder the ‘specific’ category. Some un-unlicensed bands (e.g. industrial, scientific and medical (ISM) or short-range devices (SRDs)) may
                     also be acceptable inunder the ‘specific’ category; for instance, for operations with lower integrity requirements.
              (4)    Environmental conditions that maymight affect the performance of C3 links.


                                                                                     Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                               Low                                           Medium                                   High
                                                        (SAIL II & III)                                   (SAIL IV)                            (SAIL V & VI)
                                    The UAS operator:
                                    (a) The applicant determines that the performance,
                                         RF spectrum usageuse1 and environmental
                                         conditions for C3 links, as identified in the UAS
                                                                                                                                  Same as ‘low’.
                     Criteria            flight manual2, are adequate to safely conduct
                                                                                                                                  In addition, the use of licensed45
                     Criterion #1        the intended UAS operation.                         Same as ‘low’34.
                                                                                                                                  frequency bands for C2 Llinks is
                     (Operator)     (b) has procedures for the The remote pilot has the
                                                                                                                                  required.
                                         means to continuously monitor the C3 link
                                         performance and ensures that the performance
 OSO #06                                 continues     to    meet      the     operational
 C3 link                                 requirements23.
                                    1
 characteristics                       For a low level of integrity, unlicensed frequency
 (e.g.                              bands maymight be acceptable under certain
 performance,                                                                                                                     45
                                    conditions, e.g.:                                                                                 This ensures a minimum level of
 spectrum use)                      (a)        the applicant demonstrates compliance                                              performance and is not limited to
 are appropriate                    with other RF spectrum usage requirements (e.g.          34                                   aeronautical licensed frequency bands
                                                                                               Depending on the operation, the
 for the UAS                        Directive 2014/53/EU), by showing that the UAS                                                (e.g. licensed bands for cellular
                                                                                             use of licensed frequency bands
 operation                          equipment is compliant with these requirements;                                               network).      Nevertheless,       some
                                                                                             maymight be necessary. In some
                                    and                                                                                           operations may require the use of bands
                     Comments                                                                cases, the use of non-aeronautical
                                    (b)        the use of mechanisms to protect against                                           allocated to the aeronautical mobile
                                                                                             bands (e.g. licensed bands for
                                    interference (e.g. FHSS, frequency de-deconfliction                                           service for the use of a C2 Llink (e.g.
                                                                                             cellular   network)    may     be
                                    by procedure).                                                                                5030–5091 MHz).
                                    2                                                        acceptable.
                                        The UAS designer may provide technical                                                    In any case, the use of licensed
                                    information also in other documentation.                                                      frequency bands requires needs
                                    32
                                        The remote pilot has continuousal and timely                                              authorisation.
                                    access to the relevant C3 links information that
                                    could affect the safety of flight. For operations



Annex to ED Decision 2025/018/R                                                                                                                           Page 112 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3


                                                                                      Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                                 Low                                          Medium                                   High
                                                          (SAIL II & III)                                  (SAIL IV)                            (SAIL V & VI)
                                    requesting only a low level of integrity for this OSO,
                                    this could be achieved by monitoring the C2 link
                                    signal strength and receiving an alert from the UAS
                                    HMI if the signal strength becomes too low.
                                    The UAS designer determines:
                                    (a) the performance and the RF spectrum use 1 for
                                         C3 links and specifies them in the UAS flight                                            Same as ‘low’.
                     Criterion #2
                                         manual;                                             Same as ‘low’3.                      In addition, the use of licensed4
                     (Designer)
                                    (b) that the means to continuously monitor the C3                                             frequency bands for C2 links is required.
                                         link performance are available and are defined
                                         in the UAS flight manual2.
                                    1
                                      For a low level of integrity, unlicensed frequency
                                    bands may be acceptable under certain conditions,
                                    e.g.:
                                                                                                                                  4
                                    (a) the UAS designer demonstrates compliance with                                                This ensures a minimum level of
                                    other RF spectrum use requirements (e.g. Directive                                            performance and is not limited to
                                    2014/53/EU) by showing that the UAS equipment is 3                                            aeronautical licensed frequency bands
                                                                                                Depending on the operation, the
                                    compliant with these requirements; and                                                        (e.g. licensed bands for cellular
                                                                                             use of licensed frequency bands
                                    (b) the use of mechanisms to protect against                                                  network).       Nevertheless,         some
                                                                                             might be necessary. In some cases,
                                    interference (e.g. FHSS).                                                                     operations may require the use of bands
                                                                                             the use of non-aeronautical bands
                                                                                                                                  allocated to the aeronautical mobile
                                    2                                                        (e.g. licensed bands for cellular
                                      The remote pilot has continuous and timely access                                           service for the use of C2 link (e.g. 5030–
                                                                                             network) may be acceptable.
                                    to the relevant C3 link information that could affect                                         5091 MHz).
                                    the safety of flight. For operations requesting only a                                        In any case, the use of licensed
                                    low level of integrity for this OSO, this could be                                            frequency bands needs authorisation.
                                    achieved by monitoring the C2 link signal strength
                                    and receiving an alert from the UAS HMI if the signal
                                    strength becomes too low.




Annex to ED Decision 2025/018/R                                                                                                                            Page 113 of 204
                                                                          AMC & GM to Regulation (EU) 2019/947
                                                                                 Issue 1, Amendment 3


                                                                                        Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                               Low                                             Medium                                             High
                                                        (SAIL II & III)                                     (SAIL IV)                                      (SAIL V & VI)
                                                                                                                                             The competent authority should
                                                                                            The competent authority should request the       request the to UAS operator should
                         Criteria                                                           applicant to UAS operator should use a UAS       use a UAS for which EASA has issued
                         Criterion    The UAS operator applicant declares that the          for which EASA has verified the claimed          a type certificate or a restricted type
                         #1           required level of integrity has been achieved.        integrity through a design verification report   certificate in accordance with Annex
                         (Operator)                                                         (DVR) issued following an application from       I (Part 21) to Regulation (EU) No
                                                                                            the UAS designer.                                748/2012 following an application
                                                                                                                                             from the UAS designer.
                         Comments     N/A.                                                  N/A                                              N/A
                                      The UAS designer declares that the required
                                      level of integrity has been achieved.
                                                                                                                                             The UAS designer should obtain a
 OSO #06
                         Criterion                                                                                                           type certificate or a restricted type
 C3 link                              If the operation is classified as SAIL III, the UAS   The UAS designer should obtain a design
                         #2                                                                                                                  certificate issued by EASA in
 characteristics (e.g.                operator should use a UAS for which the UAS           verification report (DVR) issued by EASA.
                         (Designer)                                                                                                          accordance with Annex I (Part 21) to
 performance,                         designer has issued a statement of declared
                                                                                                                                             Regulation (EU) No 748/2012.
 spectrum use) are                    with the MoC to OSO #061 using the form
 appropriate for the                  attached to the MoC.2
 UAS operation                        1
                                        https://www.easa.europa.eu/en/document-
                                      library/product-certification-
                                      consultations/means-compliance-moc-
                                      design-uas-operated-sail
                                      2
                                         For UAS operations classified in SAIL II, the
                                      UAS operator may still use an UAS for which
                         Comments                                                           N/A                                              N/A
                                      the UAS designer issued a statement of
                                      compliance with the MoC to OSO #6.
                                      However, the UAS designer should be allowed
                                      to experiment new solutions. In this case a
                                      statement of compliance not referring to a
                                      published MoC might be acceptable.




Annex to ED Decision 2025/018/R                                                                                                                                     Page 114 of 204
                                                                       AMC & GM to Regulation (EU) 2019/947
                                                                              Issue 1, Amendment 3


OSO #07 — Inspection of the UAS (product inspection) to ensure consistency with the ConOps Conformity check of the UAS configuration
(a)    The intent of this OSO is that the UAS operator assures that the UAS used for the operation conforms to the UAS data used to support the
       approval/authorisation of the intended UAS operation.
(b)    This OSO does not describe a pre- or post-flight inspection as part of normal operations; these are covered under OSO #8.
                                                                                     Level of integrity LEVEL of INTEGRITY
 TECHNICAL ISSUE WITH THE UAS                            Low                                          Medium                                      High
                                                      (SAIL I & II)                                 (SAIL III & IV)                           (SAIL V & VI)
 OSO #07                               The remote crew ensures that the UAS is in a condition for safe operation and conforms to the approved ConOps. 1
 Inspection of the                     The operator has UAS conformity check procedures in place ensuring periodically that:
                         Criteria
 UAS (product
                         Criterion     (a) the UAS intended to be used for the operation is in a condition for safe operation; and
 inspection) to
 ensure consistency                    (b) the UAS configuration conforms to the information contained in the UAS flight manual and to the authorised configuration 1.
 with the ConOps                       1
                                         The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
 Conformity check
                         Comments      (see the table below).
 of the UAS
                                       The allowed UAS configuration should be defined by the UAS designer according to the configuration control criteria as per OSO #2.
 configuration

                                                                                       Level of assurance LEVEL of ASSURANCE
 TECHNICAL ISSUE WITH THE UAS                               Low                                      Medium                                         High
                                                         (SAIL I & II)                             (SAIL III & IV)                              (SAIL V & VI)
                                           Product inspection is The UAS operator
                                                                                                                                 Same as ‘medium’. In addition, the
                                           declares it has UAS conformity check
                                                                                    Same as ‘low’. In addition, the UAS          product inspection procedures are
                        Criterion #1       procedures in place documented and
 OSO #07                                                                            conformity checks are the product            validated by the competent authority of
                        (Procedures)       which take into consideration accounts
 Inspection of the                                                                  inspection is documented using checklists.   the Member State or by an entity that is
                                           for the manufacturer’s UAS designer’s
 UAS (product                                                                                                                    designated by the competent authority.
                                           recommendations, if available.
 inspection) to
                        Comments           N/A                                      N/A                                          N/A
 ensure consistency
                                           The UAS operator declares that the       (a) A training syllabus, including a UAS     The competent authority of the Member
 with the ConOps
                                           remote crew is trained to perform the    conformity check product inspection          State or an entity that is designated by the
 Conformity check
                        Criterion #2       UAS conformity check the product         procedure, is available.                     competent authority:
 of the UAS
                        (Training)                                                  (b) The UAS operator provides evidence of    (a) validates the training syllabus; and
 configuration                             inspection, and that training is self-
                                                                                    the competency-based, theoretical and        (b) verifies     the       remote       crew
                                           declared (with evidence available).      practical training.                          competencies.
                        Comments           N/A                                      N/A                                          N/A


Annex to ED Decision 2025/018/R                                                                                                                              Page 115 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3




E.3      OSOs related to operational procedures

OSO #08 — Operational procedures are defined, validated and adhered to
(a)    Operational procedures address normal, abnormal and emergency situations potentially resulting from technical issues with the UAS or from external
       systems supporting the UAS operation, human error or adverse environmental conditions.
(b)    Standard operational procedures are a set of instructions covering policies, procedures and responsibilities set out by the UAS operator that support
       operational personnel in ground and flight operations of the UA safely and consistently during normal situations.
(c)    Contingency procedures are designed to potentially prevent a significant future event (e.g. loss of control of the operation) that has an increased
       likelihood to occur due to the current abnormal state of the operation. These procedures should return the operation to a normal state and enable the
       return to using standard operational procedures or allow the safe cessation of the flight.
(d)    Emergency procedures are intended to mitigate the effect of failures that could cause or could lead to an emergency situation.
(e)    The emergency response plan (ERP) deals with the potential hazardous secondary or escalating effects following a loss of control of the operation (e.g.
       in the case of ground impact, mid-air collision or fly-away) and is decoupled from the emergency procedures as it does not deal with the control of the
       UA during operation.
                                                                                     Level of integrity LEVEL of INTEGRITY
 OPERATIONAL PROCEDURES                                      Low                                                Medium                                High
                                                           (SAIL I)                                             (SAIL II)                        (SAIL III to VI)
                   Criterion #1
                   (UAS flight    The UAS designer develops a UAS flight manual, including the relevant information (e.g. limitations).
 OSO #08, OSO      manual)
 #11, OSO #14
 and OSO #21
                   Comments       N/A
 Operational
 procedures
 are defined,                     (a) The UAS operator develops operational procedures1 appropriate for the proposed operation, taking into account the relevant
 validated and                    information (e.g. limitations) listed in the UAS flight manual are defined and, as a minimum, cover the following elements:
                   Criterion #2
 adhered to                           (1) Flight planning;
                   (pProcedure
                                      (2) Pre- and post-flight inspections;
                   definition)
                                      (3) Procedures to evaluate the environmental conditions before and during the flight mission (i.e. real-time evaluation), including
                                          the assessment of meteorological conditions (METAR, TAF, etc.) with a simple recording system;


Annex to ED Decision 2025/018/R                                                                                                                            Page 116 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3


                                                                                  Level of integrity LEVEL of INTEGRITY
 OPERATIONAL PROCEDURES                                       Low                                            Medium                                   High
                                                            (SAIL I)                                          (SAIL II)                         (SAIL III to VI)
                                      (4) Procedures to cope with unexpected adverse operating conditions (e.g. when ice is encountered during an operation that is not
                                          approved for icing conditions);
                                      (5) Normal procedures;
                                      (6) Contingency procedures (to cope with abnormal situations);
                                      (7) Emergency procedures (to cope with emergency situations), including an ERP;
                                      (8) Pre-flight procedures, including briefing of any involved persons about the potential risks and actions to take in case the UA
                                          misbehaves;
                                      (89) Occurrence-reporting procedures; and
                                  (b) The limitations of the external systems supporting the UAS operation 2 are defined in anthe OM.
                                  1
                                    Operational procedures cover the deterioration of the UAS itself and of any external system supporting the UAS operation. Please,
                                  refer to Part B of the OM example for UAS operations published on the EASA website at
                                  https://www.easa.europa.eu/en/downloads/139674/en.
                                  To properly address the deterioration of external systems required for the operation, it is recommended to:
                                  (a) identify these ‘external systems’;
                                  (b) identify the modes of deterioration of the ‘external systems’ (e.g. complete loss of GNSS, GDOP/PDOP, latency issues, etc.) which
                                         would lead to a loss of control of the operation;
                                  (c) describe the means to detect these modes of deterioration of the external systems ; and
                   Comments
                                  (d) describe the procedure(s) to be used when deterioration is detected (e.g. activation of the emergency recovery capability, switch
                                         to manual control, etc.).
                                  2
                                    In the scope of this assessment, external systems supporting the UAS operation are defined as systems that are not already part of the
                                  UAS but are used to:
                                  (a) launch / take off the UA;
                                  (b) make pre-flight checks; or
                                  (c) keep the UA within its operational volume (e.g. GNSS, satellite systems, air traffic management, U-space).
                                  External systems activated/used after a loss of control of the operation are excluded from this definition.
                                  Operational procedures are complex and may potentially       Contingency/emergency procedures
                   Criterion #2
                                  jeopardise the crew’s ability to respond by increasing the   require manual control by the remote    Operational     procedures     are
                   (Procedure
                                  remote crew’s workload and/or their interaction with         pilot2 when the UAS is usually          simple.
                   complexity)
                                  other entities (e.g. ATM, etc.).                             automatically controlled.




Annex to ED Decision 2025/018/R                                                                                                                           Page 117 of 204
                                                                          AMC & GM to Regulation (EU) 2019/947
                                                                                 Issue 1, Amendment 3


                                                                                    Level of integrity LEVEL of INTEGRITY
 OPERATIONAL PROCEDURES                                          Low                                            Medium                                   High
                                                               (SAIL I)                                         (SAIL II)                           (SAIL III to VI)
                                                                                                2
                                                                                                  It should be considered that not all
                                                                                                UAS have a mode where the pilot could
                   Comments         N/A                                                         directly     control    the   surfaces;   N/A
                                                                                                moreover, it may require significant
                                                                                                skill not to make things worse.
                                                                             1
                   Criterion #3     Ast a minimum, operational procedures provide:
                                                                                                                                          Same as ‘medium’. In addition,
                   (Consideration   (a) include a clear distribution and assignment of tasks,
                                                                                                Operational procedures take human         the remote crew3 receives crew
                   of Ppotential    and
                                                                                                error into consideration.                 resource management (CRM)4
                   Hhuman           (b) rely on an internal checklists to ensure staff are
                                                                                                                                          training.
                   Eerror)          adequately performing their assigned tasks.
                                                                                                                                          3
                                                                                                                                            In the context of SORA, the term
                                                                                                                                          ‘remote crew’ refers to any
                                                                                                                                          person involved in the operation
                                                                                                                                          mission.
                                                                                                                                          4
                                                                                                                                             CRM training focuses on the
                                    N/A
                                    1                                                                                                     effective use of all the remote
                                      Please, refer to Part B of the OM example published on
                   Comments                                                                         N/A                                   crew to ensure safe and efficient
                                    the EASA website at
                                                                                                                                          operation,      reducing     error,
                                    https://www.easa.europa.eu/en/downloads/139674/en.
                                                                                                                                          avoiding stress and increasing
                                                                                                                                          efficiency. Elements of the CRM
                                                                                                                                          training may be found in the AMC
                                                                                                                                          and GM to point ORO.FC.115 to
                                                                                                                                          Regulation (EU) No 965/2012.
                                    The ERP:
                                    (a) is suitable for a given situation6;
                   Criterion #4     (b) effectively mitigates all anticipated hazardous secondary effects after the initial crash;
                   (Emergency       (c) clearly delineates the duties of the remote crew member(s);
                   response plan    (d) is practical to use and for training purposes, so that the remote crew can execute the procedures effectively under stress.
                   (ERP))
                                    The ERP contains as a minimum:
                                    (a) the list of anticipated emergency situations with secondary effects;




Annex to ED Decision 2025/018/R                                                                                                                               Page 118 of 204
                                                                        AMC & GM to Regulation (EU) 2019/947
                                                                               Issue 1, Amendment 3


                                                                                      Level of integrity LEVEL of INTEGRITY
 OPERATIONAL PROCEDURES                                         Low                                              Medium                                    High
                                                              (SAIL I)                                           (SAIL II)                            (SAIL III to VI)
                                      (b) the procedures for each of the identified anticipated emergency situations (including criteria to identify each of these situations);
                                      (c) the list of relevant contacts to reach (e.g. ATC, police, fire brigade, first responders).
                                      6
                                        The ERP should be proportional to the potential secondary effects of a ground impact, i.e. those effects that may occur after the initial
                                      ground impact (e.g. fire, release of poisonous gas). AMC3 UAS.SPEC.030(3)(e) provides additional information. The ERP chapter of the
                   Comments
                                      OM published on the EASA website (https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-
                                      civil-drones#group-easa-downloads) may be considered as a reference.

                                                                                      Level of assurance LEVEL of ASSURANCE
OPERATIONAL PROCEDURES                                    Low                                               Medium                                            High
                                                        (SAIL I)                                            (SAIL II)                                    (SAIL III to VI)
                                                                                                                                             SAIL III same as SAIL I and II.
                                                                                                                                             SAIL IV: EASA has verified the
                                                                                                                                                 claimed integrity through a
                                                                                                                                                 design verification report
                                                                                                                                                 (DVR) issued following an
                                                                                                                                                 application from the UAS
OSO #08, OSO                                                                                                                                     designer.
                                  The UAS operator should use a UAS for which the UAS designer has issued a statement of compliance
#11, OSO #14      Criterion #1                                                                                                               SAIL V and VI: EASA has verified the
                                  with MoC to OSO #081 using the form attached to the MoC.
and OSO #21                                                                                                                                      claimed integrity through the
Operational                                                                                                                                      issuance of a type certificate
procedures                                                                                                                                       according with Annex I (Part
are defined,                                                                                                                                     21) to Regulation (EU) No
validated and                                                                                                                                    748/2012 issued following an
adhered to                                                                                                                                       application from the UAS
                                                                                                                                                 designer.


                                  1
                                          https://www.easa.europa.eu/en/document-library/product-certification-consultations/means-
                  Comments                                                                                                                   N/A
                                          compliance-moc-design-uas-operated-sail




Annex to ED Decision 2025/018/R                                                                                                                                  Page 119 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


                                                                                                                                           Same as ‘medium’.
                                                                                     (a)  Normal, contingency, and emergency               In addition:
                                                                                          procedures are documented and part of the        (a) Flight tests performed to
                                                                                          operations manual (OM).                              validate    the     operational
                                                                                     (ab) Operational procedures and the ERP are               procedures and the checklists
                                                                                          validated against developed according to             cover the complete flight
                                  (a)   Operational procedures do not require             AMC2 UAS.SPEC.030(3)(e)                  and         envelope or are proven to be
                                        validation against either a standard or a         AMC3 UAS.SPEC.030(3)(e)         respectively.        conservative.
                                        means of compliance that is considered            standards considered adequate by the             (b) The operational procedures,
                                        adequate by the competent authority of            competent authority of the MS and/or in              checklists, flight tests and
                  Criteria #2,          the MS.                                           accordance with the means of compliance              simulations are validated by
                  #3 and #4       (b)   The UAS operator declares the adequacy            acceptable to that authority1.                       the competent authority of the
                                        of the operational procedures and the        (bc) The adequacy of the contingency and                  Member State or by an entity
                                        ERP. is declared, except for As a                 emergency procedures is proven through:              that is designated by the
                                        minimum, the emergency procedures,                (1) dedicated flight tests; or                       competent authority.
                                        which are tested.                                 (2) simulation,     provided     that    the     (c) The representativeness of the
                                                                                               representativeness of the simulation            tabletop exercise1 of the ERP is
                                                                                               means is proven valid for the intended          validated by the competent
                                                                                               purpose with positive results; or               authority of the Member State
                                                                                          (3) any other means acceptable to the                or by an entity that is
                                                                                               competent authority.                            designated by the competent
                                                                                                                                               authority.
                                  N/A
                                                                                     1
                                  Operational procedures do not require                AMC2 UAS.SPEC.030(3)(e) (Operational procedures for medium and high levels of
                  Comments        validation against either a standard or a means    robustness) is considered an acceptable means of compliance. The tabletop exercise may
                                  of compliance that is considered adequate by       involve the third parties identified in the ERP.
                                  the competent authority.
                  Alternative
                  criteria #2,    FUNCTIONAL-TEST-BASED (FTB) METHODS (for SAILs up to and including IV)
                  #3 and #4
                                  If the UAS operator has evidence of the FTB flight hours proportionate to the risk/SAIL of the UAS operation meeting either set of conditions
                  taking
                  credit for      described either in Section E.3(c) or in Section E.3(d) and executed:
                  functional-     (a) within the full operational scope/envelope intended by the UAS operator; and
                  test-based
                  (FTB)           (b) following the operational procedures included in the operation manual,
                  methods



Annex to ED Decision 2025/018/R                                                                                                                               Page 120 of 204
                                                                       AMC & GM to Regulation (EU) 2019/947
                                                                              Issue 1, Amendment 3


                                  then the assurance that the operational procedures are adequate is fulfilled at the level corresponding to the SAIL being demonstrated by
                                  the FTB approach2.
                                  2
                                   As an example, if the number of test cycles supporting the FTB flight hours is proportionate to the risk of a SAIL III operation (i.e. 3 000 FH),
                  Comments
                                  the assurance level for OSO #08 is fulfilled at ‘high’ level.




Annex to ED Decision 2025/018/R                                                                                                                                    Page 121 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


OSO #09 — Remote crew trained and current
       (a)    The UAS operator needs to propose a competency-based, theoretical and practical training that:
              (1)    is appropriate for the operation to be approved allowing the remote crew to control the normal, abnormal and emergency situations
                     potentially resulting from technical issues with the UAS or from external systems supporting the UAS operation, human errors or adverse
                     environmental conditions; and
              (2)    includes proficiency requirements and recurrent training.
       (b)    The entire remote crew (i.e. any person involved in the operation) should receiveundergo competency-based, theoretical and practical training
              specific to their duties (e.g. pre-flight inspection, ground equipment handling, evaluation of the meteorological conditions, etc.).
                                                                                 Level of integrity LEVEL of INTEGRITY
 REMOTE CREW COMPETENCIES                             Low                                              Medium                                    High
                                                   (SAIL I & II)                                     (SAIL III & IV)                         (SAIL V & VI)
                                   The competency-based, theoretical and practical training is adequate for the operation1 and ensures knowledge of:
                                   (a) ensures knowledge of:

                                       (a1) the UAS Regulations;
                                       (b2) airspace operating principles;
                                       (c3) airmanship and aviation safety;
                                       (d4) human performance limitations;
                                       (e5) meteorology and assessment of meteorological conditions;
 OSO #09, OSO
                     Criteria          (f6) navigation/charts;
 #15 and OSO
                     Criterion         (g7) the UAS; and
 #22
                                       (h8) operating operational procedures and the ERP.; and
 Remote crew
 trained and                           (9) the use of external services, including service limitations and system recovery, if any1;
 current
                                   (b) is adequate for the UAS operation, i.e. allows the remote crew to control the normal, abnormal and emergency situations
                                   potentially resulting from technical issues with the UAS or from external systems supporting the UAS operation, human errors or
                                   adverse environmental conditions2,3;

                                   (c) specifies proficiency requirements and training recurrence.
                                   1
                                    If external services are used, the UAS operator is responsible for using the services in the intended manner (e.g. as defined in a service
                     Comments
                                   level agreement) and ensuring that the remote crew is trained to use the services as intended.




Annex to ED Decision 2025/018/R                                                                                                                               Page 122 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


                                   2
                                    The details of the areas to be covered for the different subjects listed above are provided in AMC1 UAS.SPEC.050(1)(d) ‘Theoretical
                                   knowledge subjects for the training of the remote pilot and all personnel in charge of duties essential to the UAS operation in the
                                   “specific” category’, in AMC2 UAS.SPEC.050(1)(d) ‘Practical-skill training of the remote pilot and all personnel in charge of duties
                                   essential to the UAS operation in the “specific” category’ and in AMC3 UAS.SPEC.050(1)(d) ‘UAS operation-specific endorsement
                                   modules’.
                                   13
                                     The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
                                   (see table below).

                                                                                  Level of assurance LEVEL of ASSURANCE
 REMOTE CREW COMPETENCIES                             Low                                         Medium                                          High
                                                   (SAIL I & II)                                (SAIL III & IV)                               (SAIL V & VI)
                                                                               (a) The Ttraining syllabus is available and    The competent authority of the Member
 OSO #09, OSO
                                                                                     kept up to date.                         State or an entity that is designated by the
 #15 and OSO
                     Criteria      Training is self-declared (with evidence    (b) The        UAS       operator  provides    competent authority:
 #22
                     Criterion     available).                                       competency-based, Evidence of the        (a) validates the training syllabus; and
 Remote crew
                                                                                     theoretical and practical training is    (b) verifies      the      remote       crew
 trained and
                                                                                     available.                                   competencies.
 current
                     Comments      N/A                                         N/A                                            N/A

E.5    OSOs related to safe design
       (a)    The objectives of OSO#10 and OSO#12 are to complement the technical containment safety requirements by addressing the risk of a fatality
              while operating over populated areas or assemblies of people.
       (b)    In the scope of this assessment, external systems supporting UAS operations are defined as systems that are not already part of the UAS but are
              used to:
              (1)    launch/take off the UA;
              (2)    make pre-flight checks; or
              (3)    keep the UA within its operational volume (e.g. GNSS, satellite systems, air traffic management, U-space).
              External systems activated/used after a loss of control of the operation are excluded from this definition.
                                                                                          LEVEL of INTEGRITY
                                                  Low                                                      Medium                                                High




Annex to ED Decision 2025/018/R                                                                                                                           Page 123 of 204
                                                                           AMC & GM to Regulation (EU) 2019/947
                                                                                  Issue 1, Amendment 3


                                                                                 When operating over populated areas or assemblies of people, it can be
                                  When operating over populated areas            reasonably expected that a fatality will not occur from any single failure3 of the
                                  or assemblies of people, it can be             UAS or any external system supporting the operation.
                                  reasonably expected that a fatality will       SW and AEH whose development error(s) could directly lead to a failure affecting        Same as
                 Criteria
                                  not occur from any probable1 failure2 of       the operation in such a way that it can be reasonably expected that a fatality will     medium
                                  the UAS or any external system                 occur, are developed to a standard considered adequate by the competent
                                  supporting the operation.                      authority and/or in accordance with means of compliance acceptable to that
                                                                                 authority.
                                  1
                                     For the purpose of this assessment,
 OSO #10
                                  the term ‘probable’ should be
 & OSO #12
                                  interpreted in a qualitative way as,
                                  ‘anticipated to occur one or more times        3
                                                                                   Some structural or mechanical failures may be excluded from the no-single
                                  during the entire system/operational
                                                                                 failure criterion if it can be shown that these mechanical parts were designed to
                 Comments         life of a UAS’.
                                  2                                              a standard considered adequate by the competent authority and/or in
                                    Some structural or mechanical failures
                                                                                 accordance with a means of compliance acceptable to that authority
                                  may be excluded from the criterion if it
                                  can be shown that these mechanical
                                  parts were designed according to
                                  aviation industry best practices.

                                                                                                     LEVEL of ASSURANCE
                                                               Low                                                Medium                                         High
                                                                                                Same as low. In addition, the level of
                                      A design and installation appraisal is available. In
                                                                                                integrity claimed is substantiated by            The competent authority should
                                      particular, this appraisal shows that:
                                                                                                analysis and/or test data with supporting        request the applicant to use a UAS for
                                      (a)       the design and installation features
                                                                                                evidence.                                        which EASA has issued a type
                                      (independence, separation and redundancy) satisfy
OSO #10           Criteria                                                                      If the operation is classified as SAIL IV, the   certificate     or   restricted  type
                                      the low integrity criterion; and
& OSO #12                                                                                       competent authority should request the           certificate in accordance with Annex I
                                      (b)       particular risks relevant to the ConOps (e.g.
                                                                                                applicant to use a UAS for which EASA has        (Part 21) to Regulation (EU) No
                                      hail, ice, snow, electromagnetic interference, etc.)
                                                                                                verified the claimed integrity through a         748/2012.
                                      do not violate the independence claims, if any.
                                                                                                DVR.
                  Comments            N/A                                                       N/A                                              N/A




Annex to ED Decision 2025/018/R                                                                                                                                         Page 124 of 204
                                                                     AMC & GM to Regulation (EU) 2019/947
                                                                            Issue 1, Amendment 3


E.6    OSOs related to the deterioration of external systems supporting UAS operations

OSO #13 — External services supporting UAS operations are adequate for the UAS operation
       For the purpose of the SORA and this specific OSO, the term ‘external services supporting UAS operations’ encompasses any service providers necessary
       for the safety of the flight1, such as:
       —      communication service providers;
       —      navigation service providers (e.g. GNSS);
       —      and U-space service providers48;
       —      externally provided electrical power (e.g. in the case where no emergency backup generator is available and the safety of the flight is dependent
              on continuous power supply).
       The interface between the UAS operator and the external service provider(s) may take the form of a service level agreement (SLA) or a similar document.



 DETERIORATION OF EXTERNAL                                                          Level of integrity LEVEL of INTEGRITY
 SYSTEMS SUPPORTING UAS
                                                    Low                                     Medium                                             High
 OPERATIONS
                                                 (SAIL I & II)                              (SAIL III)                                    (SAIL IV to VI)
 OSO #13                            The applicantUAS operator ensures that the level of performance for any externally provided service necessary for the safety of the
 External           Criteria        flight1 is adequate for the intended UAS operation.
 services           Criterion       If the externally provided service requires communication between the UAS operator and the service provider, the applicant UAS
 supporting UAS                     operator ensures there is effective communication to support the service provision.

48
   External service should be understood as any service that is provided to the UAS operator, which is necessary to ensure the safety of a UAS operation and is provided by
a service provider other than the UAS operator. Examples of external services are:
- provision of geographical zones data and geographical limitations (including orography);
- collection and transfer of occurrence data;
- training and assessment of remote pilots;
- communication services that support the C2 link and any other safety-related communication;
- services that support navigation, e.g. GNSS services (compliance with requirement UAS.STS-01.030(6) could be ensured by referring to the conditions of use of such
   services in the corresponding Service Definition Document (SDD) or an equivalent one if available.);
- provision of services related to flight planning and management, including related safety assessments; and
- U-space services, which are defined in the corresponding regulation(s) and may include one or more of the above-mentioned services.


Annex to ED Decision 2025/018/R                                                                                                                             Page 125 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3



 DETERIORATION OF EXTERNAL                                                            Level of integrity LEVEL of INTEGRITY
 SYSTEMS SUPPORTING UAS
                                                  Low                                    Medium                                             High
 OPERATIONS
                                               (SAIL I & II)                             (SAIL III)                                    (SAIL IV to VI)
 operations are                   Roles and responsibilities between the applicantUAS operator and the external service provider are defined.
 adequate for
 the UAS
 operation

                                  1
                    Comments          A service whose loss would directly lead to a loss of control of the operation as identified per OSO #05.
                                                                                                                           Requirements for contracting services with the
                                                                                                                           service provider(s) may be derived from ICAO
                    Comments      N/A                                         N/A
                                                                                                                           Standards and Recommended Practices (SARPs)
                                                                                                                           that are currently under development.


 DETERIORATION OF EXTERNAL                                                          Level of assurance LEVEL of ASSURANCE
 SYSTEMS SUPPORTING UAS
                                                 Low                                               Medium                                                  High
 OPERATIONS
                                              (SAIL I & II)                                        (SAIL III)                                         (SAIL IV to VI)
                                                                        The applicantUAS operator has supporting evidence that the
                                                                        required level of performance for any externally provided           Same as ‘medium’. In addition:
                                  The applicantUAS operator             service required for the safety of the flight can be achieved for   (a) the      evidence     of     the
                                  declares1 that the requested          the full duration of the operation mission.                             performance of an externally
 OSO #13                          level of performance for any          This may take the form of an SLA or any official commitment             provided service is achieved
 External           Criteria      externally provided service           that prevails between a Sservice Pprovider and the                      through demonstrations; and
 services           Criterion     necessary for the safety of the       applicantUAS operator on relevant aspects of the service            (b) the competent authority of the
 supporting UAS                   flight is achieved. (without          (including quality, availability and responsibilities).                 Member State or an entity that
 operations are                   evidence being necessarily            The applicantUAS operator has means to monitor externally               is designated by the competent
 adequate for                     available).                           provided services that affect flight-critical systems and takes         authority validates the claimed
 the UAS                                                                appropriate actions if real-time performance could lead to the          level of integrity.
 operation                                                              loss of control of the operation.
                                  N/A
                    Comments      1                                     N/A                                                                 N/A
                                    Supporting evidence for this
                                  declaration  may     still be



Annex to ED Decision 2025/018/R                                                                                                                                 Page 126 of 204
                                                                        AMC & GM to Regulation (EU) 2019/947
                                                                               Issue 1, Amendment 3


                                  requested by the competent
                                  authority.
                                  Supporting evidence may take
                                  the form of a service level
                                  agreement (SLA) or any official
                                  commitment         that    prevails
                                  between a service provider and
                                  the UAS operator on relevant
                                  aspects of the service (including
                                  quality,      availability     and
                                  responsibilities).
                                  As an example, if a UAS operator
                                  uses an external surveillance
                                  service, it should have evidence
                                  available supporting the claim
                                  that the service meets the
                                  performance requirements of
                                  Annex D to this AMC.

E.7    OSOs related to human error




Annex to ED Decision 2025/018/R                                                                                Page 127 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3


OSO #16 — Multi-crew coordination
       This OSO applies only to those personnel directly involved in the flight operation.

                                                                                  Level of integrity LEVEL of INTEGRITY
 HUMAN ERROR MULTI-CREW
                                                 Low                                      Medium                                         High
 COORDINATION
                                             (SAIL I & II)                              (SAIL III & IV)                              (SAIL V & VI)
                                    The UAS operator develops Pprocedures(s) to ensure coordination between the crew members, and robust and effective
                                    communication channels is (are) available and ast a minimum cover:
                     Criterion #1   (a)     assignment of tasks to the crew;, and
                     (Procedures)   (b)     establishment of step-by-step communications, including the establishment and use of proper phraseology between the
                                    remote crew members involved in the aerial part of the operation 1.1

                                    1
                                      The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
                     Comments
                                    (see the table below).
                     Criterion #2   Remote crew training covers       Same as ‘low’. In addition, the remote crew2
                                                                                                                             Same as ‘medium’.
                     (Training)     multi-crew coordination           receives CRM3 training.
                                                                      2
                                                                        In the context of the SORA In line with definition
                                                                      I.110 ‘Remote pilot (in command)’ provided in Annex
                                                                      I to this AMC, the term ‘remote crew’ refers to any
 OSO #16 Multi-
                                                                      person that performs duties essential to the safety
 crew
                                                                      of flight (e.g. AOs, UA observers) involved in the
 coordination        Comments       N/A                                                                                      N/A
                                                                      mission.
                                                                      3
                                                                        CRM training focuses on the effective use of all the
                                                                      remote crew to assure a safe and efficient
                                                                      operation, reducing error, avoiding stress and
                                                                      increasing efficiency.
                                                                      Communication devices comply with standards
                                                                      considered adequate by the competent authority Same               as   ‘medium’.     In     addition,
                                                                      and/or in accordance with a means of compliance Ccommunication devices are redundant4 and
                     Criterion #3                                     acceptable to that authority.                          comply with standards considered adequate
                     (Communicati   N/A
                     on devices)                                      The UAS operator determines that the performance by the competent authority and/or in
                                                                                                                             accordance with a means of compliance
                                                                      of communication devices is adequate to safely
                                                                                                                             acceptable to that authority.
                                                                      conduct the UAS operation.




Annex to ED Decision 2025/018/R                                                                                                                            Page 128 of 204
                                                                        AMC & GM to Regulation (EU) 2019/947
                                                                               Issue 1, Amendment 3


                                                                           The remote crew has the means to check the
                                                                           performance of the communication devices at
                                                                           intervals deemed appropriate to ensure the
                                                                           performance continues to meet the operational
                                                                           requirements throughout the operation.
                                                                                                                                   4
                                                                                                                                    This implies the provision of an extra device
                     Comments            N/A                               N/A                                                     to cope with the failure of the first device.


                                                                                                    LEVEL of ASSURANCE
 HUMAN ERROR                                             Low                                              Medium                                            High
                                                      (SAIL I & II)                                    (SAIL III & IV)                                  (SAIL V & VI)
                                                                                 (a) Procedures are validated against standards             Same as ‘medium’. In addition:
                                          (a) Procedures are do not require          considered adequate by the competent authority         (a) flight tests performed to
                                              validation validated against           of the Member State and/or in accordance with the          validate the procedures cover
                                              either a standard or a means           means of compliance acceptable to that authority1.         the complete flight envelope or
                                              of compliance considered           (b) The adequacy of the procedures is proven through:          are proven to be conservative;
                     Criterion #1             adequate by the competent              (1) dedicated flight tests; or                             and
                     (Procedures)             authority of the Member                (2) simulation,          provided     that       the   (b) the procedures, flight tests and
                                              State.                                       representativeness of the simulation means is        simulations are validated by the
                                          (b) The     adequacy    of   the                 proven valid for the intended purpose with           competent authority of the
                                              procedures and checklists is                 positive results; or                                 Member State or an entity
                                              declared.                              (3) any other means acceptable to the                      designated by the competent
 OSO #16 Multi-                                                                            competent authority.                                 authority.
 crew                                                                            1
                                                                                   AMC2 UAS.SPEC.030(3)(e) (‘Operational procedures
 coordination        Comments             N/A                                    for medium and high levels of robustness’) is considered   N/A
                                                                                 an acceptable means of compliance.
                                          FUNCTIONAL-TEST-BASED (FTB) METHODS (for SAILs up to and including IV):
                     Alternative
                                          If the UAS operator has evidence of the FTB flight hours proportionate to the risk/SAIL of
                     criterion #1
                     taking credit for    the operation meeting either set of conditions described either in Section 3(c) or in Section
                                          3(d) and executed:                                                                                N/A3
                     functional-test-
                     based (FTB)          ●     within the full operational scope/envelope intended by the UAS operator; and
                     methods
                                          ●     following the operational procedures referred to in the operational authorisation,



Annex to ED Decision 2025/018/R                                                                                                                                  Page 129 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


                                                                                                  LEVEL of ASSURANCE
 HUMAN ERROR                                            Low                                            Medium                                            High
                                                    (SAIL I & II)                                    (SAIL III & IV)                                 (SAIL V & VI)
                                      then the assurance that the operational procedures are adequate is fulfilled at the level
                                      corresponding to the SAIL being demonstrated by the FTB approach2.
                                      2                                                                                                   3
                                        As an example, if the number of test cycles supporting the FTB flight hours is proportionate        FTB methods are not considered
                     Comments         to the risk of a SAIL III operation (i.e. 3 000 FH), the assurance level for OSO #16 Criterion #1   feasible for operations with a SAIL V
                                      is fulfilled at ‘medium’ level.                                                                     or VI.
                                                                                                                                          The competent authority of the
                                                                                                                                          Member State or an entity that is
                                                                            (a) Training syllabus is available.                           designated by the competent
                     Criterion #2     Training is self-declared (with       (b) The UAS operator provides competency-based,               authority:
                     (Training)       evidence available).                      Evidence of the theoretical and practical training is     (a) validates the training syllabus;
                                                                                available.                                                     and
                                                                                                                                          (b) verifies the remote crew
                                                                                                                                               competencies.
                     Comments         N/A                                   N/A                                                           N/A
                                                                            The applicantUAS operator has supporting evidence             Unless the communication device is
                                                                            that the required level of integrity is achieved. This is     included in the UAS type design, T
                                                                            typically done by testing, analysis, simulation11,            the competent authority or an
                                                                            inspection, design review or through operational              entity that is designated by the
                     Criterion #3                                           experience.                                                   competent authority validates the
                     (Communication   N/A                                                                                                 claimed level of integrity. should
                     devices)                                                                                                             request the applicant to operate a
                                                                                                                                          UAS designed by an organisation
                                                                                                                                          approved by EASA according to
                                                                                                                                          Subpart J of Annex I (Part 21) to
                                                                                                                                          Regulation (EU) No 748/2012.
                                                                            1
                                                                              When simulation is performed, the validity of the
                     Comments         N/A                                   targeted environment that is used in the simulation           N/A
                                                                            needs to be justified.




Annex to ED Decision 2025/018/R                                                                                                                                Page 130 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


OSO #17 — Remote crew is fit to operate
        (a)    For the purpose ofSORA, the expression ‘fit to operate’ should be interpreted as physically and mentally fit to perform their duties and safely
               discharge their responsibilities.
        (b)    Fatigue and stress are contributingory factors to human error. Therefore, to ensure that vigilance is maintained at a satisfactory level of safety,
               consideration may be given to the following:
               (1)    remote crew workload and duty times;
               (2)    regular breaks;
               (3)    rest periods;
               (4)    personal protective equipment (PPE)49;
               (5)    workplace environment, including ergonomics of the workstation49; and
               (46) handover/takeover procedures.
                                                                                     Level of integrity LEVEL of INTEGRITY
 HUMAN ERROR                                       Low                                            Medium                                           High
                                                (SAIL I & II)                                   (SAIL III & IV)                                (SAIL V & VI)
                                   The applicantUAS operator has a
                                                                          Same as ‘low’. In addition:
                                   policy defining the criteria1 and the
                                                                         (a) Duty, flight duty and resting times for the remote Same as M‘medium’. In addition:
                                   means on how the remote crew can
                                                                             crew are defined by the applicantUAS operator and (a) The remote crew is medically fit.,
                     Criteria      declare themselves fit to operate
                                                                             are adequate for the operation.                    (b) A fatigue risk management system
                     Criterion     before starting their duty, and on
                                                                         (b) The UAS operator defines requirements                   (FRMS) is in place to manage any
 OSO #17                           how to report themselves unfit, if
                                                                             appropriate for the remote crew to operate the          escalation in duty/flight duty times.
 Remote crew is                    required, during their shift.
                                                                             UAS.
 fit to operate                    conducting any operation.
                                   N/A
                                   1
                                     Criteria should take into account
                     Comments      national legislation and may cover N/A                                                        N/A
                                   drugs (including prescriptions) and
                                   alcohol consumption.



49
     In accordance with national occupational safety and health regulations.


Annex to ED Decision 2025/018/R                                                                                                                           Page 131 of 204
                                                                  AMC & GM to Regulation (EU) 2019/947
                                                                         Issue 1, Amendment 3


                                                                                        LEVEL of ASSURANCE
 HUMAN ERROR                                   Low                                     Medium                                                 High
                                            (SAIL I & II)                            (SAIL III & IV)                                     (SAIL V & VI)
                                                                                                                         Same as ‘medium’. In addition:
                                                                                                                        (a) Medical standards considered adequate
                                                                                                                            by the competent authority and/or the
                                                                                                                            means of compliance acceptable to that
                                  The policy defining the criteria
                                                                     Same as ‘low’. In addition:                            authority are established and the
                                  and the means for to define how
                                                                    (a) Remote crew duty, flight duty and the resting       competent authority of the Member State
                                  the remote crew to declares
                                                                        time policy are documented.                         or an entity that is designated by the
                                  themselves fit to operate before
                                                                    (b) Remote crew duty cycles are logged and cover        competent authority verifies that the
                                  starting their duty and to report
                                                                        ast a minimum:                                      remote crew is medically fit.
 OSO #17             Criteria     themselves unfit, if required,
                                                                        1.(1) when the remote crew members’s duty       (b) The competent authority of the Member
 Remote crew is      Criterion    during their shift (before an
                                                                        day commences;,                                     State or an entity that is designated by the
 fit to operate                   operation) is documented.
                                                                        2.(2) when the remote crew members are free         competent authority validates the
                                  The remote crew fit-to-operate
                                                                        from duties;, and                                   duty/flight duty times.
                                  declaration       (before     an
                                                                        3.(3) resting times within the duty cycle.      (c) If an The FRMS is used, it is validated and
                                  operation) is based on a policy
                                                                                                                            monitored by the competent authority of
                                  defined by the applicant.
                                                                                                                            the Member State or by an entity that is
                                                                                                                            designated by the competent authority
                                                                                                                            and internally monitored by the UAS
                                                                                                                            operator.
                     Comments     N/A                              N/A                                                   N/A




Annex to ED Decision 2025/018/R                                                                                                                         Page 132 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


OSO #18 — Automatic protection of the flight envelope from human errors
       (a)    Each UA is designed with a flight envelope that describes its safe performance limits with regard to relevant flight parameters such as minimum
              and maximum operational speeds, and its operating structural strength.
       (b)    Automatic protection of the flight envelope is intended to prevent the remote pilot from operating the UA outside its flight envelope. If the
              applicantUAS operator demonstrates that the remote-pilot remote pilot is not in the loop, this OSO is not applicable.
       (c)    A UAS implementing such an automatic protection function will ensure that the UA is operated within an acceptable flight envelope margin even
              in the case of incorrect remote-pilot control inputs (human errors).
       (d)    UAS without automatic protection functions are susceptible to incorrect remote-pilot control inputs (human errors), which can result in the loss
              of the UA if the designed performance limits of the UA aircraft are exceeded.
       (e)    Failures or development errors of the flight envelope protection are addressed in OSOs #5, #10 and #12.
                                                                                              LEVEL of INTEGRITY
         HUMAN ERROR                                     Low                                               Medium                                 High
                                                       (SAIL III)                                          (SAIL IV)                          (SAIL V & VI)
                                  The UAS flight control system incorporates automatic
                                  protection of the flight envelope to prevent the        The UAS flight control system incorporates automatic protection of the flight
                    Criteria      remote pilot from making any single input under         envelope to ensure the UA remains within the flight envelope or ensures a
 OSO #18
                    Criterion     normal operating conditions that would cause the UA     timely recovery to the designed operational flight envelope following remote-
 Automatic
                                  to exceed its flight envelope or prevent it from        pilot error(s).1,2.
 protection of
                                  recovering in a timely fashion.
 the flight                                                                               1
                                                                                            The distinction between a medium and a high level of robustness for this
 envelope from
                                                                                          criterion is achieved through the level of assurance (see table below).
 human errors                                                                             2
                    Comments      N/A                                                       Compared to the low level of robustness, medium and high levels need to
                                                                                          address any operating conditions (normal, abnormal and emergency) and the
                                                                                          potential for multiple errors.




Annex to ED Decision 2025/018/R                                                                                                                        Page 133 of 204
                                                                  AMC & GM to Regulation (EU) 2019/947
                                                                         Issue 1, Amendment 3


                                                                                        LEVEL of ASSURANCE
        HUMAN ERROR                                  Low                                          Medium                                         High
                                                   (SAIL III)                                     (SAIL IV)                                  (SAIL V & VI)
                                  The UAS designer develops the automatic
                                  protection of the flight envelope has been
                                                                                                                                 The competent authority should
                                  developed in-house or out of the box (e.g.
                                                                                The competent authority should request the       request the UAS operator should to
                                  using commercial off-the-shelf elements),
                                                                                applicant UAS operator should to use a UAS for   use a UAS for which EASA has issued a
                                  without following specific standards.
                   Criteria                                                     which EASA has verified the claimed integrity    type certificate or a restricted type
 OSO #18
                   Criterion                                                    through a design verification report (DVR)       certificate in accordance with Annex I
 Automatic                        The UAS operator should use a UAS for which
                                                                                issued following an application from the UAS     (Part 21) to Regulation (EU) No
 protection of                    the UAS designer has issued a statement of
                                                                                designer.                                        748/2012 following an application
 the flight                       compliance with the MoC to OSO #181 using
                                                                                                                                 from the UAS designer.
 envelope from                    the form attached to the MoC.
 human errors
                                  N/A
                                  1
                                    https://www.easa.europa.eu/en/document-
                                                                                N/A
                   Comments       library/product-certification-                                                                 N/A
                                  consultations/means-compliance-moc-design-
                                  uas-operated-sail




Annex to ED Decision 2025/018/R                                                                                                                        Page 134 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3


OSO #19 — Safe recovery from human errors
       (a)    This OSO addresses the risk of human errors which may affect the safety of the operation if not prevented or detected and recovered in a timely
              fashion.
              (i)     Errors can be made by anyone involved in the operation.
              (ii)    An example could be a human error leading to the incorrect loading of the payload, with the risk of it falling off the UA during the operation.
              (iii)   Another example could be a human error not to extend the antenna mast, thus reducing the C2 link coverage.
              Note: tThe flight envelope protection is excluded from this OSO since it is specifically covered by OSO #18.
       (b)    This OSO covers: the UAS design, i.e. systems detecting and/or recovering from human errors (e.g. safety pins, use of acknowledgment features,
              fuel or energy consumption monitoring functions, etc.).
              i)      procedures and lists,
              ii)     training, and
              iii)    UAS design, i.e. systems detecting and/or recovering from human errors (e.g. safety pins, use of acknowledgment features, fuel or energy
                      consumption monitoring functions …)
       (c)    Operational procedures and training are covered in OSO #08 and OSO #09 respectively.




Annex to ED Decision 2025/018/R                                                                                                                      Page 135 of 204
                                                                     AMC & GM to Regulation (EU) 2019/947
                                                                            Issue 1, Amendment 3


                                                                                                LEVEL of INTEGRITY
           HUMAN ERROR                                   Low                                               Medium                                           High
                                                       (SAIL III)                                        (SAIL IV & V)                                    (SAIL VI)
                                        Procedures and checklists that mitigate the risk of potential human errors from any person involved with the mission are defined
                     Criterion #1       and used.
                     (Procedures and    Procedures provide at a minimum:
                     checklists)        —         a clear distribution and assignment of tasks, and
                                        —         an internal checklist to ensure staff are adequately performing their assigned tasks.
                     Comments           N/A                                         N/A                                                           N/A
                                                                     1
                     Criterion #2       —         The remote crew is trained to use procedures and checklists.
                     (Training)         —         The remote crew1 receives CRM2 training.3
                                        1
                                          In the context of SORA, the term ‘remote crew’ refers to any person involved in the mission.
                                        2
                                          CRM training focuses on the effective use of all the remote crew to ensure a safe and efficient operation, reducing error, avoiding
 OSO #19
                     Comments           stress and increasing efficiency.
 Safe recovery                          3
                                          The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of
 from Hhuman
                                        assurance (see table below).
 Eerror
                                                                                    Systems detecting and/or recovering from human errors
                                        Systems detecting and/or recovering
                     Criterion #3                                                   are developed to standards considered adequate by the
                                        from human errors are developed                                                                           Same as ‘medium’.
                     (UAS design)                                                   competent authority and/or in accordance with a means of
                                        according to industry best practices.
                                                                                    compliance acceptable to that authority.
                                                                                    N/A
                                                                                    1
                                                                                       National Aviation Authorities (NAAs) may define the
                                                                                    standards and/or the means of compliance they consider
                     Comments           N/A                                                                                                       N/A
                                                                                    adequate. The SORA Annex E will be updated at a later
                                                                                    point in time with a list of adequate standards based on the
                                                                                    feedback provided by the NAAs.

                                                                                              LEVEL of ASSURANCE
          HUMAN ERROR                                     Low                                            Medium                                          High
                                                        (SAIL III)                                     (SAIL IV & V)                                   (SAIL VI)
                                       (a)      Procedures and checklists are not                                                         Same as medium. In addition:
                                                                                      (a)      Procedures and checklists are
 OSO #19                               validated against either a standard or a                                                           (a)       Flight tests performed to
                    Criterion #1                                                      validated against standards considered
 Safe recovery                         means of compliance considered adequate                                                            validate the procedures and
                    (Procedures                                                       adequate by the competent authority of the
 from human                            by the competent authority of the MS.                                                              checklists cover the complete
                    and checklists)                                                   MS and/or in accordance with the means of
 error                                 (b)      The adequacy of the procedures                                                            flight envelope or are proven to
                                                                                      compliance acceptable to that authority1.
                                       and checklists is declared.                                                                        be conservative.


Annex to ED Decision 2025/018/R                                                                                                                               Page 136 of 204
                                                                   AMC & GM to Regulation (EU) 2019/947
                                                                          Issue 1, Amendment 3


                                                                                             LEVEL of ASSURANCE
          HUMAN ERROR                                  Low                                              Medium                                          High
                                                     (SAIL III)                                       (SAIL IV & V)                                   (SAIL VI)
                                                                                     (b)       The adequacy of the procedures and       (b)       The procedures,
                                                                                     checklists is proven through:                      checklists, flight tests and
                                                                                         (1) dedicated flight tests, or                 simulations are validated by the
                                                                                         (2) simulation, provided that the              competent authority of the MS or
                                                                                         representativeness of the simulation means an entity that is designated by the
                                                                                         is proven valid for the intended purpose       competent authority.
                                                                                         with positive results; or
                                                                                         (3) any other means acceptable to the
                                                                                         competent authority of the MS.
                                                                                     1
                                                                                       AMC2 UAS.SPEC.030(3)(e) (Operational
                                                                                     procedures for medium and high levels of
                    Comments       N/A                                                                                                  N/A
                                                                                     robustness) is considered an acceptable means
                                                                                     of compliance.
                    Criterion #2   Consider the criteria defined for the level of assurance of the generic remote crew training OSO (i.e. OSO #09, OSO #15 and OSO
                    (Training)     #22) corresponding to the SAIL of the operation.
                    Comments       N/A                                               N/A                                                N/A
                                                                                     The applicant UAS designer has supporting
                                                                                     evidence that the required level of integrity is
                                                                                     achieved. That evidence is provided through
                                                                                     testing, analysis, simulation2, inspection, design
                                                                                                                                         The competent authority should
                                                                                     review or operational experience.
                                   The applicant UAS designer declares that the                                                         request the applicant UAS
                                                                                     If the operation is classified as SAIL IV, the
                                   required level of integrity has been                                                                 operator should to use a UAS for
                                                                                     competent authority should request the
                                   achieved1.                                                                                           which EASA has issued a type
                                                                                     applicant UAS operator should to use a UAS for
                    Criterion #3   The UAS operator should use a UAS for which                                                          certificate or a restricted type
                                                                                     which EASA has verified the claimed integrity
                    (UAS design)   the UAS designer has issued a statement of                                                           certificate in accordance with
                                                                                     through a design verification report (DVR)
                                   compliance with MoC to OSO #19/#201 using                                                            Annex I                      (Part 21)
                                                                                     issued following an application from the UAS
                                   the form attached to the MoC.                                                                        to Regulation (EU) No 748/2012
                                                                                     designer.
                                                                                                                                        following an application from the
                                                                                     If the operation is classified as SAIL V, the
                                                                                                                                        UAS designer.
                                                                                     competent authority should request the
                                                                                     applicant UAS operator should to use a UAS for
                                                                                     which EASA has issued a type certificate or a
                                                                                     restricted type certificate in accordance with


Annex to ED Decision 2025/018/R                                                                                                                              Page 137 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


                                                                                            LEVEL of ASSURANCE
          HUMAN ERROR                                Low                                               Medium                                       High
                                                   (SAIL III)                                        (SAIL IV & V)                                (SAIL VI)
                                                                                    Annex I (Part 21) to Regulation (EU)
                                                                                    No 748/2012 following an application from the
                                                                                    UAS designer.
                                  1 Supporting evidence may or may not be
                                  available.
                                  1                                                 2
                                   https://www.easa.europa.eu/en/document-            When simulation is performed, the validity of
                     Comments     library/product-certification-                    the targeted environment that is used in the      N/A
                                  consultations/means-compliance-moc-               simulation needs to be justified.
                                  design-uas-operated-sail




OSO #20 — A human factors evaluation has been performed and the HMI has been found appropriate for the intended UAS operation mission
                                                                                             LEVEL of INTEGRITY
           HUMAN ERROR                                Low                                            Medium                                       High
                                                  (SAIL II & III)                                  (SAIL IV & V)                                (SAIL VI)
                                                                                                                                 Same as ‘medium’. In addition, the
                                                                                                                                 human factors evaluation is expected
 OSO #20                                                                                                                         to cover:
 A Hhuman                                                                                                                        (a) an appraisal to check that the
 Ffactors                                                                                                                            remote crew workload remains
 evaluation has                                                                                                                      acceptable in both normal and
                                   The UAS information and control interfaces are clearly and succinctly presented and do not
 been performed       Criteria                                                                                                       emergency situations;
                                   confuse, cause unreasonable fatigue, or contribute to remote crew errors that could
 and the HMI has      Criterion
                                   adversely affect the safety of the operation.
 been found                                                                                                                      (b) an appraisal of the efficiency of the
 appropriate for                                                                                                                     emergency procedures (efficacy of
 the intended UAS                                                                                                                    the actions, expected potential
 operation mission                                                                                                                   latencies);
                                                                                                                                 (c) analyses to check if prioritisation
                                                                                                                                     of alarms and emergency



Annex to ED Decision 2025/018/R                                                                                                                          Page 138 of 204
                                                                  AMC & GM to Regulation (EU) 2019/947
                                                                         Issue 1, Amendment 3


                                                                                                                                       procedures should be put in place
                                                                                                                                       to organise emergency procedures
                                                                                                                                       in such a way that they remain
                                                                                                                                       adapted to the criticality of the
                                                                                                                                       situation.
                                   If an electronic means is used to support the remote crew members potential airspace observer(s) VOs in their role to maintain
                                   awareness of the position of the unmanned aircraft, its HMI:
                                   — is sufficient to allow the remote crew members potential airspace observer(s)) VO to determine the position of the UA during
                      Comments     operation; and
                                   — does not degrade the remote crew members’ potential airspace observer(s)) VO ability to:
                                      — scan the airspace visually where the unmanned aircraft is operating for any potential collision hazard; and
                                      — maintain effective communication with the remote pilot at all times.

                                                                                          LEVEL of ASSURANCE
          HUMAN ERROR                               Low                                          Medium                                           High
                                                (SAIL II & III)                                (SAIL IV & V)                                    (SAIL VI)
                                                                                 Same as L‘low’ but the HMI evaluation is
                                                                                 based on demonstrations or simulations.1
                                                                                 The competent authority should request          Same as M‘medium’. In addition, EASA
                                  The applicant UAS designer conducts a
                                                                                 EASA to witness the HMI evaluation of the       witnesses the HMI evaluation of the UAS
                                  human factors evaluation of the UAS to
 OSO #20                                                                         UAS.                                            and the competent authority of the MS or
                                  determine whether the HMI is appropriate
 A Hhuman                                                                        For operations classified in SAIL IV, the       an entity that is designated by the
                                  for the intended UAS operation mission. The
 Ffactors                                                                        UAS operator should use a UAS for which         competent authority witnesses the HMI
                                  HMI evaluation is based on inspection or
 evaluation has                                                                  EASA has issued a design verification           evaluation of the possible electronic
                      Criteria    analyses.
 been performed                                                                  report (DVR) following an application           means used by the AO. the UAS operator
                      Criterion   The adequacy of the result of the HMI
 and the HMI has                                                                 from the UAS designer.                          should use a UAS for which EASA has
                                  evaluation is declared.
 been found                                                                      For operations classified in SAIL V, the UAS    issued a type certificate or a restricted
                                  The UAS operator should use a UAS for which
 appropriate for                                                                 operator should use a UAS for which EASA        type certificate in accordance with Annex
                                  the UAS designer has issued a statement of
 the intended UAS                                                                has issued a type certificate or a restricted   I (Part 21) to Regulation (EU) No
                                  compliance with MoC to OSO #19/#201 using
 operation                                                                       type certificate in accordance with Annex       748/2012 following an application from
                                  the form attached to the MoC.
 mission                                                                         I (Part 21) to Regulation (EU) No 748/2012      the UAS designer.
                                                                                 following an application from the UAS
                                                                                 designer.
                                                                                 1
                                                                                     When simulation is performed, the
                      Comments    N/A                                                                                            N/A
                                                                                 validity of the targeted environment that



Annex to ED Decision 2025/018/R                                                                                                                             Page 139 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3


                                      1
                                       https://www.easa.europa.eu/en/document-         is used in the simulation needs to be
                                      library/product-certification-                   justified.
                                      consultations/means
                                      If the UAS designer has evidence of the FTB
                                      flight hours proportionate to the risk/SAIL of
                                      the operation meeting either set of
                                      conditions described either in Section 3(c) or
                                      in Section 3(d) and executed:
                      Alternative
                      criterion for   (a) within     the    full   operational
                      taking credit       scope/envelope intended by the UAS
                      for                 operator; and                                N/A
                      functional-
                      test-based      (b) following the operational procedures
                      (FTB)               and the remote crew training referred to
                      methods             in the operational authorisation,

                                      then the assurance that the operational
                                      procedures are adequate is fulfilled at the
                                      level corresponding to the SAIL being
                                      demonstrated by the FTB approach2.
                                      2
                                        As an example, if the number of test cycles
                                      supporting the FTB flying hours is
                      Comments        proportionate to the risk of a SAIL III          N/A
                                      operation (i.e. 3 000 FH), the assurance level
                                      for OSO #20 is fulfilled at ‘low’ level.




Annex to ED Decision 2025/018/R                                                                                                Page 140 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


E.8    OSOs related to adverse operating conditions

OSO #23 — Environmental conditions for safe operations are defined, measurable and adhered to
                                                                                              LEVEL of INTEGRITY
       ADVERSE OPERATING
                                                       Low                                            Medium                                           High
          CONDITIONS
                                                    (SAIL I & II)                                   (SAIL III & IV)                                (SAIL V & VI)
                   Criterion #1
                                   The environmental conditions for safe operations are defined and reflected in the UAS flight manual or equivalent document.1.
                   (Definition)
                                   1
 OSO #23                             The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
 Environmental     Comments        (see table below). For SAL III, compliance with the EASA MoC to OSO #24 already determines compliance with OSO #23. Refer to
 conditions for                    OSO #24.
 safe              Criterion #2    Procedures to evaluate environmental conditions before and during the mission (i.e. real-time evaluation) are available and include
 operations are    (Procedures)    assessment of meteorological conditions (METAR, TAFOR, etc.) with a simple recording system.2
                                   2
 defined,                            The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
                   Comments
 measurable                        (see table below).
 and adhered       Criterion #3
 to                                Training covers assessment of meteorological conditions.3
                   (Training)
                                   3
                                     The distinction between a low, a medium and a high level of robustness for this criterion is achieved through the level of assurance
                   Comments
                                   (see table below).

                                                                                             LEVEL of ASSURANCE
       ADVERSE OPERATING
                                                 Low                                           Medium                                                  High
          CONDITIONS
                                              (SAIL I & II)                                  (SAIL III & IV)                                       (SAIL V & VI)
                                                                         The applicant UAS designer has supporting evidence
                                                                         that the required level of integrity is achieved. This is
                                                                                                                                     The competent authority should request
 OSO #23                                                                 typically done by testing, analysis, simulation,
                                                                                                                                     the applicant UAS operator should to use
 Environmental                                                           inspection, design review or through operational
                                   The applicant UAS designer                                                                        a UAS for which EASA has issued a type
 conditions for     Criterion #1                                         experience.
                                   declares that the required level of                                                               certificate or a restricted type certificate
 safe operations    (Definition)                                         If the operation is classified as SAIL IV, the competent
                                   integrity has been achieved.                                                                      in accordance with Annex I (Part 21) to
 are defined,                                                            authority should request the applicant UAS operator
                                                                                                                                     Regulation (EU) No 748/2012 following
 measurable and                                                          should to use a UAS for which EASA has issued a
                                                                                                                                     an application from the UAS designer.
 adhered to                                                              design verification report (DVR) following an
                                                                         application from the UAS designer.
                    Comments       N/A



Annex to ED Decision 2025/018/R                                                                                                                                Page 141 of 204
                                                                     AMC & GM to Regulation (EU) 2019/947
                                                                            Issue 1, Amendment 3


                                   .
                                                                          (a)       Procedures are validated against standards
                                                                          considered adequate by the competent authority of
                                                                                                                                 Same as medium. In addition:
                                   (a)      Procedures do not             the MS and/or in accordance with the means of
                                                                                                                                 (a)      Flight tests performed to
                                   require validation against either a    compliance acceptable to that authority1.
                                                                                                                                 validate the procedures cover the
                                   standard or a means of                 (b)       The adequacy of the procedures is proven
                                                                                                                                 complete flight envelope or are proven
                                   compliance considered adequate         through:
                    Criterion #2                                                                                                 to be conservative.
                                   by the competent authority of          (1)       dedicated flight tests, or
                    (Procedures)                                                                                                 (b)      The procedures, flight tests and
                                   the MS.                                (2)       simulation, provided that the
                                                                                                                                 simulations are validated by the
                                   (b)      The adequacy of the           representativeness of the simulation means is
                                                                                                                                 competent authority of the MS or an
                                   procedures and checklists is           proven valid for the intended purpose with positive
                                                                                                                                 entity that is designated by the
                                   declared.                              results; or
                                                                                                                                 competent authority.
                                                                          (3)       any other means acceptable to the
                                                                          competent authority of the MS.
                                                                          1
                                                                            AMC2 UAS.SPEC.030(3)(e) (Operational procedures
                    Comments       N/A                                    for medium and high levels of robustness) is           N/A
                                                                          considered an acceptable means of compliance.
                                                                                                                                 The competent authority of the MS or
                                                                                                                                 an entity that is designated by the
                                                                          —        Training syllabus is available.               competent authority:
                    Criterion #3   Training is self-declared (with
                                                                          —        The UAS operator provides competency-         —        validates the training syllabus;
                    (Training)     evidence available).
                                                                          based, theoretical and practical training.             and
                                                                                                                                 —        verifies the remote crew
                                                                                                                                 competencies.
                    Comments       N/A                                    N/A                                                    N/A




Annex to ED Decision 2025/018/R                                                                                                                            Page 142 of 204
                                                                    AMC & GM to Regulation (EU) 2019/947
                                                                           Issue 1, Amendment 3


OSO #24 — The UAS is designed and qualified for to operate in adverse environmental conditions (e.g. UA controllability and performance, adequate
      sensors, DO-160 qualification)
       (a)    To assess the integrity of this OSO, the applicant UAS designer determines:
              (1)    whether credit can be taken for the equipment environmental qualification tests / declarations, e.g. by answering the following questions:
                     (i)       Is there a Declaration of Design and Performance (DDP) available to the applicant UAS designer stating the environmental
                               qualification levels to which the equipment was tested?
                     (ii)      Did the environmental qualification tests follow a standard considered adequate by the competent authority (e.g. DO-160)?
                     (iii)     Are the environmental qualification tests appropriate and sufficient to cover the envisaged environmental envelope?
                     (iv)      If the tests were not performed following a recognised standard, were the tests performed by an organisation/entity that is qualified
                               or that has experience in performing DO-160-like tests?
              (2)    Can the suitability of the equipment for the intended/expected UAS environmental conditions be determined from either in-service
                     experience or relevant test results?
              (3)    Any environmental limitations which, if exceeded, would compromise affect the suitability of the equipment or the operability or
                     controllability of the UA (e.g. maximum cross wind) for the intended/expected UAS environmental conditions.
       (b)    The lowest integrity level should be considered for those cases where a piece of an equipment installed in the UAS has only a partial
              environmental qualification and/or a partial demonstration by similarity and/or parts with no qualification at all.
                                                                                              LEVEL of INTEGRITY
     ADVERSE ENVIRONMENTAL
                                                                                           Medium                                           High
      OPERATING CONDITIONS                             N/A
                                                                                           (SAIL III)                                  (SAIL IV to VI)
                                                                                                                        The UAS is designed according to using
                                                                           The UAS is designed to limit the effect of   environmental standards considered adequate by
                             Criteria
                                          N/A                              the environmental conditions defined         the competent authority and/or in accordance
 OSO #24                     Criterion
                                                                           and reflected in the UAS flight manual.      with a means of compliance acceptable to EASA
 The UAS is designed
                                                                                                                        that authority.
 and qualified for to
                                                                           N/A
 operate in adverse
                                                                           As an example, if a UAS is proposed to be
 environmental
                                                                           operated in raining conditions, it is not
 conditions                  Comments     N/A                                                                           N/A
                                                                           necessary to comply with DO-160G
                                                                           waterproof conditions; the rain threshold
                                                                           may be limited as long as it is


Annex to ED Decision 2025/018/R                                                                                                                          Page 143 of 204
                                                    AMC & GM to Regulation (EU) 2019/947
                                                           Issue 1, Amendment 3


                                                           representative   of    the      envisaged
                                                           environmental conditions.



                                                                              LEVEL of ASSURANCE
      ADVERSE ENVIRONMENTAL
                                                                                    Medium                                            High
       OPERATING CONDITIONS                   N/A
                                                                                    (SAIL III)                                   (SAIL IV to VI)
                                                                                                                     If the operation is classified as SAIL IV,
                                                                                                                     the competent authority should
                                                                                                                     request the applicant UAS operator
                                                                                                                     should to use a UAS for which EASA
                                                                The applicant UAS designer has supporting
                                                                                                                     has issued a design verification report
                                                                evidence that the required level of integrity has
                                                                                                                     (DVR) following an application from
                                                                been achieved. This is typically done by testing,
                                                                                                                     the UAS designer.
                                                                analysis, simulation12, inspection, design review
                                                                                                                     If the operation is classified as SAIL V
                          Criteria                              or through operational experience.
                                        N/A                                                                          or VI, the competent authority should
                          Criterion
                                                                                                                     request the applicant UAS operator
                                                                The UAS operator should use a UAS for which
                                                                                                                     should to use a UAS for which EASA
                                                                the UAS designer has issued a statement of
 OSO #24                                                                                                             has issued a type certificate or a
                                                                compliance with the MoC to OSO #242 using the
 The UAS is designed                                                                                                 restricted    type      certificate     in
                                                                form attached to the MoC.
 and qualified for to                                                                                                accordance with Annex I (Part 21) to
 operate in adverse                                                                                                  Regulation (EU) No 748/2012
 environmental                                                                                                       following an application from the UAS
 conditions                                                                                                          designer.
                                                                12
                                                                  When simulation is performed, the validity of
                                                                the targeted environment that is used in the
                                                                simulation needs to be justified.
                          Comments      N/A                     2                                                    N/A
                                                                  https://www.easa.europa.eu/en/document-
                                                                library/product-certification-
                                                                consultations/means-compliance-moc-design-
                                                                uas-operated-sail
                          Alternative                           FUNCTIONAL-TEST-BASED (FTB) METHODS:
                                        N/A                                                                          N/A
                          criterion
                                                                If the UAS designer has evidence of the FTB flight



Annex to ED Decision 2025/018/R                                                                                                               Page 144 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3


                                                                           LEVEL of ASSURANCE
      ADVERSE ENVIRONMENTAL
                                                                                 Medium                                        High
       OPERATING CONDITIONS                N/A
                                                                                 (SAIL III)                               (SAIL IV to VI)
                                                             hours proportionate to the SAIL of the operation
                                                             meeting either set of conditions described
                                                             either in Section E.3(c) or in Section E.3(d) and
                                                             executed

                                                             (a) within the full operational scope/envelope
                                                                 intended by the UAS operator; and
                                                             (b) following the maintenance instructions, the
                                                                 operational procedures and the remote
                                                                 crew training referred to in the operational
                                                                 authorisation,
                                                             then the assurance that the operational
                                                             procedures are adequate is fulfilled at the level
                                                             corresponding to the SAIL being demonstrated
                                                             by the FTB approach1.
                                                             1
                                                               As an example, if the number of test cycles
                                                             supporting the FTB flight hours is proportionate
                          Comments   N/A                     to the risk of a SAIL III operation (i.e. 3 000 FH),   N/A
                                                             the assurance level for OSO #24 is fulfilled at
                                                             ‘medium’ level.




Annex to ED Decision 2025/018/R                                                                                                      Page 145 of 204
                                              AMC & GM to Regulation (EU) 2019/947
                                                     Issue 1, Amendment 3



E.3 Functional-test-based (FTB) approach
(a)      The objective of this section is to give some insight into the FTB approach referenced
         throughout Annex E to this AMC. This is articulated around three different but complementary
         perspectives:
         (1)    FTB as a means of compliance (MoC) to support UAS designers in demonstrating UAS
                operational reliability for the purpose of obtaining an FTB design appraisal;
         (2)    FTB design appraisal performed by UAS designers supporting UAS operators when
                showing compliance with some of the OSOs of Annex E to this AMC;
         (3)    FTB as a means for UAS operators to take credit for safe and successful operations over
                time to expand their operational authorisation (based on the concept of ‘reliability
                growth model’).
         These three approaches are detailed in the following points (b), (c) and (d).
(b)      For FTB as a MoC to support UAS designers in demonstrating UAS operational reliability, please
         refer to the EASA MoC SC Light-UAS FTB50.
(c)      FTB design appraisal performed by UAS designers supporting UAS operators when showing
         compliance with some of the OSOs of Annex E to this AMC:
         (1)    An FTB design appraisal obtained by a UAS designer presents several benefits both for
                the UAS operator going through the operational authorisation process and the
                competent authority issuing such operational authorisation, in particular when the UAS
                operator does not have a strong cooperation with the UAS designer or does not have all
                the design details.
         (2)    In order for a UAS operator to take credit for an FTB design appraisal obtained by a UAS
                designer, the following conditions as a minimum should be met:
                (i)     The functional tests supporting the FTB design appraisal obtained by the UAS
                        designer have been performed within the full operational scope/envelope
                        intended by the UAS operator; this means that the test cycles are fully
                        representative of the UAS operator’s operations with test points to verify safe
                        operation at the operational limits and corners of the UA envelope.
                (ii)    The functional tests supporting the FTB design appraisal obtained by the UAS
                        designer have been performed following the operational procedures and the
                        remote crew training referred to in the operational authorisation (and meeting the
                        integrity assurance of the associated OSOs).
                (iii)   The UAS operator’s maintenance instructions are established based on the UAS
                        designer’s instructions and requirements which were used for maintenance, repair
                        or replacement of the UAS subsystems during the functional tests supporting the
                        FTB design appraisal obtained by the UAS designer.
                (iv)    Any UAS configuration differences compared to the initial configuration used by

50    https://www.easa.europa.eu/en/document-library/product-certification-consultations/final-means-compliance-
      special-condition-light



Annex to ED Decision 2025/018/R                                                                        Page 146 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3



                        the UAS designer to obtain the FTB design appraisal are confirmed by the UAS
                        designer in order not to impair the validity of the FTB design appraisal.
                (v)     The minimum number of test cycles are proportionate to the risk of the UAS
                        operation, with at least:
                        —       30 hours for SAIL I;
                        —       300 hours for SAIL II; and
                        —       3 000 hours for SAIL III
                        in order to achieve a 95 % confidence (assuming a binomial/Poisson distribution
                        for the operational level hazard rate and no failures during the test)51.
                        Note that FTB methods are not considered feasible for UAS operations with a SAIL
                        above or equal to IV.
                (vi)    The functional tests supporting the FTB design appraisal obtained by the UAS
                        designer have been performed by the UAS designer according to the
                        principles/standards considered adequate by the competent authority in charge of
                        granting the operational authorisation, including as a minimum the following
                        principles:
                        —       The functional tests supporting the FTB design appraisal obtained by the UAS
                                designer have been performed using an acceptable sample size of the UA.
                        —       Safe life limits for UAS subsystems sensitive to wear-out conditions based on
                                the maximum cycles and hours demonstrated by one or more fleet leader
                                UAS (i.e. the UAS with the longest time and/or cycles compared to other UAS
                                used during the FTB testing) have been derived by the UAS designer and
                                captured in the FTB design appraisal limitations.
        (3)     Additionally, induced-failure tests may help demonstrate compliance with the following
                OSOs and Step #8:
                (i)     OSO #05 and Step #8: safety and reliability/safe design (e.g. induced-failure tests
                        with no loss of control or containment as pass–fail criteria);
                (ii)    OSO #06: C3 link performance appropriate for the UAS operation (e.g. if the
                        distance from a C2 radio transmitter/receiver is a critical factor, then the
                        demonstration of the maximum allowable range from the transmitter/receiver in
                        the most likely worst-case conditions is required);
                (iii)   OSO #18: Automatic protection of the flight envelope from human error.
                However, induced-failure testing is not addressed in this version of Annex E to this AMC
                since competent authorities are still in the process of defining the modalities of test-
                based approaches. In the meantime, credit for induced-failure testing may be proposed
                on a case-by-case basis by a UAS operator depending on the scope of the FTB design
                appraisal obtained by the UAS designer.


52   See the Rule of Three at https://en.wikipedia.org/wiki/Rule_of_three_(statistics).



Annex to ED Decision 2025/018/R                                                                Page 147 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



(d)    FTB as a means for UAS operators to take credit for safe and successful operations over time to
       expand their operational authorisation (based on the concept of ‘reliability growth model’):
       (1)    An FTB approach should also allow UAS operators to take credit for safe and successful
              operations over time to expand their operational authorisation based on the concept of
              ‘reliability growth’, while still meeting the conditions of point E.3(c).
       (2)    UAS operators should be able to operate with a low SAIL approval and then, through
              operational experience, gather sufficient operational data to justify an increase in the
              SAIL, based upon the increase in operational reliability demonstrated by UAS operators.
              This approach would only be valid under representative operating conditions, not
              requiring additional strategic or tactical mitigations.
              Note 1: The competent authority may accept accumulation of FTB hours between
                      operators if the UAS configuration, operational procedures, training, etc., are
                      demonstrated to be equivalent.
              Note 2: This option does not cover expanded operating conditions which would require
                      additional testing and/or analysis to be performed by the UAS designer. As an
                      example, a UAS operator may start with a SAIL II operational authorisation to
                      fly over population density up to 500 people/km2 and, if they demonstrate
                      3 000 hours with no loss of control, they could be allowed to fly a SAIL III
                      operation under the exact same operating conditions, except for an increase of
                      the maximum population density allowed (5 000 people/km2).
       (3)    To be relevant, the UAS operator would need to show that:
              (i)     the next population band does not introduce new or unique hazards, or if it does,
                      these new or unique hazards are shown to be properly mitigated through test or
                      analysis;
              (ii)    the reliability demonstrated through operational testing demonstrates the
                      required operational reliability at the higher SAIL level desired;
              (iii)   any UAS configuration differences compared to the initial configuration do not
                      impair the validity of the argument.




Annex to ED Decision 2025/018/R                                                          Page 148 of 204
                                                                             AMC & GM to Regulation (EU) 2019/947
                                                                                    Issue 1, Amendment 3




E.4 Containment requirements
(a)      Section S.4.8 of this AMC (SORA Main Body, Step #8) ‘Determination of the containment requirements’ addresses the risk posed by an operational loss
         of control that could infringe on areas adjacent to the operational volume and buffers. The ground risk (in the adjacent ground area) determines the
         level of safety requirements to be met by containment design features and operational procedures.
(b)      The following section provides the generic containment requirements for the following three levels of containment: low, medium and high.

                                                                                               LEVEL of INTEGRITY
 Containment of
 untethered UA                                 Low                                                  Medium                                               High2

                                                                                                                                      The UAS should be designed such that:

                                                                                                                                      • (qualitative) no remote single failure3 of
                         The UAS should be designed such that:                                                                          the UAS or of any external system
                                                                                                                                        supporting the operation could lead to
                             •   (qualitative) no probable1 single failure of the UAS or of any external system supporting the
      Criterion #1                                                                                                                      operation outside the operational
                                 operation could lead to operation outside the operation volume;
                                                                                                                                        volume;
(Operational volume
                         OR
   containment)                                                                                                                       OR
                             •   (quantitative) the probability of the failure condition ‘UA leaving the operational volume’ should
                                                                                                                                      • (quantitative) the probability of the
                                 be less than 10–3/FH.
                                                                                                                                        failure condition ‘UA leaving the
                                                                                                                                        operational volume’ should be less than
                                                                                                                                        10–4/FH3.


                                                                                                                                      2
                                                                                                                                        This may be achieved by a tether that
                                                                                                                                      prevents the UA from exiting the operational
                         1
      Comments               Failures anticipated to occur one or more times during the entire operational life of an item.           volume (see containment of tethered UA
                                                                                                                                      below).
                                                                                                                                      3
                                                                                                                                          ‘failure’ needs to be understood as an



Annex to ED Decision 2025/018/R                                                                                                                               Page 149 of 204
                                                                              AMC & GM to Regulation (EU) 2019/947
                                                                                     Issue 1, Amendment 3



                                                                                                                                        occurrence that affects the operation of a
                                                                                                                                        component, part or element such that it can
                                                                                                                                        no longer function as intended. Errors may
                                                                                                                                        cause failures but are not considered failures.
                                                                                                                                        Some structural or mechanical failures may
                                                                                                                                        be excluded from the criterion if it can be
                                                                                                                                        shown that such structural or mechanical
                                                                                                                                        parts were designed according to aviation
                                                                                                                                        industry best practices.
                                                                                                                                        3
                                                                                                                                          Failures unlikely to occur with each UA
                                                                                                                                        during its operational life but that may occur
                                                                                                                                        several times when considering the total
                                                                                                                                        operational life of a number of UA of a
                                                                                                                                        particular type.
                                                                                                                                        4
                                                                                                                                          This means a reduction by a factor of 10 of
                                                                                                                                        the likelihood of exiting the operational
                                                                                                                                        volume compared to the ‘low’ and ‘medium’
                                                                                                                                        integrity containment.


       Criterion #2
                              When the UA leaves the operational volume, the immediate termination of the flight should be initiated through a combination of procedures/processes
(End of flight upon exit of   and/or available technical means.
 the operational volume)


                              Such criteria may be satisfied by the operational procedures developed by the UAS operator that may rely (fully or partially, depending on the level of
       Comments
                              automation of the UAS) on technical means developed by the UAS designer and documented in the UAS flight manual.




   Annex to ED Decision 2025/018/R                                                                                                                               Page 150 of 204
                                                                           AMC & GM to Regulation (EU) 2019/947
                                                                                  Issue 1, Amendment 3




                           The UAS operator defines the size of the
                           ground risk buffer. In principle, the ground
                           risk buffer should at least adhere to the 1:1
                           principle5. Alternatively, as the 1:1 rule may
                           not be suitable for some UA configurations
                           (e.g. fixed-wing or parachute-equipped UA),
                           the competent authority may require In addition to ‘low’ robustness, the ground risk buffer should consider the following points:
                           defining the ground risk buffer based on a
                                                                          (a) Probable7 single failures (including the projection of high-energy parts such as rotors and propellers)
     Criterion #3          ballistic methodology approach, a glide
                                                                              which would lead to an operation outside the operational volume;
                           trajectory6, representative flight tests
(Definition of the final                                                  (b) Meteorological conditions (e.g. maximum sustained wind);
                           and/or a combination of these.
  ground risk buffer)
                           A smaller ground risk buffer value may be      (c) UAS latencies (e.g. latencies that affect the timely manoeuvrability of the UA);
                           proven by the UAS operator for a rotary-
                                                                          (d) UA behaviour when activating a technical containment measure considering UA performance.
                           wing UA using a ballistic methodology
                           approach acceptable to the competent
                           authority.

                           If the UAS uses a parachute, the UAS
                           operator should consider the effect of wind
                           on the UAS when it is deployed.


                           5
                              The 1:1 principle refers to applying a
                           ground risk buffer that is as wide as the
                           maximum height of the operational volume.
                                                                        7
                           For the evaluation of the size of the ground   For the purpose of this assessment, the term ‘probable’ should be interpreted in a qualitative way as
      Comments
                           risk buffer based on the 1:1 principle, see ‘anticipated to occur one or more times during the entire operational life of a UAS’.
                           Annex A Section A.5.2.4.
                           6
                               See Annex A Section A.5.2.4.




 Annex to ED Decision 2025/018/R                                                                                                                                 Page 151 of 204
                                                                         AMC & GM to Regulation (EU) 2019/947
                                                                                Issue 1, Amendment 3




                                                                     The UAS should be designed such that no single failure8 of the UAS or of any external system supporting
   Criterion #4                                                      the operation could lead to operation outside the ground risk buffer.

(Ground risk buffer      N/A                                         Software (SW) and airborne electronic hardware (AEH) whose development error(s) could directly lead
   containment)                                                      to operations outside the ground risk buffer should be developed to an industry standard or
                                                                     methodology recognised as adequate by the competent authority.


                                                                     8
                                                                         Example methods for achieving this may include:

                                                                     — an independent flight termination system (FTS) that will initiate the end of the flight when the UA exits
                                                                       the operational volume; or
    Comments             N/A
                                                                     — a secondary independent emergency flight control system that ends the flight in a controlled manner
                                                                       without exceeding the ground risk buffer; or

                                                                     — a tether that prevents the UA from exiting the ground risk buffer.




Containment of                                                                          LEVEL of ASSURANCE
untethered UA                                Low                                                 Medium                                                    High

                                                                                                                                          Same as ‘medium’.
                         The applicant declares1 that the required   The applicant has supporting evidence that the required level
                                                                                                                                          The UAS operator should use a UAS for
                         level of integrity has been achieved.       of integrity has been achieved. This is typically done by testing,
                                                                                                                                          which EASA has verified the claimed
                                                                     analysis, simulation2, inspection and design review.
                         The UAS designer:                                                                                                integrity through a design verification
  For all criteria
                                                                     Among the supporting evidence:                                       report ‘DVR’.
                         (a) for criterion #1, conducts a design and
                             installation appraisal2 including as a (a) for criterion #1 and criterion #4: same as criterion #1,          In addition, the competent authority of
                             minimum:                                   ‘low’;                                                            the Member State or the entity that is
                                                                                                                                          designated by the competent authority



Annex to ED Decision 2025/018/R                                                                                                                               Page 152 of 204
                                                                              AMC & GM to Regulation (EU) 2019/947
                                                                                     Issue 1, Amendment 3



                             — design and installation features (e.g.     (b) for criterion #2: the adequacy of the emergency               validates the claimed level of integrity
                               independence,       separation     or          procedures to terminate the flight is proven through:         for the non-design-related criteria.
                               redundancy claims);
                                                                                — dedicated flight tests; or
                             — any relevant particular risk (e.g. hail,
                                                                                — simulation provided the simulation is proven valid for
                               ice,     snow,         electromagnetic
                                                                                  the intended purpose with positive results.
                               interference, etc.) associated with the
                               UAS operation and how they are
                               being addressed;

                         (b) for criterion #2, tests the technical
                            means to safely end the flight and
                            includes the procedures in the UAS flight
                            manual.

                         The UAS operator:

                         — for criterion #2, tests the adequacy of
                           the emergency procedures to terminate
                           the flight.


                                                                          2
                                                                           When simulation is used, the suitability of the targeted
                         1
                           Supporting evidence for this declaration       environment used in the simulation needs to be justified.
                         may still be requested by the competent
                                                                          The UAS operator may use a UAS for which the UAS designer
                         authority.
                                                                          has issued a statement of compliance with the MoC to Light-
                         2
                          A simple, written justification from the UAS    UAS.2511         (https://www.easa.europa.eu/en/document-
    Comments             designer, including functional diagrams and                                                                        N/A
                                                                          library/product-certification-consultations/final-means-
                         a description of how the system works,           compliance-light-uas2511-moc-light) using the form attached
                         explaining why the integrity claim (i.e. no      to the MoC when the UAS meets the conditions defined in such
                         (probable/remote) single failure criterion) is   MoC. For UAS configurations exceeding the applicability of such
                         met is an acceptable means of compliance.        MoC, the competent authority may decide to still accept
                                                                          statements based on such MoC with evidence available, or to



Annex to ED Decision 2025/018/R                                                                                                                                Page 153 of 204
                                                                              AMC & GM to Regulation (EU) 2019/947
                                                                                     Issue 1, Amendment 3



                                                                            accept appropriate MoC proposed by the UAS designer.
                                                                            Otherwise, the competent authority may request the UAS
                                                                            operator to use a UAS for which EASA has verified the claimed
                                                                            integrity.


  The following section is an alternative which should only be used in the specific use of a tether:

                                                                                                    LEVEL of INTEGRITY
Containment of tethered UA
                                                                                                  Low, Medium and High1
                                    (a) The length of the line is adequate to contain the UA in the operational volume.

         Criterion #1               (b) The strength of the line is compatible with the ultimate loads 2 expected during the operation.

      (Technical design)            (c) The strength of attachment points is compatible with the ultimate loads 2 expected during the operation.

                                    (d) The tether cannot be cut by rotating propellers.

                                    UAS operators may purchase a UAS designed to be used with a tether or they may apply a tether. In this case, the UAS operator is required to
          Comments
                                    comply with criterion #1.

         Criterion #2
                                    The UAS operator has procedures to install and periodically inspect the condition of the tether.
        (Procedures)

                                    1
                                        The distinction between a ‘medium’ and a ‘high’ level of robustness for this criterion is achieved through the level of assurance provided below.
          Comments                  2
                                     Ultimate loads are identified as the maximum loads to be expected in service, including all possible nominal and failure scenarios multiplied by
                                    a 1.5 factor of safety.




  Annex to ED Decision 2025/018/R                                                                                                                                 Page 154 of 204
                                                                           AMC & GM to Regulation (EU) 2019/947
                                                                                  Issue 1, Amendment 3




                                                                                                   LEVEL of ASSURANCE
Containment of tethered UA
                                                   Low                                          Medium                                                 High

                                    The UAS designer or the UAS            The UAS designer or the UAS operator has            The claimed level of integrity is validated by the
                                    operator declares1 that the            supporting evidence (including the tether           competent authority of the Member State or by an
                                    required level of integrity has been   material specifications) to claim the required      entity that is designated by the competent authority.
                                    achieved.                              level of integrity has been achieved.
         Criterion #1                                                      (a) This is typically achieved through testing or
     (Technical design)                                                        operational experience.

                                                                           (b) Tests can be based on simulations;
                                                                               however, the validity of the target
                                                                               environment used in the simulation needs
                                                                               to be justified.

                                    1
                                     Supporting evidence for this
         Comments                   declaration may still be requested     N/A                                                 N/A
                                    by the competent authority.

                                                                                                                               Same as ‘medium’. In addition:
                                                                           (a) Procedures are validated against standards
                                                                               considered adequate by the competent            (a) flight tests performed to validate the procedures
                                                                               authority and/or in accordance with means           cover the complete flight envelope or are proven
         Criterion #2               The UAS operator declares to               of compliance acceptable to that authority.         to be conservative;
        (Procedures)                have adequate procedures.
                                                                           (b) The adequacy of the procedures is proved        (b) the procedures, flight tests and simulations are
                                                                               through:                                            validated by the competent authority of the
                                                                                                                                   Member State or by an entity that is designated by
                                                                                 — dedicated flight tests; or
                                                                                                                                   the competent authority.




  Annex to ED Decision 2025/018/R                                                                                                                             Page 155 of 204
                                                                      AMC & GM to Regulation (EU) 2019/947
                                                                             Issue 1, Amendment 3



                                                                           — simulation provided the simulation is
                                                                             proven valid for the intended purpose
                                                                             with positive results.



                                                                      1
                                  1
                                                                         National aviation authorities (NAAs) may
                                    Procedures do not require
                                                                      define the standards and/or the means of
                                  validation against either a
                                                                      compliance they consider adequate. The SORA
       Comments                   standard or a means of compliance                                                      N/A
                                                                      Annex B will be updated at a later point in time
                                  considered adequate by the
                                                                      with a list of adequate standards based on the
                                  competent authority.
                                                                      feedback provided by the NAAs.




Annex to ED Decision 2025/018/R                                                                                                Page 156 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3




Annex I to AMC1 Article 11
GLOSSARY OF TERMS

 Term                             Acronym     Definition
I.1. Abnormal situation                       A situation in which it is no longer possible to continue the flight
                                              using normal procedures.

I.2. Acceptable risk                          The level of risk that individuals or groups are willing to accept
                                              given the benefits gained. Each organisation will have its own
                                              acceptable risk level, which is derived from its legal and regulatory
                                              compliance responsibilities, its threat profile, and its
                                              business/organisational drivers and impacts.
I.3. Adequate                                 Whatever is necessary or sufficient for a specific requirement.

I.4. Adjacent airspace                        The airspace adjacent to the operational volume.
                                              See Section S.2.2.6 of AMC1 Article 11.

I.5. Adjacent ground area                     The ground area adjacent to the ground risk buffer.
                                              See also Section S.2.2.5 of this AMC (SORA Main Body).

I.6. Aerodrome                                A defined area (including any buildings, installations and
                                              equipment), on land or on water, on a fixed, fixed offshore or
                                              floating structure, including any buildings, installations and
                                              equipment thereon, intended to be used either wholly or in part
                                              for the arrival, departure and surface movement of aircraft.
I.7. Aerodrome                                The aerodrome environment is normally protected by the
     environment                              Member State through the creation of a geographical zone
                                              defined according to Article 15 of Implementing Regulation (EU)
                                              2019/947. The aerodrome environment in the SORA context is
                                              generally defined as:
                                              (a) class A, B, C, D or E controlled airspace which touches the
                                                  surface with an aerodrome and/or controlled airspace which
                                                  does not touch the surface, but in connection to an
                                                  aerodrome (normally depicted on aeronautical charts and
                                                  sectionals); or
                                              (b) any TMZ in class A, B, C, D or E controlled airspace.
I.8. Aeronautical                 AIP         A publication issued by or with the authority of a State and
     information publication                  containing aeronautical information of a lasting character
                                              essential to air navigation.
I.9. Air risk class               ARC         The ARC is an initial assignment of generic collision risk of airspace
                                              before mitigations are applied. The ARC is assigned to airspace
                                              encounter categories (AECs) based on a qualitative assessment of
                                              collision risk of generic types of airspace.
I.10. Aircraft                    a/c         Any machine that can derive support in the atmosphere from the
                                              reactions of the air other than the reaction of the air against the
                                              earth’s surface.

I.11. Airframe                                The fuselage, booms, nacelles, cowlings, fairings, air foil surfaces
                                              (including rotors but excluding propellers and rotating air foils of
                                              engines) and landing gear of an UA, and their accessories and
                                              controls.




Annex to ED Decision 2025/018/R                                                                      Page 157 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.12. Airspace encounter          AEC         The AEC is a qualitative classification of the probability that a UAS
     category                                 would encounter a manned aircraft in typical civil airspace found
                                              in the U.S. and Europe. The airspace encounter risk is grouped by
                                              operational altitude, airport environment, controlled airspace,
                                              uncontrolled TMZ airspace, and in uncontrolled airspace over
                                              rural and/or urban populations. The AEC is based on the
                                              assessment of the proximity (the more aircraft in the airspace, the
                                              higher the rate of proximity, the greater the risk of collision),
                                              geometry (an airspace structure which reduces the probability
                                              that an aircraft finds itself on collision courses), and dynamics (in
                                              general, the faster the speed of the aircraft in the airspace, the
                                              greater the number of collision risks over a set time). Airspace
                                              where there is a higher density of manned aircraft, few airspace
                                              structural controls, and high aircraft closing speeds will
                                              experience higher airspace encounter rates than in airspace
                                              where there is low density, high airspace structure and slow
                                              speeds.
I.13. Airspace observer           AO          Means a person who assists the remote pilot by performing
                                              unaided visual scanning of the airspace in which the unmanned
                                              aircraft is operating for any potential hazard in the air.
                                              (Article 2(25) of Implementing Regulation (EU) 2019/947)

I.14. Airworthiness                           The condition of an item (aircraft, aircraft system, or part) in
                                              which that item operates in a safe manner to accomplish its
                                              intended function.
I.15. Applicant                               An individual or an organisation that desires to operate a UAS in
                                              a limited or restricted manner and submits the necessary
                                              technical, operational and human information related to the
                                              intended use of the UAS to the competent authority.
                                              See also Section S.2.5(b) of this AMC (SORA Main Body).

I.16. Assemblies of people                    Means gatherings where persons are unable to move away due
                                              to the density of the people present.
                                              (Article 2(3) of Implementing Regulation (EU) 2019/947)

I.17. Assurance                               The level of verification required by the competent authority prior
                                              to granting an approval. All the integrity requirements must still
                                              be fulfilled by the UAS operator, but the verification of the
                                              implementation can happen before the approval is granted or
                                              after in auditing.




Annex to ED Decision 2025/018/R                                                                     Page 158 of 204
                                               AMC & GM to Regulation (EU) 2019/947
                                                      Issue 1, Amendment 3



 Term                               Acronym      Definition
I.18. Atypical air                               Airspace where the risk of collision between a UAS and manned
     environment                                 aircraft is acceptably low. Examples are:
                                                 (a) restricted airspace or segregated areas;
                                                 (b) airspace where normally manned aircraft should not be
                                                     present (e.g. at a height low enough or close to an obstacle,
                                                     excluding those potential landing sites for manned aircraft,
                                                     see examples below)52;

                                                                  Minimum 20m

                                                                                             Maximum
                                                                                            operational
                                                                  Maximum flight            volume 50m
                                                                  geography 30m




                                                 (c) airspace not covered in airspace encounter categories (AECs)
                                                     1 through 11.
I.19. Authority                                  The organisation responsible within the State concerned with the
                                                 certification of compliance with applicable requirements.


52   Only in areas where applicable and accepted by the competent authority.



Annex to ED Decision 2025/018/R                                                                     Page 159 of 204
                                             AMC & GM to Regulation (EU) 2019/947
                                                    Issue 1, Amendment 3



 Term                             Acronym      Definition
I.20. Authorisation                            The permit granted to a UAS operator by a competent authority.

I.21. Automatic system                         Any system in which the remote crew is supported by mechanised
                                               or computerised components executing predefined processes.

I.22. Autonomous UA                            Means an operation during which an unmanned aircraft operates
                                               without the remote pilot being able to intervene.
                                               (Article 2(17) of Implementing Regulation (EU) 2019/947)

I.23. Barrier                                  A material object or set of objects that separates, demarcates or
                                               serves as a barricade; or something immaterial that impedes or
                                               separates. Both physical and non-physical barriers are utilised and
                                               applied in hazard control, i.e. anything used to control, prevent or
                                               impede unwanted adverse energy flow and/or anything used to
                                               control, prevent or impede unwanted event flow.
I.24.   Beyond visual line of     BVLOS        Means a type of UAS operation which is not conducted in VLOS.
        sight operation                        (Article 2(8) of Implementing Regulation (EU) 2019/947)

I.25.   Beyond visual line of     BVLOS        A UAS operation whereby the remote pilot maintains
        sight operation with      with AOs     uninterrupted situational awareness of the airspace in which the
        airspace observers                     UAS operation is being conducted via visual airspace surveillance
                                               through one or more airspace observers, possibly aided by
                                               technological means. The remote pilot-in-command (RPIC) has
                                               direct control of the UAS at all times.
I.26.   Catastrophic                           Failure condition that could result in one or more fatalities.

I.27.   Certification                          The legal recognition based on an appropriate assessment that a
                                               product, part, service, organisation or person complies with the
                                               applicable requirements through the issuance of a certificate,
                                               licence, approval or other documents as required by national laws
                                               and procedures, attesting such compliance.

I.28.   Civil aircraft                         Aircraft other than public/State or military aircraft.

I.29.   Collision avoidance                    Averting physical contact between an aircraft and any other
                                               object or terrain.

I.30.   Command and               C2 link      Means the data link between the UA and the CMU for the purpose
        control link                           of managing the flight.
                                               (Article 2(27) of Implementing Regulation (EU) 2019/947)

I.31.   Commercial off-the-       COTS         Components designed to be implemented into existing systems
        shelf                                  without extensive customisation and for which design data is not
                                               always available to the customer.

I.32.   Competent authority                    The authority responsible to assess the safety measures proposed
                                               by the UAS operator for a safety operation, following a specific
                                               operations risk assessment (SORA) and issuing the operational
                                               authorisation.
                                               See also Section S.2.5(e) of this AMC (SORA Main Body).

I.33.   Compliance                             Successful performance of all mandatory activities; agreement
                                               between the expected or specified result and the actual result.




Annex to ED Decision 2025/018/R                                                                         Page 160 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.34.   Component                             Any self-contained part, combination of parts, subassemblies or
                                              units, which perform a distinct function necessary to the
                                              operation of the system.
I.35.   Configuration                         The requirements, design and implementation that define a
                                              particular version of a system or system component.

I.36.   Configuration                         The process of evaluating, approving or rejecting, and
        control/management                    coordinating changes to configuration items after the formal
                                              establishment of their configuration identification.

I.37.   Conformity                            Aircraft or parts checked against design documents for
                                              correctness.
I.38.   Contingency area                      Means the projection of the contingency volume on the surface
                                              of the earth.
                                              (Article 2(31) of Implementing Regulation (EU) 2019/947)

I.39.   Contingency                           Planned course of action designed by the organisation to respond
        procedures                            effectively to a future event or abnormal situation that may or
                                              may not happen. It includes procedures executed by the remote
                                              pilot, or by the UA in case of autonomous flights, to return to
                                              normal operations or allow the safe cessation of the flight.
I.40.   Contingency volume                    Means the volume of airspace outside the flight geography where
                                              contingency procedures described in point (6)(d) of Appendix 5 to
                                              the Annex are applied.
                                              (Article 2(30) of Implementing Regulation (EU) 2019/947)
                                              See also Section S.2.2.3 of this AMC (SORA Main Body).

I.41.   Control and               CMU         Means the equipment to control and monitor unmanned aircraft
        monitoring unit                       remotely as defined in point (32) of Article 3 of Regulation (EU)
                                              2018/1139.
                                              (Article 2(26) of Implementing Regulation (EU) 2019/947)

I.42.   Controlled airspace                   Airspace class A, B, C, D and E. Airspace of defined dimensions
                                              within which air traffic control service is provided in accordance
                                              with the airspace classification. Controlled airspace does not
                                              imply that separation services are provided at all times.
                                              Classes A, B, C, D and E are described in ICAO Annex 11, and in
                                              ICAO Annex 2 Section 6.

I.43.   Controlled ground                     Means the ground area where the UAS is operated and within
        area                                  which the UAS operator can ensure that only involved persons are
                                              present.
                                              (Article 2(21) of Implementing Regulation (EU) 2019/947)
                                              Note: the concept of controlled ground area is applicable also for
                                              UAS operations over water surfaces.

I.44.   Cooperative aircraft                  Aircraft that have an electronic means of identification (i.e. a
                                              transponder) aboard and operating.

I.45.   Critical (function)                   A function whose loss would prevent the continued safe flight and
                                              landing of the UA thereby causing a significant increase in the
                                              safety risk to third parties and/or the environment involved.



Annex to ED Decision 2025/018/R                                                                   Page 161 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.46.   Critical area                         The ground area where persons would be expected to be
                                              impacted by the UA in the event of a loss of control of the
                                              operation or an unplanned landing.
I.47.   Critical infrastructure               Means systems and assets vital to national defence, national
                                              security, economic security, public health or safety including both
                                              regional and national infrastructure.

I.48.   Critical systems                      Systems required for the operation to perform one or more
                                              critical functions.
I.49.   Criticality                           The degree of impact a malfunction has on the operation of a
                                              system.
I.50.   Danger area                           A danger area is airspace of defined dimensions within which
                                              activities dangerous to the flight of aircraft may exist at specified
                                              times.
I.51.   Data link                             A term referring to all interconnections to, from and within the
                                              UAS. It includes control, flight status, communication and payload
                                              links.
I.52.   Demonstration                         A method of proof of performance by observation.

I.53.   Detect and avoid          DAA         The capability to see, sense or detect conflicting traffic or other
                                              hazards and take the appropriate action to comply with the
                                              acceptable rules of flight.

I.54.   Emergency recovery                    A UAS safety feature (e.g. return-to-home) that provides for the
        capability                            cessation of the UA operation in a manner that minimises the risk
                                              to persons on the ground, other airspace users and critical
                                              infrastructure.
I.55.   Emergency                             Planned course of action designed by the UAS operator to
        procedures                            respond effectively to an emergency condition. They deal with
                                              controlling the aircraft to either return to a state where the
                                              operation is ‘in control’ or to minimise hazards until the flight has
                                              ended. It includes procedures that are executed by the remote
                                              pilot or by the UA itself.
                                              See also Section S.2.3.2(d) of this AMC (SORA Main Body).

I.56.   Emergency response        ERP         Plan of actions to be conducted in a certain order or manner, in
        plan                                  response to an emergency event.
                                              For additional information, please refer to Section S.2.3.2(e) of
                                              AMC1 Article 11.

I.57.   Environment                           (a) The aggregate of operational and ambient conditions to
                                                  include the external procedures, conditions and objects that
                                                  affect the development, operation and maintenance of a
                                                  system. Operational conditions include traffic density,
                                                  communication density, workload, etc. Ambient conditions
                                                  include weather, EMI, vibration, acoustics, etc.; and
                                              (b) Everything external to a system which can affect or be
                                                  affected by the system.
I.58.   Equipment                             A complete assembly operating either independently or within a
                                              system/subsystem that performs a specific function.



Annex to ED Decision 2025/018/R                                                                     Page 162 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.59.   Failure                               The loss of a function or the malfunction of a system or a part of
                                              it.
                                              It should be understood as an occurrence that affects the
                                              operation of a component, part or element such that it can no
                                              longer function as intended. Errors may cause failures but are not
                                              considered failures. Some structural or mechanical failures may
                                              be excluded from the criterion if it can be shown that these
                                              structural or mechanical parts were designed according to
                                              aviation industry best practices.

I.60.   Failure mode                          The way in which the failure of an item occurs.

I.61.   Fixed-wing UA                         It includes configurations such as aeroplanes, kites, gliders, etc.

I.62.   Flight geography                      Means the volume(s) of airspace defined spatially and temporally
                                              in which the UAS operator plans to conduct the operation under
                                              normal procedures described in point (6)(c) of Appendix 5 to the
                                              Annex.
                                              (Article 2(28) of Implementing Regulation (EU) 2019/947)
                                              See also Section S.2.2.2 of this AMC (SORA Main Body).

I.63.   Flight termination        FTS         Procedure or function which aims to immediately end the flight.
        system
I.64.   Fly-away                              A condition due to loss of control of the operation, where the UAS
                                              is leaving the operational volume and it is not possible to regain
                                              control of the UA with none of the normal, contingency or
                                              emergency procedures being effective.
I.65.   Functional test based     FTB         An approach to demonstrate compliance with some OSOs, as
                                              defined in Section 3 of Annex E to this AMC.

I.66.   Geo-awareness                         Means a function that, based on the data provided by Member
                                              States, detects a potential breach of airspace limitations and
                                              alerts the remote pilots so that they can take immediate and
                                              effective action to prevent that breach.
                                              (Article 2(15) of Implementing Regulation (EU) 2019/947)

I.67.   Geo-caging                            An automatic function that helps the remote pilot to maintain the
                                              UAS within the defined overall volume (a ‘cage’).
I.68.   Geo-fencing                           An automatic function for preventing the UA from entering a
                                              prescribed volume.
I.69.   Ground risk buffer                    An area over the surface of the earth, which surrounds the
                                              operational volume and that is specified in order to minimise the
                                              risk to third parties on the surface in the event of the unmanned
                                              aircraft leaving the operational volume.
                                              (Article 2(33) of Implementing Regulation (EU) 2019/947)
                                              See also Section S.2.2.4 of this AMC (SORA Main Body).

I.70.   Handover                              The act of passing command and control from one control and
                                              monitoring unit to another.
I.71.   Hazard                                A potentially unsafe condition resulting from failures, external
                                              events, errors, or a combination of these.




Annex to ED Decision 2025/018/R                                                                     Page 163 of 204
                                              AMC & GM to Regulation (EU) 2019/947
                                                     Issue 1, Amendment 3



 Term                             Acronym       Definition
I.72.   Height                                  The vertical distance of a level, a point or an object considered as
                                                a point, measured from a specified datum.

I.73.   Human error                             Human action with unintended consequences.

I.74.   Human factors             HF            Factors affecting human performance and referring to principles
                                                that apply to aeronautical design, certification, training,
                                                operations and maintenance, and that seek safe interfaces
                                                between the human and other system components by proper
                                                consideration to human performance.
I.75.   Human factors                           Principles which apply to aeronautical design, certification,
        principles                              training, operations and maintenance, and that seek safe
                                                interface between the human and other system components by
                                                proper consideration to human performance.
I.76.   Initial air risk class    Initial       Initial classification of the airspace where UAS operations are
                                  ARC           intended to be performed before risk mitigations are applied.
I.77.   Intrinsic ground risk     iGRC          Initial classification of the ground risk before ground mitigations
        class                                   are applied.

I.78.   Intrinsic ground risk     iGRC          The projection of the operational volume plus ground risk buffer
        class footprint           footprint     on the surface of the earth.

I.79.   Incident                                An occurrence other than an accident that affects or could affect
                                                the safety of operations.

I.80.   Industry standard                       A published document established by consensus and approved by
                                                a recognised body that sets out specifications and procedures to
                                                ensure that a material, product, method or service meets its
                                                purpose and consistently performs to its intended use.
                                                Standards are industry-developed standards that define
                                                minimum safety and performance requirements of an acceptable
                                                product or a means of compliance to specific requirements.
I.81.   Inspection                              An examination of an item against a specific standard.
I.82.   Integrated airspace       IA            Integrated airspace is considered 500 ft AGL up to VHL airspace
                                                (≈FL600) and any airspace where manned aircraft will operate
                                                below 500 ft AGL for take-off and landing. It is airspace where
                                                UAS are expected to conform and comply with the existing
                                                manned aircraft operating rules, procedures and equipment.

I.83.   Integrity                               Attribute of a system or an item indicating that it can be relied
                                                upon to work as expected.
I.84.   Involved person                         A person directly involved with the operation of the UAS or is fully
                                                aware that the UAS operation is being conducted near them.
                                                Involved persons are fully aware of the risks involved with the UAS
                                                operation and have accepted these risks. The UAS operator
                                                informs involved persons of the risks and provides training in the
                                                relevant emergency procedures and/or contingency plans.
I.85.   Loss of control of the                  A situation
        operation                               — whose outcome heavily relies on providence; or
                                                — which cannot be handled by a contingency procedure.




Annex to ED Decision 2025/018/R                                                                      Page 164 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.86.   Lost C2 link (loss of                 The loss of the command-and-control link contact with the UA
        data link)                            such that the remote pilot can no longer intervene in the UA’s
                                              flight control.
I.87.   Maintenance                           The inspection, overhaul,        repair,   preservation    and/or
                                              replacement of parts.
I.88.   Malfunction                           The occurrence of a condition whereby the UAS operation is
                                              outside specified limits.
I.89.   Maximum take-off          MTOM        Means the maximum unmanned aircraft mass, including payload
        mass                                  and fuel, as defined by the manufacturer or the builder, at which
                                              the unmanned aircraft can be operated.
                                              (Article 2(22) of Implementing Regulation (EU) 2019/947)

I.90.   Mid-air collision         MAC         An accident where two aircraft come into contact with each other
                                              while both are in flight.

I.91.   Minimum aviation          MASPS       A MASPS specifies the characteristics that should be useful to UAS
        system performance                    designers, installers, service providers and users of systems
        standard                              intended for operational use within a defined volume. Where the
                                              systems are global in nature, the system may have international
                                              applications that are taken into consideration. The MASPS
                                              describes the system (subsystems/functions) and provides
                                              information needed to understand the rationale for system
                                              characteristics, operational goals, requirements and typical
                                              applications. Definitions and assumptions essential to the proper
                                              understanding of the MASPS are provided as well as minimum
                                              system test procedures to verify system performance compliance
                                              (e.g. end-to-end performance verification).

I.92.   Mitigation                            A means to reduce the risk of a hazard.
I.93.   Minimum                   MOPS        A MOPS provides standards for specific equipment that are useful
        operational                           to UAS designers, installers and users of the equipment. The word
        performance                           ‘equipment’ used in a MOPS includes all components and units
        specification                         necessary for the system to properly perform its intended
                                              function(s). The MOPS provides the information needed to
                                              understand the rationale for the equipment characteristics and
                                              the requirements stated. The MOPS describes typical equipment
                                              applications and operational goals and establishes the basis for
                                              required performance under the standard. Definitions and
                                              assumptions essential to the proper understanding are provided
                                              as well as installed equipment tests and operational performance
                                              characteristics for equipment installations.
I.94.   Multiple                  MSO         UA operations where multiple UA are under a common
        simultaneous UAS                      (centralised) flight management and the individual UA either:
        operations                            — operate relative to each other under the common flight
                                                management (e.g. formation flights with a swarm of UAS
                                                performing displays for entertainment); or
                                              — operate independently of each other under the common flight
                                                management.




Annex to ED Decision 2025/018/R                                                                   Page 165 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.95.   National aviation         NAA         Also referred to as ‘civil aviation authority’, is a government
        authority                             statutory authority in each Member State that issues the
                                              operational authorisation and conduct the oversight if the UAS
                                              operator.
I.96.   Night                                 ‘Night’ means the hours between the end of evening civil twilight
                                              and the beginning of morning civil twilight as defined in
                                              Implementing Regulation (EU) No 923/2012.
                                              (Article 2(34) of Implementing Regulation (EU) 2019/947)
                                              Note: Civil twilight ends in the evening when the centre of the
                                              sun’s disc is 6 degrees below the horizon and begins in the
                                              morning when the centre of the sun’s disc is 6 degrees below the
                                              horizon.

I.97.   Normal procedure                      A set of instructions covering those features of operations which
                                              lend themselves to a definite or standardised procedure without
                                              loss of effectiveness.
I.98.   Operation out of                      An operation unintentionally being conducted outside the limits
        control                               approved in the authorisation.
I.99.   Operational life                      It is defined by the UAS designer as the maximum flight hours
                                              and/or cycles a UAS operator should use the UAS while
                                              continuously conforming with the maintenance design
                                              requirements.
I.100. Operations manual          OM          A manual containing procedures, instructions and guidance for
                                              use by operational personnel in the execution of their duties.
                                              Annex A to this AMC illustrates an example for its content.

I.101. Operational volume                     Is the combination of the flight geography and the contingency
                                              volume.
                                              (Article 2(32) of Implementing Regulation (EU) 2019/947)
                                              See also Section S.2.2.1 of this AMC (SORA Main Body).

I.102. Parachute                              A device used or intended to be used to retard the fall of a body
                                              or object through the air.

I.103. Population density                     The number of people living per unit of an area (e.g. per square
                                              mile or square kilometre).

I.104. Procedure                              Standard, detailed steps that prescribe how to perform specific
                                              tasks.

I.105. Process                                A set of interrelated resources and activities, which transform
                                              inputs into outputs.
I.106. Qualification                          A process through which a State / competent authority / applicant
                                              ensures that a specific implementation satisfies the applicable
                                              requirements with an adequate level of confidence.
I.107. Quantification                         The act of assigning a numerical value to or measuring the
                                              probability that a specific event will occur.

I.108. Reliability                            The probability that an item will perform a required function
                                              under specified conditions, without failure, for a specified period
                                              of time.



Annex to ED Decision 2025/018/R                                                                   Page 166 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.109. Remote crew                            A member of the crew that performs duties essential to the safety
       member                                 of flight and whose duties and responsibilities have been assigned
                                              to them by the UAS operator. It may include the remote pilot-in-
                                              command (RPIC), airspace observers (AOs) and UA observers,
                                              maintenance staff, launch and recovery system operators etc..

I.110. Remote pilot (in           RPIC        A person, nominated by the UAS operator, responsible for the
       command)                               safe conduct of the flight of a UA by operating its flight controls
                                              either manually or, when the UA flies automatically, by
                                              monitoring its course and remaining able to intervene and change
                                              the UA course at any time.
I.111. Risk                                   The combination of the frequency (probability) of an occurrence
                                              and its associated level of severity.

I.112. Risk analysis                          The development of qualitative and/or quantitative estimate of
                                              risk based on evaluation and mathematical techniques.

I.113. Risk assessment                        The process by which the results of a risk analysis are used to
                                              make decisions.

I.114. Risk estimation                        The combination of the consequences and likelihood of the
                                              hazard.

I.115. Risk ratio                             The ratio between a conditional probability with a mitigating
                                              system, divided by a conditional probability without a mitigating
                                              system. An example of conditional probability is the chance that,
                                              given an encounter, a potential mid-air collision occurs.
                                              A relative risk measure, which compares the probability of an
                                              event in a non-mitigated scenario to the probability of the same
                                              event in a mitigated scenario.

I.116. Robustness                             Means the property of mitigations resulting from combining the
                                              safety gain provided by the mitigations and the level of assurance
                                              and integrity that the safety gain has been achieved.
                                              (Article 2(5) of Implementing Regulation (EU) 2019/947)

I.117. Rotorcraft-helicopter                  It includes all vertical-lift UA configurations having up to 2 rotors.
       UA
I.118. Rural air volume                       In the context of air risk, it is the volume not defined as urban
                                              environment and is not within the aerodrome traffic zone (ATZ)
                                              of an airport.
I.119. Safety                                 The state in which the risk of harm to persons or property on the
                                              ground or water surface is reduced to, and maintained at or
                                              below, an acceptable level through a continuing process of hazard
                                              identification and risk management.
I.120. Safety objective                       A measurable goal or desirable outcome related to safety.

I.121. Safety risk                            The composite of predicted severity and likelihood of the
                                              potential effect of a hazard.
I.122. See and avoid              S&A         The requirement for the pilot of an aircraft to ‘see’ and ‘avoid’ a
                                              collision, and to remain well clear of other aircraft in accordance
                                              with 14 CFR 91.113, SERA.3201, and ICAO Annex 2 Section 3.2.



Annex to ED Decision 2025/018/R                                                                      Page 167 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.123. Segregated airspace                    Airspace of specified dimensions allocated for exclusive use to a
                                              specific user(s).
I.124. Sense and avoid            SAA         See, detect and avoid.

I.125. Separation                             Maintaining a specific minimum distance between two or more
                                              aircraft or between aircraft and terrain to avoid collisions,
                                              normally by requiring aircraft to fly at set levels or level bands, on
                                              set routes or in certain directions, or by controlling an aircraft’s
                                              speed.
I.126. Severity                               The consequence or impact of a hazard’s effect or outcome in
                                              terms of degree of loss or harm.
I.127. Sheltering                             Expected protection of people from the UA in case it crashes into
                                              a building or a structure.

I.128. Specific operations        SORA        A methodology to guide both the UAS operator and the
       risk assessment                        competent authority in determining whether a UAS operation can
                                              be conducted in a safe manner.
I.129. ‘Specific’ category                    A UAS operation category where a proportionate approach to the
                                              assessment of the risk will be taken by requiring the UAS operator
                                              to present a specific operations risk assessment (SORA) of the UAS
                                              operation before operational authorisation is granted by the
                                              competent authority.
I.130. Standard operational       SOP         A set of instructions covering those features of operations which
       procedure                              lend themselves to a definite or standardised procedure without
                                              loss of effectiveness.
I.131. Standard scenario          STS         A description of a type of UAS operation for which a specific
                                              operations risk assessment (SORA) has been conducted and on
                                              the basis of which mitigations have been proposed that are
                                              deemed acceptable by the competent authority. The use of a
                                              standard scenario greatly simplifies and expedites the application
                                              process for both the UAS operator and the competent authority.
I.132. Strategic conflict                     A set of procedures aimed at reducing the UAS encounter
       mitigation                             probability prior to UAS take-off. Strategic mitigation is about
                                              controlling or mitigating risks by reducing local aircraft density or
                                              time of exposure of an individual UAS. Strategic mitigations tend
                                              to take the form of operational restrictions of time or space.
                                              Strategic mitigations do not fulfil the 14 CFR 91.113, SERA.3201,
                                              or ICAO Annex 2 Section 3.2 ‘see and avoid’ requirement.
                                              (Examples of strategic mitigation: an operational restriction to fly
                                              between the hours of 10PM and 3AM; operational restriction to
                                              stay below 500 ft AGL; operational restriction to stay within 1 mile
                                              of a geographic location; etc.)
                                              Strategic mitigation traces to the strategic layer of ICAO’s conflict
                                              management concept.

I.133. System                                 A combination of interrelated items arranged to perform a
                                              specific function or specific functions.




Annex to ED Decision 2025/018/R                                                                      Page 168 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.134. System safety                          System safety is a specialty within system engineering that
                                              supports programme risk management. It is the application of
                                              engineering and management principles, criteria and techniques
                                              to optimise safety. The goal of system safety is to optimise safety
                                              through the identification of safety-related risks, eliminating or
                                              controlling them through design and/or procedures, based on
                                              acceptable system safety precedence.
I.135. Tactical conflict                      The act of mitigating collision risk over a very short time horizon
       mitigation                             (minutes to seconds). Tactical mitigations take the form of SDAF
                                              loops (see, decide, action and feedback loop). Tactical mitigation
                                              systems operate using a sensor to ‘see’ the threat, ‘deciding’ how
                                              to mitigate the risk, ‘acting’ on the decision, and then having a
                                              feedback system in order to monitor the risk and implement new
                                              corrections if needed. Tactical mitigation may fulfil the 14 CFR
                                              91.113, SERA.3201 and ICAO Annex 2 Section 3.2 ‘See and Avoid’
                                              requirement (examples of tactical mitigation: TCAS, ATC, ACAS,
                                              MIDCAS, DAA, ABSAA, GBSAA, see and avoid, etc.).
                                              Tactical mitigation traces to the separation requirements and
                                              collision avoidance layers of the ICAO’s conflict management
                                              concept.

I.136. Testing                                The process of operating a system under specified conditions,
                                              observing or recording the results, and making an evaluation of
                                              some aspects of the system.
I.137. Third party                            A party that derives no economic benefit and has no control over
                                              the risk associated with the UAS operation.

I.138. Threat                                 An occurrence that in the absence of appropriate threat barriers
                                              can potentially result in a hazard.

I.139. Total system error                     All errors impacting the position of the UA. It includes the
                                              accuracy of the navigation solution, the flight technical error of
                                              the UAS, as well as the path definition error (e.g. map error) and
                                              latencies. Errors are usually determined by the interaction of
                                              several contributes, such as positioning sensors providing
                                              position, navigation and flight control systems, system and
                                              human latencies, and environment.
I.140. Transponder                TMZ         Airspace of defined dimensions in which the carriage and
       mandatory zone                         operation of pressure-altitude reporting transponders is
                                              mandatory.




Annex to ED Decision 2025/018/R                                                                   Page 169 of 204
                                            AMC & GM to Regulation (EU) 2019/947
                                                   Issue 1, Amendment 3



 Term                             Acronym     Definition
I.141. UA characteristic          UA CD       The width of the UA in the direction transversal to the direction
       dimension                              of flight (refer to Annex F Edition 2.5, critical area). For example:
                                              — for fixed-wing UA, regardless of the number of planes,
                                                including hybrid configurations, the UA characteristic
                                                dimension is the wingspan;




                                              — for rotorcraft UA (e.g. helicopters or gyroplanes), the UA
                                                characteristic dimension is the diameter of the main rotor;




                                              — for VTOL-capable aircraft (VCA), such as multicopters, the UA
                                                characteristic dimension is defined by the maximum distance
                                                (i.e. the diagonal distance) between the blade tips.




I.142. UAS flight manual                      Sometimes also referred to as ‘manufacturer’s instructions’, it is
                                              a manual developed by the designer of the UAS, containing
                                              limitations within which the aircraft is to be considered airworthy,
                                              and instructions and information necessary to the flight crew
                                              members for the safe operation of the aircraft.
I.143. UAS traffic                UTM         A specific aspect of air traffic management which manages UAS
       management (UTM)                       operations safely, economically and efficiently through the
                                              provision of facilities and a seamless set of services in
                                              collaboration with all parties and involving airborne and ground-
                                              based functions. In Europe, it is referred to as
                                              ‘U-space’.
I.144. UAS component                          The organisation designing and producing a component to be
       design and                             installed on a UAS (e.g. a parachute). It is also responsible for
       production                             carrying out the test, check compatibility and interface with the
       organisation                           UAS models listed in the component instructions manual.




Annex to ED Decision 2025/018/R                                                                     Page 170 of 204
                                             AMC & GM to Regulation (EU) 2019/947
                                                    Issue 1, Amendment 3



 Term                             Acronym      Definition
I.145. UAS component                           The organisation responsible for installing a component (e.g. a
       installer                               parachute) on a UAS model listed in the component instructions
                                               manual, using the procedure defined in the same manual.
                                               Depending on the level of integration of the component, the
                                               component installer may be the UAS operator or in some cases
                                               the UAS production organisation or the organisation designated
                                               by them.
I.146. UAS operation                           It may consist in one or multiple flights, even in different locations
                                               and with different purposes, conducted with a UAS with the same
                                               features, characterised by the same final air risk, final ground risk,
                                               SAIL score, ground and air risk mitigations and containment level.
I.147. UAS operator                            Means any legal or natural person operating or intending to
                                               operate one or more UAS.
                                               (Article 2(2) of Implementing Regulation (EU) 2019/947)
                                               See also Section S.2.5(c) of this AMC.

I.148. Uncontrolled                            For the purpose of this assessment, uncontrolled airspace is that
       airspace                                defined as class G airspace.
I.149. Uninvolved persons                      Means persons who are not participating in the UAS operation or
                                               who are not aware of the instructions and safety precautions
                                               given by the UAS operator.
                                               (Article 2(18) of Implementing Regulation (EU) 2019/947)

I.150. Unmanned aircraft          UA           Means any aircraft operating or designed to operate
                                               autonomously or to be piloted remotely without a pilot on board.
                                               (Article 3(30) of Regulation (EU) 2018/1139)

I.151. Unmanned aircraft          UAS          Means an unmanned aircraft, as defined in Article 3(30) of
       system                                  Regulation (EU) 2018/1139, and its control and monitoring unit.
                                               (Article 2(1) of Implementing Regulation (EU) 2019/947)

I.152. Urban air volume                        In the context of air risk, it is the volume above a town or a city,
                                               starting from the ground, where there is a higher probability that
                                               air operations (with or without pilots on board) may take place
                                               for several purposes (e.g. aerial work, delivery, transport,
                                               emergency, etc.).

I.153. U-space                                 The UAS traffic management (UTM) concept defined in Europe
                                               through Implementing Regulation (EU) 2021/664.
I.154. Verified                                A term used to describe controls / safety requirements that are
                                               objectively determined to have been met.

I.155. Very high-level            VHL          Airspace from FL600 and above. The altitude of FL600 is not a hard
       airspace                   airspace     value, but an initial value used in this assessment as a starting
                                               point for discussion. It may be adjusted by the regulatory
                                               authorities as needed. UAS operating in VHL airspace may have to
                                               comply with operating rules, procedures and equipment not yet
                                               identified. VHL airspace is airspace where manned aircraft
                                               operations are very infrequent.




Annex to ED Decision 2025/018/R                                                                       Page 171 of 204
                                              AMC & GM to Regulation (EU) 2019/947
                                                     Issue 1, Amendment 3



 Term                             Acronym       Definition
I.156. Very low-level             VLL           Airspace from ground level to 500 ft AGL. The altitude of
       airspace                   airspace      500 ft AGL is not a hard value, but an initial value used in this
                                                assessment as a starting point for discussion and may be adjusted
                                                by the regulatory authorities as needed. UAS operating in VLL
                                                airspace may have to comply with operating rules, procedures
                                                and equipment not yet identified. VLL airspace is airspace where
                                                manned aircraft operations are very infrequent. VLL airspace
                                                excludes class A, B, C, D, E and F airspace and airport
                                                environments.

I.157. Visual line of sight       VLOS          Means a type of UAS operation in which the remote pilot is able
       operation                  operation     to maintain continuous unaided visual contact with the
                                                unmanned aircraft, allowing the remote pilot to control the flight
                                                path of the UA in relation to other aircraft, people and obstacles
                                                for the purpose of avoiding collisions.
                                                (Article 2(7) of Implementing Regulation (EU) 2019/947)

I.158. VTOL-capable UA                          It includes vertical-lift UA configurations with 3 or more rotors
                                                and fixed-wing aircraft capable of vertically taking off and landing.
                                                It includes multirotor UA.


AMC1bis Article 11 Rules for conducting an operational risk
assessment
SPECIFIC OPERATIONS RISK ASSESSMENT (SORA) (SOURCE: JARUS SORA V2.0)
Edition: December 2020
[…]

AMC1 Article 12(2)(a) Authorising operations in the ‘specific’
category
GRANTING AN OPERATIONAL AUTHORISATION FOR UAS OPERATIONS CLASSIFIED IN A SAIL WHERE
THE LEVEL OF ROBUSTENSS OF OSOS AND MITIGATIONS IS LOW
When the risk assessment defined in Article 11 classifies the level of robustness of the operational
safety objectives and the mitigations as ‘low’, the competent authority may issue an operational
authorisation based on the applicant’s declaration of compliance with the related OSOs and
mitigations.
The same applies in case the level of robustness is classified as ‘medium’ and the applicant has
provided a declaration based on a means of compliance published by EASA.
For a VLOS UAS operation classified up to SAIL II according to AMC1 Article 11 (SORA), the competent
authority may only validate the compliance matrix (i.e. Chapter A.4 of Annex A to AMC1 Article 11)
provided by the UAS operator. The competent authority may authorise the operation without
receiving evidence (e.g. the operations manual).




Annex to ED Decision 2025/018/R                                                                       Page 172 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3



       The applicant is responsible to comply with all the requirements and produce or obtain any required
       evidence (e.g. operations manual) and keep it updated during the time of validity of the operational
       authorisation.



       AMC1 UAS.SPEC.030(2) Application for an operational authorisation
       — EASA Form 208
       APPLICATION FORM FOR AN OPERATIONAL AUTHORISATION
       The UAS operator should submit an application for an operational authorisation according to the
       following form. The application and all the documentation referred to or attached to the application
       should be stored for at least 2 years after the expiry of the related operational authorisation or
       submission of application in case of refusal. The UAS operator should ensure the protection of the
       stored data from unauthorised access, damage, alteration, and theft. The declaration may be
       complemented by the description of the procedures to ensure that all operations are in compliance
       with Regulation (EU) 2016/679 on the protection of natural persons with regard to the processing of
       personal data and on the free movement of such data, as required by point UAS.SPEC.050 (1)(a)(iv) of
       the UAS Regulation.



                                   Application for an operational authorisation for the ‘specific’ category
                                                                   Issue 2




Data protection: Personal data included in this application is processed by the competent authority pursuant to
Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of
natural persons with regard to the processing of personal data and on the free movement of such data, and
repealing Directive 95/46/EC (General Data Protection Regulation). Personal data will be processed for the
purpose of the performance, management and follow-up of the application by the competent authority in
accordance with Article 12 of Regulation (EU) 2019/947 of 24 May 2019 on the rules and procedures for the
operation of unmanned aircraft.
If the applicant requires further information concerning the processing of their personal data or exercising their
rights (e.g. to access or rectify any inaccurate or incomplete data), they should refer to the point of contact of
their competent authority.
The applicant has the right to file a complaint regarding the processing of their personal data at any time to the
national data protection supervisory authority.


   New application                                              Amendment to operational authorisation NNN-
                                                             OAT-xxxxx/yyy
                                                1. UAS operator data
1.1 UAS operator registration number
1.2 UAS operator name
1.3 Operational point of contact


       Annex to ED Decision 2025/018/R                                                               Page 173 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3




   Name
   Telephone
   Email
                                          2. Details of the UAS operation
2.1 Expected date of start of the operation                   DD/MM/YYYY              2.2 Expected         DD/MM/YYYY
                                                                                      end date
2.3 Intended location(s) for the operation
2.43 Risk assessment reference and revision                       SORA edition date __                 PDRA # __-__
                                                              edition date
                                                                    other _________
2.5 Level of assurance and integrity
2.64 Type of operation                                              VLOS        BVLOS
2.75 Transport of dangerous goods                                   Yes         No
2.6 Dropping material                                               Yes         No
2.8 Ground risk            2.8.1 Operational area
characterisation
                           2.8.2 Adjacent area
2.9 Upper limit of the operational volume
2.10 Airspace volume of the intended operation                      A       B     C       D        E       F      G
                                                                    U-space          Other, specify
2.11 Residual air risk     2.12.1 Operational volume                ARC-a       ARC-b      ARC-c        ARC-d
level
                           2.11.2. Adjacent volume                  ARC-a       ARC-b      ARC-c        ARC-d
2.7 What is the minimum RP:UA ratio allowed                   RP:UA ___:____
between the remote pilot (RP) and the UA that may be
operated simultaneously?
2.128 Operations manual reference
2.139 Compliance evidence matrix file reference
                                                      3. UAS data
3.1                                                           3.2 Model name
ManufacturerDesign
organisation name
3.3 Type of UAS                Aeroplane Fixed-wing           3.4 Maximum UA               _____ m
                                                              characteristic
                               Rotorcraft- – Hhelicopter
                                                              dimensions
                               Rotorcraft-gyroplane
                               VTOL-capable aircraft
                                (VCA) (including
                                multirotors)
                               Lighter than air / other



       Annex to ED Decision 2025/018/R                                                                     Page 174 of 204
                                              AMC & GM to Regulation (EU) 2019/947
                                                     Issue 1, Amendment 3




3.5 Take-off mass           _____ kg                        3.6 Maximum              _____ m/s (_____ kt)
                                                            operational speed
3.7 Type of C2 link
3.8 Size of the adjacent ground area                        ____ km
3.9 Is the UAS tethered during the operation?                  Yes        No
3.10 Type of propulsion system                                 Electric       Combustion
                                                               Hybrid, specify type: ______________________
                                                               Other, please specify: _____________________
3.711 Serial number or, if applicable, UA registration
mark
3.812 Type certificate (TC) or design verification report
(DVR) number and issue date, if applicable
3.913 Number of the certificate of airworthiness
(CofA), if applicable
3.140 Number of the noise certificate, if applicable
3.15 E-conspicuity system                                      Direct remote ID        Network remote ID
                                                               SRD-860 In              SRD-860 Out
                                                               ADS-B In           ADS-B Out     Other________
3.16 Green flashing light                                      Yes            No
                                                               No      Yes, low      Yes, medium     Yes, high
3.11 Mitigation of effects of ground impact

3.1213 Technical requirements for containment                  Basic      Enhanced


   I, the UAS operator, declare that:
    — the UAS operation complies with any applicable Union and national regulations related to privacy, data
        protection, liability, insurance, security, and environmental protection;
    — I have developed procedures to ensure that the intended UAS operation complies with the security
        requirements applicable to the area(s) of operation;
    — I have developed measures to protect against unlawful interference and unauthorised access;
    — I have developed procedures to ensure that all flights comply with Regulation (EU) 2016/679 on the
        protection of natural persons with regard to the processing of personal data and on the free movement
        of such data;
    — I have developed procedures for the remote pilot(s) to plan UAS operations in a manner that minimises
        nuisance, including noise- and other emissions-related nuisance, to people and animals;
    — I have records of:
          — all relevant qualifications and training courses completed by the remote pilot(s) and other
             personnel in charge of duties essential to the UAS operation and by maintenance staff, for at least
             3 years after those persons have ceased employment with the organisation or have changed their
             position within the organisation;
          — the maintenance activities carried out on the UAS for a minimum of 3 years;




       Annex to ED Decision 2025/018/R                                                          Page 175 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3



       — the information on UAS operations, including any unusual technical or operational occurrences and
            other data as required by the declaration or by the operational authorisation for a minimum of 3
            years;
       — an up-to-date list of designated remote pilots-in-command for each flight, and if applicable, for
            each phase of flight;
       — an up-to-date list of maintenance staff employed to carry out maintenance activities;
    — the insurance coverage, if applicable, will be in place at the expected date of start of the UAS operation.

                                   Section 4 – Specific operations risk assessment (SORA)


                                    Step #1 — Documentation of the proposed operation


Step #1.1 Description of proposed locations      •   If location-specific:
                                                 Give reference to the file:
                                                 ___________________________________


                                                 •   If location-independent: (generic authorisation)
                                                 Give reference to the file as example of a location:
                                                 ___________________________________


Step #1.2 Short description of the proposed operation



Step #1.3 Dimensions of the operational          Maximum height of the flight          HFGmax      ________ m
   volume and the adjacent volume                geography
   (Rounded up to first decimal place)
                                                 Maximum height of the                 HCVmax      ________ m
                                                 contingency volume

                                                 Width of the contingency volume SCVmax            ________ m

                                                 Width of the ground risk buffer       SGRBmax     ________ m

                                                 Width of the adjacent volume          SAV         ________ m


                                   Step #2 — UAS intrinsic ground risk class (iGRC)


Step #2.1 Type of operational areas or               controlled ground area                  people/km2
    maximum population density on the                sparsely populated area                      up to 5
    ground (including flight geography,
                                                                                                 up to 50
    contingency volume and ground risk
    buffer)                                                                                     up to 500



       Annex to ED Decision 2025/018/R                                                               Page 176 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3



                                                    populated area                          up to 5 000
                                                                                            up to 50 000
                                                                                       more than 50 000
                                                     assemblies of people                       no limit


Step #2.2 Specify the intrinsic ground risk
   class (iGRC)


Step #2.3 Remarks/Reasoning for Step #2 (optional)




                          Step #3 — Final ground risk class (GRC) determination (optional)


Step #3.1 Specify the ground risk mitigations M1(A) Strategic mitigation — sheltering
    applied and the level of robustness
    (if applicable)                           ☐None         ☐Low       ☐Medium


                                                 M1(B) Strategic mitigation — operational restrictions

                                                 ☐None                       ☐Medium                ☐High


                                                 M1(C) Tactical mitigation — ground observation

                                                 ☐None           ☐Low


                                                 M2 Effects of UA impact dynamics are reduced

                                                 ☐None                       ☐Medium             ☐High


Step #3.2 Specify the final ground risk class
   (GRC)


Step #3.2 Remarks/Reasoning for Step #3 (optional)



                                         Step #4 — Initial air risk class (ARC)


Step #4.1 Classification of the airspace where ☐A       ☐B      ☐C            ☐D       ☐E      ☐F          ☐G
    the operation is intended to be
    conducted (multiple answers possible)
                                               ☐Restricted area                         ☐Danger area




       Annex to ED Decision 2025/018/R                                                              Page 177 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3




                                                 ☐TMZ          ☐RMZ          ☐ATZ        ☐CTR        ☐CTA        ☐FIZ


Step 4.2 Specify the initial air risk class (ARC) ☐ARC-a     ☐ARC-b ☐ARC-c ☐ARC-d
    of the operational volume




Step #4.3 Remarks/Reasoning for choosing the ARC in Step #4



                         Step #5 — Strategic air risk mitigations and final air risk class (ARC)


Step #5.1 Specify the strategic mitigations of                                ☐ VLOS
    the air risk class, if applied
                                                                              ☐BVLOS with AOs
                                                 ☐No
                                                                              ☐ Operational restrictions

                                                                              ☐ Common rules and structures


Step #5.2 Residual air risk class                ☐ARC-a ☐ARC-b ☐ARC-c ☐ARC-d
    (after strategic mitigation)


Step #5.3 Remarks/Reasoning for Step #5 (not needed if no mitigation applied)




             Step #6 — Tactical mitigation performance requirements (TMPRs) and robustness level


Step #6 Tactical mitigation performance          ☐ No requirement (VLOS / BVLOS with AOs)
        requirements (TMPRs)
                                                 ☐BVLOS

                                                    ☐No requirement (ARC-a)

                                                    ☐Low (ARC-b)

                                                    ☐Medium (ARC-c)

                                                    ☐High (ARC-d)


Step #6.1 Remarks/Reasoning for Step #6 (optional)




       Annex to ED Decision 2025/018/R                                                             Page 178 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3




                                            Step #7 — SAIL determination


Step #7.1 Specific assurance and integrity       ☐SAIL I ☐SAIL II      ☐SAIL III   ☐SAIL IV       ☐SAIL V   ☐SAIL VI
    level (SAIL)


                               Step #8 — Determination of containment requirements


Step #8.1 Containment                            ☐Low ☐Medium ☐High                    Tethered


Step #8.2 Assembly of people within 1 km of
                                            ☐No ☐Yes
  the operational volume?


Step #8.2 Remarks/Reasoning for Step #8 (optional)




                           Step #9 — Identification of operational safety objectives (OSOs)


Step #9.1 Operational safety objectives



                                                     45. Remarks




                                             5. Declaration of compliance
I, the undersigned, hereby declare that the UAS operation will comply with:
— any applicable Union and national regulations related to privacy, data protection, liability, insurance, security,
     and environmental protection;
— the applicable requirements of Regulation (EU) 2019/947; and
— the limitations and conditions defined in the operational authorisation provided by the competent authority.
Moreover, I declare that the related insurance coverage, if appliable, will be in place at the start date of the UAS
operation.
Date                                                      Signature and stamp
DD/MM/YYYY
EASA Form 208
       Instructions for filling in the application form
       If the application relates to an amendment to an existing operational authorisation, indicate the
       number of the operational authorisation and fill out in red the fields that are amended compared to
       the last operational authorisation.


       Annex to ED Decision 2025/018/R                                                               Page 179 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3




Annex to ED Decision 2025/018/R                                          Page 180 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



Section 1
1.1    UAS operator registration number in accordance with Article 14 of the UAS Regulation.
1.2    UAS operator’s name as declared during the registration process.
1.3    Name of the accountable manager or, in the case of a natural person, the name of the UAS
       operator.
1.34 Contact details of the person responsible for the operation, in charge to answer possible
     operational questions raised by the competent authority.
2.1    Date on which the UAS operator expects to start the operation.

Section 2
2.2    Date on which the UAS operator expects to end the operation. The UAS operator may ask for
       an unlimited duration; in this case, indicate ‘Unlimited’.
2.3    Location(s) where the UAS operator intends to conduct the UAS operation. The identification of
       the location(s) should contain the full operational volume and ground risk buffer (the red line
       in Figure 1). Depending on the initial ground and air risk and on the application of mitigation
       measures, the location(s) may be ‘generic’ or ‘precise’ (refer to GM2 UAS.SPEC.030(2)).


                                        Ground risk buffer
                 Adjacent area            Operational area              Adjacent area



                           Figure 1 — Operational area and ground risk buffer
2.43 Select one of the three options. If the SORA is used, indicate the version edition date as defined
     in AMC1 Article 11. In case a PDRA is used, indicate the number and its revision edition date as
     defined in the applicable AMC to Article 11. In case a risk assessment methodology is used other
     than the SORA, provide its reference. In this last case, the UAS operator should demonstrate
     that the methodology complies with Article 11 of the UAS Regulation. In case a PDRA is used,
     then section 4 of this form is not required to be completed.
2.5    If the risk methodology used is the SORA, indicate the final SAIL of the operation, otherwise the
       equivalent information provided by the risk assessment methodology used.
2.6    Select one of the two options.
2.7    Select one of the two options. If the UAS flight manual provided by the UAS designer indicates
       that it is designed with a level of automation that reduces the remote pilot’s workload allowing
       one remote pilot (RP) to control multiple UA simultaneously, then specify the number of UA
       that one remote pilot is permitted to control (e.g. in case one RP is able to control
       simultaneously five UA, indicate RP:UA 1:5). This number should not exceed the limit defined in
       the UAS flight manual. Additionally, the UAS operator may decide to have a pool of remote
       pilots controlling multiple UA simultaneously. In this case, clear procedures should be
       developed to define who is the pilot-in-command, responsible during each phase of the flight
       (e.g. in case three RPs are permitted to control simultaneously ten UA, indicate RP:UA 3:10).
2.8    Characterise the ground risk (i.e. density of overflown population density, expressed in persons
       per km2, if available, or ‘controlled ground area’, ‘sparsely populated area’, ‘populated area’,
       ‘gatherings of people’) for both the operational and the adjacent area.



Annex to ED Decision 2025/018/R                                                           Page 181 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



2.9    Insert the maximum flight altitude, expressed in metres and feet in parentheses, of the
       operational volume (adding the air risk buffer, if applicable) using the AGL reference when the
       upper limit is below 150 m (492 ft), or use the MSL reference when the upper limit is above
       150 m (492 ft).
2.10 Select one or more of the nine options. Select ‘Other’ in case none of the previous applies (i.e.
     military areas).
2.11 Select one of the four options.
2.128 Indicate the OM’s identification and revision number. This document should be attached to the
      application.
2.139 Indicate the compliance evidence matrix file identification and revision number. (e.g. the
      compliance matrix defined in Chapter A.4 of Annex A to AMC1 Article 11 (SORA). This document
      should be attached to the application.

Section 3
This section may be replicated for all authorised UAS models to be used under this operational
authorisation.
3.1    Name of the manufacturer of the UAS.
3.2    Model of the UAS as defined by the manufacturerdesign organisation in the UAS flight manual.
3.3    Select one of the five options. Fixed-wing UA includes configurations such as aeroplanes, kites,
       gliders, etc.).
       Rotorcraft-helicopter UA includes all vertical-lift configurations having up to 2 rotors.
       Rotorcraft-gyroplane UA is a special configuration with unpowered rotor.
       VTOL-capable aircraft (VCA) UA includes vertical-lift configurations with 3 or more rotors and
       fixed-wing UA capable of vertically taking off and landing.
       Lighter-than-air configurations include configurations such as airships, hot-air balloons, etc.
3.4    Indicate the maximum dimensions of the UA in metres (refer to definition I.141 ‘UA
       characteristic dimension’ in Annex I of AMC1 Article 11 (SORA)). e.g. for aeroplanes: the length
       of the wingspan; for helicopters: the diameter of the propellers; for multirotors: the maximum
       distance between the tips of two opposite propellers) as used in the risk assessment to identify
       the ground risk.
3.5    Indicate the maximum value, expressed in kg, of the UA take-off mass (TOM), expressed in kg,
       at which the UAS operation may be operated. All flights should then be conducted without
       operated not exceeding that the specified TOM. The TOM may be different from (however, not
       exceeding higher than) the MTOM defined by the UAS manufacturerdesign organisation in the
       UAS flight manual.
3.6    Maximum operational cruise airspeed, expressed in m/s and kt in parentheses, that the remote
       pilot will not exceed during the operation. This should always be lower than the maximum as
       defined in the manufacturer’s instructions UAS flight manual.
3.7    Indicate the type of C2 link to be used during the operation (e.g. radio link, LTE/5G, satellite,
       etc.).
3.8    indicate the size in km to be considered for the adjacent ground area starting from the limits of
       the ground risk buffer, using the instructions defined in Section S.4.8.4 of AMC1 Article 11
       (SORA).



Annex to ED Decision 2025/018/R                                                             Page 182 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



3.711 This field is mandatory if the UA is registered according to Article 14(7) of Implementing
      Regulation (EU) 2019/947. If the UA is not registered, the NAA may indicate the Uunique serial
      number (SN) of the UA defined by the manufacturer design organisation according to standard
      ANSI/CTA-2063-A-2019, Small Unmanned Aerial Systems Serial Numbers, 2019, or the UA
      registration mark if the UA is registered. In case of privately built UAS or UAS not equipped with
      a unique SN, insert the unique SN of the remote identification system. For UAS operations
      classified in SAIL V or higher, the serial numbers of all UAS should be provided and any change
      to them would require the competent authority’s prior approval. For UAS operations classified
      up to SAIL IV, a change to the serial number does not require a prior approval from the
      competent authority.
3.812 Include the EASA TC number, or the UAS design verification report (DVR) number issued by
      EASA, if applicable.
3.913 If a UAS with an EASA TC is required by the competent authority, the UAS should have a
      certificate of airworthiness (CofA).
3.1014 If a UAS with an EASA TC is required by the competent authority, the UAS should have a noise
      certificate.
3.15 Multiple options are possible. Direct remote ID developed according to EN 4709-002.
3.11 Select one of the four options.
3.12 Select one of the two options.
In order to compile Section 4, please refer to AMC1 Article 11 (SORA).

Section 4
Step #1.1:
The identification of the location(s) should contain the full operational volume and ground risk buffer
(the red line in Figure 1; refer to Annex A to AMC1 Article 11 for guidance and examples on the
calculation of the operational volume and ground risk buffer). Depending on the initial ground and air
risk classification determined using the SORA process and on the application of mitigations, the
location(s) may be ‘generic’ or ‘precise’ (refer to GM2 UAS.SPEC.030(2)).


                                            Ground risk buffer
                     Adjacent area            Operational area              Adjacent area




                             Figure 1 — Operational area and ground risk buffer

—      Please, refer to GM2 UAS.SPEC.030(2) for guidance on the conditions to apply for ‘generic’
       versus ‘precise’ locations.
—      If location-specific: please, provide a list with the geo-coordinates for each location including
       the operational volume (flight geography and contingency volume), the ground risk buffer and
       the air risk buffer (if available) as a separate file using either ‘.txt’, ‘.kmz’ or ‘.kml’.
—      If location-independent: please, provide a reference to the documented process for the
       determination of volumes and buffers and the assessment of the local conditions and their



Annex to ED Decision 2025/018/R                                                             Page 183 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3



       compliance limitations. An example of a geographical file (e.g. ‘.kmz’ or ‘.kml’) may be provided
       to show a typical operational volume, ground risk buffer and the air risk buffer (if available).
Step #1.2: Insert, for example, transport, inspection, filming, testing, etc.
Step #1.3: Please, provide a list with this information if location-specific with multiple locations.
Step #4.1: For information on the airspace classification, refer to Article 2 and to points SERA.6001
and SERA.6005 of Regulation (EU) No 923/2012.
Step #9.1: List the OSOs and the level of robustness you intend to comply with. The level of robustness
should as a minimum reflect the one defined in Table 14 of Section S.4.9.3 of AMC1 Article 11
considering the SAIL listed in point ‘Step #7.1’ of this form.

Section 5         Free-text field for the addition of any relevant remark.
Note 1: Section 3 may include more than one UAS. In that case, it should be filled in with the data of
all the UASs intended to be operated. If needed, fields may be duplicated.
Note 2: The signature and stamp may be provided in electronic form.



AMC1 UAS.SPEC.030(3)(e)                          Application            for      an      operational
authoriszation
OPERATIONS MANUAL — TEMPLATE
For all operations classified in the ‘specific’ category, the UAS operator should develop an OM
structured according to Chapter A.3 of Annex A of AMC1 Article 11.
The OM should be submitted to the competent authority for operations classified in SAIL III and higher.
For operations classified in SAIL I or II, please refer to AMC1 Article 12(2)(a).
When required in accordance with UAS.SPEC.030(3)(e), the OM should contain at least the
information listed below, if applicable, customised for the area and type of operation.
0.     Cover and contact.
       0.1    Cover identifying the UAS operator with the title ‘Operations Manual’, contact
              information and OM revision number.
       0.2    Table of contents.
1.     Introduction
       1.1    Definitions, acronyms and abbreviations.
       1.2    System for amendment and revision of the OM (list the changes that require prior
              approval and the changes to be notified to the competent authority).
       1.3    Record of revisions with effectivity dates.
       1.4    List of effective pages (list of effective pages unless the entire manual is re-issued and the
              manual has an effective date on it).
       1.5    Purpose and scope of the OM with a brief description of the different parts of the
              documents.



Annex to ED Decision 2025/018/R                                                              Page 184 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3



       1.6    Safety statement (include a statement that the OM complies with the relevant
              requirements of Regulation (EU) 2019/947 and with the authorisation or the terms of
              approval of the light UAS operator certificate (LUC), in the case of a LUC holder, and
              contains instructions that are to be complied with by the personnel involved in flight
              operations).
       1.7    Approval signature (the accountable manager must sign this statement).
2.     Description of the UAS operator’s organisation (include the organigram and a brief description
       thereof).
3.     Concept of operations (ConOps
       For each operation, please describe the following:
       3.1    Nature of the operation and associated risks (describe the nature of the activities
              performed and the associated risks).
       3.2    Operational environment and geographical area for the intended operations (in general
              terms, describe the characteristics of the area to be overflown, its topography, obstacles
              etc., and the characteristics of the airspace to be used, and the environmental conditions
              (i.e. the weather and electromagnetic environment); the definition of the required
              operation volume and risk buffers to address the ground and air risks).
       3.3    Technical means used (in general terms, describe their main characteristics, performance
              and limitations, including UAS, external systems supporting the UAS operation, facilities,
              etc.)
       3.4    Competency, duties and responsibilities of personnel involved in the operations such as
              the remote pilot, UA observer, visual observer (VO), supervisor, controller, operations
              manager, etc. (initial qualifications; experience in operating UAS; experience in the
              particular operation; training and checking; compliance with the applicable regulations
              and guidance to crew members concerning health, fitness for duty and fatigue; guidance
              to staff on how to facilitate inspections by competent authority personnel).
       3.5    Risk analysis and methods for reduction of identified risks (description of methodology
              used; bow-tie presentation or other).
       3.6    Maintenance (provide maintenance instructions required to keep the UAS in a safe
              condition, covering the UAS manufacturer’s maintenance instructions and requirements
              when applicable).
4.     Normal procedures;
       (The UAS operator should complete the following paragraphs considering the elements listed
       below. The procedures applicable to all UAS operations may be listed in paragraph 4.1.)
       4.1    General procedures valid for all operations
       4.2    Procedures peculiar to a single operation
5.     Contingency procedures
       (The UAS operator should complete the following paragraphs considering the elements listed
       below. The procedures applicable to all UAS operations may be listed in paragraph 5.1).
       5.1    General procedures valid for all operations
       5.2    Procedures peculiar to a single operation
6.     Emergency procedures



Annex to ED Decision 2025/018/R                                                           Page 185 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3



         (The UAS operator should define procedures to cope with emergency situations.)
7.       Emergency response plan (ERP) (optional)
8.       Security (security procedures referred to in UAS.SPEC.050(a)(ii) and (iii); instructions, guidance,
         procedures, and responsibilities on how to implement security requirements and protect the
         UAS from unauthorised modification, interference, etc.]
9.       Guidelines to minimise nuisance and environmental impact referred to in UAS.SPEC.050(a)(v);
10.      Occurrence reporting procedures according to Regulation (EU) No 376/2014.
11.      Record-keeping procedures (instructions on logs and records of pilots and other data
         considered useful for the tracking and monitoring of the activity).



AMC2 UAS.SPEC.030(3)(e)                                Application                for        an        operational
authorisation
OPERATIONAL PROCEDURES WITH ‘MEDIUM’ AND ‘HIGH’ LEVEL OF ROBUSTNESS
1.       Scope of this AMC
         1.1     This AMC addresses the criteria for the ‘medium’ and ‘high’ level of robustness of the
                 operational procedures that are required under the following OSOs:
                 (a)     OSO #08: Technical issue with the UAS — Operational procedures are defined,
                         validated and adhered to.;
                 (b)     OSO #11: Deterioration of the external systems that support the UAS operations —
                         Procedures are in place to handle the deterioration of the external systems that
                         support the UAS operations;
                 (c)     OSO #14: Human error — Operational procedures are defined, validated and
                         adhered to; and
                 (d)     OSO #21: Adverse operating conditions — Operational procedures are defined,
                         validated and adhered to.
                 These criteria may be used to also address the criteria for the ‘medium’ and ‘high’ levels
                 of robustness of the operational procedures required in other sections of the SORA
                 (e.g. under the mitigations means for the ground risk, which are defined in Annex B to
                 AMC1 Article 11 or for the air risk defined in Annex D to Article 11.
2.         Criteria for the level of integrity

         2.1.    Criterion #1: Procedure definition
                 2.1.1. Annex E to AMC1 Article 11 provides the minimum elements that the operational
                        procedures need to appropriately cover for the intended UAS operations.
                 2.1.2. Chapter A.3 of Annex A to AMC1 Article 11 provides an example of an operations
                        manual structure and a table referencing each OM chapter with the OSOs the
                        requirements refer to. AMC1 UAS.SPEC.030(3)(e) on the OM template53 for the


53    EASA is working within JARUS to amend Annex A to the SORA. When this activity will be completed (planned for 2022/Q2)
      the title of Annex A will be changed to ‘Operations manual’ and it will describe how the UAS operator should develop an




Annex to ED Decision 2025/018/R                                                                             Page 186 of 204
                                             AMC & GM to Regulation (EU) 2019/947
                                                    Issue 1, Amendment 3



                      operational authorisation of UAS operations in the ‘specific’ category and the
                      corresponding guidance in GM1 UAS.SPEC.030(3)(e) should be followed to define
                      the procedures, as they provide more details on the elements that are referred to
                      in point 2.1.1.
        2.2.   Criterion #2: Procedure complexity
               2.2.1. Based on the SORA criterion of ‘procedure complexity’ for a low level of integrity,
                      procedures with a higher level of integrity should not be complex. This implies that
                      the workload and/or the interactions with other entities (e.g. air traffic
                      management (ATM), etc.) of remote pilots and/or other personnel in charge of
                      duties essential to the UAS operation should be limited to a level that may not
                      jeopardise their ability to adequately follow the procedures.
               2.2.2. Procedures should be validated in accordance with point 3.5.
        2.23. Criterion #23: Consideration of potential human error
               Operational procedures should be developed to minimise human errors:
               (a)    each of the tasks and the complete sequence of the tasks of a procedure should be
                      intuitive, unambiguous, and clearly defined;
               (b)    the tasks should be clearly assigned to the relevant roles and persons, ensuring a
                      balanced workload (see point 2.2); and
               (c)    the procedures should adequately address fatigue and stress, considering, among
                      other aspects, the following: duty times, regular breaks, rest periods, the
                      applicable health and safety requirements in the operational environment,
                      handover/takeover procedures, responsibilities, and workload.
        2.3.   Criterion #3: Emergency response plan (ERP)
               For more information regarding the ERP procedure, the UAS operator should refer to
               AMC3 UAS.SPEC.030(3)(e).
3.      Criteria for the level of assurance
        3.1.   The purpose of the validation process described in this AMC is to confirm whether the
               proposed operational procedures are complete and adequate to ensure the safe conduct
               of the intended UAS operations.
        3.2.   The validation process should include the following:
               (a)    a review of the completeness of the procedures to ensure that:
                      (1)    all elements that are indicated in points 2.1.1 and 2.1.2 have been
                             addressed; and
                      (2)    all relevant references have been considered, including but not limited to:

                             (i)     the applicable regulations;
                             (ii)    the requirements from the competent authority and/or other
                                     relevant authorities or entities;
                             (iii)   the local requirements and conditions;


     operations manual with a content proportionate to SAIL of its operation. Annex A to the SORA will also replace
     AMC1 UAS.SPEC.030(3)(e) and GM1 UAS.SPEC.030(3)(e).




Annex to ED Decision 2025/018/R                                                                     Page 187 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3



                            (iv)    the available recommended practices for the intended type of UAS
                                    operations;
                            (v)     the instructions from the UAS designer manufacturer and of any other
                                    UAS equipment designer manufacturer, if applicable;
                            (vi)    the instructions and requirements from externally provided services
                                    that support the UAS operations, if applicable;
                            (vii)   the results from previous experience, including tests and/or
                                    simulations as those indicated in point (c) and (d); and
                            (viii) consensus-based voluntary industry standards;
              (b)    an expert judgement to assess the adequacy of the procedures based on:
                     (1)    the objective(s) of each procedure;
                     (2)    relevant key performance parameters/indicators and/or benchmarking of
                            options, if applicable;
                     (3)    an assessment of the procedures’ complexity in accordance with point 2.2;
                            and
                     (4)    an assessment of the effect of human factors on procedures in accordance
                            with point 2.32;
              (c)    a proof of the adequacy of the procedures through tests or practical exercise for
                     phases of the UAS operation other than the UA flight, which involve the UAS and/or
                     any external system that supports the operation;
              (d)    a proof of the adequacy of the contingency and emergency procedures through:
                     (1)    dedicated flight tests conducted in an area with reduced air and ground risk
                            and/or representative subsystems tests; or
                     (2)    simulation, provided it is proven valid for the intended purpose with positive
                            results; or
                     (3)    any other means acceptable to the competent authority that issues the
                            authorisation;
              (e)    if the option in point (d)(3) is selected, a substantiation of the suitability of those
                     means for proving the adequacy of the procedures;
              (f)    a record of proof of the adequacy of the procedures, including at least:
                     (1)    the UAS operator’s name and registration number;
                     (2)    the date(s) and place(s) of tests or simulations;
                     (3)    identification of the means used, e.g. for tests or simulations that use actual
                            UASs: the type category, the name of the UAS designer manufacturer, and
                            the model and serial number of each UA used;
                     (4)    a description of tests or simulations conducted, including their purpose, the
                            expected results (including key performance parameters/indicators, where
                            relevant), how they were conducted, the results obtained, and conclusions;
                            and
                     (5)    the signature of the person that is appointed by the UAS operator to conduct
                            the tests or simulations;



Annex to ED Decision 2025/018/R                                                              Page 188 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



              (g)    for UAS operations that require a ‘high’ level of assurance, the procedures and the
                     dedicated flight tests, simulations, or other means acceptable to the competent
                     authority, which are indicated in point 3.2, validated by the competent authority
                     that issues the authorisation or by an entity that is recognised by that competent
                     authority.
       3.3.   The following conditions apply to the dedicated flight tests that are indicated in
              point 3.2(d)(1):
              (a)    the configuration of the UAS hardware and software should be identified;
              (b)    the UAS operator should conduct the dedicated flight tests;
              (c)    if no simulations as the ones indicated in point 3.2(d)(2) are conducted, the
                     dedicated flight tests should cover all the relevant aspects of the contingency and
                     emergency procedures;
              (d)    for UAS operations that require a ‘high’ level of assurance, the dedicated flight
                     tests that are performed to validate the procedures and checklists should cover the
                     complete flight envelope or proven to be conservative;
              (e)    the UAS operator should conduct as many flight tests as agreed with the
                     competent authority to prove the adequacy of the proposed procedures;
              (f)    the dedicated flight tests should be conducted in a safe environment (reducing the
                     ground and air risks to the greatest extent possible), while ensuring the
                     representativeness of the tests’ results for the intended UAS operations; and
              (g)    the UAS operator should record the flight tests as part of the information to be
                     recorded as per point UAS.SPEC.050(1)(g), e.g. in a logbook, as indicated in
                     AMC1 UAS.SPEC.050(1)(g); such a record should include any potential issues
                     identified.
       3.4.   To ensure that the integrity criterion of point 2.2 is met, the complexity of the procedures
              should be validated. The UAS operator should reduce the complexity of the procedures
              as much as possible.
              3.4.1. This validation should The verification of the complexity of the procedures may
                     include:
                     (a)    an expert judgement, as indicated in point 3.3(b); and
                     (b)    a proof of the adequacy of the procedures, as indicated in point 3.3(c) and
                            (d).
              3.4.2. The UAS operator should may adopt a method for the evaluation of the complexity
                     of the procedures applied by the relevant personnel, i.e. the remote pilot and/or
                     other personnel in charge of duties essential to the UAS operation. That method
                     should be adequate for the evaluation of the workload that is required by the
                     task(s) of each procedure.
                     For example, a suitable method for evaluating the workload of the remote pilot
                     and/or other personnel in charge of duties essential to the UAS operation may be
                     the ‘Bedford Workload Scale’, which was conceived as a qualitative and relatively
                     simple methodology for rating the pilots’ workload that is associated with the
                     design of an aircraft’s human–machine interface (HMI). However, this
                     methodology is deemed to be adequately generic to be also applicable to the tasks
                     associated with the operational procedures to be conducted by remote pilots
                     and/or other personnel in charge of duties essential to the UAS operation.


Annex to ED Decision 2025/018/R                                                             Page 189 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3



                     Figure 1 depicts the Bedford Workload Scale adapted to operational procedures
                     for UAS operations: ‘pilot’ is replaced by ‘remote crew member’ (i.e. the remote
                     pilot or other personnel in charge of duties essential to the UAS operation), and
                     ‘pilot decision’ is replaced by ‘remote crew member performs a procedure task’.
                     A procedure may include one or more tasks.




    Figure 1 — Bedford Workload Scale adapted to operational procedures for UAS operations




Annex to ED Decision 2025/018/R                                                         Page 190 of 204
                                           AMC & GM to Regulation (EU) 2019/947
                                                  Issue 1, Amendment 3




AMC3 UAS.SPEC.030(3)(e) Application                                   for         an    operational
authorisation
EMERGENCY RESPONSE PLAN (ERP) WITH ‘MEDIUM’ AND ‘HIGH’ LEVEL OF ROBUSTNESS
1.     Scope of this AMC
       1.1    This AMC defines the content of an ERP as well as the methodology for its validation.
              It may be used to meet Criterion #41 (Procedures) of Mitigation M3 — An ERP is in place,
              UAS operator validated and effective of Annex B to AMC1 Article 11 for medium and high
              level of robustness. of OSO #8 (ERP) of Annex E to AMC1 Article 11.
       1.2    The risk assessment, as required by Article 11 of the UAS Regulation, should address the
              safety risks that are associated with the loss of control of a UAS operation, which may
              result in:
              (a)    fatal injuries to third parties on the ground;
              (b)    injuries to third parties in the air; or
              (c)    damage to critical infrastructure.
              Note: As per point Section S.2.3.2 of B.4 of Annex B to AMC1 Article 11, the loss of control
                    of a UAS operation corresponds to situations where the contingency emergency
                    procedures would not have provided achieved the desired effect., the UAS
                    operation is in an unrecoverable state, and:
              the outcome of the situation relies highly on providence; or
              the situation could not be handled via a contingency procedure; or
              there is a grave and imminent danger of fatalities.
       1.3.   Therefore, in line with the risk assessment applied, the scope of this AMC is limited to
              addressing the response to emergency situations that are caused by the UAS operation,
              as well as the potential consequences that are indicated in point 1.2. However, the
              response to such emergency situations should not be limited to the potential risk/harm
              only to third parties but also to the UAS operator’s personnel.
       1.4.   […]
2.     Purpose of the ERP
       […]
3.     Effectiveness of the ERP
       […]
4.     Emergency situations, response activation, procedures, and checklists
       […]


5.     Roles, responsibilities, and key points of contact
       […]
6.     Emergency response means
       […]



Annex to ED Decision 2025/018/R                                                             Page 191 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3



7.     ERP validation
       7.1.   [..]
       7.2.   […]
              (f)     is performed with the periodicity that is indicated in the ERP.
              However, if the UAS operator is a one-person entity and does not manage external
              personnel in an emergency response, a tabletop exercise may not be appropriate as the
              participation of third parties is not required. In such case, the conditions of point 7.1 are
              deemed sufficient and proportionate to the level of simplicity of the operator and, in
              principle, of the UAS operations.
              For UAS operators with a more complex structure as well as for complex UAS operations,
              the tabletop exercises may need to be complemented with partial emergency exercises
              and/or full-scale exercises, including the corresponding drills. If the level of robustness
              that is required or claimed for the ERP is high, such exercises and drills are needed.
       7.3.   If the level of robustness of the ERP is high:
              (a)     the ERP and its effectiveness with respect to limiting the number of people at risk
                      should be validated by the competent authority itself or by an entity designated by
                      the competent authority;
              (b)     the UAS operator should coordinate and agree on the ERP with all third parties that
                      are identified in the plan; and
              (c)     the representativeness of the tabletop exercise is validated by the competent
                      authority that issues the authorisation or by an entity that is designated by that
                      competent authority.
       7.43. After following the procedures that are described in the ERP in a real emergency
             situation, the UAS operator should conduct an analysis of the way the emergency was
             managed and verify the effectiveness of the ERP.
8.     ERP training
       […]
       8.4.   The competent authority that issues the authorisation or an entity that is designated by
              that competent authority should verify the competencies of the relevant personnel if the
              level of assurance that is required or claimed for the ERP is high.


GM1 UAS.SPEC.030(3)(e) Application for an operational
authorisation
OPERATIONS MANUAL — TEMPLATE
A non-exhaustive list of topics to be considered by the UAS operator when compiling
some chapters of the OM is provided below:
‘1.2   System for amendment and revision of the OM’
       (a)    A description of the system for indicating changes and of the methodology for recording
              effective pages and effectivity dates; and
       (b)    Details of the person(s) responsible for the revisions and their publication.
‘2     Description of the UAS operator’s organisation’



Annex to ED Decision 2025/018/R                                                               Page 192 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



       (a)    The organisational structure and designated individuals. Description of the operator’s
              organisational structure, including an organisational chart showing the different
              departments, if any (e.g. flight/ground operations, operational safety, maintenance,
              training, etc.) and the head of each department;
       (b)    Duties and responsibilities of the management personnel; and
       (c)    Duties and responsibilities of remote pilots and other members of the organisation
              involved in the operations (e.g. payload operator, ground assistant, maintenance
              technician, etc.).
‘3.4   Competency, duties and responsibilities of personnel involved in the operations such as the
       remote pilot, UA observer, VO, supervisor, controller, operations manager etc.’
       (a)    Theoretical, practical (and medical) requirements for operating UAS in compliance with
              the applicable regulation;
       (b)    Training and check programme for the personnel in charge of the preparation and/or
              performance of the UAS operations, as well as for the VOs, when applicable;
       (c)    Training and refresher training records; and
       (d)    Precautions and guidelines involving the health of the personnel, including precautions
              pertaining to environmental conditions in the area of operation (policy on consumption
              of alcohol, narcotics and drugs, sleep aids and anti-depressants, medication and
              vaccination, fatigue, flight and duty period limitations, stress and rest, etc.).
‘5.1   General procedures valid for all operations’:
       (a)    Consideration of the following to minimise human errors:
              (1)    a clear distribution and assignment of tasks; and
              (2)    an internal checklist to check that staff are properly performing their assigned
                     tasks.
       (b)    Consideration of the deterioration of external systems supporting the UAS operation; in
              order to assist in the identification of procedures related to the deterioration of external
              systems supporting the UAS operation, it is recommended to:
              (1)    identify the external systems supporting the operation;
              (2)    describe the deterioration modes of these external systems which would prevent
                     the operator maintaining a safe operation of the UAS (e.g. complete loss of GNSS,
                     drift of the GNSS, latency issues, etc.);
              (3)    describe the means put in place to detect the deterioration modes of the external
                     systems; and
              (4)    describe the procedure(s) in place once a deterioration mode of one of the external
                     systems is detected (e.g. activation of the emergency recovery capability, switch to
                     manual control, etc.).
       (c)    Coordination between the remote pilot(s) and other personnel;
       (d)    Methods to exercise operational control; and
       (e)    Pre-flight preparation and checklists. These include, but are not limited to, the following
              points:
              (1)    The site of the operation:




Annex to ED Decision 2025/018/R                                                             Page 193 of 204
                                          AMC & GM to Regulation (EU) 2019/947
                                                 Issue 1, Amendment 3



                     (i)     the assessment of the area of operation and the surrounding area, including,
                             for example, the terrain and potential obstacles and obstructions for keeping
                             a VLOS of the UA, potential overflight of uninvolved persons, potential
                             overflight of critical infrastructure (a risk assessment of the critical
                             infrastructure should be performed in cooperation with the responsible
                             organisationfor the infrastructure, as they are most knowledgeable of the
                             threats)
                     (ii)    the assessment of the surrounding environment and airspace, including, for
                             example, the proximity of restricted zones and potential activities by other
                             airspace users;
                     (iii)   when UA VOs are used, the assessment of the compliance between visibility
                             and planned range, the potential terrain obstruction, and the potential gaps
                             between the zones covered by each of the UA VOs; and
                     (iv)    the class of airspace and other aircraft operations (local aerodromes or
                             operating sites, restrictions, permissions).
              (2)    Environmental and weather conditions:
                     (i)     environmental and weather conditions adequate to conduct the UAS
                             operation; and
                     (ii)    methods of obtaining weather forecasts.
              (3)    Coordination with third parties, if applicable (e.g. requests for additional permits
                     from various agencies and the military when operating, for example, in
                     environmentally protected areas, areas restricted to photographic flights, near
                     critical infrastructure, in urban areas, emergency situations, etc.);
              (4)    the minimum number of crew members required to perform the operation, and
                     their responsibilities;
              (5)    the required communication procedures between the personnel in charge of
                     duties essential to the UAS operation, and with external parties when needed;
              (6)    compliance with any specific requirement from the relevant authorities in the
                     intended area of operations, including those related to security, privacy, data and
                     environmental protection, use of the RF spectrum; also considering cross-border
                     operations (specific local requirements) when applicable;
              (7)    the required risk mitigations put in place to ensure the operation is safely
                     conducted (e.g. a controlled ground area, securing the controlled ground area to
                     avoid third parties entering the area during the operation, and ensuring
                     coordination with the local authorities when needed, etc.); and
              (8)    procedures to verify that the UAS is in a condition to safely conduct the intended
                     operation (e.g. update of geographical zones data for geo-awareness or geo-
                     fencing systems; definition and upload of lost link contingency automatic
                     procedures; battery status, loading and securing the payload;).
       (f)    Launch and recovery procedures;
       (g)    In-flight procedures (operating instructions for the UA (reference to or duplication of
              information from the manufacturer’s manual); instructions on how to keep the UA within
              the flight geography, how to determine the best flight route; obstacles in the area, height;
              congested environments, keeping the UA in the planned volume);



Annex to ED Decision 2025/018/R                                                             Page 194 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



       (h)    Post-flight procedures, including the inspections to verify the condition of the UAS;
       (i)    Procedures for the detection of potentially conflicting aircraft by the remote pilot and,
              when required by the UAS operator, UA VOs; and
       (j)    Dangerous goods (limitations on their nature, quantity and packaging; acceptance prior
              to loading, inspecting packages for any evidence of leakage or damage).
‘5.2   Procedures peculiar to a single operation’
       (a)    Procedures to cope with the UA leaving the desired ‘flight geography’;
       (b)    Procedures to cope with the UA entering the ‘containment’ volume;
       (c)    Procedures to cope with uninvolved persons entering the controlled ground area, if
              applicable;
       (d)    Procedures to cope with adverse operating conditions (e.g. in case icing is encountered
              during the operation, if the operation is not approved for icing conditions);
       (e)    Procedures to cope with the deterioration of external systems supporting the operation.
              In order to help properly identify the procedures related to the deterioration of external
              systems supporting the UAS operation, it is recommended to:
              (1)    identify the external systems supporting the operation;
              (2)    describe the deterioration modes of these external systems which would prevent
                     the operator maintaining a safe operation of the UAS (e.g. complete loss of GNSS,
                     drift of the GNSS, latency issues, etc.);
              (3)    describe the means put in place to detect the deterioration modes of the external
                     systems; and
              (4)    describe the procedure(s) in place once a deterioration mode of one of the external
                     systems is detected (e.g. activation of the emergency recovery capability, switch to
                     manual control, etc.).
       (f)    De-confliction scheme (i.e. the criteria that will be applied for the decision to avoid
              incoming traffic). In cases where the detection is performed by UA VOs, the phraseology
              to be used.
‘6     Emergency procedures’
       (a)    Procedures to avoid or, at least minimise, harm to third parties in the air or on the ground.
              With regard to the air risk, an avoidance strategy to minimise the collision risk with
              another airspace user (in particular, an aircraft with people on board); and
       (b)    Procedures for the emergency recovery of the UA (e.g. landing immediately, termination
              of the flight with FTS or a controlled crash/splash, etc.).
‘7.    Emergency response plan (ERP)’
       See AMC3 UAS.SPEC.030(3)(e).




Annex to ED Decision 2025/018/R                                                              Page 195 of 204
                                                 AMC & GM to Regulation (EU) 2019/947
                                                        Issue 1, Amendment 3




       AMC1 UAS.SPEC.040(1) Operational authorisation — EASA Form 209
      OPERATIONAL AUTHORISATION TEMPLATE

      The competent authority should produce the operational authorisation according to the following
      form:



                                Operational authorisation for the ‘specific’ category
                                                       Issue 2

                                        1. Authority that issues the authorisation

1.1 1 Issuing authority

1.2 Point of contact
   NameOffice
   Telephone
   Email

                                                  2. UAS operator data

2.1 UAS operator registration number

2.2 UAS operator name

2.3 Operational point of contact
   Name
   Telephone
   Email

                                                3. Authorised operation

3.1 Authorised location(s) including the lower and upper               Generic,
limits of the operational volume
                                                                   lower limit __m (__ ft), upper limit __m (__ ft)


                                                                       Precise, specify coordinates
                                                                   _______________________, lower limit __m (__ ft),
                                                                   upper limit __m (__ ft)

3.2 Extent of the adjacent area                                    ____ km

3.32 Risk assessment reference and revision                            SORA version edition date___
                                                                       PDRA # __-__ edition date___




      Annex to ED Decision 2025/018/R                                                                 Page 196 of 204
                                               AMC & GM to Regulation (EU) 2019/947
                                                      Issue 1, Amendment 3



                                                                     other _________
                                                                     SAIL I           SAIL II             SAIL III
3.43 Level of assurance and integrity
                                                                     SAIL IV          SAIL V             SAIL VI
                                                                     Other____________

3.45 Type of operation                                               VLOS        BVLOS

3.56 Transport of dangerous goods                                    Yes        No

3.6 Dropping material                                                Yes        No

3.7 Ground risk               3.7.1 Operational area                 controlled ground area                 people/km2
characterisation              (maximum population density)
                                                                     sparsely populated area                     up to 5
                                                                                                               up to 50
                                                                                                              up to 500
                                                                     populated area                         up to 5 000
                                                                                                           up to 50 000
                                                                                                     more than 50 000
                                                                     assemblies of people                       no limit

                              3.7.2 Adjacent ground area                                                    people/km2
                              (average population density)
                                                                     sparsely populated area                    up to 50
                                                                                                              up to 500
                                                                     populated area                         up to 5 000
                                                                                                           up to 50 000
                                                                     assemblies of people                        no limit

                              3.7.3 Adjacent ground area             up to 40 000 people
                              (outdoor assemblies of people
                                                                     up to 400 000 people
                              allowed within 1 km of the
                              operational volume)                    more than 400 000 people

3.8 Ground risk               3.8.1 Strategic mitigations           No           Yes, lLow          Yes, mMedium
mitigations                   M1(A) — Sheltering                 Yes, high
                                                                    No          Yes, low        Yes, mMedium         Yes,
                              3.8.2. ERP M1(B) —
                                                                 hHigh
                              Operational restrictions
                                                                     No         Low
                              3.8.3 M1(C) — Ground
                              observation
                                                                     No         Medium            High
                              3.8.4 M2 — Mitigation to
                              reduce effect of ground impact

3.9 Final ground risk class (GRC)


      Annex to ED Decision 2025/018/R                                                              Page 197 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3




3.9 Height limit of the operational volume                        _____ m (______ ft)

3.10 Residual air risk level 3.10.1 in the operational volume         ARC-a       ARC-b       ARC-c      ARC-d

3.10.2 adjacent volume                                                ARC-a       ARC-b       ARC-c      ARC-d

3.11 Air risk mitigations      3.11.1 Strategic mitigations           No          Yes
                                                                  If yes, please describe _________________

                               3.11.2 Tactical mitigation
                               methods
                                                                      Low        Medium        High        Tethered
3.12 Achieved level of containment
                                                                      Basic       Enhanced

3.13 What is the minimum RP:UA ratio allowed between RP:UA ___:____
     the remote pilot (RP) and the UA that may be
     operated simultaneously?

3.143 Remote pilot competency

3.154 Competency of staff, other than the remote pilot,
essential for the safety of the operation

3.165 Type of events to be reported to the competent
authority (in addition to those required by Regulation (EU)
No 376/2014)

3.176 Insurance                                                       No        Yes

3.17 Operations manual references

3.18 Compliance evidence matrix file reference

3.19 Remarks / additional limitations

                                               4. Data of authorised UAS

4.1 Manufacturer                                                  4.2 Model name
                                                                  (optional)
Design organisation
name (optional)

4.3 Type of UAS               Aeroplane Fixed-wing              4.4 Maximum UA               _____ m
                                                                characteristic
                                  Rotorcraft-helicopter       –
                                                                dimensions
                          Helicopter
                              Rotorcraft-gyroplane
                               VTOL-capable UA (including
                               multirotors)




       Annex to ED Decision 2025/018/R                                                            Page 198 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3



                              Lighter than air/other

4.5 Take-off mass         _____ kg                                4.6 Maximum                _____ m/s (_____ kt)
(optional)                                                        operational speed

4.7 Type of C2 link

4.8 Size of the adjacent ground area                              ____ km

4.97 Additional technical requirements

4.108 Serial number or, if applicable, UA registration mark
(optional)

4.119 Number of type certificate (TC) or design verification
report (DVR), number and issue date if required (optional)

4.120 Number of the certificate of airworthiness (CofA), if
required (optional)

4.131 Number of the noise certificate, if required (optional)

4.14 E-conspicuity system                                             Direct remote ID       Network remote ID
                                                                      SRD-860 in             SRD-860 out
                                                                      ADS-B In         ADS-B Out        Other ________

4.12 Mitigation to reduce effect of ground impact                    No           Yes, low         Yes, medium        Yes,
                                                                  high
                                                                  Required to reduce the ground risk       No         Yes,

4.13 Technical requirements for containment                           Basic      Enhanced

                                                       5. Remarks




                                             6. Operational authorisation

[insert UAS operator name] is authorised to conduct UAS operations with the UAS(s) defined in
Section 4 and according to the conditions and limitations defined in Section 3, for as long as it complies
with this operational authorisation, with Implementing Regulation (EU) 2019/947, and with any
applicable Union and national regulations related to privacy, data protection, liability, insurance,
security, and environmental protection.
Any flight outside [insert Member State name] must comply with all the requirements defined in this operational
authorisation and is subject to validation by the competent authority of the Member State where the operation is
intended to be performed, in accordance with Article 13 of Implementing Regulation (EU) 2019/947. The conditions


       Annex to ED Decision 2025/018/R                                                              Page 199 of 204
                                                AMC & GM to Regulation (EU) 2019/947
                                                       Issue 1, Amendment 3



specified in this operational authorisation shall be supplemented, where necessary, by proof of compliance with the
local conditions published by the Member State where the operation is intended to be performed and the
implementation of mitigations to address risks specific to the airspace, terrain, population and climatic conditions
of the flight area.

6.1 Operational authorisation number

6.2 Valid from                   DD/MM/YYYY                       6.32 Expiry date             DD/MM/YYYY

Date                                                              Signature and stamp
DD/MM/YYYY
EASA Form 209
       Instructions for filling in the operational authorisation form
       1.1    Name of the competent authority that issues the operational authorisation, including the name
              of the State.
       1.2    Contact details of the competent authority’s office responsible for the file.
       2.1    UAS operator’s registration number in accordance with Article 14 of the UAS Regulation.
       2.2    UAS operator’s name, as registered in the UAS operator’s registration database. This is an
              optional field as the information may be retrieved from the UAS operator’s registration.
       2.3    Contact details of the person responsible for the UAS operation, in charge to answer possible
              operational questions raised by the competent authority.
       3.1    Location(s) where the UAS operator is authorised to operate. It should include the maximum
              flight altitude, expressed in metres and feet in parentheses, of the approved operational volume
              using the AGL reference when the upper limit is below 150 m (492 ft), or use the MSL reference
              when the upper limit is above 150 m (492 ft).
              The identification of the location(s) should contain the full operational volume and ground risk
              buffer (the red line in Figure 21). Depending on the initial ground and air risk classification
              determined using the SORA process and on the application of mitigations measures, the
              location(s) may be ‘generic’ or ‘precise’ (refer to GM2 UAS.SPEC.030(2)). When the UAS
              operation is conducted in a Member State other than the State of registration, the competent
              authority of the Member State of registration should specify the location(s) only after receiving
              confirmation from the State of operation, according to Article 13 of the UAS Regulation.
              In case of ‘precise’ locations, the information may be provided in a separate file listing all
              authorised locations using a file format to display geographic data (e.g. kml, Json, etc..).


                                                Ground risk buffer
                        Adjacent area           Operational area               Adjacent area



                                 Figure 21 — Operational area and ground risk buffer


       3.2    Provide the maximum distance in km to be considered for the adjacent area, starting from the
              limits of the ground risk buffer.


       Annex to ED Decision 2025/018/R                                                             Page 200 of 204
                                        AMC & GM to Regulation (EU) 2019/947
                                               Issue 1, Amendment 3



3.23 Select one of the three options. If the SORA is used, indicate the edition date as defined in
     AMC1 Article 11. In case a PDRA is used, indicate the number and its edition date as defined in
     the applicable AMC to Article 11. In case a risk assessment methodology is used other than the
     SORA, provide its reference. In this last case, the UAS operator should demonstrate that the
     methodology complies with Article 11 of the UAS Regulation.
3.34 If the risk methodology used is the SORA, indicate the final SAIL of the operation, otherwise
     select ‘other’ and provide the equivalent information provided by the risk assessment
     methodology used.
3.5    Select one of the two options.
3.6    Select one of the two options.
3.7    If a qualitative measurement of the population density is used, then select one of the qualitative
       descriptors, otherwise check one of the descriptors linked to the maximum population density
       allowed.
3.8.1 Select one of the four options. In case the risk assessment is based on the SORA, this consists in
      M1 mitigation.
3.8.2 Select one of the four options. In case the risk assessment is based on the SORA, this consists in
      M3 mitigation.
3.9    Insert the maximum flight altitude, expressed in metres and feet in parentheses, of the
       approved operational volume (adding the air risk buffer, if applicable) using the AGL reference
       when the upper limit is below 150 m (492 ft), or use the MSL reference when the upper limit is
       above 150 m (492 ft). If the SORA has been used, indicate the final risk class achieved after the
       application of the ground mitigations. If another risk assessment methodology has been used,
       indicate the equivalent information.
3.10 Select one of the four options.
3.11.1 Select one of the two options.
3.11.2Describe the air risk tactical mitigation methods to be applied by the UAS operator (e.g. employ
      airspace observer(s) or UA observer(s), etc.).
3.12 Select one of the two options.
3.13 If the UAS flight manual provided by the UAS designer indicates that it is designed with a level
     of automation that reduces the remote pilot’s workload allowing one remote pilot (RP) to
     control multiple UA simultaneously, then specify the number of UA that one remote pilot is
     permitted to control (e.g. in case one RP is able to control simultaneously five UA, indicate
     ‘RP:UA 1:5’). This number should not exceed the limit defined in the UAS flight manual.
     Additionally, the UAS operator may decide to have a pool of remote pilots controlling multiple
     UA simultaneously. In this case, clear procedures should be developed to define who is the pilot-
     in-command, responsible during each phase of flight (e.g. in case three RPs are permitted to
     control simultaneously ten UA, indicate ‘RP:UA 3:10’).
3.134 Specify the competency or the type of the remote pilot certificate, if required; otherwise,
      indicate ‘Declared’.
3.145 Specify the competency or the type of the certificate for the staff, other than the remote pilot,
      essential for the safety of the operation, if required; otherwise, indicate ‘Declared’.
3.156 List the type of events that the UAS operator should report to the competent authority, in
      addition to those required by Regulation (EU) No 376/2014, if applicable.
3.16 Select one of the two options.


Annex to ED Decision 2025/018/R                                                            Page 201 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



3.17 Indicate the OM’s identification and revision number.
3.18 Indicate the compliance evidence matrix file identification and revision number (e.g. the
     compliance matrix defined in Chapter A4 of Annex A to AMC1 Article 11 (SORA).
3.19 Additional limitations defined by Free-text field where the competent authority may provide
     any additional relevant information.
Section 4. Only the UAS features/characteristics required to be used for the operation should be
      identified in the form (e.g. in case the UAS qualifies for enhanced containment but the operation
      requires a basic containment, and the operator developed consistent procedures, then the basic
      containment should be ticked) This section may be replicated for all authorised UAS models to
      be used under this operational authorisation.
4.1    Name of the organisation designing the UAS. This field is optional.
4.2    Model of the UAS as defined by the design organisation in the UAS flight manual. This field is
       optional.
4.3    Select one of the five options. Fixed-wing UA includes configurations such as aeroplanes, kites,
       gliders, etc.
       Rotorcraft-helicopter UA includes all vertical-lift configurations having up to 2 rotors.
       Rotorcraft-gyroplane UA is a special configuration with unpowered rotor.
       VTOL-capable aircraft (VCA), including rotorcraft, includes vertical-lift configurations with 3 or
       more rotors and fixed-wing UA capable of vertically taking off and landing.
       Lighter-than-air configurations include configurations such as airships, hot-air balloons, etc.
4.4    Indicate the maximum dimensions of the UA in metres (refer to definition I.141 ‘UA
       characteristic dimension’ in Annex I to AMC1 Article 11 (SORA)). e.g. for aeroplanes: the length
       of the wingspan; for helicopters: the diameter of the propellers; for multirotors: the maximum
       distance between the tips of two opposite propellers) as used in the risk assessment to identify
       the ground risk.
4.5    Indicate the maximum value, expressed in kg, of the UA take-off mass (TOM), expressed in kg,
       at which the UAS operation may be operated. All flights should then be conducted without
       operated not exceeding that the specified TOM. The TOM may be different from (however, not
       exceeding higher than) the MTOM defined by the UAS manufacturerdesign organisation in the
       UAS flight manual. This field is optional.
4.6    Maximum operational cruise airspeed, expressed in m/s and kt in parentheses, that the UA will
       not exceed during the operation. This should always be lower than the maximum speed defined
       in the UAS flight manual manufacturer’s instructions.
4.7    Indicate the type of C2 link to be used during the operation (e.g. radio link, LTE/5G, satellite,
       etc.).
4.8    Provide the size in km to be considered for the adjacent ground area, starting from the limits of
       the ground risk buffer using the instructions defined in Section S.4.8.4 of AMC1 Article 11
       (SORA).
4.79 List any additional technical requirements established by the competent authority.
4.810 This field is mandatory in case the UA is registered according to Article 14(7) of Implementing
      Regulation (EU) 2019/947. If the UA is not registered, the NAA may indicate the Uunique serial
      number (SN) of the UA defined by the manufacturer design organisation according to standard
      ANSI/CTA-2063-A-2019, Small Unmanned Aerial Systems Serial Numbers, 2019, or the UA



Annex to ED Decision 2025/018/R                                                             Page 202 of 204
                                         AMC & GM to Regulation (EU) 2019/947
                                                Issue 1, Amendment 3



       registration mark if the UA is registered. In case of privately built UAS or UAS not equipped with
       a unique SN, insert the unique SN of the remote identification system. For UAS operations
       classified in SAIL V or higher, the serial numbers of all UAS should be provided and any change
       to them would require a prior approval from the competent authority. For UAS operations
       classified up to SAIL IV, a change to the serial number does not require prior approval from the
       competent authority.
4.11 Include the EASA TC number, or the UAS design verification report (DVR) number issued by
     EASA, asif required by the competent authority.
4.9    Include the EASA TC number, or the UAS design verification report number issued by EASA, as
       required by the competent authority.
4.102 If a UAS with an EASA TC is required, the UAS should have a certificate of airworthiness (CofA),
      and the competent authority should require compliance with the continuing airworthiness
      rules.
4.113 If a UAS with an EASA TC is required, the UAS should have a noise certificate.
4.12 Select one of the four options of the first row. In case the risk assessment is based on the SORA,
      this consists in M2 mitigation. Even if the UAS may be equipped with such system, this
      mitigation may not be required in the operation to reduce the ground risk. In this case, in the
      second row select ‘NO’. If the mitigation is instead used to reduce the ground risk, select ‘YES’
      and the operator is required to include in the OM the related procedures.
4.13 Select one of the two options.
4.14 Multiple options are possible.
5      Free-text for the addition of any relevant remark.
6.1    Reference number of the operational authorisation, as issued by the competent authority. The
       number should have the following format:
       NNN-OAT-xxxxx/yyy
       Where:
       —      ‘NNN’ is the ISO 3166 Alpha-3 code of the Member State that issues the operational
              authorisation;
       —      ‘OAT’ is a fixed field meaning ‘operational authorisation’;
       —      ‘xxxxx’ are up to 12 alphanumeric characters defining the operational authorisation
              number; and
       —      ‘yyy’ are 3 alphanumeric characters defining the revision number of the operational
              authorisation;
       each amendment of the operational authorisation will determine a new revision number.
6.2 The duration of the operational authorisation may be unlimited; in this case, indicate ‘Unlimited’.
     The authorisation will be valid for as long as the UAS operator complies with the relevant
     requirements of the UAS Regulation and with the conditions defined in the operational
     authorisation.
Note 1: In section 4, more than one UAS may be listed. If needed, the fields may be duplicated.
Note 2: The signature and stamp may be provided in electronic form. The quick response (QR) code in
      section 6 should provide the link to the national database where the operational authorisation
      is stored.



Annex to ED Decision 2025/018/R                                                            Page 203 of 204
                                  AMC & GM to Regulation (EU) 2019/947
                                         Issue 1, Amendment 3




Annex to ED Decision 2025/018/R                                          Page 204 of 204
