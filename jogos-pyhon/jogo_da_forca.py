import os

print('*******************************')
print('*** Bem-vindo ao jogo da Forca ***')
print('*******************************')

palavra_secreta = input('Digite uma palavra: ').lower()
os.system('cls' if os.name == 'nt' else 'clear')  # limpa tela

letras_acertadas = ['_' for _ in palavra_secreta]
letras_tentadas = set()

erros = 0
max_erros = 6

while True:
    print("\nPalavra:", " ".join(letras_acertadas))
    print("Tentativas:", ", ".join(sorted(letras_tentadas)))

    chute = input("Digite uma letra: ").lower().strip()

    if len(chute) != 1 or not chute.isalpha():
        print("Digite apenas UMA letra válida.")
        continue

    if chute in letras_tentadas:
        print("Você já tentou essa letra.")
        continue

    letras_tentadas.add(chute)

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_acertadas[i] = letra
    else:
        erros += 1
        print(f"Errou! Restam {max_erros - erros} tentativas.")

    if '_' not in letras_acertadas:
        print("\nParabéns! Você acertou:", palavra_secreta)
        break

    if erros >= max_erros:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)
        break
