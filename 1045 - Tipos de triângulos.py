# -*- coding: utf-8 -*-
Ent=input()
ListaEnt=list(map(float,Ent.split(" ")))

A=max(ListaEnt)
ListaEnt.remove(A)
B=max(ListaEnt)
ListaEnt.remove(B)
C=max(ListaEnt)
ListaEnt.remove(C)

Resul=1
if A>=B+C:
    print("NAO FORMA TRIANGULO")
    Resul=0
if Resul!=0:
    if A**2==B**2 +C**2:
        print("TRIANGULO RETANGULO")
    if  A**2>B**2 +C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2<B**2 +C**2:
        print("TRIANGULO ACUTANGULO")
    if A==B and B==C:
        print("TRIANGULO EQUILATERO")
    elif A==B or A==C or B==C:
        print("TRIANGULO ISOSCELES")