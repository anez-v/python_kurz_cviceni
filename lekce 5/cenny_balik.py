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
        return price

    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"

class Valuable_package(Package):
    def __init__ (self, address, weight, state, value):
         super().__init__(address, weight, state,)
         self.value = value
    def __str__(self):
        return super().__str__() + f"Hodnota balíku je: {self.value}."
    def delivery_price(self):
        return super().delivery_price()+ (self.value * 0.05)
    
package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
cenny_balik1 = Valuable_package("Vydrník svatého Drába 13", 0.5, "nedoručen", 1200)

print(cenny_balik1.delivery_price())


