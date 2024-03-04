class Package:  
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
    def delivery_price(self):
        if self.weight <= 10:
            price = 129
        elif self.weight <= 20:
            price = 159
        else:
            price = 359
        return f"Cena dopravy je {price}Kč"
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"

balik_1 = Package ("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
balik_2 = Package ("Maiselova 7, Praha 1", 12.3, "doručen")
