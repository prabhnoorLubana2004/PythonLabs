#Ques 1
n = int(input("Enter an integer greater than 1: "))


# Check if input is greater than 1

if n <= 1:

   print("Invalid input. Please enter an integer greater than 1.")

else:

   # Initialize variables to store the sum and count of integers

   total = 0

   count = 0

   

   # Loop through all integers from 1 to n

   for i in range(1, n+1):

       total += i

       count += 1


   # Compute the average

   average = total / count


   print("The average of all integers from 1 to", n, "is", average)

#Ques 2
#The loop condition is While i < 11, but i is never incremented inside the loop. This will lead to an infinite loop, as i will always be 1.
#The variable SomeNumber is incremented by 1 in each iteration, but it should be incremented by the value of i to add integers from 1 to 10.

SomeNumber = 0
i = 1

while i < 11:
    SomeNumber += i
    i += 1

print(SomeNumber)
