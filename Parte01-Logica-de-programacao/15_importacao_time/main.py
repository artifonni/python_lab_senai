import os
import time

try:
    n = int(input('Informe um numero inteiro: '))

    os.system('cls' if os.name == 'nt' else 'clear')

    while n >= 0:
        print(f'{n}...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        n -= 1
    print('👀')

except Exception as erro:
    print(f'Não foi possível iniciar a a contagem. {erro}')