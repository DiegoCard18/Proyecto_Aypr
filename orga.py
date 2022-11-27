#Realizada por Diego Cardenas
from sys import stdin
def merge_sort(lista):
   if len(lista) < 2:
      return lista
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

def merge(lista1, lista2):
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
def main():
    listaoriginal = ['ha','mucho','tiempo','que','vivía','hidalgo','los','lanza','astillero','adarga','antigua','rocín','flaco']
    print(merge_sort(listaoriginal))
main()