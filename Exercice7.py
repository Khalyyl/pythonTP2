
while(True):
    a=int(input("le premier nombre"))
    if(a>0):
        break;
while(True):
    b=int(input("le deuxieme nombre"))
    if(b>0):
        break;
a1=a
b1=b

while(a!=b):
    if(a>b):
        a=a-b
    else:
        b-=a;
print("le pgcd est%d"%(a))
