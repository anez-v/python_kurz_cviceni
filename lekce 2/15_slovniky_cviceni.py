#například český jazyk, matematiku a dějepis
vysvedceni = {"český jazyk": 2, "matematika": 1, "dějepis": 3}
for predmet in vysvedceni:
    print(predmet, vysvedceni[predmet])

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
#Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů
#U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100

sales ["Noc, která mě zabila"] = 0
sales ["Vrah zavolá v deset"] += 100
#sales ["Vrah zavolá v deset"] += 100 je to samé jako bych psala:
#sales ["Vrah zavolá v deset"] = sales ["Vrah zavolá v deset"] + 100

print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
#Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku
#Zkontroluj, zda je číslo lístku ve slovníku. 
#Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrá

cislo_listku = input("Zadej číslo lístku:")
cislo_listku = int(cislo_listku)
vyhra = 0
for cislo in tombola:
    if cislo == cislo_listku:
       print(tombola [cislo_listku])
       vyhra = 1

if vyhra == 0:
    print("Bohužel nevyhráváš nic.")