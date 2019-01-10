# -*- coding: utf-8 -*-

A=1
ListaResul=[]
while A==1:
    B=input().split(" ")
    ListaEnt=list(map(int,B))
    Mult,Va=ListaEnt[0],ListaEnt[1]
    if Mult==0 and Va==0:
        A=2
        break
    ValorNovo=Mult*Va
    ListaResul.append(ValorNovo)

for i in ListaResul:
    print(i)
    
    
    
