def cadastrar_participantes():
    participantes = []
    while True:
        nome = input("Digite o nome do participante (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        participantes.append(nome)
    return participantes

def listar_participantes(lista):
    for i, nome in enumerate(lista, start=1):
        print(f"{i}. {nome}")
