num2 = 1
resultado = 1
fibonacci_lista = []

numero = int(input("Digite um número: "))

while resultado <= numero:
    fibonacci_lista.append(resultado)
    num1 = num2
    num2 = resultado
    resultado = num1 + num2

if numero in fibonacci_lista:
    print(f"O número {numero}, pertence a sequência de fibonacci")
else:
    print(f"O número {numero} Não pertence a sequência de Fibonacci")
