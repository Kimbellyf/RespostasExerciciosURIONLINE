# -*- coding: utf-8 -*-
A=1
Sd=[]
while A==1:
    B=input().split(" ")
    BLi=list(map(int,B))
    st=""
    Maior=max(BLi)
    Menor=min(BLi)
    if Maior<=0 or Menor<=0:
        A=2
        break

    ListaNum=[]
    for i in range(Menor,Maior+1,1):
        ListaNum.append(i)
        if i==Maior:
            R="Sum="+str(sum(ListaNum))
            st+=str(i)+" "+R
        else:
            st+=str(i)+" "
            
    Sd.append(st)
                
        
for i in Sd:
    print(i)
    
