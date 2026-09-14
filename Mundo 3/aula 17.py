from cores import *
print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*16 )

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

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

# for v in valores: # printa os valores conforme a formatação no print
#     print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')



print('\n','='*15,f'{VERMELHO} FIM {LIMPA}','='*20)