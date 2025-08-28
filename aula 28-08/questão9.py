salario = float(input("Digite o salario do trabalhador: R$ "))
presta = float(input("Digite o valor da prestação do emprestimo: R$ "))


if presta > salario*0.2:
    print("\nEmprestimo não concedido")
else:
    print("\nEmprestimo concedido")