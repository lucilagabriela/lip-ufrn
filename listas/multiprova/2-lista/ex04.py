# Pontos mais distantes
# As coordenadas (x, y) de um ponto no plano podem ser armazenadas em uma tupla, como mostrado abaixo: ponto1 = (10.4, 5.5)
# Salve em uma lista um conjunto de n tuplas, representando n pontos informados pelo usuário. Mostre na tela quais são os dois pontos deste conjunto que apresentam a maior distância entre si. A distância entre dois pontos é dado pela Norma Euclidiana
# Dica: para calcular a raiz quadrada, use a função sqrt da biblioteca math como mostrado na "Solução Inicial"
# Importando as funções de biblioteca math (import math)
# Imprimindo a raíz quadrada de 9 ( print (math.sqrt(9)) ) 
# Atribuindo a raíz quadrada de 8 à variável x ( x = math.sqrt(8) )

import math

pontos1 = ( float(input('')), float(input('')) )
pontos2 = ( float(input('')), float(input('')) )

a = (pontos2[0]-pontos1[0])**2
b = (pontos2[0]-pontos1[0])**2
c = math.sqrt(a+b)
print(c)