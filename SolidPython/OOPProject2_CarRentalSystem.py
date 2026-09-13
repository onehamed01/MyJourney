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
        self.rented_vehicles_list:Vehicle = list[Vehicle]

    @classmethod
    def active_rental_limit(cls) -> int:
        return cls.active_rental_limit
    
    def rent_car(self, vehicle: Vehicle) -> bool:
        rent_car_method = vehicle.rented_car()
        if rent_car_method and len(self.rented_vehicles_list) <= self.active_rental_limit:
            self.rented_vehicles_list.append(vehicle)
            return rent_car_method
        
    def return_car(self, vehicle: Vehicle) -> bool:
        return_car_method = vehicle.return_car()
        if not return_car_method:
            self.return_car()
            return return_car_method 


class PremiumCustomer(Customer):
    active_rental_limit = 4
    def __init__(self, customer_name, customer_id) -> None:
        super().__init__(customer_name, customer_id)
        self.rented_vehicles_list = list[Vehicle]

    def rent_car(self, vehicle: Vehicle) -> bool:
        if len(self.rented_vehicles_list) <= self.active_rental_limit:
            return super().rent_car(vehicle)

class Company:
    pass

porsche = Vehicle('Porsche', 'Macan', 1200, True)
toyota = Vehicle('Toyota', 'Yaris', 340, True)
rolls_royce = LuxuryVehicle("Rolls-Royce", 'Culinan', 3600, True, 14)
benz = Vehicle('Mercedes-benz', 'SL 63', 639, True)
aston_martin = LuxuryVehicle('Aston Martin', 'DB 12', 2099, True, 33)

# Customers
hami = Customer('Hami Vand', 1002)
print(hami.rent_car(porsche))