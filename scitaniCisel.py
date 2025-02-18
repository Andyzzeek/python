def scitaniCisel(cisla):
    if len(cisla) == 0:  # Když je seznam prázdný, vrátí 0
        return 0
    prvniCislo = cisla[0]  # První číslo v seznamu
    zbytek = cisla[1:]
    return prvniCislo + scitaniCisel(zbytek)

print(scitaniCisel([1, 9, 3, 4, 5]))
c = 5
print("idk", c)