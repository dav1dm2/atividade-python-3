#codigo antigo
'''
n = int(input("Digite um número: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(f"Pares: {i}")
    else:
        print(f"Números ímpares: {i}")
'''
#o codigo faz uma divisão e inclue os numeros com resto igual ou não a 0 a suas respectivas listas
#para então printa-las

try:
    num = input("digite um numero: ")

    pares = []
    impares = []

    for i in range(1, int(num) + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print("\nNumeros pares no intervalo de 1 até", num, ":")
    print(pares)

    print("\nNumeros ímpares no intervalo de 1 até", num, ":")
    print(impares)

except ValueError:
    print(f"{num} não é um valor numerico")