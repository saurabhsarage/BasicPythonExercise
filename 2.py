"""
To accept an object mass in kilograms and velocity in meters per second and display its momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity

"""

def cal_momentam(mass,velocity):
    momentam = mass*velocity
    return momentam

mass = float(input("Enter Mass Of Object (Kilogram):- "))
velocity = float(input("Enter Velocity Of Object(meter per second):- "))
print("Momentam of Object :- ",cal_momentam(mass,velocity),"kg-m/s")
