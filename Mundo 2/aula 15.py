# n = s = 0
# while True:
#     n = int(input('digite um numero: '))
#     if n == 999:
#         break
#     s += n
#print(f'A soma vale {s}.')


from cores import *
print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*15 )



#desafio 66
# que leia vários números inteiros. Pare quando 999 for digitado.
# quantos foram digitados e a soma entre eles.

# print(f'Somatório de numero!')
# print(f'Digite 999 para parar')
# numero = 0
# contador = 0
# soma = 0
# while True:
#     numero = int(input(f'Digite o número: '))
#     if numero == 999:
#         break
#     soma += numero
#     contador += 1
#
# print()
# print(f'{VERMELHO}-={LIMPA}' *20)
# print()
# print(f'foram digitados {contador} números')
# print(f' A soma entre eles é {soma}')


# desafio 67
# mostre a tabuada de um número.
# Pare quando um número negativo for inserido

# print('Calculadora')
# contador = 1
# while True:
#     print(f'{AMARELO}-={LIMPA}' * 20)
#     numero = int(input(f'Digite o numero: '))
#     if contador > 10:
#         contador = 1
#     if numero < 0:
#         break
#     while contador <= 10:
#         print(f' {numero} x {contador} = {numero * contador}')
#         contador += 1



# desafio 68
# jogue par ou impar com o computador.
# Interromper quando o jogador perder
# mostrando os valores do jogo atual, e o resultado
# mostrando o total de vitórias.

# from random import randint
# contador = 0
# print('Tente ganhar do computador em um jogo de par ou impar')
# while True:
#     jogador = int(input(f'Escolha um numero: '))
#     escolha = ' '
#     while escolha != 'par' and escolha != 'impar':
#         escolha = str(input('Par ou impar: ')).strip().lower()
#     computador = randint(0,10)
#     print(f'{AMARELO}-={LIMPA}' * 20)
#     if (computador + jogador) % 2 == 0 and escolha == 'par' or (computador + jogador) % 2 == 1 and escolha == 'impar':
#         contador += 1
#         print(f'Você ganhou!!')
#         print(f'voce escolheu {escolha} e a soma deu {computador + jogador}', end = '')
#         print(' (PAR)' if (computador + jogador) % 2 == 0 else ' (IMPAR)')
#     elif (computador + jogador) % 2 == 0 and escolha == 'impar' or (computador + jogador) % 2 == 1 and escolha == 'par':
#         print(f'Você perdeu!!')
#         print(f'voce escolheu {escolha} e a soma deu {computador + jogador}', end = '')
#         print(' (PAR)' if (computador + jogador) % 2 == 0 else ' (IMPAR)')
#         break
#     print(f'{AMARELO}-={LIMPA}' * 20)
# print(f'voce ganhou {contador} vezes seguidas!!!')



# desafio 69
# leia idade e sexo de várias pessoas.
# a cada entrada perguntar se quer parar ou continuar
# no final mostrar quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

count_masc = 0
count_idade = 0
count_fem = 0
sexo = ' '
pergunta = ' '
while True:
    idade = int(input('Digite uma idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print(f'{AMARELO}-={LIMPA}' * 20)
    if sexo == 'M':
        count_masc += 1
    if sexo == 'F' and idade < 20:
        count_fem += 1
    if idade >= 18:
        count_idade += 1
    if pergunta == 'N':
        break
print(f'''no total foram {count_idade} pessoas com mais de 18 anos;
No total foram {count_masc} homens cadastrados;
No total temos {count_fem} mulheres com menos de 20 anos;
''')



# desafio 70
# leia o nome e preço de vários produtos
# perguntar ao usuário se vai continuar
# no final mostar o total gasto
# quantos produtos custaram mais de 1000
#qual o nome do produto mais barato



# desafio 71
# simule um caixa eletrônico
# no início perguntar qual o valor a ser sacado
# e informar quantas células de cada valor serão entregues
# usar as notas de 1, 10, 20 e 50.



print()
print('='*15,f'{VERMELHO} FIM {LIMPA}','='*20)