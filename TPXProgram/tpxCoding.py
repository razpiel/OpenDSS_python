# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:40:11 2019

@author: Ricardo José Ramírez Barquero
"""
import Functions as UC
import numpy as np

# Inicialización de listas
name=[]
nphases=[]
units=[]
units=[]
normamps=[]
kron=[]

rcc=[]
rnn=[]
xcc=[]
xnn=[]
xdcc=[]
xdcn=[]

i=0

with open("TPXcode.dss","r") as f:
    data = f.readlines()


for line in data:
    words = line.split()
    
    # Separación de opciones basicas para OpenDSS    
    #print(words[1])
    name.append(words[1][8:])
    nphases.append(words[2])
    units.append(words[3])
    normamps.append(words[4])
    kron.append(words[5])
    #print(name[8:])
    
    # Obtencion de datos desde las lineas
    Rc=float(words[6][3:])
    Rn=float(words[7][3:])
    GMRc=float(words[8][5:])
    GMRn=float(words[9][5:])
    T=float(words[10][2:])
    Dc=float(words[11][3:])
    Dn=float(words[12][3:])
    
    # Formato de datos para impresión de los mismos
    rcc.append(str(round(UC.unitConverter('mi',words[13][7:],Rc)+0.0953,4)))
    rnn.append(str(round(UC.unitConverter('mi',words[13][7:],Rn)+0.0953,4)))
    rij=str(0.0953)
    
    xcc.append(str(round(0.12134*(np.log(1/UC.unitConverter('Ft',words[14][9:],GMRc))+7.93402),4)))
    xnn.append(str(round(0.12134*(np.log(1/UC.unitConverter('Ft',words[14][9:],GMRn))+7.93402),4)))
    
    Dcc=2*(UC.unitConverter('Ft',words[16][7:],T))+(UC.unitConverter('Ft',words[15][7:],Dc))
    Dcn=(UC.unitConverter('Ft',words[16][7:],T))+(0.5)*(UC.unitConverter('Ft',words[15][7:],Dc))+(0.5)*(UC.unitConverter('Ft',words[15][7:],Dn))
    
    xdcc.append(str(round(0.12134*(np.log(1/Dcc)+7.93402),4)))
    xdcn.append(str(round(0.12134*(np.log(1/Dcn)+7.93402),4)))
    
    
    #Crear archivo TPXLineCode.dss
with open("TPXcode_solved.dss", "w") as s:
    for line in data:    
        s.write("new Linecode."+name[i]+" "+nphases[i]+" "+units[i]+"\n")
        s.write("~ rmatrix=[ "+rcc[i]+" "+rij+" "+rij+" | "+rij+" "+rcc[i]+" "+rij+" | "+rij+" "+rij+" "+rnn[i]+" ]\n")
        s.write("~ xmatrix=[ "+xcc[i]+" "+xdcc[i]+" "+xdcn[i]+" | "+xdcc[i]+" "+xcc[i]+" "+xdcn[i]+" | "+xdcn[i]+" "+xdcn[i]+" "+xnn[i]+" ]\n")
        s.write("~ "+normamps[i]+"\n")
        s.write("~ "+kron[i]+"\n")

        i=i+1
    
s.close()    
f.close()
    
    