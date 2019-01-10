# -*- coding: utf-8 -*-
NumPosit=[]
for i in range(6):
    Num=float(input())
    if Num>0:
        NumPosit.append(Num)
MediaValoresPos=(sum(NumPosit))/len(NumPosit)
print("""%d valores positivos
%.1f"""%(len(NumPosit),MediaValoresPos))