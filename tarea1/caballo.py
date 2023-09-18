movimientos = {
    0: [6, 4],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

# Usaremos memoización para almacenar los resultados calculados
memo = {}


def calcular(inicio, pasos, n):
    # Verificar si ya calculamos esto antes
    if (inicio, pasos, n) in memo:
        return memo[(inicio, pasos, n)]

    movs = 0
    if pasos == 0:
        return 1
    if n > 0:
        for siguiente in movimientos[inicio]:
            movs += calcular(siguiente, pasos - 1, n - 1)

    # Almacenar el resultado calculado en la memoización
    memo[(inicio, pasos, n)] = movs

    return movs


def totalizar(pasos, n):
    total = 0
    for i in range(10):
        total += calcular(i, pasos, n)
    return total


n = 100  # Especifica el número de movimientos
total_movements = totalizar(n, n)
print(f"Total de movimientos para {n} pasos: {total_movements}")