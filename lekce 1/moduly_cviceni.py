#1 zaokrouhlovani 
import math
x = 4.24
print(math.ceil (x))
print(math.floor (x))

#2
#prumer z CJ, AJ, Mat, Fyz

import statistics
vysvedceni = [
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

# vytvorit prazdny seznam
znamky = []

# pomocí cyklu vložit do nového seznamu známky z CJ, AJ, Mat, Fyz
for predmet in vysvedceni:
   if predmet[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
     znamka = predmet[1]
     znamky.append(znamka)
   #když dám print už sem, tak to bude vypisovat postupně a ne rovnou celý
print(znamky)

# použij metodu statistics.mean() k výpočtu průměru
print (statistics.mean(znamky))

# zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů
print("Nejlepsi znamka", (min(znamky)))
print("Nejhorsi znamka", (max(znamky)))



#nejčastější odpověď 
votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]

print (statistics.mode (votes))
