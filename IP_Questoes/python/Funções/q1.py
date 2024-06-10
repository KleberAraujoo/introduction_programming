# função calculo cp maximo
def cp_maximo(ataque, defesa, stamina, cp_multiplicador):
    return (ataque * (defesa**0.5) * (stamina**0.5) * (cp_multiplicador**2)) / 10

# função para calcular se tem empate ou não
def desempate(cp_pokemon):
    maior_cp = -1
    pokemon_maior_cp = ""

    for pokemon in cp_pokemon:
        cp = pokemon[1]
        nome_do_pokemon = pokemon[0]

        if cp > maior_cp:
            maior_cp = cp
            pokemon_maior_cp = nome_do_pokemon
        elif cp == maior_cp and len(nome_do_pokemon) > len(pokemon_maior_cp):
            pokemon_maior_cp = nome_do_pokemon
        
    return pokemon_maior_cp, maior_cp
   
reg_pokemon = []
cp_pokemon = []


# codigo principal
while True:
    nome_pokemon = input()

    if nome_pokemon == "Fim":
        break
    
    if nome_pokemon in reg_pokemon:
        print("Opa, esse Pokémon já foi analisado.")
        continue
    
    reg_pokemon.append(nome_pokemon)
    
    ataque = int(input())
    defesa = int(input())
    stamina = int(input())
    cp_multiplicador = float(input())
    
    cp_max_pokemon = cp_maximo(ataque, defesa, stamina, cp_multiplicador)
    cp_pokemon.append((nome_pokemon, cp_max_pokemon))
    
    print("Pokémon computado com sucesso.")


if cp_pokemon:
    pokemon_maior_cp, maior_cp = desempate(cp_pokemon)
    print(f"O Pokémon com o maior CP na região de Kanto é: {pokemon_maior_cp}, com CP máximo de {maior_cp:.2f}")
else:
    print("Nenhum Pokémon foi registrado.")