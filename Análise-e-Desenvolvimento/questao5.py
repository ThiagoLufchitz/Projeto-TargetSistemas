# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverterString():
    try:
        s = input("Digite uma string: ")
        if not isinstance(s, str):
            print("Erro: Entrada inválida, Inserir uma entrada valida")
            return
        invertido = ''
        for char in s:
            invertido = char + invertido
        print(f"String invertida: {invertido}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
