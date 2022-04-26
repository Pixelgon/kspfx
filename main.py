from baseconvert.baseconvert import base

origin = open("01.in", "r") # Nacetem file cislem
output = open("01.out", "w") # Nactem/vytvorime file na output

num = tuple(map(int, origin.readline().strip())) # precteme vstup, prevedeme na tuple
zaklad_soustavy = 2
zaklad_soustavy_max = 0
pocet_nul_max = 0
print("Probíha výpočet, čekejte prosím...")
while True:
    # prevadime cislo do určite soustavy
    kolekce = base(num, 10, zaklad_soustavy)
    pocet_nul = 0
    zaklad_soustavy = zaklad_soustavy + 1
    for i in kolekce: # Pocitame nuly
        if i == 0:
            pocet_nul = pocet_nul + 1
        else:
            pocet_nul = 0
        # Pokud je cislo v kolekci viceciferne
        if len(str(i)) >= 2:
            tupi = [int(z) for z in str(i)]
            for y in tupi:
                if y == 0:
                    pocet_nul = 0 + 1
                else:
                    pocet_nul = 0
    # Pokud je pocet nul vyssi nez nez nejvetsi pocet nul předchozího cisla
    if pocet_nul >= pocet_nul_max:
        pocet_nul_max = pocet_nul
        zaklad_soustavy_max = zaklad_soustavy
    # Pokud je nejvetsi pocet nul vetsi nebo rovno delce kolekce
    if len(kolekce) <= pocet_nul_max:
        output.write(str(zaklad_soustavy_max - 1))
        print("Hotovo!")
        break

origin.close()
output.close()
