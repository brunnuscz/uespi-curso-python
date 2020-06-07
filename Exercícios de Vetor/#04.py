Lista = []
c = s = 0
for i in range(10):
    num = float(input('Digite um número real: '))
    Lista.append(num)
for i in range(10):
    if Lista[i] < 0:
        c += 1
    if Lista[i] > 0:
        s = s + Lista[i]
print(f'\nA quantidade de números negativos é: {c}')
print(f'A soma dos números positivos é: {s}')