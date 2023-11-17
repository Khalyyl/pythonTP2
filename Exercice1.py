a=int(input("donner un nombre :"))
x=int(input("donner la 1ère borne de l'intervalle :"))
y=int(input("donner la 2ère borne de l'intervalle :"))

if (x<=a<=y):
    print ( "le nombre" ,a, "appartient à l'intervalle")
elif(y<=a<=x):
    print ( "le nombre" ,a, "appartient à l'intervalle")
else:
    print ( "le nombre" ,a, "n'appartient pas à l'intervalle")
