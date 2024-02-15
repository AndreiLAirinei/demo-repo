import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than 0!"

        # Assign to self object
        # print(f"An instance created: {name}"
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than 0!"

        # Assign to self object
        # print(f"An instance created: {name}"
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        Item.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1



# Item.instantiate_from_csv()
# print(Item.all)


# Separating every instance by an attribute, using a for loop
# for instance in Item.all:
#    print(instance.name)


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
