n1 = float(input("Digite a 1º nota: "))
n2 = float(input("\nDigite a 2º nota: "))

if 0.0 <= n1 <= 10.0 and 0.0 <= n2 <= 10.0:
    media = (n1 + n2)/2
    print("\nA media do aluno é ", media)
else:
    print("\n\nNota invalida\n\n")