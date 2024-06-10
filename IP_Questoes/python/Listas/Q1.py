num_animais = int(input())
lista_animais = []

while num_animais != len(lista_animais):
    comando = input()
 
    if comando == "REGISTRA":
        animal = input()
        if animal in lista_animais:
            print(f"{animal} já foi registrado antes!")
        else:
            lista_animais.append(animal)
            print(f"{animal} registrado com sucesso.")

    elif comando == "CORRIGE":
        if len(lista_animais) != 0:
            lista_animais.pop()
            print("Último registro apagado com sucesso.")
        else:
            print("O catálogo ainda está vazio.")
    
    elif comando == "REINICIA":
        lista_animais = []
        print("Catálogo redefinido com sucesso.")

print("Todos os animais foram registrados!")
print("\nCatálogo de animais:")

for i in range(len(lista_animais)):
    print(f"{i+1}: {lista_animais[i]}")