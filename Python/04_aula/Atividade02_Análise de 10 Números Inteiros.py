soma = 0
maior = None
menor = None

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 10

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos números: {media}")
