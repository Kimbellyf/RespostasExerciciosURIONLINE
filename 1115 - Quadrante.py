# -*- coding: utf-8 -*-
ListaP=[]
while True:
    try:
        Ent=input()
        ListaEnt=list(map(float,Ent.split(" ")))
        X=ListaEnt[0]
        Y=ListaEnt[1]
        if X==0 or Y==0:
            break
        if X>0 and Y<0:
            ListaP.append("quarto")
            
        if X>0 and Y>0:
            ListaP.append("primeiro")
            
        if X<0 and Y>0:
            ListaP.append("segundo")
            
        if X<0 and Y<0:
            ListaP.append("terceiro")
    except:
        continue


for i in ListaP:
    print(i)