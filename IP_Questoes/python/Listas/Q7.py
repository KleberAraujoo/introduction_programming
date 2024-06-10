dimensao = input().split(" x ") # Dimensão da matriz
linha = int(dimensao[0]) # Linha da matriz
coluna = int(dimensao[1]) # Coluna da matriz

# Criação da matriz
matriz = []
for x in range(linha):               
    linha_elemento = []
    for y in range(coluna):
        linha_elemento.append(0)
    matriz.append(linha_elemento)

# Recebe a quantidade de elementos que tera nivel de atratividade juntamente com sua coordenada que precisara ser posicionada na matriz
qntd_elementos = int(input())
for p in range(qntd_elementos):
    elemento = input().split(" ")  # Separa o nível de atratividade da coordenada
    atratividade = int(elemento[0])  # Convertendo o nível de atratividade para inteiro
    coordenada = elemento[1].replace("(", "").replace(")", "")  # Essa variável coordenada é usada para pegar a coordenada da lista de elementos e retirar os parênteses
    linha_elemento, coluna_elemento = map(int, coordenada.split(","))  # A linha e a coluna é equivalente à coordenada
    matriz[linha_elemento][coluna_elemento] = atratividade  # Coloca a atratividade nos valores da linha e da coluna da matriz


operacao = input() # Recebe a operação que será feita
while operacao != 'Fim':

    # Permutação da matriz
    if operacao == "Permutar":
        entrada = input().split(" ") # Recebe as duas coordenadas que contem o elemento para permutar e transforma em uma lista
        coordenada_permutacao_1, coordenada_permutacao_2 = entrada[0].replace("(", "").replace(")", ""), entrada[1].replace("(", "").replace(")", "") # Pega a primeira e segunda coordenada 
        linha_permutacao_1, coluna_permutacao_1 = coordenada_permutacao_1.split(",") # Linha e Coluna da primeira coordenada para permutar
        linha_permutacao_2, coluna_permutacao_2 = coordenada_permutacao_2.split(",") # Linha e coluna da segunda coordenada para permutar 
        elemento_1_matriz, elemento_2_matriz  = matriz[int(linha_permutacao_1)][int(coluna_permutacao_1)], matriz[int(linha_permutacao_2)][int(coluna_permutacao_2)] # Variavel para guardar o elemento que esta na posicao (x,y) da natruz
        matriz[int(linha_permutacao_1)][int(coluna_permutacao_1)], matriz[int(linha_permutacao_2)][int(coluna_permutacao_2)] = elemento_2_matriz, elemento_1_matriz # A coordenada (x,y) da matriz irá receber o elemento em questão

    # Transposição de Matriz
    elif operacao == "Transposição":
        transposta = []
        for c in range(coluna):
            linha_transposta = []
            for l in range(linha):
                linha_transposta.append(matriz[l][c])
            transposta.append(linha_transposta)
        matriz = transposta
        linha, coluna = coluna, linha
    
    # Remoção do menor elemento da Matriz
    elif operacao == "Remover":
        menor_nivel = 1000000
        for l in range(linha):
            for c in range(coluna):
                if matriz[l][c] != 0 and matriz[l][c] < menor_nivel:
                    menor_nivel = matriz[l][c]
        for l in range(linha):
            for c in range(coluna):
                if matriz[l][c] == menor_nivel:
                    matriz[l][c] = 0

    operacao = input() # Recebe a operação que será feita


print("Atual Arranjo:")
for m in range(linha):
    for n in range(coluna):
        if n < coluna - 1:
            print(matriz[m][n], end=' ')
        else:
            print(matriz[m][n])
