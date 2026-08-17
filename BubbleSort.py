numeros = [5, 3, 8, 2, 77]


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


print(bubble_sort(numeros))
# BUSCA PELO MENOR NUMERO E DEIXA ELE EM PRIMEIRO