def cadastrar_jogador():
    nome = input('Nome do jogador: ')
    partidas = list()
    qtd_partidas = int(input(f"Quantidade de partidas do {nome} ? "))

    cont = 0
    for i in range(qtd_partidas):
        list(str(qtd_partidas))
        partidas.append(int(input(f'Quantos gols ele fez na {i} partida ? ' )))
        
        soma = sum(partidas)
        dic = {'Nome': nome, 'Gols': partidas, "Total": soma}


    print('-=-'*20)
    print(dic)
    print('-=-'*20)
    print(f'O campo nome tem o valor{nome}\nO campo gols tem o valores {partidas}\nO campo total tem o valor {soma}')
    print('-=-'*20)

    print(f'O jogador {nome} tem {qtd_partidas} partidas.')

    for i in range(qtd_partidas):
        print(f"Na partida {i}, fez {partidas[i]} gols")

    print(f'O total de gols foi de {soma} gols !')


