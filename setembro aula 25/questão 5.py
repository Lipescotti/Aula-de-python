#Fatorial 

n = -1
while n < 0:
    n = int(input("Escreva um numero (inteiro e > 0) para ser fatorado: "))
    if n < 0:
        print("\nNúmero invalido\n\n")


fatorial = 1
for i in range(n, 0, -1): 
    print(fatorial, "*", i, " = ", fatorial * i)
    fatorial = fatorial * i

print(f"\n\nO fatorial de {n} = {fatorial}")