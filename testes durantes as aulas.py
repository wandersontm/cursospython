# aula 6:

#n1 = int(input("digite um numero: "))
#n2 =int(input("digite outro numero: "))
#s = n1 + n2
#print(f"A soma entre {n1} e {n2} é igual a {s}!")
# int é numero inteiro  str é texto  float é numero real bool é true ou false 3520

n = (input("digite algo: "))
print(type(n))
print("o resultado é um texto?", n.isalpha())
print("o resultado é um numero?", n.isnumeric())
print("o resultado é um alfanumerico?", n.isalnum())
print("o resultado é um ascii?", n.isascii())
print("o resultado é um decimal?", n.isdecimal())
print("o resultado é um title?", n.istitle())
print("o resultado é um lower?", n.islower())
print("o resultado é um upper?", n.isupper())
print("o resultado é somente espaços?", n.isspace())
