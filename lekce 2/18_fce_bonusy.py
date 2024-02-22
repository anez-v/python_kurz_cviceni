#Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.

#Návod:
#Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
#Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami
#Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat


numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]

nejdelsi = 0

for cislo in numbers:
    dlouhy = (len(str(cislo)))
    if nejdelsi < dlouhy:
        nejdelsi = dlouhy
print(nejdelsi)


def zarovnat (znak, cislo):
    dlouhy = (len(str(cislo)))
    znaku = znak * (nejdelsi - dlouhy)
    print(znaku, cislo)

zarovnat(" ", 88)

for cislo in numbers:
    zarovnat (" ", cislo)

    