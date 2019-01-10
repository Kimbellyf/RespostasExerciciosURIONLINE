# -*- coding: utf-8 -*-
st1=input()
st1Lista=list(map(float,st1.split(" ")))
A=st1Lista[0]
B=st1Lista[1]
C=st1Lista[2]

pi= 3.14159
AreaCirculo=pi*(C**2)
AreaTriRet=(A*C)/2
AreaTrapezio=(((A+B)*C)/2)
AreaQuad=B*B
AreaRet=A*B

print("""TRIANGULO: %.3f
CIRCULO: %.3f
TRAPEZIO: %.3f
QUADRADO: %.3f
RETANGULO: %.3f"""%(AreaTriRet,AreaCirculo,AreaTrapezio,AreaQuad,AreaRet))
