from participantes import cadastrar_participantes, listar_participantes
from produtos import cadastrar_produtos, listar_produtos
from utils import verificar_idade, contador_pares_for, contador_pares_while

def main():
    print("=== Sistema de Gestão de Evento ===\n")

    idade = int(input("Digite sua idade: "))
    if verificar_idade(idade):
        print("Entrada permitida!\n")
    else:
        print("Desculpe, idade mínima é 18 anos.\n")
        return  

    print("Números pares de 1 a 100 com for:")
    contador_pares_for()
    print("\nNúmeros pares de 1 a 100 com while:")
    contador_pares_while()
    print()

    participantes = cadastrar_participantes()
    print("\nLista de participantes cadastrados:")
    listar_participantes(participantes)
    print()

    produtos = cadastrar_produtos()
    print("\nProdutos disponíveis no evento:")
    listar_produtos(produtos)

if __name__ == "__main__":
    main()
