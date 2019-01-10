# -*- coding: utf-8 -*-
import math
Ent=input()
ListaEnt=list(map(float,Ent.split(" ")))
A=ListaEnt[0]
B=ListaEnt[1]
C=ListaEnt[2]

ElDentro=((B**2)-4*A*C)
Baixo=2*A
if ElDentro<0 or 2*A==0:
    print("Impossivel calcular")
        
else:
    Raiz=math.sqrt(ElDentro)
    FormBhaskara1=((-B+Raiz)/Baixo)
    FormBhaskara2=((-B-Raiz)/Baixo)
    print("R1 = %.5f"%FormBhaskara1)
    print("R2 = %.5f"%FormBhaskara2)
