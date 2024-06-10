# Pontuação
pontuacao_Charles = int(input())
pontuacao_Max = int(input())

# Classificou?
if pontuacao_Charles == 0:
    print("Oxe! E vai morrer por causa de 25 pontos?")
else: 
    if pontuacao_Charles == 25:
        print("O meu favorito venceu! Pode torar o aco Verstappen")
    elif 15 <= pontuacao_Charles < 25:
        print("Esse Charles eh arretado mesmo")
    elif 10 <= pontuacao_Charles < 18:
        print("Ele eh desenrolado demais")

    # Diferença entre Charles e Max
    diferenca = abs(pontuacao_Charles - pontuacao_Max)
    if diferenca <= 4 and pontuacao_Charles > pontuacao_Max:
        print("Ta com a molestia, vai perder para Max Verstappen eh")
    elif diferenca <= 4 and pontuacao_Charles < pontuacao_Max:
        print("Ta com a molestia, vai perder para Max Verstappen eh")
    elif diferenca > 4 and pontuacao_Charles > pontuacao_Max:
        print("Deu o sangue")
