import random

print("""
*********************************************
* Dungeons & Dragons Combat Tool by Uğurcan *
*********************************************
""")

print("İnsiyatif Zarlarınızı atın!")
zar = range(1,21)

Enes = random.choice(zar)
uğur = random.choice(zar)
hidayet = random.choice(zar)
mustafa = random.choice(zar)
kadir = random.choice(zar)

print("Enes:",Enes)
print("uğur:",uğur)
print("hidayet:",hidayet)
print("mustafa",mustafa)
print("kadir",kadir)

oyuncular = [Enes,uğur,hidayet,mustafa,kadir]

sıralanmış_oyuncular = sorted(oyuncular)
print("Savaşa ilk {} başlayacak,sırasıyla {},{},{},{} devam edecek!".format(sıralanmış_oyuncular[0],sıralanmış_oyuncular[1],sıralanmış_oyuncular[2],
                                                              sıralanmış_oyuncular[3],sıralanmış_oyuncular[4]))






