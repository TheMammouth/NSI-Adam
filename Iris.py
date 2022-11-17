# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:02:43 2022

@author: arist
"""

import csv #Comma Separated Values
from csv import DictReader 
#converti les lignes en Dictionnaire python {}
with open ("iris.csv") as f:
    table_fleur=[]
    lon_fleur=[]
    lar_fleur=[]
    couleur=[]
    for ligne in DictReader(f):
        ligne=dict(ligne) #on converti les infos de la ligne 
        lon_sep=float(ligne['longueur du sepale'])
        lar_sep=float(ligne['largeur du sepale'])
        if (ligne['espece']=='Iris-setosa'):
            couleur.append([1,0,0])  
        if (ligne['espece']=='Iris-versicolor'):
            couleur.append([0,1,0])
        if (ligne['espece']=='Iris-virginica'):
            couleur.append([0,0,1])
        lon_fleur.append(lon_sep)
        lar_fleur.append(lar_sep)
        