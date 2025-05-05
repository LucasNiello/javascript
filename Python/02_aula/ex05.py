def calcular_prestacao():
    # Solicita o valor, a taxa e o tempo ao usuário
    valor = float(input("Digite o valor da compra: "))
    taxa = float(input("Digite a taxa de juros: "))
    tempo = int(input("Digite o tempo de atraso em dias: "))
    
    # Calcula a prestação em atraso
    prestacao = valor + (valor * (taxa / 100) * tempo)
    
    # Exibe o valor da prestação
    print(f"O valor da prestação em atraso é: R${prestacao:.2f}")

calcular_prestacao()
