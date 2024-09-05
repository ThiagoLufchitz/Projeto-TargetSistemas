# Estágio - Ribeirão Preto
# Autor : Thiago Dorfman Lufchitz
# Universitario : TADS 2º semestre
# Pergunta 2 de 2
# Técnica:

# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.


# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?

# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, 
# mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
from fibonacci import fibonacciNumero
from fibonacci import fibonacci
from contraLetras import InitcontarLetras 
import imprimirSoma
def sequencia():
    seq_a = [1,3,5,7]
    seq_b = [2,4,8,16,32,64]
    seq_c = [0,1,4,9,16,25,36]
    seq_d = [4,16,36,64]
    seq_e = [1,1,2,3,5,8]
    seq_f = [2,10,12,16,17,18,19]
    print("a) ", seq_a,", __")
    print("a) ", seq_a = seq_a.append(seq_a[-1] + 2))
    
    print("b) ", seq_b,", __")
    print("b) ", seq_b = seq_b.append(seq_a[-1] * 2))
    
    print("c) ", seq_c,", __")
    print("c) ", seq_c = seq_c.append((len(seq_c))**2))
        
    print("d) ", seq_d,", __")
    print("d) ", seq_d = seq_d.append((len(seq_d) * 2 )**2))
    
    print("e) ", seq_e,", __")
    print("e) ", seq_e = seq_e.append(seq_e[-1] + seq_e[-2]))
    
    print("f) ", seq_f,", __")
    print("f) ", seq_f = seq_f.append(seq_f[-1] + 1))

def luzes():
    print("Essa questao vi em um Seriado se chama 'alice in borderland' acho que era no 5 jogo da serie era esse enigima")
    print("Passo 1: Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.")
    print("Passo 2: Desligue o primeiro interruptor e ligue o segundo interruptor.")
    print("Passo 3: Vá até as salas das lâmpadas.")
    print("Passo 4: Identifique a lâmpada quente, a lâmpada acesa e a lâmpada fria.")
    print("Passo 5: A lâmpada quente é controlada pelo primeiro interruptor.")
    print("Passo 6: A lâmpada acesa é controlada pelo segundo interruptor.")
    print("Passo 7: A lâmpada fria é controlada pelo terceiro interruptor.")    

def main():
    print("Escolha o número do problema a ser executado:")
    print("1. Verificação de número na sequência de Fibonacci")
    print("2. Contagem de ocorrências da letra 'a'")
    print("3. Valor da variável SOMA")
    print("4. Completar a sequência")
    print("5. Identificação dos interruptores e lâmpadas")
    
    escolha = input("Digite o número do problema: ")

    try:
        match escolha:
            case "1":
                fibonacci()
            case "2":
                InitcontarLetras()
            case "3":
                imprimirSoma()
            case "4":
                sequencia()
            case "5":
                luzes()
            case _:
                print("Escolha inválida. Por favor, digite um número entre 1 e 5.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()