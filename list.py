liso = [1,2,3,4,5,6,7,8,9,10,12,12,13,14]
def Sumarray(ar):
        c=0
        arrlen= len(ar)
        print(ar)
        for i in range(arrlen):
            c= c+ar[i]
            print(ar[i])

        return c
    
def Sumarrayy(*ar):
        s=0
        print(ar)
        for i in ar:
            s += ar
            print(ar)

        return s
        

s=Sumarrayy(liso)

for i in liso:
    print(i)        
        
print(s)    
    