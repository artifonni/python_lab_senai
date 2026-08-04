pais = input("Informe o pais a ser pesquisado: ")

paises = [
    "Brasil",
    "Argentina",
    "Chile",
    "Uruguai",
    "Paraguai",
    "Bolívia",
    "Peru",
    "Equador",
    "Colômbia",
    "Venezuela",
    "México",
    "Canadá",
    "Estados Unidos",
    "França",
    "Alemanha",
    "Itália",
    "Espanha",
    "Portugal",
    "Reino Unido",
    "Japão",
    "China",
    "Índia",
    "Austrália",
    "Nova Zelândia",
    "África do Sul",
    "Egito",
    "Nigéria",
    "Marrocos",
    "Rússia",
    "Coreia do Sul",
    # Duplicidades
    "Brasil",
    "Argentina",
    "Japão",
    "França",
    "Canadá",
    "Índia",
    "Brasil",
    "Portugal",
    "China",
    "México"
]

qtd_repeticoes = paises.count(pais)
print(f"{pais} foi encontrado {qtd_repeticoes} de vezes!")