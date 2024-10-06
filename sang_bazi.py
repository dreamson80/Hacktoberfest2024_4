# Write your code here
number = int(input())
vorodi = []
for i in range(number):
    vorodi.append(input().strip())

vorodi_capital = []
for i in vorodi:
    a = i.capitalize()
    vorodi_capital.append(a)

columns = {i: set() for i in range(10)}

for i in vorodi_capital:
    color, column = i[0], int(i[1])
    columns[column].add(color)

count = 0
for i in columns.values():
    if {"W", "B", "G"}.issubset(i):
        count += 1

print(count)
