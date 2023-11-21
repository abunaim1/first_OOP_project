from abc import ABC, abstractmethod
class Shop:
    product = []
    
    def __init__(self, product_name, price) -> None:
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def add_product(self):
        pass
        
        

class Product(Shop):
    def __init__(self, product_name, price, quantity) -> None:
        self.quantity = quantity
        super().__init__(product_name, price)

    def add_product(self):
        product = {'product_name': self.product_name, 'price': self.price, 'quantity': self.quantity}
        self.product.append(product)

    


# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
