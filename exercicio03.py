nomes = ["joão","carlos","maria","luiza","isabel"]
pesquisa= input("digite um nome para pesquisar: ")
for x in range(len(nomes)):
    if pesquisa == nomes[x]:
        print(f"quem procuras é {pesquisa} e está na posição {x} ")