liste = []
anzahl = int(input(""))
for x in range(anzahl):
    eingabe = input("")
    liste.append(eingabe)
for i in range(0, len(liste), 2):
    print(liste[i])