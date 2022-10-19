# Escreva um programa para armazenar os pedidos de pizzas de uma pizzaria. Cada pizza deve ser um dicionário com as seguintes chaves:
# - nome: cujo valor associado deve ser uma string
# - preco: cujo valor associado deve ser um valor inteiro
# - ingredientes: uma lista com os ingredientes da pizza
# O seu programa deve ler os pedidos de pizza do usuário até que o usuário forneça o valor 'sair' para o nome de uma pizza. 
# Cada pedido consiste em três linhas da entrada, onde na primeira linha temos o nome da pizza, na segunda o preço e na terceira os ingredientes da pizza.
# Seu programa deve imprimir uma listagem de todos os pedidos de pizza seguindo o formato abaixo:
# - Exemplo de Entrada
# Marguerita
# 3
# queijo tomate manjericão
# Palmito
# 4
# queijo palmito azeitona
# Frang
# 3
# queijo frango cebola milho
# sair
# - Exemplo de Saída
# Pizzas Pedidas:
# Marguerita (R$ 30): [queijo, tomate, manjericão]
# Palmito (R$ 40): [queijo, palmito, azeitona]
# Frango (R$ 35): [queijo, frango, cebola, milho]


pizzas = []

nome = input()
print('Pizzas Pedidas:')
while nome != 'sair':
    preco = int(input())
    ingredientes = input().split()
    pizza = {'nome': nome, 'preco': preco, 'ingredientes': ingredientes,}
    pizzas.append(pizza)
    print(f'{nome} (R$ {preco}): {ingredientes}')
    nome = input()


'''pizza1 = {
    'nome': '',
    'preco': '',
    'ingredientes': '',
}
pizza2 = {
    'nome': '',
    'preco': '',
    'ingredientes': '',
}
pizza3 = {
    'nome': '',
    'preco': '',
    'ingredientes': '',
}

comando = True

while comando == True:
    nomePizza = input()
    precoPizza = int(input())
    ingredientesPizza = input()
    pizza1['nome'] = nomePizza
    pizza1['preco'] = precoPizza
    pizza1['ingredientes'] = ingredientesPizza
    pizza2['nome'] = nomePizza
    pizza2['preco'] = precoPizza
    pizza2['ingredientes'] = ingredientesPizza
    pizza3['nome'] = nomePizza
    pizza3['preco'] = precoPizza
    pizza3['ingredientes'] = ingredientesPizza
    break

print(f'Pizzas pedidas:')
print(f'pizza1['nome'] (R$pizza1['preco']): pizza1['ingredientes'] )
print(f'pizza2['nome'] (R$pizza2['preco']): pizza2['ingredientes'] )
print(f'pizza3['nome'] (R$pizza3['preco']): pizza3['ingredientes'] )'''