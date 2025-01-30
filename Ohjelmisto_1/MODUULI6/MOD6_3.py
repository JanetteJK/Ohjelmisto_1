def bensiini(gallona):
    return gallona * 3.785
def main():
    gallona = int(input("Montako gallonaa bensiiniä haluat?\n"))
    while gallona>= 0:
        gallonat = bensiini(gallona)
        print(f"Se on {gallonat} litraa!")
        gallona = int(input("Montako gallonaa bensiiniä haluat?\n"))
main()