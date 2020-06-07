Lista = ['Ana','Bruno','Natan','João','Brena','Maria','Zaza','Zé','Mateus','José']
while True:
    nome = str(input('Digite um nome: '))
    for i in range(10):        
            if Lista[i] == nome:
                print('O nome {} está na {}ª posição da Lista'.format(nome, 1+i))
    if nome not in Lista:
        print('O valor não está em Lista')
    c = int(input('Para encerra o programa digite um número negativo: '))
    if c < 0:
        break
    
                