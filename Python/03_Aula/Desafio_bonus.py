def calcular_capacidade_reservatorio(altura, largura, comprimento):
    """Calcula a capacidade total do reservatório em litros"""
    volume_cm3 = altura * largura * comprimento
    capacidade_total = volume_cm3 / 1000  # Convertendo cm³ para litros
    return capacidade_total

def calcular_autonomia(capacidade_total, consumo_diario):
    """Calcula a autonomia do reservatório em dias"""
    return capacidade_total / consumo_diario

def classificar_consumo(autonomia):
    """Classifica o consumo com base na autonomia"""
    if autonomia < 2:
        return "Consumo elevado"
    elif 2 <= autonomia <= 7:
        return "Consumo moderado"
    else:
        return "Consumo reduzido"

def main():
    # Entrada de dados
    altura = float(input("Digite a altura do reservatório (em cm): "))
    largura = float(input("Digite a largura do reservatório (em cm): "))
    comprimento = float(input("Digite o comprimento do reservatório (em cm): "))
    consumo_diario = float(input("Digite o consumo médio diário (em litros/dia): "))

    # Cálculos
    capacidade_total = calcular_capacidade_reservatorio(altura, largura, comprimento)
    autonomia = calcular_autonomia(capacidade_total, consumo_diario)
    classificacao = classificar_consumo(autonomia)

    # Exibição dos resultados
    print(f"\nCapacidade total do reservatório: {capacidade_total:.2f} litros")
    print(f"Autonomia do reservatório: {autonomia:.2f} dias")
    print(f"Classificação do consumo: {classificacao}")

if __name__ == "__main__":
    main()
