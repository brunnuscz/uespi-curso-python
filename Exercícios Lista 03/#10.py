maior = 0
lista = []
for i in range(10):
    n = int(input(f"{i+1}º Valor: "))
    while True:
        if n in lista:
            print("ERRO !")
            n = int(input(f"{i+1}º Valor: "))
        else:
            break
    if (i == 0):
        maior = n
    elif (i > 0):
        if (n > maior):
            maior = n
    lista.append(n)
print("\nO Maior valor digitado = {}".format(maior))