estoque = {"caneta": 10, "lapis": 5}

estoque["caneta"] -= 3  # 10 - 3 = 7

# "borracha" não existe → get retorna 0, soma 2 e cria a chave
estoque["borracha"] = estoque.get("borracha", 0) + 2

print(estoque["caneta"], estoque["borracha"])  # 7 2
