a = [1, 2]
b = a        # b aponta para o mesmo lugar que a (referência)
c = a.copy() # c é uma cópia independente de a

b.append(3)  # modifica b e a (são o mesmo objeto)
c.append(4)  # modifica só c

print(a)  # [1, 2, 3]
print(c)  # [1, 2, 4]
