while(True):
    moyenne=float(input("Donner la moyenne :"))
    if(0<=moyenne<=20):
        break;


if(moyenne >=16):
       print('Très bien')
elif (14<= moyenne < 16 ):
       print('Bien')
elif (12 <= moyenne < 14 ):
       print('Assez bien')
elif(10 <= moyenne <14 ) :
       print('Passable')
else:
       print('Redoublant')
    