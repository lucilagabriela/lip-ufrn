dic = {
    'nome': 'Julio Verne', # 'chave': 'valor'
    'peso': 69.6,
    'altura': '1.83',
}

# print(dic['chave']) -- mostrar chave do dic
# print(dic.get('chave')) -- mostrar valor do dic
# print(dic.get('peso', 'Valor não encontrado')) -- se não achar o valor, mostra essa mensagem
# dic.setdefault('chave') retorna valor da chave
#-
# print(dic.keys()) -- obter todas as chaves
# print(dic.values()) -- obter todos os valores
# print(dic.items()) -- percorre 'chave': 'item'

# dic['chave'] = valor
# dic.update({'chave':valor}) ou dic.update(chave=valor)

# del dic['chave']
# dic.pop('chave')
# dic.popitem() exclui ultimo item
# dic.clear() deixar vazio

# copia = dic.copy()

#* dic.fromkeys()

for chave in dic.keys():
    print(f'Chave = {chave} e Valor = {dic[chave]}')