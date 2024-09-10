# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def processandooFaturamento():
    try:
        # Carregar os dados do faturamento (a partir do arquivo json)
        with open('dados.json') as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'dados.json' não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro: Arquivo 'dados.json' corrompido ou em formato inválido.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    try:
        # Lista para armazenar os valores de faturamento (apenas os que são maiores que 0)
        faturamentos = []
        for dia in dados:
            if dia["valor"] > 0:
                faturamentos.append(dia["valor"])

        if not faturamentos:
            print("Não há dados de faturamento disponíveis.")
            return

        # • Cálculos do menor, maior valor e a média
        menor_valor = min(faturamentos)
        maior_valor = max(faturamentos)
        media_mensal = sum(faturamentos) / len(faturamentos)

        # • Calcular o número de dias com faturamento acima da média
        dias_acima_da_media = 0
        for valor in faturamentos:
            if valor > media_mensal:
                dias_acima_da_media += 1

        # Exibir os resultados
        print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
        print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
