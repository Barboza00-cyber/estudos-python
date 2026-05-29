dados = [[1, 2], [3, 4]]
copia = dados.copy()  # cópia rasa: as sublistas ainda são compartilhadas

copia[0].append(9)  # altera a sublista compartilhada → afeta dados também
copia.append([5])   # adiciona só em copia, não afeta dados

print(dados)  # [[1, 2, 9], [3, 4]]
print(copia)  # [[1, 2, 9], [3, 4], [5]]
