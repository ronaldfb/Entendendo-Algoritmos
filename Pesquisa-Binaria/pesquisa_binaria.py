def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 # 4
    #                        Passo 1                                      Passo 2                                 Passo 3
    while baixo <= alto:   # 0 <= 4 true                         | 0 <= 1 true                          | 1 <= 1 true
        meio = (baixo + alto) // 2  # (0 + 4) // 2 => 4 // 2 = 2 | (0 + 1) // 2 = 0                     | (baixo + alto) // 2 = (1 + 1) // 2 = 1
        chute = lista[meio] # meio = 2 logo chute = lista[2] = 5 | meio = 0 => chute = lista[0] = 1     | meio = 1 => chute = lista[1] = 3
        if chute == item: # chute 5 não é igual a item 3 = false | chute 1 não é igual a item 3 = false | chute 3 == item 3 => chute é igual a item
            return meio  #                                       |                                      | vai retornar a posição do item 3 que queriamos = 1
        if chute > item: # chute 5 é maior que item 3 = true     | chute 1 não é maior que item 3 false | A função retorna 1, indicando que o item 3 está na posição 1 da lista minha_lista
            alto = meio - 1 # meio - 1 => 2 - 1 = 1 => alto = 1  |                                      |
        else:                                                  # |                                      |
            baixo = meio + 1                                   # | baixo = meio + 1 => 0 + 1 = 1        |
    return None
    
minha_lista = [1, 3, 5, 7, 9]
    
print(pesquisa_binaria(minha_lista, 3)) # => 1
print(pesquisa_binaria(minha_lista, -1)) # => None