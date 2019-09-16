# find the are of a trinagle*/
import math

shape = input("The Shape of the Object is: ")

if shape == 'triangle':
    b = int(input("Input the Base: "))
    h = int(input("Input the Height: "))
    area = 1 / 2 * b
    print("Area= ", area)
elif shape == "rectangle":
    b = int(input("Input the Base: "))
    h = int(input("Input the Height: "))
    area = b * h
    print("Area= ", area)
elif shape == "circle":
    r = int(input('Input the Radius: '))
    area = math.pi * r * r
    print("Area= ", area)
elif shape == "trapizoid":
    b1 = int(input("Input the base1: "))
    b2 = int(input("Input the base2: "))
    h1 = int(input("Input the height1: "))
    h2 = int(input("Input the height2: "))
    area = 1 / 2 * (b1 + b2) * (h1 + h2)
    print("Area= ", area)














