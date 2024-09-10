import json

caminho_arquivo = 'dados.json'

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)


valores = [item["valor"] for item in dados if item["valor"] != 0]
menor_valor = min(valores)
maior_valor = max(valores)
media = sum(valores) / len(valores)
sup_media = sum(1 for valores in valores if valores > media)

print(f"O menor valor ocorrido no mês (ignorando os zeros) foi: R${menor_valor:.2f}")
print(f"O maior valor ocorrido no mês foi: R${maior_valor:.2f}")
print(f"O número de dias com faturamente acima da média mensal é: {sup_media}")


