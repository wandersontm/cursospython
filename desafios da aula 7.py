#desafio 005:

# while True:
#     try:
#        n1 = int(input('Digite um valor: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'o número escolhido foi',n1)
# print(f'o número anterior a {n1} é: {n1 - 1} e o número posterior a {n1} é: {n1 + 1}')

#desafio 006:

# while True:
#     try:
#        n1 = int(input('Digite um valor: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'o número escolhido foi',n1)
# print(f'o seu dobro é {n1*2}, o seu tripo é {n1*3}, é sua raiz quadrada é {n1**(1/2)}')

#desafio 007:
#
# print('Vamos calcular a média de nossos alunos?')
# while True:
#     try:
#        n1 = float(input('Digite a nota da primeira prova: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# while True:
#     try:
#        n2 = float(input('Digite a nota da segunda prova: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'As notas foram: {n1} da primeira prova e {n2} da segunda prova'
#       f'\n A média do aluno foi: {(n1 + n2)/2}')
#
#desafio 008

# print('vamos converter um valor em metros para centímetros e milímetros')
# while True:
#     try:
#        n1 = int(input('Digite um valor em metros: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'o valor em centimetres é {n1*100};\nE o valor em milímetros é {n1*1000}.')

#desafio 009:
#
# print('vamos escrever a tabuada?')
# while True:
#     try:
#        n1 = int(input('Digite um número: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'A tabuada do número {n1} é: \n{n1} x1 é {n1*1};\n{n1} x2 é {n1*2}; '
#       f'\n{n1} x3 é {n1*3};\n{n1} x4 é {n1*4};\n{n1} x5 é {n1*5};\n{n1} x6 é {n1*6};\n{n1} x7 é {n1*7}; '
#       f'\n{n1} x8 é {n1*8};\n{n1} x9 é {n1*9};\n{n1} x10 é {n1*10}')

#desafio 010:
#
# print('Conversão de Real para Dólar: planeje sua viagem!!')
# #print('A cotação atual (fictícia) é U$ 1,00 = R$ 3,27')
# print('A cotação atual é U$ 1,00 = R$ 5,27')
# while True:
#     try:
#        n1 = float(input('Digite a quantidade de reais que voce possuí: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um numero!')
# cotacao = n1/5.27
# reais = int(cotacao)
# centavos = int((cotacao - reais)* 100)
# print(f'Com a quantidade de Reais disponíveis, você terá {reais} Dólares e {centavos} Cents.')

#desafio 011:
#
# print('Calculadora de quantidade de litros de tinta')
# while True:
#     try:
#         n1 = float(input('Digite a largura da parede: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# while True:
#     try:
#         n2 = float(input('Digite a altura da parede: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# print(f'A quantidade de litros necessário para pintar uma parede de {n1} por {n2} '
#       f'é igual a: {((n1*n2)/2)} litros de tinta')

#desafio 012:
#
# print('calcule o desconto de 5% sobre a mercadoria')
# while True:
#     try:
#         n1 = float(input('digite o valor da mercadoria: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# cotacao = n1*0.95
# reais = int(cotacao)
# centavos = int((cotacao - reais)* 100)
#
# print(f'O valor da mercadoria com 5% de desconto é igual a {reais} reais e {centavos} centavos')

#desafio 013


print('aumentando o salario do funcionario em 15%')
while True:
    try:
        n1 = float(input('digite o valor inicial do salario: '))
        break
    except ValueError:
        print('Por favor, digite um numero!')

cotacao = (n1*115)/100
reais = int(cotacao)
centavos = int((cotacao - reais)* 100)

print(f'O novo salario do funcionario é igual a {reais} reais e {centavos} centavos')
