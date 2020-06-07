cont = 0
for i in range(6):
    num = int(input(f"{i+ 1}º Valor: "))
    while (num ==  0):
        num = int(input(f"{i+1}º Valor: "))
    if(num > 0):
        cont += 1
print(f"\n{cont} valores positivos")