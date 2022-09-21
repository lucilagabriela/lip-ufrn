# Escreva um programa que recebe uma string e imprime 'Legal' na tela caso a string contenha apenas números e letras. Imprima 'Chata' caso contrário. Lembre-se, uma string nada mais é que uma lista de caracteres. 
# Dica: Use in ou not in para verificar se um valor qualquer está ou não está contido em uma lista.
# minha_string = "Este é um texto de exemplo"
#if 'a' in minha_string:
#  print(f"A letra 'a' está em '{minha_string}'")
#else:
#  print(f"A letra 'a' não está em '{minha_string}'")

#palavra = input('')
#if palavra.isdigit() == True:
#    print('Legal')
#elif palavra.isalpha() == True:
#    print('Legal')
#else:
#    print('Chata')

palavra = input('')
digito = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
banco = 'abcdefghijklmnopqrstuvwxyz0123456789'
legal = True
for letra in palavra:
    if letra in banco:
        legal = False
if legal:
    print('Legal')
else:
    print('Chata')