# Criar uma lista de 5 nomes de alunos e exibir do 2º ao 5º


lista = []


for i in range(5):
    print(f"Digite o {i+1}º nome: ")
    nome = input("")

    lista.append(nome)

print(f"Lista de nomes: {lista[:]}")
print(f"Nomes do 2 ao 5: {lista[1:]}")

