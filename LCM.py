# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:53:11 2022

@author: anumo
"""
def lcm_of_2_num(x,y):
    a=x*1000
    b=y*1000
    c=int(a*b)
    lcm=c
    for i in range(2,c):
        if (i % a == 0) and (i % b == 0):
            lcm=i
            break
    return lcm/1000
    
    
print("Welcome to the program!!")
x1=input("Enter the lattice parameter of Al2Ca in X (3 decimal): ")
x1=float(x1)
x2=input("Enter the lattice parameter of orthogonal Mg in X (3 decimal): ")
x2=float(x2)

x_lcm = lcm_of_2_num(x1,x2)

print("LCM of X is :",x_lcm)

y1=input("Enter the lattice parameter of Al2Ca in Y (3 decimal): ")
y1=float(y1)
y2=input("Enter the lattice parameter of orthogonal Mg in Y (3 decimal):")
y2=float(y2)

y_lcm = lcm_of_2_num(y1,y2)

print("LCM of Y is ",y_lcm)

input("Press Enter to exit ;)")
    