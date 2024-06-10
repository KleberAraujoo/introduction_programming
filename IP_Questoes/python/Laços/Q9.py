num_musicas = int(input())
musica_atual = 1
palavra = ''
underline= ''
tentativa = 0

for i in range(num_musicas):
    musica = input()
    palavra = ''
    tentativas = 0

    print("Bem vindo ao jogo da forca do ye!")

    if i+1 != musica_atual:
        print(f"Esta é a música {i+1} de {num_musicas}.")
    else:
        print("Última música!")

    # Loop para guardar os '_' da palavra
    for j in musica:
        if j != " ":
            palavra += "_"
            tentativas += 2 # Numero de tentativas 
        else:
            palavra += ' '
            
    # Loop para verificar o jogo da forca
    while palavra != musica and tentativas != 0:

            
      