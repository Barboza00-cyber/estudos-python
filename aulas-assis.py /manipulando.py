notas = [5, 7, 9]
notas.append(6)        # adiciona 6 ao final → [5, 7, 9, 6]
notas[1] = notas[1] + 1  # índice 1 era 7, vira 8 → [5, 8, 9, 6]

print(notas)  # [5, 8, 9, 6]
