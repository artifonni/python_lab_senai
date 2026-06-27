nome = input('Informe o seu nome: ').title()
idade = int(input('Informe a sua idade: '))
altura = float(input('Informe a sua altura: ').replace(',', '.'))
programador = True

print("************** Saída de dados *************")
print(f'Nome: {nome}, {type(nome)}')
print(f'Idade: {idade}, {type(idade)}')
print(f'Altura: {altura}, {type(altura)}')
print(f'Altura: {programador}, {type(programador)}')

