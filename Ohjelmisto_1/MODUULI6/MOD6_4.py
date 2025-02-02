
import  math
luvut= []
yhteensa = sum(luvut)

def kokonaisluvut(luvut):
    for l in luvut:
        print (yhteensa)

def main():
    luku = input("Anna ensimmäinen luku:\n")
    while luku!="":
        luvut.append(luku)
        luku = input("Anna toinen luku tai paina Enter:\n")
    kokonaisluvut(luvut)


main()




