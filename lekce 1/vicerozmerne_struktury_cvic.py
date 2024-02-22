vysledky = [
    ["Brunner Radek", [3, 0, 9]], 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]

#1
#čas prvniho a druheho ve dvou promennych v minutach a spocitat rozdil 
print(vysledky [0][1][0])
prvni = ((vysledky [0][1][0]) * 60)+(vysledky [0][1][1])
druhy = ((vysledky [1][1][0]) * 60)+(vysledky [1][1][1])
rozdil = druhy - prvni 
print(rozdil)

# ALE CO VTEŘINY??
print(vysledky [0][1][0])
prvni = float ((((vysledky [0][1][0]) * 3600)+((vysledky [0][1][1])*60)+ (vysledky [0][1][2])) / 60)
druhy = float ((((vysledky [1][1][0]) * 3600)+((vysledky [1][1][1])*60)+ (vysledky [1][1][2])) / 60)
rozdil = druhy - prvni
print(rozdil)

#2
# seznam jmeno a cas v minutach jako desetinne c. (cyklus a append)
poradi = []
kolikaty = 1
for bezec in vysledky:
   
    cas = bezec [1] 
    cas = float (((cas [0] * 3600) + (cas [1]*60)+ (cas[2])) / 60)
    rozdil = cas - prvni
    poradi.append([kolikaty, rozdil])
    kolikaty = kolikaty + 1
    

print (poradi)
print(vysledky)