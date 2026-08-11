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

# print('vamos escrever a tabuada?')
# while True:
#     try:
#        n1 = int(input('Digite um número: '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um número!')
#
# print(f'A tabuada do número {n1} é:')
# print(f'{n1} x 1 é {n1*1:2};')
# print(f'{n1} x 2 é {n1*2:2};')
# print(f'{n1} x 3 é {n1*3:2};')
# print(f'{n1} x 4 é {n1*4:2};')
# print(f'{n1} x 5 é {n1*5:2};')
# print(f'{n1} x 6 é {n1*6:2};')
# print(f'{n1} x 7 é {n1*7:2};')
# print(f'{n1} x 8 é {n1*8:2};')
# print(f'{n1} x 9 é {n1*9:2};')
# print(f'{n1} x10 é {n1*10}.')

#desafio 010:
#
# print('Conversão de Real para Dólar: planeje sua viagem!!')
# #print('A cotação atual (fictícia) é U$ 1,00 = R$ 3,27')
# print('A cotação atual é    D$ 1,00 = R$ 5,27')
# print('A cotação atual é    U$ 1,00 = R$ 5,92')
# print('A cotação atual é ien$ 31,00 = R$ 1,00')
# while True:
#     try:
#        n1 = float(input('Digite a quantidade de reais que voce possuí: R$ '))
#        break
#
#     except ValueError:
#         print('Por favor, digite um numero!')
# cotacao = n1/5.27
# reais = int(cotacao)
# centavos = int((cotacao - reais)* 100)
# print(f'Com a quantidade de Reais disponíveis, você terá {reais} Dólares e {centavos} Cents.')
# print(f'Com a quantidade de Reais disponíveis, você terá {n1/5.92:.2f} Euros.')
# print(f'Com a quantidade de Reais disponíveis, você terá {n1/0.032:.2f} Ienes.')

#desafio 011:

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
# print(f'Uma parede de {n1} metros por {n2} metros')
# print(f'Com uma aréa de parede é igual a {n1 * n2} metros quadrados')
# print(f'Precisa de {((n1*n2)/2)} litros de tinta')

#desafio 012:

# while True:
#     try:
#         n1 = float(input('digite o valor da mercadoria: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# while True:
#     try:
#         n2 = float(input('digite o valor do desconto em porcentagem: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# print(f'calculo do desconto de {n2:.0f}% sobre a mercadoria')
#
# cotacao = n1*((100-n2)/100)
# reais = int(cotacao)
# centavos = int((cotacao - reais)* 100)
#
# print(f'O valor da mercadoria com {n2:.0f}% de desconto é igual a {reais} reais e {centavos} centavos')

#desafio 013

# while True:
#     try:
#         n1 = float(input('digite o valor inicial do salario: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# while True:
#     try:
#         n2 = float(input('digite o valor do aumento em porcentagem: '))
#         break
#     except ValueError:
#         print('Por favor, digite um numero!')
#
# if n2.is_integer():
#     print(f'aumentando o salario do funcionario em {n2}%')
# else:
#     print(f'aumentando o salario do funcionario em {n2:.2f}%')
# cotacao = (n1*(n2 + 100))/100
# reais = int(cotacao)
# centavos = round((cotacao - reais)* 100)
#
# print(f'O novo salario do funcionario é igual a {reais} reais e {centavos} centavos')

# desafio 14
# while True:
#   try:
#       n1 = float(input('digite uma temperatura : '))
#       break
#   except ValueError:
#       print('por favor, digite um número!')
# print(f'A temperatura de {n1}ºC corresponde a {n1*1.8+32:.2f}ºF')
#
# desafio 15

print('Calculadora de gasto com carro alugado')

while True:
    try:
        diaria = float(input('digite o valor da diaria cobrado: '))
        break
    except ValueError:
        print('Por favor, digite um número!')

while True:
    try:
        valor_km = float(input('digite o valor do km rodado cobrado (em centavos): '))
        break
    except ValueError:
        print('Por favor, digite um número!')

while True:
    try:
        n1 = int(input('digite a quantidade de dias o carro foi alugado: '))
        break
    except ValueError:
        print('Por favor, digite um número!')

while True:
    try:
        n2 = float(input('digite a quantidade de quilômetros rodados: '))
        break
    except ValueError:
        print('Por favor, digite um número!')

while True:
    try:
        preco_combustivel = float(input('digite o preço pago no litro de combustivel: '))
        break
    except ValueError:
        print('Por favor, digite um número!')

total_gasto = (n1*diaria) + (n2*valor_km/100)
reais = int(total_gasto)
centavos = round((total_gasto - reais)*100)

if centavos >= 100:
    reais += 1
    centavos -= 100

if centavos > 0:
    print(f'O total gasto nessa viagem com o aluguel do carro foi igual a {reais} reais e {centavos} centavos')
else:
    print(f'O total gasto nessa viagem com o aluguel do carro foi igual a {reais} reais')

total_combustivel = n2/11*preco_combustivel
custo_em_real = int(total_combustivel)
custo_em_centavos = round((total_combustivel - custo_em_real)*100)

if custo_em_centavos >= 100:
    custo_em_real+=1
    custo_em_centavos -= 100

if custo_em_centavos > 0:
    print(f'O consumo de combustivel do veiculo foi de {custo_em_real} reais e {custo_em_centavos} centavos')
else:
    print(f'O consumo de combustivel do veiculo foi de {custo_em_real} reais')

real_final = reais + custo_em_real
centavos_final = custo_em_centavos + centavos

if centavos_final >= 100:
    real_final += 1
    centavos_final -= 100

if centavos_final > 0:
    print(f'O valor total gasto com o carro durante a viagem foi de {real_final} reais e {centavos_final} centavos ')
else:
    print(
        f'O valor total gasto com o carro durante a viagem foi de {real_final} reais')