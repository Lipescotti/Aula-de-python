# Sequencia de fibonate {1, 1, 2, 3, 5, 8, 13, 21 ...}

tamanho = 0
while tamanho <= 0:
    tamanho = int(input("Escreva quantos numeros quer na sequencia: "))
    if tamanho <= 0:
        print("Tamanho invalido\n\n")

        
anterior = 0
proximo = 1

for n in range(tamanho):
    atual = proximo
    print(f"{proximo} ")
    proximo = anterior + atual
    anterior = atual
