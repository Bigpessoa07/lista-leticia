distancia = int(input("Diga a distancia percorrida:"))
tempo = int(input("Diga o tempo de aluguel:"))

if distancia > 100:
 taxa = (distancia - 100) * 12
 valor = tempo * 90 + taxa
 print(f"Valor com taxa: {valor}")
 
else:
 valor = tempo * 90
 print(f"Valor livre de taxa: {valor}")
