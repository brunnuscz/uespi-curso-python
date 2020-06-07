matriz1 = []
lista1 = []
matriz2 = []
lista2 = []
S = []
D = []
soma1 = soma2 = 0
sub1 = sub2 = 0

for i in range(2):
    lista1.clear
    for j in range(3):
        num = int(input(f"Digite MATRIZ A: [{i+1},{j+1}] "))
        lista1.append(num)
    matriz1.append(lista1[:])
print("_"*50)

for i in range(2):
    lista2.clear
    for j in range(3):
        num = int(input(f"Digite MATRIZ B: [{i+1},{j+1}] "))
        lista2.append(num)
    matriz2.append(lista2[:]) 
print()
for i in range(2):
    for j in range(3):
        soma1 = soma1 + matriz1[i][j]
        soma2 = soma2 + matriz2[i][j]
S.append(soma1 + soma2)
D.append(soma1 - soma2)

print(f"SOMA = {S}\nSUBTRAÇÂO = {D}\n")
print("_"*50)
print("\n")
print("MATRIZ A:\n")
for i in range(2):
    for j in range(3):
        print(f"[  {matriz1[i][j]}  ]", end = '')
        if (j == 2):
            print("\n")
print("_"*50)
print("\n")
print("MATRIZ B:\n")
for i in range(2):
    for j in range(3):
        print(f"[  {matriz2[i][j]}  ]", end = '')
        if (j == 2):
            print("\n")
print("_"*50)
input()