def contarLetras(string):
    return string.lower().count('a')

def InitcontarLetras():
    try:
        String = input("Digite a String a ser analisada : ")
        if not isinstance(String, str):
            raise ValueError("Entrada invalida")
        count = contarLetras(String)
        print(f"A letra 'a' apareceu {count} vezes nessa string")
    except ValueError as e:
        print(f"Erro: {e}")