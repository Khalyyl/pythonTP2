while(True):
    a=int(input("donner le premier nombre"))
    if(a>=0):
        break;
while(True):
    b=int(input("donner le deuxieme nombre"))
    if(b>=0):
        break;
while(True):
    c=int(input("donner le troisieme nombre"))
    if(c>=0):
        break;
if(a>c):
    aux=a
    a=c
    aux=a
if(b>c):
    aux=b
    b=c
    aux=b
if(a==b==c):
    print("le triangle est équilatérale")
elif(a**2+b**2==c and a==b):
    print("le triangle est isocèle et rectangle")
elif(a**2+b**2==c):
    print("le triangle est rectangle")
elif(a+b>c):
    print("les longueurs correspondent à un triangle")
else:
    print("n est pas un triangle")
