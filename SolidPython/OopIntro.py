class Product:
    currency = "GBP"

    @classmethod
    def change_currency(cls, currency):
        cls.currency = currency

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self._stock = stock

    def is_available(self) -> bool:
        return self._stock > 0

    def sell(self, quantity: int) -> bool:
        if quantity <= 0 or quantity > self._stock:
            return False
        
        self._stock -= quantity
        return True
    @property
    def stock(self):
        return self._stock

    def final_price(self) -> float:
        return self.price


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity

class Order:
    def __init__(self, order_items: list[OrderItem]):
        self.order_items = order_items

    def total_price(self):
        final_price = 0
        for item in self.order_items:
            final_price += item.total_price()

        return final_price

class DiscountProduct(Product):
    def __init__(self, name, price, stock, discount_percent):
        super().__init__(name, price, stock)

        self.discount_percent = discount_percent

    def final_price(self):
        return self.price - (self.price * self.discount_percent / 100)



candle = Product('Candle', 10.00, 9)
rosie = Product('Rosie', 760.00, 13)
discount_candle = DiscountProduct('LX Candle', 20.00, 4, 30)
discount_rosie = DiscountProduct('Rosie brown colour', 49.00, 2, 15)
orders_list = [candle, discount_rosie, rosie, discount_candle]

for item in orders_list:
    print(item.final_price())
