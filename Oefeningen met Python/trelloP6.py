fruitenlist = ['banana', 'appel', 'peer', 'sinnsappelsap', 'ananas']
x = fruitenlist.index("appel")
print(x)


list1 = []
print("jouw list is nog leeg!")
while True:
    print("typt u t om iets te toevoegen typt u v om iets te verwijderen \n:")
    antwoord = input()
    if antwoord == "t":
        print("wat wilt u graag toevoegen")
        antwoord = input()
        list1.append(antwoord)
    elif antwoord == "v":
        print("wat wilt u verwijderen?")
        antwoord = input()
        list1.remove(antwoord)
    print(list1)
