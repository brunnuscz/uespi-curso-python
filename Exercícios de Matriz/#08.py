
matriz = []
aluno = []
r = a = 0
for i in range(5):
    aluno.clear()
    media = 0
    soma = 0
    for j in range(2):
        nota = int(input(f"Digite {j+1}ª NOTA: "))
        soma = soma + nota
    print("-"*50)
    media = soma/2
    aluno.append(media)
    if (media >= 7):
        aluno.append("APROVADO")
        a+=1
    else:
        r+=1
        aluno.append("REPROVADO")
    matriz.append(aluno[:])
print()

for i in range(5):
    print(f"{i+1}º Aluno Média = {matriz[i][0]} Situação = {matriz[i][1]}")
print(f"\nAPROVADOS = {a}\nREPROVADOS = {r}")