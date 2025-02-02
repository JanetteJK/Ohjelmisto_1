import math
luku = str(input("Anna luku:"))
pienin = math.inf
suurin = -math.inf
while luku!= "":
    luku = int(luku)
    if luku>suurin:
        suurin=luku
    if luku<pienin:
        pienin=luku
    luku = str(input("Anna luku:"))
print(f"luvuistasi pienin oli {pienin} ja suurin oli {suurin}")
