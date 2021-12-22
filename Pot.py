anzahl = int(input())
list = []
x = 0
for i in range(0, anzahl):
    list.append(int(input()))
for i in list:
    a = i % 10
    b = i//10
    x += (b**a)
print(x)

