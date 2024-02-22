pisemka= [
    ["A", [9, 7, 8, 5]],
    ["B", [5, 3, 6, 6]],
    ["C", [8, 4, 9, 7]],
    ["D", [8, 5, 4, 8]],
    ["E", [10, 6, 10, 7]]
    ]

print(sum(pisemka [0][1]))
#znamky jednotlivych studentu
for student in pisemka:
    soucet_bodu = sum(student [1])
    if soucet_bodu < 20:
        print (student [0],"5")
    elif soucet_bodu < 26:
        print(student [0],"4")
    elif soucet_bodu < 32:
        print(student [0], "3")
    elif soucet_bodu < 36:
        print(student [0],"2")
    else:
        print(student [0],"1")

#dvourozmerny seznam 
znamky = []

for student in pisemka:
    soucet_bodu = sum(student [1])
    if soucet_bodu < 20:
        znamka = 5
    elif soucet_bodu < 26:
        znamka = 4
    elif soucet_bodu < 32:
        znamka = 3
    elif soucet_bodu < 36:
        znamka = 2
    else:
        znamka = 1
    jmeno = student[0]
    znamky.append([jmeno, znamka])
print(znamky)


#pruměrne body jednotlivych otazek 
cislo_otazky = 0
prumery = []
for otazka_cislo in [0, 1, 2, 3]:
    bodiky =[]
    for student in pisemka:
        otazka = student[1][otazka_cislo] 
        bodiky.append(otazka)
    soucet = sum(bodiky)
    prumer = soucet / len(pisemka)
    cislo_otazky = cislo_otazky + 1
    print(cislo_otazky, prumer)

    prumery.append(prumer)
print(prumery)

#maximální a minimální průměr
print (max(prumery))
print (min(prumery))

#nejvyšší průměr (tak aby se zobrazil i s číslem otázky)
m = 0
cislo_otazky = 1
m_cislo_otazky = 0
for ci in prumery:
    if m < ci:
        m_cislo_otazky = cislo_otazky
        m = ci
    cislo_otazky = cislo_otazky + 1
print(m_cislo_otazky, m)

#nejnižší průměr (tak aby se zobrazil i s číslem otázky)
mi = m
cislo_otazky = 1
mi_cislo_otazky = 0
for ci in prumery:
    if mi > ci:
        mi_cislo_otazky = cislo_otazky
        mi = ci
    cislo_otazky = cislo_otazky + 1
print(mi_cislo_otazky, mi)