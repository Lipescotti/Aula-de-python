#Crie uma lista de 5 em 5 com 10 valores
#Organize em ordem inversa
#Conte os valores
#Volte a ordem normal 
#Exiba do 3º até o 6º valor


lista = []

for i in range(10):
    lista.append(i*5)


lista.reverse()
print(f"Lista inversa = {lista[:]}")
print(f"Tamanho da lita = {len(lista)}")
lista.reverse()
print(f"Lista normal = {lista[:]}")
print(f"Lista indo 3 ao 6 = {lista[2:6]}")

