numeros = [72, 49, 26, 13, 81, 64, 74, 31, 23, 20, 34, 59, 33, 83, 92, 46, 72, 22, 40, 38]


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
lista, trocas = bubble_sort(numeros)
print("Bubble Sorted: ", lista)
print("Trocas: ", trocas)

# BUSCA PELO MENOR NUMERO E DEIXA ELE EM PRIMEIRO