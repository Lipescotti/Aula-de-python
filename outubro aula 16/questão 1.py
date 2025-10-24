# Crie um algoritimo que leia os dados de um triangulo e classifique seu tipo.

sair = "Não"


while sair == "Não":

    lado1 = 0
    lado2 = 0
    lado3 = 0
    angulo1 = 0
    angulo2 = 0
    angulo3 = 0
    escolha = 0

    while (escolha != 1 and escolha != 2):
        escolha = int(input("Digite 1 para classificar o triangulo pelos lados\nDigite 2 para classificar o triangulo pelos angulo\n\n"))

        if escolha == 1:
            while lado1 <= 0:
                lado1 = float(input("Digite o valor do 1º lado: "))
                if(lado1 <= 0):
                    print("\nValor invalido\n\n")

            while lado2 <= 0:
                lado2 = float(input("Digite o valor do 2º lado: "))
                if(lado2 <= 0):
                    print("\nValor invalido\n\n")


            while lado3 <= 0:
                lado3 = float(input("Digite o valor do 3º lado: "))
                if(lado3 <= 0):
                    print("\nValor invalido\n\n")


        elif escolha == 2:
            while angulo1 <= 0 or angulo1 >= 180:
                angulo1 = float(input("Digite o valor do 1º angulo (em graus): "))
                if(angulo1 <= 0 or angulo1 >= 180):
                    print("\nValor invalido\n\n")

            while (angulo2 <= 0) or (angulo2+angulo1 >= 180):
                print("Digite o valor do 2º angulo (em graus e <", (180.0-angulo1),"): ")
                angulo2 = float(input(""))
                if(angulo2 <= 0) or (angulo2+angulo1 >= 180):
                    print("\nValor invalido\n\n")

            angulo3 = 180 - angulo1 - angulo2
            print("O 3º angulo é iqual a ", angulo3, "\n")

        else:
            print("\n\nOpção invalida\n\n")


    if(escolha == 1):
        if(lado1 == lado2 and lado2 == lado3):
            print("\n\nEsse triangulo é Equilátero")
        elif(lado1 == lado2 and lado2 != lado3) or (lado1 != lado2 and lado2 == lado3) or (lado1 == lado3 and lado2 != lado3):
            print("\n\nEsse triangulo é Isósceles")
        else:
            print("\n\nEsse triangulo é Escaleno")

    else:
        if(angulo1 == 90) or (angulo2 == 90) or (angulo3 == 90):
            print("\n\nEsse triangulo é Retângulo")
        elif(angulo1 <= 60) and (angulo2 <= 60) and (angulo3 <= 60):
            print("\n\nEsse triangulo é Acutângulo")
        else:
            print("\n\nEsse triangulo é Obtusângulo")
    
    
    sair = "a"
    
    while(sair != "Não" and sair != "Sim"):
        sair = input("\n\nDeseja sair(S ou N) ? ")

        if(sair == "Não" or sair == "N" or sair == "Nao" or sair == "não" or sair == "n" or sair == "nao"):
            sair = "Não"

        elif(sair == "Sim" or sair == "sim" or sair == "s" or sair == "S"):
            sair = "Sim"

        else:
            print("\n\nEntrada invalida\n\n")

