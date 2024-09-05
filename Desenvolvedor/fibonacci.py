def fibonacciNumero(numero):
    
    if numero < 0:
        return False
    a = 0
    b = 1
    while a < numero:
        aux = a
        a = b
        b = aux + b
    return a == numero

def  fibonacci():
    try:
        numero = input("Digite o valor de vezes do Fibonacci? ")(int)
        if fibonacci(numero):
            print(f"O numero {numero} pertence á sequencia de Fibonacci. ")   
        else:
            print(f"O numero {numero} não pertence á sequencia de Fibonacci. ")  
    except ValueError:
        print("Por Favor , Digitar um valor válido") 