notas = 0
qnt_notas_info = 0

while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    if nota == -1:
        break
    notas = notas + nota
    qnt_notas_info += 1

if qnt_notas_info > 0:
    media = notas / qnt_notas_info
    print(f"A quantidade de notas informadas é: {qnt_notas_info}")
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")
