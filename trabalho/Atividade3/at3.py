# --- Cadastro de nomes de alunos ---

alunos = []

print("Digite os nomes dos alunos. Para encerrar, digite 'sair'.")

while True:
    nome = input("Nome do aluno: ")

    if nome.lower() == "sair":
        break

    alunos.append(nome)

print("\nLista de alunos cadastrados:")
for aluno in alunos:
    print("-", aluno)
