nome = input("Informe seu nome: ")
telefone = input('Informe um telefone para contato: ')


print("Olá, ", nome,", o número de telefone ", telefone, ' foi salvo com sucesso.')
print('Olá ' + nome + ', o número de telefone' + telefone + ' foi salvo com sucesso.')
print('Olá {}, o número de telefone {}.'.format(nome, telefone))
print(f'Olá, {nome}, o número de telefone {telefone} foi salvo com sucesso.')
