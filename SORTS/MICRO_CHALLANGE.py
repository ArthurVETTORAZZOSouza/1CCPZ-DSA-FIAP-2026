

numeros = [
    886, 348, 937, 639, 139, 988, 237, 583, 698, 593, 312, 556, 988, 983, 848, 747, 389, 606, 237, 73,
    370, 953, 803, 223, 685, 889, 329, 760, 223, 731, 239, 50, 756, 131, 779, 701, 262, 542, 481, 883,
    879, 582, 426, 363, 349, 402, 116, 614, 426, 364, 654, 552, 344, 106, 466, 31, 145, 409, 774, 772,
    255, 970, 939, 719, 837, 324, 42, 313, 688, 952, 114, 540, 968, 602, 827, 797, 889, 506, 810, 51,
    756, 931, 385, 409, 831, 895, 789, 725, 391, 670, 269, 864, 148, 275, 63, 66, 707, 61, 608, 769,
    867, 449, 921, 128, 349, 621, 425, 1, 574, 159, 892, 980, 617, 472, 44, 356, 320, 697, 119, 156,
    765, 678, 211, 9, 671, 545, 681, 599, 860, 604, 232, 30, 423, 299, 872, 355, 567, 275, 79, 782,
    988, 278, 838, 91, 354, 12, 336, 297, 138, 266, 843, 873, 5, 457, 682, 870, 400, 827, 183, 884,
    308, 478, 713, 654, 821, 188, 596, 146, 754, 860, 721, 590, 50, 826, 10, 70, 12, 93, 515, 870,
    483, 287, 14, 147, 197, 949, 973, 884, 889, 361, 228, 710, 170, 353, 149, 578, 50, 947, 81, 205
]




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
