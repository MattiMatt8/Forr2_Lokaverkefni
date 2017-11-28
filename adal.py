# Óðinn og Matti
# 21.11.2017
from klasar.klasi1 import *
from klasar.klasi2 import *


nagdyrin = []
afl = [2,4,6]
nagdyrin.append(nagdyr("mús",1,afl[randint(0,2)]))
nagdyrin.append(nagdyr("hamstur",randint(2,100),afl[randint(0,2)]))
for x in range(3):
    nagdyrin.append(nagdyr("rotta", randint(2, 100), afl[randint(0, 2)]))
print(nagdyrin)
print()
for x in range(5):
    nagdyrin[x].prenta()

print()
#nagdyrin[0].prenta()
#nagdyrin[0] = nagdyrin[0].nyStadsetning(100)
#nagdyrin[0].prenta()

nagdyrin[3].prenta()
nagdyrin[3] = nagdyrin[3].nyStadsetning(3)
nagdyrin[3].prenta()
mus = 0
def rotturStad(kast):
    haetta = False
    tilBaka = False
    tilBakaUm = 0
    if tilBaka == False:
        fra = nagdyrin[mus].stadsetning()
        til = nagdyrin[mus].stadsetning()+kast+1
        um = 1
    else:
        print("TIL BAKA")
        fra = nagdyrin[mus].stadsetning()
        til = nagdyrin[mus].stadsetning() - tilBakaUm + 1
        um = -1
    for x in range(fra,til,um):
        print(x)
        for y in range(2, 5):
            rotta = nagdyrin[y].stadsetning()
            if x == rotta:
                print("Rotta", rotta, "er á reyti", x)
                if nagdyrin[mus].afl() < nagdyrin[y].afl():
                    haetta = True
                    tilBaka = True
                    tilBakaUm = nagdyrin[y].afl()
                elif nagdyrin[mus].afl() == nagdyrin[y].afl():
                    haetta = True
        if haetta == True:
            if tilBaka == True:
                print()
            break
keyrsla = True
while keyrsla != False:
    kast = nagdyrin[mus].teningur()
    nyrReytur = kast + nagdyrin[mus].stadsetning()
    print("Hann kastaði",kast)
    rotturStad(kast)
    break