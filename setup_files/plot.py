import csv as cv
import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from setup_files import parameters as parameters

plt.figure(figsize=(10, 9))
plt.rcParams['font.size'] = 15
def plot(filename,foldername,Xaxisname,Yaxisname,log,title,arrow):

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
        plt.title(title,fontsize=30)
        plt.xlabel('Gate V [V]', fontsize = 20)
        plt.ylabel('Drain I [A]',fontsize = 20)
        # plt.xlim([-20,10])
        # plt.ylim([10**-12, 10**-3])
        if log == True:
            plt.yscale('log')

        line = plt.plot(V,log_I,label=filename)[0]


        # plot arrow on each line:
        if arrow == True:
            x = V
            y = I

            # calculate position and direction vectors:
            x0 = x.iloc[range(len(x)-1)].values
            x1 = x.iloc[range(1,len(x))].values
            y0 = y.iloc[range(len(y)-1)].values
            y1 = y.iloc[range(1,len(y))].values
            xpos = (x0+x1)/2
            ypos = (y0+y1)/2
            xdir = x1-x0
            ydir = y1-y0

            for X,Y,dX,dY in zip(xpos, ypos, xdir, ydir):
                plt.annotate("", xytext=(X,Y),xy=(X+0.001*dX,Y+0.001*dY),
                arrowprops=dict(arrowstyle="fancy",color=line.get_color()), size = 6)

        else:
            plt.scatter(V,log_I, s=6)

        y2=np.array(log_I)
        plt.legend()
        z2=[]
        for i in range(len(y2)-1):
            z2.append(2*(y2[i]-y2[i-1]))
        print("s.s:",max(z2)**-1) ## s.s

    plt.savefig('./setup_files/data/'+foldername+'/'+filename+'.png')
    plt.legend() # loc='upper left'
    plt.show()

def plot3(filename,foldername,Xaxisname,Yaxisname,Yaxisname2,log,title,arrow):
    fig, ax1 = plt.subplots()
    print(filename)

    for filename in filename:

        ld = pd.read_csv('./setup_files/data/'+foldername +'/' + filename +'.CSV',engine='python',header=0)
        V = pd.DataFrame(ld, columns=[Xaxisname])
        I = pd.DataFrame(ld, columns=[Yaxisname])
        # min_i = I.min()
        # max_i = I.max()
        # print(filename)
        # parameters.on_off_current_ratio(max_i,min_i)
        # z = []
        # y=np.array(I)
        # for i in range(len(y)-1):
        #     z.append(2*(y[i]-y[i-1]))
        # t=np.array(V)
        # th=-y[z.index(max(z))]/max(z)+t[z.index(max(z))]
        # print("Vth:",th) ## Vth
        # # plt.show()
        log_I = I
        # plt.title(title,fontsize=25)
        # plt.xlabel('Gate Voltage(V)', fontsize = 20)
        # plt.ylabel('Drain Current(A)',fontsize = 20)
        # plt.xlim([-20,10])
        # plt.ylim([10**-12, 10**-3])
        if log == True:
            ax1.set_yscale('log')

        A = ax1.plot(V,log_I,label=filename)

        # plot arrow on each line:
        if arrow == True:
            x = V
            y = I

            # calculate position and direction vectors:
            x0 = x.iloc[range(len(x)-1)].values
            x1 = x.iloc[range(1,len(x))].values
            y0 = y.iloc[range(len(y)-1)].values
            y1 = y.iloc[range(1,len(y))].values
            xpos = (x0+x1)/2
            ypos = (y0+y1)/2
            xdir = x1-x0
            ydir = y1-y0

            for X,Y,dX,dY in zip(xpos, ypos, xdir, ydir):
                ax1.annotate("", xytext=(X,Y),xy=(X+0.001*dX,Y+0.001*dY),
                arrowprops=dict(arrowstyle="fancy",color=A.get_color()), size = 6)

        # else:
        #     ax1.scatter(V,log_I, s=6)

        # y2=np.array(log_I)
        # plt.legend()
        # z2=[]
        # for i in range(len(y2)-1):
        #     z2.append(2*(y2[i]-y2[i-1]))
        # print("s.s:",max(z2)**-1) ## s.s

    ax2 = ax1.twinx()
    for filename in filename:
        # ld = pd.read_csv('./setup_files/data/'+foldername +'/' + filename +'.CSV',engine='python',header=0)
        V = pd.DataFrame(ld, columns=[Xaxisname])
        I2 = pd.DataFrame(ld, columns=[Yaxisname2])

        log_I2 = I2
        # plt.title(title,fontsize=25)
        # plt.xlabel('Gate Voltage(V)', fontsize = 20)
        # plt.ylabel('Drain Current(A)',fontsize = 20)
        # plt.xlim([-20,10])
        # plt.ylim([10**-12, 10**-3])
        # if log == True:
        #     ax2.set_yscale('log')

        B = ax2.plot(V, log_I2, label=filename)


        # plot arrow on each line:
        # if arrow == True:
        #     x = V
        #     y = I2
        #
        #     # calculate position and direction vectors:
        #     x0 = x.iloc[range(len(x)-1)].values
        #     x1 = x.iloc[range(1,len(x))].values
        #     y0 = y.iloc[range(len(y)-1)].values
        #     y1 = y.iloc[range(1,len(y))].values
        #     xpos = (x0+x1)/2
        #     ypos = (y0+y1)/2
        #     xdir = x1-x0
        #     ydir = y1-y0
        #
        #     for X,Y,dX,dY in zip(xpos, ypos, xdir, ydir):
        #         ax2.annotate("", xytext=(X,Y),xy=(X+0.001*dX,Y+0.001*dY),
        #         arrowprops=dict(arrowstyle="fancy",color=B.get_color()), size = 6)
        #
        # else:
        #     ax2.scatter(V,log_I2, s=6)

    # plt.savefig('./setup_files/data/'+foldername+'/'+filename+'.png')
    plt.show()

