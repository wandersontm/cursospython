#aula 4:

heroi = input("qual o nome do seu heroi?")
while True:
    sexo = input("Digite seu gênero (Feminino/Masculino): ").strip().lower()

    if sexo in ['feminino', 'f']:
        sexo = "feminino"
        break
    elif sexo in ['masculino', 'm']:
        sexo = "masculino"
        break
    else:
        print("Opção inválida. Por favor, digite 'Feminino' ou 'Masculino'.")

print(f"{heroi}, sua aventura começa agora!")

#aula 6:
monstro = str(input(f"digite o nome do monstro: "))
vida = int(100)
o = str("a") if sexo == "feminino" else str("o")
O = str("A") if sexo == "feminino" else str("O")
print(f"durante sua aventura, voce se deparou com um {monstro} agresivo")
print(input("(aperte enter para continuar)"))
print(f"o {monstro} ataca {o} {heroi}!")

while True:
    try:
        # Tenta converter a entrada para inteiro
        a1 = int(input(f"digite o ataque do {monstro}: "))

        # Se sucesso, sai do loop (break)
        break

    except ValueError:
        # Se falhar (ex: usuário digitou "abc"), executa este bloco
        print("Por favor, digite apenas números inteiros.")

while True:
    try:
        # Tenta converter a entrada para inteiro
        d2 = int(input(f"digite a defesa d{o} {heroi}: "))

        # Se sucesso, sai do loop (break)
        break

    except ValueError:
        # Se falhar (ex: usuário digitou "abc"), executa este bloco
        print("Por favor, digite apenas números inteiros.")

if a1 <= d2:
    print(f"{O} {heroi} conseguiu evitar o ataque do {monstro}!")
else:
    print(f":O {monstro} mordeu a perna d{o} {heroi}, causando {a1 - d2} de dano!")
    print(f"Restando agora {vida - (a1 - d2)} pontos de vida")
