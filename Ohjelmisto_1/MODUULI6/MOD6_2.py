import random


def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)


def main():
    tahkot = int(input("Moniko tahkoista noppaa heitetään?\n"))
    while True:
        silmaluku  = heitä_noppaa(tahkot)
        print(f"silmäluku on {silmaluku}")
        if silmaluku == tahkot:
            break
main()
