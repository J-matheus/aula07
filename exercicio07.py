usuarios= ["matheus", "igor", "rafa", "tomas", "jailton"]
senhas= ["11111", "22222", "33333", "44444", "55555"]

for l in range (len(usuarios)):
    login = input("informe o nome do usuario: ")
    senha = input("informe a senha do usuario: ")
    if login == usuarios and senha == senhas:
        print(f"seja bem vindo {login} seu login foi efetuado com sucesso")
    else:
        print("seu login ou senha está incorreto")
