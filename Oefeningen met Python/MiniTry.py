score = 0

print("Wilt u mee spelen?")
antwoord = input("ja of nee")
if antwoord == "ja":
    print(" Mooi laat we dan bignnen.")
elif antwoord == "nee":
    print("Nice to see you")
    exit()

print(" De spel is simple zolang u ja toevoegt u scoort als u nee toevoegt dan is het verrassing")
while True:
    klik = input("Ja of Nee :").upper()
    if klik == "Nee":
        print(" jij hebt zowel punten: " + str(score))
        print("U verloort")
        break
    elif klik == "JA":
        score += 1
        print(" jij hebt zowel punten: " + str(score))
    else:
        print("voeg de juiste antwoord!")
