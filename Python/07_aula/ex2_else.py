# O else é usado quando a condição se torna falsa.

x=0
while x < 5:
    print(x)
    x = x+1
else:
    print("Acabou.")
# O else é executado quando o loop termina normalmente, ou seja, não foi interrompido por um break.
# O loop while continua enquanto x for menor que 5. Quando x atinge 5, o loop termina e o else é executado.
# O mesmo vale para o loop for.