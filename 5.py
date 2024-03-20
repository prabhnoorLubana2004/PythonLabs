# 1. Functions for circumference and area of a circle
import math
rad = int(input("Enter the circle of radius:"))
def area (rad):
    a = math.pi * rad**2
    return a 
def circcumfencee (rad):
    c = 2*math.pi*rad
    return c

a = area(rad)
c = circcumfencee(rad)
print("The area of circle is",a)
print("the circumfence of circle is",c)

# area of rectangle
lengthRec = float(input("Enter the length of rectangle:"))
breadthRec = float(input("Enter the breadth of rectangle:"))

def area_rectangle (lengthRec,breadthRec):
    A = lengthRec * breadthRec
    return A
A = area_rectangle(lengthRec,breadthRec)
print(" The area of rectangle is",A)


# average interger

N = int(input("Enter the integer greater than 1: "))

def number(N):
    total = 0
    for i in range(1, N+1):
        total = i + total
    average =  total/N
    return average
average = number(N)
print("the average is",average)


# calculator
firstNumber = int(input("Enter the first number:"))
secondNumber = int(input("Enter the second number:"))
sign = input("Enter the sign:")

def add(a,b):
    return a +b
def subtract(a,b):
    return a -b
def multiply(a,b):
    return a *b
def divide(a,b):
    return a/b


if sign =="add":
    result = add(firstNumber,secondNumber)
elif sign =="subtract":
    result = subtract(firstNumber,secondNumber)
elif sign == "multiple":
    result = multiply(firstNumber,secondNumber)
elif sign == "divide":
    result = divide(firstNumber,secondNumber)
else:
    result = "Invalid"

print("The result is",result)
