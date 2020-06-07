import os
hora = ["SEG","TER","QUA","QUI", "SEX"]
matriz = []
lista = []

for i in range(2):
    lista.clear()
    for j in range(5):
        horario = str(input("Materia: "))
        lista.append(horario)
    matriz.append(lista[:])
os.system("cls")
print()
print("{:^100}".format("HÓRARIO"))
print("_"*100)
print()
print("     | ", end = '')
for v in range(5):
    print("{:^15} |".format(f"[{hora[v]}]"), end = '')
print()
print("_"*100)
print("\n")
for i in range(2):
    print(f"AULA | ", end = '')
    for j in range(5):
        print("{:^15} |".format(f"[{matriz[i][j]}]"), end = '')
        if (j == 4):
            print("\n")
print("_"*100)
aula = int(input("Nº Aula: "))
dia = int(input("Nº Dia: "))
print(f"\n{matriz[aula-1][dia-1]}")
input()