#Napiš funkci spocitej_pokutu(), která bude mít dva parametry - pocet_naprav (počet náprav vozidla) a hmotnost (v tunách). 
#Funkce na základě těchto parametrů vypočte výši pokuty a vráti ji jako celé číslo.

#Pokud je limit překročen, platí provozovatel pokutu 1000 Kč za každou tunu, o které je vozidlo těžší.
#Počet náprav	Maximální dovolená hmotnost v tunách
#2	            18
#3	            25
#4	            32
#5	            48

def spocitej_pokutu (pocet_naprav, hmotnost):
    if pocet_naprav == 2 and hmotnost > 18:
        hmotnost_navic = hmotnost - 18
    if pocet_naprav == 3 and hmotnost > 25:
        hmotnost_navic = hmotnost - 25
    if pocet_naprav == 4 and hmotnost > 32:
        hmotnost_navic = hmotnost - 32
    if pocet_naprav == 5 and hmotnost > 48:
        hmotnost_navic = hmotnost - 48
    pokuta = hmotnost_navic * 1000
    return (pokuta)

print(spocitej_pokutu(4, 34))

vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]

celkem_pokuty = 0
for auto in vazeni:
    celkem_pokuty = celkem_pokuty + spocitej_pokutu (*auto)
print(celkem_pokuty)


