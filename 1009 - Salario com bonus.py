# -*- coding: utf-8 -*-
nomeFunc=input()
salariofixo=float(input())
totalvendas=float(input())
totalvendascomissao=(totalvendas/100)*15

totalcomcomissao=salariofixo+totalvendascomissao
print("TOTAL = R$ %.2f"%totalcomcomissao)