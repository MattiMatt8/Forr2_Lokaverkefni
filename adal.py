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
mus = nagdyr(nagdyrin[0])
hamstur = nagdyr(nagdyrin[1])
keyrsla = True
print()
while keyrsla != False:
    for x in range(5):
        nagdyrin[x].prenta()
    break