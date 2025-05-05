def classificar_temperatura(temperatura):
    """Classifica a temperatura de acordo com os critérios fornecidos"""
    if temperatura < 35.0:
        return "Estado de hipotermia"
    elif temperatura < 37.2:
        return "Temperatura normal"
    elif 37.2 <= temperatura < 38.0:
        return "Estado febril"
    elif 38.0 <= temperatura < 39.0:
        return "Febre"
    else:
        return "Febre alta"

def main():
    total_pessoas = 0
    soma_temperaturas = 0.0

    while True:
        # Solicita a temperatura do paciente
        try:
            temperatura = float(input("Digite a temperatura corporal (ou 'sair' para encerrar): "))
        except ValueError:
            print("Entrada inválida! Para encerrar, digite 'sair'.")
            break

        # Classificação da temperatura
        classificacao = classificar_temperatura(temperatura)
        print(f"Classificação: {classificacao}")

        # Atualiza o contador de pessoas e a soma das temperaturas
        total_pessoas += 1
        soma_temperaturas += temperatura

    if total_pessoas > 0:
        media_temperaturas = soma_temperaturas / total_pessoas
        print(f"\nQuantidade total de pessoas analisadas: {total_pessoas}")
        print(f"Média geral das temperaturas: {media_temperaturas:.2f} °C")
    else:
        print("Nenhuma temperatura foi registrada.")

if __name__ == "__main__":
    main()
