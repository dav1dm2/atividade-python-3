#o codigo execulya uma das 2 funções baseada na opção que o usuario selecionar e então calcula o resultado

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

while True:
    print("\nescolha uma opção:")
    print("\n1. converter de Celsius para Fahrenheit")
    print("\n2. converter de Fahrenheit para Celsius")

    opcao = input("digite a opção desejada (1 ou 2): ")

    if opcao == "1":
        celsius = float(input("\ndigite a temperatura em Celsius: "))
        
        fahrenheit = celsius_para_fahrenheit(celsius)

        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
        break

    elif opcao == "2":
        fahrenheit = float(input("\ndigite a temperatura em Fahrenheit: "))
        
        celsius = fahrenheit_para_celsius(fahrenheit)
        
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
        break
    
    else:
        print("\nopção inválida! Por favor, escolha 1 ou 2.")