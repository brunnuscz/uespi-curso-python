Lista = []
print('\n{:^20}'.format('MENU'))
print('_'*30)
print('''\n[1] - Cadastrar nome
[2] - Pesquisar nome
[3] - Lista nomes
[4] - Deletar um nome na lista
[5] - sair do porgrama''')
print('_'*30)
while True:
    op = int(input('Digitar opção: '))
    if op == 1:       
        print('_'*30)
        Lista.append(str(input('Digite o nome: ')))
        print('Cadastrado com sucesso.')
        print('_'*30)
    if op == 2:
        pes = str(input('\nQual nome deseja pesquisar: '))
        if pes in Lista:
            print('{} está na Lista na '.format(pes), end = '')
            for i in range(len(Lista)):
                if Lista[i] == pes:
                    print('{}ª posição'.format(i+ 1))
        else:

            print('\nO nome não está na Lista')
    if op == 3:
        if len(Lista) == 0:
            print('A Lista está vazia.')
        else:
            print('_'*30)
            for i in range(len(Lista)):
                print(f'\n{i+1}ª {Lista[i]}')
            print('_'*30)
    if op == 4:
        print('_'*30)
        dele = str(input('Qual nome deseja deletar? '))
        if dele in Lista:
            Lista.remove(dele)
            print('Nome deletado com sucesso')
        else:
            print('O nome não está em Lista')
        print('_'*30)
    if op == 5:
        break
    