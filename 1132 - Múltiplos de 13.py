# -*- coding: utf-8 -*-
X=int(input())
Y=int(input())
Lista=[]

if X>Y:
    valor=X
    menor=Y
else:
    valor=Y
    menor=X
for i in range(menor,valor+1):
    if (i%13)!=0:
        Lista.append(i)

print(sum(Lista))