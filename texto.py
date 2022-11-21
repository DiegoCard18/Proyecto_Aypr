def quitar_simbolos(texto):
    texto = str(texto)
    texto = texto.replace("\n"," ")
    texto = texto.replace("  ", " ")
    carracteres = ".,:;()!¡¿?"
    for x in range(len(carracteres)):
        texto = texto.replace(carracteres[x]," ")
    texto = texto.replace("  ", " ")
    return texto 

def main():
    archivo = open("texto1.txt", encoding="utf-8")
    texto = str(archivo.read())
    print(quitar_simbolos(texto.lower()))
main()