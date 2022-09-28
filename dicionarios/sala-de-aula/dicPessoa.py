pessoa = {
    'nome': 'Julio Verne',
    'peso': 69.6,
    'altura': '1.83',
}

IMC = pessoa['peso']/pessoa['altura']**2

pessoa['IMC'] = IMC

print(pessoa)