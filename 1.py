"""
To calculate salary of an employee given his basic pay (take as input from user). Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions
"""

def gross_Sal(basic_pay):
    hra = (10/100)*basic_pay
    ta = (5/100)*basic_pay
    total_sal = basic_pay+hra+ta
    tax = (2/100)*total_sal
    net_sal = total_sal - tax
    return net_sal
basic_pay = float(input("Enter Basic Salary:- "))
print("Total Salary :- ",gross_Sal(basic_pay))
