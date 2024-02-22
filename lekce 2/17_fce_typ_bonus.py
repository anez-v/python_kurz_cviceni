
#Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu.
#Parametr breakfast je nepovinný a výchozí hodnota je False.
#Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price (persons, breakfast = False):
    cena_ubytko = int(persons) * 850 
    cena_snidane = 0
    if breakfast == True:
# stačí jenom "if breakfast:" to True už není nutný
       cena_snidane = int(persons) * 125
    cena_celkem = cena_ubytko + cena_snidane
    print(cena_celkem)

total_price (2, True)
total_price (3)