qntd_pessoas = int(input())
frase1 = "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!"
frase2 = "Não gostei. Muito sem graça, onde já se viu nome com duas letras?"
frase3 = "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso."
aprovacao = 0
rejeicao = 0
abstencao = 0

for i in range(qntd_pessoas):
    pessoa = input()

    if pessoa == frase1:
        aprovacao += 1
    elif pessoa == frase2:
        rejeicao += 1
    else:
        abstencao += 1

totais = aprovacao + rejeicao + abstencao
taxa_de_aprovacao = "{:.2f}".format((aprovacao / totais)*100)
taxa_de_rejeicao =  "{:.2f}".format((rejeicao / totais)*100)
taxa_de_abstencao =  "{:.2f}".format((abstencao / totais)*100)

print("A pesquisa terminou e os resultados foram os seguintes:")
print(taxa_de_aprovacao)
print(taxa_de_rejeicao)
print(taxa_de_abstencao)

if taxa_de_aprovacao > taxa_de_rejeicao:
    print("YES!!! Sabia que as pessoas gostariam!")
elif taxa_de_aprovacao < taxa_de_rejeicao:
    print("Ops... Por essa eu não esperava.")
else:
    print("Bom... Vou olhar para o copo meio cheio!")

