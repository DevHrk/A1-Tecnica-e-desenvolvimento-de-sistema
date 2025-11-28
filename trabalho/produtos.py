def cadastrar_produtos():
    produtos = {}
    while True:
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        try:
            preco = float(input(f"Digite o preço de {nome}: "))
        except ValueError:
            print("Preço inválido! Tente novamente.")
            continue
        produtos[nome] = preco
    return produtos

def listar_produtos(dicionario):
    for nome, preco in dicionario.items():
        print(f"{nome}: R$ {preco:.2f}")
