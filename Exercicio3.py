import json

with open('dados.json', 'r') as file:
    valores = json.load(file)

valores_validos = [dia['valor'] for dia in valores if dia['valor'] > 0]

valor_maximo = max(valores_validos)
valor_minimo = min(valores_validos)


media_mensal = sum(valores_validos) / len(valores_validos)

dias_acima_media = len([dia for dia in valores if dia['valor'] > media_mensal])

print(f"Dia com maior valor {valor_maximo}")
print(f"Dia com o menor valor {valor_minimo}")
print(f"Quantidade de dias com faturamento acima da média: {dias_acima_media}")