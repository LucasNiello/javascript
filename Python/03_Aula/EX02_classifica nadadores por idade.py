def classificar_nadador():
    # Entrada de dados
    idade = int(input("Digite a idade do nadador: "))
    
    # Classificação
    if 5 <= idade <= 7:
        categoria = "Infantil A"
    elif 8 <= idade <= 11:
        categoria = "Infantil B"
    elif 12 <= idade <= 13:
        categoria = "Juvenil A"
    elif 14 <= idade <= 17:
        categoria = "Juvenil B"
    else:
        categoria = "Adulto"
    
    # Exibição do resultado
    print(f"O nadador está na categoria: {categoria}")

classificar_nadador()
