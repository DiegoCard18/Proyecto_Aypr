#Realizado por Diego Cardenas y Samuel Albarracin
from sys import stdin
def quitar_simbolos(texto):
    """
    Recibe un texto y quita todos los simbolos de este mismo
    (str)->(str)
    """
    carracteres = ",:.();?¿!¡"
    for x in range(len(carracteres)):
        texto = texto.replace(carracteres[x],"")
    texto = texto.replace("  ", " ")
    return texto

def quitar_saltos_linea(texto):
    """
    Recibe un texto y quita todos los saltos de linea
    (str)->(str)
    """
    texto = texto.replace("\n"," ")
    texto = texto.replace("   "," ")
    texto = texto.replace("  "," ")
    return texto

def contar_cantidad_palabras(texto):
    """
    Recibe un texto y cuenta la cantidad de palabras que hay
    (str)->(int)
    """
    rest = quitar_saltos_linea(quitar_simbolos(texto)).split(" ")
    return len(rest)

def cantidad_parrafos(texto):
    """
    Recibe un texto y cuenta la cantidad de parrafos que hay
    (str)->(int)
    """
    texto = texto.split(".\n")
    return len(texto)

def cantidad_oraciones(texto):
    """
    Recibe un texto y cuenta la cantidad de oraciones que hay
    (str)->(int)
    """
    texto = texto.split(".")
    return len(texto)-1

def cantidad_carracteres(texto):
    """
    Recibe un texto y cuenta la cantidad de letras que hay
    (str)->(int)
    """
    texto =str(texto)
    texto = quitar_saltos_linea(quitar_simbolos(texto))
    texto = texto.replace(" ","")
    return len(texto)

def verificar_ingresado(h):
    """
    Recibe un valor para verificar si esta bien introducido o o y devuelve un valor boleano
    (str)->(bool)
    """
    if h == "si" or h == "no":
        if h == "si": return True
        else: return False
    else:
        print('Ingrese un valor valido')
        return verificar_ingresado(str(stdin.readline().strip()).lower())

def buscar_palabra(palabra,texto):
    """
    Recibe una palabra y un texto y vrifica si se encuentra y si esta devuelve la cantidad de veces que aparece este mismo
    (str,str)->(str,int)
    """
    if (" " + palabra + " ") in (" " + texto + " "):
        return "Si", buscar_cantidad_palabra(palabra)
    else:
        return "No"

def buscar_cantidad_palabra(palabra):
    """
    Recibe una palabra y cuenta cuantas veces aparece en el texto
    (str)->(int)
    """
    texto = quitar_saltos_linea(quitar_simbolos(abrir_archvio().lower())).split(" ")
    contador = 0
    for i in texto:
        if i == palabra:
            contador+=1
    return contador

def tipo_frecuencia(fu,texto):
    """
    Recibe una palabra y un texto y manda al tipo de frecuencia que desea el usuario y lo devuelve de la manera en que lo solicito
    (str,str)->(list)
    """
    if fu == "apa" or fu == "org" or fu == "may":
        if fu == "apa": return orden_aparicion(texto)
        elif fu == "org": return orden_palabras_mayor_menor(texto)
        else: return orden_mayor_menor(texto)
        
def frecuencia(texto):
    """
    Recibe un texto y realiza una fercuencia quitando duplucados y transformandolo en listas y lo retorna de manera lista
    (str)->(list)
    """
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
    """
    Recibe un texto y devulve una lista en la frecuancia de orden de aparición 
    (str)->(list)
    """
    frecu = frecuencia(texto)
    rest = map(buscar_cantidad_palabra,frecu)
    return zip(frecu,rest)

def orden_mayor_menor(texto):
    """
    algoritmo de ordenamiento que recibe un texto y ordena una lista por orden de mayor a menor de la cantidad de palabras que hay
    (str)->(int)
    """
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

def orden_palabras_mayor_menor(texto):
    """
    Recibe un texto y adjunta la cantidad de veces que aparece una palabra en el texto de la frecuencia
    (str)->(list)
    """
    frecu = merge_sort(frecuencia(texto))
    rest = map(buscar_cantidad_palabra,frecu)
    return zip(frecu,rest)

def merge_sort(lista):
    """
    Algoritmo de ordenamiento que divide en mitades hasta retoenar cuando oslo quede una y de manera ordenada
    (list)->(list)
    """
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

def merge(lista1, lista2):
    """
    Algoritmo que recibe dos lista ordenadas y ordena de menor a mayor
    (list,list)->(list)
    """
    i, j = 0, 0
    result = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    result += lista1[i:]
    result += lista2[j:]
    return result

def cantidad_prepociones(texto):
    """
    Recibe un texto y cuenta la cantidad de proposiciones que hay en este
    (str)->(int)
    """
    prepocicioens = ['a','ante','bajo', 'cabe','con','contra','de','desde','durante',\
        'en','entre','hacia','hasta','mediante','para','por','según','sin','so','sobre','tras','versus','vía']
    texto = quitar_saltos_linea(quitar_simbolos(texto)).split(" ")
    contador = 0
    for i in texto:
        for k in prepocicioens:
            if i == k:
                contador+=1
    return contador

def abrir_archvio():
    """
    Abre el archivo de texto
    """ 
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
                    print(*i)
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
            
    print('Desea imprimir las palabras que mas se repiten (Si/No)')
    if verificar_ingresado(str(stdin.readline().strip()).lower()) == True:
        print('Digite la cantidad de palabras que quiere saber que se repiten')
        cant = stdin.readline().strip()
        frecue = []
        rest = list(tipo_frecuencia("may",texto.lower()))
        for i in range(int(cant)):
            frecue.append(rest[i])
        print('Las {} palabras mas repetidas son:'.format(str(cant)))
        top = 1
        print("# Palabra  Cantidad")
        for i in frecue:
            print("Top "+str(top)+":",*i)
            top+=1

    print('Desea saber cuantas prepociciones hay (Si/No)')
    if verificar_ingresado(str(stdin.readline().strip()).lower()) == True:
        print('En el texto existen {} prepociciones '.format(cantidad_prepociones(texto.lower())))

    print('Fin del programa')
main()