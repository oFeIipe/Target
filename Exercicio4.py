valor_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(valor_mensal.values())

for chave in valor_mensal:

    valor_estado = valor_mensal[chave]
    nome_estado = chave

    porcentagem = (valor_estado / valor_total) * 100
    
    print(f"Estado: {nome_estado} Representação {porcentagem:.2f}%")

