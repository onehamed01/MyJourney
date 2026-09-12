class Vehicle:
    def __init__(self, brand: str, model: str, daily_rental_price: float, availability: bool) -> None:
        self.brand = brand
        self.model = model
        self.daily_rental_price = daily_rental_price
        self._availability = availability

    @property
    def availability(self) -> bool:
        return self._availability

    def rent_vehicle(self) -> bool:
        if not self._availability:
            return False
        self._availability = False
        return True
    
    def calculate_daily_price(self, count_date: int) -> float:
        return self.daily_rental_price * count_date
    
    def return_vehicle(self) -> bool:
        if self._availability:
            return False
        self._availability = True
        return True
    
class LuxuryVehicle(Vehicle):
    def __init__(self, brand, model, daily_rental_price, availability, luxury_percentage) -> None:
        super().__init__(brand, model, daily_rental_price, availability)
        self.luxury_percentage = luxury_percentage
    
    def calculate_daily_price(self, count_date: int) -> float:
        calculate_one_day = ((self.luxury_percentage / 100) * self.daily_rental_price) + self.daily_rental_price
        return calculate_one_day * count_date

porsche = Vehicle('Porsche', '911', 1000, True)
porsche_macan = LuxuryVehicle(
    'Porsche',
    'Macan',
    3000,
    True,
    13
)
print(porsche_macan.calculate_daily_price(4))