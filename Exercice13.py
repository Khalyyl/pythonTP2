while(True):
    max=int(input('Donner un Max'))
    if(max>0):
        break;
s=0
p=1
somme_inverse=0
for i in range(1,max+1):
    s=s+i
    p=p*i
    if((i%5)== 0):
        continue;
    somme_inverse=somme_inverse+(1/i)
print(f'La somme est {s}\n  le produit est {p}  \n la somme des inverse est {somme_inverse}')
    
