import os

os.system('cls' if os.name == 'nt' else 'clear')

try:
    nome = input('Informe o seu nome: ')
    idade = input('Informe a sua idade: ')


    idade_minima = ''
    nome_filme = ''

    while True:
        print(f'{'*'  * 20} Cineminha Maroto {'*' * 20}')
        print('Sala 1 - A volta dos que não foram (Livre)')
        print('Sala 2 - A roda quadrada (12 anos)')
        print('Sala 3 - As tranças do rei careca (14 anos)')
        print('Sala 4 - Poeira em alto mar (16 anos)')
        print('Sala 5 - A vingança do frango assado (18 anos)')


        sala = input('Informe o número da sala: ')


        match sala:
            case  '1':
                idade_minima = 0
                nome_filme = 'A volta dos que não foram (Livre)'
            case '2':
                idade_minima = 12
                nome_filme = 'A roda quadrada (12 anos)'
            case '3':
                idade_minima = 14
                nome_filme = 'As tranças do rei careca (14 anos)'
            case '4':
                idade_minima = 16
                nome_filme = 'Poeira em alto mar (16 anos)'
            case '5':
                idade_minima = 18
                nome_filme = 'A vingança do frango assado (18 anos)'
            case _:
                print('Sala sala ')



except Exception as error:
    print(error)