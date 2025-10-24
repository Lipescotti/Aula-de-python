#Lista de nº pares de 0 a 50 e organizar a lista em ordem decrescente

lista = []

for i in range(0,51):
    if(i%2 ==0):
        lista.append(i)

lista.reverse()
print(lista[:])
