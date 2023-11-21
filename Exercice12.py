while(True):
    a=int(input("Donner un nombre"))
    if(a>0):
        break;

if(a==0):
    print("le resultat est 1")
else:
    s=1
    i=1
    while(i<=a):
        s*=i
        i+=1
    print("le factoriel est %d"%(s))
