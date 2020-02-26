alice = [15 ,1,13]
bob = [14,2,30]

def checkresult(a,b):
    alen= len(a)
 #   blen= len(b)
    c= [0,0]
    x=0
    y=0
    for i in range(alen):
        if a[i] > b[i]:
            x+=1
            c[0]=x
        
        elif a[i] < b[i]:
            y+=1
            c[1]=y
            
        else:
            c[0]=x
            c[1]=y
            
    return c

result= checkresult(alice,bob)
print(result)
