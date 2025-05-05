def verificar_aprovacao():
    # Entrada de dados
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Cálculo da média
    media = (nota1 + nota2) / 2
    
    # Verificação da aprovação
    if media >= 6:
        print("Aprovado!")
    else:
        print("Reprovado!")

verificar_aprovacao()
