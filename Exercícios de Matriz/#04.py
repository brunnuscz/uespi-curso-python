matriz = []
lista = []
SL = []
SC = []
somal = l = c = somac = 0


for i in range(3):
    lista.clear()
    for j in range(3):
        num = int(input(f"Digite: [{i+1},{j+1}] "))
        lista.append(num)
    matriz.append(lista[:])
print("\n")
for i in range(3):
    for j in range(3):
        print(f"[  {matriz[i][j]}  ]", end = '')
        if (j == 2):
            print("\n")
for i in range(3):
    for j in range(3):
        somal = somal + matriz[i][c]
        c = c + 1
    c = 0
    SL.append(somal)
    somal = 0
for i in range(3): 
    for j in range(3):
        somac = somac + matriz[l][i]
        l = l + 1    
    l = 0
    SC.append(somac)
    somac = 0

print(f"\nSoma Linha = {SL}\nSoma Coluna = {SC}")