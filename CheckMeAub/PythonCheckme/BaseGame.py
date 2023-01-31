import random
import time


class player():
    def normal_atk(self):
        attack = random.randint(0, 20)
        print("test", type(attack))
        return attack

    def spec_attack(self):
        spec_atk = random.randint(30, 50)
        print("test", type(spec_atk))
        return spec_atk

    def heal(self):
        healing = (20)
        return healing


def first_go():
    go = random.randint(0, 4)
    if go == 0:
        return 'Computer'
    else:
        return name


player_hp = 130
player_energy = 0
Computer_hp = 130
Computer_energy = 0

ready = input("bent u klaar om mij uit te dagen? Type Y/N: ")
name = input(" Aub voeg even u naam?: ")
turn = first_go
player = player()
Computer = player

while player_hp > 0 and Computer_hp > 0:
    print(f"\n{turn}'s turn")
    if turn != 'Computer':
        action = int(input(
            f"{name}, Aub neem u een actie:\n1)Normal Attack\n2) Special Attack\n3) heal\n"))
        if action == 1:
            player_normal_attack = player.normal_atk()
            Computer_hp = Computer_hp - player_normal_attack
            player_energy += 15
            time.sleep(2)
            print(f"\n{name} U deed {player_normal_attack} damage!")
            print(f"{name} U heeft nu {player_hp} heath en {player_energy} energy")
            time.sleep(2)
            turn = 'Computer'
        elif action == 2 and player_energy >= 20:
            player_special_attack = player.spec_attack()
            Computer = Computer_hp = player_special_attack
            player_energy -= 20
            time.sleep(2)
            print(f"\n{name} U deed {player_special_attack} damage!")
            print(f"{name} hij heeft nu {player_hp} health en {player_energy} energy")
            time.sleep(2)
            print(
                f"The Computer nu heeft {Computer_hp} health en {Computer_energy} energy")
            turn = 'Computer'
        elif action == 3 and player_energy >= 16:
            player_heal = player.heal()
            player_hp += player_heal
            player_energy -= 16
            time.sleep(1)
            print(f"\n{name} Heeft een beter hp {player_heal}")
            print(f"{name} heeft {player_hp} hp en {player_energy} energy")
            turn = 'Computer'
        elif action == 2 or action == 3 and player_energy < 15:
            print(f"\n{name} U heeft {player_hp} hp en {player_energy} energy")
            print(
                f"\n{name} U energy is te laag, vult u Aub keuze 1) Normal attack:")
        else:
            print("Aub Voeg het juiste actie")
    else:
        if Computer_hp < 50 and Computer_energy >= 15:
            Computer_heal = player.heal()
            Computer_hp + Computer_heal
            Computer_energy -= 15
            time.sleep(1)
            print(f"\nDe computer heeft een beter hp {Computer_hp}")
            print(f"{name} hij heeft nu {player_hp} hp en {player_energy} energy")
            time.sleep(1)
            print(
                f"De computer heeft nu {Computer_hp} hp en {Computer_energy} energy ")
            turn = name
        if Computer_energy >= 20:
            Computer_special_attack = player.spec_attack()
            player_hp = player_hp - Computer_special_attack
            Computer_energy -= 20
            time.sleep(1)
            print(f"\n De Computer just did {Computer_special_attack} damage")
            print(f"{name} nu heeft {player_hp} hp en {player_energy} energy")
            time.sleep(1)
            print(
                f" de Computer heeft nu {Computer_hp} hp en {Computer_energy} energy")
            turn = name

        else:
            Computer_normal_attack = player.normal_atk()
            player_hp = player_hp - Computer_normal_attack
            Computer_energy += 10
            time.sleep(1)
            print(f"nComputer deed  {Computer_normal_attack} damaged!")
            print(f"n{name} heeft nu {player_hp} hp en {player_energy} energy")
            print(
                f" The computer heeft nu { Computer_hp} hp and {Computer_energy}")
            turn = name

if player_hp <= 0:
    print("The Computer heeft gewonnen op dit round! ")
elif Computer_hp <= 0:
    print(f"\n{name} heeft gewonnen op dit round!")
