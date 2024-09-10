# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se 
# o número informado pertence ou não a sequência.

def fibonacci(n):
    
    if n < 0:
        return False
    a = 0
    b = 1
    while a < n:
        aux = a
        a = b
        b = aux + b
    return a == n

def nFibonacci():
    try:
        numero = int(input("Digite um número: "))
        if fibonacci(numero):
            print(f"{numero} pertence à sequência de Fibonacci.")
        else:
            print(f"{numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
