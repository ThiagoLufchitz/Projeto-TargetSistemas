# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

def calcularPercentage():
    try:
        faturamento_estados = {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53
        }

        faturamento_total = sum(faturamento_estados.values())

        if faturamento_total == 0:
            print("Erro: O faturamento total é zero, não é possível calcular os percentuais.")
            return

        print(f"Faturamento total: R${faturamento_total:.2f}\n")

        for estado, valor in faturamento_estados.items():
            percentual = (valor / faturamento_total) * 100
            print(f"{estado}: {percentual:.2f}%")
    except Exception as e:
        print(f"Erro ao calcular o percentual de faturamento: {e}")
