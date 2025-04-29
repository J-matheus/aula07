vetorA = [0] * 5
variaX = 0
mult = 0
vetorM = []
for x in range(len(vetorA)):
    vetorA[x] = int(input("informe os numeros: "))
variaX= int(input("informe o multiplicador: "))
for valor in vetorA:
    vetorM.append(mult*valor)
for i in vetorM:
    print(i)

