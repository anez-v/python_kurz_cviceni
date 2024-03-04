class Package:  
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
   
    def delivery_price(self):
        if self.weight <= 10:
            price = 129
        elif self.weight <= 20:
            price = 159
        else:
            price = 359
        return price

def total_weight(package_list):
    total_weight = 0
    for package in package_list: 
        total_weight += package.weight
    return total_weight



package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

print(total_weight(package_list))

#Využij balíky v seznamu package_list a spočítej celkové náklady na jejich přepravu.
#Náklady na přepravu jednoho balíku zjistíš voláním metody delivery_price().
total_del_price = 0
for package in package_list:
    total_del_price += package.delivery_price()
print(total_del_price)