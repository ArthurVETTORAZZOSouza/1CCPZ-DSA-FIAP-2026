def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
 

numeros = [8, 10, 16, 17, 18, 19, 20, 25, 71, 91, 20000]

posicao = busca_binaria(numeros, 71)

print (posicao)