def somatorio(n):
    soma = 0

    for i in range(n+1):
        soma += i

    return soma

print(somatorio(5))