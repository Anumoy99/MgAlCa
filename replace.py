# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:29:57 2022

@author: anumo
"""

print("Welcome to the program !!")
#count=0
name= input('Enter the location and name of the txt file:')
name_output = input("Enter the name of the Output file:")

find = input("What do you wanna replace :")
repl = input("What do you wanna replace with: ")
with open(name) as f:
    if f:
        print("File opened successfully !")
    line=f.readline()
    with open(name_output,'w') as s:
        while line:
            l= line.replace(find,repl)
            s.write(l)
            #s.write('\n')
            #print(count)
            #count=count+1
            line=f.readline()
print("All Done!!")