#boolean-tyyppinen muuttuja, ilmoittaa onko luku alkuluku vai ei

onAlku = True
luku = int(input("Anna kokonaisluku:\n"))
for jakaja in range (2, luku//2):
    if luku % jakaja == 0:
        onAlku = False
        break
if (onAlku == True):
    print("Lukusi on alkuluku")
else:
    print("Lukusi ei ole alkuluku")
