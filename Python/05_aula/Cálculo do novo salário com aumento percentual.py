# Entrada do salário atual e percentual de aumento
salario = float(input("Digite o salário atual: "))
percentual = float(input("Digite o percentual de aumento (%): "))

# Cálculo do salário atualizado
novo_salario = salario + (salario * percentual / 100)

# Saída
print(f"O novo salário é: R$ {novo_salario:.2f}")
