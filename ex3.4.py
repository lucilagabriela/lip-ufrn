listaPessoas = ['Slash', 'Alx', 'Paul']
listaPessoas[1] = 'James'
print(f'Oi, {listaPessoas[0]}. Vamos jantar?')
print(f'Oi, {listaPessoas[1]}. Vamos jantar?')
print(f'Oi, {listaPessoas[2]}. Vamos jantar?')

listaPessoas.append('Lu')
print(listaPessoas[3])

listaPessoas.sort()
print(listaPessoas)

listaPessoas.sort(reverse=True)
print(listaPessoas)

tamanho = len(listaPessoas)
print(tamanho)