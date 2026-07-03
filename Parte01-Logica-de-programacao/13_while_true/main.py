try :
    idade_minima = 18
    altura_minima = 1.25
    while True:
        nome = input('Informe o nome: ')
        idade = int(input('Informe a idade: '))
        altura = float(input('Informe a sua altura: '))

        if idade >= idade_minima and altura >= altura_minima :
            print(f'{nome}, sua entrada está liberada.')
        else: print(f'{nome}, entrada não altorizada.')

        print('1 - Passar novo pagante | 2 - Encerrar programa')

        opcao = int(input('Informe uma opção: '))

        match opcao: 
            case 1:
                continue
            case 2:
                print("Encerrando...")
                break
            case _:
                print('Opção inválida.')
                continue
except:
    print('Encerrando...')
