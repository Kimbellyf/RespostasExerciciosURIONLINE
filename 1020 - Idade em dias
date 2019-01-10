# -*- coding: utf-8 -*-
diasdaID=int(input())
diasquesobrou=0
diasMenosQueAnos=0
ano=0
mes=0
if diasdaID>=365:
    if diasdaID%365==0:
        divANO=int(diasdaID/365)
        ano+=divANO
    else:
        divANO=int(diasdaID/365)
        ano+=divANO
        diasMenosQueAnos=diasdaID%365
        if diasMenosQueAnos>=30:
            if diasMenosQueAnos%30==0:
                divMES=int(diasMenosQueAnos/30)
                mes +=divMES
            else:
                divMES=int(diasMenosQueAnos/30)
                mes +=divMES
                MenoresqueMes=diasMenosQueAnos%30
                diasquesobrou+=MenoresqueMes

else:
    if diasdaID>=30:
        if diasdaID%30==0:
            divMES=int(diasdaID/30)
            mes +=divMES
        else:
            divMES=int(diasdaID/30)
            mes +=divMES
            MenoresqueMes=diasdaID%30
            diasquesobrou+=MenoresqueMes
    else:
        diasquesobrou+=diasdaID
        
   
    
print("""%d ano(s)
%d mes(es)
%d dia(s)""" %(ano,mes,diasquesobrou))