# Função para verificar idade
def verificar_idade(idade):
    return idade >= 18

# Contador de números pares usando for
def contador_pares_for():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")

# Contador de números pares usando while
def contador_pares_while():
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1
