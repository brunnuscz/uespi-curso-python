V1 = []
V2 = []
V3 = [[],[]]
c = 0
for i in range(1,7):
    num = int(input('Digite o {}ª valor: '.format(i)))
    V1.append(num)
for i in range(1,7):
    num = int(input('Digite o {}ª valor: '.format(i)))
    V2.append(num)
for i in range(6):
    if V1[i] == V2[i]:
        V3[0].append(V1[i])
        V3[1].append(i+1)
        c +=1
print('Os números {} foi repetido {} vezes na posição {}'.format(V3[0], c, V3[1]))