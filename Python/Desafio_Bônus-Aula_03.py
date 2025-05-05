# Programa para controle de consumo de reservatório de água

# Entrada de dados
altura = float(input("Digite a altura do reservatório (em cm): "))
largura = float(input("Digite a largura do reservatório (em cm): "))
comprimento = float(input("Digite o comprimento do reservatório (em cm): "))
consumo_diario = float(input("Digite o consumo médio diário (em litros): "))

# Cálculo do volume em cm³
volume_cm3 = altura * largura * comprimento

# Conversão para litros
capacidade_litros = volume_cm3 / 1000

# Cálculo da autonomia em dias
autonomia_dias = capacidade_litros / consumo_diario

# Classificação do consumo
if autonomia_dias < 2:
    classificacao = "Consumo elevado"
elif 2 <= autonomia_dias <= 7:
    classificacao = "Consumo moderado"
else:
    classificacao = "Consumo reduzido"

# Saída dos resultados
print("\n=== Resultados ===")
print(f"Capacidade total do reservatório: {capacidade_litros:.2f} litros")
print(f"Autonomia do reservatório: {autonomia_dias:.2f} dias")
print(f"Classificação do consumo: {classificacao}")
