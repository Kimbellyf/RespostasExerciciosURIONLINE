# -*- coding: utf-8 -*-

salario=float(input())

if salario<=(float(400.00)):
    aumento=salario*0.15
    percentual=15
if salario>(float(400.00)) and salario<=800:
    aumento=(salario/100)*12
    percentual=12
if salario>(float(800.00)) and salario<=1200:
    aumento=(salario/100)*10
    percentual=10
if salario>(float(1200.00)) and salario<=2000.00:
    aumento=(salario/100)*7
    percentual=7
if salario>2000:
    aumento=(salario/100)*4
    percentual=4
SalarioFinal=aumento+salario
print("""Novo salario: %.2f
Reajuste ganho: %.2f
Em percentual: %d %%""" %(SalarioFinal,aumento,percentual))
