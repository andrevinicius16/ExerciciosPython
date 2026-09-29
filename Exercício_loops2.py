dia = input("Informe o dia da semana e a data: ")
quantidades_transacoes = int(input("Por favor, informe a quantidades de tranções que realizou ao longo do dia: "))
total_transacoes = 0
for transação in range(1, quantidades_transacoes + 1, 1):
    valor = float(input("Informe o valor da transação {}: ".format(transação)))
    total_transacoes = total_transacoes + valor
media = total_transacoes/quantidades_transacoes
print(f"No {dia}, foi gasto um total de R${total_transacoes}, com uma média de R${media} por transação.")
