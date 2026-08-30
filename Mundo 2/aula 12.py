# Desafio 36
# o programa deve perguntar o valor da casa, o salário e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# 1% ao mes sem ser cumulativo:

# from cores import *
# valor = int(input(f'Digite o valor da casa em {BRANCO_UNDERLINE}reais{LIMPA}: '))
# salario = int(input(f'Digite o valor do salario em {BRANCO_UNDERLINE}reais{LIMPA}: '))
# periodo_ano = int(input(f'Digite em {BRANCO_UNDERLINE}quantos anos{LIMPA} pretende pagar: '))
# periodo_mes = periodo_ano * 12
# juros = valor * 0.005 * periodo_mes
# print(juros)
# prestacao = (valor + juros) / periodo_mes
#
# if prestacao > salario * 0.30:
#     print(f'O valor da prestação supera 30% do salario de {salario} reais, logo o empréstimo será negado!')
# else:
#     print(f'A prestação é {VERDE}{prestacao:.2f}{LIMPA} reais ({VERMELHO}{(100 * prestacao) / salario:.2f}{LIMPA} % do {BRANCO_BOLD}sálario){LIMPA}.')
#     print(f'O valor total de juros é {VERMELHO}{juros:.2f}{LIMPA}R%. E o juros mensal é {LILAS}{juros/periodo_mes:.2f}{LIMPA} R$.')
#     print(f'E deverá ser pago em {AZUL}{periodo_mes}{LIMPA} meses')



# Desafio 37
# leia um número inteiro e peça para o usuário escolher qual será a base de conversão
# # 1 para binario ; 2 para octal ; 3 hexadecimal

# numero = int(input(f'Digite um número inteiro: '))
# print('Digite "1" para binario')
# print('Digite "2" para octal')
# print('Digite "3" para hexadecimal')
# codigo = int(input(f'sua entrada: '))
# binario = bin(numero)
# octal = oct(numero)
# hexadecimal = hex(numero)
# while True:
#     if codigo == 1:
#         print(f'O Numero {numero} na base binaria é {bin(numero)[2:]}')
#         break
#     elif codigo == 2:
#         print(f'O Numero {numero} na base octal é {octal[2:]}')
#         break
#     elif codigo == 3:
#         print(f'O Numero {numero} na base hexadecimal é {hexadecimal[2:]}')
#         break
#     else:
#         print(f'Opção errada, digite novamente')
#         codigo = int(input(f'sua entrada: '))



# Desafio 38
# leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
#  - O primeiro valor é maior
#  - o segundo valor é maior
#  - não existe valor maior, os dois são iguais.

# from random import *
#
# from cores import *
# n1 = randint(1, 100)
# n2 = randint(1, 100)
#
# print('Comparando dois valores:')
# print(f'  "{AZUL}{n1}{LIMPA}" e "{AZUL}{n2}{LIMPA}".')
#
# # from time import sleep
# # sleep(1)
#
# if n1 > n2:
#     print(f'O {BRANCO_BOLD}Primeiro numero{LIMPA} "{LILAS}{n1}{LIMPA}" é maior que o segundo "{AMARELO}{n2}{LIMPA}"!')
# elif n1 < n2:
#     print(f'O {BRANCO_BOLD}Segundo numero{LIMPA} "{LILAS}{n2}{LIMPA}" é maior que o primeiro "{AMARELO}{n1}{LIMPA}"!')
# else:
#     print(f'Os {BRANCO_BOLD}Dois números{LIMPA} são {BRANCO_UNDERLINE}iguais{LIMPA}!')



# Desafio 39
# leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# Se já passou do tempo do alistamento
# o prog deve ainda mostrar o tempo que falta ou que passou do prazo.

# from datetime import date
# nome = str(input('Digite seu nome: '))
# sexo = str(input('Digite seu sexo (M/F): '))
# nasc = int(input('Digite o ano de seu nascimento: '))
# atual = date.today().year
# idade = atual - nasc
# if sexo == 'M':
#     if idade > 18:
#         print(f'Olá, {nome}!')
#         print(f'Você tem {idade} anos.')
#         print('Já passou do ano de se alistar!')
#     elif idade < 18:
#         print(f'Olá, {nome}!')
#         print(f'voce tem {idade} anos.')
#         print(f'Você ainda vai se alistar!')
#         print(f'Faltam {18 - idade} anos para se alistar!')
#         print(f'Você deverá se alistar em {nasc + 18} anos.')
#     else:
#         print(f'Olá, {nome}!')
#         print('Parabéns, você tem 18 anos!! Esta na hora de se alistar!')
# elif sexo == 'F':
#     print(f'Olá, {nome}!')
#     print('Você não precisa se alistar para o serviço militar obrigatório!')



# Desafio 40
# leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: reprovado;
# média entre 5.0 e 6.9: recuperação;
# média 7.0 ou superior: aprovado;

# from random import randint
# n1 = randint(0,10)
# n2 = randint(0,10)
#
# media = (n1 + n2) /2
#
# print(f'Primeira nota {n1}.')
# print(f'A segunda nota {n2}.')
# print(f'A sua média foi {media:.1f}.')
#
# if media >= 7:
#     print('Parabens, você foi Aprovado!')
# elif 7 > media >= 5:
#     print('Você está de recuperação!')
# else:
#     print('Você foi reprovado.')



# Desafio 41
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: Mirim
# até 14 anos: Infantil
# até 19 anos: Junior
# acima: master

# from datetime import date
# nome = str(input('Digite seu nome: '))
# sexo = str(input('Digite seu sexo (M/F): '))
# nasc = int(input('Digite o ano de seu nascimento: '))
# atual = date.today().year
# idade = atual - nasc
# print(f'Olá, {nome}, sua idade é {idade} anos!')
# if sexo == 'M':
#     if idade <= 9:
#         print(f'Você participará na categoria Mirim Masculino! ')
#     elif idade <= 14:
#         print(f'Você participará na categoria Infantil Masculino! ')
#     elif 14 < idade <= 19:
#         print('Você participará na categoria Junior Masculino! ')
#     elif idade > 19:
#         print('Você participará na categoria Master Masculino!')
#
# elif sexo == 'F':
#     if idade <= 9:
#         print(f'Você participará na categoria Mirim Feminino! ')
#     elif idade <= 14:
#         print(f'Você participará na categoria Infantil Feminino! ')
#     elif idade <= 19:
#         print(f'Você participará na categoria Junior Feminino! ')
#     elif idade > 19:
#         print(f'Você participará na categoria Master Feminino! ')



# Desafio 42
# triangulo equilátero
# triangulo isosceles
# triangulo escaleno

# from random import randint
# a = randint(1,100)
# b = randint(1,100)
# c = randint(1,100)
# a = 9
# b = 7
# c = 30
# lista = [a,b,c]
# ordem = sorted(lista)
# from cores import *
#
# if ((ordem[0])**2 + (ordem[1])**2) == (ordem[2])**2:
#     print(f'{ordem[0]**2} + {ordem[1]**2} == {ordem[2]**2}')
#     print(f' Os números {ordem[0]}, {ordem[1]} e {ordem[2]} forma um {LILAS}triangulo retângulo{LIMPA}!')
#
# elif ordem[0] == ordem[1] == ordem[2]:
#     print(f' Os números formam um {AZUL}triangulo equilátero{LIMPA} de lado "{a}".')
#
# elif ordem[0] + ordem[1] > ordem[2]:
#         if ordem[0] == ordem[1]:
#             print(f' Os números {ordem[0]}, {ordem[1]} e {ordem[2]} forma um {VERDE}triangulo isósceles{LIMPA}!')
#         else:
#               print(f' Os números {ordem[0]}, {ordem[1]} e {ordem[2]} formam um {AMARELO}triangulo escaleno{LIMPA}!')
#
# else:
#     print(f'Os números {ordem[0]}, {ordem[1]} e {ordem[2]} {VERMELHO_UNDERLINE}não{LIMPA} formam um triangulo!')



# Desafio 43
# leia peso e altura e calcule IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do Peso
# 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

# from cores import *
# from random import randrange
# peso = randrange(40,150)
# altura = randrange(140,220)

# peso = float(input('Qual o seu peso?  '))
# altura = float(input('Qual a sua altura (em cm)?  '))
# metros = altura /100
# imc = peso / (metros ** 2)
#
# print(f'Seu peso é {peso} Kg')
# print(f'Sua altura é {metros:.2f} metros')
# print(f'Seu IMC é igual a {imc:.1f}.')
# if imc < 18.5:
#     print(f'{AMARELO_BOLD}Abaixo do peso{LIMPA}!')
# elif imc < 25:
#     print(f'{BRANCO_BOLD}Peso normal{LIMPA}!')
# elif imc < 30:
#     print(f'{AMARELO_BOLD}Sobrepeso{LIMPA}!')
# elif imc < 40:
#     print(f'{LILAS_BOLD}Obesidade{LIMPA}!')
# else:
#     print(f'{VERMELHO_BOLD}Obesidade mórbida{LIMPA}!')



# Desafio 44
# leia o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#  a vista 10% de desconto
#  cartão 5%
#  até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros.

# preco = float(input('Digite o preço do produto: '))
#
# print("""Digite a forma de pagamento!
# [1] para a vista com 10% de desconto;
# [2] para cartão a vista com 5% de desconto;
# [3] para cartão até 2x sem juros;
# [4] para cartão em 3x ou mais com 20% de juros.""")
# pagamento = int(input('Digite: '))
# parcela = 0
# while True:
#         if pagamento == 1:
#             forma = 'a vista'
#             total = preco - (preco * 10 / 100)
#             break
#         elif pagamento == 2:
#             forma = 'a vista no cartão'
#             total = preco - (preco * 5 / 100)
#             break
#         elif pagamento == 3:
#             parcela = 2
#             forma = '2x sem juros no cartão'
#             total = preco
#             break
#         elif pagamento == 4:
#             parcela = int(input('Digite a quantidade de parcelas: '))
#             forma = '3x ou mais no cartão com 20% de juros'
#             total = preco + (preco * 20 / 100)
#             break
#         else:
#             print(f'Forma de pagamento invalida! digite [1]; [2]; [3] ou [4] para continuar!')
#             pagamento = int(input('Digite: '))
#
# print(f'O preço inicial do produto era {preco:.2f} R$.')
# print(f'''Com a forma de pagamento {forma}.
# O preço do produto será {total:.2f} R$. ''')
# if parcela != 0:
#     print(f'Em {parcela} parcelas de {total/parcela} R$.')

# Desafio 45
# crie um programa que faça o computador jogar Jokenpô
from random import choice
resultado = 'empate'
ganha = 'ganha de'
print('Desafie o computador em um jogo de pedra, papel e tesoura')
print(f'Famoso "Jokenpo!')
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
jogador = str(input('Escolha "pedra", "papel" ou "tesoura": '))
while True:
        if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
            break
        else:
            print('opção errada, tente novamente')
            jogador = str(input(f'Escolha "pedra", "papel" ou "tesoura": '))

# if jogador == computador:
#     resultado = 'empate'
# elif jogador == 'pedra':
#     if computador == 'papel':
#         resultado = 'Você perdeu, pedra perde para papel!'
#     elif computador == 'tesoura':
#         resultado = 'Você ganhou, pedra ganha de tesoura!'
# elif jogador == 'papel':
#     if computador == 'pedra':
#         resultado = 'Você ganhou, papel ganha de pedra!'
#     elif computador == 'tesoura':
#         resultado = 'Você perdeu, papel perde para pedra!'
# elif jogador == 'tesoura':
#     if computador == 'pedra':
#         resultado = 'Você perdeu, tesoura perde para pedra!'
#     elif computador == 'papel':
#         resultado = 'Você ganhou, tesoura ganha de papel!'

if jogador == computador:
    resultado = 'Empate'
    ganha = 'empata com'
elif jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    resultado = 'Você ganhou!'
    ganha = 'ganha de'
else:
    resultado = 'Você perdeu'
    ganha = 'perde de'

from time import sleep
print('JO...',end='')
sleep(0.5)
print('KEN...',end='')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print(f'''Você jogou {jogador}; 
O computador jogou {computador};
{resultado}! {jogador} {ganha} {computador}!!''')