liste = []
for x in range(1,6):
    a = 0
    for number in input().split():
        a += int(number)
    liste.append(a)


max_value = max(liste)
print(liste.index(max_value)+ 1)
print(max_value)


