from item import Item
from keyboard import Keyboard

# item1 = Item("MyItem", 750)

# Setting an Attribute
# item1.name = "OtherItem"

# Getting an attribute
# It will also execute whatever code is within the property
# print(item1.name)

# Example of encapsulation for price attribute
# item2 = Item("2ndItem", 800)
# item2.apply_increment(0.1)
# print(item2)

# Abstraction example
# item2.send_email()

item1 = Keyboard("Keyboard", 1000, 10)
item1.apply_discount()
print(item1.price)

if __name__ == '__main__':
    pass
