def realizar_operacoes():
    # Entrada de dados
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    # Operações matemáticas
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    
    # Verificação para divisão
    if numero2 != 0:
        divisao = numero1 / numero2
        print(f"Resultado da divisão: {divisao:.2f}")
    else:
        print("Não é possível dividir por zero.")
    
    # Exibição dos resultados das outras operações
    print(f"Resultado da subtração: {subtracao:.2f}")
    print(f"Resultado da multiplicação: {multiplicacao:.2f}")

realizar_operacoes()
