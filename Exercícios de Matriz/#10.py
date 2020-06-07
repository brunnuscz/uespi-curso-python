
matriz = []
lista = []

for i in range(3):
    lista.clear()
    for j in range(3):
        lista.append(i+j)
    matriz.append(lista[:])
print()
for i in range(3):
    for j in range(3):
        print(f"[  {matriz[i][j]}  ]", end = '')
        if (j == 2):
            print("\n")