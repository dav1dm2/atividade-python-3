#o programa calcula a media dos inputs e informa o ususario de sua situação academica

while True:
    print("bem vindo ao calculador de notas :)\n")

    nota_1 = input("digite sua primeira nota: ")
    nota_2 = input("digite sua segunda nota: ")
    nota_3 = input("digite sua terceira nota")

    try:
        media_das_notas = (float(nota_1) + float(nota_2) + float(nota_3)) /3 

        if media_das_notas >= 7:
            print(f"\naprovado!, sua media foi: {round(media_das_notas, 2)} :D ")
            break
        elif media_das_notas > 4 and media_das_notas < 7:
            print(f"\nreposição, sua media foi: {round(media_das_notas, 2)} ")
            break
        else:
            print(f"\nreprovado :(, sua media foi: {round(media_das_notas, 2)}")    
            break
            
    except ValueError:
        print("\nError: Valores não numericos >:( ")