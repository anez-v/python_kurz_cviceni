


school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

#Napiš program, který spočte průměrnou známku ze všech předmětů.
celkem = 0
for znamka in school_report.values():
    celkem += znamka 
prumer = celkem/len(school_report.values())
print(prumer)

#Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

