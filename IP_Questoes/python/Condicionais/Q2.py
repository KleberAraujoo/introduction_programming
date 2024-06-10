# pistas: Mônaco, Ímola ou Spa-Francorchamps.
# 250km/h e a máxima foi de 260km/h em Mônaco.
# 261km/h e a máxima foi de 285km/h em Ímola.
# 286km/h e a máxima foi de 310km/h em Spa-Francorchamps.
# Tempo ensolarado, chuvoso ou neblina.
# Com o tempo ensolarado, não existem mudanças no padrão de velocidade atingida por ele na pista.
# Com o tempo chuvoso, para Senna nada mudava. Ele era o rei da chuva!
# Por último, quando havia neblina, a velocidade máxima que Senna atingia na pista na qual corria era equivalente à 
# velocidade máxima da pista imediatamente anterior. Entenda Mônaco como anterior à Ímola e Ímola como anterior à Spa-Francorchamps.

vel_maxima = int(input())
tempo = input()

if tempo == "neblina":
    if 286 <= vel_maxima <= 310: # antes era spa e agora ta monaco
        print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")

    elif 261 <= vel_maxima <= 285: # antes era imola e ta spa
        print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")

    elif 250 <= vel_maxima <= 260: # antes era monaco e agora ta imola
        print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
else:
    if  250 <= vel_maxima <= 260  and tempo == "ensolarado" or tempo == "chuvoso":
        print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")

    elif 261 <= vel_maxima <= 285 and tempo == "ensolarado" or tempo == "chuvoso":
        print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")

    elif 286 <= vel_maxima <= 310 and tempo == "ensolarado" or tempo == "chuvoso":
        print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")

