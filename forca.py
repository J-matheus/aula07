palavra = "celular".lower()
chances = 6
letra_descoberta = ["_"] * len(palavra)
letra_errada= []

forca = [
    r"""
     _______
    |      |
    |     ( )
    |     
    |      
    |     
   _|___
""",
    r"""
     _______
    |       |
    |      (0)
    |     
    |      
    |     
   _|___
""",
    r"""
     _______
    |       |
    |      (0)
    |       |
    |       
    |     
   _|___
""",
    r"""
     _______
    |       |
    |      (0)
    |      /|
    |       
    |     
   _|___
""",
    r"""
     _______
    |/      |
    |      (0)
    |      /|\
    |       
    |     
   _|___
""",
    r"""
     _______
    |/      |
    |      (0)
    |      /|\
    |      /
    |       
   _|___
""",
    r"""
     _______
    |/      |
    |      (0)
    |      /|\
    |      / \
    |    
   _|___
"""
]

while chances > 0 and "_" in letra_descoberta:
    print(forca[6 - chances])
    print("Palavra: ", " ".join(letra_descoberta))
    print("Letras erradas: ", " ".join(letra_errada))
    print("Chance restante: ", chances)

    letra = input("Digite uma letra: ").lower()

    if letra in letra_descoberta or letra in letra_errada:
        print("Você já tentou essa letra.\n")
        continue

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas UMA letra.\n")
        continue

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letra_descoberta[i] = letra
    else:
        letra_errada.append(letra)
        chances -= 1
    print("\n" + "-"*40 + "\n")

print(forca[6 - chances])
print("palavra: ", " ".join(letra_descoberta))

if "_" not in letra_descoberta:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu! A palavra era:", palavra)



