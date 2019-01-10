# -*- coding: utf-8 -*-

def Fatorial(Numero):
    f=1
    while Numero>1:
        f*=Numero
        Numero-=1
    return f


ListaResul=[]
while True:
    try:
        ia=input().split(" ")
        ListaXY=list(map(int,ia))
        X,Y=ListaXY[0],ListaXY[1]
        FatX=Fatorial(X)
        FatY=Fatorial(Y)
        SomaFat=FatX+FatY
        ListaResul.append(SomaFat)
    
    except:
        break
for i in ListaResul:
    print(i)
     
