import math

try:
    while True:
        PI = math.pi
        raio = float(input('Informe o valor do raio:').replace(',', '.'))

        area = PI * (raio **2)
        print(f'Área do círculo: {area:.2f}²')

        opcao = input('1 - Calcular área do círculo | 2 - Encerrar o programa')
    
        match opcao:
                    case "1":
                            continue
                    case "2":
                            break
                    case _:
                            print('Opção iválida.')

except Exception as erro:
    print(f'Não foi possível calcular a area circunferência.Erro: {erro}')
