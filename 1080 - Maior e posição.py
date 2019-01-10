# -*- coding: utf-8 -*-
ListaNum=[]

for i in range(100):
    num=int(input())
    ListaNum.append(num)
ElMaior=max(ListaNum)
Pos=ListaNum.index(ElMaior)
PosMais1=Pos+1
print(ElMaior)
print(PosMais1)
