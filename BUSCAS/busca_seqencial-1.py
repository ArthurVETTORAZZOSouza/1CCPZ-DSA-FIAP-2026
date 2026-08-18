def busca_sequncial(lista, procurado):
    for i in range(len(lista)):
        if lista[i] == procurado:
            return i
    return - 1


nome = [ "Arthur", "Luiza", "Heitor", "Isabela", "Renato", "Victor"]

posicao = busca_sequncial(nome, "Arthur")

print (posicao) 