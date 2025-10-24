# Crie um algoritimo que leia vários valores e classifique entre: par, impar, zero, soma dos pares, multiplique os impares e conte os 0, até que o usuario pare

sair = "Não"

somaPar = 0
multImpar = 1.0
zeros = 0

while(sair == "Não"):

    numero = float(input("Digite um numero: "))

    if numero%2==0 and numero != 0:
        somaPar = somaPar + numero
        print("\nO numero é par\n")

    elif numero != 0:
        multImpar = multImpar*numero
        print("\nO numero é impar\n")

    else:
        zeros = zeros + 1
        print("\nO numero é 0\n")

    sair = "a"
    
    while(sair != "Não" and sair != "Sim"):
        sair = input("\n\nDeseja sair(S ou N) ? ")

        if(sair == "Não" or sair == "N" or sair == "Nao" or sair == "não" or sair == "n" or sair == "nao"):
            sair = "Não"

        elif(sair == "Sim" or sair == "sim" or sair == "s" or sair == "S"):
            sair = "Sim"

        else:
            print("\n\nEntrada invalida\n\n")


print(f"Soma total de nº pares = {somaPar}\nMultiplicação total de nº impares = {multImpar}\nTotal de zeros digitados = {zeros}\n\n")