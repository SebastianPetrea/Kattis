anzahl = int(input())
liste = []
for i in range(anzahl):
    zahlen = int(input())
    liste.append(zahlen)
for x in reversed(liste):
    print(x)
