def menu():
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
            
        if deseja == 1 or deseja == 2 or deseja == 3:
            if deseja == 1:
                print('-=-'*20)
                print('OPCÃO 1')
                print('-=-'*20)
                
            elif deseja == 2:
                print('-=-'*20)
                print('OPÇÃO 2')
                print('-=-'*20)

            print('\033[031mPor favor digite uma opção válida !')

menu()