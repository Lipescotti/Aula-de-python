n1 = int(input("Escreva o 1º nº inteiro: "))
n2 = int(input("Escreva o 2º nº inteiro: "))

if n1 > n2:
    print("\n", n1, " > ", n2, "\nA diferença entre eles é de: ", n1 - n2)
elif n1 < n2:
    print("\n", n1, " < ", n2, "\nA diferença entre eles é de: ", n2 - n1)
else:
    print("\n ", n1, " = ", n2)