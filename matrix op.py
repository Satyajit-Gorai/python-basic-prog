# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:41:51 2020

@author: Satyajit Gorai
"""
# MAtrix input
R =int(input("Enter the numberof rows :"))
C =int(input("Enter the numberof columns :"))
matrix=[]
print("Enter the matrix in row wise: ")
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
    print()
    
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()
    
print()
tot=0
msum=[]
a=0

for i in range(R):
    for j in range(C):
        if i==j:
            print(matrix[i][j])
            #msum[a]=matrix[i][j]
            tot += matrix[i][j]

#for i in msum:
 #   tot += i
    
print(tot)
            
            
            
            
            

        
