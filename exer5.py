# o codigo mostra uma lista de dicionários representando os produtos
produtos = [
    {'nome': 'Produto 1', 'preco': 50.00},
    {'nome': 'Produto 2', 'preco': 60.00},
    {'nome': 'Produto 3', 'preco': 70.00},
    {'nome': 'Produto 4', 'preco': 80.00},
]


for produto in produtos:
    nome = produto['nome']
    preco = produto['preco']
    print(f"{nome} - {preco:.2f} R$")
