# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:43:37 2025

@author: danie
Pythagorean triple Finder
"""

import math

year=2025

print("when", year, "is c which is the hypotenuse")
for n in range(int(math.sqrt(year))):
    m=math.sqrt(year-n**2)
    if m==int(m):
        if math.gcd(int(m), n) == 1:
            print("n=",n,"m=",m," ", "|", m**2-n**2, 2*m*n, m**2+n**2)

print("-"*20)
print("when", year, "is a which is a leg")
time=10**8
for n in range(time):
    m=math.sqrt(year+n**2)
    if m==int(m):
        if math.gcd(int(m), n) == 1:
            print("n=",n,"m=",m," ", "|", m**2-n**2, 2*m*n, m**2+n**2)
    if n%(time/10)==0:
        print(round(n/time,2))