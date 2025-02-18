def get_numbers():
    """Získá libovolný počet čísel od uživatele."""
    pocet_cisel = int(input("Kolik čísel chcete zadat? "))
    cisla = []
    for i in range(pocet_cisel):
        cislo = float(input(f"{i + 1}. číslo: "))
        cisla.append(cislo)
    return cisla

def display_options():
    """Zobrazí uživateli možnosti operací."""
    print("""Máte tyto možnosti:
    (1) + pro sčítání
    (2) x pro násobení
    (3) průměr
    (4) minimum čísla
    (5) maximum čísla""")
    return input("Zadejte volbu: ")

def main():
    # Získání čísel
    cisla = get_numbers()
    # Zobrazení možností a získání volby
    otazka = display_options()

    # Zpracování volby
    if otazka == "1":
        print(f"Součet čísel: {sum(cisla)}")
    elif otazka == "2":
        soucin = 1
        for cislo in cisla:
            soucin *= cislo
        print(f"Součin čísel: {soucin}")
    elif otazka == "3":
        prumer = sum(cisla) / len(cisla) if cisla else 0
        print(f"Průměr čísel: {prumer}")
    elif otazka == "4":
        print(f"Minimum z čísel: {min(cisla)}")
    elif otazka == "5":
        print(f"Maximum z čísel: {max(cisla)}")
    else:
        print("Neplatný vstup. Zkuste to znovu.")

# Spuštění programu
if __name__ == "__main__":
    main()





# SPATNE # print(input("chcete tato cisla secist(+) nebo je vynasobit(x)?"))
# # if input == "+":
# #     print(c1 + c2 + c3)
# # elif input == "x":
# #     print(c1 * c2 * c3)
# # else:
# #     print("Neplatný vstup")