# Escreva um programa que lê três listas que especificam os ingredientes de diferentes saladas de frutas. Em seguida, o seu programa deve ler qual é a fruta favorita do usuário e imprimir uma mensagem informando se a fruta favorita do usuário ocorre em todas as saladas de frutas ou não.
# Os ingredientes de cada salada de frutas serão fornecidos em uma linha própria, onde cada ingrediente de uma salada será separado por espaços. Veja o exemplo de entrada e saída abaixo.
# - Exemplo de Entrada 1:
# banana maçã laranja mamão
# uva banana manga
# kiwi laranja pêssego banana
# banana
# - Exemplo de Saída 1:
# banana aparece em todas as saladas
# - Exemplo de Entrada 2:
# banana maçã laranja mamão
# goiaba uva banana manga
# kiwi laranja pêssego
# laranja
# - Exemplo de Saída 2:
# laranja não aparece em todas as saladas

# use split para formar uma lista a partir de uma linha da entrada
# salada = input().split()

lista1 = []
lista2 = []
lista3 = []

lista1 = input().split()
lista2 = input().split()
lista3 = input().split()
fruta = input('')
if fruta in lista1 and fruta in lista2 and fruta in lista3:
    print(f'{fruta} aparece em todas as saladas')
else:
    print(f'{fruta} não aparece em todas as saladas')