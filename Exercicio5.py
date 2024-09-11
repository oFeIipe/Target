frase = input("Digite uma frase a ser invertida: ")

frase_invertida = ""

for char in range(len(frase) -1, -1, -1):
    frase_invertida += frase[char]

print(frase_invertida)