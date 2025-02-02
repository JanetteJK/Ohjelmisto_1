import random
summa = 0
nopat = int(input("Montako noppaa heitetään?:\n"))
for i in range (nopat):
    silmaluvut = (random.randint(1,6))
    print(silmaluvut)
    summa += silmaluvut
print(f"Silmälukujen summa on {summa}")


