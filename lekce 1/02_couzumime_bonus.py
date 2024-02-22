#1
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

znamky = []

for predmet in school_report:
   if predmet[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
     znamka = predmet[1]
     znamky.append(znamka)
print(znamky)

average = sum (znamky) / len(znamky)

print(f"Průměrná známka z relevantních předmětů je {average}.")

#2
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

#Kolik přišlo mužů a kolik žen?
pohlavi = []
for rod_ci in rodna_cisla:
    rod_ci = rod_ci.split("/") 
    bbb = list(rod_ci[0])
    ccc = int(bbb[2])
    if ccc > 4:
        pohlavi.append ("žena")
    else:
        pohlavi.append ("muž")
print(pohlavi)

muz = 0
zena = 0
for poh in pohlavi:
   if poh == "muž":
      muz = muz + 1
   else:
      zena = zena +1
print(f"Přišlo {zena} žen/a a {muz} muž/ů.")

#Kdy se narodil nejstarší a kdy nejmladší pacient?
data = []
for rod_ci in rodna_cisla:
    rod_ci = rod_ci.split("/") 
    datum = rod_ci [0]
    data.append(datum)
print(data)


for vek in data:
   

print (max(data))
print (min(data))
