Lista = []
for i in range(1,16):
    num = int(input(f'Digite o {i}ª valor: '))
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    Lista.append(num)
c = 0
for i in range(15):
    if Lista[i] == maior:
        if c < 1:
            print('\nO maior elemento é {} está na'.format(maior), end = '')
            c += 1
        print(' {}ª posição'.format(i + 1), end = '')
a = 0
for i in range(15):
    if Lista[i] == menor:
        if a < 1:
            print('\nO menor elemento é {} está na'.format(menor), end = '')
            a += 1
        print(' {}ª posição, '.format(i + 1), end = '')