import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def subthreshold_swing():

    return

def saturation_mobility(Vgs,Vth,i):
    L =50*10E-6
    W =1000*10E-6
    Vgs = 1# csv 임포트
    Vth = 1 # Threshold 계산
    if i ==1 :
        Id = 20
    else:
        Id = 40

    gm = 2*Id/(Vgs-Vth)
    Ci = 17 * 10E-9 #F
    Vds = 1 # 변수
    mu_sat = (L*gm)/(W*Ci*Vds)

    return mu_sat

def on_off_current_ratio(on,off):
    on_off_current_ratio = on / off
    print('on_off_ratio:' , float(on_off_current_ratio))
    return  on_off_current_ratio

def threshold_volatge():

    return

