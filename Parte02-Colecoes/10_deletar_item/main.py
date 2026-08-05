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

nome = input("Informe o nome que deseja deletar: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)
    del(nomes[indice])
    print(nomes)
else:
    print("Nome não encontrado!")