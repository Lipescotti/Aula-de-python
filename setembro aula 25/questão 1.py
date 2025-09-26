n = -1
print("Adivinhe um numero de 0 a 100\n")


while n != 0:
    while n < 0 or n > 100:
        n = int(input("Escreva um numero: "))
        if n < 0 or n > 100:
            print("\nNumero invalido\n\n")

    if n != 0:
        print("Você errou\n")
        n = -1

print("Parabéns, você advinhou o número")
