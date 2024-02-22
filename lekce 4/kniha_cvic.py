class Book:  
    def __init__(self, title, pages, prize):
        self.title = title
        self.pages = pages
        self.prize = prize
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stránek a stojí {self.prize}."

    def get_time_to_read(self, minutes_per_page = 4):
        time_to_read = (self.pages * minutes_per_page) / 60
        return f"Přečíst knihu {self.title} bude trvat přibližně {time_to_read} hodin."
    
kniha_1 = Book ("Knížka1", 216, 399)
kniha_2 = Book ("Knížka2", 110, 259)

print(kniha_1.get_info())
print(kniha_1.get_time_to_read())