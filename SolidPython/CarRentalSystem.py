class Vehicle:
    def __init__(self, brand: str, model: str, daily_rental_price: float, availability: bool) -> None:
        self.brand = brand
        self.model = model
        self.daily_rental_price = daily_rental_price
        self._availability = availability

    @property
    def availablity(self) -> bool:
        return self._availability

    def rent_vehicle(self) -> bool:
        if self._availability == False:
            return False
        self._availability = False
    
    def calculate_daily_price(self, count_date: int) -> float:
        return self.daily_rental_price * count_date
    
    def return_vehicle(self) -> bool:
        if self._availability == True:
            return False
        return True
    
class LuxuryVehicle(Vehicle):
    def __init__(self, brand, model, daily_rental_price, availability, luxury_precentage) -> None:
        super().__init__(brand, model, daily_rental_price, availability)
        self.luxury_precentage = luxury_precentage
    
    def calculate_daily_price(self, count_date: int) -> float:
        return (100 / self.luxury_precentage) * (count_date * self.daily_rental_price)

porsche = Vehicle('Porsche', '911', 1000, True)
porsche_macan = LuxuryVehicle(
    'Porsche',
    'Macan',
    3000,
    True,
    13
)
print(porsche_macan.calculate_daily_price(4))