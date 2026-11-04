from cores import *
print()
print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*16 )
print()

# teste = list()
# teste.append('Gay')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# print(teste)
# teste[0] = 'Maria'
# teste[1] = 22
# print(teste)
# print(galera)
# galera.append(teste[:])
# print(galera)
# galera = [['gay', 24],['ana', 33],['gay2', 13], ['maria',45] ]
# # print(galera[2][1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos.')

# galera = list()
# dado = list()
# totalmaior = totalmenor = 0
# for c in range(0,4):
    # dado.append(str(input('Nome: ')))
    # dado.append(int(input('Idade: ')))
    # galera.append(dado[:])
    # dado.clear()
# print(galera)
#
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade')
#         totalmaior += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totalmenor += 1
# print(f'Total de maior de idade: {totalmaior}')
# print(f'Total de menor de idade: {totalmenor}')


# desafio 84
# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas,
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves.

# pessoas = list()
# dados = list()
# listamaior = list()
# listamenor = list()
# maiorpeso = menorpeso = 0
#
# while True:
#     nome = str(input(f'Digite o {len(pessoas)+1}º nome ou "sair" para finalizar: '))
#     if nome.lower() == 'sair':
#         break
#     peso = input(f'Digite o peso de {nome}: ')
#     try:
#         peso = int(peso)
#
#     except ValueError:
#         print(f'Peso {VERMELHO}invalido{LIMPA}!')
#         continue
#
#     print(f'{nome} {VERDE}adicionado{LIMPA} com sucesso!')
#     dados.append(nome)
#     dados.append(peso)
#     pessoas.append(dados[:])
#
#     if len(pessoas) == 1:
#         maiorpeso = peso
#         menorpeso = peso
#
#     if peso > maiorpeso:
#         maiorpeso = peso
#         listamaior.clear()
#         listamaior.append(dados[:])
#     elif peso == maiorpeso:
#         listamaior.append(dados[:])
#
#     if peso < menorpeso:
#         menorpeso = peso
#         listamenor.clear()
#         listamenor.append(dados[:])
#     elif peso == menorpeso:
#         listamenor.append(dados[:])
#
#     dados.clear()
#
# print(f'{"A pessoa" if len(listamaior) == 1 else "As pessoas"} com o maior peso {"é" if len(listamaior) == 1 else "são"} '
#       f'{", ".join([p[0] for p in listamaior])} com {listamaior[0][1]} Kilos')
# print(f'{"A pessoa" if len(listamenor) == 1 else "As pessoas"} com o menor peso {"é" if len(listamenor) == 1 else "são"} '
#       f'{", ".join([p[0] for p in listamenor])} com {listamenor[0][1]} Kilos')
# print(f'O total de nomes cadastrados foi: {len(pessoas)}')



# desafio 85
# crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e impares em ordem crescente


# lista = [[], []]
#
# for n in range(0,7):
#     while True:
#         numero = input(f'Digite o {n+1}º numero: ')
#         try:
#             numero = int(numero)
#         except ValueError:
#             print(f'Valor {VERMELHO}invalido{LIMPA}')
#             continue
#         if numero % 2 == 0:
#             lista[0].append(numero)
#             print(f'valor {VERDE}adicionado{LIMPA} com sucesso')
#         elif numero % 2 == 1:
#             lista[1].append(numero)
#             print(f'valor {VERDE}adicionado{LIMPA} com sucesso')
#         break
# lista[0].sort()
# lista[1].sort()
# print(f'Os valores pares foram {lista[0]}.')
# print(f'Os valores impares foram {lista[1]}.')




# desafio 86
# crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta


# matrix = list()
# for c in range(0,3):
#     numero = int(input(f'Digite o {c+1}º termo da primeira linha: '))
#     matrix.append(numero)
# for c in range(0,3):
#     numero = int(input(f'Digite o {c+1}º termo da segunda linha: '))
#     matrix.append(numero)
# for c in range(0,3):
#     numero = int(input(f'Digite o {c+1}º termo da terceira linha: '))
#     matrix.append(numero)
# print(f'[{matrix[0]:^5}][{matrix[1]:^5}][{matrix[2]:^5}]')
# print(f'[{matrix[3]:^5}][{matrix[4]:^5}][{matrix[5]:^5}]')
# print(f'[{matrix[6]:^5}][{matrix[7]:^5}][{matrix[8]:^5}]')



# desafio 87
# aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma_pares = 0
maior_segunda_linha = 0
for l in range(0,3):
    for c in range(0,3):

        while True:
            numero = input(f'Digite o termo da linha {l} e coluna {c}: ')
            try:
                numero = int(numero)
            except ValueError:
                print(f'Valor {VERMELHO}invalido{LIMPA}')
                continue
            matriz[l][c] = numero
            print(f'Valor {VERDE}adicionado{LIMPA}')
            if numero % 2 == 0:
                soma_pares += numero
            break
print()
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
matriz[1].sort()
print(f'A soma dos numeros pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {matriz[1][2]}')



# desafio 88
#  que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos serão jogos
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

# desafio 89
# que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


print('\n','='*15,f'{VERMELHO} FIM {LIMPA}','='*20)