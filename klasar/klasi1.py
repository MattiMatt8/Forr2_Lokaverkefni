# Óðinn og Matti
# 21.11.2017
from random import *

class nagdyr:
    def __init__(self,tegund,stadsetning,afl):
        self.tegundin = tegund
        self.stadsetningin = stadsetning
        self.aflid = afl
    def __str__(self):
        return "nagdyr(" + str(self.tegundin) + ", " + str(self.stadsetningin) + ", " + str(self.aflid) + ")"
    __repr__ = __str__
    def stadsetning(self):
        return self.stadsetningin
    def tegund(self):
        return self.tegundin
    def afl(self):
        return self.aflid
    def teningur(self):
        return randint(1,6)
    def prenta(self):
        print("Ég er",self.tegundin,"og er staðsett/ur á reiti",self.stadsetningin,"og er með",self.aflid,"sem afl.")
    def nyStadsetning(self,ny):
        return nagdyr(self.tegundin,ny,self.aflid)



