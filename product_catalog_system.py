'''
An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. 
Each product type shares some common characteristics but also has unique features. The system should be able to display information 
about each product appropriately.
'''

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price: $", self.price)


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print("Author:", self.author)


class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print("Specifications:", self.specs)


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print("Size:", self.size)



if __name__ == "__main__":
   
    book = Book("B001", "Python Essentials", 79.99, "J. Doe")
    electronic = Electronic("E001", "Laptop", 599.99, "15-inch, 16GB RAM, 512GB SSD")
    clothing = Clothing("C001", "T-Shirt", 10.99, "Large")

    print("Book Info:")
    book.display_info()
    print("\nElectronic Info:")
    electronic.display_info()
    print("\nClothing Info:")
    clothing.display_info()
