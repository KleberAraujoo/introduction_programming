parada = False
suspeito = []

while not parada:
    entrada = input()

    if entrada == "Sujeito mais perigoso do que pensávamos":
        indice_atual, indice_atualizar = int(input()), int(input())
        suspeito[indice_atual], suspeito[indice_atualizar] = suspeito[indice_atualizar], suspeito[indice_atual]
        
    elif entrada == "Que estranho, esses dois meliantes… troque-os de lugar":
        nome_1, nome_2 = input(), input()
        indice_nome_1, indice_nome_2 = suspeito.index(nome_1), suspeito.index(nome_2)
        suspeito[indice_nome_1], suspeito[indice_nome_2] = suspeito[indice_nome_2], suspeito[indice_nome_1]
    
    elif entrada == "Novo suspeito - altíssima periculosidade":
        suspeito.insert(0, input())
        
    elif entrada == "Novo suspeito - pouco perigoso":
        suspeito.append(input())
    
    elif entrada == "Livre de suspeita, pode remover":
        name = input()
        suspeito.remove(name)

    elif entrada == "Essa posição não esta de acordo, ele não e tão perigoso assim":
        nome = input()
        if nome in suspeito:
            suspeito.remove(nome)
            suspeito.append(nome)
        else:
            suspeito.append(nome)

    elif entrada == "Como a lista esta ficando?":
        print(", ".join(suspeito))
    
    elif entrada == "Já temos nossa lista de suspeitos":
        parada = True

print("O resultado final ficou assim:")
print(", ".join(suspeito))


