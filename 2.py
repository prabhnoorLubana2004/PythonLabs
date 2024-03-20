number1=int(input())
number2=int(input())
if number1 > number2:
    print(f"{number1} is larger.")

elif number1 < number2:
    print(f"{number2} is larger")

else:
    print("These numbers are equal")

# Simple Calculator
number1=float(input("The first number is:"))
number2=float(input("The second number is:"))
operation= input("Enter an operation(add,subtract,multipy,divide):")
if operation== "add":
    result= number1+number2
    print(f"{number1}+{number2}={result}")
elif operation == "subtract":
    result= number1 - number2
    print(f"{number1} - {number2}={result}")
elif operation == "multiply":
    result= number1*number2
    print(f"{number1}*{number2}={result}")
elif operation == "divide":
    if number2==0:
        print("Error")
    else:
        result= number1/number2
        print(f"{number1} / {number2}={result}")
else:
    print("Invalid operation")


# Multiples
number1=int(input("First Number:"))
number2=int(input("Second Number:"))
if number1 % number2==0:
    print(f"{number1} is a multiple of {number2}")
else:
    print("Not a multiple")