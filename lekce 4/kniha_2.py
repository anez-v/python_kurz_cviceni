class Book:  
    def __init__(self, title, pages, prize, sold, costs):
        self.title = title
        self.pages = pages
        self.prize = prize
        self.sold = sold
        self.costs = costs

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stránek a stojí {self.prize}."

    def get_time_to_read(self, minutes_per_page = 4):
        time_to_read = (self.pages * minutes_per_page) / 60
        return f"Přečíst knihu {self.title} bude trvat přibližně {time_to_read} hodin."
    def profit(self):
        profit = self.sold * (self.prize - self.costs)
        return f"Kniha {self.title} má výnos celkem {profit}Kč"

    #jak zavolat ten profit? 
    def rating (self):
        profit = self.sold * (self.prize - self.costs)
        if profit >= 50000:
            return "Propadák!"
        elif profit >= 500000:
            return "Průměr"
        else:
            return "Bestseller!"


kniha_1 = Book ("Knížka1", 216, 399, 1012, 299)
kniha_2 = Book ("Knížka2", 110, 259, 546, 168)

print(kniha_1.rating())


        


kniha_1 = Book ("Knížka1", 216, 399, 1012, 299)
kniha_2 = Book ("Knížka2", 110, 259, 546, 168)

"""print(kniha_1.get_info())
print(kniha_1.get_time_to_read())"""

#Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
#Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". 
#Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".