from cores import *

# maça = 0
# while not maça == 3:
#     print('Funciona?')
#     for c in range(0, 3):
#         maça +=1
#         c -=1
#         print(f'Contando maças {maça}')


print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*15 )

# desafio 57
#  que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação
# novamente até ter um valor correto.

# sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
# while sexo != 'M' and sexo != 'F' and sexo != 'MASCULINO' and sexo != 'FEMININO':
#     print('Sexo invalido, digite novamente!')
#     sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
# if sexo == 'M' or sexo == 'MASCULINO':
#     print(f'O sexo da pessoa é masculino')
# elif sexo == 'F' or sexo == 'FEMININO':
#     print(f'O sexo da pessoa é feminino')



# desafio 58
# melhore o jogo do desafio 028, o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# from random import randint
# computador = randint(0,10)
# player = int(input(f'Tente adivinhar qual o {LILAS}numero{LIMPA} entre 0 e 10: '))
# contador = 0
# while player not in range(0,11):
#     player = int(input('Entrada errada! Por favor, digite um número entre 0 e 10!!!'))
# while computador != player:
#     print()
#     print(f'{VERMELHO}Que pena{LIMPA}!! Você não acertou!')
#     contador += 1
#     print(f'Você já tentou {contador} vezes')
#     if computador > player:
#         print(f'{VERDE}DICA!!!{LIMPA} Fale um número {BRANCO_UNDERLINE}maior{LIMPA}!!')
#     elif computador < player:
#         print(f'{VERDE}DICA!!!{LIMPA} Fale um número {BRANCO_UNDERLINE}menor{LIMPA}!!')
#     player = int(input(f'{AZUL}tente novamente{LIMPA} entre 0 e 10: '))
#     while player not in range(0, 11):
#         player = int(input('Entrada errada! Por favor, digite um número entre 0 e 10!!!'))
# print(f'{AMARELO_BOLD}Parabens você acertou!{LIMPA} você precisou de {VERMELHO}{contador} vezes{LIMPA} para conseguir!!!')



# desafio 59
# que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#deverá realizar a operação solicitada em cada caso.

# programa = 0
# print(VERDE, '=-' * 30, LIMPA)
# print(f'Calculadora de dois valores!!')
#
# while True:
#     try:
#         n1 = float(input('Digite o 1º valor: '))
#         break
#     except ValueError:
#         print('Entrada invalida!')
#
# while True:
#     try:
#         n2 = float(input(f'Digite o 2º valor: '))
#         break
#     except ValueError:
#         print('Entrada invalida!')
#
# while programa not in [1,2,3,4,5]:
#
#     print()
#     print(f'As opções de operação são as seguintes:')
#     print(' [1] Somar;')
#     print(' [2] Multiplicar;')
#     print(' [3] Maior;')
#     print(' [4] Novos números;')
#     print(' [5] Sair.')
#     try:
#         programa = int(input('Digite a opção: '))
#     except ValueError:
#         print('Opção invalida! digite novamente: ')
#
#     while programa == 1:
#         print(f'A soma de {n1} e {n2} é igual à: {n1+n2}!!')
#         try:
#             programa = int(input('Digite a opção: '))
#         except ValueError:
#             print('Opção invalida! digite novamente: ')
#     while programa == 2:
#         print(f'A multiplicação de {n1} e {n2} é {n1*n2}!!')
#         try:
#             programa = int(input('Digite a opção: '))
#         except ValueError:
#             print('Opção invalida! digite novamente: ')
#     while programa == 3:
#         if n1 > n2:
#             print(f'{n1} é maior que {n2}!')
#         elif n1 < n2:
#             print(f'{n2} é maior que {n1}!')
#         else:
#             print(f'Os números são iguais!')
#         try:
#             programa = int(input('Digite a opção: '))
#         except ValueError:
#             print('Opção invalida! digite novamente: ')
#     while programa == 4:
#         print('Digite novamente os números:')
#         while True:
#             try:
#                 n1 = float(input('Digite o 1º valor: '))
#                 break
#             except ValueError:
#                 print('Entrada invalida!')
#
#         while True:
#             try:
#                 n2 = float(input(f'Digite o 2º valor: '))
#                 break
#             except ValueError:
#                 print('Entrada invalida!')
#         try:
#             programa = int(input('Digite a opção: '))
#         except ValueError:
#             print('Opção invalida! digite novamente: ')
#
#     if programa == 5:
#         print()
#




# desafio 60
# que leia um número qualquer e mostre seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120
# from math import factorial

# numero = int(input(f'Digite um número: '))
# contagem = 1
# mult = numero
# print(f'O fatorial de {numero}:')
# while numero - contagem > 1 :
#
#     mult = mult * (numero - contagem)
#     print(numero - contagem , end=' X ')
#     contagem += 1
#
# if numero - contagem == 1 :
#     print('1 é igual à ', end='')
#
# print(f'{mult}')

# n = int(input('Digite um número: '))
# mult = n
# for c in range(n,1,-1):
#     print(c)
#     mult = mult * (c - 1)
# print(mult)



# desafio 61
# refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# a1 = int(input('Digite o primeiro termo da PA: '))
# razao = int(input(f'Digite a razão da PA: '))
# contador = 0
# print('='*30)
# print(f' Os 10 primeiros termos da PA são: ')
# while contador < 10:
#     print(f' {a1 + (contador * razao)};', end = '')
#     contador += 1



# a1 = int(input('Primeiro termo da PA: '))
# razao = int(input('Razão da PA: '))
# contador = 1
# termo = a1
# while contador <= 10:
#     print(f'{termo}; ', end='')
#     termo += razao
#     contador += 1



# desafio 62
# melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos.

# a1 = int(input('Primeiro termo da PA: '))
# razao = int(input('Razão da PA: '))
# termo = 10
# contador = 1
# enezimo_termo = a1
# while contador <= termo:
#     print(f'{enezimo_termo}; ', end='')
#     enezimo_termo += razao
#     contador += 1
#     while contador == termo:
#         print(f'{enezimo_termo}; ', end='')
#         enezimo_termo += razao
#         contador += 1
#         print()
#         print('Gostaria de mostrar mais termos da PA?')
#         termo += int(input('Digite quantos termos a mais: '))
#
# print(f'Progressão finalizada com {termo} termos.')



# desafio 63
# que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# print(f'vamos mostrar uma sequencia de Fibonacci')
# a1 = int(input('Digite o 1º número: '))
# a2 = int(input(f'Digite o 2º número: '))
# nezimo_elemento = int(input(f'Digite quantos elementos deseja adicionar: ')) - 2
# print(f'A sequencia iniciando com {a1} e {a2} Será:')
# print(f'{a1} ; {a2} ', end = ' ; ' )
# while nezimo_elemento > 0:
#     an = a1 + a2
#     a1 = a2
#     a2 = an
#     print(f'{an}', end = ' ; ' )
#     nezimo_elemento -= 1



# desafio 64
# que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999.
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag.

# a1 = int(input(f'Digite um número inteiro: '))
# contador = 0
# soma = 0
#
# while a1 != 999:
#
#     soma += a1
#     contador += 1
#     a1 = int(input(f'Digite um número inteiro: '))
# print(f'A soma dos {contador} termos é igual a {soma}!!!')



# desafio 65
# que leia varios numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valor lido.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

print(f'Vamos mostrar a media dos valores!')
contagem = 0
soma = 0
media = 0
maior = 0
menor = 0
continuar ='S'
while continuar in 'Ss':
    numero = float(input(f'Digite o numero: '))
    soma += numero
    contagem += 1
    if contagem == 1:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media = soma / contagem
print(f'A soma de {contagem} números é {soma}!!!')
print(f'A média entre eles é {media}!')
print(f'O maior número é {maior}!')
print(f'O menor número é {menor}!')

print()
print()
print('='*15,f'{VERMELHO} FIM {LIMPA}','='*20)