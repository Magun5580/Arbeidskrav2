#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:08:23 2026

@author: marienavestadgundersen
"""

antall_elever= int(input("Skriv inn antall elever "))

antall_elever_per_pizza=4

antall_pizzaer=(antall_elever +antall_elever_per_pizza - 1)// antall_elever_per_pizza #[Sørger for at det heller bestilles for mye enn for lite]

print(f'Dere må bestille {antall_pizzaer} pizzaer til {antall_elever} elever')

