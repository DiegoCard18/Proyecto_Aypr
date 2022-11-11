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
    texto = texto.replace("\n"," ")
    texto = texto.replace("  "," ")
    texto = texto.replace(".","")
    texto = texto.replace("(","")
    texto = texto.replace(")","")
    texto = texto.replace(";","")
    texto = texto.replace("?","")
    texto = texto.replace("¿","")
    texto = texto.replace("¡","")
    texto = texto.replace("!","")
    texto = texto.replace(";","")
    return texto

def cantpalle(texto):
    """
    Cuenta la cantidad de palabras
    (str)->(str)
    """
    min = []
    rest = quitar_simbolos(texto)
    rest = rest.split(" ")
    for i in rest:
        i = str(i)
        i = i.lower()
        min.append(i)
    """
    tu = repe(min)
    return tu
    """
    return min

def repe(min):
    anole = []
    for i in min:
        if i not in anole:
            anole.append(i)
    """
    ju = frecuencia(min,anole)
    return ju
    """
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
    for i in matriz:
        print(*i)

def main():
    archivo = open("texto1.txt", encoding="utf-8")
    #archivo = open("texto1.txt")
    texto = str(archivo.read())
    fre = frecuencia(cantpalle(texto), repe(cantpalle(texto)),texto.lower())
    print(fre)

main()