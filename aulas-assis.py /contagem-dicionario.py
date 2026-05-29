palavras = ["py", "ia", "py", "dados", "ia", "py"]
freq = {}

# Para cada palavra, incrementa o contador no dicionário
# get(p, 0) retorna 0 se a chave ainda não existir
for p in palavras:
    freq[p] = freq.get(p, 0) + 1

print(freq["py"] + freq["ia"])   # 3 + 2 = 5
print(sorted(freq.items()))      # ordena por chave alfabeticamente
# [('dados', 1), ('ia', 2), ('py', 3)]
