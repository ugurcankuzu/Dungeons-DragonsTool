import random

print("""
**************************************
D&D DICE ROLLER by Uğurcan
**************************************

""")


while True:
    a = int(input("Please Choose Your Dice:"))

    if a == 2:
        x = [1,2]
        random.shuffle(x)
        y = random.choice(x)
        print("Dice :",y)
    elif a == 4:
        x = [1,2,3,4]
        random.shuffle(x)
        y = random.choice(x)
        print("Dice: ",y)

    elif a == 6:
        x = [1,2,3,4,5,6]
        random.shuffle(x)
        y = random.choice(x)
        print("Dice: ",y)
    elif a == 8:
        x = range(1,9)
        y = random.choice(x)
        print("Dice: ",y)
    elif a == 10:
        x = range(1,11)
        y = random.choice(x)
        print("Dice: ",y)
    elif a == 12:
        x = range(1,13)
        y = random.choice(x)
        print("Dice: ",y)
    elif a == 20:
        x = range(1,21)
        y = random.choice(x)
        print("Dice: ",y)
    elif a == 0:
        print("Hey DM! That's Enough For Today :)")
        break
    else:
        print("That's Wrong number. We haven't this dice yet DM :)")
