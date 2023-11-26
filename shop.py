class Product:
    def __init__(self, product_name, price, quantity) -> None:
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    def __repr__(self) -> str:
        return f'Product Name: {self.product_name}, Price: {self.price}, Quantity: {self.quantity}'

class Shop:
    def __init__(self) -> None:
        self.products = []
    
    def add_product(self, product_name, price, quantity):
        product = Product(product_name, price, quantity)
        self.products.append(product)

    def buy_product(self, name, quantity):
        for product in self.products:
            if product.product_name == name and product.quantity >= quantity:
                print(f'Here is your product: {name} and total price is {quantity*product.price}')
    def __repr__(self) -> str:
        return f'Dhonnobad abar ashben, abar ashben'
            
apple = Shop()
apple.add_product('iphone Xs', 2500, 100)
apple.add_product('iphone 12', 23542, 12)
apple.add_product('iphone 13', 2534, 10)
apple.add_product('iphone 15 pro', 542, 90)
apple.add_product('iphone 22 pro', 3252, 120)

apple.buy_product('iphone Xs', 5)

print(apple)

        

