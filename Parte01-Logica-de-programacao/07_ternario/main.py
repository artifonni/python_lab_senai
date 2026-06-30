
nome = input('Informe seu nome: ').title()
idade = int(input('Informe a sua idade: '))

validar_idade = f'{nome} é maior de idade.' if idade >= 18 else f'{nome} é menor de idade.'
print(validar_idade)