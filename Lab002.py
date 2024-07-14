# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
import math

print("Welcome")
num = 2
sq = num ** 2
print(f"The square of {num} is {sq}")
c = num ** 3
print(f"The cube of {num} is {c}")

num = 2
sq = math.pow(num, 2)
print(f"The square of {num} is {sq}")
cube = math.pow(num, 3)
print(f"The cube of {num} is {cube}")
