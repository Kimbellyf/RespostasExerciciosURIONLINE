# -*- coding: utf-8 -*-
A=0
ListaResul=[]
while A==0:
    J=int(input())
    if J==0:
        A=1
        break
    ListaPar=[]

    for i in range(J,J+5*2):
        if i%2==0:
            ListaPar.append(i)
    Soma=sum(ListaPar)
    ListaResul.append(Soma)

for i in ListaResul:
    print(i)
