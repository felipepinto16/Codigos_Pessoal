def menu():
    from time import sleep
    try:
        arquivo = open("cadastrados.txt", "a")
        print(f'Arquivo {arquivo} criado com sucesso !')
        arquivo.close()
    except:
        print("Deu ruim !")

    while True:
        print('-=-'*20)
        print("MENU PRINCIPAL")
        print('-=-'*20)

        print("\033[34m 1 - Ver pessoas cadastradas")
        print("\033[34m 2 - Cadastrar pessoas")
        print("\033[34m 3 - Sair do sistema")
        while True:
            try:
                deseja = int(input('\033[033mSua opção: '))
                break
            except:
                print('\033[031mERROR: Por favor, digite um número inteiro válido')
        
        if deseja == 1:
            print('-=-'*20)
            print('PESSOAS CADASTRADAS')
            print('-=-'*20)
            with open('cadastrados.txt', 'r') as cadastrados:
                leitura = cadastrados.readlines()
                for nomes in leitura:
                    nomes = nomes.rstrip('\n')
                    nome_idade = nomes.split(';')

                    print(f'{nome_idade[0]:<60} {nome_idade[1]:<3} Anos.')

        elif deseja == 2:
            print('-=-'*20)
            print('NOVO CADASTRO')
            print('-=-'*20)
            n  = input('Nome: ')
            while True:
                try:
                    i = int(input('Idade: '))
                    break
                except ValueError:
                    print('Idade e numero usuario :(')
            with open('cadastrados.txt', 'a') as arquivo:
                cadastrar = arquivo.write(f'\n{n}; {i}')
            print(f'Novo registro !')

        elif deseja == 3:
            sleep(2)
            print('Saindo do sistema... Até logo!')
            break

        else:
            print('Digite uma opção válida !')
    

menu()