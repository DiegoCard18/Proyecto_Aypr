#Realizado por Diego Cardenas y Samuel Albarracin
from sys import stdin
import matplotlib.pyplot as plt
def quitar_simbolos(texto):
    """
    Quita los simbolos del texto
    (str)->(str)
    """
    texto = str(texto)

    #texto = texto.strip(",:.)(;?¿!¡")

    texto = texto.replace(",","")
    texto = texto.replace(":","")
    texto = texto.replace(".","")
    texto = texto.replace("(","")
    texto = texto.replace(")","")
    texto = texto.replace(";","")
    texto = texto.replace("?","")
    texto = texto.replace("¿","")
    texto = texto.replace("¡","")
    texto = texto.replace("!","")

    return texto

def mejtexto(texto):
    """
    Mejorar el texto quitando saltos de linea y espacios inecesarios
    (str)->(str)
    """
    texto = str(texto)
    texto = texto.replace("\n"," ")
    texto = texto.replace("   "," ")
    texto = texto.replace("  "," ")
    return texto

def cantpal(texto):
    """
    Cuenta la cantidad de palabras
    (str)->(str)
    """
    rest = mejtexto(quitar_simbolos(texto))
    rest = rest.split(" ")
    return (len(rest))

def cantetras(texto):
    """
    Cuenta la cantidad de letras
    (str)->(str)
    """
    letras = []
    texto = quitar_simbolos(texto)
    texto = texto.replace("\n","")
    texto = texto.replace(" ","")
    for i in texto:
        letras.append(i)
    return len(letras)

def oraciones(texto):
    """
    Cuenta la cantidad de oraciones en el texto
    (str)->(int)
    """
    con = texto.split(".")
    return len(con)-1

def parrafos(texto):
    """
    Cuenta la cantidad de parrafos en el texto
    (str)->(int)
    """
    con = texto.split(".\n")
    return len(con)

def contcara(texto):
    """
    Cuenta la cantidad de caracteres
    (str)->(str)
    """
    caract = []
    texto = str(texto)
    texto = mejtexto(quitar_simbolos(texto))
    """
    texto = texto.replace("\n","")
    texto = texto.replace("  ","")
    texto = texto.replace(" ","")
    """
    for i in texto:
        caract.append(i)
    return(len(caract))

def cantpalle(texto):
    """
    Cuenta la cantidad de palabras
    (str)->(str)
    """
    min = []
    rest = str(mejtexto(quitar_simbolos(texto))).split(" ")
    for i in rest:
        i = str(i).lower()
        min.append(i)
    return min

def repe(min):
    """
    Elimina las palabras repetidas del texto
    (list)->(list)
    """
    anole = []
    for i in min:
        if i not in anole:
            anole.append(i)
    return anole

def frecuencia(min,anole,texto):
    """
    Crea una matriz con la secuencia de aparicion de las palabras y la frecuencia con la que aparecen
    (str,list,str)->(list)
    """
    matriz = [[0 for i in range(int(2))]for j in range(len(anole))]
    for i in range(len(anole)):
        for j in range(0,2):
            if j == 0:
                matriz[i][j] = anole[i]
            else:
                matriz[i][j] = str(" "+ mejtexto(quitar_simbolos(texto)) +" ").count(" "+anole[i]+" ")
    return matriz

def ordemy(lista):
    """
    Entrega una lista y la ordena de mayor a menor
    (list)->(list)
    """
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if lista[j+1][1] > lista[j][1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def printlist(  texto,fu):
    """
    Retorna la matriz dependiendo la manera en que desea organizarla
    (str,str)->(list)
    """
    if fu == "apa":
        print("Forma organizada en orden de aparición")
        return frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
    elif fu == "org":
        print("Forma organizada alfabeticamente")
        fre = frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
        return sorted(fre , key=lambda x: x[0])
    elif fu == "may":
        return ordemy(frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower()))

def saberpa(texto,palba):
    """
    Entrega el texto y una palabra y quiere saber si aparece en el texto y cuantas veces aparece en este mismo
    (str,str)->(list)
    """
    resp = []
    if (" " + palba + " ") in (" " + texto + " "):
        resp.append("Si")
        cont = str(mejtexto(quitar_simbolos(texto))).count(palba)
        resp.append(cont)
    else:
        resp.append("No")
    return resp

def deletemen3(list):
    new = []
    for i in range(0,len(list)):
        if len(list[i][0]) > 1:
            new.append(list[i])
    return new

def main():
    archivo = open("texto1.txt", encoding="utf-8")
    texto = str(archivo.read())
    print('La cantidad de palabras es: {}'.format(cantpal(texto)))
    print('La cantidad de parrafos es: {}'.format(parrafos(texto)))
    print('la cantidad de oraciones es: {}'.format(oraciones(texto)))
    print('Cantidad de caracteres del texto: {}'.format(cantetras(texto.lower())))
    print('Desea imprimir la lista de Frecuencia de las palabras (Si/No)')
    m,j = 0,0
    while j == 0:
        h = str(stdin.readline().strip()).lower()
        if h == "si" or h == "no": j = 1
        else: print('Digite una opción valida')
    if h == "si":
        print('Como desea imprimir la matriz, escriba:')
        print('"apa" para escribirlo en orden de aparición')
        print('"org" para escribirlo alfabéticamente')
        print('"may" para escribirlo de mayor a menor')
        while m == 0:
            fu = str(stdin.readline().strip())
            if fu == "apa" or fu == "org" or fu == "may":
                for i in printlist(texto,fu):
                    print(*i)
                m = 1
            else: print('Digite una opción valida')
    print('Estiba una palabra para saber si se encuentra en el texto')
    palba = str(stdin.readline().strip())
    piuy = saberpa(mejtexto(quitar_simbolos(texto.lower())),str(palba))
    if piuy[0] == "Si": print('La palabra {} si se encuentra en el texto y aparece {} vez.'.format(palba, str(piuy[1])))
    else: print('La palabra {} no se encuentra en el texto'.format(palba))
    print('Desea saber las palabras que más re repiten (Si/No)')
    pal = 0
    while pal == 0:
        hu = str(stdin.readline().strip()).lower()
        if hu == "si" or hu == "no": pal = 1
        else: print('Digite una opción valida')
    if hu == "si":
        print('Digite la cantidad de palabras que mas se repiten')
        palco = int(stdin.readline().strip())
        gtu = printlist(texto,str("may"))
        listas_top = []
        for i in range(palco):
            listas_top.append(gtu[i])
        if palco != 1:
            print('El top de las {} palabras mas repetidas son:'.format(str(palco)))
            punt = 1
            for i in listas_top:
                print("|top",str(punt)+"|:",*i)
                punt+=1
        else: print('La palabra más repetida es {} con {} apariciones en el texto :'.format(listas_top[0][0],listas_top[0][1]))
    """
    grafico
    """
    print('Desea imprimir el grafico digite (Si)/(No)')
    pva,pvo = 0,0
    while pva == 0:
        gt = str(stdin.readline().strip()).lower()
        if gt == "si" or gt == "no": pva = 1
        else: print('Digite una opción valida')
    if gt == "si":
        print('En construcción')
    print('Programa Finalizado con éxito')
main()