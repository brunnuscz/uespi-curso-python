

sem = ["Segunda","Terça","Quarta","Quinta","Sexta"]
maior = 0
for i in range(5):
    print("_"*70)
    ren = float(input(f"\nRendimento da Manhã de {sem[i]}: "))
    ren1 = float(input(f"Rendimento da Tarde de {sem[i]}: "))
    if (i == 0):
        if (ren > ren1):
            maior = ren
            dia = "Manhã"
            semana = sem[i]
        elif (ren1 > ren):
            maior = ren1
            dia = "Tarde"
            semana = sem[i]
    elif (i>0):
        if (ren > ren1):
            if (ren > maior):
                maior = ren
                dia = "Manhã"
                semana = sem[i]
               
        else:
            if (ren1 > maior):
                maior = ren1
                dia = "Tarde"
                semana = sem[i]
               
print("_"*70)
print(f"\nMaior rendimento da semana foi de R${maior} na {dia} de {semana}")
print("_"*70)
input()