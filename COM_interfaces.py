# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:58:45 2019

@author: Ricardo José Ramírez Barquero 
"""

"""
Script necesario para utilizar OpenDSS con python, 
por lo que se debe importar primero en el script 
principal antes de empezar cualquier cosa.
"""

import comtypes.client as cc

def SetUpCOMInterface():
    DSSobj     = cc.CreateObject("OpenDSSEngine.DSS")
    DSSstart   = DSSobj.Start(0)
    DSStext    = DSSobj.Text
    DSScircuit = DSSobj.ActiveCircuit
    
    return DSSobj, DSSstart, DSStext, DSScircuit