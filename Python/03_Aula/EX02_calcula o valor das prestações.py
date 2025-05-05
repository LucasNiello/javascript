def calcular_prestacoes():
    # Entrada de dados
    valor_compra = float(input("Digite o valor total da compra: "))
    num_prestacoes = int(input("Digite o número de prestações: "))
    
    # Cálculo do valor das prestações
    valor_prestacao = valor_compra / num_prestacoes
    
    # Exibição do resultado
    print(f"O valor de cada prestação é: R${valor_prestacao:.2f}")

calcular_prestacoes()
