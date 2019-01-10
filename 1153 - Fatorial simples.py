# -*- coding: utf-8 -*-
def Fatorial(Numero):
    f=1
    while Numero>1:
        f*=Numero
        Numero-=1
    return f

Ent=int(input())
print(Fatorial(Ent))
