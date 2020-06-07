cont = contf = 0
X = int(input("LEIA: "))

for i in range(X):
    num = int(input("Digite: "))
    if (num > 10 and num < 20):
        cont += 1
    else:
        contf += 1
print(f"\n{cont} Dentro\n{contf} Fora")