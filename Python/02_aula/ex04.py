def calcular_retangulo():
    # Solicita a base e a altura do retângulo
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    
    # Calcula o perímetro e a área
    perimetro = 2 * (base + altura)
    area = base * altura
    
    # Exibe o resultado
    print(f"O perímetro do retângulo é {perimetro} e a área é {area}")

calcular_retangulo()
