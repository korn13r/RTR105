# -*- coding: utf-8 -*-
from math import sin
def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**2/(1)
    S = a
    print("a0 = %6.2f S0 = %6.2f"%(a,S))
    
    while k < 10:
        k = k + 1
        R = (-1)*x*x*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        print(" a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        
    return S
print("Sin aprekinasana:")
x = float(input("Ievadi argumentu (x): "))
y = sin(x*x)
print("Sin((%.2f)^2) = %6.2f"%(x,y))

yy = mans_sinuss(x*x)
print("Sin((%.2f)^2) caur summu = %6.2f"%(x,yy))

print("                  500 ")
print("               __________")
print("               \ ")
print("                \                     k   4*k+2 ")
print("                 \                (-1) * x       ")
print(" Sin((%.2f)^2)  = >       ____________________________ "%(x))
print("                 /                 (2*K+1)! ")
print("                / ")
print("               / ")
print("               __________ ")
print("                  k=0")



print("                                    4 ")
print("                                 - x  ")
print("rekurences reizinatajs:___________________________")
print("")
print("                             2 * k * (2*k+1) ")












