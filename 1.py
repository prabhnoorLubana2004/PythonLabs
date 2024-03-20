print("Welcome")
firstName=input("Enter your first name:")
lastName=input("Enter your last name:")
age=(input("Enter your age: " ))
gpa=(input("Enter your GPA:"))
major=(input("Enter your major:"))
address=(input("Enter your address:"))
print(f"Hello,{firstName},{lastName}. You are {age} old and studying {major} with {gpa}. Your address is {address}")




#Area of Trapezoid
base1=int(input("Length of side 1:"))
base2=int(input("Length of side 2:"))
height=int(input("Height of trapezoid:"))
Area= ((base1+base2)*height)/2
print("The are of Trapezoid is:",Area)


#Volume of a cube
L=4
V=L**3 #Volume of cube: side**3
print("The Volume of Cube:", V)


# Circumference and Area of Triangle

r=2
C= 2*3.14*r
A= 3.14*r*r
print(f"The Circumference is {C}, The Area is {A}")


#Average of five numbers
sum= 1+2+3+4+5
average= sum/5
print("average is", average)