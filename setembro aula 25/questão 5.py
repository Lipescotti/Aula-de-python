#Crie um validador de notas para o ENEM, as notas devem ser de 0-100, qualquer valor fora dessa faixa deverá ser recusado


nota = -1
while nota < 0 or nota > 100:
    nota = float(input("Digite a sua nota do ENEM: "))

    if nota < 0 or nota > 100:
        print("\nNota INVALIDA, tente novamente\n\n")
        
print(f"Nota {nota} validada")
