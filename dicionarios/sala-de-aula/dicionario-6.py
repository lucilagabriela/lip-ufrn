# Construa um dicionário apenas com as palavras iniciadas com um fragmento de texto informado pelo usuário. Por exemplo, caso o usuário digite ‘i’, o dicionário resultante conterá as palavras ‘incendiar’, ‘insensato’ e ‘importante’, além de seus sinônimos.

dic = {
    'provável': ['possível', 'capaz'],
    'incendiar': ['arder', 'atear'],
    'problema': ['contrariedade', 'adversidade'],
    'insensato': ['imprudente', 'desajuizado'],
    'possível': ['provável', 'capaz'],
    'importante': ['significativo', 'grave'],
}

palavra = input('Informe o termo: ')

busca = {chave:valor for chave, valor in dic.items() if palavra in chave}

print(f'busca = {busca}')