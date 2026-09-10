#aula de tuplas.
# Tuplas são imutaveis!!!!

# lanche = ('hambúrguer','suco','pizza','pudim')
#print(lanche[-1]) # 'pudim"
# print(lanche[1])  # suco
# print(lanche[1:3]) # ('suco','pizza')
# print(lanche[2:]) #('pizza', 'pudim')
# print(lanche[:2]) #('hambúrguer', 'suco')
# print(lanche[-2:]) #('pizza', 'pudim')
# print(lanche[-2]) # pizza

#lanche[1] = 'refrigerante'  # Tuples don't support item assignment
# print(len(lanche))  #retorna a quantidade de elementos na tupla.
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
#Eu vou comer hambúrguer
#Eu vou comer suco
#Eu vou comer pizza
#Eu vou comer pudim

# for cont in range(0, len(lanche)):
#     print(cont) # retona valores numéricos : 1, 2, 3, 4 etc ate o range.
#     print(lanche[cont]) #retorna os elementos guardados em cada posição da tupla
#0
#hambúrguer

#1
#suco

#2
#pizza

#3
#pudim

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na {pos}')
# Eu vou comer hambúrguer na 0
# Eu vou comer suco na 1
# Eu vou comer pizza na 2
# Eu vou comer pudim na 3

# print(sorted(lanche))  # retorna a lista em ordem: ['hambúrguer', 'pizza', 'pudim', 'suco']
# print(lanche) # retorna a tupla : ('hambúrguer', 'suco', 'pizza', 'pudim')

# a = (2,5,4)
# b = (5,8,1,2)
# c = a + b
# d = b + a
# # print(c) #(2, 5, 4, 5, 8, 1, 2)
# # print(d) #(5, 8, 1, 2, 2, 5, 4)
# # print(len(c)) # 7
# # print(c.count(5)) # 2
# # print(d.index(8)) # 1
# print(d.index(5,1)) #5

# pessoa = ('Gustavo', 39 , 'M', 99.88)
# print(pessoa) # ('Gustavo', 39, 'M', 99.88)
# del pessoa
# print(pessoa) # ao deletar a variável, o erro ocorrerá  NameError: name 'pessoa' is not defined
# del(pessoa[0]) # TypeError: 'tuple' object doesn't support item deletion



# desafio 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.



# desafio 73
# uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
# depois mostre: ( corinthians palmeiras santos grêmio cruzeiro flamengo vasco chapecoense atletico )
#  Apenas os 5 primeiros colocados
# Os ultimos 4 colocados
# uma lista com os times em ordem alfabética
# em que posição na tabela está o time da chapecoense



# desafio 74
# crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla
# depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior
# valor que estão na tupla.



# desafio 75
# desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla. no final mostre:
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3.
# quais foram os números pares.



# desafio 76
# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
# no final, mostre uma listagem de preços, organizando os dados em forma tabular.



# desafio 77
# crie um programa que tenha uma tupla com várias palavras.
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.