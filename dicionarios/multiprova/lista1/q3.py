# Você está indo para a universidade de ônibus e deseja estimar o tempo que o ônibus vai ficar parado nos sinais. Para fazer essa estimativa, você deve se basear em uma série de informações sobre os sinais de trânsito.
# As informações sobre um sinal de trânsito devem ser representadas como um dicionário com os seguintes campos:
# - estado: indica a cor do sinal, que pode ser 'vermelho', 'verde' ou 'amarelo'
# - tamanho_fila: indica o número de carros que estão na sua frente pra passar o sinal
# O seu programa deve ler um valor inteiro N e em seguida ler as informações sobre N sinais, onde os dados de um sinal são fornecidos em uma linha, separados por espaços, seguindo o formato:
# Estado Tamanho_Fila
# Em seguida, o seu programa deve ler três valores inteiros, que indicam, respectivamente, o tempo em segundos que leva para:
# - um sinal amarelo ficar vermelho
# - um sinal vermelho ficar verde
# - um carro que está na sua frente atravessar o sinal
# Assuma que o ônibus somente pode atravessar um sinal verde. Para atravessar um sinal, é necessário esperar todos os carros na frente do ônibus atravessarem o sinal. Assuma que se um sinal está verde, sempre é possível passar por ele antes de ele fechar.
# - Exemplo de Entrada
# 3
# verde 2
# amarelo 3
# vermelho 0
# 1 5 2
# - Exemplo de Saída
# 21 segundos