# Laços (LOOPS)
#c = 0 #contador
# for c in range(0, 10, 1): (1) que é passo,
# informa o modo do contador 1 por 1, 2 por 2 etc ou ate um valor negativo para contagem regressiva
#     print(c)

# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

# s = 0
# for c in range(0, 4):
#     n = int(input('Digite um valor: '))
#     s += n
# print(f'O somatório de todos os valores é igual a {s}')



# desafio 46
# faça um programa ( la ele ) que mostre na tela uma contagem regressiva para o estouro de fogos
# de artifício indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# from cores import *
# from time import sleep
# for c in range(10, -1, -1):
#     print(f'{c}...')
#     sleep(1)
# print(f'{VERMELHO_BOLD}BOOM!!!!{LIMPA}')
# print('Feliz Ano Novo!!')
# sleep(1)
# print(f'{VERMELHO_BOLD}BOOM!!!!{LIMPA}')
# print('"fogos estourando..."')



# desafio 47
# faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# for c in range(1,51):
#     if c == 50:
#         print(f'{c}!',end='')
#     elif c%2==0:
#         print(c, '-',end=' ')

# for c in range(2,51,2):
#     print(c, end=' ')
# print('ACABOU!!!')



# desafio 48
# faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que
# se encontram no intervalo de 1 até 500.

# soma = 0
# repeticao = 0
# for c in range(1, 501, 2):
#
#     if c % 3 == 0:
#         soma += c
#         repeticao += 1
#
# print(f'A soma dos {repeticao} valores é {soma}')



# desafio 49
# refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, so que agora utilizando
# um laço for.

# numero = int(input(f'Digite um número para mostrar sua tabuada: '))
# for c in range(1,11):
#     if c < 10:
#         print(f'{numero} x {c} = {numero*c};')
#     else:
#         print(f'{numero} x {c} = {numero*c}.')



# desafio 50
# programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, desconsidere-o.

# soma = 0
# cont = 0
# for c in range(1,7):
#     n = int(input(f'Digite o {c}º número: '))
#     if n % 2 == 0:
#         soma += n
#         cont += 1
# if cont == 0:
#     print(f'Você não informou nenhum número par, logo a soma dos pares é igual a zero!!!')
# elif cont == 1:
#     print(f'Você digitou {cont} número par e a soma é igual a {soma}!!!!')
# else:
#     print(f'Você digitou {cont} números pares e a soma é igual a {soma}!!!!')



# desafio 51
# programa que leia o primeiro termo e a razão de uma PA. no final,
# mostre os 10 primeiros termos dessa progressão.

# p1 = int(input('Digite o primeiro termo da PA: '))
# razao = int(input(f'Digite a razão da PA: '))
# decimo = p1 + 10 * razao
# # for c in range(0,10):
# #     if c == 9:
# #         print(f'{p1 + razao * c}.')
# #     else:
# #         print(f'{p1 + razao * c} ->', end =' ')
#
# for c in range(p1, decimo, razao):
#     print(c, end=' ')



# desafio 52
# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# from cores import *
#
# n = int(input('Digite um número: '))
# con = 0
#
# for c in range(1,n+1):
#     if n % c == 0:
#         con += 1
#         print(f'{VERMELHO}{c}{LIMPA}',end=' ')
#
#     elif n % c != 0:
#         print(f'{c}',end=' ')
# print()
# print(f'O número {n} foi divisível {con} vezes!!!')
# if con != 2:
#     print(f'O número não é primo!!!')
# elif con == 2:
#     print(f'O número é primo!!!')



# desafio 53
# que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# print('Vamos descobrir se uma frase é um palindrome')
# # frase = str(input(f'Digite uma frase: '))
# frase = ' Ola alo'
# texto = frase
# print(f'A frase : "{frase}".')
# frase = frase.lower()
# frase = ''.join(frase.split())
# n_letras = len(frase)
# palindrome = True
# for c in range(0, n_letras):
#     if c < n_letras // 2:
#         ultima = frase[n_letras - c - 1]
#         letra = frase[c]
#         # print(frase[c], end = ' ') #debugs
#         # print(ultima, end = ' ') #debugs
#         if letra != ultima:
#             palindrome = False
#             # print(palindrome) #debugs
#         # elif letra == ultima:
#             # print(True) #debugs
#
# if palindrome:
#     print(f'A frase "{texto}" é um Palindrome!!!')
#
# if not palindrome:
#     print(f'A frase "{texto}" não é um palindrome!!!')



# desafio 54
# que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

# from datetime import date
# nascimento = 0
# maior = 0
# menor = 0
# date = date.today().year
# for c in range(0, 6):
#     nascimento += int(input(f'Digite {c+1}ª data de nascimento: '))
#     if date - nascimento >= 18 :
#         maior += 1
#     elif date - nascimento < 18 :
#         menor += 1
#
# print(date - nascimento)
# print(f'Maior de idade: {maior}!!')
# print(f'Menor de idade: {menor}!!')



# desafio 55
# que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

# atual = 0
# maior = 0
# menor = 0
# for c in range(1, 6):
#     atual = int(input(f'Digite o {c}º peso: '))
#     if c == 1:
#         maior = atual
#         menor = atual
#     elif atual >= maior:
#         maior = atual
#     elif atual <= menor:
#         menor = atual
# print(f'O maior peso foi de {maior}Kg')
# print(f'O menor peso foi de {menor}Kg')



# desafio 56
# que leia o nome, idade e sexo de 4 pessoas. No final mostre:
# a média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

# nome = 0
# idade = 0
# homem_velho = ''
# maior = 0
# dimenor = 0
# sexo = ''
# media = 0
# contador = 0
# listamulher = []
# listahomem = []
# for c in range(1, 5):
#     nome = str(input(f'Digite o nome da {c}º pessoa: '))
#     idade =int(input(f'Digite a idade da {c}º pessoa: '))
#     sexo = str(input(f'Digite o sexo (f/m): '))
#     media += idade
#     contador += 1
#
#     if sexo in 'Ff':
#         listamulher += [nome]
#         if idade < 20:
#             dimenor += 1
#
#     elif sexo == 'm':
#         listahomem += [nome]
#         if idade > maior:
#             homem_velho = nome
#             maior = idade
#
# print(listamulher)
# print(listahomem)
# print(f'''O nome do homem mais velho é {homem_velho} com {maior} anos.
# a média da idade do grupo é {media / contador:.0f} anos.''')
#
# if dimenor > 1:
#     print(f'a quantidade de mulheres com menos de 20 anos é {dimenor}.')
# elif dimenor == 1:
#     print(f' temos uma mulher com menos de 20 anos.')
# elif dimenor == 0:
#     print(f' Não temos mulheres com menos de 20 anos.')
