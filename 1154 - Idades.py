# -*- coding: utf-8 -*-
ent=0
ListaNum=[]
while ent==0:
    num=int(input())
    if num<0:
        ent+=1
        break
    else:
        ListaNum.append(num)
    
Soma=sum(ListaNum)
Tam=len(ListaNum)
Media=Soma/Tam
print("%.2f"%Media)
    
        