def calcular_juros_compostos(capital_inicial, taxa_juros, num_periodos):
    montante_final = capital_inicial * (1 + taxa_juros / 100) ** num_periodos
    juros_acumulados = montante_final - capital_inicial
    return montante_final, juros_acumulados

def menu():
    while True:
        print("Menu:")
        print("1. Calcular Juros Compostos")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            capital_inicial = float(input("Digite o valor do capital inicial: "))
            taxa_juros = float(input("Digite a taxa de juros (%) ao mês: "))
            num_periodos = int(input("Digite o número de períodos (meses): "))
            
            montante_final, juros_acumulados = calcular_juros_compostos(capital_inicial, taxa_juros, num_periodos)
            
            print(f"Montante Final: {montante_final:.2f}")
            print(f"Juros Acumulados: {juros_acumulados:.2f}")
        
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
