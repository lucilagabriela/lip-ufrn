# Diz-se que um número primo p é primo de Sophie-Germain se  também é primo. Implemente um programa que avalia um número inteiro informado pelo usuário, mostrando se ele é:
# Primo de Sophie-Germain, ou;
# Primo, ou;
# Não primo.
# Exemplos de execução do programa:
# 9 -> Numero nao primo
# 3 -> Numero primo de Sophie-Germain
# 13 -> Numero primo

n = int(input(''))
sophie = 2*n+1
divisores = []
sophieDiv = []

for x in range(1, n+1):
  if n%x == 0:
    divisores.append(n)

for x in range(1, sophie+1):
  if sophie%x == 0:
    sophieDiv.append(sophie)

if len(divisores) == 2 and len(sophieDiv) == 2:
  print('Numero primo de Sophie-Germain')
elif len(divisores) == 2: #se é primo
  print('Numero primo')
else:
  print('Numero nao primo')