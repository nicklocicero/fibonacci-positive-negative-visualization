#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:37:10 2018

@author: spy
"""

import pylab as plt
import math


numbersPositive = [-1, 1, 0, 1, 1]
numbersNegative = [1, -1, 0, -1, -1]
numbersX = [-2, -1, 0, 1, 2]

def gen(numbers, x, p, n):
    natural = True
    natural = True
    prev = 1
    curr = 1
    for i in range(3, numbers + 3):
        tmp = curr
        curr = curr + prev
        prev = tmp
        x.insert(0, -i)
        x.append(i)
        if natural:
            n.append(-curr)
            n.insert(0, -curr)
            p.append(curr)
            p.insert(0, curr)
            natural = False
        else:
            p.append(curr)
            p.insert(0, -curr)
            n.append(-curr)
            n.insert(0, curr)
            natural = True

gen(9, numbersX, numbersPositive, numbersNegative)

plt.plot(numbersX, numbersPositive)
plt.plot(numbersX, numbersNegative)
