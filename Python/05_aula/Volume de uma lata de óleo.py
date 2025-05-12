# Constante PI
PI = 3.1416

# Entrada do raio e altura
raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))

# Cálculo do volume
volume = PI * (raio ** 2) * altura

# Saída
print(f"O volume da lata de óleo é: {volume:.4f}")
