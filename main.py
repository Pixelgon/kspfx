from baseconvert.baseconvert import base

origin = open("01.in", "r")
output = open("01.out", "w")

num = tuple(map(int, origin.readline().strip()))
zaklad_soustavy = 2
zaklad_soustavy_max = 0
pocet_nul_max = 0
while True:
    copynum = num
    kolekce = base(num, 10, zaklad_soustavy)
    pocet_nul = 0
    zaklad_soustavy = zaklad_soustavy + 1
    print(kolekce)
    print(zaklad_soustavy)
    for i in kolekce:
        if i == 0:
            pocet_nul = pocet_nul + 1
        else:
            pocet_nul = 0
        if len(str(i)) >= 2:
            tupi = [int(z) for z in str(i)]
            for y in tupi:
                if y == 0:
                    pocet_nul = 0 + 1
                else:
                    pocet_nul = 0
    print(pocet_nul)
    if pocet_nul >= pocet_nul_max:
        pocet_nul_max = pocet_nul
        zaklad_soustavy_max = zaklad_soustavy
    if len(kolekce) <= pocet_nul_max:
        output.write(str(zaklad_soustavy_max - 1))
        break

origin.close()
output.close()
