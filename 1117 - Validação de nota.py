cont=0
Total=0
while True:
    try:
        if cont==2:
            print("media = %.2f"%(Total/2))
            break
        
        ent=float(input())
        if ent>0 and ent<=10:
            cont+=1
            Total+=ent
            
        else:
            print("nota invalida")

    except:
        break
        
        
        
