class cars:
    company = 0
    price = 0
    color = 0
    def car(self):
        print("car company - ",self.company)
        print("car price - ",self.price)
        print("car color - ",self.color)
        print("\n")
car1 = cars()
car1.company = "toyota"
car1.price = 15000000
car1.color = "white"
car1.car()

car2 = cars()
car2.company = "suzuki"
car2.price = 1200000
car2.color = "red"
car2.car()

car3 = cars()
car3.company = "wolswagon"
car3.price = 1400000
car3.color = "grey"
car3.car()
    
