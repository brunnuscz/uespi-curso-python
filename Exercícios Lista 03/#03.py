soma = media = cont = 0
for i in range(6):
    num = float(input(f"{i+1}º Valor: "))
    soma += num
    if (num > 0):
        cont+=1
media = soma / 6
print("\n{} Valores positivos\n{:.1f}".format(cont, media))
    