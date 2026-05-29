a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
resultado = sorted((a | b) - (a & b))
print(resultado)
