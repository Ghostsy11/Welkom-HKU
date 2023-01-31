import random

original = "hallo"
randomised = 'hallo'.join(random.sample(original, len(original)))
print(randomised)


def spaargeld(m1=100, m2=200):
    sum = m1 + m2
    return sum


result = spaargeld(100,)
print(result)


def groten(name, m):
    print("hallo", name)
    print(m)


name = str(input("Wat is je naam?: "))
groten(name, "What is going on")


a = 6  # het eerste getal van de berekening
op = "*"  # De soort berekening (rekenkundige operator)
b = 10  # het tweede getal van de berekening

# checken welke operator je hebt gekozen

if op == "+":  # Je kiest voor optellen
    result = a+b  # Bereken de uitkomst
elif op == "-":  # Je kiest voor aftrekken
    result = a-b  # Bereken de uitkomst
elif op == "/":  # Je kiest voor delen
    result = a/b  # Bereken de uitkomst
elif op == "*":  # Je kiest voor vermenigvuldigen
    result = a*b  # Bereken de uitkomst
elif op == "%":  # Je kiest voor restwaarde na deling (modulo)
    result = a % b  # Bereken de uitkomst
else:  # Je hebt geen geldige berekening gekozen
    result = 0

print(result)  # Print de uitkomst van je berekening


def my_function(x):
    return 5 * x


print(my_function(3) * my_function(5) +
      my_function(9) + my_function(20) + my_function(5))


def calculater():
    number1 = int(input("right the first nummber"))
    number2 = int(input("right the secund nummber"))
    print("uitkomst ", number1, "", number2, " =", number1 * number2)
    print("uitkomst ", number1, "+", number2, " =", number1 + number2)
    print("uitkomst ", number1, "-", number2, " =", number1 - number2)
    print("uitkomst ", number1, "/", number2, " =", number1 / number2)
    print("uitkomst ", number1, "%", number2, " =", number1 % number2)


calculater()
