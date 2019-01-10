# -*- coding: utf-8 -*-
resul=1
ListaResul=[]
while resul!=0:
    Ent=input()
    ListaEnt=list(map(int,Ent.split(" ")))

    if ListaEnt[0]<ListaEnt[1]:
        ListaResul.append("Crescente")
    
    if ListaEnt[0]>ListaEnt[1]:
        ListaResul.append("Decrescente")

    if ListaEnt[0]==ListaEnt[1]:
        resul=0

for i in ListaResul:
    print(i)
    