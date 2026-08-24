# frase = 'Olá gay!'
# print(frase)
# print(frase[1::2])  # faz um fatiamento do texto
# print(len(frase))  # mostra o tamanho do texto
# print(frase.count('a', 4, 7))  # conta quantas vezes aparece o texto pesquisado e pode ser delimitado um fatiamento
# print(frase.find('gay'))  # mostra a posição que começa o texto pesquisado
# print('gay' in frase)  #boolean da pesquisa no texto
# print(frase.replace('gay', 'mundo'))  # troca um termo por outro dentro da string
# print(frase.upper())  # transforma em maiúsculo
# print(frase.lower())  # transforma em minusculo
# print(frase.capitalize())  # transforma a primeira letra em maiúsculo
# print(frase.title())  # analisa quantas palavras e trans as primeiras letras em maiúsculo
# novo = '   Aprenda Python  '
# print(novo)
# print(novo.strip())  #remove espaços antes e depois do texto
# print(novo.rstrip())  #remove espaço depois do texto
# print(novo.lstrip())  #remove espaço antes do texto

# print(frase.split())  #separa em palavras separadas por espaço, criando uma lista
# print('_'.join(frase.split())) #junta novamente a lista, com o separador usado

# desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# o nome com todas as letras em minusculas
# quantas letras ao total sem considerar espaços
# quantas letras tem o primeiro nome

# nome = input('Qual é seu nome? ').strip()
# nome = 'Marcos Joao Junior'
# print(nome.upper())
# print(nome.lower())
# print(nome.title())
# print(nome.split())
# print('len em nome é:' , len(nome))
# print(''.join(nome.split()))
# print('O total de letras é:',len(''.join(nome.split())))
# print('O total de letras é:', len(nome) - nome.count(' '))
# separador = nome.split()
# print(separador[0])
# print('O total de letras do primeiro nome é:',len(separador[0]))



# desafio 23
# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: digite um número: 1834
# unidade 4
# dezena 3
# centena 8
# milhar 1

# numero = input('digite um número com 4 casas: ')
#
# while True:
#     if len(numero) == 4 and numero.isdigit():
#         print('seu milhar é:', numero[0])
#         print('sua centena é:', numero[1])
#         print('sua dezena é:', numero[2])
#         print('sua unidade é', numero[3])
#         break
#     else:
#         numero = input('digite um número com 4 casas: ')

# numero = int(input('Informe um numero: '))
# num = str(numero)
# while True:
#     if (len(num)) < 5:
#         u = numero // 1 % 10
#         d = numero // 10 % 10
#         c = numero // 100 % 10
#         m = numero // 1000 % 10
#         print(f'A unidade é: {u}')
#         print(f'A dezena: {d}')
#         print(f'A centena: {c}')
#         print(f'A milhar: {m}')
#         break
#     else:
#         numero = int(input('Informe um numero ate 9999: '))
#         num = str(numero)


# desafio 24
# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# frase = input('digite o nome de uma cidade: ')
#
# frase = frase.lower()
# if frase.find('santo') == 0:
#     print('Essa cidade começa com a palavra Santo')
# else:
#     print('essa cidade não começa com a palavra Santo')

# frase = input("Digite o nome de uma cidade: ").strip().lower()
# frase_separado = frase.split()
# if frase_separado[0] == "santo":
#     print('Essa cidade começa com a palavra Santo')
# else:
#     print('Essa cidade não começa com a palavra Santo')


# desafio 25
# crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# frase = input("Digite o nome de uma pessoa: ").strip().lower()
# frase_separado = frase.split()
# if "silva" in frase_separado:
#     print('Esta pessoa tem silva no nome')
# else:
#     print('Esta pessoa não tem silva no nome')


# desafio 26
# faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

# frase = input("Digite uma frase: ").strip().lower()
# frase = 'a rua de dona joana tem nove casas'
# print(frase)
# frase_separado = frase.split()
# print(len(frase))
# print('A quantidade de "A" é igual a: ',frase.count("a"))
# print(frase.find('a'))
# print(frase.rfind('a'))


# desafio 27
# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

# frase = input("Digite um nome: ").strip().lower()
# nome = frase.split()
# print(nome[0])
# print(nome[-1])