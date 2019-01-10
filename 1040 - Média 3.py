# -*- coding: utf-8 -*-

rec=input()
ListaRecNotas=list(map(float,rec.split(" ")))
N1=ListaRecNotas[0]*2
N2=ListaRecNotas[1]*3
N3=ListaRecNotas[2]*4
N4=ListaRecNotas[3]

Media=(N1+N2+N3+N4)/10
NotaDoExame=0
if Media>=7:
    print("Media: %.1f"%Media)
    print("Aluno aprovado.")
if Media<5:
    print("Media: %.1f"%Media)
    print("Aluno reprovado.")
if Media>=5 and Media<=6.9:
    NotaDadaEx=float(input())
    NotaDoExame+=NotaDadaEx
    NovaMedia=(NotaDoExame+Media)/2
    if NovaMedia>=5:
        print("Media: %.1f"%Media)
        print("Aluno em exame.")
        print("Nota do exame: %.1f"%NotaDoExame)
        print("Aluno aprovado.")
    if NovaMedia<=4.9:
        print("Media: %.1f"%Media)
        print("Aluno em exame.")
        print("Nota do exame: %.1f"%NotaDoExame)
        print("Aluno reprovado.")
    print("Media final: %.1f"%NovaMedia)