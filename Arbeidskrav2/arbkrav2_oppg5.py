#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:53:04 2026

@author: marienavestadgundersen
"""

import numpy as np

a = float(input("Hva er verdien til a? "))  #[Ber bruker legge inn verdi for lengden "a"]
b = float(input(" Hva er verdien til b? "))  #[Ber bruker legge inn verdi for lengden "b"]

areal_trekant = a*b/2       #[Finner arealet av den rettvinklede trekanten]

r=a/2  #[Finner radius i halvsirkelen]

areal_halvsirkel = 1/2*np.pi*r**2  #[Finner arealet av halvsirkelen øverst]

total_areal = areal_trekant+ areal_halvsirkel  #[Legger sammen arealene for å få det totale arealet]

omkrets_trekant = b+ np.sqrt(a**2+b**2) #[Finner omkretsen av katet + hypotenus. Finner hypotenusen ved pytagoras]
omkrets_halvsirkel = a*np.pi/2  #[Finner omkretsen av halvsirkelen på toppen]

ytre_omkrets = omkrets_trekant+omkrets_halvsirkel  #[Legger sammen omkretsene for å få total ytre omkret]

print("Arealet av figuren med a = ", a, " og b = ", b, " er ", round(total_areal,2)," og ytre omkrets er ", round(ytre_omkrets,2))