#!/usr/bin/python3
num = int(input("Enter number \n: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial is : ", end="")
print(factorial)
