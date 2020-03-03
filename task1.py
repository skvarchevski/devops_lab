#!/usr/bin/python3
m = int(input())
students = {}
for i in range(m):
    name, *args = input().split()
    avg_mark = sum(list(map(float, args))) / 3
    s = {name: avg_mark}
    students.update(s)
student_name = input()
print('%.2f' % students[student_name])
