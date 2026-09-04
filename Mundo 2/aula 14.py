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
#     player = int(input('Entrada errada! Por favor digite um numero entre 0 e 10!!!'))
# while computador != player:
#     print()
#     print(f'{VERMELHO}Que pena{LIMPA}!! você não acertou!')
#     contador += 1
#     print(f'Voce ja tentou {contador} vezes')
#     if computador > player:
#         print(f'{VERDE}DICA!!!{LIMPA} Fale um numero {BRANCO_UNDERLINE}maior{LIMPA}!!')
#     elif computador < player:
#         print(f'{VERDE}DICA!!!{LIMPA} Fale um numero {BRANCO_UNDERLINE}menor{LIMPA}!!')
#     player = int(input(f'{AZUL}tente novamente{LIMPA} entre 0 e 10: '))
#     while player not in range(0, 11):
#         player = int(input('Entrada errada! Por favor digite um numero entre 0 e 10!!!'))
# print(f'{AMARELO_BOLD}Parabens voce acertou!{LIMPA} voce precisou de {VERMELHO}{contador} vezes{LIMPA} para conseguir!!!')



# desafio 59
# que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#deverá realizar a operação solicitada em cada caso.



# desafio 60
# que leia um número qualquer e mostre seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120



# desafio 61
# refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.



# desafio 62
# melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos.



# desafio 63
# que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# ex: 0 - 1 - 1 - 2 - 3 - 5 - 8



# desafio 64
# que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999.
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag.



# desafio 65
# que leia varios numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valor lido.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
