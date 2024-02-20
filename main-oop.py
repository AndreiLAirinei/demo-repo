from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an attribute
# It will also execute whatever code is within the property
print(item1.name)

if __name__ == '__main__':
    pass
