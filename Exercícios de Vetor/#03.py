Lista = [[],[]]
par = impar = 0
for i in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par = par + 1
        Lista[0].append(num)
    else:
        impar = impar + 1
        Lista[1].append(num)
print('\nA quantidade de números pares é {}, e os números pares são {}'.format(par, Lista[0],))
print('A quantidade de números impares é {}, e os números impares são {}'.format(impar, Lista[1]))    