while(True):
    a=int(input("Donnez le premier nombre"))
    if(a>0):
        break;
while(True):
    b=int(input("Donner le deuxième nombre"))
    if(b>0):
        break;
    
s=0
for i in range(b):
    s = s + a
print(f"le resultat est {s}")
