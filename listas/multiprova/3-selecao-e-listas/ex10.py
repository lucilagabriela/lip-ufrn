# Paolo fez uma pizza muito gostosa, com vários ingredientes. Porém, seu amigo Toni pediu para acrescentar mais alguns ingredientes na pizza. Você deve escrever um programa que adicionar os ingredientes de Toni à pizza, tomando cuidado para não adicionar um ingrediente mais de uma vez.
# O seu programa deve ler uma lista dos ingredientes que Paolo usou na pizza e em seguida uma lista dos ingredientes que Toni quer adicionar.
# Ao final, seu programa deve imprimir duas listas: uma lista com os ingredientes originais da pizza, e uma lista com a composição da pizza depois de adicionar os ingredientes que Toni pediu.
# Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por vírgulas.
# - Exemplo de Entrada 1:
# queijo,cogumelo,pimenta,presunto
# pimenta,milho,queijo
# - Exemplo de Saída 1:
# ['queijo', 'cogumelo', 'pimenta', 'presunto']
# ['queijo', 'cogumelo', 'pimenta', 'presunto', 'milho']
# use split para formar uma lista a partir de uma linha da entrada
# pizza = input().split(',')

ingredientes = input().split(',')
addIngredientes = input().split(',')

print(ingredientes)

for x in addIngredientes:
  if (x not in ingredientes):
    ingredientes.append(x)
 
print(ingredientes)