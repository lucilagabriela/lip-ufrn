c = int(input('')) # numero c
hipotenusa = c
catetoA = 0
catetoB = 0

for i in range(1, c):
  for j in range(1, c):
    if (i**2+j**2) == c*c:
      i = catetoA
      j = catetoB
print(f'Tripla: {catetoA} {catetoB} {hipotenusa}')