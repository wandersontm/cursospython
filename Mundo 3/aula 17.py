from cores import *
print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*16 )
print()

# lista_num = [2, 5, 9, 1] # cria lista
# lista_num[2] = 3 # substitui o elemento em [2], no caso o número '9' por 3.
# lista_num[4] = 7 # retorna erro, pois não é possível adicionar elementos dessa forma
# lista_num.append(7) # adiciona o número 7 como ultimo elemento da lista
# lista_num.sort()  # coloca os elementos em ordem crescente
# lista_num.sort(reverse=True) # coloca os elementos em ordem decrescente
#len(lista_num) # retorna quantos elementos existem na lista
#lista_num.insert(2, 0) # na posição 2 inseri o valor '0'.
#lista_num.pop() # elimina o ultimo elemento
#lista_num.pop(2) # elimina o elemento na posição 2.
#lista_num.insert(2, 2)
#lista_num.remove(2) # remove a primeira ocorrência do valor '2'. Se valor não existe na lista, retorna erro.
#if 4 in lista_num
#    num.remove(4) # checa se o valor existe na lista antes de remover. Corrigindo o erro de não existe na lista.
# print(lista_num)

# valores = list()
# for cont in range(0,5):
#     valores.append(int(input(f'Digite um valor: ')))
#
# for v in valores: # printa os valores conforme a formatação no print
#      print(f'{v}...', end='')
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')

# a = [2,3,8,7]
# b = a # faz com que as listas sejam atualizadas juntas, mexeu b mexeu a.
# b = a[:] # forma de b receber os elementos de a sem criar vinculo entre as listas.
# b[2] = 8
# print(a)
# print(b)


# Desafio 78
# faça um programa que leia 5 valores numéricos e guarde os em uma lista.
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

# lista = []
# menor = 0
# maior = 0
#
# for posicao in range(0, 5):
#     lista.append(int(input(f'Digite o valor na posição {posicao}: ')))
#     if posicao == 0:
#         maior = menor = lista[posicao]
#     else:
#         if lista[posicao] > maior:
#             maior = lista[posicao]
#         if lista[posicao] < menor:
#             menor = lista[posicao]
# print()
# print(f'Você digitou os valores {lista}')
# print()
#
# print(f'O maior valor digitado foi: {maior}, na posição', end= ':')
#
# for indice, valor in enumerate(lista):
#     if valor == maior:
#         print(f' {indice},', end ='')
#
# print(f'\nO menor valor digitado foi: {menor}, na posição', end= ':')
#
# for indice, valor in enumerate(lista):
#     if valor == menor:
#         print(f' {indice},', end ='')
#


# desafio 79
# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# lista = []
# while True:
#     entrada = input('Digite um valor ou "n" para sair : ')
#     if entrada.lower() == 'n':
#         break
#     try:
#         entrada = int(entrada)
#
#         if entrada == int(entrada):
#             if entrada not in lista:
#                 lista.append(entrada)
#                 print(f'Valor {VERDE}adicionado{LIMPA}.')
#             else:
#                 print(f'Valor {AMARELO}duplicado{LIMPA}.')
#     except ValueError:
#         print(f'Valor {VERMELHO}invalido{LIMPA}.')
#
# lista.sort()
# print(lista)



# desafio 80
# crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# no final, mostre a lista ordenada na tela.

# lista = []
# menor = 0
# maior = 0
# segundo = 0
# quarto = 0
# terceiro = 0
# for c in range(0,5):
#     while True:
#         entrada = input(f'Digite o {c + 1}º valor: ')
#         try:
#             entrada = int(entrada)
#             if entrada == int(entrada):
#                 if entrada not in lista:
#                     if c == 0:
#                         maior = menor = segundo = quarto = terceiro = entrada
#                         lista.append(entrada)
#                         print(f'Valor {VERDE}adicionado{LIMPA}!')
#                         break
#                     elif c == 1:
#                         if entrada < lista[0]:
#                             lista.insert(0, entrada)
#                             menor = entrada
#                         if entrada > lista[0]:
#                             lista.insert(1, entrada)
#                             maior = entrada
#                         segundo = maior
#                         print(f'Valor {VERDE}adicionado{LIMPA}!')
#                         break
#
#                     elif c == 2:
#                         if entrada > maior:
#                             lista.insert(2, entrada)
#                             maior = entrada
#                         elif entrada < menor:
#                             lista.insert(0, entrada)
#                             menor = entrada
#                         elif menor < entrada < maior:
#                             lista.insert(1, entrada)
#                             segundo = entrada
#                         terceiro = maior
#                         print(f'Valor {VERDE}adicionado{LIMPA}!')
#                         break
#
#                     elif c == 3:
#                         if entrada > maior:
#                             lista.insert(3, entrada)
#                             maior = entrada
#                         elif entrada < menor:
#                             lista.insert(0, entrada)
#                             menor = entrada
#                         elif entrada < segundo:
#                             lista.insert(1, entrada)
#                             segundo = entrada
#                         elif entrada > segundo:
#                             lista.insert(2, entrada)
#                             terceiro = entrada
#                         quarto = maior
#                         print(f'Valor {VERDE}adicionado{LIMPA}!')
#                         break
#                     elif c == 4:
#                         if entrada > maior:
#                             lista.insert(4, entrada)
#                             maior = entrada
#                         elif entrada < menor:
#                             lista.insert(0, entrada)
#                             menor = entrada
#                         elif entrada < segundo:
#                             lista.insert(1, entrada)
#                             segundo = entrada
#                         elif entrada > terceiro:
#                             lista.insert(3, entrada)
#                             terceiro = entrada
#                         print(f'Valor {VERDE}adicionado{LIMPA}!')
#                         break
#                 else:
#                     print(f'Valor {AMARELO}duplicado{LIMPA}!')
#         except ValueError:
#             print(f'Valor {VERMELHO}inválido{LIMPA}!')


# for c in range(0,5):
#     while True:
#         entrada = input(f'Digite o {c + 1}º valor: ')
#         try:
#             entrada = int(entrada)
#             if entrada not in lista:
#                 if c == 0 or entrada > lista[-1]:
#                     lista.append(entrada)
#                     print(f'Valor {VERDE}adicionado{LIMPA}!')
#                     break
#                 else:
#                     pos = 0
#                     while pos < len(lista):
#                         if entrada <= lista[pos]:
#                             break
#                         pos += 1
#                     lista.insert(pos, entrada)
#                     print(f'Valor {VERDE}adicionado{LIMPA}!')
#                     break
#             else:
#                 print(f'Valor {AMARELO}duplicado{LIMPA}!')
#         except ValueError:
#             print(f'Valor {VERMELHO}inválido{LIMPA}!')
#
# print(lista)



# desafio 81
# Crie um programa que vai ler vários números e colocar em uma lista
# depois disso, mostre:
# a) quantos números foram digitados.
# b) a lista de valores, ordenada de forma decrescente.
# c) se o valor 5 foi digitado e está ou não na lista.

lista = []
contador = 0
while True:
    entrada = input(f'Digite o {contador+1}º valor ou "n" para sair: ')
    if entrada.lower() == 'n':
        break
    try:
        entrada = int(entrada)
        lista.append(entrada)
        contador += 1
        print(f'Valor {VERDE}adicionado{LIMPA}!')
    except ValueError:
        print(f'Valor {VERMELHO}inválido{LIMPA}!')

lista.sort(reverse=True)
print(f'{contador} números foram digitados, eles são: {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado e esta na lista')
else:
    print(f'O número 5 não esta na lista')



# desafio 82
# programa que leia vários números e colocar em uma lista
# depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente.
# ao final, mostre o conteúdo das três listas geradas.



# desafio 83
# programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.



print('\n','='*15,f'{VERMELHO} FIM {LIMPA}','='*20)