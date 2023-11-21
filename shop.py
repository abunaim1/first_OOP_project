class Product:
    def __init__(self, product_name, price, quantity) -> None:
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    def __repr__(self) -> str:
        return f'Product Name: {self.product_name}, Price: {self.price}, Quantity: {self.quantity}'

class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name, price, quantity):
        product = Product(product_name, price, quantity)
        self.products.append(product)
        
    def __repr__(self) -> str:
        print("Our Products")
        for product in self.products:
            print(product)
        return f'All done'   

kamal = Shop('Kamal Banana Shop')
kamal.add_product('Banana Khete moja', 10, '2 hali')
kamal.add_product('Tetul Tok', 22, '2kg')
kamal.add_product('Anarosh', 33, '10 piece')
kamal.add_product('Kumrar Bichi', 44, '40kg')

print(kamal)
        

