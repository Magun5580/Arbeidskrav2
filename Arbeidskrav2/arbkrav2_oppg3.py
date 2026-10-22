#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:17:07 2026

@author: marienavestadgundersen
"""

import numpy as np

v_grad = float(input("Skriv inn gradtallet "))

v_rad = v_grad*np.pi/180  #[Regner om tallet fra grader til radianer]

print(f' {v_grad} grader er {round(v_rad,3)} radianer')