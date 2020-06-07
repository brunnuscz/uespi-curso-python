matriz = []
lista = []
c = 0

for i in range(3):
    lista.clear()
    for j in range(3):
        num = int(input(f"Digite [{i+1},{j+1}]: "))
        while (num in lista): 
            print("Erro ! O valor já existe na MATRIZ\n")
            num = int(input("Digite: "))
        lista.append(num)
    matriz.append(lista[:])    
print("\n")
for i in range(3):
    for j in range(3):
        print(f"[  {matriz[i][j]}  ]", end = '')
        if j >= 2:
            print("\n")     
novo = int(input("Digite o número que você quer encontrar: "))
for i in range(3):
    for j in range(3):
        if (novo == matriz[i][j]):
            print(f"Existe !\nEstá na posição [{i+1},{j+1}]")
            c+=1
if(c < 1):
    print("Não Existe !")