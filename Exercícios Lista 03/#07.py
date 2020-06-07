res = 0
n = int(input("Digite: "))

for i in range(n,1,-1): 
    if (i % 2 == 0):
        res = i**2
        print(f"{i} ^ 2 = {res}")