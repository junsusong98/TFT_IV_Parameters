from setup_files import plot as plot

# Plot할 csv들의 이름을 적어 주세요 (리스트별로 plot)

ss_name = [
    'GateVia.SS',
    'GateVia2.SS',
    'NoGateVia.SS',

            ]

sd_name = [
    'GateVia2.SD',
    'GateVia2.SD_10Gate',
    'GateVia2.SD_20Gate',
]

gate_name = [
    'GateVia2.Gate',
    'NoGateVia.Gate',
]

sdg_name_ = [
    'GateVia.-20to20',
    'NoGateVia.-20to20',
    'GateVia2.-20to20'

]

refer_name = [
    'ITZO2_FMM_250_40.1',
    'ITZO2_FMM_250_40.2',
    'ITZO2_FMM_250_40',
]

refer_2_name = [
    'ITZO_FMM_250_40',
    'ITZO_FMM_250_40.1'
]

itzo_name = [
    'GateVia.ITZOvoltagesweep',
]

# plot할 csv가 들어가 있는 폴더를 적어 주세요

folder_name = '20210715'

#                             Xaxis    Yaxis
#                            -----------------
# source to source            DrainV   DrainI
# source to drain             DrainV   DrainI
# gate to gate                GateV    GateI
# gate on, source to drain    GateV    DrainI

# plot -> filename, foldername, Xaxisname, Yaxisname, log (Ture or False), title(graph name), arrow (True or False)

# 함수 적으면 실행

plot.plot(ss_name,folder_name,'DrainV','DrainI',False,'SourceToSource',False)
plot.plot(sd_name,folder_name,'DrainV','DrainI',False,'SourceToDrain',False)
plot.plot(gate_name,folder_name,'GateV','GateI',False,'GateToGate',False)
plot.plot(sdg_name_,folder_name,'GateV','DrainI',False,'SourceToDrain,GateOn',True)
plot.plot(refer_name,folder_name,'GateV','DrainI',True,'References_250_1',True)
plot.plot(refer_2_name,folder_name,'GateV','DrainI',True,'References_250_2',True)
    
    

    