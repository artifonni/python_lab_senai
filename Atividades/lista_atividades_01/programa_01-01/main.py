from bisect import bisect
import os

os.system('cls' if os.name == 'nt' else 'clear')

try:
    nome = input('Informe o seu nome: ').strip()
    altura = float(input('Informe a sua altura em cm: ').replace(',','.').strip())
    peso = float(input('Informe o seu peso: ').replace(',','.'))

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print('1 - Calcular IMC | 2 - Encerrar o programa')

        opcao = int(input('Informe a opção desejada: ').strip())

        match opcao:
            case 1:
                imc = peso / (altura * altura)

                limites = [18.5, 25.0, 30.0, 35.0, 40.0]

                categorias = [
                    'Magreza (Baixo peso)',
                    'Peso normal (Peso adequado)',
                    'Sobrepeso (Pré-obesidade)',
                    'Obesidade Grau I',
                    'Obesidade Grau II',
                    'Obesidade Grave (Grau III)'
                ]

                indice = bisect(limites, imc)
                # print(f'IMC: {imc:.2f}')
                resultado = f'[\nNome: {nome}, \nAltura: {altura},\nPeso: {peso}, \nResultado: {imc:.2f} - {categorias[indice]}\n]'

                meu_arquivo = 'Resultado - IMC'
                with open(f"programa_01-01/{meu_arquivo}.txt", "w", encoding="utf-8") as f: f.write(resultado)
                
            case 2:
                print('Encerrando...', end='\nPrograma encerrado!')
                break
            case _:
                print('Opção inválida!')
                continue
        
except Exception as error:
    print(f'Erro: {error}')