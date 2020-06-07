A = []
M = []
for i in  range(1,11):
    num = int(input('Digite o {}ª valor: '.format(i))) 
    A.append(num)
X = int(input('Digite o valor a ser multiplicado: '))
for i in range(10):
    M.append(A[i] * X)
print('O resultado da multipicação de {} e cada um número no vetor A é {}'.format(X, M))