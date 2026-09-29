"""QUESTÃO 1"""

"""
Q1.A_B
n = 22
def reduzir(n):
    print(n)
    if n <= 1:
        return
    reduzir(n // 2)
"""
"""
Q1.C
n = 22
def reduzir2(n):
    print(n)
    if n <= 1:
        return
    reduzir2(n // 2)
    reduzir2(n // 2)
    
reduzir2(n)
"""

"""QUESTÃO 2"""
"""
v = [13, 7, 11, 3, 12, 6, 10, 8]
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return esquerda + direita
print(merge_sort(v))
"""

"""QUESTÃO 3"""
""""
def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1


    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado



def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

v = [13, 7, 11, 3]
print(merge_sort(v))
"""

"""QUESTÃO 4"""
"""

esquerda = [4, 10]
direita = [6, 9]

def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

print(merge(esquerda, direita))
"""

"""QUESTÃO 5"""
"""
esquerda = [10, 4]
direita = [6, 9]
print(merge(esquerda, direita))
"""

"""QUESTÃO 6"""
"""
V = [13, 7, 11, 3, 12, 6, 10, 8]
def quick_sort(lista):
 if len(lista) <= 1:
 return lista
 pivo = lista[-1]
 menores = []
 iguais = []
 maiores = []
 for elemento in lista:
 if elemento < pivo:
 menores.append(elemento)
 elif elemento == pivo:
 iguais.append(elemento)
 else:
 maiores.append(elemento)
 resultado_ordenado = quick_sort(menores) + iguais + quick_sort(maiores)
 return resultado_ordenado
quick_sort(V)
"""