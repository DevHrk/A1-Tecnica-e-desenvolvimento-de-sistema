# Sistema de verificação de idade para entrada em eventos

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Estruturas condicionais para verificar a permissão de entrada
if idade < 14:
    print("Entrada proibida. Você não tem idade suficiente.")
elif 14 <= idade < 18:
    print("Entrada permitida somente acompanhado por um responsável.")
else:
    print("Entrada liberada! Aproveite o evento.")
