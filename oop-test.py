
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

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


# Example of modifying the discount after creating the instance
# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.__dict__)  # All the attributes for the class level
# print(item1.__dict__)  # All the attributes for the instance level

# print(item1.name)
# print(item1.calculate_total_price())

# print(item2.name)
# print(item2.calculate_total_price())
