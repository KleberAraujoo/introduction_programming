lista_peixes = ["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar", "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]

#Pescador: Pescar pelo menos 5 peixes diferentes.
#Velho Marinheiro: Pescar pelo menos 10 peixes diferentes.
#Velho Pescador: Pescar todos os tipos de peixes do vale.
#Deus Pescador: Pescar pelo menos 25 peixes no total.
stop = False

for i in range(3):
    parada = False
    verdade = False
    qntd_peixes_pescador = 0
    qntd_peixes_marinheiro  = 0
    qntd_peixes_deus = 0
    lista_peixe_pescador = []
    nome, conquista = input().split(':') 
    conquista = conquista.strip().split(", ")

    while not parada:
        peixe = input()
        if peixe in lista_peixes:
            lista_peixe_pescador.append(peixe)
        elif peixe == "FIM":
            parada = True
        
    if 'Pescador' in conquista:
        peixes_unicos_pescador = []
        for peixe in lista_peixe_pescador:
            if peixe not in peixes_unicos_pescador:
                peixes_unicos_pescador.append(peixe)
        if len(peixes_unicos_pescador) >= 5:
            verdade= True
        else:
            verdade = False

    if 'Velho Pescador' in conquista:
        if len(lista_peixe_pescador) == len(lista_peixes):
            verdade = True
        else:
            verdade = False

    if 'Velho Marinheiro' in conquista:
        peixes_unicos_marinheiro = []
        for peixe in lista_peixe_pescador:
            if peixe not in peixes_unicos_marinheiro:
                peixes_unicos_marinheiro.append(peixe)
        if len(peixes_unicos_marinheiro) >= 10:
            verdade= True
        else:
            verdade = False

    if 'Deus Pescador' in conquista and len(lista_peixe_pescador) >= 25:
        verdade = True

    if verdade:
        print(f"{nome} realmente estava falando a verdade!!!")
    else:
        print(f"{nome} é um mentiroso, ele não tem todas essas conquistas!")