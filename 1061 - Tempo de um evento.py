# -*- coding: utf-8 -*-

DiaInicial = input().split()
DiaInicial = int(DiaInicial[1])
horainicio = input().split(":")
Hinicial,minicio,sinicio = int(horainicio[0]),int(horainicio[1]),int(horainicio[2])

Diafinal = input().split()
Diafinal = int(Diafinal[1])
horafinal = input().split(":")
Hfinal,mfinal,sfinal = int(horafinal[0]),int(horafinal[1]),int(horafinal[2])

dia = Diafinal - DiaInicial

hora = Hfinal - Hinicial
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = mfinal - minicio 
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1
	
segundos = sfinal - sinicio
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print("""%d dia(s)
%d hora(s)
%d minuto(s)
%d segundo(s)"""%(dia,hora,minuto,segundos))
