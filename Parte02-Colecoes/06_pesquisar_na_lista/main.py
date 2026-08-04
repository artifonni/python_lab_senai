cidade = input("Informe a cidade a ser pesquisada: ")

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Brasília",
    "Salvador",
    "Fortaleza",
    "Recife",
    "Curitiba",
    "Porto Alegre",
    "Manaus",
    "Belém",
    "Goiânia",
    "Campinas",
    "São Luís",
    "Maceió",
    "Natal",
    "João Pessoa",
    "Teresina",
    "Aracaju",
    "Cuiabá",
    "Campo Grande",
    "Florianópolis",
    "Vitória",
    "Santos",
    "Sorocaba",
    "Ribeirão Preto",
    "Uberlândia",
    "Londrina",
    "Maringá",
    "Joinville",
    "Blumenau",
    "Chapecó",
    "Caxias do Sul",
    "Pelotas",
    "Juiz de Fora",
    "Montes Claros",
    "Anápolis",
    "Palmas",
    "Boa Vista",
    "Macapá"
]

if cidade in cidades:
    print(f'Cidade encontrada: {cidade}')
else:
    print('Cidade não encontrada!')