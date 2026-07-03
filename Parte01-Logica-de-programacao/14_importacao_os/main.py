import os
try:
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		nome = input('Informe o nome: ').strip()
		idade = int(input('Informe a idade: '))
		cpf = input('Informe o CPF: ')
		email = input('Informe o e-mail:').strip().lower()

		os.system('cls' if os.name == 'nt' else 'clear')
		
		print(f'Nome: {nome}')
		print(f'Idade: {idade}')
		print(f'CPF: {cpf}')
		print(f'email: {email}')

		print('1 - Informar dados de outro usuário | 2 - Encerrar programa')
		opcao = input('Informe  a opção dsejada: ').strip()

		match opcao:
				case "1":
						continue
				case "2":
						break
				case _:
						print('Opção iválida.')
except:
	print('Erro ao executar o programa.')