
class Item: 
    def __init__(self, title, prize):
        self.title = title
        self.price = prize
    def get_time_to_read (self):
        pass

class Book(Item):  
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def get_time_to_read(self, minutes_per_page = 4):
        time_to_read = (self.pages * minutes_per_page) / 60
        # return f"Přečíst knihu {self.title} bude trvat přibližně {time_to_read} hodin."
        return time_to_read
    
kniha_1 = Book ("Knížka1", 216, 399)
kniha_2 = Book ("Knížka2", 110, 259)

class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator
    def get_time_to_read(self):
        #return f"Poslechnout knihu {self.title} bude trvat {self.duration_in_hours} hodin."
        return self.duration_in_hours
    

book_1 = AudioBook("Problém tří těles",299, 14.4, "Zbyšek Horák")
book_2 = Book("Kadet Hornblower", 399, 242)

total_time = book_1.get_time_to_read() + book_2.get_time_to_read()
print(total_time)