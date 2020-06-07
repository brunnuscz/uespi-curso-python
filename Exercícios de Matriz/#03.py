matriz = []
lista = []
somal = 0
somat = 0
col = 0

for i in range(4):
    lista.clear()
    for j in range(4):
        num = int(input(f"Digite [{i+1},{j+1}]: "))
        somat = somat + num
        lista.append(num)
    matriz.append(lista[:])
print("\n")
for i in range(4):
    for j in range(4):
        print(f"[  {matriz[i][j]}  ]", end = '')
        if (j == 3):
            print("\n")
for j in range(4):
    somal = somal + matriz[2][j]
for i in range(4):
    col = col + matriz[i][1]
print(f"\nSoma Total = {somat}")
print(f"Soma Linha 3 = {somal}")
print(f"Soma Coluna 2 = {col}")