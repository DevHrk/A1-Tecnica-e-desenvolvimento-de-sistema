# --- Sistema simples de cadastro de produtos ---

produtos = {}

print("Cadastro de produtos. Para encerrar, digite 'sair' no nome do produto.\n")

while True:
    nome = input("Nome do produto: ")

    if nome.lower() == "sair":
        break

    preco = float(input("Preço do produto (R$): "))
    produtos[nome] = preco

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome} - R$ {preco:.2f}")
