#Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
#Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. 
#Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. 
#Vyhodnoť, do které řady číslo náleží. 
#Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
#Funkce roulette vrací hodnotu výhry. 
#Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.

rady = [
[1, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]],
[2, [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]],
[3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]
]


import random

cislo_rady = (input("Na kterou řadu sázíte? "))
if cislo_rady not in ("1", "2", "3"):
    print("Číslo řady musí být 1 nebo 2 nebo 3!")
    exit()
sazka = (input("A kolik na to chcete vsadit? "))
cislo = random.randint(0, 36)
print(f"Na ruletě padlo: {cislo}")
      
if cislo in rady[0][1]:
    rada = 1
elif cislo in rady[1][1]:
    rada = 2
else:
    rada = 3

def roulette (cislo_rady, sazka):
    cislo_rady = int(cislo_rady)
    sazka = int(sazka)
    if rada == cislo_rady:
        vyhra = sazka * 2
        print(f"Vyhráváte {vyhra}")
    else:
        print("Nevyhráváte bohužel nic.")

roulette(cislo_rady, sazka)
   
     


