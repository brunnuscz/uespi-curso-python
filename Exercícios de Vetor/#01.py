Lista = []
for i in range(1,11):
    nome = str(input('Digite o {}ª nome: '.format(i)))
    Lista.append(nome)
while True:
    nome1 = str(input('Qual nome quer procurar? '))    
    if nome1 in Lista:
        print('Achei !') 
    else:
        print('Não Achei !')
    print('No total achei {} {} na Lista'.format(Lista.count(nome1), nome1))
    c = int(input('Para parar o programa digite um número negativo: '))
    if c < 0:
        break