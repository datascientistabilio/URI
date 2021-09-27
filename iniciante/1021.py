# Notas e Moedas 1021
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtd_cedulas = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, nota))
    valor -= qtd_cedulas * nota

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = int(round(valor,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    valor -= round(qtd_moedas * moeda, 2)