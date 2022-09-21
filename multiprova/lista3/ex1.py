n = int(input(''))
numeros = []
for x in range(n):
    numeros.append(float(input()))

tetos = []
for numero in numeros:
    if numero - int(numero) > 0:
        teto = int(numero)+1
    else:
        teto = int(numero)
    numeros.append(numero)
print(*tetos)
# abrangencia:
#tetos = [int(numero)+1 if numero - int(numero) > 0 else int(numero) for numero in numeros]
#print(*tetos)

#n = int(input(''))
#numeros = []

#for x in range(n):
#  numero = float(input(''))
#  if int(numero) / numero == 1:
#    numero = int(numero)
#  else:
#    numero = (int(numero)+1)
    
#  numeros.append(numero)

#print(*numeros)

# print(teto, end=' ')