#Realizado por Diego Cardenas y Samuel Albarracin
from sys import stdin
def quitar_simbolos(texto):
    carracteres = ",:.();?¿!¡"
    for x in range(len(carracteres)):
        texto = texto.replace(carracteres[x],"")
    texto = texto.replace("  ", " ")
    return texto

def quitar_saltos_linea(texto):
    texto = texto.replace("\n"," ")
    texto = texto.replace("   "," ")
    texto = texto.replace("  "," ")
    return texto

def contar_cantidad_palabras(texto):
    rest = quitar_saltos_linea(quitar_simbolos(texto)).split(" ")
    return len(rest)

def cantidad_parrafos(texto):
    texto = texto.split(".\n")
    return len(texto)

def cantidad_oraciones(texto):
    texto = texto.split(".")
    return len(texto)-1

def cantidad_carracteres(texto):
    texto =str(texto)
    texto = quitar_saltos_linea(quitar_simbolos(texto))
    texto = texto.replace(" ","")
    return len(texto)

def verificar_ingresado(h):
    if h == "si" or h == "no":
        if h == "si": return True
        else: return False
    else:
        print('Ingrese un valor valido')
        return verificar_ingresado(str(stdin.readline().strip()).lower())

def buscar_palabra(palabra,texto):
    if (" " + palabra + " ") in (" " + texto + " "):
        return "Si", buscar_cantidad_palabra(palabra)
    else:
        return "No"

def buscar_cantidad_palabra(palabra):
    texto = quitar_saltos_linea(quitar_simbolos(abrir_archvio().lower())).split(" ")
    contador = 0
    for i in texto:
        if i == palabra:
            contador+=1
    return contador

def tipo_frecuencia(fu,texto):
    if fu == "apa" or fu == "org" or fu == "may":
        if fu == "apa": return orden_aparicion(texto)
        elif fu == "org":
            print("En creacion")
        else: return orden_mayor_menor(texto)
        
def frecuencia(texto):
    normal = []
    repetidas = []
    texto = quitar_saltos_linea(quitar_simbolos(texto)).split(" ")
    for i in texto:
        if i not in normal:
            normal.append(i)
        else:
            repetidas.append(i)
    return normal

def orden_aparicion(texto):
    frecu = frecuencia(texto)
    rest = map(buscar_cantidad_palabra,frecu)
    return zip(frecu,rest)

def orden_mayor_menor(texto):
    frecu = frecuencia(texto)
    rest = map(buscar_cantidad_palabra,frecu)
    rest = (list(rest))
    for i in range(1,len(rest)):
        for j in range(0,len(rest)-i):
            if rest[j+1] > rest[j]:
                aux = rest[j]
                rest[j] = rest[j+1]
                rest[j+1] = aux
                aux2 = frecu[j]
                frecu[j] = frecu[j+1]
                frecu[j+1] = aux2
    return zip(frecu,rest)

def cantidad_prepociones(texto):
    prepocicioens = ['a','ante','bajo', 'cabe','con','contra','de','desde','durante','en','entre','hacia','hasta','mediante','para','por','según','sin','so','sobre','tras','versus','vía']
    texto = quitar_saltos_linea(quitar_simbolos(texto)).split(" ")
    contador = 0
    for i in texto:
        for k in prepocicioens:
            if i == k:
                contador+=1
    return contador

def abrir_archvio():
    archivo = open("texto1.txt", encoding="utf-8")
    return str(archivo.read())

def main():
    texto = abrir_archvio()
    print('La cantidad de palabras es: {}'.format(contar_cantidad_palabras(texto.lower())))
    print('La cantidad de parrafos es: {}'.format(cantidad_parrafos(texto.lower())))
    print('la cantidad de oraciones es: {}'.format(cantidad_oraciones(texto.lower())))
    print('la cantidad de caracteres es: {}'.format(cantidad_carracteres(texto.lower())))
    
    print('Desea imprimir la lista de Frecuencia de las palabras (Si/No)')
    if verificar_ingresado(str(stdin.readline().strip()).lower()) == True:
        m = 0
        print('Como desea imprimir la matriz, escriba:')
        print('"apa" para escribirlo en orden de aparición')
        print('"org" para escribirlo alfabéticamente')
        print('"may" para escribirlo de mayor a menor')
        while m == 0:
            fu = str(stdin.readline().strip()).lower()
            if fu == "apa" or fu == "org" or fu == "may":
                j = tipo_frecuencia(fu, texto.lower())
                for i in j:
                    print(i)
                m = 1
            else: print('Digite una opción valida')

    print('Desea buscar una palabra en el texto y saber cuantas veces aparece (Si/No)')
    if verificar_ingresado(str(stdin.readline().strip()).lower()) == True:
        palabra_a_buscar = input('Digite la palabra a buscar: ')
        (buscar, cantidad_busqueda) = buscar_palabra(palabra_a_buscar.lower(),texto.lower())
        if buscar == "Si":
            print('La palabra {} si se encuentra en el texto y aparece {} vez.'.format(palabra_a_buscar, str(cantidad_busqueda)))
        else:
            print('La palabra {} no se encuentra en el texto'.format(palabra_a_buscar))

    print('Desea saber cuantas prepociciones hay (Si/No)')
    if verificar_ingresado(str(stdin.readline().strip()).lower()) == True:
        print('En el texto existen {} prepociciones '.format(cantidad_prepociones(texto.lower())))
    
    
    print('Fin del programa')

main()