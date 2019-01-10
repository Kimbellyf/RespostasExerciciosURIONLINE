# -*- coding: utf-8 -*-

Ent=int(input())
ListaDiv=[]
cont=0
for i in range(Ent):
    cont+=1
    if Ent%cont==0:
        ListaDiv.append(cont)
for i in ListaDiv:
    print(i)
        
