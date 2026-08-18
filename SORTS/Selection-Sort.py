

numeros = [72, 49, 26, 13, 81, 64, 74, 31, 23, 20, 34, 59, 33, 83, 92, 46, 72, 22, 40, 38]



# SELECTION_SORT
def selection_sort(lista):
    trocas = 0
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range( i + 1,n):
           if lista[j] < lista[menor]:
              menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
        trocas+=1
    return lista, trocas

print()
lista, trocas = selection_sort(numeros)
print("Selection Sort: ", lista)
print("Trocas: ", trocas)
# DEFINE UM MENOR A CADA PASSAGEM E A POSIÇÃO DELE, para servir de referencia para as proximas passagens