print("Calculo de IMC")

altura = float(input("\nAltura: "))
peso = float(input("Peso: "))

imc = (peso)/(altura*altura)
imc = round(imc, 2)

print("\nSeu IMC é", imc)
