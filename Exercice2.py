a=int(input('Donner a :'))
b=int(input('Donner b :'))

if (( a > 0 and b > 0 ) or ( a < 0 and b < 0)) :
    print(f'Le produit de {a} et {b} est positif')
elif (( a == 0) or (b == 0)):
    print(f'Le produit de {a} et {b} est null')
else:
    print(f'Le produit de {a} et {b} est negatif')

