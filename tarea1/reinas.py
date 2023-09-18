def solve_n_queens(n):
    def is_safe(board, row, col):
        # Comprueba si es seguro colocar una reina en la posición (row, col)
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def backtrack(col):
        nonlocal count
        if col == n:
            count += 1
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(col + 1)

    count = 0
    board = [-1] * n
    backtrack(0)
    return count

# Ejemplo de uso
for n in range(1, 16):
    count = solve_n_queens(n)
    print(f"Número de soluciones para {n}-reinas: {count}")