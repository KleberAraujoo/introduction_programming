nome_ouvinte = input()
quantidade_musicas = int(input())

stream_maximo = 0
stream_minimo = float('inf')
musica_mais_ouvida = ''
musica_menos_ouvida = ''

if quantidade_musicas == 0:
        print(f"{nome_ouvinte} é team Taylor e não ouviu Kanye West")
else:
    for i in range(quantidade_musicas):
        musica = input()
        quantidade_streams = int(input())

        if quantidade_streams > stream_maximo:
                musica_mais_ouvida = musica
                stream_maximo = quantidade_streams
            
        if quantidade_streams < stream_minimo:
                musica_menos_ouvida = musica
                stream_minimo = quantidade_streams

    if quantidade_musicas == 1:
            print(f"A única música que {nome_ouvinte} ouviu foi {musica} com {quantidade_streams} streams")
    elif stream_maximo == stream_minimo:
            print(f"A música que {nome_ouvinte} mais ouviu foi {musica_mais_ouvida} com {stream_maximo} streams")
    else:
            print(f'A música que {nome_ouvinte} mais ouviu foi {musica_mais_ouvida} com {stream_maximo} streams')
            print(f'A música que {nome_ouvinte} menos ouviu foi {musica_menos_ouvida} com {stream_minimo} streams')




        

