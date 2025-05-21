while True:
    resposta = input("Você gosta de Python? ").upper()
    
    if resposta == "EU GOSTO DE PYTHON":
        print("Resposta correta! Encerrando o programa.")
        break
    else:
        print("Essa não é a resposta correta, tente novamente.")
# O programa continua perguntando até que o usuário responda "EU GOSTO DE PYTHON".
# Quando a resposta correta é dada, o programa imprime "Resposta correta! Encerrando o programa." e sai do loop.