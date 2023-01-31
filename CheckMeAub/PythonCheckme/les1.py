import time

print("Hello You")
print("Ik ben Abdulrahman")
time.sleep(2)
naam = input ("wat is jou naam?")
time.sleep(1)
print("Goedemorgen " + naam)
age = int(input("hoe oud ben je?:"))
print("welkom "+ naam + " over 5 jaar ben je " + str(age+5)+" jaar oud")
time.sleep(2)
print(naam  + " Wil je mijn beter leren kennen?" )

antwoord = input("ja of Nee ")
teller = 0

if antwoord == "ja":
    print(" Mooi laat we dan bignnen.")
elif antwoord == "Nee":
    print("Nice to see you") 
    exit()

print(" wat is de sport die ik leuk vind?")
print("A kickboxen")
time.sleep(1)
print("B voetball")
time.sleep(1)
print("C zwemmen")
time.sleep(1)
antwoord = input(": ").upper()
if antwoord == "A":
    print ("Dat is goed")
    
elif antwoord == "B":
    print ("Dat is niet goed")

elif antwoord == "C":
    print ("Dat is goed")
    teller += 1
time.sleep(2)
print("Wat doe ik een mijn vrije tijd?")
time.sleep(1)
print("A Gamen met mijn broer")
time.sleep(1)
print("B Tiktok kijken")
time.sleep(1)
print("C slapen")
antwoord = input(": ").upper()

if antwoord == "A":
    print(" Dat is goed")
    teller += 1
elif antwoord == "B":   
    print(" Dat is niet goed")
elif antwoord == "C":
    print("Dat is niet goed")
    time.sleep(2)
    
print("Wat voor eten hou ik van?")
time.sleep(1)
print("A Pasta")
time.sleep(1)
print("B Pizza")
time.sleep(1)
print("C Doner")
antwoord = input(": ").upper()
time.sleep(2)
if antwoord == "A":
    print(" Dat is goed")
    teller += 1
elif antwoord == "B":   
    print(" Dat is niet goed")
elif antwoord == "C":
    print("Dat is niet goed")
time.sleep(1)
print(" jij hebt zowel punten: " + str(teller))

print("Als je 3 punten hebt je kunt mij goed.")
print("Als je 2 punten hebt je kunt mij beetje.")
print("Als je 1 punt hebt je kunt mijn heel kielen beetje.")
exit()
