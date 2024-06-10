#cin award - kanye x taylor
num_rodadas = int(input())
kanye_ponto_rodada = 0
kanye_vitorias = 0
kanye_desordem = 0
perdeu_desordem = False
taylor_ponto_rodada = 0
taylor_vitorias = 0
taylor_desordem = 0

while(kanye_vitorias < 3 and kanye_desordem < 3):
    for i in range(1, num_rodadas+1): #vai realizar o loop conforme o numero de rodadas fornecido
        print(f"{i}° RODADA:") #print inicial
        kanye_musica = input()
        for j in range(3):
            avaliacao = input()
            if(avaliacao == "boa"):
                kanye_ponto_rodada += 2 
            elif(avaliacao == "média"):
                kanye_ponto_rodada += 1
            elif(avaliacao == "ruim"):
                kanye_ponto_rodada -= 3 
            elif(avaliacao == "péssima"):
                fas_desordenados = True
                while(fas_desordenados):
                    frases_aleatorias = input()
                    if(frases_aleatorias == "ORDEM"):
                        fas_desordenados = False
                    else:
                        kanye_desordem += 1 #soma de pontos conforme a desordem não recebe "ORDEM"
                if(kanye_desordem >= 5):
                    perdeu_desordem = True
                    artista_perdedor = "Kanye West" #kanye perdeu por desordem dos fas
                    artista_vencedor = "Taylor Swift"
        if(not perdeu_desordem): #kanye nao perdeu por desordem, contar pontos e imprimir vencedor da rodada
            taylor_musica = input()
            for k in range(3):
                avaliacao = input()
                if(avaliacao == "boa"):
                    taylor_ponto_rodada += 2 
                elif(avaliacao == "média"):
                    taylor_ponto_rodada += 1
                elif(avaliacao == "ruim"):
                    taylor_ponto_rodada -= 3
                elif(avaliacao == "péssima"):
                    fas_desordenados = True
                    while(fas_desordenados):
                        frases_aleatorias = input()
                        if(frases_aleatorias == "ORDEM"):
                            fas_desordenados = False
                        else:
                            taylor_desordem += 1
                    if(taylor_desordem >= 5):
                        perdeu_desordem = True
                        artista_perdedor = "Taylor Swift"
                        artista_vencedor = "Kanye West"
            #comparar pontuacao de cada um pra rodada e definir o vencedor da rodada
            if(kanye_ponto_rodada > taylor_ponto_rodada):
                kanye_vitorias += 1
                artista_vencedor = "Kanye West"
                artista_perdedor = "Taylor Swift"
            elif(kanye_ponto_rodada == taylor_ponto_rodada):
                print(f"Não houve vencedor na {i}° rodada")
            else:
                taylor_vitorias +=1
                artista_vencedor = "Taylor Swift"
                artista_perdedor = "Kanye West"
            print(f"O(a) vencedor(a) da {i}° rodada foi {artista_vencedor}")
            
        else: #print do vencedor por desordem
            print(f"Os fãs do(a) {artista_perdedor} causaram tanta desordem que ele(a) perdeu o prêmio!")
            print(f"O(a) vencedor(a) do Cin Awards é {artista_vencedor}, parabéns!")
#comparar pontuacao de cada um pra rodada atual e definir o vencedor da competicao por merito
vitorias_vencedor = 0
if(kanye_vitorias > taylor_vitorias):
    artista_vencedor = "Kanye West"
    vitorias_vencedor = kanye_vitorias
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {vitorias_vencedor} vitórias, é {artista_vencedor}, parabéns!")
elif(kanye_vitorias == taylor_vitorias):
    print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")
else:
    artista_vencedor = "Taylor Swift"
    vitorias_vencedor = taylor_vitorias
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {vitorias_vencedor} vitórias, é {artista_vencedor}, parabéns!")