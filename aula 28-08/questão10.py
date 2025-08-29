altura = float(input("Digite sua altura: "))
sexo = int(input("Digite 1 para masculino e 2 para feminino: "))


if sexo == 1:
    ideal = (72.7 * altura) - 58

elif sexo == 2:
    ideal = (62.1 * altura) - 44.7
    
else:
    ideal = "invalido"
    print("\nEntrada invalida\n")


if ideal != "invalido":
    ideal = round(ideal, 3)
    print("Seu peso ideal = ", ideal, " kg")
