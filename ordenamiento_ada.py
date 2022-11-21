def listaord(valor):
    palabra= []
    for  i in valor:
        palabra.append(ord(i))
    return palabra


lista = ['ha','mucho','tiempo','que','vivía','hidalgo','los','lanza','astillero','adarga','antigua','rocín','flaco']
lista_yaord = map(listaord,lista)
#print(list(lista_yaord))
for i in lista_yaord:
    print(i)