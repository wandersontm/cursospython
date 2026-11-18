from cores import *
print()
print('='*15,f'{VERMELHO}COMEÇANDO{LIMPA}','='*16 )
print()

# pessoas = {'nome' : 'gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas) # printa todos os elementos do dicionário
# print(pessoas['nome']) #printa o valor atribuído a chave 'nome'
# print(pessoas['sexo']) #printa o valor atribuído a 'sexo'
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ') #exemplo de como puxar os dados dentro das chaves.
# print(pessoas.keys()) # printa todas as chaves colocadas no dicionário
# print(pessoas.values()) #printa todos os valores adicionados ao dicionário
# print(pessoas.items()) #printa todos os elementos que compõem o dicionário, valores e chaves.
# for k in pessoas.keys():
#     print(k) #printa cada uma das chaves em cada loop até passar por todas as chaves.
# for v in pessoas.values():
#     print(v) #printa cada um dos valores em cada loop até passar por todos os valores.
# del(pessoas['sexo']) #apaga a chave sexo e com ela, todos os elementos registrados dentro da chave.
# pessoas['nome']  = 'Leandro' # troca o valor atribuído a nome.
# pessoas['peso'] = 70 # adiciona uma chave que não tinha sido declarada no começo
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# brasil = [] # aqui temos diversos dicionários adicionados em uma lista.
# estado1 = {'UF' : 'Rio de Janeiro', 'Sigla' : 'RJ'}
# estado2 = {'UF' : 'São Paulo', 'Sigla' : 'SP'}
# estado3 = {'UF' : 'Minas Gerais', 'Sigla' : 'MG'}
# brasil.append(estado1)
# brasil.append(estado2)
# brasil.append(estado3)
# print(brasil[0]) #printa o elemento na posição zero da lista, no caso o dicionário 'estado1'
# print(brasil[0]['UF']) #printa a chave 'UF' do dicionário que está contido na posição zero da lista

# estado = dict() #declara um dicionário vazio
# brasil = list() #declara uma lista vazia
# for c in range(0,3): #executa o loop 3 vezes, adicionando elementos ao dicionário nas chaves 'uf' e 'sigla'
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado.copy()) # adiciona uma cópia do dict(estado) a lista conforme os elementos que foram inseridos
# no corrente loop
# for e in brasil: # cicla o loop dentro das posições existentes na lista
#     # for k, v in e.items(): # a cada posição da lista, cicla as chaves e valores.
#     #     print(f' {k}: {v}')
#     for v in e.values(): #printa as chaves e seus valores constantes no dicionário dentro do loop de cada posição da lista
#         print(v, end=' ')
#     print()


# desafio 90
# que leia o nome e média de um aluno, guardando também a situação em um dicionário. no final, mostre o conteúdo
# da estrutura na tela.



# desafio 91
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.



# desafio 92
# que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a
# CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar.



# desafio 93
# que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário
# incluindo o total de gols feitos durante o campeonato.



# desafio 94
# que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
# os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média.



# desafio 95
# aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.


print('\n','='*15,f'{VERMELHO} FIM {LIMPA}','='*20)