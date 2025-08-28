altura = float(input("Digite sua altura: "))
sexo = int(input("Digite 1 para masculino e 2 para feminino: "))

if sexo == 1:
    ideal = (72.7 * altura) - 58
    print("Seu peso ideal é :", ideal)
elif sexo == 2:
    ideal = (62.1 * altura) - 44,7
    print("Seu peso ideal é :", ideal)
else:
    print("\nEntrada invalida\n")
    