Material characterization of a
flax fiber reinforced composite for
crashworthiness applications

Tesi di Laurea Magistrale in
Aeronautical Engineering - Ingegneria Aeronautica


Author:
Elia Pinato




Student ID: 944474
Advisor: Prof. Marco Anghileri
Co-advisors: Ing. Ivan Colamartino
Academic Year: 2021-2022
                                                                                            i




Ringraziamenti
Con queste poche righe vorrei ringraziare tutte le persone che mi hanno sostenuto ed
aiutato lungo questo percorso.

Ringrazio il Professor Anghileri per avermi concesso l’opportunità di lavorare su un ar-
gomento così innovativo e stimolante. Un grazie speciale va a Impregnatex Compositi, la
quale mi ha fornito tutto il materiale e il supporto di cui avevo bisogno. In particolare,
sono grato all’Ing. Torno per avermi concesso questa occasione, all’Ing. Cavasin e al
Dott. Tagliabue per avermi sostenuto in tutte le fasi del lavoro, fornendomi consigli indis-
pensabili e ottimi spunti. Ringrazio tutto il Laboratorio Prove Sperimentali per avermi
fornito gli strumenti per l’esecuzione delle prove, in particolare sono grato all’Ing. Rubini
per la sua incredibile disponibilità e pazienza. Ringrazio tutto il personale del laboratorio
LaST, grazie all’Ing. Scampini per il supporto tecnico e ringrazio l’Ing. Colamartino
per avermi dato sempre ottimi suggerimenti, buonumore e guidandomi nell’ultima fase di
questo percorso.

Ci tengo a ringraziare anche tutti i colleghi ingegneri e tesisti del LaST che hanno con-
tribuito ad alleggerire le dure giornate di lavoro e scrittura.

Un grazie enorme va a tutti i miei più cari amici che mi hanno accompagnato in questo
percorso universitario, dandomi gioia e serenità anche nei momenti meno felici.

Ultima, ma certamente non per importanza, ringrazio la mia famiglia che mi è sempre
stata vicina e mi ha sempre sostenuto in questo lungo percorso.

Grazie di cuore a tutti voi!
                                                                                          iii




Abstract
Natural fiber composites might represent an environmentally sustainable alternative to
conventional solutions such as fiberglass and carbon fiber composites. The aim of this
work is to perform a material characterization of flax-fiber reinforced composite material,
so as to investigate both the static and dynamic mechanical performances for possible
future crashworthiness applications.

The specimens employed during experimental tests are composed by ampliTex™ 300 twill
2/2 fibers and IMP 503ZHT BC epoxy resin. Although a fabric material was considered,
static tests were performed in order to examine the properties in both warp direction at
0° and weft direction at 90°. In detail, tensile, compressive, flexural and shear properties
were achieved from static tests, while indentation, ballistic impact and tensile dynamic
responses were analyzed to probe the crashworthiness features.

In order to produce a representative numerical model of flax composite material, numerical
activity was performed through the use of LS-DYNA software. The choice of suitable
numerical elements and material card was accomplished so as to approximate both the
mechanical performances and behaviour of the material.

Eventually, a wide discussion about the results, further improvements and the future
development of bio-composites was performed.
Sommario
I materiali compositi costituiti da fibra di origine naturale possono rappresentare una
alternativa ecosostenibile rispetto alle soluzioni attualmente offerte dal mercato, come
compositi in fibra di vetro e fibra di carbonio. Lo scopo di questa tesi è quello di eseguire
una campagna di test su un materiale in fibra di lino, al fine di analizzarne le sue caratter-
istiche meccaniche, sia a livello statico che dinamico, valutando possibili utilizzi in campo
crashworthiness.

I provini in composito utilizzati durante le prove sperimentali sono costituiti da fibre di lino
ampliTex™ 300 twill 2/2 e resina epossidica IMP 503ZHT BC. Sebbene il materiale testato
sia un tessuto, sono state eseguite prove indagando sia le prestazioni lungo la direzione
0° (ordito) che quelle lungo la direzione 90° (trama). Più in dettaglio, le proprietà di
trazione, compressione, flessione e taglio sono state ottenute durante le prove statiche,
mentre le proprietà dinamiche di indentazione, trazione e la risposta dinamica ad impatti
ad alta velocità sono state analizzate al fine di approfondire le caratteristiche di resistenza
agli urti.

Un modello numerico del materiale è stato realizzato mediante l’utilizzo del software
LS-DYNA, allo scopo di effettuare una indagine preliminare valutando le scelte di model-
lazione più idonee. In particolare, la scelta del tipo di elementi numerici, insieme alla
scelta della scheda del materiale, sono state eseguite in modo da approssimare al meglio
sia le prestazioni meccaniche che il comportamento del materiale durante i fenomeni di
deformazione.

I risultati sono stati discussi ampiamente, riportando anche i possibili miglioramenti at-
tuabili al fine di migliorare le procedure di test. Infine, i possibili sviluppi futuri relativi
ai materiali bio-compositi sono stati riportati.
                                                                                          vii




Contents

Ringraziamenti                                                                              i

Abstract                                                                                  iii

Sommario                                                                                   v

Contents                                                                                  vii



1 Introduction                                                                             1

2 Literature review                                                                        3
  2.1 General overview composite materials . . . . . . . . . . . . . . . . . . . . .       3
       2.1.1 Fibrous composite materials . . . . . . . . . . . . . . . . . . . . . .       4
       2.1.2 Rule of mixture . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     7
       2.1.3 Constitutive law . . . . . . . . . . . . . . . . . . . . . . . . . . . .      8
       2.1.4 Plane-stress case . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
       2.1.5 Classical Lamination Theory . . . . . . . . . . . . . . . . . . . . . .      12
       2.1.6 Failure modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    15
  2.2 Composites manufacturing techniques . . . . . . . . . . . . . . . . . . . . .       19
       2.2.1 Spray lay-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   20
       2.2.2 Hand lay-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    20
       2.2.3 Filament winding . . . . . . . . . . . . . . . . . . . . . . . . . . . .     21
       2.2.4 Pultrusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   22
       2.2.5 Resin Transfer Moulding (RTM) . . . . . . . . . . . . . . . . . . . .        23
       2.2.6 Resin Infusion under Flexible Tool (RIFT) . . . . . . . . . . . . . .        24
       2.2.7 Compression moulding . . . . . . . . . . . . . . . . . . . . . . . . .       25
       2.2.8 Prepreg - Autoclave . . . . . . . . . . . . . . . . . . . . . . . . . . .    27
       2.2.9 Additive manufacturing . . . . . . . . . . . . . . . . . . . . . . . .       28
  2.3 Experimental testing phase . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
viii                                                                             | Contents


       2.4   Numerical modeling phase . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
             2.4.1 Material cards overview . . . . . . . . . . . . . . . . . . . . . . . . 31
             2.4.2 *MAT_058 material model . . . . . . . . . . . . . . . . . . . . . . 33

3 Natural composite materials                                                              39
  3.1 Reasons to study them . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      41
  3.2 How they are manufactured . . . . . . . . . . . . . . . . . . . . . . . . . .        44
  3.3 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   48
  3.4 Material selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   51

4 Material Characterization                                                                 57
  4.1 Samples manufacturing . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       57
  4.2 Static tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    62
      4.2.1 Testing equipment . . . . . . . . . . . . . . . . . . . . . . . . . . .         63
      4.2.2 Tensile test D3039 . . . . . . . . . . . . . . . . . . . . . . . . . . .        64
      4.2.3 Shear test D3518 . . . . . . . . . . . . . . . . . . . . . . . . . . . .        71
      4.2.4 Bending test D790 . . . . . . . . . . . . . . . . . . . . . . . . . . .         74
      4.2.5 Compression test D6641 . . . . . . . . . . . . . . . . . . . . . . . .          77
  4.3 Dynamic tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     80
      4.3.1 Strain rate sensitivity test . . . . . . . . . . . . . . . . . . . . . . .      82
      4.3.2 Indentation test D7136 . . . . . . . . . . . . . . . . . . . . . . . . .        87
      4.3.3 High-velocity impact test . . . . . . . . . . . . . . . . . . . . . . . .       93

5 Numerical simulation                                                                    97
  5.1 Model set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
  5.2 Tensile test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
  5.3 Shear test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
  5.4 Compression test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
  5.5 Bending test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

6 Conclusions and future developments                                                 107
  6.1 Future developments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108



Bibliography                                                                               111



A Appendix A                                                                               115
   A.1 Static tests specimens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
   A.2 Dynamic tests specimens . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

List of Figures                                                                       135

List of Tables                                                                        139
                                                                                         1




1 | Introduction
This thesis work aims to study innovative composite materials compared to the current
solutions offered by the market. Since environmental issue are more and more significant
nowadays, an alternative sustainable solution must be found. Green composite materials
have great potentiality in this sector, and it would be interesting to examine in depth the
mechanical features of these products.

The project here presented will focus on the applicability of these innovative materials
in the context of energy absorption applications. Due to the lack of data in literature,
material characterization activity is required so as to gather the most relevant mechanical
features of flax-fiber reinforced composite, which represents the employed material. An-
geloni Group kindly offered his facilities, support and raw materials, such natural fibers
and resins, in order to achieve the needed specimens to perform both the material char-
acterization and dynamic tests.

The first stage of this work concerns the literature review, in which a general overview
about composite materials will be performed. In detail, composite characteristics and
classification will be presented with an in-depth analysis about the most used composite
manufacturing techniques. Moreover, an introduction to both experimental and numerical
phases will be provided, so as to offer all the information about the procedures and tools
employed.

A preliminary study concerning natural composite materials will be conducted. In par-
ticular, an overview and classification of these bio-composite materials will be analysed.
Advantages and drawbacks are presented as well as the current applications of these prod-
ucts. In addition, in order to fully exploit the potential of natural composite materials,
manufacturing processes and chemical treatments will be examined. The latter are fun-
damental also to select the proper fabrication technique so as to produce the required
specimens for test phase. Eventually, the selection of flax composite material will be
investigated through the analysis of the most common fibers and resins available on the
market.

Material characterization test phase will be performed, In according to the ASTM stan-
2                                                                         1| Introduction


dards, so as to gain the characteristics of the material in the most significant loading
condition. Numerical simulations will be performed as well, LS-DYNA will be employed
to simulate tests and the most representative results will be obtained exploiting a trial
and error methodology. Dynamic properties will be investigated throughout experimental
tests in order to probe the energy absorption characteristics with respect to the traditional
solutions.

In conclusion, the data and the observations gathered in these pages want to be a solid
base for further investigations and analyses.
                                                                                          3




2 | Literature review
In this chapter a definition and classification of composite materials will be presented.
Through the dissertation of hypotheses and assumptions, the mathematical tools will
be defined, in order to properly describe the behaviour of composites under different
loading conditions. Moreover, the most popular fabrication techniques are examined to
understand the correlated features. Eventually, an introduction to both experimental and
numerical phases will presented to introduce all the required tools.


2.1.      General overview composite materials
Composite materials have been always used by humans since ancient times. Civilizations
exploit composites characteristics through the centuries, for example, Israelites used straw
to reinforce the mud-bricks and the ancient Egyptians rearranged different types of wood
in order to produce plywood, a natural material with better thermal expansion resistance
and less tendency to swell due to the presence of moisture. Even in the Middle Age
composites were used to fabricate swords and armors since they were made with different
layers of metals.




                   Figure 2.1: Straw reinforced mud-brick production
4                                                                    2| Literature review


composite materials by definition are two or more materials combined on a macroscopic
scale to form a useful third material with specific feature and properties. From a macro-
scopic point of view the constituents can be identified by the naked eyes and an interface
between them can be observed as well [14].

Classification of composite materials can be done and four commonly accepted types are
here presented:

    1. Fibrous composite materials consist in fibers in a matrix. The fiber’s section can be
       very small on the order of micrometer. Thanks to this characteristic the amount
       of flaws can be reduced to the minimum, increasing the overall mechanical perfor-
       mances. On the other hand the matrix has poor mechanical characteristics but
       is fundamental to transfer the load inside the material. The most used fibers are
       E-glass, S-glass, carbon, beryllium, boron and graphite.

    2. Laminated composite materials consist of layers of at least two different materials
       that are bonded together. Lamination is used to combine the best aspects of the
       constituent layers and bonding material in order to achieve better characteristic such
       as strength, stiffness, corrosion resistance, thermal insulation ect. Both sandwich
       and honeycomb composites are well known examples of this kind of composite.

    3. Particulate composite materials are composed of particles of one or more materials
       suspended in a matrix of another material. The particles can be either metallic
       or nonmetallic as can the matrix. An example is represented by the solid rocket
       propellants.

    4. Combinations of some or all of the first three types.

Amplitex is the material used in this study, is composed by flax fibers and epoxy resin,
which is a polymeric matrix material. It is convenient to focus on fibrous materials since
they are the most relevant for our purpose.


2.1.1.     Fibrous composite materials
As mentioned before, fibers and matrix compose fibrous composites. Fibers have a length
much greater than its diameter, the aspect ratio (length-to-diameter) can be very large.
The reinforcing phase provides the strength and stiffness and is harder, stronger, and
stiffer than the matrix.

Fibers can be classified in two different typology:

    • Continuous fiber has greater aspect ratio and a preferred orientation can be iden-
2| Literature review                                                                   5


     tified. The mechanical characteristics are greater with respect to the discontinued
     one but only in the main direction.

   • Discontinued fiber exhibits lower aspect ratio and they are organized randomly
     inside the composite. Strength and stiffness are lower but the cost can be decreased
     compared to the previous solution.




                     Figure 2.2: Continuous vs discontinuous fibers


Long fibers can be organized in different ways and create different kind of layers. Uni-
directional fibers (UD) are formed by fibers aligned in the same direction. This allow to
maximize the performances in the main direction while maintain poor characteristics in
the others.




                 Figure 2.3: Unbounded view of laminate construction
6                                                                   2| Literature review


In order to gain isotropy UD layers with different orientations can be used to form laminate
so as to gain independence between mechanical properties and orientation of fibers.

Another layout that can be exploited to achieve different mechanical properties is the
woven fabric. The latter is produced by the interlacing of wrap (0°) fibers and weft (90°)
fibers in a regular pattern or weave style. Complex geometry can be modelled and different
fibers can be mixed together (i.e. carbon and kevlar). This material is orthotropic and
remarkable mechanical properties can be achieved since the integrity is maintained by the
mechanical interlocking of the fibers.




                      Figure 2.4: Unidirectional and woven laminae


The purpose of the matrix is to bond together all the components and contribute to form
a structural element that can carry loads. The mechanical properties of this component
are poor compared to the fiber ones but despite this, they cover a vital role. Matrix
offers support for fibers, protection against corrosion and mechanical damages, stresses
are carry mainly by the fibers but matrix has the capability to transfer loads from fiber
to fiber. Even more in case of broken fiber its role is essential, the stress is transferred
towards healthy fibers, by preventing the fail of the entire structure.

All the matrices can be classified in three typology:

    • Polymeric

    • Metallic

    • Ceramic

The polymeric matrices are widely used since they allow to achieve components with
different size and shape. They can be divided in thermoset and thermoplastic. Metallic
matrices are rarely used due to the production issues and the high cost, the most relevant
2| Literature review                                                                       7


are aluminium alloy and titanium. Same as above for the ceramic, they are used as
thermal insulation and for electrical insulation too.

It is worth noting that composite materials nowadays are generally anisotropic, which
means that in different directions are observed different behaviour. Orthotropic is a special
case of anisotropy, three mutually perpendicular planes of elastic symmetry have to be
identified. By specific manufacturing process is possible to obtain orthotropic composites
in order to exploit the best mechanical properties of these materials.


2.1.2.     Rule of mixture
Focusing on fibrous composite materials with polymeric matrix we can see clearly that
resin and reinforcing fibers exhibit different properties, the resulting composite material
will combine these properties, as shows in the figure 2.5.




                   Figure 2.5: Fiber and matrix mechanical properties


Overall, the properties of the resulting composite are determined by [12]:

  1. The properties of the fiber

  2. The properties of the resin

  3. The ratio of fibre to resin in the composite (Fiber Volume Fraction)

  4. The geometry and orientation of the fibres in the composite

The ratio of the fiber to resin is related to the manufacturing process and it is also influ-
enced by the type of resin system used, and the form in which the fibres are incorporated.
8                                                                          2| Literature review


This is an important aspect since an higher fiber volume fraction improves the mechanical
properties of the composite. An upper limit is given by technological issue, the fibers need
to be fully coated in resin to be effective and capable to transfer the loads. In most of the
case a limit for FVF is approximately 30-40 % but with more sophisticated and precise
processes FVF close to 70 % can be successfully obtained.

By approximating the composite as an homogeneous, isotropic material the resulting
mechanical properties can be estimated by means of rule of mixture:


                         ρcomp Vcomp = ρf iber Vf iber + ρmatrix Vmatrix                  (2.1)

The equation (2.1) is based on the contribution of each part of the composite, in particular
it consists in a weighted average over the volume fraction of the starting properties (i.e.
Young modulus, Poisson’s ratio, density etc.). This equation can be easily understood by
considering the analogy of calculating the stiffness of two springs connected in parallel.




                    Figure 2.6: RoM model for longitudinal properties



2.1.3.     Constitutive law
In order to define constitutive law for orthotropic composite materials it is fundamental
to introduce the generalized Hooke’s law written in Voigt notation:


                                σi = Cij ϵj      i, j = 1, ..., 6                         (2.2)

Where σi are the stress components shown on a three-dimensional cube (see figure 2.7),
in x, y, and z coordinates, Cij is the stiffness matrix, and ϵj are the strain components.
2| Literature review                                                                        9




                           Figure 2.7: Stress state on a element


The stiffness matrix has 36 constants, but they can be reduced if a linear elastic anisotropic
material is considered, in this case the matrix become symmetric and only 21 constants
have to be evaluated. Moreover, if two orthogonal planes of material property symmetry
exist for a material, symmetry will exist with respect to a third mutually orthogonal
plane, in this case orthotropic material are considered and the constants to be evaluated
in the stiffness matrix reduce to 9.

It is possible to express the constitutive law as a function of the stresses rather than
strains, by defining the compliance matrix which is the inverse of the stiffness matrix.


                                ϵi = Sij σj     i, j = 1, ..., 6                         (2.3)

All the simplifications performed on the stiffness matrix can be considered for the com-
pliance matrix as well, and only 9 constants have to be defined.

The composite materials are heterogeneous by their very nature, hence assumptions are
needed in order to describe properly their behaviour. Macroscopically the material can
be treated as homogeneous since the scale of the reinforcement is small. In addition,
composites show a linear elastic behaviour approximately until brittle failure, with these
characteristics it is possible to use a Hooke’s law to define the relationship between strain
and stress.

Here is reported the constitutive law for an orthotropic material in compliant form:
10                                                                       2| Literature review


                            1       ν21    ν31                          
                                   −      −          0      0        0
                    E1            E2     E3                        
                   ϵ        ν12     1      ν32                       σ 
                     1                                                  1
                           − E           −          0      0     0 
                 
                      
                          
                                                                    
                 
                  ϵ
                       
                                1  E2      E3                         σ
                                                                              
                                                                              
                 
                    2 
                          
                              ν      ν      1
                                                                       
                                                                           2 
                                                                              
                                13     23
                        −        −
                                                                         
                 
                 ϵ                                 0      0     0  σ 
                                                                             
                         =  E1      E2    E3
                     3                                                      3
                                                                                        (2.4)
                                                                    
                   γ                                 1               
                                                                       τ23 
                    23     0       0      0               0     0 
                 
                         
                                                                      
                                                    G23
                 
                      
                                                                             
                  γ31 
                                                                   τ    
                 
                      
                                                          1           31 
                                                                              
                            0       0      0        0            0  
                 
                                                                      
                 γ                                                
                                                                         τ
                                                                              
                                                           G31
                                                                              
                    12                                                     12
                                                                 1  
                              0      0      0        0      0
                                                                 G12

Where:

     • ϵ is the normal strain

     • γ is the shear strain

     • E is the Young’s modulus or modulus of elasticity

     • ν is the Poisson’s ratio, which is defined as νij = −ϵj /ϵi

     • G is the shear modulus

     • σ is the normal stress

     • τ is the shear stress




                            Figure 2.8: Lamina coordinate system


As mentioned above, a three-dimensional Cartesian coordinate system is considered (see
figure 2.8) and the subscripts 1,2,3 are respectively refer to the longitudinal direction
(parallel to the fibers direction), transverse direction which lie on the plane of the lamina
2| Literature review                                                                     11


and it is perpendicular to the longitudinal one, and lastly the third direction is referred
to the out-of-plane direction and is defined following the right-hand rule.

It worth noting that the compliance matrix is symmetric and the constants to be deter-
mined are 9. As a matter of fact, the following equality must hold:


                                     ν21 /E2 = ν12 /E1                                 (2.5)
                                     ν31 /E3 = ν13 /E1                                 (2.6)
                                     ν32 /E3 = ν23 /E2                                 (2.7)


2.1.4.    Plane-stress case
For the purpose of analyzing orthotropic composite materials, the previous constitutive
law presented in the section 2.1.3 can be simplified by considering appropriate assump-
tions. Since the lamina cannot withstand high stresses in any direction other than that
of fibers and, usually, in-plane stresses are the only one considered, it is convenient to
assume stresses with a component in direction 3 equal to zero.

This observation means that the plane stress state is defined by setting [14]:


                         σ3 = 0           τ23 = 0            τ31 = 0                   (2.8)

so that
                          σ1 ̸= 0         σ2 ̸= 0         τ12 ̸= 0                     (2.9)

This model is particularly suitable for thin materials as laminates, since negligible thick-
ness with respect to the other two dimensions is required to apply it.

The constitutive law become:
                                                        
                                    1    ν21
                                     −              0  
                          ϵ1   Eν1   E2                 σ1 
                                
                                         1                    
                                  12
                           ϵ2 = −                    0  σ2                         (2.10)
                                                         
                         
                                E1  E2                
                           γ12                        1  τ12
                                                               
                                    0    0
                                                     G12

It worth noting that the equation (2.4) is reduced to (2.10) by considering the zero-stress
components. However, is important to highlight that the corresponding strains (ϵ3 , γ23
and γ31 ) are generally different from zero.
12                                                                  2| Literature review


2.1.5.     Classical Lamination Theory
As mentioned in 2.1.1, the interest of this study is to investigate natural fibrous composite
materials. Generally these materials are organized in typical structure called laminate,
different layers, or laminae, or plies of material are stacked together in order to obtain
the final product. This process allow the designers to optimize the orientation of each
lamina with regard to the different behaviour or response needed by the laminate, thus,
the feasibility can be maximised in every sectors of interest.

Classical lamination theory (CLT) is here presented to predict the behaviour of the whole
laminate starting from the geometry and properties of each lamina. Reasonable and accu-
rate assumptions have to be performed so as to move from a three-dimensional elasticity
case towards a two-dimensional solvable one.

Here are presented the assumptions needed to apply the CLT:

     • Each ply is considered homogeneous, orthotropic and linear-elastic

     • Plane-stress condition is always considered, both for laminate and lamina

     • The laminae are perfectly bounded together and the bonds are presumed to be
       infinitesimally thin as well as non shear-deformable

     • Plane section normal to the middle surface, is assumed to remain straight and
       perpendicular to the middle surface when the laminate is deformed (Kirchhoff hy-
       pothesis)




                  Figure 2.9: Positive rotation of principal material axes
2| Literature review                                                                     13


In the section 2.1.3 the constitutive law was presented in principal material coordinates
for an orthotropic material. However, in most cases would be useful to describe such a
relation in general coordinates, this step is fundamental to properly apply the CLT. In
order to describe the lamina properties, which are defined in material axes (1,2), in the
laminate coordinate system (x,y), it is convenient to define the transformation matrix [T ]:

                                                    
                                       m2 n2  2mn
                              [T ] =  n2 m2 −2mn                                   (2.11)
                                                    

                                      −mn mn m2 − n2

With:
                               m = cosθ            n = senθ                          (2.12)

The purpose of the above mentioned matrix is to perform a rotation between the lamina
axes and laminate axes. In particular, as reported in figure 2.9, θ can be defined as
the angle from the x-axis (general coordinate system) to the 1-axis (material coordinate
system).

Stress can be written as:                          
                                   σ
                                    x             σ1 
                                                         
                                    σy    = [T ] −1
                                                      σ2                             (2.13)
                                  
                                                  
                                                     
                                    τxy               τ12
                                                         


as well as strain:                                      
                                  ϵ
                                x                  ϵ
                                                    1    
                                   ϵy    = [T ] −1
                                                       ϵ2                            (2.14)
                                                        
                                 γxy /2              γ12 /2
                                                        


In the equation (2.14) the engineering strain vectors were used for convenience of discus-
sion. Nevertheless, in order to use them is necessary to find the link with the correspond-
ing tensor strain vectors. The Reuter matrix can be used for this purpose and is here
presented for completeness:

                                                
                                            1 0 0
                                     [R] = 0 1 0                                   (2.15)
                                                

                                            0 0 2

Eventually, the stress state in the plane of the lamina for a general coordinate system can
be obtained:
14                                                                     2| Literature review


                                                                     
                 σ
                  x                ϵ
                                      1                               ϵx 
                                                                             
                  σy    = [T ]−1
                                 [Q]   ϵ2    = [T ] −1
                                                       [Q][R][T ][R] −1
                                                                           ϵy        (2.16)
                
                                   
                                                                      
                                                                         
                  τxy                  γ12                                γxy
                                                                            


However, [R][T ][R]−1 can be shown to be [T ]−T and an abbreviation can be introduced:


                                     [Q] = [T ][Q][T ]−T                             (2.17)

Hence                                        
                            σx 
                                 Q11 Q12 Q16   ϵx 
                             σy = Q12 Q22 Q26  ϵy                                  (2.18)
                                              
                           
                                               
                                                  
                            τxy    Q16 Q26 Q66     γxy
                                                      


The resultant forces and moments per unit width acting on the laminate can be obtained
by integration of the stresses in each layer through the laminate thickness

                                            Z    zk
                                                       
                              Nx 
                                   XN
                                                       σx 
                                                          
                               Ny =                     σy    dz                     (2.19)
                                                    
                                                       
                               Nxy                      τxy k
                                   k=1
                                                           
                                                 zk−1


and                                        Z       
                                                  zk
                             Mx 
                                  XN
                                                     σx 
                                                        
                              My =                    σy    z dz                     (2.20)
                                                  
                                                     
                              Mxy                     τxy k
                                  k=1
                                                         
                                               zk−1




                      Figure 2.10: Geometry of a N-layered lamina
2| Literature review                                                                     15


By substituting the constitutive law (2.18) in both equations (2.19) and (2.20), it is
possible to integrate properly the stresses within each layer of the material, so as to
obtain from all the plies the contributions to sum, in order to compute the forces and
moments per unit width acting on the laminate.

Accordingly, reorganizing all the terms, the laminate constitutive law can be reported in
a compact form:

                            n o "        # n o
                             N              ϵ0 
                             n o = [A] [B]    n o                                    (2.21)
                             M    [B] [D]  κ 

In the latter equation coupling between forces and moments could be shown. The [B] sub-
matrix represents the extension-bending coupling, while the A16 and A26 are associated
with the shear-extension coupling, lastly the bending-torsion coupling is described by the
D16 and D26 terms.
By varying the stacking sequence of the laminae it is feasible to force to zero some of the
terms above mentioned. In fact, three different types of layout can be used:

   • Symmetric: for each ply located at +z and oriented with an angle θ exists a ply
     located at -z and oriented with the same angle θ

   • Balanced: for each ply located at z and oriented with an angle θ exists a ply oriented
     with the opposite angle -θ

   • Anti-symmetric: for each ply located at +z and oriented with an angle θ exists a
     ply located at -z and oriented with an opposite angle -θ

The symmetric laminate is capable to return [B] = 0, uncoupling stretching-bending
behaviour. While balanced layout makes the terms A16 and A26 null. Eventually, anti-
symmetric laminate nullify the terms D16 and D26 .


2.1.6.    Failure modes
Composite materials are composed by different elements and a lot of issues related with
them can arise. As a matter of fact, composites can fail in a wide variety of ways, due to
their intrinsic nature. By definition, failure of a structural element can be stated to have
taken place when it ceases to perform satisfactorily [1]. In wide terms, the definition of
failure changes based on the application and the material considered. in some conditions
small deformations or even barely visible cracks can define the failure of the component,
instead in some others the failure is not declared until the total fracture or separation
16                                                                  2| Literature review


of the component. Composites show that internal failure generally initiates well before
any appreciable changes in macroscopic appearance or behaviour. Therefore, the material
response changes before the material reaches the macroscopic failure. For example, during
the tensile test a deviation from the linear stress-strain behaviour can be seen as the
initiation of the internal damages in the structural element.




                   Figure 2.11: Damaged section of [0/90]s composite


Since polymeric matrices have been used during this project, it is interesting to analyse
which kind of issues may be subject to. Matrix microcracking are intra-laminar fractures
that traverse the width of the layer and move laterally to the fibers [28]. Considering a
[0/90]ns laminate, with a loading applied in the 0° direction, the 90° oriented plies will
exceed maximum stress level before than the 0° plies. As a consequence the cracks will
develop in the 90° oriented plies, as shown in the figure 2.11.




                              Figure 2.12: Modes of fracture


Fibers can be subjected to tensile failure and compressive failure. The first one happens
when the applied tensile load is fiber-oriented, generally the fibers show a brittle breakage
and strength depends on defects. The mechanism of compressive failure is very different
from tensile failure, the majority of the fibers exhibit instability during the application
2| Literature review                                                                       17


of a compressive load and failure of the component is easily reached since the load is no
longer sustained.

During the life cycle of a composite component its structural integrity may be affected by
loading and environment conditions, here some related issues are presented:

   • Delamination failure mechanism can be categorized into mode I, mode II, mode
     III and a mixed-mode (see figure 2.12). This phenomena consists in the interfacial
     detachment between the plies and is barely visible. It may lead to total failure of
     the structure if not recognize on time. This mode of failure can be triggered by low-
     velocity impact, loading condition characterized by great out-of-plane component
     or even by the microcracking in the matrix due to the shear stresses acting at the
     interlaminar level.

   • Fibre pull-out and debonding are mainly related with fibre-matrix interface, they
     can be caused by weak bonding and high stress level transferred trough interface.
     The process starts from matrix cracking, while the fibers may still be intact. This
     means that additional load can be carried, while matrix cracking still opening, until
     a critical value is reached. At this point, interfacial fibre-matrix debonding will occur
     and fibers are pulled out gradually. Eventually, breakage of the entire component
     occurs [19].




                       Figure 2.13: Fiber pull-out and debonding


   • Free-edge effect can influence the failure initiation. When a laminate, characterized
     by different oriented plies, is subjected to a in-plane load, each ply tends to behave
     in a different manners. Since the laminae are considered perfectly bonded together,
     compatibility has to be guaranteed. Because of this, in-plane shear stresses are
     induced on the edge of the laminate and in order to restore the equilibrium inter-
     laminar shear stresses are developed as well. The latters are responsible for the edge
18                                                                    2| Literature review


        dalamination effect. Eventually, it worth noting that CLT is valid only inside the
        laminate, since out-of-plane stress components are not taken into account.

For completeness failure modes can be presented considering loading conditions. Until now
the major issues were presented in general cases, but a more detailed overview is essential
to under how the failure could happen. It is important to highlight that the following
modes do not act independently and most of the times the stress state is complex.

     1. Failure under longitudinal tensile loads
        In a UD composite subjected to tensile loading condition failure may initiate by
        fibers breakage at the weakest cross section. This occurrence happens when 50% of
        the ultimate load is reached. Fiber pull-out and debonding appear and the broken
        fibers increase. The weakest cross section tends to reduce until ultimate failure
        occurs.

     2. Failure under longitudinal compressive load
        As above mentioned, continuous fibers subjected to compressive loads show instabil-
        ity. This can be exhibited in the form of micro-buckling. In particular, it is possible
        to have extension mode or shear mode (see figure 2.14). The first one takes place
        with low volume fraction and extensional strains are predominant, in the second one
        an higher volume fraction is present and shear strains are prevalent in this case.




                                  Figure 2.14: Microbuckling


        Moreover, transverse splitting may be present as well and appears before compressive
        failure mechanism occurs. When ultimate transverse tensile load is reached, due to
        the Poisson effect, cracks at fiber-matrix interface could develop as well.

        Eventually, a third failure mode can be described: shear mode. Experimental results
2| Literature review                                                                    19


     indicates that composites fail with this mechanism at approximately 45° to the
     loading axis.

  3. Failure under transverse tensile load
     Fibers perpendicular to the loading direction are accountable for stress concentration
     at the interface and in the matrix. Failure can be caused by matrix tensile rupture
     or by constituent dobonding and fiber splitting. It is worth noting that the fracture
     surface is in part formed by the failure of the matrix-fiber interface.

  4. Failure under transverse compressive load
     Shear failure of the matrix is the main breakage mechanism in this loading condition.
     Debonding or fibers crushing are two others mechanism that can come with the main
     mode. The fracture surface lies on a plane parallel to the fibers. Also in this case
     fiber-matrix bonding is mainly responsible for the failure and, as expected, the
     transverse compressive strength is lower with respect to the longitudinal one.

  5. Failure under transverse in-plane shear load
     In this case the failure may take place by matrix shear failure, with or without
     constituent debonding. Failure surface could include debonded portions as well.


2.2.     Composites manufacturing techniques
As mentioned in section 2.1 composite materials are composed by two or more con-
stituents. Several manufacturing methods are available in order to overcome all the
technological issues that may arise. Fibers and matrices are partially responsible for
the mechanical features of the final component, also design and production processes can
assume a fundamental role. In general, a relevant aspect that must be considered during
the manufacturing process is the fiber-matrix interface. It is essential that the matrix
adequately wets the fibers so as to fill up any gaps that may be present, this could reduce
the number of flaws and the risks related with cracks. Moreover, an appropriate fiber-
matrix interface is able to guarantee the continuity inside the component and the correct
transfer of stresses. Lastly, the polymeric matrix undergoes the cross-link process [31],
which ensures solidification and cohesion of the whole component.

In the following subsections all the most common methods and all their main features
will be investigated.
20                                                                 2| Literature review


2.2.1.    Spray lay-up
Spray-up is a open-mould application technique for composite. In the first step, the mould
is prepared with the application of mould release layer covered by gel coat layer. Then,
the mould is cured in order to be ready for the process [23]. The fibers and catalysed
resin are sprayed into the mould using a hand-held chopper spray gun. In order to apply
simultaneously both materials the continuous fiber tow is chopped and the resulting short
fibers are directly blown into the sprayed resin stream. Once the spray procedure is
completed an operator compact the laminate by hand with a roller so as to remove air
and create a smooth surface (see figure 2.15), then the part is left to cure under standard
atmospheric conditions.




                            Figure 2.15: Spray lay-up process


It is worth noting that the method ensure design flexibility and low costs, but as a
drawbacks relies on operator skill for product quality and only short-fiber component can
be obtained, limiting the mechanical properties.


2.2.2.    Hand lay-up
Hand lay-up is the most common and widely used open contact moulding technique for
fabricating composite materials, is generally suitable for the production of a few large
products. Similarly for Spray-up, the mould is prepared with anti-adhesive coat and with
gel coat if needed. The consecutive phase consists in laying the dry fibers, in form of
woven, knitted, stitched, or bonded fabrics, in the mould. Then, the liquid catalysed
resin is poured over the fibers bed. An operator spreads the resin by using brushes or
nip-roller-type impregnators in order to compact the material, and force the matrix to wet
the fibers so as to remove any entrapped air (see figure 2.16), the process is repeated for
2| Literature review                                                                     21


each layer. Eventually, laminates are left to cure under standard atmospheric conditions.




                            Figure 2.16: Hand lay-up process


Another similar method is called Wet lay-up process. In this case a pressure is applied to
the laminate after the lamination process in order to improve the consolidation. A plastic
film is sealed over the laid-up laminate and then, through a valve, all the air is extracted
by means of a vacuum pump.




                             Figure 2.17: Wet lay-up process


Differently by the Spray-up method, both Hand lay-up and Wet lay-up allow the produc-
tion of long-fiber components, which guarantee an increasing of the mechanical feature.


2.2.3.    Filament winding
Filament winding is a continuous process method that can be highly automated, this
could lead to an increasing of the repeatability and a reduction of material costs. The
fabrication method is useful to create axisymmetric, as well as some non-axissymmetric,
22                                                                  2| Literature review


composite products such as pipes, pipe bends and tanks [28]. Continuous prepreg sheets,
rovings and continuous dry fibers are driven by several pulleys onto a cylindrical tool
called mandrel, which has the final shape of the component. In particular, the dry fibers
are made pass through a resin bath so as to be wetted. The nip-roller applies the fibers
on the rotating mandrel trough a transverse carriage, which allows to obtain different
orientation angles and different layouts. Once the desired thickness is achieved the curing
phase takes place at room temperature.




                          Figure 2.18: Filament winding process


As above mentioned, this fabrication methods has low costs and the entire procedure is
fast. Additionally, the final components has execelent structural properties, since straight
fibers can be positioned in order to match the loads requirements. As drawback, the
obtainable shapes are limited and the external surface is unmoulded, thus the quality
is poor. It is interesting to notice that filament winding is one example of aerospace
composite material.


2.2.4.    Pultrusion
Composite pultrusion is an automated fabrication method for producing continuous length
component with constant cross-section. In this process, fibers are pulled from a creel
through a heated resin-wetting station, then the wetted fibers are pulled into a heated die
so as to obtain the desired cross-sectional shape. In greater detail, the last step complete
the impregnation process, by controlling the resin content and curing the material in its
final shape. Eventually, parts are made by cutting the long-cured piece. The method can
2| Literature review                                                                    23


be very fast and economical, high fiber content can be easily achieved, thus increasing
the mechanical feature. On the negative side, the process is able to produce only linear
component with a constant coss-section such as beams (e.g. I or T shapes), ladders and
mouldings. Fabrics can be used too in order to provide other diretions than 0°.




                             Figure 2.19: Pultrusion process


An alternative variant of the fabrication method is called pulforming, it allows for some
variation in the cross-section shape. The wetted fibers are pulled through the die and
then clamped in a mould for the curing process. Small changes in the section can be
obtained, but the continuity of the method is lost.


2.2.5.    Resin Transfer Moulding (RTM)
An alternative fabrication process to replace hand lay-up is the resin transfer moulding
(RTM) technique. Firstly, the dry fibers are laid in the mould and then pre-pressed
in order to have preformed fiber reinforcements. After, the mould is treated with release
agent and the preformed fibers are positioned in the tool. A second mould is then clamped
over the first, and pre-heated resin is injected through inlets into the cavity with a low-
to-moderate pressure. Generally, the liquid resin has low viscosity and is mixed with
catalyst so as to accomplish the polymerization process. When the mould is full and all
the trapped air is expelled through the outlets, the resin supply is removed and both
mould inlets and outlets are sealed. In the last phase the mould is heated so as to cure
the component.
24                                                                 2| Literature review




                      Figure 2.20: Resin Transfer Moulding process


A variation of the RTM process is called vacuum-assisted resin transfer moulding (VARTM).
The difference is that in VARTM, vacuum is applied to the outlet of the mold, and the
resin is drawn into the mold by vacuum only. Hence, high heat or high pressure are not
required to consolidate the laminate structure, and expel completely the air in the cavity.

These simple and effective processes can be employed for making both large and small
complex parts within a short cycle time. The costs are low due to the simple tools
and the possibility to automate the procedure. A variety of layout of fibers with its
orientations can be exploited: continuous-strand mat, woven roving, or even cloth can
be used. Thus high-quality and high-strength composite structure with a good quality
surface can be achieved. As drawback, extreme large component cannot be obtained with
this procedure.


2.2.6.    Resin Infusion under Flexible Tool (RIFT)
The RIFT manufacturing method is conceptually similar to VARTM technique. The
preformed dry reinforcement is placed onto a mould tool, and a peel-ply is applied in
order to spread the resin over the fibers. Then, a flexible plastic polymeric bag, equipped
with valves, is positioned over so as to close and seal the component. Through a vacuum
pomp, all the entrapped air is evacuated and then the catalysed resin is drawn into
the reinforcement [36]. After the curing process the component is extracted and further
processes will be performed.
2| Literature review                                                                    25




                Figure 2.21: Resin Infusion under Flexible Tool process


This technology was developed to reduce the detrimental styrene emissions produced by
the polyester resin. However, with respect to both VARTM and RTM, the RIFT process
is able to reduce the costs associated with the tools, since half of the conventional rigid
mould is replace with a plastic bag. On the other side, there is no direct control over the
thickness of the final composite structure, and good quality surface is achieved only on
the moulded side. The method is suitable for the production of large components with a
low volume production.


2.2.7.    Compression moulding
This process is a matched-die moulding fabrication method, which produces a large num-
ber of reinforced thermosetting resin products. The process is fast and simple, the pre-
formed moulding compounds or premix with partially catalysed resin are placed in the
preheated mould. The mould halves are closed and controlled pressure is applied in the
cavity, in this way the resin becomes liquid and the complete polymerization occurs. Once
the mould is cooled, the component can be extracted. This method offers an high degree
of productivity and automation, high-quality and high-strength components can be pro-
duced in a large variety of size and shape in a short cycle time. The most used preformed
moulding compounds such as bulk or dough molding compounds (BMC and DMC), sheet
moulding compound (SMC) and prepregs are presented below.
26                                                                  2| Literature review




                       Figure 2.22: Compression moulding process



Bulk or dough moulding compounds (BMC and DMC)
These compounds consist of a dough-like or putty-like mixture of fibers, resin and filler
to which pigments and others materials may be added [1]. They are made by mean of an
high-shear z-blade mixer, the final compound can be extruded into rope form ready to be
used directly in the mould.


Sheet moulding compound (SMC)
To manufacture SMC a continuous polyethylene film is covered with an appropriate
polyester resin, then a layer of fiber reinforcement (chopped strand mat or chopped rov-
ings) is deposited. A second layer of polyethylene film coated with resin is placed over the
reinforcement, and the sandwich thus formed is forced to pass through a series of rollers
so as to properly wet the fibers. Eventually the compound is roll while the resin thickens,
the results is a flat and tack-free sheet composed by either glass, carbon or aramid fibers.
In order to use the product, both films of polyethylene have to be removed, then the
required size of SMC can be placed in the mold, pressed and cured.


Prepreg
Preimpregnated fiber-reinforced plastics are produced in a similar way to sheet moulding
compounds, where the reinforcement is sandwiched between two layers of resin system
applied to suitable release film. In particular, the first step consists in wetting the fiber
reinforcement into a resin bath, then through a metering roller assembly the picked resin
is controlled. The wetted fibers are forced to pass through an heating zone to evaporate
the solvent and partially cure the resin. Then, two release films are applied on both sides
of the prepreg so as to form the sandwich shape, heated rollers may be used to ensure
and adequate wetting of the fibers. Eventually, the final sheet is rolled up and the curing
2| Literature review                                                                     27


process proceeds until a tack-free product is obtained, the product can be stock for several
weeks to months in an appropriate environment. Different types of fiber reinforcements
can be use: continuous unidirectional, woven fabric or random chopped-fiber sheets, while
the epoxy resin is the most employed. The difference with SMC is that thickening agents,
fillers, pigments, and additives are rarely used in the resin system. Lastly, the prepregs
can be use in the compression moulding method similarly to SMC.




                          Figure 2.23: Sample of prepreg lamina



2.2.8.    Prepreg - Autoclave
This bag moulding process is one of the oldest and most versatile manufacturing composite
parts. In the first step the mould is prepared, release coating is applied and a peel-ply
is used so as to protect the mould surface. Optionally, an extra release film can be used
to facilitate the final stage of the process. At this stage, the pre-impregnated material
with semi-catalysed resin (see 2.2.7) is positioned in the mould, and then breather layer
is applied externally to the whole sandwich structure. The latter layer allows to absorb
excess resin and promotes the evacuation of the entrapped air and volatile substances. All
the above-mentioned elements are placed inside a vacuum bag, equipped with valves, and
sealant tape is used to ensure no air leakage. Once the air is pumped out, the sandwich
structure is laid in the autoclave (see figure 2.24). In the chamber the curing process
takes place, the temperature is raised up to 180° and the pressure applied can reach up
to 5 atmospheres. This allows the resin to to reflow and cure, while the entrapped air
is completely evacuated due to the applied high external pressure. Eventually, after the
curing cycle and the cooling phase, the prepreg can be extracted from the mould.
28                                                                 2| Literature review




                       Figure 2.24: Autoclave production process


This fabrication method offers composites with high mechanical features and good quality
surface. Since inexpensive tooling are required, the cost are limited. On the other side,
the laying-up and bagging steps are crucial for obtaining high quality products. Con-
sequently, the workers skill and know-how are essential to properly perform every step
of the procedure. Eventually, the method is time-consuming and it is suitable for low
production volume.


2.2.9.    Additive manufacturing
Additive manufacturing (AM) is a tree-dimensional (3D) printing technique. The pro-
cess starts from 3D CAD model, then several thin layers of material can be successively
printed, by means of a specif 3D printing machine, in order to obtain the final compo-
nent. Generally, AM guarantees high level of geometrical complexity, and provides a wide
range over the selection of fiber volume, orientation and type. Since the requirement of
moulds is eliminated, cost, cycle time and material wasting can be considerably reduced.
Hence, the method is particularly suitable for the design-to-prototype phase of product
development [27]. As drawbacks, low mechanical features are achieved and poor quality
surface is obtained as well.
2| Literature review                                                                     29




                      Figure 2.25: Additive manufacturing process



2.3.      Experimental testing phase
Material characterization needs an experimental testing campaign in order to achieve
all the relevant mechanical features of the material. Different approaches are available,
but the most effective is the building block approach (BBA), which is is used during
airworthiness certification process of an aircraft. The aim is to conduct numerical analysis
and related tests at various levels of structural complexity so as to fulfil all the safety
requirements. The BBA can be seen with a pyramidal organization and, in the lowest
level, a large amount of tests on simple, cheap and standard specimens are performed.

The focus of this work concerns the lowest level of the BBA. In detail, the material charac-
terization of composites needs reliable method to obtain information such as: stress-strain
relationship, elastic constant and damage mechanism. Unfortunately, different elements
could affect the results of the tests, especially: orthotropy, non-homogeneity, inelasticity
and stacking sequence. Even production problems must be taken into consideration, since
composite materials are produced in batches. Quality of the raw materials and human
work play a major role on the final product, thus a quality check is needed to ensure
adequate mechanical features. Therefore, non-destructive inspection (NDI) techniques
must be used on proper samples, the most used are ultrasound and radiography. High-
resolution experimental methods are able to offer a comprehensive overview of the material
response, based on the study of the micromechanics a detailed stress-strain relationship
can be obtained and an understanding of material damage process can be acquired as
well. In order to achieve a complete analytical material model the damage effects have
to be considered, the reason is related with the dependency between damage mechanism
and loading condition. In this way a long-term response can be reached, since composites
30                                                                  2| Literature review


can be subjected to a large variety of loading conditions during their life cycle.




                  Figure 2.26: Schematic of a building block approach


For this thesis work the American Society for Testing and Materials (ASTM) standards
have been considered so as to perform the characterization tests. Eventually, by apply-
ing well known analytical models the damage evolution have been predicted from the
experimental results.


2.4.      Numerical modeling phase
Numerical simulation is largely used nowadays in order to achieve more precise solutions
in a short amount of time. Generally, this tool is implemented when dealing with complex,
non-linear mathematical problems is required. In the field of structural engineering, the
Finite Element Method (FEM) is the most employed approach, from this, thanks to his
functionality and adaptability, different commercial codes have been developed through
the years. Composite materials behaviour is very complex and in order to capture such a
response many materials models were developed. Especially, damages and failure modes
are the most challenging parts to be modelled, since a trade off between computational
costs and accuracy have to be found in order to obtain a valuable solution in the shortest
amount of time. Indeed, the development process is still ongoing nowadays and phenom-
ena such as delamination and microscopic behaviour are being investigated.
2| Literature review                                                                       31


LS-DYNA is a commercial software used to solve highly non-linear transient dynamic
finite element analysis (FEA) problems exploiting explicit time integration. Green com-
posite materials are a new and innovative solution recently on market, due to the relevance
of numerical simulations it is essential to replicate their behaviour so as to develop in-
creasingly accurate and efficient material models. LS-DYNA was selected to start this
process due to its huge variety of material cards already present in the software library.
Parameters will be found in order to predict and simulate both the static and dynamic
behaviour. It worth noting that the selected solver is the most suited in the context of
dynamic impacts.

As well known, composite materials are made by layers stacked together and are mostly
used in aeronautical and automotive fields. The manufactured components are panels
usually joined together, which can be seen as thin-wall structures. For this reason plane-
stress condition and CLT (see sections 2.1.4 and 2.1.5) were presented so as to approximate
the behaviour of these structures. Different mesh element can be chosen in order to nu-
merically simulate composites. Two-dimensional (2D) shells and three-dimensional (3D)
thick shells are the most suitable for this purpose, by exploiting through-the-thickness
integration points each ply can be considered in the numerical procedure and the stacking
sequence of the composite material can be thus easily modeled within one element [8]. In
order to evaluate out-of-plane shear resistance the 3D thick shell elements can be used,
since Kirchhoff hypothesis is discarded. Overall, shells are very efficient since good results
can be achieved with a limited computational effort. By exploiting solid (brick) elements a
more accurate solution can be obtained as well, but is essential to highlight that bricks are
not suitable for this purpose, as the plies stacking sequence cannot be explicitly defined
within one element, thus increasing exponentially the computational cost. Eventually,
stacked-shell approach can be introduced: each layer is numerically modelled by a single
shell and then the constraints between the plies are properly imposed. This model allows
to take into account delamination phenomena, but the drawbacks are an increasing of the
computational cost and additional experimental tests for the calibration phase.

In conclusion, even if 2D shell elements are not capable to capture interlaminar behaviour,
they are the most suitable for representing numerically natural composite materials be-
haviour.


2.4.1.     Material cards overview
The first material models were very simple, generally elastic behaviour until failure was
preferred. Over the years development led to more advanced models in which post-failure
32                                                                  2| Literature review


evolution and damage parameters were taken into account. In doing so the LS-DYNA
material library has been expanded, offering a wide choice in terms of orthotropic material
models.




              Figure 2.27: Comparison of MAT054, MAT058 and MAT262


In the LS-DYNA database the first composite material card is *MAT_022, which is based
on the Chang-Chang failure criteria. A linear elastic law until failure is used, but nei-
ther failure in longitudinal compression nor post-failure behaviour are exhibited. The
*MAT_054/055 models are the most used in crash simulations [7], are based respectively
on Chang-Chang and Tsai-Wu failure criteria. with respect to the previous material,
a post-failure phase is introduced, in detail a pseudo-elastic response is exploited while
a strain-based failure criterion defines the ultimate failure. The *MAT_058 is based
on Matzenmiller work [18] and the first improved version, based on *MAT_054, was
presented in [32]. Non-linear behaviour until failure can be defined by setting appro-
priate damage parameters, and post-failure phenomena can be described as well as in
*MAT_054. Failure in the three directions can be completely uncoupled and a bi-linear
stress-strain relationship can be achieved in the shear direction. Because of these features
the model is able to simulate complex forms such as woven fabric. The material mod-
els *MAT_261 and *MAT_262 were respectively developed by Pinho and Camanho. A
linear behaviour until failure is chosen, while the post-failure damages are represented
by a linear or bi-linear degradation formulation. Additional fracture toughness tests are
needed in order to achieve the parameters useful to calibrate the material models.

Eventually, a trade-off among results accuracy, computational cost and number of exe-
cutable tests must be found in order to select the best material model. The *MAT_058
fits all the requirements to accomplish the numerical characterization phase.
2| Literature review                                                                             33


2.4.2.     *MAT_058 material model
The material card 58 relies on an anisotropic elastic damage model, where micro-cracks
and voids development is taken into consideration during the deformation process. This
assumption leads to degradation of stiffness and other elastic properties, as well as to
plastic deformation. In this way, the typical brittle-elastic behaviour of natural composite
material can be assessed.

In the context of homogenized continuum (see 2.1.3), for each lamina of the composite
structure four failure criteria can be defined following the Hashin methodology (1980). In
particular, fiber failure mode and matrix failure mode are divided, as well as compressive
and tensile stress conditions.

Here the quadratic parameters:

   • Tensile fiber mode (σ11 ≥ 0):

                                                      2             (
                                                 σ11                      ≥ 0 f ailed
                                   e2m =                    −1                                (2.22)
                                                 Xt                       < 0 elastic

   • Compressive fiber mode (σ11 < 0):

                                                      2             (
                                                 σ11                   ≥ 0 f ailed
                                   e2c =                    −1                                (2.23)
                                                 Xc                    < 0 elastic

   • Tensile matrix mode (σ22 ≥ 0):

                                            2                 2         (
                                       σ22                  τ                   ≥ 0 f ailed
                          e2m =                   +                   −1                      (2.24)
                                       Yt                   Sc                  < 0 elastic

   • Compressive matrix mode (σ22 < 0):

                                            2                 2         (
                                       σ22                 τ                  ≥ 0 f ailed
                           e2d =                  +                   −1                      (2.25)
                                       Yc                  Sc                 < 0 elastic

Where strength coefficients Xt , Xc , Yt , Yc , Sc can be obtained from uniaxial loading tests.

The effective stresses must be considered in the equations above since only the undamaged
part of a cross section can carry load. In order to obtain this stress definition the net area
34                                                                     2| Literature review


is considered. Besides, it is possible to specify the relationship between effective stresses
and nominal (true) stresses:

                                                                 
                                   1
                                              0           0        
                     σ̂11   1 − ω11
                                                                 σ11 
                                                1                  
                       σ̂22 =  0                          0       σ22               (2.26)
                                                                 
                     
                                         1 − ω22                   
                       σ̂12                               1       σ12 
                                   0            0
                                                        1 − ω12

Where ωij is called damage parameter and must lower than one (ωij < 1).

It must be noted that ω11 and ω22 assume different values for tension (ω11t and ω22t ) and
compression (ω11c and ω22c ) so as to account for the on-sidedness of the phenomenon,
typical for many materials. The parameter ω12 is assumed to be independent from the
sign of the shear stress τ .

The constitutive law for plane-stress condition and orthtropic material can be now written
as function of the damage parameters:


                                                                         
 σ 1 
              (1 − ω11 )E1         (1 − ω11 )(1 − ω22 )ν21 E2      0        ϵ1 
                                                                             
       1                                                                       
   σ2 = (1 − ω11 )(1 − ω22 )ν12 E1       (1 − ω22 )E2              0       ϵ2
                                                                           
 
     D                                                                    
                                                                              
   τ                 0                          0              D(1 − ω12 )G    γ
                                                                                 


                                                                                      (2.27)


With
                           D = 1 − (1 − ω11 )(1 − ω22 )ν12 ν21 > 0                    (2.28)

The state of damage is uncharged in the elastic range, which is bounded by the failure sur-
faces. The threshold values described by the failure criteria can be defined by substituting
the nominal stresses with the effective stresses:

                                            2
                                          σ11
                             f∥ =                   2
                                                        − r∥c,t = 0                   (2.29)
                                    (1 − ω11c,t )2 Xc,t
                                  2
                                 σ22                  τ2
                      f⊥ =                  2
                                               +                 − r⊥ = 0             (2.30)
                           (1 − ω22c,t )2 Yc,t   (1 − ω12 )2 Sc2

Where the size of the elastic region is defined by the damage threshold r.
2| Literature review                                                                     35


In order to obtain all the failure criteria independent from each other a partial uncoupling
of the failures can be performed. Here the general solution with non-smooth failure
surfaces is presented:

                                            2
                                          σ11
                             f∥ =                   2
                                                        − r∥c,t = 0                  (2.31)
                                    (1 − ω11c,t )2 Xc,t
                                              2
                                             σ22
                              f⊥ =                      2
                                                           − r⊥ = 0                  (2.32)
                                       (1 − ω22c,t )2 Yc,t
                                             τ2
                                fs =                    − rs = 0                     (2.33)
                                        (1 − ω12 )2 Sc2

The state of damage changes once the state of stress is outside of the failure criteria. In
particular, for the damage parameters many evolution laws are possible. with respect to
material model 54 a smooth increasing of damage is described and the material response
gradually changes. In this way the *MAT_058 proves to be more accurate and physically
more correct.

                                                               mi 
                                             1              ϵi
                               ωi = 1 − exp                                          (2.34)
                                            mi e            ϵf

With ϵf is the nominal failure strain:


                                       Xt,c                        Yt,c
                              ϵf ∥ =             ;      ϵf ⊥ =                       (2.35)
                                       E∥                          E⊥

The parameter mi describes the development of the different failure modes in the different
directions. When the damage parameter is equal to 1, complete failure is reached.

The application of strain softening damage models can bring the localization effect. When,
in the loaded element, the stress level exceeds the maximum stress value, strain softening
starts and due to minor numerical differences some elements are further deformed, whereas
other elements are unloaded. This problem introduce the mesh size dependencies into any
FE model and it must be considered. To avoid the localization effect a modification to
the damage evolution law is introduced. The idea consists in not letting the stress fall
below a threshold value, the yield-stress. After the reaching of this limit value the damage
parameter ω becomes:


                                                     αXt,c
                                         ω =1−                                       (2.36)
                                                      Eϵ
36                                                                     2| Literature review


In order to relate the yield stress with the strength value α is defined. In particular, the
value can be 0 ≤ α ≤ 1. For α = 1 (without softening) the strains grow in all the elements
in a similar manner, whereas for value of α lower than 1 localization effect is still present
and the damage growth is only in the first affected elements.

The implementation of the material model can be now reported by highlighting the most
significant parameters. The table below shows the card structure [17].

     MID       RO         EA         EB          EC       PRBA        TAU1      GAMMA1
     GAB       GBC       GCA      SLIMT1      SLIMC1     SLIMT2      SLIMC2       SLIMS
     AOPT     TSIZE    ERODS       SOFT          FS        EPSF       EPSR        TSMD
      XP        YP        ZP         A1          A2         A3        PRCA        PRCB
      V1        V2        V3         D1          D2         D3        BETA      LCDFAIL
     E11C     E11T       E22C       E22T       GMS
      XC       XT         YC         YT          SC

                            Table 2.1: *MAT_058 card overview


In the table 2.1 there are elastic constant, strength-related terms and some non-physical
parameters. The latter can considerably change the material behaviour. It is worth
introducing the most relevant [9]:

     • SLIMxx: it represents the constant α in the equation (2.36). It can be defined both
       in tension and compression for each material direction. It should not be set to zero.

     • ERODS: it is the maximum effective strain for an element layer. It control the
       elementqfailure determining the complete failure (complete deletion). It is define as:
       ϵef f = 23 ϵij ϵij

     • FS: Failure surface type, see equations from (2.29) to (2.33)

     • SOFT: This factor is related to the material strength in crashfront. In order to
       simulate crack propagation, the elements adjacent to the deleted ones are subjected
       to a stress reduction during the softening phase.

     • Non-linear (bi-linear) stress-strain curve for shear part: if failure surface definition
       (2.33) is considered, non-linear shear behaviour can be set through parameters:
       GAMMA1, TAU1, GMS, SC. For a better understanding the figure 2.28 is reported.
2| Literature review                                                        37




             Figure 2.28: Non-linear stress-strain relationship for shear
                                                                                         39




3 | Natural composite materials
As already mentioned in the section 2.1, composite materials have been used the first time
more than 3000 years ago. In particular, natural fibers and natural matrices represented
the only available sources to achieved composites. Over the last centuries, the technolog-
ical progress led to the development of synthetic composite materials with increasingly
better mechanical performances and remarkable reliability. Nowadays, the environmental
issues are more and more relevant and the need to develop new materials, that are entirely
based on renewable resources, is only the first step to reduce the consumption of fossil
fuel and the consequently production of CO2 emissions. Natural composite materials can
represent a valid alternative to the petroleum-based composites [29]. Through the last
years, the studies and researches on these materials exhibit significant mechanical fea-
tures and competitiveness with respect to the traditional solutions. Although there is
still a lot of work to be completed, these results show the opportunity to employ these
new products in a sustainable and responsible way [25]. Bio-based composite materials
advantages have been already exploited in recent years in different industrial sectors, such
as: transportation (automobiles, railway coaches, aerospace), building and construction
industries (ceiling paneling, partition boards), packaging, consumer products, etc. In
addition, their mechanical features and dynamic behaviour have attracted their use in
many crashworthiness applications. Natural composite materials can be defined as the
combination of fibers and matrix where at least one component has a natural source. If
in the composites both the constituents are obtained from renewable resources, the prod-
uct can be called green composite material. On the other side, a partially eco-friendly
composite is obtained. Natural fibers can be either plant or animal sourced. The latter
are composed by proteins, whereas the first typology are comprised of cellulose. For the
sake of simplicity, in composite industry and in this work, natural fibers are referred to
vegetables fibers. It is worth noting that most of the natural composites are composed
by natural fibers with polymeric matrix, due to technological limitations in obtaining a
suitable natural matrix.
40                                                     3| Natural composite materials




                         Figure 3.1: Classification of bio-composites


Natural composite materials can be divided in three different type [21]:

     • Synthetic polymers matrix reinforced with natural fibers, they are the most used
       due to their mechanical characteristics and production ease.

     • Bio-polymers reinforced with synthetic fibers such as glass or carbon, they are the
       least used due to their disposal issue at the end of their life cycle.

     • Green composite materials are composed by natural fibers and natural matrix. They
       are the most interesting, as acceptable mechanical properties can be achieved while
       preserving biodegradability.

Bio-base fibers can be vegetable, animal or mineral origin, excluding the plant fibers, the
remaining fibers are the least used due to the lack of applications or even because are
banned by the law. Indeed, animal fibres are not commonly used and asbestos was banned
due to risks of exposure and risks associated with human health. Hence, plant fibers are
the most commonly used in industry and the most analysed by the research community,
thanks to their renewability, wider availability and short growth period. These fibers can
be divided in six basic types:

     1. Bast fibers (jute, flax and hemp)

     2. Leaf fibers (abaca, sisal and pineapple)

     3. Seed fibers (coir, cotton and kapok)

     4. Core fibers (kenaf, hemp and jute)

     5. Grass and reed fibers (wheat, corn and rice)

     6. All other types (wood and roots)
3| Natural composite materials                                                           41


Natural fibers may offer a large variety of properties depending on the plant species
employed. Cellulose, hemicellulose and lignin compose a generic plant structure, and each
of these constituents have an influence on the fiber features, such as: strength, thermal
degradation, biological degradation, moisture absorption and UV degradation. It is worth
noting that linear cellulosic macromolecules are linked by hydrogen bonds and are closely
associated with hemicelluloses and lignin, which confer stiffness to fibres. Additionally,
the latter are responsible for the cellulose containment within the fibre cell wall and hold
the fibres together [5].

The properties of a bio-composite materials depend on the polymeric matrix chosen. To
produce this constituent can be exploited either bio-based sources (plant or animal) or
synthetic (oil-base product). The natural polymer or bio-polymer are biodegradable and
to produce them starch or proteins can be used. Nowadays, poor mechanical perfor-
mances are offered by this product due to the lack of interfacial adhesion between matrix
and fibers, however development is just begun and a wide room of improvement is still
available. Synthetic fillers can be divide in thermoset and thermoplastic. The latter can
be melted over a certain temperature, the van der Waals and hydrogen bonds are tem-
porarily broken allowing molecular manoeuvrability. Due to its behaviour, this matrix
type can be reused, but the mechanical features can fulfil non-structural requirements.
The thermosets have a wide range of applications thanks to their good adhesion, high
thermal and chemical resistance and excellent mechanical properties. Their are the most
used in composite industry since good mechanical features such as: strength, stiffness,
toughness and transverse fracture stress can be obtained in the final composites. Also
the matrix-fiber interfacial properties fulfil all the structural mechanical requirements.
Unfortunately, thermoset matrices are difficult to recycle and reuse.


3.1.      Reasons to study them
As well known, traditional composite materials have several advantages with respect to
the metals, and they were capable of satisfying the market demand for several decades.
However, the requests changed over the past few years and new needs must be satisfied.
For this reason, natural composite materials become more and more attractive in com-
posites industry, due to their numerous advantages and the possibility to develop and
improve considerably their main features.

In table 3.1 the most important benefit and drawbacks are reported. In particular, the
low density of these materials must be taken into account in the context of the mechan-
ical properties. When the specific modulus is considered, the natural fibers show data
42                                                      3| Natural composite materials


comparable or even better than those of glass fibers [21]. In table 3.2, the specific gravity
is evaluated to obtain the specific quantities, in detail it can be defined as the ratio of the
fiber’s density over the water’s density. These higher specific properties can be exploited
in applications where, besides the request of good mechanical feature, the weight aspect
plays a major role. In the context of crashworthiness, due to the elongation property, high
energy absorption capability can be reached as well as high specific energy absorption,
thanks to the low density values [24].

     Advantages                                 Disadvantages
     • Good thermal insulation                  • High hygroscopicity
     • High acoustic damping                    • Low thermal resistance
     • Vibrations damping                       • Low durability
     • Low cost materials                       • Poor fiber-matrix adhesion
     • High specific mechanical properties
     • Environmentally friendly
     • Light weight/low density
     • Less health hazard
     • Ease in fabrication
     • Availability
     • Morphological flexibility
     • Corrosion resistance
     • Electrical insulation

                 Table 3.1: Pros and cons of natural composite materials


During crash tests on ramie epoxy composites, a ductile behaviour was exhibited and
there was no debris split after crushing, this can be attributed to the high elongation
property of ramie fibers [11]. Several studies pointing out the lower cost of natural fibers
comparing with synthetic fibers, for example were demonstrated that plain weave jute
fabric combined with epoxy resin is considerably cheaper than the synthetic counterpart
such as glass/epoxy or carbon/epoxy [4]. However, in order to perform a correct evalua-
tion it is essential to consider the applications, the production process and the life cycle
costs. In general, raw natural fibers are cheap and require low energy processes to be
manufactured, this leads to a reduction of the overall costs with respect to traditional
reinforcing fibers (see table 3.3).
3| Natural composite materials                                                              43


             Fiber        Specific    Tensile Strength     Modulus Specific
                          Gravity         (MPa)             (GPa)  Modulus
              Jute            1.3            393               55            38
              Sisal           1.3             510              28            22
              Flax            1.5            344               27            50
             Hemp            1.07             389              35            32
           Glass fiber       2.5             3400              72            28

                           Table 3.2: Specific mechanical properties


At the actual rate of consumption, the world petroleum resources are estimated to last for
the next 50 years or so [33]. Moreover, several environmental issues are rising throughout
the last years. Hence, pollution laws are getting stricter leading to an increasing of the dis-
posal costs of synthetic composite materials. Natural composite materials are able to meet
these needs by exploiting their most relevant benefit: biodegradability. The production
process starts from the plantation, which is a labor-intensive activity. Nowadays, plants
are cultivated extensively but most of their abundant wastes do not have any usefulness.
Since natural fibers are extracted manually, the human resources prove to be fundamental
to complete such task. Hence, the natural composites can represent an economic interest
for agricultural entrepreneurs while creating new employment opportunities, especially in
developing countries, where the primary sector is predominant [29]. During the plantation
phase, a huge benefit is given by the consumption of CO2 in favor of the emission of O2
back to the environment. Additionally, the manufacturing process for natural compos-
ites requires less amount of energy with respect to the traditional solutions, leading to
a further reduction of emitted CO2 . Eventually, at the end of their life cycle, natural
composites can be reuse for other application. Otherwise, if not recycled, they will not
represent a threat for the environment, thanks to their biodegradable feature.

                     Fiber          Cost (US$/ton)      Energy (GJ/ton)
                 Natural fiber         200-1000                  4
                  Glass fiber          1200-1800                30
                 Carbon fiber            12500                  130

                         Table 3.3: Energy and cost of different fibres


As reported in table 3.1 the drawbacks are mostly related with degradable nature of
these materials. A major problem is represented by the thermal resistance, due to the
44                                                      3| Natural composite materials


presence of cellulose inside the natural fibers, the product is not suitable either for high
temperature treatments or applications. When fibers are exposed to such conditions can
easily catch fire. To effectively address this problem, a flame retardant substance can be
add during the production process, so as to minimize fire hazards [13]. Another important
issue to be considered is associated with the higher variability of the raw materials, several
aspects such as soil composition and morphology can influence the quality of the fibers,
thus the mechanical properties of the final product. Green fibers are rich of cellulose,
hemicelluloses, lignin, and pectin, all these components are usually hydrophilic sources
[22]. This cause the fibers to be highly hygroscopic and prone to absorb water, especially
when exposed to moisture. This feature is in contrast with the hydrophobic nature of
polymeric matrices, thus interface adhesion issue between fiber and matrix can arise.
As well known, mechanical properties are related with this aspect, so a reduction of
strength can happen if a proper adhesion is not performed. Eventually, in the context of
crashworthiness studies, in order to reduce the moisture content of the composite materials
a pre-production treatment on fibers is performed, this consists in adding an appropriate
amount of nanoparticles so as to reduce adhesion uncertainties.


3.2.      How they are manufactured
The manufacturing techniques employed to fabricate natural composite materials are
similar to those used for the traditional synthetic composites. However, due to their
innovative nature, researches and experiments are still going on. Hence, various and
new manufacturing methods are investigated so as to improve and develop the natural
composites features, reducing the costs and increasing the overall efficiency.

The first stage of the manufacturing process starts from the extraction of the raw materi-
als, as mentioned in the previous section (see section 3.1), this operation relies mainly on
human labor. Many extraction techniques can be exploited such as mechanical, chemical
or a combination of both, some of them are rudimentary processes and there is no scien-
tific consensus or standards capable of allowing a robust comparison. These techniques
can produce crops with good quality, but a long and laborious work is required. It is
worth noting that bast fibers are the most widely used due to their ease of extraction
and remarkable mechanical properties. As well known, natural fibers are affected by high
level of water absorption index, and adhesion problems related with the fiber-matrix in-
terface may arise. In order to address these issues several techniques have been studied
through the years such as water-repellent chemicals, coupling agents and physical treat-
ment. Those are able to improve the final mechanical properties by modifying the surface
3| Natural composite materials                                                             45


morphology and the roughness of the fibers. Physical treatments are most economical and
practical, since they do not involve the use of detrimental chemical product. Four meth-
ods can be presented as the most popular: corona treatment, plasma treatment, steam
treatment and heat treatment [21]. Corona and plasma rely on two different technologies,
but the aim is similar: forming an ionized region so as to induce a surface modification
of the fibers, this can promote the wettability of the reinforcement. Steam treatment is
exploited to give permanent deformation to fibers, high temperature and moisture are
used to achieved such a result. Eventually, heat treatment is the most widely and valid
accepted techniques to dry natural fibers, different tools can be employed such as hot air
jets, rotating driers, ventilated ovens, in order to reduce the humidity level below 3%. An-
other solution employed to improve matrix-fiber interfacial adhesion and fiber dispersion,
and to reduce the formation of voids inside the material, consists in the addition of small
amounts of a “third component”, which acts as an adhesion promoter between polymer
matrix and cellulosic fiber. The latter is called coupling agent, in detail its molecules are
characterized by a hydrophilic part, able to create the bonds with the polar groups typi-
cally present on cellulosic fibers, and a hydrophobic part, which shows higher affinity to
the macromolecular chains. Generally, coupling agents are identified as suitable polymer
and the most used are methyl methacrylate, acrylamide, acrylonitrile and maleic anhy-
dride polyethylene. An example of the improvements that a maleated adhesion promoter
can assure to a green composite based on polypropylene matrix and 30 wt.% wood flour
is reported in table 3.4 [16].

                   Property            Standard GC        GC with 3%MAPP
           Elastic modulus (MPa)             954                    1035
           Tensile strength (MPa)            19.5                   27.2
           Elongation at break (%)           4.2                     4.6
           Impact strength (J/m)              83                     98

Table 3.4: Mechanical features green composite (GC) without and with the use of a
maleated adhesion promoter (MAPP)


More invasive chemical treatment are available in the market, these are based on the
utilization of reactive functional groups which are able to interact with the fiber structures
and changing their composition. The objective is to make fibers hydrophobic and improve
the interfacial adhesion, thus enhancing the overall final performance. The most employed
chemical treatments and their effects are reported in the table 3.5 [2, 15, 37].
46                                                    3| Natural composite materials


 Treatment                                         Effect
                     Reduce the lignin content. Improve fibre-matrix adhesion, thermal
 Alkali
                     stability and heat resistivity
 Acetylation         Improve tensile and flexural strength
 Benzoylation        Improve hydrophobicity
 Enzyme              Reduce the lignin content
                     Improve UV-protective properties, hydrophobicity and mechanical
 Grafting
                     properties
 Isocyanate          Surface modification
 Mercerization       Reduce the moisture regain and improve the mechanical properties
 Methacrylate        Improve tensile and flexural strength
 Ozone               Affect surface energy and contact angle
 Peroxide            Reduce the moisture regain
 Silane              Improve hydrophobic and mechanical properties
 Sodium chlorite     Improve tensile strength, young’s modulus and elongation at break

Table 3.5: Chemical treatments on natural fibers and their effects on functional properties




     Figure 3.2: Illustration of hand lay-up of natural kenaf fiber/epoxy composite


Once that all the materials are prepared, the manufacturing process can take place. In
the section 2.2 the most popular fabrication techniques were presented, among those the
most suitable were selected to produce natural composite materials, so as to obtain the
best mechanical features possible. The most used method is hand lay-up due to their low
cost and ease of use, it can be applied for many types of fibers and resins. Especially for
3| Natural composite materials                                                            47


natural fibers, voids can represent a relevant issue, in order to prevent their occurrence in
the hand lay-up process an intensive use of the rollers is performed to facilitate uniform
resin distribution and the removal of air pocket. In addition, this procedure can be
used with compression bladder to improve the mechanical feature. In the field of energy
absorption composite structures (EACS) an intensive use of the VARTM techniques is
employed. One of the biggest advantages of this method is that 70% of fiber volume
fraction (FVF) content can be achieved. This aspect allows for increasing the SEA value
and performing possible modification in the composite composition so as to fulfill all the
needed requirements.




Figure 3.3: Illustration of vacuum bagging manufacturing of GFRP and CFRP composite
cylindrical shell


Another suitable technique for the production of EACS is the filament winding, it can
be used to fabricate cylindrical structures. The materials most commonly employed are
continuous fibers such as yarn and liquid resin such as epoxy, polyester and vinyl ester.
Some studies have been conducted on compression molding techniques with good results,
however the low thermal resistance of natural components affects the processing tempera-
ture, which should be kept below 200°. Eventually, natural fibers can be organized in the
form of prepreg, this allows for the employment of the autoclave, as reported in section
2.2.8. The method is economical and good mechanical properties can be easily achieved.
As a drawback, the processing temperature is a critical aspect and should be properly
set. It should be pointed out that small amount of humidity is not always detrimental
48                                                    3| Natural composite materials


for natural composites, on the contrary water can help to “soften” the fibers allowing
for an easier manipulation of the material, especially during the placement phase of the
manufacturing process.

Innovative methods are still investigating to guarantee even more effective and more eco-
nomical procedures. For example, electromagnetic induction properties are exploited in
compression molding technique in order to gain an instantaneous heating of the mold
surface. In this way the production cycle time is reduced as well as the related cost.
To maximize the benefits of this method thermoplastic matrix must be employed [35].
Stirring technique has been investigated so as to prepared a green composite based on
dispersion-type biodegradable resin and cellulose nanofibers. A relevant increase in flex-
ural modulus and strength have been found with respect to traditional molding method-
ology [34]. Moreover, improvement of mechanical properties can be obtained by adding
semi-synthetic cellulose fiber (Lyocell) to hemp fiber-reinforced PLA composites. The
results show that combining hemp and Lyocell in a composite can improve the impact
properties by 160% compared to hemp fiber reinforced composites [21].


3.3.     Applications
Since composite materials have been created, their applicability has been exploited in
many different sectors. Natural composite materials make no exception, and their nu-
merous advantages are already used in several applications. As reported in section 3.1,
characteristics such as low specific weight, relatively high strength, resistance to corro-
sion and fatigue, relatively low production cost and biodegradability may allow for an
increasingly employment of these materials. Another important aspect that allows for
this widespread application is given by the huge amount of natural fiber types available.
Each fibers type has unique features that can fulfil different market needs.

Natural composite materials are particularly suited for automotive and transportation
industry due to low density and satisfactorily high specific properties. Body parts such as
engine hood, dashboards, storage tanks, bumpers and so forth can be manufactured by
using reinforcements of natural fibers such as flax, hemp, jute, sisal, and ramie. Numer-
ous car companies invested in the research and development of this technology, in order
to assure the good quality of manufactured natural products. In addition, from these
analyses emerged that the use of natural composites leads to an overall vehicle weight re-
duction, thus reducing the amount of carbon dioxide released to the environment. Some
of the above-mentioned car components fall under the energy absorption structures, their
purpose is to absorb the majority of the impact energy so as to guarantee protection of
3| Natural composite materials                                                          49


passengers from severe impact injuries or death. The aim is to substitute the current
traditional solutions with natural composite materials. In particular, their mechanical
features can be exploited in order to improve important characteristics such as energy
absorption, average load, peak load and crash force efficiency [3]. In this regard, inves-
tigative studies with promising results have been conducted in recent years. For example,
crashworthiness characteristics have been studied on natural silk-epoxy rectangular tubes
[10], or on carbon-jute-glass-epoxy composite circular tubes [4], or even a comparison
among hemp-epoxy, flax-epoxy and jute-epoxy composite cones has been conducted [20].
Since 90s, natural materials were already employed for the production of non-structural
car components. Especially, car interior parts such as seat backs, parcel shelves, front
and rear door coating, trunk coating, and door-trim panels were fabricated with plant
reinforced composites (for furthers details, see [22]). In this case, mechanical resistance
was neglected in favor of low purchasing and maintenance costs, which are the drivers
chosen by car companies to select most suitable material.




        Figure 3.4: Abt Cupra XE body sheel made of flax composite materials


Natural material composites show to be promising for acoustic energy absorption appli-
cations. Their use can be extended to include vibration control and noise reduction. This
behavior was noticed during crashworthiness studies, in fact the use of these materials
in low and mid-frequency region event can damp both mechanical and acoustic vibra-
tions during crash scenario [13]. Moreover, composite structures with bamboo, cotton,
and flax fibers with PLA showed to be great solutions for the improvement of the sound
50                                                     3| Natural composite materials


absorption coefficient in automobile door panels [27]. Natural fiber-reinforced thermoset
and thermoplastic composites fulfil the properties required for aircraft interior panels
such as resistance to heat and flame, serving easy recycling, and disposal of materials
being cheaper and lightweight over conventional sandwich panels. Although traditional
composites show to be suitable for aerospace applications, they exhibit some difficulty in
recycling. Bio-composites can overcome this issue by taking advantage of their low cost
and biodegradable features. Some attempts to fabricate structural parts has been per-
formed: aircraft wing boxes made of ramie fiber composites revealed a 12–14% decrease
in weight. In addition, hybrid kenaf/glass fiber-reinforced polymer composites showed
increased resistance to rain erosion, which is suitable aspect for aircraft application [27].




                       Figure 3.5: Door panel made of hemp fiber


The new green buildings generation must be ecologically mindful, suitable and healthy
place to live and work, for these reasons natural composites can be considered one of
the major used materials in the construction phase. With respect to their applications,
bio-composites can be classified in two main products: structural bio-composites and non-
structural bio-composites. The latter include window, exterior construction, composites
panels, and door frame, while the first can comprehend bridge as well as roof structure.
Thin-walled elements made by sisal fiber reinforced composites exhibit good mechanical
properties such as both high strength in tension and compression, this can allow for a
wide area of application in the structural field. Additionally, bamboo fibers can be used
in structural concrete elements as reinforcement, while both sisal fiber and coir fiber
composites have been used in roofing components in order to replace asbestos [22].
3| Natural composite materials                                                           51


3.4.      Material selection
For the purpose of performing experimental analyses so as to confirm the good quality of
natural composite materials, the most appropriate fiber and matrix must be chosen among
the numerous. This section aims to investigate the most popular solutions in order to
determine the most suitable natural composite materials for this thesis work.

          Fiber        Density        Diameter         Length         Moisture
                       (g/cm3 )         (µm)            (mm)         Content(%)
         Abaca       1.5       10–30 (20)  4.6–5.2 (4.9)                   14
        Bamboo 0.6–1.1 (0.85) 25–88 (56.5) 1.5–4 (2.75)                11–17 (14)
         Banana     1.35       12–30 (21) 0.4–0.9 (0.65)              10–11 (10.5)
          Coir       1.2       7–30 (18.5) 0.3–3 (1.65)                    10
         Cotton     1.21      12–35 (23.5) 15–56 (35.5)               33–34 (33.5)
          Flax      1.38       5–38 (21.5) 10–65 (37.5)                    7
          Hemp      1.47      10–51 (30.5)   5–55 (30)                      8
          Jute      1.23        5–25 (15)   0.8–6 (3.4)                    12
          Kenaf      1.2       12–36 (24)  1.4–11 (6.2)               6.2–12 (9.1)
        Pineapple    1.5      8–41 (24.5)    3–8 (5.5)                     14
         Ramie      1.44       18–80 (49)  40–250 (145)               12–17 (14.5)
           Silk     1.32            -            -                          -
          Sisal      1.2        7–47 (27)   0.8–8 (4.4)                    11

  Table 3.6: Physical properties of natural fibres (average value between parenthesis)


Because of their natural origin several factors may influence the fibers properties such as
the type of soil, growing conditions, harvesting conditions, weather and post-treatment
as well as damage during processing [25]. Due to this relevant variability in the final
characteristics, it must be taken into consideration that there is not one type of fiber
better than the others. Indeed, the suitable fiber selection process depends by several
aspects such as type of application requirements, type of composites to be manufactured,
fibers availability and the possibility to guarantee properties levelling among different
crops or batches. The fiber length is the first issue to be addressed, many studies show the
existence of a critical fiber length value, which is required to develop a complete stresses
condition in the material. In general, fiber lengths shorter than the critical one can lead
to premature failure due to the debonding at the fiber-matrix interface. However, fiber
lengths greater than the critical length can represent a threat as well, since an increase
in fiber length corresponds to an increase in defects, which can compromise the final
52                                                     3| Natural composite materials


mechanical performances. Hence, a compromise must be found in order to maximize the
final performances of the composite. In detail, in crashworthiness application were found
that longer fibers are suitable for this purpose, as the energy absorbing features results
to be superior with respect to the shorter fiber-reinforced composites [21].

            Fiber         Tensile             Young’s            Elongation at
                      Strength (MPa)        Modulus (GPa)         Break (%)
           Abaca       430–813 (621.5)      31.1–33.6 (32.35)           2.9
          Bamboo         270–862 (566)         17–89 (53)          1.3–8 (4.65)
           Banana      529–914 (721.5)        27–32 (29.5)           5–6 (5.5)
            Coir              175                   6               15–25 (20)
           Cotton        287–597 (442)          6–10 (8)             2–10 (6)
            Flax        343–1035 (689)         50–70 (60)           1.2–3 (2.1)
            Hemp        580–1110 (845)         30–60 (45)         1.6–4.5 (3.05)
            Jute         187–773 (480)        20–55 (37.5)        1.5–3.1 (2.3)
            Kenaf       295–930 (612.5)        22–60 (41)         2.7–6.9 (4.8)
          Pineapple    170–1627 (898.5)        60–82 (71)             1–3 (2)
           Ramie         400–938 (669)       61.4–128 (94.7)          2–4 (3)
             Silk       500–1300 (900)            5.22                 15.4
            Sisal        507–855 (681)         9–22 (15.5)         1.9–3 (2.45)

 Table 3.7: Mechanical properties of natural fibres (average value between parenthesis)


As show in the tables 3.6 and 3.7, the most relevant properties of natural fibers are
gathered to give an overall overview of the main available products on the market. Starting
from the density values it shows that bamboo has lowest value, while abaca, pineapple,
hemp and ramie have the highest values among the bio-fibers. Diameter can be another
important aspect for the mechanical resistance, jute and coir exhibit the lowest average
values, while ramie and bamboo have the thickest fibers. Regarding the tensile strength
the best results are exhibited by flax, hemp, ramie, pineapple, sisal and banana. Moreover,
ramie, pineapple and flax confirm their good mechanical properties with higher Young’s
modulus values, on the other side fibers such as coir and cotton exhibit low stiffness
values. Another important aspect to be addressed is the elongation at break, in this
case coir shows the best value with respect to all the others fibers. As already explained,
moisture represents one of the major threats for the stability of the mechanical properties,
fibers such as sisal, coir, banana, flax and hemp are able to achieve remarkable results,
while cotton does not reach adequate results.
3| Natural composite materials                                                            53


It becomes obvious that from these analyses the promising fibers can be identified as
bamboo, banana, hemp, flax, jute and ramie. Although the good mechanical features,
both banana and bamboo fibers are not suitable for energy absorbing application due to
their poor fiber length, which unlikely will be higher than the critical fiber length value.
Ramie can represent a valid solution, but due to the limited regions of production an
adequate availability cannot be offered, in addition expensive pre-treatments are required
with respect to the other bast fibers. Hence, flax, hemp and jute are the most interesting
products available on the market.

Flax fiber is one of the oldest fiber crops in the world, an increasing interest about this
plant has grown through the last years due to their mechanical features such as low
density, relatively high toughness, high strength and stiffness. It is worth noting that flax
has specific tensile properties greater than E-glass fiber. Hemp fiber is another interesting
solution, it belongs to the cannabis family and it is an annual plant that grows in many
areas of the world. It is characterized by excellent mechanical features and the availability
is guaranteed by an advanced supply chain due to their current use in the textile industry.
Jute fiber is obtained from plants of the genus Corchorus, which includes about 100
species. Jute has remarkable features such as high aspect ratio, high strength to weight
ratio and good insulation properties. Fabric and fiber forms can be easily produced, which
establish this plant as a valid solution for several applications [29].




                    Figure 3.6: Macroscopic detail for each fiber type


Eventually, the crashworthiness features of these fibers have been investigated, unwoven
hemp exhibits an SEA value of 54.3 J/g comparable with carbon fiber (55.7 J/g). While
woven flax had a SEA of 48.5 J/g and woven jute 32.6 J/g [20]. However, a fundamental
aspect should be considered: the fiber volume fraction (VF) content. It must be high-
lighted that hemp samples exhibit the highest fiber VF (43.51–52.52%), while flax and jute
have lower values. In detail, jute has the lowest one with a VF content of 30.27–31.6%.
From this study is emerged that an increasing of VF in the composite leads to highest
54                                                    3| Natural composite materials


values of SEA. Hence, it appears reasonable to expect better performance both from flax
composite and jute composite materials.




                 Figure 3.7: Polylactic acid (PLA) in raw material form


Alternative solution to synthetic matrices were found in bio-polymer matrices, which are
mostly renewable and biodegradable. Some of the natural matrices are obtained in form
either of polysaccharides such as gelatine and starch or as protein such as collagen and
soy protein. Other formulations include polyester such as polyvinyl acetate, polyvinyl
alcohols, polybutylene succinate (PBS), polyhydroxybutyrate-co-valerate (PHBV), poly-
hydroxybutyrate (PHB) and polylactic acid (PLA). PHBV are produced by a wide range
of microorganisms, their appeal is due to their good mechanical properties comparable
to those of traditional thermoplastics such as polyethylene and polypropylene [21]. Al-
though the good features their high costs hinder the growth of their popularity in the
market. PLA is one of the most popular bio-based polyester employed in the market. It
is a thermoplastic matrix and its basic component is lactic acid which derives from the
fermentation of corn starch. In general, it is used for non-structural applications such as
casings of electronic products, interior parts of automobiles. Additionally, several tests
show that PLA is suitable for embedding fibers in composites. Soy protein is obtained
from soybean and represent the least expensive and one of the most widely available ma-
terial in the world. The matrix obtained from these proteins has many befits such fire
retardant, vibration damping, remarkable impact strength, gas barrier, water resistance.
Moreover, bending, torsional and tensile deformations can be tolerated without visible
damages, thanks to their ductile behavior. Eventually, Protein-based matrix contains
3| Natural composite materials                                                          55


polar groups which allow for the strong bonding between matrix and fibers, thus good ad-
hesion can be achieved. As drawbacks, only non-structural applications can be performed
with protein-based matrices.

In conclusion, in order to perform the experimental tests phase the most suitable materials
for crashworthiness application must be chosen. As reported, either hemp, jute or flax
are valid solutions, but the most encouraging and easily achievable appears to be flax
fiber solution. Regarding the filler matrix, the natural solutions presented are unable
to guarantee the required mechanical features. As a consequence, a thermoset matrix
is needed to obtain remarkable results. In particular, epoxy resin is selected due to its
low density, low viscosity, high strength, good mechanical characteristics and chemical
stability [10].
                                                                                        57




4 | Material Characterization
In this chapter all the required activities to perform a complete material characterization
will be analyzed. In detail, the first section will be presented so as to provide as much
information as possible about the used material and the manufacturing procedure to
which it was subjected. Then, the experimental activities will be subdivided in two
major sections: static tests and dynamic tests. The latter aim to analyze the dynamic
features of the materials, while the first activities are performed to obtain the material
characteristics in terms of elastic constants and strength-related parameters.




                    Figure 4.1: Detail of an ampliTex™ 300 laminate



4.1.     Samples manufacturing
The selected natural composite material is a flax-based fiber product called ampliTex™
obtained through the collaboration between Bcomp and Angeloni Group.
58                                                       4| Material Characterization




                (a) Mold plates                         (b) Drawing phase




     (c) Prepregs on mold                           (d) Molds laid on breather




                            (e) Vacuum bag placed in autoclave

           Figure 4.2: Production phases of flax composite laminates
4| Material Characterization                                                            59


In particular, ampliTex™ 300 twill 2/2 prepreg was employed to fabricate the required
samples. The fabric is bidirectional with fibers oriented at 0° and 90° with a density of
1.33 g/cm3 . In order to obtain the prepreg product the dry fibers are chemically treated
to increase the compatibility with both epoxy and polyester resins. In order to achieve the
best mechanical performances epoxy-based prepreg was employed. in particular the used
epoxy resin was IMP 503ZHT BC, which is particularly suitable for composite natural
materials.

To produce the flax composite specimens the manufacturing procedure presented in sec-
tion 2.2.8 was accomplished. As show in figure 4.2b, the first step consists in drawing
the lamina shape on the prepreg sheet and for each sketched layer both the upper side
and zero direction must be marked in order to prevent any mistakes. As shown in figure
4.2a, the employed molds were simple metal plates, both molds and counter-molds were
required to achieved an high-quality surface. At this stage, the realise film were applied
only on molds in order to protect the surface. Then, the adequate sized prepreg layers
were carefully laid on the release film, following the proper stacking lamination sequence.
Another important purpose of the micro-perforated film is to ensure that all trapped air
can be properly removed, so as to ensure perfect adhesion between the plies (see figure
4.2c). To guarantee the temperature control during the autoclave cycle a thermocouple
is installed on the mould. Thereafter, the structure is positioned in between a breather
layer which has the function to absorb all the excess resin and promotes the air transfer
from the prepreg towards the outlet valves. Eventually, the prepreg is laid in a sealed
vacuum bag equipped with valves (see figure 4.2e).

The following step consists in pumping out all the air from the vacuum bag, to assure
this is essential to minimize the amount of wrinkles present on the bag, hence an high
competence is required to fulfill such task. At least 10 minutes are required to guarantee
the complete debulking procedure. After this phase the prepreg can be placed inside
the autoclave where not only the vacuum condition is maintained, but also a controlled
increasing both in temperature and pressure are applied inside the chamber. In detail,
the employed autoclave is produced by Maroso, the latter is characterized by a capacity
of 3315 l, a maximum pressure of 12 bar and a maximum temperature of 250 °C. As show
in the graph 4.3 the pressure and temperature are reported over the time. In the first
phase the temperature is increased up to 80 °C in about 30 minutes. In the second stage
the temperature is maintained constant while the pressure is set to ambient pressure.
As shown by the thermocouples measurements, almost 2 hours are need to reach the
set temperature and guarantee a complete temperature homogenization of the prepregs.
During the third phase, an increasing both of pressure and temperature is performed,
60                                                      4| Material Characterization


especially the temperature value is raised to 130 °C, while the pressure is set to 6 bar,
the time required to reach such condition is 30 minutes. In the last phase both value of
pressure and temperature are maintained constant so as to allow the resin to reflow and
cure, guaranteeing a complete expulsion of the air from the laminates and homogenization
of the prepreg temperature. After 60 minutes the temperature is gradually reduced,
whereas the pressure value is kept at operating value for at least 90 minutes in order to
assure the complete polymerization of the epoxy resin.




                         Figure 4.3: Autoclave cycle parameters


At the end of the procedure three different laminates were obtained, two of them were
characterized by a 6 plies layout, whereas the third laminate has a greater thickness due
to the 8 plies layout. The latter will be employed for the realization of the shear test
samples. The cutting procedure is the last phase, in order to accomplish such task the
ProtoMAX abrasive waterjet cutter was employed. This technology offers the possibility
to achieve precise cut, on the other hand the usage of water can be an issue for natural
composites as explained in section 3.1. For this reason, the achieved specimens must be
dried by means of a industrial oven. The set heating temperature must be limited to 60
°C so as to stay well below the glass transition temperature (Tg ) and avoiding the damage
of the fibers.
4| Material Characterization                                                      61




                   Figure 4.4: ProtoMAX abrasive waterjet cutter


It is worth noting that the Tg of the flax composite laminates was determined through
the dynamic mechanical analysis (DMA) performed in the Impregnatex (Angeloni Gruop)
laboratories.




           Figure 4.5: Dynamic mechanical analysis of 8-layered composite
62                                                         4| Material Characterization


As shown in the graph 4.5, the DMA results of the least thick laminate are reported. In
detail, storage modulus (E ′ ) represents the elastic portion, loss modulus (E ′′ ) represents
the viscous part and δ represents the phase lag between stress and strain and can be
defined as: δ = arctan(E ′′ /E ′ ). From the storage modulus is possible define the Tg value
that appears to be 120.8 °C. However, it must be noted that changes in the physical
features are exhibited from about 75 °C, as shown by the small changes in the slope of
E ′′ . Hence, a precautionary limit heating temperature is set at 60 °C.


4.2.      Static tests
Static tests are performed in a condition where all the dynamic effect are minimized,
especially inertia forces. Since a small velocity component will be always present in this
test typology, it is unfeasible to apply forces at a zero-velocity condition. For this reason,
the tests are defined as "quasi-static". This does not represent a threat for the consistency
of the results, on the condition that the loads are applied in order to be sufficiently slow to
neglect the inertia forces. American Society for Testing and Materials (ASTM) standards
are considered so as to define aspects such as the size specimens, testing procedures and
calculus procedures. In this way, repeatability and consistency of the results can be
assured, providing reliable test.

The static tests selected to conduct the material characterization are:

     • ASTM D3039 Tensile test

     • ASTM D6641 Compression test

     • ASTM D3518 Shear test

     • ASTM D790 Three-point bending test

As reported in section 2.3, these tests represent the lowest level of the building block
approach. In order to achieve an all-round knowledge of natural composite materials a
strict procedure must be followed so as to provide an adequate level of characterization.
The latter requirement is essential to move towards the upper level: the lamina/laminate
level testing phase. It is worth noting that thermo-physical features of the material can be
very important to determine the behaviour of a component in different working conditions,
testing activities such as moisture absorption, void volume, etc. can represent a basic step
in the testing campaign.

However, this thesis work aims to characterize the mechanical features of the material and
thus the testing will be limited to such activities. ASTM standards assure the statistical
4| Material Characterization                                                          63


validity of the tests, since at least five samples must be tested for each type of test.
However, an increase number of specimens, derived from at least three different batches,
can be used in order to obtain even more consistent results. Although the good outcomes,
the latter methodology may increase the general costs related with the manufacturing
process, as a consequence the minimum number of required specimens was employed to
perform the tests of this project. Lastly, environmental conditions and sample conditions
may represent a relevant source of uncertainties. In order to increase repeatability, an
industrial oven was employed before each test. Samples were heated up to 60 °C for at
least 2 hours so as to dry them and guarantee the least amount of moisture content. In
this way specimens can be tested under the same conditions regardless of environmental
conditions.


4.2.1.    Testing equipment
In order to perform static tests two different machines were employed: MTS 858 Table
Top System for bending test and MTS 370.10 Elastomer System for all the remaining
type of tests (see figure 4.6).




                  (a) MTS 858                       (b) MTS 370.10

                     Figure 4.6: Employed material testing system


The data were collected directly from the machines, both of them are able to return
64                                                      4| Material Characterization


applied load and crosshead displacement. The latter does not allow for an accurate
measurement of the strain value, hence some of the specimens were equipped with strain
gages. In particular, two models were used: the biaxial KYOWA KFGS-3-350-D16-11
and the uniaxial KYOWA KFGS-3-350-C1-11. The former was used to perform tensile
and shear tests, whereas the latter was employed for compression test. In addition, the
axial extensometer MTS 634.31F-24 was used to guarantee the results consistency.


4.2.2.      Tensile test D3039
This test method is designed to produce in-plane tensile properties of polymer matrix,
fiber-reinforced composite materials. Thin flat specimens of material with a constant
rectangular cross-section are mounted in the grips of a mechanical testing machine and
axially loaded in tension until failure, as proscribed by the ASTM D3039 rule. The
recorded data are used to determine the stress-strain response of the material and others
fundamental information such as:

     • Ultimate tensile strength

     • Ultimate tensile strain

     • Tensile chord modulus of elasticity

     • Poisson’s ratio

     • Transition strain

The employed specimens and their sizes are reported in table 4.1. A digital caliper with
a resolution of 0.01 mm and an accuracy of 0.03 mm were used to take all the measures.
Samples were measured in three different points, then the average values were obtained
for each dimension. The specimens names are reported as: "material name_fibers ori-
entation_specimen number", for example, "APX300_0_1" identifies sample number 1,
made of ampliTex 300 with 0-degrees fiber orientation. This nomenclature can be used
even with woven fabric composites, ideally warp and weft directions should exhibit the
same mechanical features. However, due to manufacturing process, the warp direction
(0°) tends to show slightly better performance than weft direction (90°). Hence, fibers
orientation must be considered during test procedure.

The test setup is presented in figure 4.7. As shown the sample is characterized by both
the presence of the biaxial strain gage and the extensometer. The specimen is directly
clamped in at both ends by the wedge grips. The load can be properly transferred due to
the presence of coarse emery cloth, thus the presence of tabs is not required to perform
4| Material Characterization                                                     65


such test.




                              Figure 4.7: Tensile test set-up


         Specimen ID       Length (mm)       Width (mm)         thickness (mm)
             APX300_0_1         251.07            24.97              2.34
             APX300_0_2         250.18            24.98              2.36
             APX300_0_3         250.12            25.01              2.32
             APX300_0_4         251.21            25.03              2.32
             APX300_0_5         250.06            25.02              2.36
             APX300_0_6         249.93            25.02              2.36
             APX300_0_7         249.73            25.01              2.33
             APX300_0_8         250.14            25.06              2.32
         APX300_90_1            251.15            25.00              2.36
         APX300_90_2            249.91            24.99              2.32
         APX300_90_3            250.88            25.01              2.35
         APX300_90_4            250.04            24.97              2.36
         APX300_90_5            250.03            25.01              2.34
         APX300_90_6            251.22            24.99              2.36

                          Table 4.1: Tensile test specimens sizes
66                                                        4| Material Characterization


Once the tests are completed the data are organized so as to obtain the stress-strain
curve, the latter represents a fundamental outcome from which many observations and
parameters can be extrapolated. The ultimate tensile strength is one of them, it can be
easily achieved from the expression:


                                      σmax = Fmax /A                                   (4.1)

Where σmax represents the ultimate tensile strength, Fmax the maximum applied forced
recorded by the machine and A is the cross-sectional area of the specimen. The value of
the strain can be performed considering three different measurements:

     1. Crosshead displacement measure

     2. Extensometer measure

     3. Strain gage measure

The strain measure from the crosshead displacement require some manipulation to be
obtained. The acquired data from the machine is in form of displacement, whereas the
required result is in the form of a strain. In order to achieve such value the definition of
strain can be applied:
                                         ϵ = ∆l/l0                                     (4.2)

Where ϵ is the strain, l0 represents the gage section length and ∆l is the crosshead
displacement that comes directly from the acquired data. The gage section describe the
part of the specimen between the wedge grip of the machine. However, by considering
this definition an important assumption is made: no slippage condition inside the grips.
From the graph 4.8 it can be seen that the crosshead strain, for the same value of stress,
is higher with respect to the others strain measures. From this observation, it can be
deduced that the approximation of no-slip condition is not valid in most of the cases,
as a consequence, this strain value may be used for qualitative evaluations. In addition,
from the graph a discrepancy between the strain measures obtained from strain gage and
extensometer can be seen. In particular, the extensometer strain value is overestimated,
the reason is related with two aspects. Firstly, the device is not rigidly connected to the
specimen and, additionally, the possible presence of human errors during the setup phase
can be a source of uncertainties as well. Hence, the strain gage measure represents the
most accurate value of the strain.
4| Material Characterization                                                               67




                              (a) Stress-strain curve APX300_0_2




                             (b) Stress-strain curve APX300_90_2

                        Figure 4.8: Stress-strain curve comparison


The results of the tensile test are reported for both the 0° oriented samples and 90° oriented
samples in the table 4.2 and figure 4.9. The tested material is a woven fabric, but it worth
noting that a difference in the mechanical performances between the two fibers directions
can be observed. In particular, the the 0° oriented samples show better ultimate tensile
stress. The reason for such behaviour can be associated with the manufacturing process
68                                                        4| Material Characterization


to produce prepregs, the fibers in the warp direction are maintained straight and pulled
during the process, whereas the fiber in the weft direction are bent, thus lower mechanical
performance are generally achieved.




                             (a) Stress-strain curve APX300_0_x




                            (b) Stress-strain curve APX300_90_x

                      Figure 4.9: Stress-strain curve for tensile test


The Poisson’s ratio is calculated from the measure of the axial strain and transverse strain
acquired by the strain gage sensor, the interval for the calculation is in between 1000µϵ
4| Material Characterization                                                              69


and 3000µϵ, as prescribed by the standard. The expression use is:


                                        ν = −ϵ⊥ /ϵ||                                    (4.3)


As expected for fabric composites, the results obtained for both fibers orientations are
similar, but it must be highlighted that the result for 0° oriented samples has a high
variance value. In order to verify the outcome, the relationship Eν12  11
                                                                          = Eν21
                                                                              22
                                                                                 can be used,
thus the calculated Poisson’s coefficient ν12C results equal to 0.15. This consideration
confirms the less accuracy of the ν12 experimental outcome, which should be closer to
calculated coefficient. So as to justify such high variance value, the sample APX300_0_5
should be considered due to its low Poisson’s ratio equal to 0.08. In fact, if the latter
sample is not assessed a drop in standard deviation larger than 12% is show and a Poisson’s
ratio closer to 0.15 value is reached. The elastic modulus outcomes show consistent data
with low value of variance. In this case the formula to obtain this parameter is:


                                        E = ∆σ/∆ϵ                                       (4.4)


As with the Poisson’s ratio, the interval for the calculation is provided by the standard
and is always in between 1000µϵ and 3000µϵ.

                          Avarage value    Std. Dev.      Coeff. of variation (%)
                                        APX300_0
       σ1_max (MPa)           181.39           5.84                  3.22
         E1 (GPa)             17.73            0.46                  2.62
         ϵ1_max (%)            1.28            0.04                  3.14
             ν12               0.13            0.06                  45.62
       ϵ1_trasition (%)        0.35            0.004                 1.01
                                       APX300_90
       σ2_max (MPa)           161.69           7.30                  4.52
         E2 (GPa)             17.87            1.45                  8.11
         ϵ2_max (%)            1.15            0.23                  20.23
             ν21               0.15            0.01                  7.57
       ϵ2_trasition (%)        0.31            0.08                  26.25

                          Table 4.2: Tensile mechanical properties
70                                                        4| Material Characterization




                         (a) Transition strain point for APX300_0_2




                        (b) Transition strain point for APX300_90_2

                          Figure 4.10: Transition strain points


So as to determine the transition strain point two linear stress functions were generated
starting from the longitudinal stress function. As show in the figure 4.10, the linear
functions are tangent to the two ends of the longitudinal stress function. In order to
determine the left end linear function a strain range between 100µϵ and 2000µϵ was
taken, the starting point was selected other than zero so as to obtain a more consistent
4| Material Characterization                                                             71


result. The right end linear function was generated considering an interval in between
8000µϵ and 11000µϵ, if the fail occurs before 11000µϵ, the ultimate strain value is selected
as maximum limit of the range.

Eventually, failure mode examination is the last step to obtain a whole evaluation of the
experimental test. So as to validate the test an understanding of location and type of
failure must be performed. In this case, the APX300_0_x samples shown homogeneous
results and the failures always occurred within the gage section. On the other side, the
samples with weft oriented fibers did not always exhibit compliant failure. For example,
althogh the specimen APX300_90_2 shows results consistent with the others, the failure
occurs inside the wedge grip. In addition, sample APX300_90_5 shows lower mechanical
performances, presumably due to the presence of flaws inside the material. Further details
of failures are shown in appendix A.


4.2.3.    Shear test D3518
The in-plane shear response of polymer matrix composite materials is ruled by ASTM
D3518 standard. The set-up procedure is similar to test method D3039 applied for tensile
tests, the differences are both in samples stacking sequence and sizes. In detail, a ±45°
balanced and symmetric laminate, characterized by greater thickness, is employed to in-
vestigate mechanical response. During the evaluation of the final results must be taken
into consideration the free-edge effect. As mentioned in 2.1.6, the in-plane normal stress
component, combined with the ±45° oriented plies layout, lead to a complex stress field
near the free-edges. In particular, a three-dimensional stress field is achieved and CLT
cannot be employed to predict such behaviour, since out-of-plane component is not consid-
ered. Considering the complexity in investigating such test outcomes, through the years
many procedures were developed. The first version of the shear test method was presented
by Petit [26], then Rosen [30] improved it obtaining the current test methodology.

         Specimen ID       Length (mm)        Width (mm)        thickness (mm)
         APX300_45_1            249.96             25.03               3.12
         APX300_45_2            249.59             25.02               3.15
         APX300_45_3            250.03             25.02               3.17
         APX300_45_4            250.97             25.03               3.17
         APX300_45_5            250.03             25.07               3.17
         APX300_45_6            249.66             25.01               3.17

                          Table 4.3: Shear test specimens sizes
72                                                          4| Material Characterization




                               Figure 4.11: Shear test set-up


From the in-plane shear stress versus shear strain chart, information such as shear modu-
lus, maximum shear stress and maximum shear strain can be achieved. In order to draw
such graph, in-plane shear stress can be defined as τ12 = Fx /2A, where F is the applied
force and A is the section area. While, the shear strain can be described as γ12 = ϵx − ϵy ,
where ϵx and ϵy are respectively the longitudinal and transverse strains measured by the
biaxial strain gage sensor applied on the specimen. It must be noted that the subscripts
1,2 represent the lamina directions, whereas x,y are referred to laminate directions.

In order to calculate the shear modulus of elasticity the following equation can be used:

                                                  σx
                                      G12 =                                              (4.5)
                                              2(ϵx − ϵy )

With σx is the longitudinal stress term calculated as the ratio of applied force to the cross-
section of the sample. The shear strain range of 2000 to 6000 µϵ is selected to perform
the calculus. This interval is obtained considering the normal strain range used for tensile
test D3039, if ±45° sample is employed a Poisson’s ratio near to 1 can be assumed, thus
the selected range for shear test corresponds approximately to the normal strain range
of 1000 to 3000 µϵ used for tensile test. The ultimate in-plane shear stress is achieved
considering the maximum load at or below 5% shear strain. If a maximum stress value is
recorded with a corresponding strain value greater than 5%, the maximum shear stress is
taken at 5% of the shear strain. The specimen APX300_45_3 shown this behaviour and
4| Material Characterization                                                           73


its maximum stress value was discarded because at 5.5% of shear strain. So as to obtain
the ultimate shear strain, the value at the corresponding ultimate shear stress, within 5%
of shear deformation, was considered. The outcomes are presented in table 4.4.

                        Avarage value      Std. Dev.     Coeff. of variation (%)
                                       APX300_45
      τ12_max (MPa)          46.21            0.46                  0.99
        γ12_max (%)           4.71            0.25                  5.29
        G12 (GPa)             1.96            0.06                  2.89

                         Table 4.4: Shear mechanical properties


It is worth noting that the upper limit of the engineering shear strain defined at 5% is
not accidental. The above mentioned issues, in addition with large deformation effect
(fibers rotation or scissoring) and the total thickness effect can alter the measurements,
hence producing non-compliant results. Eventually, though failures occur always within
the gage section, the specimen APX300_45_3 shown lower mechanical performances.
Such behaviour can be explained considering the presence of defects and voids inside the
material or due to an incorrect application of the strain gage sensor.




                      Figure 4.12: Stress-strain curve for shear test
74                                                        4| Material Characterization


4.2.4.    Bending test D790
Out-of-plane properties can be defined through bending test method in according with
ASTM D790 standard. The test is performed through a 3-point-bending machine, in
detail the setup is presented in figure 4.13. The specimen is simply supported by two
steel cylinders with a diameter of 15 mm and is loaded by means of a third cylindrical
loading nose midway between the supports.




                            Figure 4.13: Bending test set-up


         Specimen ID       Length (mm)       Width (mm)        thickness (mm)
         APX300_0_1            120.02             14.93               2.33
         APX300_0_2            120.02             14.95               2.28
         APX300_0_3            119.92             15.34               2.34
         APX300_0_4            119.16             14.97               2.30
         APX300_0_5            119.13             14.97               2.34
         APX300_0_6            119.17             14.96               2.32
         APX300_0_7            119.95             14.93               2.31
         APX300_0_8            119.15             14.98               2.34

                         Table 4.5: Bending test specimens sizes


In order to guarantee a failure in the outer surface of the specimen, a support span-to-
depth ratio of 32:1 was chosen to perform the test. In detail, the average thickness of the
4| Material Characterization                                                           75


specimens is 2.35 mm, thus the obtained span value is 75 mm. The first flexural feature
that can be achieved is the flexural stress, below the general equation is reported:


                       σf = (3F L/2bt2 )[1 + 6(D/L)2 − 4(t/L)(D/L)]                  (4.6)

Where:

   • F is the applied force

   • L is the span distance

   • b is the specimen width

   • t is the specimen thickness

   • D is the loading nose vertical displacement

The equation 4.6 was employed due to the high span-to-depth ratio selected. Significant
end forces are developed at the supports when relatively large deflection occurs, this can
affect the moment in a simple supported beam. In the latter equation these terms are
considered through correction factors. Due to the orthotropic nature of flax composite
fabric, shear deflection may seriously reduce the apparent modulus of elasticity, hence
tangent modulus was considered. The following formula was considered:


                                       EB = L3 m/4bd3                                (4.7)


The parameter m represents the slope of the tangent to the initial portion of the load-
deflection curve. As in tensile test, a range in between 1000µϵ and 3000µϵ was defined to
perform the calculus. In table 4.6 the most relevant results are reported.

                         Avarage value     Std. Dev.    Coeff. of variation (%)
                                         APX300_0
       σf _max (MPa)          199.80          12.40                  6.21
         ϵf _max (%)           1.86            0.12                  6.58
         EB (GPa)             15.95            0.44                  2.74

                         Table 4.6: Flexural mechanical properties
76                                                      4| Material Characterization




                 Figure 4.14: Force-displacement curve for bending test




                    Figure 4.15: Stress-strain curve for bending test


It is worth noting that the specimen was able to carry a portion of the load even af-
ter reaching the maximum stress peak, thanks to the undamaged plies in the laminate.
Eventually, a step descending trend can be observed in figure 4.15. Lastly, all the tested
samples were able to fail in compliance with the standard. As a verification a low value
of variance can be noted from the results.
4| Material Characterization                                                          77


4.2.5.    Compression test D6641
This test method determines the in-plane compressive properties of natural composite
materials by means of a combined loading compression test fixture. The used ASTM
D6641 standard applies the compressive load on the specimen through a combination of
shear and axial forces. In this way instability is prevented, with respect to test method
D3410 where a pure shear-loading is used. The most relevant compressive features of
the material are ultimate compressive strength and compressive modulus of elasticity.
The test method setup is similar to tensile test method, but with a loading acting in
compression. The specimen geometry reported in table 4.7 are in compliance with the
standard, but a larger value of thickness could have been employed so as to minimize
instability phenomena (or Euler column buckling) during the test. However, the latter
phenomena was taken into consideration during the selection of a suitable gage section
value. Thanks to this, the provided samples were able to give consistent results while
avoiding the instability phenomena.

         Specimen ID       Length (mm)      Width (mm)        thickness (mm)
         APX300_0_1            140.01            16.09              2.34
         APX300_0_2            139.75            16.09              2.31
         APX300_0_3            139.88            16.07              2.31
         APX300_0_4            139.76            16.06              2.31
         APX300_0_5            139.99            16.10              2.36
         APX300_0_6            140.00            16.10              2.36
         APX300_0_7            139.95            16.04              2.34
         APX300_90_1           140.06            16.06              2.36
         APX300_90_2           140.06            16.07              2.36
         APX300_90_3           140.08            16.07              2.34
         APX300_90_4           140.05            16.12              2.35
         APX300_90_5           140.00            16.07              2.33
         APX300_90_6           140.02            16.08              2.29
         APX300_90_7           140.06            16.10              2.35
         APX300_90_8           140.02            16.10              2.34

                      Table 4.7: Compression test specimens sizes
78                                                            4| Material Characterization


In table 4.8 the outcomes are presented. In particular, the compressive modulus of elas-
ticity was obtained through the equation 4.4, used for tensile, and a range in between
1000 µϵ and 3000 µϵ were used. In order to evaluate the strain value and guarantee the
control of the induced bending, two axial strain gages were employed on both the surfaces
of the specimen. In detail, the following percent bending equation were used:

                                              ϵ1 − ϵ2
                                      By =            × 100                                (4.8)
                                              ϵ1 + ϵ2

This parameter can be affected by imperfections in test specimen, test fixture, or even
testing procedure. During the evaluation of the modulus, values no greater than 5% were
reached, this result allows the test to be considered valid, as the maximum admissible
value is 10%. Eventually, the evaluation of the strain consists in an average between the
measurements given by the two sensors applied on both sides. By means of equation 4.1
the ultimate compressive stress value can be evaluated, comparable results were achieved
both for 0° and 90° oriented samples.




       (a) Front view of compressive sample          (b) Side view of compressive sample

                Figure 4.16: Strain gages layout of compressive specimen
4| Material Characterization                                                           79




                             (a) Elastic modulus APX300_0_x




                             (b) Elastic modulus APX300_90_x

         Figure 4.17: Graphical representation of elastic compressive modulus


This test method is very sensitive to specimen geometry, manufacturing defects, fiber ori-
entation and improper alignment. From failure mode analysis it is possible to understand
if some of these aspects have altered the in-plane compressive features. From appendix
A, the samples show through-thickness failures limited to gage section , which means that
compliant test have been performed. Lastly, it is worth noting that no explosive failure
80                                                         4| Material Characterization


were observed, which is an essential aspect in the context of crashworthiness applications.

                          Avarage value      Std. Dev.     Coeff. of variation (%)
                                         APX300_0
        σ1_max (MPa)            141.57          5.10                   3.61
           E1 (GPa)             15.04           0.69                   4.60
                                         APX300_90
        σ2_max (MPa)            141.53          0.85                   1.00
           E2 (GPa)             15.02           0.10                   0.69

                        Table 4.8: Compressive mechanical properties



4.3.       Dynamic tests
During design procedures the mechanical performance obtained from static tests are as-
sessed in order to properly sizing structural components for the harshest loading condi-
tions. However, during design phase dynamic properties may be important as well. As-
pects such as weight reduction can be optimized and crash phenomena (e.g. bird strike)
can be properly evaluated during this stage so as to minimize structural failure. In order
to evaluate the dynamic response of flax composite material three tests were performed:

     • Strain rate sensitivity test

     • ASTM D7136 Indentation test

     • High-velocity impact test




           (a) Data acquisition system                 (b) High-speed camera layout

                             Figure 4.18: Data acquisition devices
4| Material Characterization                                                             81


In order to measure strain rate, the standard ISO 8256:2004 recommendations were con-
sidered, but not fully implemented. In particular, the specimens geometry was modified
so as to maximize the number of tests and analyse the response with different cross sec-
tions. This choice has allowed to maintain low manufacturing costs, while ensuring the
consistency of the test. Low-velocity impact test was conducted, in according to the
ASTM D7136 standard, so as to verify the impact resistance of flax laminates. For the
same reason high-velocity impact test were performed as well, in this case no standard
were applied. Eventually, the failure modes and behaviour of natural composites was
investigated.




                         Figure 4.19: Step Lab DW1000 system


Both the indentation and strain rate tests were performed exploiting the Step Lab DW1000
drop weight tower functionalities (see figure 4.19). Information such as impact load,
velocity and energy were provided directly from the machine. All the data are acquired
with a sampling frequency of 3MHz and then a filter of 50 kHz is applied. Additionally,
some specimens of the strain rate test were equipped with uniaxial strain gages, in order to
82                                                         4| Material Characterization


accurately compare stress-strain dynamic behaviour with static results. So as to perform
the ballistic test the gas gun reported in figure 4.20 was employed. Lastly, high-speed
Phantom VEO-E 310L cameras were used, for both strain rate and ballistic tests, in order
to measure the input and output velocities, capture the details during the failure stages
and validate the tests.




      (a) Barrel tip with sabot stopper         (b) Barrel base attached to pressure vessel

                                  Figure 4.20: Gas gun set-up



4.3.1.     Strain rate sensitivity test
This test aims to investigate strain rate dependency of flax fiber composite material. In
order to execute the test the specimen is clamped in the lower grip, which is free to
move, then the upper part is clamped to the machine-integrated grips. It is important to
highlight that specimens are devoid of tabs, however, to guarantee a correct distribution
of the load over the clamped area, both emery cloth and aluminium plates were applied
between the sample and the grip, as shown in figure 4.22. So as to provide the tensile
dynamic load a weight of 12.85Kg is applied on a sled, the latter is released from a certain
height in order to impact the lower end of the specimen. The maximum impact velocity
depends on the maximum height reachable by the machinery, while the maximum energy
is bounded with the used weight. Although these limits, both suitable value of energy
and velocity have been obtained during the test. In fact, due to the relatively small
cross-sectional area the failure of the samples have always been guaranteed.
4| Material Characterization                                                         83




                          Figure 4.21: Strain rate test set-up




                            Figure 4.22: Lower grip set-up


The geometry of the employed samples is reported in table 4.9, the specimens are fab-
ricated using woven fabric prepreg with 0° oriented fibers (warp direction), in order to
inspect the greatest mechanical performances.
84                                                           4| Material Characterization


Strain rate is defined as the variation of strain over the time, it represents the sensitivity of
material characteristics with respect to the deformation velocity. In general, the materials
tends to exhibit an increase of mechanical properties such as ultimate stress, ultimate
strain and Young’s modulus. This aspect can be taken into consideration during design
phase so as to optimize the mass distribution. In order to obtain strain rate values the
following equation was used:
                                         dϵ     1 dL      v
                                    ϵ̇ =     =        =                                     (4.9)
                                         dt    L0 dt     L0
Where v is the impact velocity of the sled and L0 is the gage section of the specimen.
By means of these parameters a wide strain rate range can be considered to perform the
tests. This dynamic evaluation aims to verify whether the flax composite material shows
an increasing of mechanical performances with an increasing of strain rate.

          Specimen ID          Length (mm)        Width (mm)         thickness (mm)
          APX300_0_1                164.93              9.41                 2.35
          APX300_0_2                164.94              9.41                 2.37
          APX300_0_3                164.92              9.40                 2.37
          APX300_0_4                165.00              9.39                 2.33
          APX300_0_5                164.89              9.38                 2.33
          APX300_0_6                164.77              9.39                 2.33
          APX300_0_7                165.15              9.38                 2.34
          APX300_0_8                165.05              9.39                 2.35
          APX300_0_9                164.88              9.43                 2.37
       APX300_0_1_SG                165.04              15.13                2.37
       APX300_0_2_SG                165.00              15.16                2.36
       APX300_0_3_SG                165.05              15.10                2.35
       APX300_0_4_SG                165.03              15.11                2.33
       APX300_0_5_SG                165.07              15.14                2.34
       APX300_0_6_SG                165.05              15.12                2.33

                   Table 4.9: Strain rate sensitivity test specimens sizes


At first, the specimens were tested with a gage section of 40 mm, and the drop height was
continuously modified so as to obtain different strain rate values. From the graph 4.23 the
relationship between stress and strain rate is reported. In particular, the material exhibits
an increasing of more than 22% in stress value for higher strain rate, and a positive trend
is depicted as well. The latter represents a significant aspect, since it is possible to assume
4| Material Characterization                                                                85


that similar behaviour may be exhibited for even higher strain rate values.




                     Figure 4.23: Strain rate effect on ultimate stress




         Figure 4.24: Comparison between static and dynamic tensile response


Modulus of elasticity is another important parameter to verify the strain rate sensitivity
of the material. In the figure 4.24 the stress-strain relationship is reported, this result was
obtained by exploiting the strain gage sensor installed on some samples. A comparison
86                                                        4| Material Characterization


between static result and dynamic is made, in the first half of the graph less steep trend is
shown by the dynamic outcome, on the contrary in the second half the increase of elastic
modulus it is obvious. In detail, The maximum value of the modulus is 21.77 GPa, which
represents an increase of 23% with respect to the static result. The poor results obtained
in the first half can be attributed to slippage phenomena at grips level.

An analysis about the specific absorbed energy (SEA) can be conducted as well. This
parameter can be obtained either as the integral of the force with respect to the displace-
ment or as the difference between the kinetic energy before and after impact. The results
reported in graph 4.25 show an increasing of the energy parameter with higher strain rate.
In detail, the best result achieved value twice as high as in the static case and a positive
trend was identified as well. Although acceptable results were achieved, the use of tabs
may lead to better outcomes with more accurate behaviour.




                      Figure 4.25: Strain rate effect on tensile SEA


Overall, the analysed parameters have exhibited sensitivity to strain rate variation. Lastly,
it is worth noting that the increasing in the mechanical performances is comparable both
for the ultimate stress and Young’s modulus parameters, while for specific absorbed energy
the best improvement was found. This proves the consistency of the achieved results.
4| Material Characterization                                                              87


4.3.2.     Indentation test D7136




                             Figure 4.26: Indentation test setup


Damage resistance of multi-directional natural composite materials is investigated through
the application of ASTM D7136 standard. In order to perform such test a drop tower is
employed with the use of a suitable impact support fixture installed on a rigid base (see
figure 4.26). Toggle clamps with rubber tips are employed to ensure a proper fixation
while avoiding damage to the plate. The test execution is very similar to the strain
rate sensitivity test, but in this case tree different hemispherical striker tips are used as
impactors, so as to ensure low-velocity indentation damage. The weight applied on the
drop tower sled can be seen as the sum of two different parts: a fixed weight of 10.260 Kg
and the weight associated with the selected tip. In detail, in table 4.10 the characteristics
of the hemispherical tips are reported:

           Tip ID      Diameter (mm)        Mass (g)     Impactor mass (Kg)
             D127             12.7            171.0                10.4305
             D16              16.0            242.0                10.5015
             D20              20.0            227.6                10.4870

                    Table 4.10: Hemispherical striker tips characteristics
88                                                     4| Material Characterization


Thus, depending on the utilized tip, the proper value of total weight must be considered
to provide the desired amount of impact energy.




                       Figure 4.27: D20 hemispherical striker tip


         Specimen ID        Length (mm)      Width (mm)       thickness (mm)
        APX300_mix_3            150.31           100.43              4.96
        APX300_mix_4            150.34           100.86              4.94
        APX300_mix_5            150.35           100.79              4.95
        APX300_mix_7            150.42            99.82              4.93
       APX300_mix_14            150.28           100.55              4.93
       APX300_mix_15            150.34           100.32              4.96
       APX300_mix_16            150.40           100.46              4.97
       APX300_mix_17            150.40           100.42              4.96
       APX300_mix_18            150.19           100.54              4.96
       APX300_mix_19            150.22           100.36              4.96
       APX300_mix_20            149.35           100.33              4.96
       APX300_mix_21            151.30           100.19              4.93

                      Table 4.11: Indentation test specimens sizes
4| Material Characterization                                                             89


In table 4.11 the specimens geometry are reported in compliance with the D7136 stan-
dards. A thickness value in between 4mm and 6mm is required to guarantee proper failure
mode. To ensure this requirement the specimens are composed by 12 plies with a stacking
sequence of [(+45/ − 45)/(0/90)]3S , as a consequence a thickness value close to 5mm can
be achieved.

The damage resistance properties generated by this test method are highly dependent
upon several factors such as impactor geometry, impactor mass and impact energy. For
this reasons, for each impactor tip at least three value of impact energy are evaluated. In
table 4.12 the parameters of each test are presented.

         Specimen        Peak           Impact         Deflection     Absorbed
            ID         force (N)    velocity (m/s)      (mm)          energy (J)
                                           D127
             19         2654.27           1.39             5.35            9.98
             21         3081.99           1.73             7.23          15.52
             15         2957.65           2.27             15.18         23.62
                                           D16
             20             -             1.10               -              -
              3         2723.22           1.32             4.89            9.11
             17             -             1.91               -              -
             14         2937.74           2.25             12.16         22.00
             18         2825.29           2.46             17.80         28.42
                                           D20
              4         2731.78           1.43             5.41          10.63
              7         2976.23           1.80             7.32          16.98
             16         3322.66           2.27             10.71         26.47
              5         3370.28           2.65             14.94         34.90

                  Table 4.12: Parameters and results of indentation test


Both force value and the initial impact velocity are directly collected from the machine. In
particular, these are used to calculate the other parameters such as velocity trend, energy
evolution and displacement. The latter cannot be assumed as an accurate value, since
obtained from the integral of velocity over time, which could be affected by some errors.
However, it is worth considering this outcome to perform relative evaluation among the
tested samples and verify the consistency of the results. Although a wide range of impact
velocity is used, the variation of peak force between the higher value and the lower one is
90                                                       4| Material Characterization


within 15%. On the other side, the increasing in terms of absorbed energy is more than
60% for D20 tests, which is in accordance with the increasing of the impact velocity, as
reasonably expected.




Figure 4.28: Peak force in relation to kinetic energy (filled elements represent complete
failures)


The graphs 4.31, 4.30 and 4.29 show the force vs displacement curves relative to the three
types of indentation tests conducted. In general, all the graphs exhibit a linear behaviour
in the first part of the curve, then a limit value is reached due to the occurrence of
delamination phenomena. Successively, a constant or quasi-constant region is shown:
here most of the impact energy is absorbed and other failure modes start to propagate.
It is worth noting that the average values for the applied force are in between 2300 N
and 3500 N for all the outcomes. In particular, the best results are exhibited by the tests
performed with D20 tip and the worst by the tests performed with D16 tip. In the last
part of the graphs two different behaviour are shown: a linear decreasing trend and a
step negative evolution. In the first case the specimen is not completely broken and the
panel does not present any breach. On the contrary, in the latter case the complete failure
of the panel leads to one or more steps, these represent the complete failure of the plies
inside the laminate.
4| Material Characterization                                      91




                 Figure 4.29: Force-displacement curve for D127




                  Figure 4.30: Force-displacement curve for D16
92                                                      4| Material Characterization




                     Figure 4.31: Force-displacement curve for D20


As mentioned, in order to obtain consistent evaluations both complete and incomplete
failures are performed. In detail, for specimens with incomplete breakages a depression
is exhibited in the upper side of the plate, with greater or lesser depth of penetration
depending on the impact energy selected. The underside is characterized by the presence
of splits and cracks, which are typical signs of delamination phenomena. It is worth
noting that for higher impact energy tests splits occur in combined forms (see image
4.32a). Samples with complete failures are characterized by the presence of a gap in the
center of the plate, in this case the most common failure modes are exhibited. With the
naked eye it is possible to observe failure mechanisms such as fiber breakage, fiber pull-
out, debonding and delamination phenomena. Eventually, it is important to highlight
that flax composite samples do not exhibit dispersion of materials following the impact
events.
4| Material Characterization                                                                  93




    (a) Underside of specimen 17 after impact     (b) Underside of specimen 18 after impact

                Figure 4.32: Representative failure modes indentation test



4.3.3.     High-velocity impact test
Ballistic impact test is performed so as to investigate the behaviour of natural composites
under high-velocity impact events. In order to execute the test a gas gun, capable of
reaching 8 bar pressure, is employed (see figure 4.20). Steel spherical bullets, with a
diameter of 18 mm and a weight of 23.7 g, are used to assure the failure of the samples.
The latter are positioned in a suitable support called sabot, which is placed at the base
of the gun barrel, immediately close to the pressure vessel. The sabots are made in teflon
to guarantee a low sliding friction and the use of the components for multiple shoots.
In order to ensure a proper force to the sabot a metal foil with a 0.25 mm thickness is
positioned in between the pressurized vessel and the base of the barrel. In detail, once the
pressure reaches the desired level, a trigger lacerates the metal foil causing an explosive
thrust. Eventually, the composite panel to test is tightened on a fixture through the use
of a proper mounting plate, so as to be aligned with the end of the barrel. The specimens
are the same employed for indentation test, except for the length, which is 2.8 mm shorter,
in table 4.13 the specimen geometry is reported.
94                                                       4| Material Characterization


           Specimen ID       Length (mm)          Width (mm)     thickness (mm)
           APX300_mix_1          122,35             100,82              4,96
           APX300_mix_2          122,34             100,41              4,99
           APX300_mix_6          122,44             100,57              4,95
           APX300_mix_8          122,08              98,74              4,95
           APX300_mix_9          122,46              100,5              4,96
          APX300_mix_11          122,16             100,45              4,95

                    Table 4.13: Ballistic impact test specimens sizes


In order to acquire the impact velocity and the output velocity, two high-speed Phantom
VEO-E 310L camera were employed. For each test at least 3 different measures are
collected so as to minimize the error associated with them. In graph 4.33 and table 4.14
the most relevant results are reported.

 Specimen          Input              output          Absorbed         Percentage
    ID         velocity (m/s)     velocity (m/s)      energy (J)    absorbed en. (%)
      1              92.00                66.67          47.55                 47.48
      2              22.25                  -                -                   -
      6              69.11                39.68          37.88                 67.03
      8              43.22                -8.22          21.31                 96.38
      9             126.16             100.20            69.55                 36.93
      11             64.51                35.47          34.35                 69.76

               Table 4.14: Parameters and results of ballistic impact test


With respect to indentation test the failed specimens do not exhibit a longitudinal evo-
lution of the crack, as reported in figure 4.34, the under side of the sample n.8 shows a
x-shape crack with no loss of debris. In addition, the latter specimen shows fiber break-
age and fiber pull-out due to the generation of high shear and bending stresses in the
non impacted side. For the same reason both n.8 and n.1 samples exhibit delamination
phenomena. On the other side, the remain specimens show a complete failure and the
presence of an hole after the impact. In particular, although the fragmentation of the non
impacted side can be seen during impact event, a limited number of debris were gener-
ated, which is a remarkable result in the context of crashworthiness applications where
the minimization of debris plays a key role. Eventually, it worth noting that the generated
holes have smaller diameter compare to the bullet diameter. This aspect highlight the
4| Material Characterization                                                                 95


elastic properties of material which is able to elastically deform during impact event.




Figure 4.33: Output velocity and percentage absorbed energy in relation to input velocity




    (a) Underside of specimen 1 after impact      (b) Underside of specimen 8 after impact

                  Figure 4.34: Representative failure modes ballistic test
                                                                                         97




5 | Numerical simulation
The last part of this project focuses on numerical modelling of the experimental tests.
In detail, the static tests presented in section 4.2 will be considered so as to probe the
suitability both of the material model and the model parameters choices. As previously
mentioned in 2.4, finite element models are exploited to perform such analysis, the used
software is LS-DYNA. Due to low thickness value with respect to length value of the
employed specimens, transverse shear deformation can be neglected in the evaluation,
hence the use of shell elements appears to be the most effective choice. Lastly, material
card *MAT_058 is considered to model flax composite materials features.


5.1.      Model set-up
As well known, static tests are performed in a quasi-static condition, where the execution
time can be even in the order of the minutes. It must be highlight that the use of LS-DYNA
may bring some issues. Firstly, the software employs a dynamic explicit solver which is
not typically recommended for these quasi-static simulations, secondly a small integration
time-step is required in order to guarantee the stability of the numerical method, which is
unfeasible due to the large time simulation needed for this type of tests. Although these
aspects, the final simulation outcomes can still be considered consistent and reliable, if
both appropriate assumptions and investigations are made. In order to obtain reasonable
computational cost, time simulation can be reduced to some tenth of a second. Despite the
huge reduction of this parameter, quasi-static condition can be still guarantee through
the assumption of low kinetic energy level with respect to total energy. In detail, the
balance equation for a simple system without the presence of dissipation effects is: T otal
Energy = Kinetic Energy + Internal Energy. Where the total energy represents the
whole energy introduced into the system while the internal energy is associated with the
deformation energy. To ensure quasi-static condition, an upper limit value for the kinetic
energy equal to 5% of the total energy is selected. This allow to prevent the achievement of
poor outcomes, while guaranteeing that the majority of the introduced energy is exploited
to deform the specimen.
98                                                             5| Numerical simulation




                                   (a) Energy comparison




                                     (b) Energy ratio

                            Figure 5.1: Energetic validation


Eventually, other energy parameters can be evaluated to assure the validation of the
model. The energy ratio is defined as the ratio between the total energy and the sum
of internal energy with external work applied on the system. If this parameter is close
or equal to 1 consistent results are guaranteed, since energy balance is satisfied and the
model is correctly working. When friction is involved in the simulation a dissipative
5| Numerical simulation                                                                 99


process takes place, the amount of energy spent in this process is measured by the energy
dissipation parameter. It is worth noting that friction is not applied for most of the
simulations, except for bending test model. Eventually, when high deformation occurs,
hourglass energy value is fundamental in the evaluation of results. In this numerical
activity the latter parameter does not represent a threat since fully integrated element
are used.

In table 2.1, the material card 58 and the associated parameters are already presented.
The latter can be divided in: physical and non-physical constants. In detail, the physical
parameters such as ultimate stress, ultimate strain or modulus of elasticity are obtained
directly from the experimental tests. On the other side, the non-physical parameters are
associated with the material behaviour and must be calibrated in order to achieve reliable
outcomes. This activity can be done in different ways, but the most simple and effective
is the trial-and-error methodology, which is particularly suitable in the first phases of
numerical modelling process. The most relevant parameters analysed are:

   • Mesh size: this is not a parameter to be defined in the card, but it is essential in
     strain damage models, since can affect the failure threshold. Several mesh size in
     between 1mm and 10mm are investigated but no sensible changes can be observed.
     Consequently, computational time is chosen as a driver and the selected final mesh
     sizes are in between 3mm and 5mm.

   • SLIM: this parameter controls the behaviour of the stress after which the ultimate
     stress value is reached. It can be assumed in between 0 and 1 and represents a
     percentage. Although several tests are performed with different values, no significant
     changes are observed in composite behaviour, unless for extreme value of 1, which
     resembles a perfectly plastic material. Since brittle behaviour are investigated the
     initial value of 0.1 is maintained.

   • ERODS: it depicts the effective strain to failure parameter. Different values are
     tested to verify changes in failure point in the stress-strain curve. Even in this
     case, no sensitivity is found, which also means that localization problem can not be
     addressed through regularization curve process.

   • SOFT: physical fidelity can be increased through this parameter. In particular,
     crack propagation process is controlled by reducing elements properties adjacent to
     failed element, so as to start the crashfront algorithm. This parameter is omitted
     since, also in this case, no influence in the failure process are observed.

The material card employed to perform numerical activities is depicted in table 5.1:
100                                                               5| Numerical simulation


        MID      1.334E-9      17730     17870        0     0.14      39.75    0.025
        1960        980        1960        0.1       0.1     0.1       0.1       1
       AOPT        1E-9         -0.3       0.9       -1       0        0        0.9
        XP          YP          ZP         A1        A2      A3       0.14      0.5
         V1         V2          V3         D1        D2      D3     BETA      LCDFAIL
      9.412E-3    1.28E-2    9.424E-3    1.15E-2   4.7E-2
       141.57     181.39      141.53     161.69    46.21

                   Table 5.1: *MAT_058 card for APX300 composite



5.2.      Tensile test
As explained above, shell elements are used with a mesh size of 5mm in order to reproduce
tensile test specimen with a geometry of 250x25x2.34mm. This layout allow to maintain
as square as possible the elements of the model, preventing from distortion, which could
be source of errors. The specimen thickness and lamination sequence are represented by
means of CLT, and layers are considered perfectly bounded. As in experimental tests,
a gage section of 150mm is considered and the two ends are constrained through nodal
boundaries. In particular, one end is clamped whereas the other end is forced to move
according to an imposed displacement law. In graphs 5.3 and 5.4 results are shown, stress
value is obtained as the ratio of force over the specimen area, while the strain is simply
calculated as ∆L/L, where the displacement increment is known and L is the section gage
of the specimen. The latter formula is capable to well represent the actual strain, since the
model does not consider any slippage at the ends and exact values both of section gage
and displacement variation are considered. The forces are measured through a section
placed in the middle of the section gage, this measure results to be more accurate and no
filter is needed to obtain final stress-strain curve.




                          Figure 5.2: Numerical tensile test set-up
5| Numerical simulation                                                               101


Samples with both 0° and 90° oriented warp fibers are tested. Although ultimate stress
and ultimate strain values are consistent with the experimental results, the model is not
able to capture the correct degradation of the elastic modulus. In detail, the transition
strain point is not located at the beginning of the stress-strain curve, but at the end of
it. This outcome can be consider acceptable, but improvement are needed to achieve a
proper stress-strain curve so as to model a proper brittle failure.




              Figure 5.3: Stress-strain curves comparison for 0° specimens




             Figure 5.4: Stress-strain curves comparison for 90° specimens
102                                                            5| Numerical simulation


5.3.      Shear test
Specimen is modelled as in tensile test but in this case a geometry of 250x25x3.12mm
is considered. Due to high deformation level, distortion of the element can be an issue.
In general, the material rely on element coordinate system, but if the element distortion
is excessively high the model can return inconsistent evaluation. In order to avoid the
latter case while obtaining reliable results a global material coordinate system is defined.
Moreover, a control over the accuracy of the model is set to ensure the stability of the
model.

As in the tensile model the forces are measured through a section located in the middle
part of the specimen. So as to achieve shear stress and shear strain, the formulas presented
in section 4.2.3 are used. To calculate shear strain both transverse and axial strains are
requested. As above mentioned, the latter is a known quantity, whereas transverse shear
has to be achieved. In order to obtain this value the assumption of Poisson’s ratio equal to
1 is employed and transverse strain can be assumed equal to axial strain. The comparison
between numerical and experimental results is shown in graph 5.5 within 5% of shear
strain. In detail, the bi-linear numerical curve slightly underestimates the real behaviour,
especially in the last part of the graph. However, acceptable outcomes are achieved if
shear modulus and maximum shear strain are considered.




             Figure 5.5: Stress-strain curves comparison for ±45° specimens
5| Numerical simulation                                                                103


5.4.     Compression test
Compression model set-up is similar to the above mentioned models, expect for the
mesh size. In this case 4mm mesh is selected to best fit the specimen geometry of
140x16x2.34mm. The material card 58 does not allow for the definition of compres-
sive Young’s modulus. Consequently, a choice is made: in order to not affect the tensile
response, the compressive modulus of elasticity is considered equal to the tensile one,
hence, only the tensile Young’s modulus is evaluated for the definition of the material
(see table 5.1). Although the presence of this assumption, the obtained results in terms
of compressive modulus are similar to the experimental outcomes. Test are performed
both for 0° and 90° oriented warp fibers samples, and a section gage of 12mm is adopted,
in compliant with standard D6641.

The achieved ultimate compressive stress values are comparable with experimental results.
In detail, for specimens with 0° oriented fibers, a maximum value of 140.87Mpa is recorded,
while for 90° samples a maximum value of 140.84Mpa is obtained. These outcomes are
less than 1% lower with respect to experimental counterparts, hence the model can be
considered suitable to numerically approximate compressive behaviour.




          Figure 5.6: Compression test numerical outcomes for 90° specimens
104                                                          5| Numerical simulation




          Figure 5.7: Compression test numerical outcomes for 90° specimens



5.5.     Bending test
Out-of-plane bending test is modelled differently with respect to the other models. The
numerical specimen is similar to the ones presented in the previous sections, but in this
case the load is generated by means of three cylinders, as shown in figure 5.8.

The latter components are modelled by exploiting shell elements so as to reduce compu-
tational cost. In the experimental tests, cylinders are made by steel, thus in numerical
model they can be considered as rigid body. In order to interact with the specimen an
AUTOMATIC_SURFACE_TO_SURFACE contact, with a static friction coefficient of
0.5, is used so as to prevent any slippage phenomena during numerical simulation. As
mentioned above, a check on the dissipative energy is conducted to ensure the consistency
of the results. Eventually, a mesh size of 3mm is selected both for the specimen and the
cylinders to achieve better numerical outcomes.
5| Numerical simulation                                                                105




                                   (a) Initial configuration




                                 (b) Deformed configuration

                       Figure 5.8: Numerical bending test set-up


The set-up to perform the test is presented below: the lower cylinders are completely
constrained, while an imposed vertical displacement is applied to the upper cylinder. The
specimen is completely free to move, but due to the static friction no motions are recorder
during the simulation. The results are shown in figure 5.9: the numerical curve is filtered
using a SAE filter with cutting frequency of 180 Hz so as to reduce the contact noise.
In the first half of the graph experimental and numerical results are comparable, while,
with high deformation, numerical test seems to be not able to capture the real behaviour
of the material. These discrepancies can be correlated with some slippage phenomena or
even with imperfect alignment during the experimental test. However, the latter are not
able to justify the poor result in terms of displacement, numerical improvement must be
performed. Hence, more refined optimization techniques must be considered to enhance
consistent numerical performances. Eventually, it worth noting that maximum numerical
force is comparable with experimental results, although premature failure occurs.
106                                                   5| Numerical simulation




      Figure 5.9: Force-displacement curves comparison for bending test
                                                                                          107




6 | Conclusions and future
              developments
This thesis work aims to investigate both the static and dynamic mechanical performances
of flax-fiber reinforced composite material and their numerical modeling, through the
development of a suitable material card. The results achieved can be considered positive
and significant, since the major mechanical features of the material were analyzed and
numerical outcomes shown a general consistency with respect to the experimental data.

Although the presence of flaws both in the procedure and in some specimens, experimental
static tests were able to provide consistent outcomes. Hence, static mechanical perfor-
mances can be considered reliable for future potential design processes. During dynamic
tests, especially strain rate sensitivity tests, some procedural issue arose. In detail, the
employed drop tower machine was not able to acquire the data in some attempts, leading
to a consequent wasting of samples. In addition, the use of emery cloth and aluminium in
place of tabs seemed to be a suitable and practical solution, though further improvement
must be perform to assure the reliability of the tests in every conditions. Nevertheless, the
presented dynamic outcomes can be considered consistent and dependable. In particular,
both indentation and ballistic impact tests parameters were not affected by issue during
test procedures, except for specimens n.20 and n.17 where the data were lost.

It worth noting that, as reported in chapter 3, the achieved specific mechanical properties
can be compared to those of the fiberglass composite. In detail, from the study [6], the
tensile properties of a composite material, made by woven glass fiber fabric and epoxy
resin, are obtained. In order to calculate the specific mechanical properties a specific
gravity equal to 2 is considered. Hence, specific ultimate stress of 129.47Mpa is obtained
and a specific Young’s modulus of 11.86GPa is achieved as well. These parameters are
lower with respect to the values acquired during this work: a specific ultimate tensile stress
of 135.98MPa and a specific elastic modulus of 13.29GPa are obtained considering the
lower specific gravity parameter of flax composite material, which is equal to 1.33. Lastly,
comparison of dynamic properties can be done as well, the mechanical improvement of
108                                         6| Conclusions and future developments


fiberglass/epoxy composite can be found even for flax-fiber reinforced composite. In detail,
in fiberglass composite tests an increase of about 30% in maximum tensile stress can be
measured, while for flax composite a maximum tensile stress improvement of more than
23% was recorded. Both the results are consistent with the excepted materials behaviour.

As mentioned above, the numerical activity presented must be considered as a preliminary
stage of the entire numerical modelling phase. Different material cards were investigated
and the most suitable was selected so as to model flax composite material. In detail,
material card 58 exhibited, except for bending test, significant and consistent outcomes
with respect to experimental data. As a consequence, this study can be considered as a
starting point for further improvement.


6.1.      Future developments
Experimental tests were conducted in order to achieve a well-rounded understanding of
natural composite material, but improvements can be surely performed. For example,
during dynamic tests, a wider range of strain rate values can be considered so as to
investigate sensitivity behaviour from the quasi-static condition to the high-speed impact
event. In addition, a larger amount of specimens, with different layout stacking sequences
and thicknesses, can be employed to gain a full understanding of the dynamic behaviour.
Data acquisition system can be improved as well, for example using accelerometer in order
to have an outcome independent of the machinery. Regarding both indentation test and
ballistic impact test, a more in-depth analysis about the geometry and size of the damaged
area can be performed through the use of nondestructive inspection techniques, such as
radiography. In addition, a detailed view of the totally failed specimens can be done so
as to perform a complete failure modes analysis.

Numerical model accuracy can be improved operating on both material card and numerical
elements. More complex material cards can be implemented such as MAT_262, but
additional experimental tests on fracture toughness must be performed in order to achieve
the required parameters. Moreover, so as to study out-of-plane behaviour of composites a
different modeling approach can be adopted by employing 3D elements or by introducing a
stacked-shell approach. Eventually, through the use of LS-OPT, which is an optimization
tools that interfaces perfectly with LS-DYNA, an optimization process of the defined
parameters can be done so as to improve the outcomes in a effective way.

Manufacturing techniques may have a great margin of improvement considering that the
interest in bio-materials developed just a few years ago. Both pre-production and post-
production treatments can be evaluated to solve issue such as high hygroscopicity and
6| Conclusions and future developments                                                   109


poor fiber-matrix adhesion. In doing so, mechanical performances and durability could
be increased significantly allowing for a wider employment of natural materials.

In conclusion, natural composite materials revealed noteworthy mechanical performances
in the context of crashworthiness applications. Especially, considering the exhibited failure
modes during dynamic tests: few debris were found in the impacted areas, thanks to the
nature of bio-fibers, which are not prone to detach from the laminate. Lastly, bio-inspired
structures such as coconut tree geometry, date palm tree structure and even bamboo
multi-cell structure, can be used during design phases in order to maximize the absorbed
energy while fully exploiting the potential of natural composite materials.
                                                                                      111




Bibliography
 [1] B. D. Agarwal, L. J. Broutman, and C. Bert. Analysis and performance of fiber
     composites. John Wiley & Sons, 2006.

 [2] A. Ali, K. Shaker, Y. Nawab, M. Jabbar, T. Hussain, J. Militky, and V. Baheti.
     Hydrophobic treatment of natural fibers and their composites—a review. Journal of
     Industrial Textiles, 47(8):2153–2183, 2018.

 [3] M. Alkbir, S. Sapuan, A. Nuraini, and M. Ishak. Fibre properties and crashworthi-
     ness parameters of natural fibre-reinforced composite structure: A literature review.
     Composite Structures, 148:59–73, 2016.

 [4] M. A. Attia, M. A. Abd El-Baky, M. A. Hassan, T. A. Sebaey, and E. Mahdi. Crash-
     worthiness characteristics of carbon–jute–glass reinforced epoxy composite circular
     tubes. Polymer Composites, 39(S4):E2245–E2261, 2018.

 [5] H. Chen. Biotechnology of lignocellulose. Theory and Practice. China: Chemical
     Industry Press and Springer, 2014.

 [6] W. Chen, Q. Meng, H. Hao, J. Cui, and Y. Shi. Quasi-static and dynamic tensile
     properties of fiberglass/epoxy laminate sheet. Construction and Building Materials,
     143:247–258, 2017.

 [7] A. Cherniaev, C. Butcher, and J. Montesano. Predicting the axial crush response
     of cfrp tubes using three damage-based constitutive models. Thin-walled structures,
     129:349–364, 2018.

 [8] O. Cousigné, D. Moncayo, D. Coutellier, P. Camanho, and H. Naceur. Numerical
     modeling of nonlinearity, plasticity and damage in cfrp-woven composites for crash
     simulations. Composite Structures, 115:75–88, 2014.

 [9] M. Deorsi and C. Ermoli. Numerical and experimental characterization of composite
     materials. Master’s thesis, Politecnico di Milano, 2022.

[10] R. A. Eshkoor, S. A. Oshkovr, A. Sulong, R. Zulkifli, A. K. Ariffin, and C. H.
112                                                                      | Bibliography


      Azhari. Comparative research on the crashworthiness characteristics of woven natural
      silk/epoxy composite tubes. Materials & Design, 47:248–257, 2013.

[11] M. J. Ghoushji, R. A. Eshkoor, R. Zulkifli, A. B. Sulong, S. Abdullah, and
     C. H. Azhari. Energy absorption capability of axially compressed woven natural
     ramie/green epoxy square composite tubes. Journal of Reinforced Plastics and Com-
     posites, 36(14):1028–1037, 2017.

[12] Guide to composite.        Gurit Holding AG.                https://www.gurit.com/-
     /media/Gurit/Datasheets/guide-to-composites.pdf.

[13] C. W. Isaac and C. Ezekwem. A review of the crashworthiness performance of energy
     absorbing composite structure within the context of materials, manufacturing and
     maintenance for sustainability. Composite Structures, 257:113081, 2021.

[14] R. M. Jones. Mechanics of composites materials. Taylor & Francis, 1999.

[15] M. Kabir, H. Wang, T. Aravinthan, F. Cardona, and K.-T. Lau. Effects of natural fi-
     bre surface on composite properties: A review. In Proceedings of the 1st International
     Postgraduate Conference on Engineering, Designing and Developing the Built Envi-
     ronment for Sustainable Wellbeing (eddBE 2011). University of Southern Queensland,
     2011.

[16] F. La Mantia and M. Morreale. Green composites: A brief review. Composites Part
     A: Applied Science and Manufacturing, 42(6):579–588, 2011.

[17] LS-DYNA ® KEYWORD USER’S MANUAL VOLUME II Material Models Liver-
     more Software Technology (LST), An Ansys Company. LSTC, 1992.

[18] A. Matzenmiller, J. Lubliner, and R. L. Taylor. A constitutive model for anisotropic
     damage in fiber-composites. Mechanics of materials, 20(2):125–152, 1995.

[19] Q. Meng and Z. Wang. Theoretical analysis of interfacial debonding and fiber pull-
     out in fiber-reinforced polymer-matrix composites. Archive of Applied Mechanics, 85
     (6):745–759, 2015.

[20] J. Meredith, R. Ebsworth, S. R. Coles, B. M. Wood, and K. Kirwan. Natural fibre
     composite energy absorption structures. Composites Science and Technology, 72(2):
     211–217, 2012.

[21] B. Mitra. Environment friendly composite materials: Biocomposites and green com-
     posites. Defence science journal, 64(3), 2014.

[22] L. Mohammed, M. N. Ansari, G. Pua, M. Jawaid, and M. S. Islam. A review on
| Bibliography                                                                        113


    natural fiber reinforced polymer composite and its applications. International journal
    of polymer science, 2015, 2015.

[23] T.-D. Ngo. Introduction to composite materials. Composite and Nanocomposite
     Materials—From Knowledge to Industrial Applications, 2020.

[24] S. Oshkovr, R. Eshkoor, S. Taher, A. Ariffin, and C. Azhari. Crashworthiness char-
     acteristics investigation of silk/epoxy composite square tubes. Composite Structures,
     94(8):2337–2342, 2012.

[25] P. Peças, H. Carvalho, H. Salman, and M. Leite. Natural fibre composites and their
     applications: a review. Journal of composites science, 2(4):66, 2018.

[26] P. Petit. A simplified method of determining the inplane shear stress-strain response
     of unidirectional composites. In Composite materials: Testing and design. ASTM
     International, 1969.

[27] D. K. Rajak, D. D. Pagar, P. L. Menezes, and E. Linul. Fiber-reinforced polymer
     composites: Manufacturing, properties, and applications. Polymers, 11(10):1667,
     2019.

[28] D. K. Rajak, P. H. Wagh, and E. Linul. A review on synthetic fibers for polymer
     matrix composites: performance, failure modes and applications. Materials, 15(14):
     4790, 2022.

[29] K. Rohit and S. Dixit. A review-future aspect of natural fiber reinforced composite.
     Polymers from Renewable Resources, 7(2):43–59, 2016.

[30] B. W. Rosen. A simple procedure for experimental determination of the longitudinal
     shear modulus of unidirectional composites. Journal of Composite Materials, 6(3):
     552–554, 1972.

[31] A. Rubini. Analisi del processo produttivo di componenti in fibra di carbonio con
     autoclave: il caso di hp composites. Master’s thesis, Politecnico di Torino, 2020.

[32] K. Schweizerhof, K. Weimar, T. Munz, and T. Rottner. Crashworthiness analysis
     with enhanced composite material models in ls-dyna–merits and limits. In LS-DYNA
     world conference, pages 1–17, 1998.

[33] E. S. Stevens. Green plastics: an introduction to the new science of biodegradable
     plastics. Princeton University Press, 2002.

[34] H. Takagi and A. Asano. Effects of processing conditions on flexural properties of
114                                                                6| BIBLIOGRAPHY


      cellulose nanofiber reinforced “green” composites. Composites Part A: Applied Science
      and Manufacturing, 39(4):685–689, 2008.

[35] K. Tanaka, T. Katsura, Y. Kinoshita, T. Katayama, and K. Uno. Mechanical prop-
     erties of jute fabric reinforced thermoplastic moulded by high-speed processing using
     electromagnetic induction. WIT Trans Built Environ, 97:211–219, 2008.

[36] C. Williams, S. Grove, and J. Summerscales. The compression response of fibre-
     reinforced plastic plates during manufacture by the resin infusion under flexible tool-
     ing method. Composites Part A: applied science and manufacturing, 29(1-2):111–114,
     1998.

[37] M. Zin, K. Abdan, N. Mazlan, E. Zainudin, and K. Liew. The effects of alkali
     treatment on the mechanical and chemical properties of pineapple leaf fibres (palf)
     and adhesion to epoxy resin. In IOP Conference Series: Materials Science and
     Engineering, volume 368, page 012035. IOP Publishing, 2018.
                                                                       115




A | Appendix A
A.1.   Static tests specimens




          Figure A.1: Tensile test specimens with 0° oriented fibers
116                                                           A| Appendix A




      Figure A.2: Tensile test specimens with 90° oriented fibers
A| Appendix A                                      117




                Figure A.3: Shear test specimens
118                                                      A| Appendix A




       Figure A.4: Bending test specimens (top view)




      Figure A.5: Bending test specimens (bottom view)
A| Appendix A                                                             119




         Figure A.6: Compression test specimens with 0° oriented fibers




        Figure A.7: Compression test specimens with 90° oriented fibers
120                                                              A| Appendix A


A.2.   Dynamic tests specimens




          Figure A.8: Strain rate test specimens without strain gages




       Figure A.9: Strain rate test specimens equipped with strain gages
A| Appendix A                                              121




                Figure A.10: Indentation test specimen 3




                Figure A.11: Indentation test specimen 4
122                                              A| Appendix A




      Figure A.12: Indentation test specimen 5




      Figure A.13: Indentation test specimen 7
A| Appendix A                                               123




                Figure A.14: Indentation test specimen 14




                Figure A.15: Indentation test specimen 15
124                                               A| Appendix A




      Figure A.16: Indentation test specimen 16




      Figure A.17: Indentation test specimen 17
A| Appendix A                                               125




                Figure A.18: Indentation test specimen 18




                Figure A.19: Indentation test specimen 19
126                                               A| Appendix A




      Figure A.20: Indentation test specimen 20




      Figure A.21: Indentation test specimen 21
A| Appendix A                                                   127




                Figure A.22: Ballistic impact test specimen 1




                Figure A.23: Ballistic impact test specimen 2
128                                                   A| Appendix A




      Figure A.24: Ballistic impact test specimen 6




      Figure A.25: Ballistic impact test specimen 8
A| Appendix A                                                    129




                Figure A.26: Ballistic impact test specimen 9




                Figure A.27: Ballistic impact test specimen 11
130                                                       A| Appendix A




      Figure A.28: Ballistic impact evolution of specimen 1
A| Appendix A                                                       131




            Figure A.29: Ballistic impact evolution of specimen 6
132                                                       A| Appendix A




      Figure A.30: Ballistic impact evolution of specimen 9
A| Appendix A                                                        133




            Figure A.31: Ballistic impact evolution of specimen 11
                                                                                          135




List of Figures
 2.1 Straw reinforced mud-brick production . . . . . . . . . . . . . . . . . . . .         3
 2.2 Continuous vs discontinuous fibers . . . . . . . . . . . . . . . . . . . . . .        5
 2.3 Unbounded view of laminate construction . . . . . . . . . . . . . . . . . .           5
 2.4 Unidirectional and woven laminae . . . . . . . . . . . . . . . . . . . . . . .        6
 2.5 Fiber and matrix mechanical properties . . . . . . . . . . . . . . . . . . . .        7
 2.6 RoM model for longitudinal properties . . . . . . . . . . . . . . . . . . . .         8
 2.7 Stress state on a element . . . . . . . . . . . . . . . . . . . . . . . . . . . .     9
 2.8 Lamina coordinate system . . . . . . . . . . . . . . . . . . . . . . . . . . .       10
 2.9 Positive rotation of principal material axes . . . . . . . . . . . . . . . . . .     12
 2.10 Geometry of a N-layered lamina . . . . . . . . . . . . . . . . . . . . . . . .      14
 2.11 Damaged section of [0/90]s composite . . . . . . . . . . . . . . . . . . . . .      16
 2.12 Modes of fracture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   16
 2.13 Fiber pull-out and debonding . . . . . . . . . . . . . . . . . . . . . . . . .      17
 2.14 Microbuckling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   18
 2.15 Spray lay-up process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    20
 2.16 Hand lay-up process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     21
 2.17 Wet lay-up process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
 2.18 Filament winding process . . . . . . . . . . . . . . . . . . . . . . . . . . . .    22
 2.19 Pultrusion process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
 2.20 Resin Transfer Moulding process . . . . . . . . . . . . . . . . . . . . . . . .     24
 2.21 Resin Infusion under Flexible Tool process . . . . . . . . . . . . . . . . . .      25
 2.22 Compression moulding process . . . . . . . . . . . . . . . . . . . . . . . . .      26
 2.23 Sample of prepreg lamina . . . . . . . . . . . . . . . . . . . . . . . . . . .      27
 2.24 Autoclave production process . . . . . . . . . . . . . . . . . . . . . . . . .      28
 2.25 Additive manufacturing process . . . . . . . . . . . . . . . . . . . . . . . .      29
 2.26 Schematic of a building block approach . . . . . . . . . . . . . . . . . . . .      30
 2.27 Comparison of MAT054, MAT058 and MAT262 . . . . . . . . . . . . . . .               32
 2.28 Non-linear stress-strain relationship for shear . . . . . . . . . . . . . . . . .   37

 3.1   Classification of bio-composites . . . . . . . . . . . . . . . . . . . . . . . . 40
136                                                                       | List of Figures


  3.2   Illustration of hand lay-up of natural kenaf fiber/epoxy composite . . . . .         46
  3.3   Illustration of vacuum bagging manufacturing of GFRP and CFRP com-
        posite cylindrical shell . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   47
  3.4   Abt Cupra XE body sheel made of flax composite materials . . . . . . . .             49
  3.5   Door panel made of hemp fiber . . . . . . . . . . . . . . . . . . . . . . . .        50
  3.6   Macroscopic detail for each fiber type . . . . . . . . . . . . . . . . . . . . .     53
  3.7   Polylactic acid (PLA) in raw material form . . . . . . . . . . . . . . . . . .       54

  4.1 Detail of an ampliTex™ 300 laminate . . . . . . . . . . . . . . . . . . . . .          57
  4.2 Production phases of flax composite laminates . . . . . . . . . . . . . . . .          58
  4.3 Autoclave cycle parameters . . . . . . . . . . . . . . . . . . . . . . . . . .         60
  4.4 ProtoMAX abrasive waterjet cutter . . . . . . . . . . . . . . . . . . . . . .          61
  4.5 Dynamic mechanical analysis of 8-layered composite . . . . . . . . . . . . .           61
  4.6 Employed material testing system . . . . . . . . . . . . . . . . . . . . . . .         63
  4.7 Tensile test set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    65
  4.8 Stress-strain curve comparison . . . . . . . . . . . . . . . . . . . . . . . . .       67
  4.9 Stress-strain curve for tensile test . . . . . . . . . . . . . . . . . . . . . . .     68
  4.10 Transition strain points . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    70
  4.11 Shear test set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     72
  4.12 Stress-strain curve for shear test . . . . . . . . . . . . . . . . . . . . . . . .    73
  4.13 Bending test set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     74
  4.14 Force-displacement curve for bending test . . . . . . . . . . . . . . . . . . .       76
  4.15 Stress-strain curve for bending test . . . . . . . . . . . . . . . . . . . . . .      76
  4.16 Strain gages layout of compressive specimen . . . . . . . . . . . . . . . . .         78
  4.17 Graphical representation of elastic compressive modulus . . . . . . . . . . .         79
  4.18 Data acquisition devices . . . . . . . . . . . . . . . . . . . . . . . . . . . .      80
  4.19 Step Lab DW1000 system . . . . . . . . . . . . . . . . . . . . . . . . . . .          81
  4.20 Gas gun set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      82
  4.21 Strain rate test set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     83
  4.22 Lower grip set-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     83
  4.23 Strain rate effect on ultimate stress . . . . . . . . . . . . . . . . . . . . . .     85
  4.24 Comparison between static and dynamic tensile response . . . . . . . . . .            85
  4.25 Strain rate effect on tensile SEA . . . . . . . . . . . . . . . . . . . . . . . .     86
  4.26 Indentation test setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      87
  4.27 D20 hemispherical striker tip . . . . . . . . . . . . . . . . . . . . . . . . . .     88
  4.28 Peak force in relation to kinetic energy . . . . . . . . . . . . . . . . . . . .      90
  4.29 Force-displacement curve for D127 . . . . . . . . . . . . . . . . . . . . . . .       91
| List of Figures                                                                         137


   4.30 Force-displacement curve for D16 . . . . . . . . . . . . . . . . . . . . . . . 91
   4.31 Force-displacement curve for D20 . . . . . . . . . . . . . . . . . . . . . . . 92
   4.32 Representative failure modes indentation test . . . . . . . . . . . . . . . . 93
   4.33 Output velocity and percentage absorbed energy in relation to input velocity 95
   4.34 Representative failure modes ballistic test . . . . . . . . . . . . . . . . . . 95

   5.1   Energetic validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
   5.2   Numerical tensile test set-up . . . . . . . . . . . . . . . . . . . . . . . . . . 100
   5.3   Stress-strain curves comparison for 0° specimens . . . . . . . . . . . . . . . 101
   5.4   Stress-strain curves comparison for 90° specimens . . . . . . . . . . . . . . 101
   5.5   Stress-strain curves comparison for ±45° specimens . . . . . . . . . . . . . 102
   5.6   Compression test numerical outcomes for 90° specimens . . . . . . . . . . . 103
   5.7   Compression test numerical outcomes for 90° specimens . . . . . . . . . . . 104
   5.8   Numerical bending test set-up . . . . . . . . . . . . . . . . . . . . . . . . . 105
   5.9   Force-displacement curves comparison for bending test . . . . . . . . . . . 106

   A.1 Tensile test specimens with 0° oriented fibers . . . . . . . . . . . . . . . . . 115
   A.2 Tensile test specimens with 90° oriented fibers . . . . . . . . . . . . . . . . 116
   A.3 Shear test specimens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
   A.4 Bending test specimens (top view) . . . . . . . . . . . . . . . . . . . . . . . 118
   A.5 Bending test specimens (bottom view) . . . . . . . . . . . . . . . . . . . . 118
   A.6 Compression test specimens with 0° oriented fibers . . . . . . . . . . . . . 119
   A.7 Compression test specimens with 90° oriented fibers . . . . . . . . . . . . . 119
   A.8 Strain rate test specimens without strain gages . . . . . . . . . . . . . . . . 120
   A.9 Strain rate test specimens equipped with strain gages . . . . . . . . . . . . 120
   A.10 Indentation test specimen 3 . . . . . . . . . . . . . . . . . . . . . . . . . . 121
   A.11 Indentation test specimen 4 . . . . . . . . . . . . . . . . . . . . . . . . . . 121
   A.12 Indentation test specimen 5 . . . . . . . . . . . . . . . . . . . . . . . . . . 122
   A.13 Indentation test specimen 7 . . . . . . . . . . . . . . . . . . . . . . . . . . 122
   A.14 Indentation test specimen 14 . . . . . . . . . . . . . . . . . . . . . . . . . . 123
   A.15 Indentation test specimen 15 . . . . . . . . . . . . . . . . . . . . . . . . . . 123
   A.16 Indentation test specimen 16 . . . . . . . . . . . . . . . . . . . . . . . . . . 124
   A.17 Indentation test specimen 17 . . . . . . . . . . . . . . . . . . . . . . . . . . 124
   A.18 Indentation test specimen 18 . . . . . . . . . . . . . . . . . . . . . . . . . . 125
   A.19 Indentation test specimen 19 . . . . . . . . . . . . . . . . . . . . . . . . . . 125
   A.20 Indentation test specimen 20 . . . . . . . . . . . . . . . . . . . . . . . . . . 126
   A.21 Indentation test specimen 21 . . . . . . . . . . . . . . . . . . . . . . . . . . 126
   A.22 Ballistic impact test specimen 1 . . . . . . . . . . . . . . . . . . . . . . . . 127
138                                                                   | List of Figures


  A.23 Ballistic impact test specimen 2 . . . . . . . . . . . . . . . . . . . . . . . . 127
  A.24 Ballistic impact test specimen 6 . . . . . . . . . . . . . . . . . . . . . . . . 128
  A.25 Ballistic impact test specimen 8 . . . . . . . . . . . . . . . . . . . . . . . . 128
  A.26 Ballistic impact test specimen 9 . . . . . . . . . . . . . . . . . . . . . . . . 129
  A.27 Ballistic impact test specimen 11 . . . . . . . . . . . . . . . . . . . . . . . 129
  A.28 Ballistic impact evolution of specimen 1 . . . . . . . . . . . . . . . . . . . 130
  A.29 Ballistic impact evolution of specimen 6 . . . . . . . . . . . . . . . . . . . 131
  A.30 Ballistic impact evolution of specimen 9 . . . . . . . . . . . . . . . . . . . 132
  A.31 Ballistic impact evolution of specimen 11 . . . . . . . . . . . . . . . . . . . 133
                                                                                              139




List of Tables
 2.1   *MAT_058 card overview . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

 3.1   Pros and cons of natural composite materials . . . . . . . . . . . . . . . . .         42
 3.2   Specific mechanical properties . . . . . . . . . . . . . . . . . . . . . . . . .       43
 3.3   Energy and cost of different fibres . . . . . . . . . . . . . . . . . . . . . . .      43
 3.4   Mechanical features green composite (GC) without and with the use of a
       maleated adhesion promoter (MAPP) . . . . . . . . . . . . . . . . . . . . .            45
 3.5   Chemical treatments on natural fibers and their effects on functional prop-
       erties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   46
 3.6   Physical properties of natural fibres (average value between parenthesis) . .          51
 3.7   Mechanical properties of natural fibres (average value between parenthesis)            52

 4.1 Tensile test specimens sizes . . . . . . . . . . . . . . . . . . . . . . . . . .         65
 4.2 Tensile mechanical properties . . . . . . . . . . . . . . . . . . . . . . . . .          69
 4.3 Shear test specimens sizes . . . . . . . . . . . . . . . . . . . . . . . . . . .         71
 4.4 Shear mechanical properties . . . . . . . . . . . . . . . . . . . . . . . . . .          73
 4.5 Bending test specimens sizes . . . . . . . . . . . . . . . . . . . . . . . . . .         74
 4.6 Flexural mechanical properties . . . . . . . . . . . . . . . . . . . . . . . . .         75
 4.7 Compression test specimens sizes . . . . . . . . . . . . . . . . . . . . . . .           77
 4.8 Compressive mechanical properties . . . . . . . . . . . . . . . . . . . . . .            80
 4.9 Strain rate sensitivity test specimens sizes . . . . . . . . . . . . . . . . . .         84
 4.10 Hemispherical striker tips characteristics . . . . . . . . . . . . . . . . . . .        87
 4.11 Indentation test specimens sizes . . . . . . . . . . . . . . . . . . . . . . . .        88
 4.12 Parameters and results of indentation test . . . . . . . . . . . . . . . . . .          89
 4.13 Ballistic impact test specimens sizes . . . . . . . . . . . . . . . . . . . . . .       94
 4.14 Parameters and results of ballistic impact test . . . . . . . . . . . . . . . .         94

 5.1   *MAT_058 card for APX300 composite . . . . . . . . . . . . . . . . . . . 100
