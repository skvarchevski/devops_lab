#!/usr/bin/python3
keys = str(input("Enter keys \n: "))
list = keys.split(" ")
values = str(input("Enter values \n: "))
listval = values.split(" ")
dictionary = {}
for i in range(len(list)):
    if i < len(listval):
        dictionary[list[i]] = listval[i]
    else:
        dictionary[list[i]] = "None"
print(dictionary)