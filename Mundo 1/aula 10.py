# nome = str(input('Qual seu nome? '))
# nome_lower = nome.lower()
# primeiro_nome = nome_lower.split()
# if primeiro_nome[0] == 'joao':
#     print('Que nome bonito!')
# else:
#     print('Que nome mais mediano!')
# print(f'Bom dia, {primeiro_nome[0]}')
# from datetime import date

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# media = (nota1 + nota2) / 2
# print(f'A sua media foi {media:.1f}')
# if media >= 7:
#     print('Parabens você foi aprovado com louvor')
# if 5 <= media <= 6.9:
#     print('Você foi aprovado, mas deve estudar mais')
# if media < 5:
#     print('Você foi reprovado')




# desafio 28
#escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#o programa devera escrever na tela se o usuário venceu ou perdeu.

# import random
# print('Maquina de sorteio. acerte o número premiado e ganhe!')
# numero_sorteado = random.randint(0,5)
# sair = 0
# tentativas = 0
# while True:
#     if sair == 'x':
#         break
#     print('DEBUG o numero sorteado é :',numero_sorteado)
#     tentativas = tentativas +1
#     print('Numero de tentativas:',tentativas)
#
#     while True:
#         try:
#             numero = int(input('1 Escolha um numero inteiro entre 0 e 5: '))
#             if 0 <= numero <= 5:
#                 break
#             else:
#                 print('2 numero fora do intervalo de 0 e 5')
#         except ValueError:
#             print('3 Entrada invalida, digite um numero inteiro entre 0 e 5')
#
#     if numero == numero_sorteado:
#         print('Parabens, você acertou o numero da sorte!')
#         sair = input('4 Gostaria de reiniciar? aperte ENTER, x para sair ')
#         numero_sorteado = random.randint(0,5)
#
#     else:
#         print('Que pena, você não acertou, gostaria de tentar novamente?')
#         sair = input('5 Pressione ENTER para tentar novamente, x para sair ')






# desafio 29
# escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar r$ 7,00 por cada km acima do limite.

# from random import randint
#  #velocidade = int(input('Qual a velocidade do carro? ')) # entrada manual de velocidade
# velocidade = randint(10,200)  # entrada automática de velocidade
# print(f'A velocidade que o carro passou no radar foi de: {velocidade} Km/h')
# if velocidade > 80:
#     multa = (velocidade - 80) * 7
#     print('Excesso de velocidade!')
#     print(f'Voce foi multado em R$ {multa:.2f}')





# desafio 30
# crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

# from random import randint
# num = randint(1,1000)

# while True:
#     try:
#         num = int(input('Digite um número inteiro: '))
#         break
#     except ValueError:
#         print('Por favor digite um número inteiro: ')
#
# if num % 2 == 0:
#     print(f'O número {num} é par')
# else:
#     print(f'O número {num} é impar')





# desafio 31
# desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem
# cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

# from random import randint
# dist = randint(1,500)
# print(f'A distancia da viagem é {dist} Km')
#
# if dist <= 200:
#     print(f'O custo da passagem é igual a R${dist*0.5:.2f}.')
# else:
#     print(f'O custo da passagem é igual a R${dist*0.45:.2f}.')





# desafio 32
# faça um program que leia um ano qualquer e mostre se ele é bissexto.

# from random import randint
# ano = randint(1000, 3000)
# from datetime import date

# ano = int(input("Digite o ano (digite 0 para usar o ano atual): "))
# if ano == 0:
#     ano = date.today().year
#
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f'O ano de {ano} é bissexto!')
# else:
#     print(f'O ano {ano} não é bissexto!')





# desafio 33
# faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# from random import randint
#
# a1 = randint(0,100)
# a2 = randint(0,100)
# a3 = randint(0,100)
#
# lista = [a1,a2,a3]
# ordem = sorted(lista)
#
# print(f'Os numeros são: {a1},{a2},{a3}.')
# print(f' O menor número é {ordem[0]} e o maior é {ordem[-1]}.')
# print(f' O menor número é {min(lista)} e o maior é {max(lista)}.')




# desafio 34
# que pergunte o salário de um funcionário e calcule o valor do seu aumento
# para salários superiores a 1250,00 calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%

# import random
#
# salario = random.randrange(500,2000)
# print(f'O salario é R${salario:.2f}')
# if salario > 1250:
#     print(f'O salario de R${salario:.2f} aumentado de 10% é igual a R${salario * 1.1:.2f}')
# else:
#     print(f'O salario de R${salario:.2f} aumentado de 15% é igual a R${salario * 1.15:.2f}')




# desafio 35
# desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triangulo.
# from random import randint
# a = randint(1,100)
# b = randint(1,100)
# c = randint(1,100)
# # a = 3
# # b = 4
# # c = 10
# lista = [a,b,c]
# ordem = sorted(lista)
#
# if ((ordem[0])**2 + (ordem[1])**2) == (ordem[2])**2:
#     print(f'{ordem[0]**2} + {ordem[1]**2} == {ordem[2]**2}')
#     print(f' Os números {a}, {b} e {c} forma um triangulo retângulo')
#
# elif ordem[0] + ordem[1] > ordem[2]:
#     print(f' Os números {a}, {b} e {c} formam um triangulo')
#
# else:
#     print(f'Os numeros {a}, {b} e {c} não formam um triangulo')


from random import randint
lista = [randint(0,100),randint(0,100),randint(0,100)]
ordem = sorted(lista)
a, b, c = ordem
print(a,b,c)
if a + b <= c:
    print(f'Os lados {a} e {b} e {c} não formam um triangulo')
elif a == b == c:
    print(f' Os lados de {a} formam um triangulo equilátero')
elif a**2 + b**2 == c**2:
    print(f' Os catetos {a} e {b} mais a hipotenusa {c} formam um triangulo retângulo')
else:
    print(f'Os lados {a} e {b} e {c} foram um triangulo qualquer')