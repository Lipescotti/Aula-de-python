print ("Calculadora\n\n")

n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))

operacao = int(input("\n\nDigite qual operação deseja realizar \n" \
                        "Soma --> 1\n" \
                        "Subteração --> 2\n" \
                        "Multiplicação --> 3\n" \
                        "Divisão --> 4\n" \
                        "Divisão sem resto --> 5\n" \
                        "Resto da divisão --> 6\n" \
                        "Potenciação --> 7\n\n" \
                        "Nada --> 0\n"
                        "\nEscolha: "))


if operacao == 1:
    resultado = n1 + n2
    imagem = " + "

elif operacao == 2:
    resultado = n1 - n2
    imagem = " - "

elif operacao == 3:
    resultado = n1 * n2
    imagem = " x "

elif operacao == 4:
    resultado = n1 / n2
    imagem = " / "

elif operacao == 5:
    resultado = n1 // n2
    imagem = " // "

elif operacao == 6:
    resultado = n1 % n2
    imagem = " % "

elif operacao == 7:
    resultado = n1**n2
    imagem = "^"

else :
    operacao == 0
    print("\n\nCalculo cancelado")

if operacao != 0:
    print("\n\nO resultado de:\n", n1, imagem, n2, " = ", resultado)
