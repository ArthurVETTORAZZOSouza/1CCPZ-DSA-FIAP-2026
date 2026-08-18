

numeros = [72, 49, 26, 13, 81, 64, 74, 31, 23, 20, 34, 59, 33, 83, 92, 46, 72, 22, 40, 38]

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

print()
lista, trocas = insertion_sort(numeros)
print("Insertion Sort: ", lista)
print("Trocas: ", trocas)

