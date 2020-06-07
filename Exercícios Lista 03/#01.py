cont = 0
for i in range(5):
    num = int(input(f"{i+1}º Valor: "))
    if (num % 2 == 0):
        cont+=1
print(f"\n{cont} valores pares")
    