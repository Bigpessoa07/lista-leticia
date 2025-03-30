preco = int(input("Diga o valor:"))
if preco > 500:
    taxa = (preco - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor com taxa de 50%: {valor_taxado}")
else:
    print("Compra livre de taxa.")
