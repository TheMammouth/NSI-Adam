# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:02:43 2022

@author: arist
"""

import csv #Comma Separated Values
from csv import DictReader 

with open ("iris.csv") as f:
    table_fleur=[]
    l_x=[]
    l_y=[]
    for ligne in DictReader(f):
        ligne=dict(ligne)
        print(ligne['longueur du sepale'])
        l_xappend(float)