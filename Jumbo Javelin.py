anzahl =int(input())
list = []
for i in range(anzahl):
    eingabe = int(input())
    list.append(eingabe)
b = sum(list)
if anzahl > 1:
    anzahl -= 1
    print(b-anzahl)



