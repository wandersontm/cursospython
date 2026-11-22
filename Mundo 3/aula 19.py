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
# que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.

# aluno: dict[str, str | float] = {'nome': str(input('Qual o nome do aluno? '))}
# while True:
#     try:
#         aluno['media'] = float(input(f'Qual a média do {aluno["nome"]}? '))
#     except ValueError:
#         print(f'Valor {VERMELHO}invalido{LIMPA}. digite novamente!')
#         continue
#     break
# print(f'O nome do aluno é {aluno["nome"]}.')
# print(f'Sua media foi {aluno["media"]}.')
# print(f'O aluno {aluno["nome"]} ' + ('foi aprovado.' if aluno["media"] >= 7 else 'está em recuperação.' if aluno["media"] >= 5 else 'está reprovado.'))

# if aluno['media'] >= 7:
#     aluno['situacao'] = 'Aprovado'
# elif 5<= aluno['media'] < 7:
#     aluno['situacao'] = 'Recuperação'
# else:
#     aluno['situacao'] = 'Reprovado'
# for k, v in aluno.items(): # print montado com uma chave especifica para a situação do aluno.
#     print(f'{k} é igual a {v}')



# desafio 91
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# dados = dict()
#
#
# from random import randint
# from time import sleep
# from operator import itemgetter
# dados['jogador_1'] = randint(1,6)
# dados['jogador_2'] = randint(1,6)
# dados['jogador_3'] = randint(1,6)
# dados['jogador_4'] = randint(1,6)
#
# # for k, v in dados.items():
# #     print(f'O {k} tirou o número {v}.')
# #     sleep(0.5)
#
# print()
# rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
#
# for i, v in enumerate(rank):
#     print(f'O {i+1}º lugar: {v[0]} tirou o número {v[1]}.')
#     sleep(0.5)



# desafio 92
# que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a
# CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar.

# dados = dict()
# from datetime import date
#
# dados['O nome e'] = str(input('Nome: '))
# while True:
#     try:
#         dados['A idade e'] = date.today().year - (int(input('Ano de Nascimento: ')))
#     except ValueError:
#         print(f'Valor {VERMELHO}invalido{LIMPA}')
#         continue
#     break
# while True:
#     try:
#         dados['A carteira e'] = int(input('Carteira de trabalho (0 para não possui): '))
#     except ValueError:
#         print(f'Valor {VERMELHO}invalido{LIMPA}')
#         continue
#     break
#
#
# if dados['A carteira e'] != 0:
#     while True:
#         try:
#             dados['O salario e'] = int(input('Seu salario é: '))
#         except ValueError:
#             print(f'Valor {VERMELHO}invalido{LIMPA}')
#             continue
#         break
#     while True:
#         try:
#             dados['foi contratado em'] = int(input('Ano em que foi contratado: '))
#         except ValueError:
#             print(f'Valor {VERMELHO}invalido{LIMPA}')
#             continue
#         break
#     dados['aposentadoria com'] = (35 - (date.today().year - dados['foi contratado em'])) + dados['A idade e']
#     dados['faltam anos para aposentar:'] = dados['aposentadoria com'] - dados['A idade e']
#     dados['Nos anos trabalhados até hoje, recebeu um total de R$'] = dados['O salario e']*(date.today().year - dados['foi contratado em'])*12
# print()
# for k, v in dados.items():
#     print(f'{k} {v}')



# desafio 93
# que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário
# incluindo o total de gols feitos durante o campeonato.


# dados = dict()
# gol = list()
# dados['nome'] = str(input('Qual o nome do jogador?: '))
#
# while True:
#     try:
#         dados['partidas'] = int(input('quantos jogos ele jogou?: '))
#     except ValueError:
#         print(f'Valor {VERMELHO}inválido{LIMPA}!')
#         continue
#     break
# for c in range(1, dados['partidas']+1):
#     while True:
#         try:
#             gol.append(int(input(f'Fez quantos gols na {c}ª partida?: ')))
#         except ValueError:
#             print(f'Valor {VERMELHO}inválido{LIMPA}!')
#             continue
#         break
# dados['gols'] = gol[:]
# dados['soma'] = sum(gol)
# print()
# print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
# for c, v in enumerate(dados['gols']):
#     print(f' Na {c+1}ª partida, fez {v} gols.')
# print(f'Foi um total de {dados["soma"]} gols.')



# desafio 94
# que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
# os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média.

# dados = dict()
# pessoas = list()
# temp = soma = 0
# encontrou_f = False
#
# while True:
#     while True:
#         try:
#             temp = str(input('Nome ou "sair" para sair: '))
#         except ValueError:
#             print(f'Nome {VERMELHO}inválido{LIMPA}.')
#             continue
#         break
#     if temp == 'sair':
#         break
#     dados['nome'] = temp
#     while True:
#         try:
#             dados['sexo'] = str(input('sexo: [m/f] : ')).upper()[0]
#         except ValueError:
#             print(f'Entrada {VERMELHO}inválida{LIMPA}.')
#             continue
#         if dados['sexo'] in 'MF':
#             break
#         print(f'Entrada {VERMELHO}inválida{LIMPA}.')
#
#     while True:
#         try:
#             dados['idade'] = int(input('idade: '))
#         except ValueError:
#             print(f'Valor {VERMELHO}inválido{LIMPA}.')
#             continue
#         break
#
#     pessoas.append(dados.copy())
#
# print()
# print(f'Ao total foram cadastradas {len(pessoas)} pessoas. ')
#
# for dicionario in pessoas:
#     soma += dicionario['idade']
#
# print(f'A média das idades é {soma/len(pessoas):5.2f} anos.')
#
# print(f'As mulheres cadastradas foram:', end=' ')
#
# for dicionario in pessoas:
#     if dicionario['sexo'] == 'F':
#         print(dicionario['nome'], end=', ')
#         encontrou_f = True
#
# if not encontrou_f:
#     print("Nenhuma", end='')
#
# print()
# print(f'A lista das pessoas que estão acima da média de idade é:')
# for dicionario in pessoas:
#     if dicionario['idade'] > (soma/len(pessoas)):
#         print(f'Nome = {dicionario["nome"]}, sexo = {dicionario["sexo"]}, idade = {dicionario["idade"]}')



# desafio 95
# aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

time = list()
dados = dict()
gol = list()

while True:
    dados.clear()
    gol.clear()
    temp = str(input('Qual o nome do jogador? ou "sair": '))
    if temp == 'sair':
        break
    dados['jogador'] = temp

    while True:
        try:
            dados['partidas'] = int(input('quantos jogos ele jogou?: '))
        except ValueError:
            print(f'Valor {VERMELHO}inválido{LIMPA}!')
            continue
        break
    for c in range(1, dados['partidas']+1):
        while True:
            try:
                gol.append(int(input(f'Fez quantos gols na {c}ª partida?: ')))
            except ValueError:
                print(f'Valor {VERMELHO}inválido{LIMPA}!')
                continue
            break
    dados['gols'] = gol[:]
    dados['soma'] = sum(gol)
    time.append(dados.copy())

print()
print(f'Cod   nome                   gols                   total')
print('-'*60)

for cod, dicionario in enumerate(time):
    print(f'{cod:>2}   {str(dicionario["jogador"]):<20}{str(dicionario["gols"]):<28}{str(dicionario["soma"]):<8}')
    # print(f'{cod:>2}', end=' ')
    # for v in dicionario.values():
    #     print(f'{str(v):<20}', end='')
    # print()

while True:
    try:
        nome = int(input('Mostrar dados de qual jogador(Cod)? (999 para sair):  '))
    except ValueError:
        print(f'Valor {VERMELHO}inválido{LIMPA}!')
        continue

    if nome == 999:
        break

    if nome >= len(time):
        print(f'Valor {VERMELHO}inválido{LIMPA}!')
        continue

    print(f'Levantamento do jogador: {time[nome]["jogador"]}')

    for c, v in enumerate(time[nome]['gols']):
        print(f' Na {c+1}ª partida, fez {v} gols.')
    print(f'Foi um total de {time[nome]["soma"]} gols.')

print(len(time))

print('\n','='*15,f'{VERMELHO} FIM {LIMPA}','='*20)