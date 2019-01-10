# -*- coding: utf-8 -*-

N=int(input())

Lista=[]
cont=0
st=""
ListaResul=[]
for i in range(N):
    if cont==0:
        A=0
        cont+=1
        Lista.append(A)
        st+=str(A)
        if cont!=N:
            st+=" "
    elif cont==1:
        A=1
        cont+=1
        Lista.append(A)
        st+=str(A)
        if cont!=N:
            st+=" "
    elif cont==2:
        A=1
        cont+=1
        Lista.append(A)
        st+=str(A)
        if cont!=N:
            st+=" "
    else:
        A=Lista[cont-1]+Lista[cont-2]
        cont+=1
        Lista.append(A)
        st+=str(A)
        if cont!=N:
            st+=" "
    ListaResul.append(st)

print(ListaResul[-1])
    
            
            
        
        
    
    
