pizzas = []
nmrPizzas = int(input('São quantas pizzas? '))
for x in range(nmrPizzas):
    pizza = input('Digite o nome da pizza: ')
    pizzas.append(pizza)

for x in range(nmrPizzas):
    print(pizzas[x])