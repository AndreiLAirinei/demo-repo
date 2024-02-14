
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than 0!"

        # Assign to self object
        # print(f"An instance created: {name}"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 4)

print(Item.__dict__)  # All the attributes for the class level
print(item1.__dict__)  # All the attributes for the instance level

# print(item1.name)
# print(item1.calculate_total_price())

# print(item2.name)
# print(item2.calculate_total_price())
