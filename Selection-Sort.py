numeros = [5, 3, 8, 2]



# SELECTION_SORT
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range( i + 1,n):
           if lista[j] < lista[menor]:
              menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

print()
print("Selection sort:")
print(selection_sort(numeros))
# DEFINE UM MENOR A CADA PASSAGEM E A POSIÇÃO DELE, para servir de referencia para as proximas passagens