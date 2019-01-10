# -*- coding: utf-8 -*-

Ent=float(input())
if Ent>=0.00 and Ent<=(int(25.00)):
    print("Intervalo [0,25]")
    
elif Ent>25.00 and Ent<=int(50):
    print("Intervalo (25,50]")
    
elif Ent>50.00 and Ent<=int(75):
    print("Intervalo (50,75]")
    
elif Ent>75.00 and Ent<=int(100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
