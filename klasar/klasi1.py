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
    def prenta(self):
        print("Ég er ",self.tegundin,"sem er staðsettur",self.stadsetningin,"og er með",self.aflid,"sem afl.")

