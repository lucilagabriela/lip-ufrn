# Escreva um programa que recebe uma string e imprime 'Legal' na tela caso a string contenha apenas números e letras. Imprima 'Chata' caso contrário. Lembre-se, uma string nada mais é que uma lista de caracteres. 
# Dica: Use in ou not in para verificar se um valor qualquer está ou não está contido em uma lista.

palavra = input('')

if palavra.isdigit() == True:
    print('Legal')
elif palavra.isalpha() == True:
    print('Legal')
else:
    print('Chata')