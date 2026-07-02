try:
    numero = int(input('Informe um número inteiro: '))
    while(numero >= 0):
        print(numero)
        numero-=1
except:
    print('Não foi possível exibir a contagem.')