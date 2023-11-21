import math

sexe = str(input('Donner le sexe (M/F)'))
taille = float(input('Entrer la taille en cm'))
poids = float(input('donner le poids en Kg'))

IMC = ( poids/(taille*taille))

if ( sexe == 'M' or sexe =='m' ):
    if ( IMC >= 25 ):
        print('« vous devriez surveiller votre alimentation »')
    elif (IMC < 19 ):
        print('« Vous devriez prendre des forces »')
    else :
        print ('« Vous êtes à votre poids de forme »')
elif ( sexe == 'F' or sexe =='f' ):
    if ( IMC >= 23):
        print('« vous devriez surveiller votre alimentation »')
    elif (IMC < 18 ):
        print('« Vous devriez prendre des forces »')
    else :
        print ('« Vous êtes à votre poids de forme »')
else:
    print('Verifier le sexe (M/F)')

