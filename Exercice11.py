while(True):
    a=int(input("donner un nombre"))
    if(a>0):
        break;
s=0;
for i in range(2,a):
    if(a%i==0):
        s=1
if(s==1):
    print("ce n'est est pas un nombre premier")
else:
    print("c'est un nombre premier")
