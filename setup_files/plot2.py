import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
ld =[]
plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 9)
plt.rcParams['font.size'] = 15
filename = [
    'AS',
    '200°C',
    '300°C',
    '400°C'
]
folder_name = 'noiso_HP_100_50'
# for i in range(4):
#     ld[i] = pd.read_csv('./data/'+ folder_name +'/' + filename[i] +'.CSV',engine='python',header=0)
#     V[i] = pd.DataFrame(ld[i], columns=['GateV'])
#     I[i] = pd.DataFrame(ld[i], columns=['DrainI'])
#     I2[i] = pd.DataFrame(ld[i], columns=['GateI'])
# print(ld)

# def makeDF(n,ld,V,I,I_g):
#     filename = [
#         'AS_100(W)_50(L)',
#         '150C_100(W)_50(L)',
#         '200C_100(W)_50(L)',
#         '250C_100(W)_50(L)'
#     ]
#     folder_name = 'iso_HP_100_50'
#     ld = pd.read_csv('./data/'+ folder_name +'/' + filename[n] +'.CSV',engine='python',header=0)
#     V = pd.DataFrame(ld, columns=['GateV'])
#     I = pd.DataFrame(ld, columns=['DrainI'])
#     I_g = pd.DataFrame(ld, columns=['GateI'])
#     return ld,I,V,I_g

# makeDF(0,ld0,V0,I0,I0_g)
# makeDF(1,ld1,V1,I1,I1_g)
# makeDF(2,ld2,V2,I2,I2_g)
# makeDF(3,ld3,V3,I3,I3_g)
def ld(folder_name,filename):
    tmp = pd.read_csv(f"./data/{folder_name}/{filename}.csv",engine='python',header=0)
    return tmp

def setV0(folder_name,filename):
    tmp = pd.read_csv(f"./data/{folder_name}/{filename}.csv",engine='python',header=0)
    tmp_df = pd.DataFrame(tmp,columns=['GateV'])
    return tmp_df

def setI0(folder_name,filename):
    tmp = pd.read_csv(f"./data/{folder_name}/{filename}.csv",engine='python',header=0)
    tmp_df = pd.DataFrame(tmp,columns=['DrainI'])
    return tmp_df

def setI0_g(folder_name,filename):
    tmp = pd.read_csv(f"./data/{folder_name}/{filename}.csv",engine='python',header=0)
    tmp_df = pd.DataFrame(tmp,columns=['GateI'])
    return tmp_df

V0 = setV0(folder_name,filename[0])
ld0 = pd.read_csv('./data/'+ folder_name +'/' + filename[0] +'.CSV',engine='python',header=0)
V0 = pd.DataFrame(ld0, columns=['GateV'])
I0 = pd.DataFrame(ld0, columns=['DrainI'])
I0_g = pd.DataFrame(ld0, columns=['GateI'])

ld1 = pd.read_csv('./data/'+ folder_name +'/' + filename[1] +'.CSV',engine='python',header=0)
V0 = pd.DataFrame(ld0, columns=['GateV'])
I1 = pd.DataFrame(ld1, columns=['DrainI'])
I1_g = pd.DataFrame(ld1, columns=['GateI'])

ld2 = pd.read_csv('./data/'+ folder_name +'/' + filename[2] +'.CSV',engine='python',header=0)
V0 = pd.DataFrame(ld0, columns=['GateV'])
I2 = pd.DataFrame(ld2, columns=['DrainI'])
I2_g = pd.DataFrame(ld2, columns=['GateI'])

ld3 = pd.read_csv('./data/'+ folder_name +'/' + filename[3] +'.CSV',engine='python',header=0)
V0 = pd.DataFrame(ld0, columns=['GateV'])
I3 = pd.DataFrame(ld3, columns=['DrainI'])
I3_g = pd.DataFrame(ld3, columns=['GateI'])

fig, ax1 = plt.subplots()
ax1.set_title("Without Isolation",fontsize=30)
ax1.set_xlabel('Gate V [V]', fontsize=20)
ax1.set_ylabel('Drain I [A]',fontsize=20)
ax1.set_yscale('log')
ax1.set_ylim([10**-12, 10**-3])
# ax1.plot(V0, I0, label = filename[0])
# ax1.plot(V0, I1, label = filename[1])
# ax1.plot(V0, I2, label = filename[2])
# ax1.plot(V0, I3, label = filename[3])
for i in [I0,I1,I2,I3]:
    line = ax1.plot(V0, i)
    x = V0
    y = i
    # calculate position and direction vectors:
    x0 = x.iloc[range(len(x)-1)].values
    x1 = x.iloc[range(1,len(x))].values
    y0 = y.iloc[range(len(y)-1)].values
    y1 = y.iloc[range(1,len(y))].values
    xpos = (x0+x1)/2
    ypos = (y0+y1)/2
    xdir = x1-x0
    ydir = y1- y0
    for X,Y,dX,dY in zip(xpos, ypos, xdir, ydir):
        ax1.annotate("", xytext=(X,Y),xy=(X+0.001*dX,Y+0.001*dY),
                arrowprops=dict(arrowstyle="fancy",color = line[0].get_color()), size = 6)

ax2 = ax1.twinx()
ax2.set_ylabel('Gate I [A]',fontsize=20)
ax2.set_yscale('log')
ax2.set_ylim([10**-12, 10**-3])
ax2.plot(V0, I0_g,'', label = filename[0])
ax2.plot(V0, I1_g, label = filename[1])
ax2.plot(V0, I2_g, label = filename[2])
ax2.plot(V0, I3_g, label = filename[3])

ax2.legend()
ax2.legend(loc='upper left')

plt.show()


