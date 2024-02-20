from item import Item
from phone import Phone

Item.instantiate_from_csv()


if __name__ == '__main__':
    print(Item.all)


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
