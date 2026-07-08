#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Link budget bottom-up per 4 scenari di quota - Connettivita' Pentema.
Firmamento Technologies - analisi-bottom-up/01-connettivita.md
Approccio: prima approssimazione, free-space + margini, LOS geometry.
"""
import math

C = 2.998e8
K_DBW = -228.6

def fspl_db(f_mhz, d_km):
    # Free space path loss, d in km, f in MHz
    return 32.44 + 20*math.log10(f_mhz) + 20*math.log10(d_km)

def radio_horizon_km(h_platform_m, h_user_m=2.0):
    # 4/3 earth radio horizon
    return 4.12*(math.sqrt(h_platform_m) + math.sqrt(h_user_m))

def slant_range_km(alt_m, elev_deg):
    # flat-earth slant range to platform at given elevation angle (small alt vs earth radius)
    return (alt_m/1000.0)/math.sin(math.radians(elev_deg))

def cn0(eirp_dbw, L_total_db, gt_dbk):
    return eirp_dbw - L_total_db + gt_dbk - K_DBW

def snr_db(cn0_dbhz, bw_hz):
    return cn0_dbhz - 10*math.log10(bw_hz)

def gt(g_rx_dbi, T_sys_k, L_rx=1.0):
    return (g_rx_dbi - L_rx) - 10*math.log10(T_sys_k)

print("="*78)
print("GEOMETRIA LOS - raggio orizzonte radio (4/3 earth), utente h=2 m")
print("="*78)
for name, h in [("Aerostato 300 m AGL",300),("VTOL 2 km",2000),
                ("VTOL 4 km",4000),("MALE 7 km",7000),("HALE 20 km",20000)]:
    rh = radio_horizon_km(h)
    print(f"  {name:22s}: orizzonte geometrico = {rh:6.1f} km  (raggio LOS teorico su terreno piatto)")

print()
print("="*78)
print("SLANT RANGE al bordo cella per elevazione minima")
print("="*78)
for name, h in [("VTOL 2 km",2000),("VTOL 4 km",4000),("MALE 7 km",7000),("HALE 20 km",20000)]:
    for elev in [10,5]:
        sr = slant_range_km(h, elev)
        print(f"  {name:12s} elev {elev:2d} deg: slant = {sr:6.1f} km")

# ---------------------------------------------------------------------------
# A) DOWNLINK cella-da-quota -> HANDHELD (smartphone), banda 700 MHz e 2.6 GHz
#    Piattaforma EIRP modesto (payload leggero). Handheld G/T scarso.
# ---------------------------------------------------------------------------
print()
print("="*78)
print("A) DOWNLINK piattaforma -> HANDHELD (smartphone)  [cell-on-wings]")
print("="*78)
# Handheld RX: G=-3 dBi (body+omni), NF 9 dB -> Tsys ~ 290*(10^0.9)=~2300K? use T=290*10^(NF/10)
def tsys_from_nf(nf_db, Tamb=290):
    return Tamb*(10**(nf_db/10))
Tue = tsys_from_nf(7)     # handheld approx (antenna+rx), medium
gt_ue = gt(0.0, Tue, L_rx=0)   # 0 dBi omni handheld
print(f"  Handheld G/T assunto = {gt_ue:.1f} dB/K (0 dBi, NF7, Tsys={Tue:.0f}K)  [med]")
# scenarios: (label, freq_mhz, eirp_dbw, dist_km, bw_hz, extra_loss)
dl = [
  ("700MHz  VTOL2km  r=15km",   700, 13, 15, 5e6, 3),   # eirp 13 dBW=20W*gain? P=5W+... keep modest
  ("700MHz  VTOL2km  r=30km",   700, 13, 30, 5e6, 3),
  ("2600MHz VTOL2km  r=15km",  2600, 16, 15, 10e6, 4),
  ("700MHz  MALE7km  r=50km",   700, 16, 50, 5e6, 4),
  ("700MHz  HALE20km r=50km",   700, 20, 55, 5e6, 4),   # slant ~55 at nadir+offset
  ("2600MHz HALE20km r=30km",  2600, 23, 36, 10e6, 5),
]
print(f"  {'scenario':26s} {'FSPL':>7s} {'Ltot':>7s} {'C/N0':>7s} {'SNR':>6s} {'verdetto'}")
for lab,f,eirp,d,bw,ex in dl:
    L = fspl_db(f,d)+ex
    c0 = cn0(eirp, L, gt_ue)
    s = snr_db(c0, bw)
    verdict = "OK(demod)" if s>3 else ("marg" if s>0 else "FAIL")
    print(f"  {lab:26s} {fspl_db(f,d):7.1f} {L:7.1f} {c0:7.1f} {s:6.1f}  {verdict}")

# ---------------------------------------------------------------------------
# B) UPLINK handheld (23 dBm) -> piattaforma  [IL COLLO DI BOTTIGLIA]
# ---------------------------------------------------------------------------
print()
print("="*78)
print("B) UPLINK HANDHELD (23 dBm=0.2W) -> piattaforma  [bottleneck reale]")
print("="*78)
# Platform RX: decent antenna + cooled-ish LNA. G=10 dBi (sector/AESA beam modest), NF 3
Tplat = tsys_from_nf(3, 290)
gt_plat = gt(10.0, Tplat, L_rx=1)
print(f"  Piattaforma G/T = {gt_plat:.1f} dB/K (10 dBi beam, NF3)  [med]")
eirp_ue = (23-30) + 0.0  # dBW = -7 dBW, 0 dBi handheld
print(f"  EIRP handheld = {eirp_ue:.1f} dBW (23 dBm, 0 dBi)")
ul = [
  ("700MHz  r=15km  bw1.4M",  700, 15, 1.4e6, 3),
  ("700MHz  r=30km  bw1.4M",  700, 30, 1.4e6, 3),
  ("700MHz  r=50km  bw1.4M",  700, 50, 1.4e6, 4),
  ("2600MHz r=15km  bw1.4M", 2600, 15, 1.4e6, 4),
  ("700MHz  HALEr55 bw0.36M", 700, 55, 0.36e6, 4),
]
print(f"  {'scenario':22s} {'FSPL':>7s} {'C/N0':>7s} {'SNR':>6s} verdetto (req QPSK1/2 ~1dB +6 margin)")
for lab,f,d,bw,ex in ul:
    L = fspl_db(f,d)+ex
    c0 = cn0(eirp_ue, L, gt_plat)
    s = snr_db(c0, bw)
    verdict = "OK" if s>7 else ("marg" if s>1 else "FAIL")
    print(f"  {lab:22s} {fspl_db(f,d):7.1f} {c0:7.1f} {s:6.1f}  {verdict}")

# ---------------------------------------------------------------------------
# C) BACKHAUL WiFi/PtP piattaforma <-> dish a terra (5 GHz) - relay a bassa quota
# ---------------------------------------------------------------------------
print()
print("="*78)
print("C) BACKHAUL PtP 5 GHz: piattaforma <-> antenna direttiva a terra")
print("="*78)
# ground dish 23 dBi, platform 8 dBi. Tsys NF5
Tbh = tsys_from_nf(5)
gt_bh = gt(23.0, Tbh, L_rx=1)  # ground rx dish
print(f"  Ground dish G/T = {gt_bh:.1f} dB/K (23 dBi, NF5)")
bh = [
  ("5.8GHz aerostato r=5km  bw20M", 5800, 5, 20e6, 2, 8+23),  # eirp: P +8dBi plat +? handled below
  ("5.8GHz VTOL r=15km      bw20M", 5800, 15, 20e6, 3, 8+23),
  ("5.8GHz VTOL r=30km      bw20M", 5800, 30, 20e6, 3, 8+23),
]
# platform tx: 1W=0 dBW +8 dBi = 8 dBW EIRP
eirp_bh = 0 + 8
print(f"  EIRP piattaforma = {eirp_bh} dBW (1W, 8 dBi)")
print(f"  {'scenario':32s} {'FSPL':>7s} {'C/N0':>7s} {'SNR':>6s} verdetto")
for lab,f,d,bw,ex,_ in bh:
    L = fspl_db(f,d)+ex
    c0 = cn0(eirp_bh, L, gt_bh)
    s = snr_db(c0, bw)
    verdict = "OK" if s>10 else ("marg" if s>3 else "FAIL")
    print(f"  {lab:32s} {fspl_db(f,d):7.1f} {c0:7.1f} {s:6.1f}  {verdict}")

# ---------------------------------------------------------------------------
# D) LoRa IoT: sensore 14 dBm 868 MHz -> gateway airborne
# ---------------------------------------------------------------------------
print()
print("="*78)
print("D) IoT LoRa 868 MHz: sensore (14 dBm) -> gateway a bordo piattaforma")
print("="*78)
# LoRa SF12 BW125k sensitivity ~ -137 dBm. gateway antenna 3 dBi, NF6
Tlora = tsys_from_nf(6)
gt_lora = gt(3.0, Tlora, L_rx=1)
eirp_lora = (14-30)+2.0  # sensor 14dBm +2 dBi ant
# received power = EIRP - FSPL + Grx ; compare to sensitivity
print(f"  Sensore EIRP={eirp_lora:.1f} dBW; gateway 3 dBi; sensib SF12 ~ -137 dBm")
for lab,d in [("r=20km",20),("r=50km",50),("r=80km",80)]:
    L = fspl_db(868,d)+3
    prx_dbm = (eirp_lora+30) - L + 3.0   # +Grx 3dBi
    marg = prx_dbm-(-137)
    verdict="OK" if marg>10 else ("marg" if marg>0 else "FAIL")
    print(f"  LoRa SF12 {lab:8s}: FSPL={L-3:6.1f}  Prx={prx_dbm:6.1f} dBm  margin={marg:5.1f} dB  {verdict}")
