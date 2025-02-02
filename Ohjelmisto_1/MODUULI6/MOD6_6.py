import math


def pizza(pizzahalk, pizzahint):
    sade = pizzahalk / 2.0
    pintaala = math.pi * sade ** 2 / 100
    mammamia = pizzahint * pintaala

    return mammamia


def main():
    pizza1halk = float(input("Sano ensimmäisen pizzan halkaisija: "))
    pizza1hint = float(input("sano ensimmisen pizzan hinta: "))
    pizza1laskettu = pizza(pizza1halk, pizza1hint)

    pizza2halk = float(input("Sano toisen pizzan halkaisija: "))
    pizza2hint = float(input("Sano toisen pizzan hinta: "))
    pizza2laskettu = pizza(pizza2halk, pizza2hint)

    if (pizza2laskettu < pizza1laskettu):
        print("Pizza 2 on halvempi")
    elif (pizza2laskettu > pizza1laskettu):
        print("Pizza 1 on halvempi")
    else:
        print("Pizzat ovat saman hintaiset.")


main()