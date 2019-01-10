
cont=0
Total=0
while True:
    try:
        if cont==2:
            print("media = %.2f" %(Total/2))
            Total=0
            print("novo calculo (1-sim 2-nao)")
        
        ent=float(input())
        if cont==2:
            a=0
            while True:
                if (int(ent)==2):
                    a=1
                    break
                elif ((int(ent)>2) or (int(ent)<1)):
                    print("novo calculo (1-sim 2-nao)")
                    ent=float(input())
                else:
                    cont=0
                    Total=0
                    ent=float(input())
                    break
            if a==1:
                break

        
        if ent>=0 and ent<=10:
            cont+=1
            Total+=ent

        else:
            print("nota invalida")
            
        
    except:
        break
