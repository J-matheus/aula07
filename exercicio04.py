notas= [0.0]*5
soma = 0
cont = 0
for n in range(len(notas)):
    notas[n]=float(input(f"digite a nota do aluno {n}: "))
for s in range(len(notas)):
    soma+=notas[s]
media=soma/len(notas)
for c in range (len(notas)):
    if notas[c]>media:
        cont+=1
print(f"Encontramos {cont} alunos acima da média")


