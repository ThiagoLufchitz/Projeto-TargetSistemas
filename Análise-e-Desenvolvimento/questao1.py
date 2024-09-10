# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

def calcularsoma():
    try:
        INDICE = 13
        SOMA = 0
        K = 0

        while K < INDICE:
            K = K + 1
            SOMA = SOMA + K

        print(f"O valor final da variável SOMA é: {SOMA}")
    except Exception as e:
        print(f"Erro inesperado: {e}")