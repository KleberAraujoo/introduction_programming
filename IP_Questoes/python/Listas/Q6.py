# Anjolina 
# Vai receber um número inteiro que vai indicar a quantidade de galinheiros que a fazenda possui
# Vai receber uma entrada que é a especie de cada animal presente no galinheiro
# Coelho, galinha e pato

# Ricardo
# A gente vai receber uma lista das frutas que vai ser plantada 
# E depois outra lista contendo as sementes que estao sendo vendidas 
# porém pode ser que nao tenha todas as sementes para as frutas 

# Stefan
# a gente vai receber como entrada os materiais que stefan possui na mochila    
# depois a quantidade para cada item
# Para construir cada para-raios, necessitará de :
#“Barra de ferro” (1 unidade)
#“Quartzo refinado” (1 unidade)
#“Asa de morcego” (5 unidades)

# Anjolina
num_galinheiros = int(input())
qntd_coelho, qntd_galinha, qntd_pato = 0,0,0

for i in range(num_galinheiros):
    especie = input().split(", ")
    for j in especie:
        if j == "Coelho": 
            qntd_coelho += 1
        elif j == "Galinha": 
            qntd_galinha += 1
        else: 
            qntd_pato += 1
    
# Verifica se tem pelo menos um coelho, galinha e pato
if qntd_coelho >= 1: print(f"A fazenda tem {qntd_coelho} coelhos!")
else: print("Poxa que pena, não temos coelhos.")
if qntd_galinha >= 1: print(f"A fazenda tem {qntd_galinha} galinhas!")
else: print("Poxa que pena, não temos galinhas.")
if qntd_pato >= 1: print(f"A fazenda tem {qntd_pato} patos!")
else: print("Poxa que pena, não temos patos.")


# Ricardo
# Lista de frutas que vai comprar e lista das sementes que estão vendendo 
lista_frutas, sementes = input().split(", "), input().split(", ")
lista_compras = []

if "Melão" in lista_frutas: print("Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...")

lista_compras = [x for x in lista_frutas if x in sementes]

if len(lista_compras) == len(lista_frutas):
    print("Consegui comprar todas as frutas que queria!")

elif len(lista_compras) > 1:
    print("Consegui comprar as seguintes sementes:")
    lista_de_compra_alfabetica = sorted(lista_compras)
    print(", ".join(lista_de_compra_alfabetica))
else:
    print("Poxa, acho que ficaremos sem plantações.")

# Stefan
materiais_stefan = input().split(", ")
qntd_itens = input().split(", ")
para_raio = []

for y in range(len(materiais_stefan)):
    item = materiais_stefan[y]
    quantidade = int(qntd_itens[y])

    if item == "Barra de ferro" or item == "Quartzo refinado" or item == "Asa de morcego":
        # Calcula quantos para-raios Stefan pode construir com base na quantidade de cada item
        if item == "Asa de morcego":
            para_raio.append(quantidade // 5)  # Para cada para-raio são necessárias 5 asas de morcego
        else:
            para_raio.append(quantidade)  # As barras de ferro e quartzo refinado são usadas em quantidade igual à necessária para cada para-raio
    else:
        continue

num_para_raios = min(para_raio)
print(f"Com os itens que tenho, consigo fazer {num_para_raios} para-raios!")

    








