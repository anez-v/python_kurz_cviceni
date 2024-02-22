#Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

#ceny_Kc = []
#for ingredience in recept["ingredience"]:
 #   ceny_Kc.append(ingredience [2])

#ceny = []
#for cena in ceny_Kc: 
 #   x = cena.strip("kč")
  #  x = float(x)
   # cena = x
#    ceny.append(x)

#celkova_cena = sum(ceny)
#print (celkova_cena)


# nebo lépe
celkova_cena = 0
for ingredience in recept["ingredience"]:
    cena_kc = ingredience[2]
    cena = float(cena_kc.strip("kč"))
    celkova_cena += cena 
print (celkova_cena)


