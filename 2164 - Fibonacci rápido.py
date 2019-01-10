# -*- coding: utf-8 -*-
import math

Ent=int(input())

el1=((1+math.sqrt(5))/2)**Ent-((1-math.sqrt(5))/2)**Ent
Fibonacci=el1/math.sqrt(5)

print("%.1f"%Fibonacci)
