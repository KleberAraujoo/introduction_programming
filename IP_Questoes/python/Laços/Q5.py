candidato1=input()
candidato2=input()
delegado1=0
delegado2=0
c1=0
c2=0
totalvotos1=0
totalvotos2=0

if candidato1 != 'Kanye West' and candidato2 != 'Kanye West':
    print("Sem o Ye, sem eleição!")
else:
    estadoedelegado=input()
    while estadoedelegado != 'FIM':
        estado, delegado = estadoedelegado.split(", ") 
        votos1=input()
        votos2=input()
        while votos1=='Taylor Swift roubou as urnas!' or votos2=='Taylor Swift roubou as urnas!':
            print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
            votos1=input()
            votos2=input()
          
        votos1=int(votos1)
        if votos2 != 'FIM':
            votos2=int(votos2)
            if votos1 > votos2:
                porcentagem=(votos1/(votos1+votos2))*100
                print (f"{candidato1} obteve maioria no(a) {estado} com {int(porcentagem)}% dos votos.")
                delegado1+=int(delegado)
                c1+=1
                totalvotos1+=votos1
                estadoedelegado = input()
            elif votos2 > votos1:
                porcentagem=(votos2/(votos1+votos2))*100
                print (f"{candidato2} obteve maioria no(a) {estado} com {int(porcentagem)}% dos votos.")
                delegado2+=int(delegado)
                c2+=1
                totalvotos2+=votos2
        
        
        
    
    if c1 > c2 and candidato1 == 'Kanye West':
      print(f"Temos o resultado final! {candidato1} vence a disputa pela presidência, com o apoio de {delegado1} delegados do colégio eleitoral e {totalvotos1} votos populares.")
      print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
    elif c2 > c1 and candidato2 == 'Kanye West':
      print(f"Temos o resultado final! {candidato2} vence a disputa pela presidência, com o apoio de {delegado2} delegados do colégio eleitoral e {totalvotos2} votos populares.")
      print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
    elif c1 > c2 and candidato2 == 'Kanye West':
      print(f"Temos o resultado final! {candidato1} vence a disputa pela presidência, com o apoio de {delegado1} delegados do colégio eleitoral e {totalvotos1} votos populares.")
      print("Não tem problema, eu obtive o molho!")
    elif c2 > c1 and candidato1 == 'Kanye West':
      print(f"Temos o resultado final! {candidato2} vence a disputa pela presidência, com o apoio de {delegado2} delegados do colégio eleitoral e {totalvotos2} votos populares.")
      print("Não tem problema, eu obtive o molho!")