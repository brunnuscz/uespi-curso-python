contp = conti = contpo = contn = 0
for i in range(5):
    num = int(input("Digite: "))
    if(num % 2 == 0):
        contp += 1
    else:
        conti += 1
    if (num > 0):
        contpo += 1
    else:
        contn += 1
print(f"\n{contp} PARES\n{conti} IMPARES\n{contpo} POSITIVOS\n{contn} NEGATIVO")