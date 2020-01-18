"""
To accept N numbers from user. Compute and display maximum in list, minimum in list, sum and average of numbers.
"""



n = int(input("How many Numbers you enter:- "))
l = []
print("Enter Numbers:- ")
for i in range(n):
    l.append(int(input()))
    
print("Maximum in list:- ",max(l))
print("Minimum in List:- ",min(l))
print("Sum of List",sum(l))
print("Average of List:- ",(sum(l))/n)
