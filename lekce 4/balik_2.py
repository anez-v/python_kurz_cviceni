class Package:  
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
    def delivery_price(self):
        if self.weight <= 10:
            prize = 129
        elif self.weight <= 20:
            prize = 159
        else:
            prize = 359
        return f"Cena dopravy je {prize}Kč"
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"

balik_1 = Package ("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
balik_2 = Package ("Maiselova 7, Praha 1", 12.3, "doručen")

"""Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a
zaznamená tak jeho doručení. Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. 
Pokud ano, metoda vrátí zprávu "Balík již byl doručen". 
Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo"."""

print(balik_1.deliver())
print(balik_1)

print(balik_1.deliver())
print(balik_1)

print(balik_2.deliver())
print(balik_2)


