# -*- coding: utf-8 -*-
ent=int(input())
listaImpares=[]

for i in range(ent+1,ent+13,1):
    if i%2!=0:
        listaImpares.append(i)
        print("%d"%i)