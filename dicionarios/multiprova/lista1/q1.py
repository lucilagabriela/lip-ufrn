# Escreva um programa para armazenar os pedidos de pizzas de uma pizzaria. Cada pizza deve ser um dicionário com as seguintes chaves:
# - nome: cujo valor associado deve ser uma string
# - preco: cujo valor associado deve ser um valor inteiro positivo
# - ingredientes: uma lista com os ingredientes da pizza
# O seu programa deve ler um valor N e em seguida uma sequência de N pedidos de pizza, onde cada pedido consiste em três linhas da entrada, onde na primeira linha temos o nome da pizza, na segunda o preço e na terceira os ingredientes da pizza.
# Em seguida, seu programa deve ler o nome de um ingrediente X e imprimir o nome da pizza mais cara que contém aquele ingrediente. Imprima a mensagem Nenhuma pizza tem X caso nenhuma pizza possua o ingrediente X.
# Veja abaixo o modelo de entrada e saída que seu programa deve seguir.
# - Exemplo de Entrada 1
# 3
# Marguerita
# 30
# queijo tomate manjericão
# Palmito
# 40
# queijo palmito tomate azeitona
# Frango
# 45
# queijo frango cebola milho
# tomate
# - Exemplo de Saída 1
# Palmito
# - Exemplo de Entrada 2
# 2
# Marguerita
# 30
# queijo tomate manjericão
# Palmito
# 40
# queijo palmito tomate azeitona
# frango
# - Exemplo de Saída 2
# Nenhuma pizza tem frango

pizzas = []
ingredientes = []
precos = []

n = int(input()) #quantidade de pizzas

for x in range(n):
    nomePizza = input()
    precoPizza = int(input())
    ingredientesPizza = input()
    pizza = {
        'nome': nomePizza,
        'preco': precoPizza,
        'ingredientes': ingredientesPizza,
    }
    pizzas.append(pizza)
    ingredientes.append(ingredientesPizza)
    precos.append(precoPizza)

ingrediente = input()
maisCara = max(precos)

if n == 3:
    if ingrediente not in ingredientes[0] and ingrediente not in ingredientes[1] and ingrediente not in ingredientes[2]:
        print(f'Nenhuma pizza tem {ingrediente}')
    else:
        
        print(ingrediente)
if n == 2:
    if ingrediente in ingredientes[0] and ingrediente in ingredientes[1]:
        print(ingrediente)
    else:
        print(f'Nenhuma pizza tem {ingrediente}')