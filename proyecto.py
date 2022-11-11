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
    return (len(letras))

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

def printlist(texto,fu):
    if fu == "apa":
        print("Forma organizada en orden de aparición")
        return frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
    elif fu == "org":
        print("Forma organizada alfabeticamente")
        fre = frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
        return sorted(fre , key=lambda x: x[0])
    elif fu == "may":
        print("Forma mayor a menor")
        fre = frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
        return sorted(fre , key=lambda x: -x[1])



def main():
    archivo = open("texto1.txt", encoding="utf-8")
    texto = archivo.read()
    print("La cantidad de palabras es:",cantpal(texto))
    print("La cantidad de letras es:",cantetras(texto))
    print("La cantidad de caracteres es:",contcara(texto))
    print('Desea imprimir la lista de Frecuencia de las palabras (Si/No)')
    m,j = 0,0
    while j == 0:
        h = str(stdin.readline().strip()).lower()
        if h == "si" or h == "no":
            j = 1
        else:
            print('Digite una opcion valida')
    """
    Funcion imprimir lista de cantidad de palabras
    """
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
            print('Digite una opcion valida')
    if hu == "si":
        print('Digite la cantidad de palabras que mas se repiten')
        palco = int(stdin.readline().strip())
        fre = frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
        gtu = sorted(fre , key=lambda x: -x[1])

        
        



    
    """
    Fin imprimir palabra repiten
    """
    print('Programa Finalizado con extito')
main()