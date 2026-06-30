nome = input('Informe o nome do aluno: ').title()
nota = float(input('Informe a nota do aluno: ').replace(',','.'))

if nota >= 0 and nota <=10 :
    if nota >= 7:
        print(f'{nome}, Parabéns, você está aprovado')
    elif nota >= 5:
        print(f'{nome}, você está de recuperação.')
    else:
        print(f'{nome} você está reprovado.')
else:
    print(f'Nota de {nome} é inválida.')

