from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an attribute
# It will also execute whatever code is within the property
print(item1.name)

# Example of encapsulation
item2 = Item("2ndItem", 800)

print(item2)
item2.apply_increment(0.1)

item2.send_email()


if __name__ == '__main__':
    pass
