# Serão n decisões 
# As seguintes n linhas de entrada serão as práticas de programação
# a cada pratica vai ter uma pontuacao que deve ser atribuida
# e também vai precisar saber quantas praticas foram, entao criar uma variavel para armazenar as quantidades de praticas no loop
# vai precisar fazer uma media aritmetica da pontuacao obtida com as praticas de progrmacao recebidas
# media aritmetica é somar a quantidade da pontuação e dividir pelo numero de praticas 
# Se a soma das pontuações for negativa, atribuir 0 à pontuação total.
# Se o número de n linhas que é as praticas de programacao for zero, deve-se considerar que a média de Kayne foi zero.
# Se a média for acima de 10, atribuir 10 à media. Faça isso depois de extrair a média aritmética.

decisoes = int(input())
pontos = 0
stop = False

if decisoes == 0:
    media = 0
    print("É melhor voltar a cantar mesmo!")
    stop = True
else:
    for i in range(decisoes):
        praticas = input()

        if praticas == "Programar utilizando uma boa IDE":
            pontos += 3
        elif praticas == "Códigos limpos e organizados" or praticas == "Assistir às aulas do REDU" or praticas == "Tirar dúvidas com os monitores e professores":
            pontos += 10
        elif praticas == "Nomenclatura objetiva e de fácil identificação de variáveis":
            pontos += 7
        elif praticas == "Comentários significativos" or praticas == "Evitar repetições desnecessárias de códigos":
            pontos += 5
        elif praticas == "Programar sem utilizar IDE" or praticas == "Nomenclatura confusa e difícil de identificar variáveis":
            pontos -= 5
        elif praticas == "Código bagunçado e mal estruturado":
            pontos -= 6
        else:
            pontos -= 1


    media = (pontos/ i)

    if media > 10:
        media = 10
    elif media < 3: #media menor que 3
        print("É melhor voltar a cantar mesmo!")
        
    elif media < 7: #media maior ou igual a 3 e menor que 7
        print("Vai precisar se esforçar um pouco mais, meu cantor!")

    elif media == 7: #media igual a 7
        print("Na conta certa!")

    elif media <= 9: #media maior que 7 e menor ou igual a 9
        print("Nasceu para programar!")

    else: #media cima de 9
        print("Já pode ser chamado de Kanye, the dev, West!")