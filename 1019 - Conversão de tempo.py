# -*- coding: utf-8 -*-

Num=int(input())
Nota100=0
Nota50=0
Nota20=0
Nota10=0
Nota5=0
Nota2=0
Nota1=0
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

print("""%d
%d nota(s) de R$ 100,00
%d nota(s) de R$ 50,00
%d nota(s) de R$ 20,00
%d nota(s) de R$ 10,00
%d nota(s) de R$ 5,00
%d nota(s) de R$ 2,00
%d nota(s) de R$ 1,00"""%(Num,Nota100,Nota50,Nota20,Nota10,Nota5,Nota2,Nota1))