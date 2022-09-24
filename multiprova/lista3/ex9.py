# Paolo fez uma pizza muito gostosa, com vários ingredientes. Porém, seu amigo Toni não pode comer alguns dos ingredientes da pizza. Você deve escrever um programa que indica os ingredientes que Paolo pode usar na pizza de modo que Toni vai poder comer também.
# O seu programa deve ler uma lista dos ingredientes que Paolo usou na pizza e em seguida uma lista dos ingredientes que Toni não pode comer. 
# Ao final, seu programa deve imprimir duas listas: uma lista com os ingredientes originais da pizza, e uma lista com os ingridentes dela que Toni pode comer.
# Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por espaços.
# - Exemplo de Entrada 1:
# queijo cogumelo pimenta presunto
# pimenta milho queijo
# - Exemplo de Saída 1:
# ['queijo', 'cogumelo', 'pimenta', 'presunto']
# ['cogumelo', 'presunto']
# use split para formar uma lista a partir de uma linha da entrada
# ingredientes = input().split()


ingredientes = input().split()
nãoPode = input().split()
pode = []
print(ingredientes)
for x in ingredientes: # para cada elemento de ingredientes
    if x not in nãoPode and x not in pode:
        pode.append(x)
print(pode)