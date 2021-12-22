eingabe = str(input(""))
ergebnis = 1
for i in range(0,len(eingabe)):
    speicher = eingabe[i]
    for y in range(i+1,len(eingabe)):
        if speicher == eingabe[y]:
            ergebnis = 0
            break
        
print(ergebnis)