class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)


# Usage
p1 = Product("Laptop", 50000)
print(p1.name)
print(p1.price)

p2 = Product("Mouse", 500)
print(p2.name)
print(p2.price)

order = Order()
order.add_item(p1)
order.add_item(p2)

print(order.total())