# import emoji
# print(emoji.emojize('Olá gay.:earth_americas:', language='alias'))

#função ceil de import de math faz arrendondamento de número para cima
# floor arredonda para baixo
#trunc elimina a parte após a vírgula sem nenhum arrendamento
#pow potência de um número
#sqrt calcula uma raiz quadrada
#factorial calcula um fatorial de um número

# import math
# # from math import sqrt << quando quiser importar somente uma função.
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual a {math.trunc(raiz)}')

# from math import sqrt, floor
# num = int(input('Digite um número: '))
# raiz = sqrt(num)
# print(f'A raiz de {num} é igual a {floor(raiz)}')

# import random
# num = random.random()
# #randomiza um número entre 0 e 1
# print(num)

# num_ran = random.randint(1, 100)
# #randomiza um número em um intervalo específico
# print(num_ran)


# desafio 16:
# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: digite um número: 6.127
# o número 6.127 tem a parte inteira 6.
#
# import math
# num = float(input('digite um numero:'))
# print(f' O número {num} tem a parte inteira {math.trunc(num)}')


# desafio 17:
# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# import math
# cateto_a = int(input("Digite o valor de cateto a: "))
# teteto_b = int(input("Digite o valor de cateto b: "))
# print(math.hypot(cateto_a,teteto_b))


# desafio 18:
# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse angulo.

# import math
# num = float(input(f'digite um numero: '))
# graus_num = math.radians(num)
# print(f'o seno de {num}º é {math.sin(graus_num):.2f}, seu cosseno é {math.cos(graus_num):.2f} e sua tangente é {math.tan(graus_num):.2f}')


# desafio 19:
# um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# import math
# import random
# alunos = ("Aline","Joice","Jao","Gay")
# aluno_escolhido = random.choice(alunos)
# if aluno_escolhido in ["Aline","Joice"]:
#     print(f'Entre os alunos da classe, o escolhido para a tarefa foi a {aluno_escolhido}')
# else:
#     print(f'Entre os alunos da classe, o escolhido para a tarefa foi o {aluno_escolhido}')


# desafio 20:
# o prof quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# import random
# from random import shuffle
#
# alunos = ['Aline','Joice','Jao','Gay']
# aluno_escolhido = random.choice(alunos)
#
# print(f' Os alunos da turma são {', '.join(alunos)}.')
# shuffle(alunos)
# print(f' A sequencia de apresentação será: {', '.join(alunos)}')


# desafio 21:
# faça um programa em python que abra e reproduza um audio de um arquivo mp3.