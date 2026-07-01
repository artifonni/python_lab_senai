n1 = float(input('Informe o valor X: ').replace(',', '.'))
n2 = float(input('Informe o valor Y: ').replace(',', '.'))

print('******** Escolha uma operação **********')
print('1 - Somar | 2 - Subtrair | 3 Multiplicar | 4 - Dividir')

opcao = input('Informe uma opção: ').strip()


match opcao:
    case '1':
        print(f'A soma de X e Y é: {n1 + n2}.')
    case '2':
        print(f'A subtração de X e Y é: {n1 - n2}.')
    case '3':
        print(f'A multiplicação de X e Y é: {n1 * n2}.')
    case '4':
        print(f'A divisão de X e Y é: {n1 / n2}.')
    case _:
        print('Opção inválida...')