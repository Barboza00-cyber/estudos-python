pilha = []

# Empilha os itens um por um
for item in ["A", "B", "C"]:
    pilha.append(item)  # pilha = ["A", "B", "C"]

x = pilha.pop()  # remove o último: C
y = pilha.pop()  # remove o novo último: B

print(x, y)  # C B
