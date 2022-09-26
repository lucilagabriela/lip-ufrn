# Paolo fez uma pizza muito gostosa, com vários ingredientes. Seu amigo Toni também fez uma pizza e gostaria de saber se a pizza de Paolo possui todos os ingredientes que ele usou na sua própria pizza.
# O seu programa deve ler uma lista dos ingredientes que Paolo usou na pizza e em seguida uma lista dos ingredientes que Toni usou.
# Ao final, seu programa deve imprimir duas listas: uma indicando os ingredientes que os dois usaram e outra indicando os ingredientes que só Paolo usou.
# Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por espaços.
# - Exemplo de Entrada 1:
# queijo cogumelo pimenta presunto
# pimenta milho queijo
# - Exemplo de Saída 1:
# ['queijo, 'pimenta']
# ['cogumelo, 'presunto]
# use split para formar uma lista a partir de uma linha da entrada
# pizza = input().split()

paolo = input().split()
toni = input().split()
osDois = []
apenasPaolo = []

for x in paolo: # verificar qual é a intersecção dos resultados
  if (x in toni):
    osDois.append(x)
print(osDois)

for x in paolo:
  if(x not in toni):
    apenasPaolo.append(x)
print(apenasPaolo)