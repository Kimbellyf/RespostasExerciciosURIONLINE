# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

Num=float(input())

Resto=0

Nota100=int(Num/100)
Sobroude100=(Num%100)
Nota50=int(Sobroude100/50)
Sobroude50=(Sobroude100%50)
Nota20=int(Sobroude50/20)
Sobroude20=(Sobroude50%20)
Nota10=int(Sobroude20/10)
Sobroude10=Sobroude20%10
Nota5=int(Sobroude10/5)
Sobroude5=Sobroude10%5
Nota2=int(Sobroude5/2)
Sobroude2=Sobroude5%2
Nota1=int(Sobroude2)
Sobroude1=Sobroude2-Nota1


MulSobrou1=Sobroude1*100
MenosMoeda50=MulSobrou1%50


Moeda50=int(Sobroude1/0.5)
SobroudeMoeda50=Sobroude1%0.5


Moeda25=int(MenosMoeda50/25)
SobroudeMoeda25Mult=(MenosMoeda50%25)
SobroudeMoeda25=SobroudeMoeda25Mult/100


Moeda10=int(SobroudeMoeda25Mult/10)
SobroudeMoeda10=SobroudeMoeda25Mult%10
    
Moeda005=int(SobroudeMoeda10/5)
SobroudeMoeda005=SobroudeMoeda10%5

Moeda001=int(SobroudeMoeda005/1)
SobroudeMoeda001=SobroudeMoeda005%1
                   

print("""NOTAS:
%d nota(s) de R$ 100.00
%d nota(s) de R$ 50.00
%d nota(s) de R$ 20.00
%d nota(s) de R$ 10.00
%d nota(s) de R$ 5.00
%d nota(s) de R$ 2.00
MOEDAS:
%d moeda(s) de R$ 1.00
%d moeda(s) de R$ 0.50
%d moeda(s) de R$ 0.25
%d moeda(s) de R$ 0.10
%d moeda(s) de R$ 0.05
%d moeda(s) de R$ 0.01"""%(Nota100,Nota50,Nota20,Nota10,Nota5,Nota2,Nota1,Moeda50,Moeda25,Moeda10,Moeda005,Moeda001))
