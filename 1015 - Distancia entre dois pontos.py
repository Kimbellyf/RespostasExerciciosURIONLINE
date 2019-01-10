# -*- coding: utf-8 -*-

import math

entX1Y1=input()
entX2Y2=input()
X1Y1lista=list(map(float,entX1Y1.split(" ")))
x1=X1Y1lista[0]
y1=X1Y1lista[1]

X2Y2lista=list(map(float,entX2Y2.split(" ")))
x2=X2Y2lista[0]
y2=X2Y2lista[1]

Valjun=(x2-x1)**2 + (y2-y1)**2
Distancia=math.sqrt(Valjun)
print("%.4f"%Distancia)
