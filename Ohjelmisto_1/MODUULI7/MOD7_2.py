names = set()
give_names = input("Give me a name:\n")
while give_names != "":
    for name in names:
        if name == give_names:
            print("Name already on list \n")
    names.add(give_names)
    give_names = input("Give me a new name or press enter:\n")
print(names)
