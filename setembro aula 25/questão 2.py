print("|||Calculo da soma de uma PA|||")

print("\n\nValor inicial = 1\nRasão = 1\nValor final = 10\n")

soma = 0

for i in range(1, 11, 1):
    soma = soma + i
    print(f"Soma da PA quando n é {i} = {soma}")

print(f"\n\nA soma total da PA quando Sn de 10 = {soma}")