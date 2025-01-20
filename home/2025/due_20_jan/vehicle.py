class Vehicle:
    def __init__(self, make, model, price, purchaseYear, miles):
        self.make = make
        self.model = model
        self.price = price
        self.purchaseYear = purchaseYear
        self.miles = miles
    
    def calculateSalesPrice(self):
        depreciation = (2025 - self.purchaseYear) * 10
        if self.miles >  50000:
            depreciation += 20
        elif self.miles > 30000:
            depreciation += 15
        elif self.miles > 20000:
            depreciation += 10
        elif self.miles > 10000:
            depreciation += 5
        return '£' + str(self.price*((100 - depreciation)/100))

class Car(Vehicle):
    def __init__(self, make, model, price, purchaseYear, miles):
        super().__init__(make, model, price, purchaseYear, miles)
    
    def calculateSalesPrice(self):
        depreciation = (2025 - self.purchaseYear) * 7.5
        if self.miles >  50000:
            depreciation += 20
        elif self.miles > 30000:
            depreciation += 15
        elif self.miles > 20000:
            depreciation += 10
        elif self.miles > 10000:
            depreciation += 5
        return '£' + str(self.price*((100 - depreciation)/100))

class Truck(Vehicle):
    def __init__(self, make, model, price, purchaseYear, miles):
        super().__init__(make, model, price, purchaseYear, miles)
    
    def calculateSalesPrice(self):
        depreciation = (2025 - self.purchaseYear) * 12.5
        if self.miles >  50000:
            depreciation += 20
        elif self.miles > 30000:
            depreciation += 15
        elif self.miles > 20000:
            depreciation += 10
        elif self.miles > 10000:
            depreciation += 5
        return '£' + str(self.price*((100 - depreciation)/100))

lambo = Truck('lamborghini', 'aventador', 100000, 2020, 17000)
print(lambo.calculateSalesPrice())
print(lambo.make)