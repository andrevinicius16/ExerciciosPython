numero_fibonacci = int(input("Por favor digite um número inteiro: "))
anterior1 = 1
anterior2 = 2
for n_elemento in range(1, numero_fibonacci + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_fibonacci == atual:
        print("Ação bem sucedida")
        break
    elif numero_fibonacci < atual:
        print("Ação falhou")
        break
