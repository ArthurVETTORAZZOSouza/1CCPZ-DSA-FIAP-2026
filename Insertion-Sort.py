
numeros = [5, 3, 8, 2]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = atual
    return lista
print()
print("Insertion sort")

print(insertion_sort(numeros))
#