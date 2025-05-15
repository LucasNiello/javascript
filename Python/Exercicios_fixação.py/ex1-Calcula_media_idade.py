# IDADE MEDIA HOMENS E MULHERES
# Este programa calcula a idade média de homens e mulheres a partir de 10 entradas de idade e sexo.
# O programa também calcula a idade média do grupo total.



# Inicializando as variáveis
soma_idade_mulheres = 0
soma_idade_homens = 0
total_mulheres = 0
total_homens = 0
soma_idade_grupo = 0

# Lê a idade e o sexo de 10 pessoas
for i in range(10):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    
    soma_idade_grupo += idade
    
    if sexo == 'F':
        soma_idade_mulheres += idade
        total_mulheres += 1
    elif sexo == 'M':
        soma_idade_homens += idade
        total_homens += 1

# Calculando as idades médias
if total_mulheres > 0:
    media_idade_mulheres = soma_idade_mulheres / total_mulheres
else:
    media_idade_mulheres = 0

if total_homens > 0:
    media_idade_homens = soma_idade_homens / total_homens
else:
    media_idade_homens = 0

media_idade_grupo = soma_idade_grupo / 10  # O grupo tem 10 pessoas

# Imprimindo os resultados
print(f"Idade média das mulheres: {media_idade_mulheres:.2f}")
print(f"Idade média dos homens: {media_idade_homens:.2f}")
print(f"Idade média do grupo: {media_idade_grupo:.2f}")
 