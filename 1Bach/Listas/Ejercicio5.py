x=1
s=[]
try:
    while x!=0:
        n=int(input("Dime un numero (escribe un 0 para parar): "))
        s.append(n)
        if n==0:
            s2=sum(s)
            print("La media de todos esos numeros es:",s2/len(s))
            break
except:
    print("Solo trabajo con números")