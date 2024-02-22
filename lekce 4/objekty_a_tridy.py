class Package:  
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

#"Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
    def delivery_price(self):
        if self.weight <= 10:
            prize = 129
        elif self.weight <= 20:
            prize = 159
        else:
            prize = 359
        return f"Cena dopravy je {prize}Kč"

balik_1 = Package ("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
balik_2 = Package ("Maiselova 7, Praha 1", 12.3, "doručen")

print(balik_2.get_info())
print (balik_2.delivery_price())


#Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. 
#Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč 
#a cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.


