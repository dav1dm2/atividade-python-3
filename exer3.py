#o codigo mostra todos os valores antecedentes e incluindo ' n ' multiplicados por 2

while True:
    try:
        n = input("digite um valor: ")

        for i in range(1, int(n) + 1):
            dobro = i * 2
            print(f"O dobro de {i} é {dobro}")

        break
    except ValueError:
        print('valor não numerico')