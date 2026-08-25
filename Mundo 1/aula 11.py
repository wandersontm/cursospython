# \033[style;text;fundom
#style:          text             fundo (back)
# 0 none         30 branco        40 branco
# 1 Bold         31 vermelho      41 vermelho
# 4 Underline    32 verde         42 verde
# 7 Negative     33 amarelo       43 amarelo
#                34 azul          44 azul
#                35 roxo          45 roxo
#                36 ciano         46 ciano
#                37 cinza         47 cinza

#print('\033[7;33;44m Olá gay\033[m')
# a = 3
# b = 5
# print(f'Os valores são \033[7;33;44m{a}\033[m e \033[7;31;44m{b}\033[m !!!')

# lucas = 'gay'
# print(f'Olá {'\033[31m'}{lucas}{'\033[m'}!!!')
#print('Olá {}{}{}!!!'.format('\033[31m', nome, '\033[m'))

# nome = 'gay'
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'preto':'\033[7;30m',
#          'vermelho':'\033[31m',
#          'verde':'\033[32m',
#          'lilas':'\033[35m',}
#
# print(f'Olá {cores['lilas']}{nome}{cores['limpa']}!!!')

# nome = 'gay'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
LILAS = '\033[35m'
LIMPA = '\033[m'
BRANCO = '\033[30m'
CIANO = '\033[36m'
CINZA = '\033[37m'
#
# print(f'Olá {LILAS}{nome}{LIMPA}!!!!')