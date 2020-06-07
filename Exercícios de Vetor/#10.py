Lista = []
for i in range(1,11):
    num = int(input('Digite o {}ª valor: '.format(i)))
    Lista.append(num)
Lista.sort()
print('Os valores digitados em ordem crescente é: {}'.format(Lista))