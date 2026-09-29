quantidades_alimentos = int(input("Por favor informe a quantidade de alimentos que voçê consimiu hoje: "))
total_calorias = 0
for alimento in range(1, quantidades_alimentos + 1, 1):
    caloria = int(input("Informe a quantidades de calorias consumidas do {} alimento: ". format(alimento)))
    total_calorias = total_calorias + caloria
print("Foram consumidas {} calorias ao longo do dia".format(total_calorias))