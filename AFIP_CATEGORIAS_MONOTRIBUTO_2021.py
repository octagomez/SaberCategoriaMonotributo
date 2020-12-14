# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:03:15 2020

@author: Escritorio
"""

# Funcionalidad
# Al igresar el promedio facturado por mes el sistema me dice en que categoria estoy de mono tributo y cuanto debera abonar
#funcionalidad 2 ingresar un monto total facturado al año y devuelve el promedio de facturacion mensual y en que categoria

# Crear un array de Categorias (A B C D E F G H I J K ), este array debe contener otro array con lso datos de la categoria 
# LETRA, 
# BRUTO_FACTURADO_ANUAL, 
# CUOTA_MENSUAL

import numpy as np

#declaro array bidimencional
categorias = np.array([["A",273453,2562],["B",410180,2864 ],["C",546907,3275],
              ["D",820361,3862],["E",1093014,5072],["F",1367268,6072],
              ["G",1640722,7082],["H",2278780,12383],["I",2677577,114852],
              ["J",3076353,17058],["K",3418170,19280]])

#print(categorias)

facturacion_media = float(input("Ingrese su facturacion media: $"))

def buscarCategoria (categorias,facturacion_media):
    #indicador = 0;
    #recorro por fila el array
    for row in categorias:
        
        for cat in row :
          
            tope_mensual = float(row[1]) / 12
            if(tope_mensual >= facturacion_media):
                return "Categoria : " + row[0] + "\n" + "Limite de Facturacion : $" + str(round(tope_mensual,2)) + "\n" + "Debera pagar por mes : $" + str(row[2])
            
cat_resultante = buscarCategoria (categorias,facturacion_media)         
print(cat_resultante)           



