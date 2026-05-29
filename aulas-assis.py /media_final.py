# float() converte a entrada (string) para número decimal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Média aritmética simples
media = (nota1 + nota2) / 2

# :.2f formata com 2 casas decimais
print(f"Média final: {media:.2f}")
