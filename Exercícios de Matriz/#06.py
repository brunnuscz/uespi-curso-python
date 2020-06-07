Matriz = []
Lista = []
res = []
l = 0

for i in range(3):
    Lista.clear()
    for j in range(3):
        num = int(input(f"Digite[{i+1},{j+1}]: "))
        Lista.append(num)
    Matriz.append(Lista[:])
print("\n")
for i in range(3):
    for j in range(3):
        print(f"[  {Matriz[i][j]}  ]", end = '')
        if (j == 2):
            print("\n")
novo = int(input("Digite: "))
for j in range(3):
    var = novo * Matriz[l][j]
    l = l + 1
    res.append(var)
print(f"Multiplicação dos elementos da diagonal principal por {novo}:\n{res}")