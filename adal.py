# Óðinn og Matti
# 21.11.2017
from klasar.klasi1 import *
from klasar.klasi2 import *
from random import *


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
class faerast:
    tilBaka = False
    tilBakaUm = 0
    def rotta(self,rotta,kast):
        afram = randint(0,1)
        if afram == 1:
            for x in range(kast):
                print("Rotta",x)

    def mus(self,kast):
        haetta = False
        if self.tilBaka == False:
            fra = nagdyrin[mus].stadsetning()
            til = nagdyrin[mus].stadsetning()+kast+1
            um = 1
        else:
            print("TIL BAKA")
            fra = nagdyrin[mus].stadsetning()
            til = nagdyrin[mus].stadsetning() - self.tilBakaUm - 1
            um = - 1
        stada = nagdyrin[mus].stadsetning()
        for x in range(fra,til,um):
            print(x)
            if self.tilBaka == False:
                stada += 1
            else:
                stada -= 1
            for y in range(2, 5):
                rotta = nagdyrin[y].stadsetning()
                if x == rotta:
                    print("Rotta", rotta, "er á reyti", x)
                    print(nagdyrin[mus].afl(),"mús og rotta",nagdyrin[y].afl())
                    if nagdyrin[mus].afl() < nagdyrin[y].afl():
                        haetta = True
                        self.tilBaka = True
                        self.tilBakaUm = nagdyrin[y].afl()
                        if nagdyrin[mus].stadsetning()-self.tilBakaUm < 0:
                            self.tilBakaUm = nagdyrin[mus].stadsetning()-self.tilBakaUm+abs(self.tilBakaUm)+1
                        elif nagdyrin[mus].stadsetning()-self.tilBakaUm == 0:
                            self.tilBakaUm = self.tilBakaUm - 1
                    elif nagdyrin[mus].afl() == nagdyrin[y].afl():
                        stada = stada + 1
                        haetta = True
                hamstur = 1
                hamsturinn = nagdyrin[hamstur].stadsetning()
                if x == hamsturinn:
                    print("Hamstur kastar um",nagdyrin[hamstur].afl(),"reiti")
                    stada = stada + nagdyrin[hamstur].afl()
            if haetta == True:
                if self.tilBaka == True:
                    print()
                break
        print("Staðsetningin 222",stada)
        nagdyrin[mus] = nagdyrin[mus].nyStadsetning(stada)

nagdyrin[3].prenta()
nagdyrin[3] = nagdyrin[3].nyStadsetning(3)
nagdyrin[3].prenta()
mus = 0
keyrsla = True
while keyrsla != False:
    kast = nagdyrin[mus].teningur()
    nyrReytur = kast + nagdyrin[mus].stadsetning()
    print("Hann kastaði",kast)
    fer = faerast()
    fer.mus(6)
    if fer.tilBaka == True:
        print("Til baka =",fer.tilBakaUm)
        print("Staðsetning mús =",nagdyrin[mus].stadsetning())
        fer.mus(fer.tilBakaUm)
        fer.tilBaka = False
    nagdyrin[2].teningur()
    print("Staðsetning músar",nagdyrin[mus].stadsetning())
    break