itens_desejados = input().split(", ")
itens_encontrados = input().split(", ")
itens = []
itens_faltante = []

for i in itens_desejados:
    if i in itens_encontrados:
        itens.append(i)
    else:
        itens_faltante.append(i)

if len(itens) == 0: 
     print(f"Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {len(itens_desejados)} itens aqui na fazenda.")

else:
    print("Estes são os itens que já tenho na fazenda:")
    for p in range(len(itens)):
            print(f"{p+1}º item: {itens[p]}")
    if itens == itens_desejados:
        print(f"Perfeito, encontrei todos os {len(itens_desejados)} itens aqui na fazenda!")
    else:
        print(f"Vou precisar adquirir {len(itens_faltante)} itens antes do festival!")
    
    print("Estou pronto para o festival de Stardew Valley! Que comece a diversão!")