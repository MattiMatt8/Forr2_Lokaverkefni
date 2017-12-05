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
        if nagdyrin[mus].stadsetning() == nagdyrin[1].stadsetning():
            fra = nagdyrin[mus].stadsetning()+nagdyrin[1].afl()+1
            til = nagdyrin[mus].stadsetning()+nagdyrin[1].afl()+kast+1
            um = 1
            nagdyrin[mus] = nagdyrin[mus].nyStadsetning(nagdyrin[mus].stadsetning()+nagdyrin[1].afl())
            print("Hamstur kastar mús um",nagdyrin[1].afl(),"reiti")
        elif self.tilBaka == False:
            fra = nagdyrin[mus].stadsetning()+1
            til = nagdyrin[mus].stadsetning()+kast+1
            um = 1
        else:
            fra = nagdyrin[mus].stadsetning() - 1
            til = nagdyrin[mus].stadsetning() - self.tilBakaUm - 1
            um = - 1
        stada = nagdyrin[mus].stadsetning()
        for x in range(fra,til,um):
            if self.tilBaka == False:
                stada += 1
            else:
                stada -= 1
            for y in range(2, 5):
                rotta = nagdyrin[y].stadsetning()
                if stada == rotta:
                    print("Mús afl",nagdyrin[mus].afl())
                    print("Rotta afl",nagdyrin[y].afl())
                    if nagdyrin[mus].afl() < nagdyrin[y].afl():
                        haetta = True
                        self.tilBaka = True
                        self.tilBakaUm = nagdyrin[y].afl()
                        print("Rotta vinnur og kastar mús til baka um",nagdyrin[y].afl(),"reiti")
                        if stada-self.tilBakaUm < 0:
                            self.tilBakaUm = stada-self.tilBakaUm+abs(self.tilBakaUm)+1
                        elif stada-self.tilBakaUm == 0:
                            self.tilBakaUm = self.tilBakaUm - 1
                    elif nagdyrin[mus].afl() == nagdyrin[y].afl():
                        stada = stada + 1
                        haetta = True
                        print("Rotta og mús hafa sama afl og mús fer fram um einn reit")
                hamstur = 1
                hamsturinn = nagdyrin[hamstur].stadsetning()
                if stada == hamsturinn:
                    print("Hamstur kastar mús um",nagdyrin[hamstur].afl(),"reiti")
                    stada = stada + nagdyrin[hamstur].afl()
            if haetta == True:
                break
        if stada > 100:
            stada = 100
        nagdyrin[mus] = nagdyrin[mus].nyStadsetning(stada)
    def rotta(self,rotta,kast,afram):
        haetta = False
        if afram == 1:
            fra = nagdyrin[rotta].stadsetning()+1
            til = nagdyrin[rotta].stadsetning()+kast+1
            um = 1
        else:
            if self.tilBaka == False:
                if nagdyrin[rotta].stadsetning() - kast - 1 < 1:
                    til = 0
                else:
                    til = nagdyrin[rotta].stadsetning() - kast - 1
            else:
                til = nagdyrin[rotta].stadsetning() - self.tilBakaUm - 1
            fra = nagdyrin[rotta].stadsetning() - 1
            um = - 1
        stada = nagdyrin[rotta].stadsetning()
        for x in range(fra,til,um):
            if afram == 1:
                stada += 1
            else:
                stada -= 1
            musStada = nagdyrin[mus].stadsetning()
            if stada == musStada:
                print("Mús afl",nagdyrin[mus].afl())
                print("Rotta afl",nagdyrin[rotta].afl())
                if nagdyrin[rotta].afl() < nagdyrin[mus].afl():
                    haetta = True
                    self.tilBaka = True
                    self.tilBakaUm = nagdyrin[mus].afl()
                    print("Rottu kastað til baka um", nagdyrin[mus].afl(),"reiti")
                    if stada - self.tilBakaUm < 0:
                        self.tilBakaUm = stada - self.tilBakaUm + abs(self.tilBakaUm) + 1
                    elif stada - self.tilBakaUm == 0:
                        self.tilBakaUm = self.tilBakaUm - 1
                elif nagdyrin[mus].afl() == nagdyrin[rotta].afl():
                    stada = stada - 1
                    haetta = True
                    print("Rotta og mús hafa sama afl og rotta fer tilbaka um einn reit")
                else:
                    stada = stada - 1
                    haetta = True
            hamstur = 1
            hamsturinn = nagdyrin[hamstur].stadsetning()
            if stada == hamsturinn:
                print("Hamstur og rotta á sama reit",hamsturinn)
                if afram == 1:
                    stada = stada + 1
                    nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(hamsturinn-1)
                    haetta = True
                    print("Rotta fer áfram um einn reit")
                    print("Hamsturinn fer aftur á bak um einn reit")
                else:
                    stada = stada - 1
                    nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(hamsturinn+1)
                    haetta = True
                    print("Rotta fer aftur á bak um einn reit")
                    print("Hamsturinn fer áfram um einn reit")
            if haetta == True:
                break
        if stada > 100:
            stada = 100
        elif stada < 1:
            stada = 1
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
            fra = nagdyrin[hamstur].stadsetning() - 1
            til = nagdyrin[hamstur].stadsetning() - kast - 1
            um = - 1
        stada = nagdyrin[hamstur].stadsetning()
        for x in range(fra, til, um):
            if afram == 1:
                stada += 1
            else:
                stada -= 1
            musStada = nagdyrin[mus].stadsetning()
            if stada == musStada:
                print("Mús á sama reit og hamstur")
                print("Hamsturinn kastar músinni í næstu umferð")
                haetta = True
            for y in range(2, 5):
                rotta = nagdyrin[y].stadsetning()
                if stada == rotta:
                    print("Rotta og Hamstur á sama reiti")
                    if afram == 1:
                        nagdyrin[y] = nagdyrin[y].nyStadsetning(stada-1)
                        stada = stada + 1
                        haetta = True
                        print("Hamsturinn fer áfram um einn reit")
                        print("Rotta fer aftur á bak um einn reit")
                    else:
                        nagdyrin[y] = nagdyrin[y].nyStadsetning(stada+1)
                        stada = stada - 1
                        haetta = True
                        print("Hamsturinn fer aftur á bak um einn reit")
                        print("Rotta fer áfram um einn reit")
            if haetta == True:
                break
        if stada > 100:
            stada = 100
        elif stada < 1:
            stada = 1
        nagdyrin[hamstur] = nagdyrin[hamstur].nyStadsetning(stada)
def linur():
    print("-\t-\t-\t-\t-\t-")
mus = 0
keyrsla = True
while keyrsla != False:
    fer = faerast()
    kast = randint(1,6)
    linur()
    print("  Músin kastaði")
    teningur(kast)
    linur()
    fer.mus(kast)
    if fer.tilBaka == True:
        print("Músinni er kastað til baka um",fer.tilBakaUm)
        fer.mus(fer.tilBakaUm)
        fer.tilBaka = False
    print("Ný staðsetning músarinnar:",nagdyrin[mus].stadsetning())
    nagdyrin[2].teningur()
    rotta1 = 2
    kast = randint(1,6)
    afram = randint(0,1)
    linur()
    print("  Rotta 1 kastaði")
    teningur(kast)
    linur()
    fer.rotta(rotta1,kast,afram) # Rotta 1
    if fer.tilBaka == True:
        print("Til baka ROTTA =",fer.tilBakaUm)
        fer.rotta(rotta1,fer.tilBakaUm,0)
        fer.tilBaka = False
    print("Ný staðsetning rottunnar:",nagdyrin[rotta1].stadsetning())
    rotta2 = 3
    kast = randint(1,6)
    afram = randint(0,1)
    linur()
    print("  Rotta 2 kastaði")
    teningur(kast)
    linur()
    fer.rotta(rotta2,kast,afram) # Rotta 2
    if fer.tilBaka == True:
        print("Til baka ROTTA =",fer.tilBakaUm)
        fer.rotta(rotta2,fer.tilBakaUm,0)
        fer.tilBaka = False
    print("Ný staðsetning rottunnar:",nagdyrin[rotta2].stadsetning())
    linur()
    rotta3 = 4
    kast = randint(1,6)
    afram = randint(0,1)
    linur()
    print("  Rotta 3 kastaði")
    teningur(kast)
    linur()
    fer.rotta(rotta3,kast,afram) # Rotta 3
    if fer.tilBaka == True:
        print("Til baka ROTTA =",fer.tilBakaUm)
        fer.rotta(rotta3,fer.tilBakaUm,0)
        fer.tilBaka = False
    print("Ný staðsetning rottunnar:",nagdyrin[rotta3].stadsetning())
    linur()
    print("  Hamstur kastaði")
    teningur(kast)
    linur()
    kast = randint(1,6)
    fer.hamstur(kast)
    print("Ný staðsetning hamstursins :",nagdyrin[1].stadsetning())
    stadsetningar = {nagdyrin[mus].stadsetning():"Mús",nagdyrin[1].stadsetning():"Hamstur",nagdyrin[rotta1].stadsetning():"Rotta 1",nagdyrin[rotta2].stadsetning():"Rotta 2",nagdyrin[rotta3].stadsetning():"Rotta 3"}

    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-")
    print("\t\t\tStaðsetning á öllum")
    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-")
    print("Dýr\t\t| ",end=" ")
    for k,v in sorted(stadsetningar.items()):
        print(v,end="\t\t")
    print()
    print("Reitur\t| ",end=" ")
    for k,v in sorted(stadsetningar.items()):
        print(k,end="\t\t\t")
    print()
    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-")
    if nagdyrin[mus].stadsetning() == 100:
        for x in range(5):
            nagdyrin[x].prenta()
        print()
        print("  Músinn VANN")
        break
