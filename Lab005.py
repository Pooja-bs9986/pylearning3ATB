#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1=int(input("enter num1\n"))
num2=int(input("enter num2\n"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num1} is lesser than {num2}")
else:
    print(f"{num1} is equal to {num2}")
