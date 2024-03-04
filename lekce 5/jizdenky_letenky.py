class Ticket:
    def __init__ (self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket): 
    def __init__ (self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class 
    def get_price(self):
        if self.fare_class == "business":
            bussines_price = self.basic_price * 1.3
            return bussines_price
        elif self.fare_class == "economy":
            return self.basic_price
        
class PlaneTicket (TrainTicket):
    def __init__ (self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages 
    
    def get_price(self):
        if self.fare_class == "business":
            bussines_price = self.basic_price * 1.5 + (self.checkout_luggages * 2000)
            return bussines_price
        elif self.fare_class == "economy":
            economy_luggage = self.basic_price + (self.checkout_luggages * 2000)
            return economy_luggage

train_1 = TrainTicket (150, 23, "business")
train_2 = TrainTicket (150, 23, "economy")

plane_1 = PlaneTicket (6000, 45, "economy", 1)
plane_2 = PlaneTicket (6000, 45, "business", 1)

print(plane_1.get_price())

total_price = (train_1.get_price()) + (plane_1.get_price())
print(total_price)