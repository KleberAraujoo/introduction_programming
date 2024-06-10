# primeira entrada é um N inteiro que indica a quantidade de exercicios que serão realizados em cada um dos treinos
# A quantidade de exercícios por treino será a mesma para TODOS os treinos e padre Marcelo irá ouvir UMA música por exercício.
# a cada inicio de treino a gente vai receber uma string indicando o tipo de treino
# se for fim do treino então o treino é finalizado




qntd_exercicios = int(input())
stop = False
tipo_de_treino = input()

for i in range(qntd_exercicios):
    if not stop:
        print(tipo_de_treino)
        pont_musica_boa = 0

        for j in range(qntd_exercicios):
            musica = input()
            nota_musica = int(input())

            print(f"{j+1}° música {musica} tocando agora")

            if nota_musica >= 7: 
                print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
                pont_musica_boa += 1
            else:
                print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")

    if not stop:   
            eficacia = (j+1)/2
            if pont_musica_boa >= j+1 or pont_musica_boa >= eficacia: 
                print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
            else:
                print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")
    if not stop:   
        tipo_de_treino = input()
        if tipo_de_treino == "Fim do Treino":
            stop = True