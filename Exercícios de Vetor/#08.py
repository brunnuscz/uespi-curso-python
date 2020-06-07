A = []
B = []
Soma = []
for i in range(10):
    num = int(input('Digite o {}ª valor para o vetor A: '.format(i+1)))
    A.append(num)
for i in range(10):
    num = int(input('Digite o {}ª valor para o vetor B: '.format(i+1)))
    B.append(num)
for i in range(10):
   C = A[i] + B[i]  
   Soma.append(C)
print('\nO resultado da soma dos elementos do vetor A + B é {}'.format(Soma))