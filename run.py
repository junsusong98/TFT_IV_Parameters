import csv as cv
import pandas as pd
import numpy as np
from setup_files import parameters as parameters
from matplotlib import pyplot as plt

csv_name = [
    '200_1',
    '200_20v_1',
    '200_20v_2',
    '250_1',
    '250_2',
    '250_3',
    '250_20v',
    '250_20v_2',
    '300_1',
    '300_2',
    '300_20v_1',
    'as depo_1',
    'as depo_20v_1',

            ]
for csv in csv_name:

    ld = pd.read_csv('./setup_files./data/' + csv +'.csv',engine='python',header=2)
    gateV = pd.DataFrame(ld, columns=['Gate Vg (V)'])
    drainI = pd.DataFrame(ld, columns=['Drain Id (A)'])
    plt.title(csv,fontsize=25)
    plt.xlabel("Gate V")
    plt.ylabel("Drain I")
    plt.plot(gateV,drainI)
    min_i = drainI.max()
    max_i = drainI.min()
    parameters.on_off_current_ratio(max_i,min_i)
    plt.show()
    log_drain = np.log(drainI)
    plt.plot(gateV,log_drain)
    plt.show()
    y=np.array(log_drain)
    z=[]
    for i in range(len(y)-1):
        z.append(2*(y[i]-y[i-1]))
    print(max(z)**-1) ## s.s
    