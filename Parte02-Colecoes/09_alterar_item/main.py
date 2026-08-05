nomes = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Isabela",
    "João"
]

nome_para_editar = input("Informe o nome que deseja alterar: ").strip().title()

if nome_para_editar in nomes:
    indice = nomes.index(nome_para_editar)
    nomes[indice] = input("Informe o novo nome: ")
    print(nome_para_editar)
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado!")