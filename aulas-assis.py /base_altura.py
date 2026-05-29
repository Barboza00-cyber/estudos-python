# Função que encapsula o cálculo, tornando o código reutilizável
def calcular_area(base, altura):
    return base * altura

# Leitura dos dados do usuário
base   = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

# Chama a função e armazena o resultado
area = calcular_area(base, altura)

print(f"A área do retângulo é: {area}")
