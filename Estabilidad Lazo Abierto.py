# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:48:40 2025

@author: aronc
"""

import cmath
import math

# Coeficientes
Cr,Cu,Cv = 1e-6,1e-7,1e-6
Re,Rr,Ru = 1e6,1e6,1e3

a = Cr*Cu*Cv*Re*Rr*Ru
b = (Cr*Cu*Re*Rr)+(Cr*Cu*Ru*Rr)+(Cr*Cv*Ru*Rr)+(Cv*Cu*Re*Rr)+(Cv*Cu*Re*Ru)
c = (Cr*Rr)+(Cu*Re)+(Cu*Rr)+(Cu*Ru)+(Cv*Rr)+(Cv*Ru)
d = 1

def resolver_cubica(a, b, c, d):
    """
    Resuelve ax³ + bx² + cx + d = 0
    Retorna las 3 raíces
    """
    # Cálculo de p y q
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # Discriminante
    discriminante = (q/2)**2 + (p/3)**3
    
    # Raíces cúbicas del discriminante
    u = (-q/2 + cmath.sqrt(discriminante))**(1/3)
    v = (-q/2 - cmath.sqrt(discriminante))**(1/3)
    
    # Raíces cúbicas complejas de la unidad
    omega = complex(-1/2, math.sqrt(3)/2)  # e^(2πi/3)
    omega2 = complex(-1/2, -math.sqrt(3)/2)  # e^(4πi/3)
    
    # Las tres raíces
    x1 = u + v - b/(3*a)
    x2 = omega*u + omega2*v - b/(3*a)
    x3 = omega2*u + omega*v - b/(3*a)
    
    return x1, x2, x3


raices = resolver_cubica(a, b, c, d)

print("Las tres raíces en control son:")
for i, raiz in enumerate(raices, 1):
    if abs(raiz.imag) < 1e-10:  # Es prácticamente real
        print(f"x{i} = {raiz.real:.6f}")
    else:
        print(f"x{i} = {raiz}")

# Coeficientes
Cr,Cu,Cv = 1e-6,1e-7,1e-6
Re,Rr,Ru = 1e5,1e6,1e3

a = Cr*Cu*Cv*Re*Rr*Ru
b = (Cr*Cu*Re*Rr)+(Cr*Cu*Ru*Rr)+(Cr*Cv*Ru*Rr)+(Cv*Cu*Re*Rr)+(Cv*Cu*Re*Ru)
c = (Cr*Rr)+(Cu*Re)+(Cu*Rr)+(Cu*Ru)+(Cv*Rr)+(Cv*Ru)
d = 1

def resolver_cubica(a, b, c, d):
    """
    Resuelve ax³ + bx² + cx + d = 0
    Retorna las 3 raíces
    """
    # Cálculo de p y q
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # Discriminante
    discriminante = (q/2)**2 + (p/3)**3
    
    # Raíces cúbicas del discriminante
    u = (-q/2 + cmath.sqrt(discriminante))**(1/3)
    v = (-q/2 - cmath.sqrt(discriminante))**(1/3)
    
    # Raíces cúbicas complejas de la unidad
    omega = complex(-1/2, math.sqrt(3)/2)  # e^(2πi/3)
    omega2 = complex(-1/2, -math.sqrt(3)/2)  # e^(4πi/3)
    
    # Las tres raíces
    x1 = u + v - b/(3*a)
    x2 = omega*u + omega2*v - b/(3*a)
    x3 = omega2*u + omega*v - b/(3*a)
    
    return x1, x2, x3


raices = resolver_cubica(a, b, c, d)

print("Las tres raíces en caso 1 son:")
for i, raiz in enumerate(raices, 1):
    if abs(raiz.imag) < 1e-10:  # Es prácticamente real
        print(f"x{i} = {raiz.real:.6f}")
    else:
        print(f"x{i} = {raiz}")

# Coeficientes
Cr,Cu,Cv = 1e-6,1e-7,1e-7
Re,Rr,Ru = 1e6,1e6,1e3

a = Cr*Cu*Cv*Re*Rr*Ru
b = (Cr*Cu*Re*Rr)+(Cr*Cu*Ru*Rr)+(Cr*Cv*Ru*Rr)+(Cv*Cu*Re*Rr)+(Cv*Cu*Re*Ru)
c = (Cr*Rr)+(Cu*Re)+(Cu*Rr)+(Cu*Ru)+(Cv*Rr)+(Cv*Ru)
d = 1

def resolver_cubica(a, b, c, d):
    """
    Resuelve ax³ + bx² + cx + d = 0
    Retorna las 3 raíces
    """
    # Cálculo de p y q
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # Discriminante
    discriminante = (q/2)**2 + (p/3)**3
    
    # Raíces cúbicas del discriminante
    u = (-q/2 + cmath.sqrt(discriminante))**(1/3)
    v = (-q/2 - cmath.sqrt(discriminante))**(1/3)
    
    # Raíces cúbicas complejas de la unidad
    omega = complex(-1/2, math.sqrt(3)/2)  # e^(2πi/3)
    omega2 = complex(-1/2, -math.sqrt(3)/2)  # e^(4πi/3)
    
    # Las tres raíces
    x1 = u + v - b/(3*a)
    x2 = omega*u + omega2*v - b/(3*a)
    x3 = omega2*u + omega*v - b/(3*a)
    
    return x1, x2, x3


raices = resolver_cubica(a, b, c, d)

print("Las tres raíces en control son:")
for i, raiz in enumerate(raices, 1):
    if abs(raiz.imag) < 1e-10:  # Es prácticamente real
        print(f"x{i} = {raiz.real:.6f}")
    else:
        print(f"x{i} = {raiz}")
