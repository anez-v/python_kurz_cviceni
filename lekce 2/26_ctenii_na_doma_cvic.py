purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]

#Útraty jednotlivých spolubydlících si budeme ukládat do nového slovníku. 
#Musíme si tedy nejprve vysvětlit, jak ověřit, jestli nějaká hodnota už ve slovníku je. 
#Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. 
#Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.

sum_per_person = {}
for item in purchase_list:
    person = item["Jméno"]
    value = item["Částka"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

#Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. 
#K tomu můžeme využít cyklus for. Zde je pouze jeden malý rozdíl.

total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

#Jako poslední krok zbývá určení průměrné hodnoty na osobu. 
#Zde opět využijeme funkci len, která umí pracovat i se slovníky.

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

#cviceni
#Dopiš cyklus, který projde slovník sum_per_person a pro každého ze spolubydlících vypíše,
#kolik by měl doplatit (pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).

for person, value in sum_per_person.items():
    if value < average_value:
        doplatek = round(average_value - value)
        print(f"{person} by měl doplatit {doplatek}.")
    elif value > average_value:
        přeplatek = round(value - average_value)
        print(f"{person} by měl dostat zpět {přeplatek}.")
    else:
        print(f"{person} to nemusí řešit.")
