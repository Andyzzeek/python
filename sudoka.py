import random

sudoka = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# for num in sudoka: 














# Funkce pro kontrolu, zda je číslo platné
def is_valid(sudoku, row, col, num):
    # Zkontroluj řádek
    if num in sudoku[row]:
        return False
    # Zkontroluj sloupec
    if num in [sudoku[i][col] for i in range(9)]:
        return False
    # Zkontroluj 3x3 blok
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

# Doplň prázdná pole náhodnými čísly (1-9), která splňují pravidla Sudoku
for i in range(9):
    for j in range(9):
        if sudoka[i][j] == 0:
            valid_number_found = False
            while not valid_number_found:
                rand_num = random.randint(1, 9)
                if is_valid(sudoka, i, j, rand_num):
                    sudoka[i][j] = rand_num
                    valid_number_found = True

# Výpis výsledné mřížky
print("Generovaná mřížka Sudoku:")
for row in sudoka:
    print(row)