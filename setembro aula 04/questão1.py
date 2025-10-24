print("---CADASTRO DE LIVROS---\nEscreva as informações a baixo:\n")

titulo = input("Titulo do livro: ")
nome = input("Nome do Autor: ")

genero = input("Gênero: ")

edicao = int(input("Edição (EX: 1): "))
if edicao < 1:
    print("\nValor de edição invalido \n\n")
    
else: 
    ano = int(input("Ano de publicação (de 4 digitos, ex: 1000): "))
    if ano < 1000:
        print("\nAno invalido\n\n")

    else:
        if ano >= 2024:
            classi = "Novo"
        elif 2010 <= ano:
            classi = "Recente"
        else:
            classi = "Clássico"


        mes = int(input("Mês de publicação (EX: 01): "))
        if mes < 1 or mes > 12:
           print("\nMês invalido\n\n")

        else:

            dia = int(input("Dia de publicação (EX: 01): "))
            if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                if dia <= 0 or dia > 31:
                    print("\n\nDia invalido\n\n")
                else:
                    print("\n---Confiramção de dados---" \
                    "\n____________________\n" \
                    "\nTitulo:", titulo,
                    "\nAutor:", nome,
                    "\nGênero:", genero,
                    "\nEdição:", edicao,"ª",
                    "\nData de publicação:",dia,"/",mes,"/", ano, "(", classi,") " \
                    "\n____________________\n")

            elif mes == 2:
                if dia <=0 or dia > 29:
                  print("\n\nDia invalido\n\n")
                
                else:
                    print("\n---Confiramção de dados---" \
                    "\n____________________\n" \
                    "\nTitulo:", titulo,
                    "\nAutor:", nome,
                    "\nGênero:", genero,
                    "\nEdição:", edicao,"ª",
                    "\nData de publicação:",dia,"/",mes,"/", ano, "(", classi,") " \
                    "\n____________________\n")

            elif mes == 4 or 6 or 9 or 11:
                if dia <=0 or dia > 30:
                  print("\n\nDia invalido\n\n")
                else:
                    print("\n---Confiramção de dados---" \
                    "\n____________________\n" \
                    "\nTitulo:", titulo,
                    "\nAutor:", nome,
                    "\nGênero:", genero,
                    "\nEdição:", edicao,"ª",
                    "\nData de publicação:",dia,"/",mes,"/", ano, "(", classi,") " \
                    "\n____________________\n")




                
