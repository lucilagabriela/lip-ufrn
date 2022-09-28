capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Uruguai': 'Montevideo',
    'Paraguai': 'Assunção',
}

busca = capitais.get('Chile')

if busca == None:
    novo = input('Informe a capital do Chile: ')
    capitais['Chile'] = novo
else:
    print(busca)

print(capitais)