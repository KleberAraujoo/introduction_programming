agricultura, criacao_animais, pesca, mineracao = input().split(" - "), input().split(" - "),  input().split(" - "), input().split(" - ")
stop = False
primeira = False

while not stop:
    indice_agricultura, indice_criacao_animais, indice_pesca, indice_mineracao = int(input()), int(input()), int(input()), int(input())
    
    if not primeira:
      print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")
    
    print("Combinando Itens...")
    
    item_1, item_2, item_3, item_4 = agricultura[indice_agricultura], criacao_animais[indice_criacao_animais], pesca[indice_pesca], mineracao[indice_mineracao]
    
    for i in range(1):
        print(f"Item para agricultura: {item_1}")
        print(f"Item para criação: {item_2}")
        print(f"Item para pesca: {item_3}")
        print(f"Item para mineração: {item_4}")

    opiniao = input()
    if opiniao == "Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...":
        print("Meu dia tá garantido, obrigado pela ajuda Pega Móvel!")
        stop = True
    else:
        escolha = input()
        if escolha == "Bom, vamos tentar mais uma vez...":
            primeira = True
            continue
        else:
            print("É... acho que já chega de Stardew por hoje...")
            stop = True