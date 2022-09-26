# Maior, Menor e MDC
# Escreva um programa que recebe como entrada uma sequência de 10 valores quaisquer. Seu programa deverá informar qual o maior e qual o menor  valor informado, além do MDC (máximo divisor comum) para estes dois valores.

lista = []
mdc = 0
for x in range(10):
    nmr = int(input(''))
    lista.append(nmr)
    for x in range(10):
  	    if nmr%lista[-1] == 0:
            mdc = nmr

print(f'{max(lista)} {min(lista)} {mdc}')