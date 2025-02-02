def parilliset(numerot):
    parilliset = []
    for x in numerot:
        if x % 2 == 0:
            parilliset.append(x)
    return parilliset

def main():
    numerot = [1,2,4,8,6,7]
    lista_2 = parilliset(numerot)
    print(f"Listan luvut olivat {numerot}, parittomat poistettua on lista {lista_2}")

main()