import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('1 - Gravar arquivos | 2 - Ler arquivo | 3 - Encerrar programa')

    opcao = input('Iforme a opção desejada: ').strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            novo_texto = input('Digite o seu texto: ')
            nome_arquivo = input('Informe o nome do arquivo: ').strip()
            with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
                f.write(novo_texto)
        case '2':
            nome_arquivo = input('Informe o nome do arquivo: ').strip()
            try: 
                with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "r", encoding="utf-8") as f:
                                conteudo = f.read()
                                print(conteudo)
            except FileNotFoundError as e:
                print(f'Arquivo não encontrado! {e}')
                continue
        case '3':
            print('Encerrando...', end='\n')
            print('Programa finalizado.')
            break
        case _:
            print('Opção inválida.')
            continue

