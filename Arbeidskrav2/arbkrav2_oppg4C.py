#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:47:39 2026

@author: marienavestadgundersen
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.876]
        }

land = input("Skriv inn et land ").capitalize()
hovedstad = input("Skriv inn et hovedstaden i landet ").capitalize()
antall_innbyggere = float(input("Skriv inn antall innbyggere i hovedstaden "))



data[land] =[hovedstad, antall_innbyggere] 

print(data)