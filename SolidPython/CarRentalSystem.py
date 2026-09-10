class Vehicle:
    def __init__(self, brand: str, model: str, daily_rental_price: float, availability: bool) -> None:
        self.brand = brand
        self.model = model
        self.daily_rental_price = daily_rental_price
        self._availability = availability

    @property
    def availibility(self) -> bool:
        return self._availability
    
    def rent_vehicle(self) -> None:
        if self._availability == False:
            return False
        self._availability = False

    def return_wehicle(self) -> None:
        if self._availability == True:
            return False
        self._availability = True
