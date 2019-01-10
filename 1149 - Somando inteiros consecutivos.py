# -*- coding: utf-8 -*-
def MaioresQueZero(X):
    return X>0

Ent=input().split(" ")
ListaEnt=list(map(int,Ent))
Ma=list(filter(MaioresQueZero,ListaEnt))

A=ListaEnt[0]
if A>0:
    N=Ma[1]
    ANeg=A
else:
    N=Ma[0]
    ANeg=-A
    
ListaQueQuerem=[]
for i in range(A,ANeg+N,1):
    ListaQueQuerem.append(i)

Soma=sum(ListaQueQuerem)
print(Soma)
