num=int(input())
ListaTodos=[]

for i in range(num):
    ListaTodos.append(i+1)

ListaCom=list(map(int,input().split(" ")))

Resp=""
for d in ListaTodos:
    if (d in ListaCom)==False:
        Resp+=str(d)
        break
print(Resp)
        
