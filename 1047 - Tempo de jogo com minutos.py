# -*- coding: utf-8 -*-
Ent=input()
ListaEnt=list(map(int,Ent.split(" ")))
HoraInicial=ListaEnt[0]
MinuIni=ListaEnt[1]
HoraFinal,MinuFinal=ListaEnt[2],ListaEnt[3]

if HoraInicial>=HoraFinal:
    QtdTotal=((24-HoraInicial)+HoraFinal)*60+(MinuFinal-MinuIni)
    QtdHoras=int(QtdTotal/60)
    QtdMinu=QtdTotal%60
else:
    QtdHoras=HoraFinal-HoraInicial
    QtdMinu=MinuFinal-MinuIni
    if QtdMinu<0:
        QtdHoras=QtdHoras-1
        QtdMinu=60+QtdMinu
        

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(QtdHoras,QtdMinu))
