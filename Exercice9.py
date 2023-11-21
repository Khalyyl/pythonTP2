def deviseur(n):
    a = []
    for i in range(1,n):
        if n%i == 0:
            a.append(i)
    return a

b = int(input("donner un nombre"))
s = 0
for i in range(len(deviseur(b))):
    s =  s + deviseur(b)[i]
if s == b:
    print("le nombre est parfait")
else:
    print("le nombre n'est pas parfait")
