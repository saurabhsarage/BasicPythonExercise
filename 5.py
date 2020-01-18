"""
To check whether input number is Armstrong number or not. An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.
"""
n = input("Enter Number:- ")
l = []
b = int(n)
s=0
for i in n:
    l.append(i)   
for i in l:
    s = (int(i)*int(i)*int(i))+s
if s == int(n):
    print("Number Is Armstrong")
