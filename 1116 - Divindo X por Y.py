# -*- coding: utf-8 -*-
Ent=int(input())
ListaResp=[]
for i in range(Ent):
    A=input()
    EmLi=list(map(int,A.split(" ")))
    N1=EmLi[0]
    N2=EmLi[1]
    if N2==0:
        ListaResp.append("divisao impossivel")
    else:
        Div=N1/N2
        ListaResp.append(Div)

for i in ListaResp:
    print(i)
        
        
    
