cor = input('')
preco = float(input(''))
if cor == 'amarelo':
  print('Vai comprar')
elif cor == 'verde' or cor == 'azul':
        if preco <= 20:
        	print('Vai comprar')
        else:
        	print('Não vai comprar')
else:
  print('Não vai comprar')

# if (cor == 'amarelo') or (((cor == 'verde') or (cor == 'azul')) and (preco <= 20)):