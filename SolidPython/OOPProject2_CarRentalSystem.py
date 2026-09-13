class Vehicle:
    def __init__(self, brand: str, model: str, daily_price: float, availability: bool) -> None:
        self.brand = brand
        self.model = model
        self.daily_price = daily_price
        self._availability = availability

    @property
    def availability(self) -> bool:
        return self._availability
    
    def rented_car(self):
        if self._availability:
            self._availability = False
            return True

    def return_car(self):
        if not self._availability:
            self._availability = True
            return True

    def daily_price(self, day_count: int):
        return self.daily_price * day_count
    

class LuxuryVehicle(Vehicle):
    def __init__(self, brand: str, model: str, daily_price: float, availability: bool, daily_percentage_cost) -> None:
        super().__init__(brand, model, daily_price, availability)
        self.daily_percentage_cost = daily_percentage_cost

    def daily_price(self, day_count: int) -> float:
        return ((self.daily_percentage_cost / 100) * self.daily_price) * day_count

class Customer:
    active_rental_limit = 2
    def __init__(self, customer_name, customer_id) -> None:
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.rented_vehicles:Vehicle = list[Vehicle]

    

class PremiumCustomer(Customer):
    active_rental_limit = 4

class Company:
    pass