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
    def mus(self,kast):
        haetta = False
        if self.tilBaka == False:
            fra = nagdyrin[mus].stadsetning()+1
            til = nagdyrin[mus].stadsetning()+kast+1
            um = 1
        else:
            print("TIL BAKA")
            fra = nagdyrin[mus].stadsetning() - 1
            til = nagdyrin[mus].stadsetning() - self.tilBakaUm - 1
            um = - 1
        stada = nagdyrin[mus].stadsetning()
        for x in range(fra,til,um):
            print(x)
            if self.tilBaka == False:
                stada += 1
                print(stada, "Staða")
            else:
                stada -= 1
                print(stada, "Staða")
            for y in range(2, 5):
                rotta = nagdyrin[y].stadsetning()
                if stada == rotta:
                    print("Rotta", rotta, "er á reyti", stada)
                    print(nagdyrin[mus].afl(),"mús og rotta",nagdyrin[y].afl())
                    if nagdyrin[mus].afl() < nagdyrin[y].afl():
                        haetta = True
                        self.tilBaka = True
                        self.tilBakaUm = nagdyrin[y].afl()
                        print("Rotta afl TIL BAKA",nagdyrin[y].afl())
                        if stada-self.tilBakaUm < 0:
                            self.tilBakaUm = stada-self.tilBakaUm+abs(self.tilBakaUm)+1
                            print("Shabba if setning:",stada-self.tilBakaUm)
                        elif stada-self.tilBakaUm == 0:
                            self.tilBakaUm = self.tilBakaUm - 1
                    elif nagdyrin[mus].afl() == nagdyrin[y].afl():
                        stada = stada + 1
                        haetta = True
                hamstur = 1
                hamsturinn = nagdyrin[hamstur].stadsetning()
                if stada == hamsturinn:
                    print("Hamstur kastar um",nagdyrin[hamstur].afl(),"reiti")
                    stada = stada + nagdyrin[hamstur].afl()
                    print("Hamstur stada",stada)
            if haetta == True:
                break
        print("Staðsetningin 222",stada)
        nagdyrin[mus] = nagdyrin[mus].nyStadsetning(stada)
    def rotta(self,rotta,kast,afram):
        haetta = False
        if afram == 1:
            fra = nagdyrin[rotta].stadsetning()+1
            til = nagdyrin[rotta].stadsetning()+kast+1
            um = 1
        else:
            print("TIL BAKA")
            if self.tilBakaUm == 0:
                if nagdyrin[rotta].stadsetning() - kast - 1 < 1:
                    til = 0
                else:
                    til = nagdyrin[rotta].stadsetning() - kast - 1
            else:
                til = nagdyrin[rotta].stadsetning() - self.tilBakaUm - 1
            fra = nagdyrin[rotta].stadsetning() - 1
            um = - 1
            print(nagdyrin[rotta].stadsetning())
            print(self.tilBakaUm)
            print(fra,til,um)
        stada = nagdyrin[rotta].stadsetning()
        for x in range(fra,til,um):
            print(x)
            if afram == 1:
                stada += 1
                print(stada, "Staða Rotta")
            else:
                stada -= 1
                print(stada, "Staða Rotta")
            musStada = nagdyrin[mus].stadsetning()
            if stada == musStada:
                print("--- Rotta", rotta, "er á reyti", stada)
                print(nagdyrin[rotta].afl(), "rotta og mus", nagdyrin[mus].afl())
                if nagdyrin[rotta].afl() < nagdyrin[mus].afl():
                    haetta = True
                    self.tilBaka = True
                    self.tilBakaUm = nagdyrin[mus].afl()
                    print("Mús afl TIL BAKA", nagdyrin[mus].afl())
                    if stada - self.tilBakaUm < 0:
                        self.tilBakaUm = stada - self.tilBakaUm + abs(self.tilBakaUm) + 1
                        print("Shabba if setning:", stada - self.tilBakaUm)
                    elif stada - self.tilBakaUm == 0:
                        self.tilBakaUm = self.tilBakaUm - 1
                elif nagdyrin[mus].afl() == nagdyrin[rotta].afl():
                    stada = stada - 1
                    haetta = True
                else:
                    stada = stada - 1
                    haetta = True
            hamstur = 1
            hamsturinn = nagdyrin[hamstur].stadsetning()
            print("Hamstur stada",hamsturinn)
            if stada == hamsturinn:
                print("Hamstur stada",hamsturinn)
                if afram == 1:
                    stada = stada + 1
                    nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(hamsturinn-1)
                    haetta = True
                    print("Hamsturinn nýtttttt",nagdyrin[hamstur].stadsetning())
                else:
                    stada = stada - 1
                    nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(hamsturinn+1)
                    haetta = True
                    print("Hamsturinn nýtttttt",nagdyrin[hamstur].stadsetning())
            if haetta == True:
                break
        print("Rotta Staðsetning 222",stada)
        nagdyrin[rotta] = nagdyrin[rotta].nyStadsetning(stada)
    def hamstur(self, kast):
        hamstur = 1
        hamsturinn = nagdyrin[hamstur].stadsetning()
        musStada = nagdyrin[mus].stadsetning()
        if hamsturinn < musStada:
            afram = 1
        else:
            afram = 0
        haetta = False
        if afram == 1:
            fra = nagdyrin[hamstur].stadsetning() + 1
            til = nagdyrin[hamstur].stadsetning() + kast + 1
            um = 1
        else:
            print("TIL BAKA")
            fra = nagdyrin[hamstur].stadsetning() - 1
            til = nagdyrin[hamstur].stadsetning() - kast - 1
            um = - 1
        stada = nagdyrin[hamstur].stadsetning()
        for x in range(fra, til, um):
            print(x)
            if afram == 1:
                stada += 1
                print(stada, "Staða Hamstur")
            else:
                stada -= 1
                print(stada, "Staða Hamstur")
            musStada = nagdyrin[mus].stadsetning()
            if stada == musStada:
                print("Mús staða",musStada)
                haetta = True
            for y in range(2, 5):
                rotta = nagdyrin[y].stadsetning()
                if stada == rotta:
                    print("Rotta", rotta, "er á reyti", stada)
                    if afram == 1:
                        nagdyrin[y] = nagdyrin[y].nyStadsetning(stada-1)
                        stada = stada + 1
                        haetta = True
                        print("Rotta nýtttttt",nagdyrin[y].stadsetning())
                    else:
                        nagdyrin[y] = nagdyrin[y].nyStadsetning(stada+1)
                        stada = stada - 1
                        haetta = True
                        print("Rotta nýtttttt",nagdyrin[y].stadsetning())
            if haetta == True:
                break
        print("Hamstur Staðsetning 222", stada)
        nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(stada)




nagdyrin[3].prenta()
nagdyrin[3] = nagdyrin[3].nyStadsetning(3)
nagdyrin[3].prenta()
nagdyrin[3] = nagdyr("rotta", 3, 1)
nagdyrin[2] = nagdyr("rotta", 8, 7)
nagdyrin[0] = nagdyr("mús", 2, 10)
nagdyrin[1] = nagdyr("hamstur", 12, 13)
mus = 0
for x in range(5):
    nagdyrin[x].prenta()
print()
keyrsla = True
while keyrsla != False:
    kast = nagdyrin[mus].teningur()
    nyrReytur = kast + nagdyrin[mus].stadsetning()
    print("Hann kastaði",kast)
    fer = faerast()
    #fer.mus(6)
    #if fer.tilBaka == True:
    #    print("Til baka =",fer.tilBakaUm)
    #    print("Staðsetning mús =",nagdyrin[mus].stadsetning())
    #    fer.mus(fer.tilBakaUm)
    #    fer.tilBaka = False
    #nagdyrin[2].teningur()
    #print("Staðsetning músar",nagdyrin[mus].stadsetning())
    #rotta = 2
    #fer.rotta(rotta,6,0)
    #fer.tilBakaUm = 0
    #if fer.tilBaka == True:
     #   print("Til baka ROTTA =",fer.tilBakaUm)
      #  print("Staðsetning rotta =",nagdyrin[rotta].stadsetning())
       # fer.rotta(rotta,fer.tilBakaUm,0)
        #fer.tilBaka = False
    fer.hamstur(6)
    break

    ##### Þarf að gera ef hamstur lendir á sama reiti og mús þannig að músinni er kastað í næst þegar hún kastar