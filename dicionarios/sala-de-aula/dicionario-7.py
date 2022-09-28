# Complemente o exercício anterior para que o usuário veja na tela um dicionário com todas as palavras que tenham como sinônimo um termo digitado por ele. 

dic = {
    'provável': ['possível', 'capaz'],
    'incendiar': ['arder', 'atear'],
    'problema': ['contrariedade', 'adversidade'],
    'insensato': ['imprudente', 'desajuizado'],
    'possível': ['provável', 'capaz'],
    'importante': ['significativo', 'grave'],
}

sinonimo = input('Informe o sinônimo a ser buscado: ')

busca = {chave:valor for chave, valor in dic.items() if sinonimo in chave}

print(f'busca = {busca}')