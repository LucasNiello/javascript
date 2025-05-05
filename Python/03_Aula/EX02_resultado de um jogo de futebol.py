def verificar_resultado_jogo():
    # Entrada de dados
    gols_time1 = int(input("Digite o número de gols do primeiro time: "))
    gols_time2 = int(input("Digite o número de gols do segundo time: "))
    
    # Verificação do resultado
    if gols_time1 == gols_time2:
        print("Empate")
    elif gols_time1 > gols_time2:
        print("Vitória do primeiro time")
    else:
        print("Vitória do segundo time")

verificar_resultado_jogo()
