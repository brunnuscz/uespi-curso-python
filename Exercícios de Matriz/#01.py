Lista = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
soma = l = n = 0
for i in range(4):
    for j in range(4):
        Lista[i][j] = int(input('Número para a posição [{},{}]: '.format(i+1,j+1)))
print()
for i in range(4):
    print(Lista[i])
for c in range(3,-1,-1): 
     soma = soma + Lista[l][c]
     l = l + 1
print(f'\nA soma dos valores da diagonal secundaria é: {soma}')
