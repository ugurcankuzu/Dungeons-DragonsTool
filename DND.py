import random

print("""
**************************************
D&D DICE ROLLER by Uğurcan
**************************************

""")


while True:
    a = int(input("Lütfen Kaçlık Zar Atacağınızı Giriniz:"))

    if a == 2:
        x = [1,2]
        random.shuffle(x)
        y = random.choice(x)
        print("Zarınız :",y)
    elif a == 4:
        x = [1,2,3,4]
        random.shuffle(x)
        y = random.choice(x)
        print("Zarınız: ",y)

    elif a == 6:
        x = [1,2,3,4,5,6]
        random.shuffle(x)
        y = random.choice(x)
        print("Zarınız: ",y)
    elif a == 8:
        x = range(1,9)
        y = random.choice(x)
        print("Zarınız: ",y)
    elif a == 10:
        x = range(1,11)
        y = random.choice(x)
        print("Zarınız: ",y)
    elif a == 12:
        x = range(1,13)
        y = random.choice(x)
        print("Zarınız: ",y)
    elif a == 20:
        x = range(1,21)
        y = random.choice(x)
        print("Zarınız: ",y)
    elif a == 0:
        print("Bugünlük bu kadar oyun yeter galiba :)")
        break
    else:
        print("Lütfen geçerli bir zar gir DM :)")
