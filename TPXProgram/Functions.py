# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:28:38 2019

@author: Ricardo José Ramírez Barquero
"""

"""
Función de conversión de unidades para la realización de la biblioteca de 
cable triplex para OpenDSS.

A la función ingresan tres variables en este orden:
    - obj: Con la cual se define si el objetivo final de la conversión es milla
           o pie
    - unitActual: Define las unidades actuales del dato a ingresar, por lo señala
                  la unidad en la cual se inicia en el proceso de conversión.
    - value: El valor numérico del dato ingresado.
    
Esta función está definia para entregar los valores finales en Ohm/milla o en pie
por lo que cualquier combinación de unidades que se desee fuera de las anteriores
debe agregarse a la función.

V1.5: Agregado la conversión desde mils hasta milla y pies
"""

def unitConverter(obj,unitActual,value):
    temp=0
    if obj == 'mi':
        if unitActual=='mi':
            temp=value
        elif unitActual=='kft':
            temp=value*5.28
        elif unitActual=='km':
            temp=value*1.6093
        elif unitActual=='m':
            temp=value*1609.344
        elif unitActual=='Ft':
            temp=value*5280
        elif unitActual=='in':
            temp=value*63360
        elif unitActual=='cm':
            temp=value*160934.4
        elif unitActual=='mils':
            temp=value*(1.578E-8)
            
    elif obj=='Ft':
        if unitActual=='mi':
            temp=value*5280
        elif unitActual=='kft':
            temp=value*1000
        elif unitActual=='km':
            temp=value*3280.8399
        elif unitActual=='m':
            temp=value*3.2808
        elif unitActual=='Ft':
            temp=value
        elif unitActual=='in':
            temp=value*0.0833
        elif unitActual=='cm':
            temp=value*0.0328
        elif unitActual=='mils':
            temp=value*(8.33E-5)
            
    return temp