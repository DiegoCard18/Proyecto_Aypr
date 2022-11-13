# -*- coding: utf-8 -*-
from sys import stdin
def quitar_simbolos(texto):
    """
    Quita los simbolos del texto
    (str)->(str)
    """
    texto = str(texto)
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
    rest = quitar_simbolos(texto)
    rest = rest.replace("\n"," ")
    rest = rest.replace("  "," ")
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
    return letras
    #return sorted(repe(letras))

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
    texto = texto.replace("\n","")
    texto = texto.replace("  ","")
    texto = texto.replace(" ","")
    for i in texto:
        caract.append(i)
    return(len(caract))

def cantpalle(texto):
    """
    Cuenta la cantidad de palabras
    (str)->(str)
    """
    min = []
    rest = str(quitar_simbolos(texto))
    rest = rest.replace("\n"," ")
    rest = rest.replace("  "," ")
    rest = rest.split(" ")
    for i in rest:
        i = str(i)
        i = i.lower()
        min.append(i)
    return min

def repe(min):
    anole = []
    for i in min:
        if i not in anole:
            anole.append(i)
    return anole

def contar(texto, palabra):
    cade = []
    lista = cantpalle(texto)
    for i in lista:
        cade.append(lista.count(i))
    print(cade)

def frecuencia(min,anole,texto):
    matriz = [[0 for i in range(int(2))]for j in range(len(anole))]
    for i in range(len(anole)):
        for j in range(0,2):
            if j == 0:
                matriz[i][j] = anole[i]
            else:
                matriz[i][j] = str(texto).count(anole[i])
    return matriz

def ordemy(lista):
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
    resp = []
    if (" " + palba + " ") in (" " + texto + " "):
        resp.append("Si")
        cont = str(texto).count(palba)
        resp.append(cont)
    else:
        resp.append("No")
    return resp

def main():
    archivo = open("texto1.txt", encoding="utf-8")
    texto = str(archivo.read())
    print("La cantidad de palabras es: {}".format(cantpal(texto)))
    print('La cantidad de parrafos es: {}'.format(parrafos(texto)))
    print('la cantidad de oraciones es: {}'.format(oraciones(texto)))
    #print('Cantidad de caracteres del texto: {}'.format(cantetras(texto.lower())))
    #print(cantetras(texto.lower()))
    
    """
    Funcion imprimir lista de cantidad de palabras
    """
    print('Desea imprimir la lista de Frecuencia de las palabras (Si/No)')
    m,j = 0,0
    while j == 0:
        h = str(stdin.readline().strip()).lower()
        if h == "si" or h == "no":
            j = 1
        else:
            print('Digite una opcion valida')
    if h == "si":
        print('Como desea imprimir la matriz, escriba:')
        print('"apa" para escribirlo en orden de aparición')
        print('"org" para escribirlo alfabeticamente')
        print('"may" para escribirlo de mayor a menor')
        while m == 0:
            fu = str(stdin.readline().strip())
            if fu == "apa" or fu == "org" or fu == "may":
                for i in printlist(texto,fu):
                    print(*i)
                m = 1
            else:
                print('Digite una opcion valida')
    """
    Fin imprimir lista
    """ 



    """
    Funcion imprimir caracteres Alfabeticos
    """


    """
    Fin imprimir caracteres Alfabeticos
    """






    """     
    Funcion saber si una palabra dada se encuentra en el texto
    """


    print('Estiba una palabra para saber si se encuentra en el texto')
    palba = str(stdin.readline().strip())
    piuy = saberpa(mejtexto(quitar_simbolos(texto.lower())),str(palba))
    if piuy[0] == "Si":
        print('La palabra {} si se encunetra en el texto y aparece {} veces.'.format(palba,str(piuy[1])))
    else:
        print('La palabra {} no se encuentra en el texto'.format(palba))


    
    """
    Fin imprimir palabra
    """





    """
    Funcion palabras que mas se repiten
    """
    print('Desea saber las palabras que mas re repiten (Si/No)')
    pal,pol = 0,0
    while pal == 0:
        hu = str(stdin.readline().strip()).lower()
        if hu == "si" or hu == "no":
            pal = 1
        else:
            print('Digite una opción valida')
    if hu == "si":
        print('Digite la cantidad de palabras que mas se repiten')
        palco = int(stdin.readline().strip())
        gtu = printlist(texto,str("may"))
        listas_top = []
        for i in range(palco):
            listas_top.append(gtu[i])
        print('El top de las {} palabras mas repetidas son:'.format(str(palco)))
        punt = 1
        for i in listas_top:
            print("top",str(punt)+":",*i)
            punt+=1
    """
    Fin imprimir palabra repiten
    """


    print('Programa Finalizado con extito')
main()