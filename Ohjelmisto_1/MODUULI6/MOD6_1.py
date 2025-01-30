import random


def heitä_noppaa():
    return (random.randint(1,6))
def main():
    while True:
        silmaluku = heitä_noppaa()
        print(f"Silmäluku {silmaluku}")
        if silmaluku == 6:
            break
main()









