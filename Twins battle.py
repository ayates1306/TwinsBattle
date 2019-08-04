import random
print("----------------------TWINS BATTLE SIMULATOR!!!!!v.B1.2.4----------------------")
print("")
print("Instructions:")
print("Your options are attack or heal. Type these in respectively to make your move.")
print("To start off, the Twins have around 500 health, you have around 300 health, and around 5 healing potions depending  on the difficulty, which     heal 100 health each. Your attack does 50 damage, unless you")
print("land a critical hit, or if you miss (random). Type 'E','N'or'H' to select Easy, Normal or Hard and summon the Twins and begin.")
Start = input()
Difficulty = ["E","N","H"]
while Start not in Difficulty:
    Start = input("Type the respective letters to select difficulty and begin.").upper()
if Start == "E":
    TwinsHealth = 450
    MaxP_Health = 300
    PlayerHealth = 300
    HealingPotions = 5
    Random_number1 = 3
    Random_number2 = 6
elif Start == "N":
    TwinsHealth = 500
    MaxP_Health = 300
    PlayerHealth = 300
    HealingPotions = 4
    Random_number1 = 4
    Random_number2 = 5
elif Start == "H":
    TwinsHealth = 500
    MaxP_Health = 250
    PlayerHealth = 250
    HealingPotions = 4
    Random_number1 = 5
    Random_number2 = 4
print ("The Twins have awoken!")
while TwinsHealth > 1:
    command = input("What is your move?").lower()
    if command == "attack":
        if Start == "E":
            Attack = 50
            if Random_number1 == random.randint(1,3):
                Attack = Attack + random.randint(10,20)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,6)):
                    print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
        elif Start == "N":
            Attack = 45
            if Random_number1 == random.randint(1,4):
                Attack = Attack + random.randint(5,20)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,5)):
                print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
        elif Start == "H":
            Attack = 40
            if Random_number1 == random.randint(1,5):
                Attack = Attack + random.randint(3,10)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,4)):
                print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
    elif command == "heal":
        HealingPotions = HealingPotions - 1
        PlayerHealth = PlayerHealth + 100
        if HealingPotions <1:
            PlayerHealth = PlayerHealth - 100
            print("You're out of healing potions!")
        elif PlayerHealth > MaxP_Health:
            PlayerHealth = MaxP_Health
            print("Your health is maxed out!")
        elif HealingPotions > 0:
            print("You drank a healing potion! Gained 100 health.")
    print("Twins health is" ,TwinsHealth, "!")
    if HealingPotions < 0:
                HealingPotions = 0
    print("You have" ,HealingPotions, "healing potions left!")
    if TwinsHealth < 1:
        print("The Twins have been defeated!")
        break
    else:
        if Random_number2 == random.randint(1,5):
            print("You dodged the Twins' attack!")
        else:
            if Start == "E":
                TwinsDamage = random.randint(25, 45)
            elif Start == "N":
                TwinsDamage = random.randint(25, 50)
            elif Start == "H":    
                TwinsDamage = random.randint(30, 55)
            print ("Twins attacked! Lost" ,TwinsDamage, "health!")
            PlayerHealth = PlayerHealth - TwinsDamage
            print("You have" ,PlayerHealth, "health!")
    if PlayerHealth < 1:
            print("You were slain...")
            break



