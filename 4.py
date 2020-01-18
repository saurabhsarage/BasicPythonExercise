"""
To accept student’s five courses marks and compute his/her result. Student is passing if he/she scores marks equal to and above 40 in each course. If student scores aggregate greater than 75%, then the grade is distinction. If aggregate is 60>= and = and = and
"""

marks = []
print("Enter 5 Subject marks:- ")
for i in range(5):
    marks.append(float(input()))
if min(marks) >= 40:
    percent = (sum(marks)/500)*100
    if percent > 75:
        print("Pass With Distinction ",percent,"%")
    elif percent <= 75 and percent >=60:
        print("Pass With First Class",percent,"%")
    elif percent<60 and percent>=40:
        print("Pass With Second Class",percent,"%")
else:
    print("Student is Fail")
