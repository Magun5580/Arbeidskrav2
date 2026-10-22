#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:30:08 2026

@author: marienavestadgundersen
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.876]
        }

land = input("Skriv inn et av landene: Norge, England, Frankrike eller Italia ").capitalize()


hovedstad = data[land][0]
antall_innbyggere = data[land][1]

print(f'{hovedstad} er hovedstaden i {land}  og det er {antall_innbyggere} millioner innbyggere i {hovedstad}')





