#Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum()).

list = [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]
soucet = 0 
for num in list:
    soucet = soucet + num
print(soucet)

seznam = [22, 3, 47, 8, 20, 35, 16, 16, 34, 7, 65, 87, 134]

#Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max()).
m_cislo = 0 
for cislo in seznam:
    if m_cislo < cislo:
       m_cislo = cislo
print(m_cislo)

#Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu.
for cislo in seznam:
    if cislo % 2 == 0:
        print(cislo)

#Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam se sudými čísly a nový seznam s lichými čísly z původního seznamu.
suda = []
for cislo in seznam:
    if cislo % 2 == 0:
        suda.append (cislo)
print(suda)

licha = []
for cislo in seznam:
    if cislo % 2 == 1:
        licha.append (cislo)
print(licha)

#Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů. Výsledné pořadí prvků musí být zachováno.
bez_duplikatu = []
for cislo in seznam:
    if cislo not in bez_duplikatu:
        bez_duplikatu.append (cislo)
print(bez_duplikatu)

