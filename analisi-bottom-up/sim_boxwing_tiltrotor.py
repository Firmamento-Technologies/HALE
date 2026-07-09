#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulazione bottom-up L0/L1 — confronto architetture VTOL a scala C3 (25 kg, ~3 m).
Studio di Fattibilità HALE / Firmamento Technologies.

Obiettivo: testare il concept dell'utente (box-wing con 4 tilt-rotor: 2 anteriori
traenti + 2 posteriori spingenti, entrambe le ali portanti) contro:
  - MONO      : fixed-wing monoplano pulito NON-VTOL (soffitto aerodinamico)
  - LIFTCRUISE: quadplane 4 lift (morti in crociera) + 1 pusher  [COTS: JOUAV/Quantum]
  - RETRACT   : lift+cruise con pod di sostentamento RETRATTILI  [analogo SUPAIR ThrustPod]
  - BOXTILT   : concept utente (box-wing, 4 tilt-rotor tutti usati in crociera)

Fedelta' L0/L1 (back-of-envelope), coerente con 22-boxwing-vantaggio-tecnico.md.
Nessun dato e' una prova di volo o un CFD. Tutte le assunzioni sono esplicite e
falsificabili. Le cifre chiave sono ancorate ai numeri gia' nel repository.
"""

import math

# ----------------------------- Parametri comuni -----------------------------
g      = 9.81
MTOM   = 25.0                 # kg  (tetto duro C3)
W      = MTOM * g             # N
rho    = 1.09                 # kg/m3  (~1200 m, valle Pentema)
V      = 28.0                 # m/s cruise (~101 km/h), coerente con target 90-120 km/h (doc 10 §3.2)
b      = 3.0                  # m  apertura (vincolo C3)
AR     = 13.0                 # allungamento equivalente
S      = b**2 / AR            # m2 superficie di riferimento
eta_p  = 0.72                 # rendimento elica crociera
eta_m  = 0.88                 # rendimento motore+ESC
FM     = 0.68                 # figure of merit rotori in hover
Drot   = 0.55                 # m  diametro rotore di sostentamento
Nrot   = 4                    # rotori di sostentamento
Arot   = Nrot * math.pi/4 * Drot**2
ebatt  = 230.0                # Wh/kg  densita' energetica pacco
DoD    = 0.85                 # profondita' di scarica utile
payload= 3.5                  # kg  payload fisso C3
base_empty_frac = 0.40        # frazione MTOM per struttura+avionica+propulsione crociera (fixed-wing base)

# --- Parametri per configurazione (assunzioni esplicite, ancorate a doc 22) ---
# CD0  : parassita riferito a S. Ancore doc22: ala pulita ~0.011; VTOL "sporco" ~0.040.
# e    : efficienza di span (Oswald). Box-wing: guadagno Prandtl su drag indotto.
# down : download in hover (frazione di W aggiuntiva). Box: due ali nella scia.
# vtol_pen : massa hardware VTOL come frazione di MTOM (oltre la base fixed-wing).
# note : nota qualitativa.
CFG = {
 "MONO": dict(
    CD0=0.028, e=0.80, down=None, vtol_pen=0.00, hover=False,
    note="monoplano pulito, NON-VTOL (soffitto aero, non schierabile a Pentema)"),
 "LIFTCRUISE": dict(
    CD0=0.044, e=0.80, down=0.08, vtol_pen=0.18, hover=True,
    note="4 rotori lift ESPOSTI e fermi in crociera (dischi bluff) + booms; COTS"),
 "RETRACT": dict(
    CD0=0.031, e=0.80, down=0.08, vtol_pen=0.18, hover=True,
    note="pod lift RETRATTILI: crociera quasi pulita; analogo SUPAIR ThrustPod (brevettato)"),
 "BOXTILT": dict(
    CD0=0.034, e=1.05, down=0.14, vtol_pen=0.15, hover=True,
    note="concept utente: box-wing, 4 tilt-rotor TUTTI attivi in crociera (2 traenti+2 spingenti)"),
}

def analyze(name, p):
    # ---- massa e batteria ----
    empty = base_empty_frac*MTOM + p["vtol_pen"]*MTOM
    m_batt = MTOM - empty - payload
    E_batt = m_batt * ebatt          # Wh nominali
    # ---- crociera ----
    CL = W / (0.5*rho*V**2*S)
    CDi = CL**2 / (math.pi*AR*p["e"])
    CD = p["CD0"] + CDi
    LD = CL/CD
    D  = 0.5*rho*V**2*S*CD           # N
    P_shaft = D*V/eta_p              # W
    P_elec  = P_shaft/eta_m          # W
    endur_h = (E_batt*DoD)/P_elec    # h di sola crociera (approx, ignora salita/hover)
    range_km= V*endur_h*3.6
    # ---- hover ----
    if p["hover"]:
        T = W*(1.0+p["down"])
        P_hover_ideal = T**1.5/math.sqrt(2*rho*Arot)
        P_hover = P_hover_ideal/FM
    else:
        P_hover = float('nan')
    return dict(name=name, empty=empty, m_batt=m_batt, E_batt=E_batt, CL=CL, CD0=p["CD0"],
                CDi=CDi, CD=CD, LD=LD, P_elec=P_elec, endur_h=endur_h, range_km=range_km,
                P_hover=P_hover, note=p["note"])

rows = [analyze(n, p) for n, p in CFG.items()]

print("="*104)
print(f"SIMULAZIONE C3 box-wing tilt-rotor — MTOM {MTOM} kg, b {b} m, S {S:.3f} m2, V {V} m/s ({V*3.6:.0f} km/h), rho {rho}")
print(f"payload fisso {payload} kg, batteria {ebatt} Wh/kg (DoD {DoD}), eta_prop {eta_p}, eta_mot {eta_m}, FM {FM}")
print("="*104)
hdr = f"{'Config':<11}{'CD0':>7}{'CDi':>7}{'CD':>7}{'L/D':>7}{'Pcruise[W]':>11}{'m_batt[kg]':>11}{'endur[h]':>9}{'range[km]':>10}{'Phover[W]':>10}"
print(hdr); print("-"*104)
for r in rows:
    ph = f"{r['P_hover']:.0f}" if not math.isnan(r['P_hover']) else "  n/a"
    print(f"{r['name']:<11}{r['CD0']:>7.3f}{r['CDi']:>7.4f}{r['CD']:>7.3f}{r['LD']:>7.2f}"
          f"{r['P_elec']:>11.0f}{r['m_batt']:>11.2f}{r['endur_h']:>9.2f}{r['range_km']:>10.0f}{ph:>10}")
print("-"*104)

# ---- confronti chiave (vs LIFTCRUISE, il COTS di riferimento) ----
base = next(r for r in rows if r["name"]=="LIFTCRUISE")
box  = next(r for r in rows if r["name"]=="BOXTILT")
ret  = next(r for r in rows if r["name"]=="RETRACT")
print("\nCONFRONTI CHIAVE (riferimento = LIFTCRUISE COTS):")
def cmp(a):
    dP = (a['P_elec']-base['P_elec'])/base['P_elec']*100
    dR = (a['range_km']-base['range_km'])/base['range_km']*100
    print(f"  {a['name']:<11}: Pcruise {dP:+5.1f}%   range {dR:+5.1f}%   L/D {a['LD']:.2f} (vs {base['LD']:.2f})")
cmp(box); cmp(ret); cmp(next(r for r in rows if r['name']=='MONO'))
print(f"\n  Hover: BOXTILT {box['P_hover']:.0f} W vs LIFTCRUISE {base['P_hover']:.0f} W "
      f"({(box['P_hover']-base['P_hover'])/base['P_hover']*100:+.1f}% per download box-wing su due ali)")
print(f"  Payload fraction identica ({payload/MTOM*100:.0f}%); differenza scaricata su batteria "
      f"(BOXTILT {box['m_batt']:.2f} kg vs LIFTCRUISE {base['m_batt']:.2f} kg per penalita' VTOL minore).")
print("="*104)
print("NB: L0/L1. La conclusione ROBUSTA e' il segno (BOXTILT/RETRACT >> LIFTCRUISE in crociera),")
print("non il valore assoluto. Falsificabile con VLM/RANS e con CD0 misurato dei nacelle di tilt.")
