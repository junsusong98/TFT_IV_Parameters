import csv as cv
import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from setup_files import parameters as parameters


def plot(filename,foldername,Xaxisname,Yaxisname,log,title):

    for filename in filename:
        ld = pd.read_csv('./setup_files/data/'+foldername +'/' + filename +'.CSV',engine='python',header=0)
        V = pd.DataFrame(ld, columns=[Xaxisname])
        I = pd.DataFrame(ld, columns=[Yaxisname])
        min_i = I.min()
        max_i = I.max()
        print(filename)
        parameters.on_off_current_ratio(max_i,min_i)
        z = []
        y=np.array(I)
        for i in range(len(y)-1):
            z.append(2*(y[i]-y[i-1]))
        t=np.array(V)
        th=-y[z.index(max(z))]/max(z)+t[z.index(max(z))]
        print("Vth:",th) ## Vth
        # plt.show()
        log_I = I
        plt.title(title,fontsize=25)
        plt.xlabel(Xaxisname)
        plt.ylabel(Yaxisname)
        if log == True:
            plt.yscale('log')
        plt.plot(V,log_I,label=filename)
        y2=np.array(log_I)
        plt.legend()
        z2=[]
        for i in range(len(y2)-1):
            z2.append(2*(y2[i]-y2[i-1]))
        print("s.s:",max(z2)**-1) ## s.s

    plt.savefig('./setup_files/data/'+foldername+'/'+filename+'.png')
    plt.show()
