contador = 1
soma = 0

# Inicializa maior e menor como None
maior = None
menor = None

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número inteiro: "))
    
    # Soma para cálculo da média
    soma += numero

    # Define maior e menor na primeira iteração
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    contador += 1

# Cálculo da média
media = soma / 10

# Exibe os resultados
print("\nRESULTADOS:")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")


# O programa lê 10 números inteiros do usuário e calcula a soma, média, maior e menor valor.
# O loop continua até que o contador atinja 10.
# O programa imprime os resultados após o loop.