

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



def insertion_sort(lista):
    trocas = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j+1] = lista[j]
            j = j - 1
            trocas = trocas + 1
        lista[j+1] = atual

    return lista, trocas


def bubble_sort(lista):
    trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas +=1
    return lista, trocas

print()
lista, trocas = bubble_sort(numeros.copy())
print("Bubble sort: ", lista)
print("Trocas Realizadas: ", trocas)
print()
lista, trocas = insertion_sort(numeros.copy())
print("Insertion sort: ", lista)
print("Trocas Realizadas: ", trocas)
print()
lista, trocas = selection_sort(numeros.copy())
print("Selection sort: ", lista)
print("Trocas Realizadas: ", trocas)
