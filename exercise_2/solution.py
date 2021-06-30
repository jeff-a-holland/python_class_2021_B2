#!/Users/jeff/.pyenv/shims/python

class Item(object):
    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        self.price = price

    def __iter__(self):
        return iter((self.quantity, self.measure, self.name, self.price))

class Cart(object):
    def __init__(self):
        self.cart_list = []

    def add(self, cart_item):
        self.cart_list.append(cart_item)

    def __format__(self, format):
        tmp_str = ''
        tmp_list = []
        if (format == 'short'):
            for value in self.cart_list:
                tmp_list.append(value.name)
            tmp_str = ', '.join(tmp_list)
        elif (format == 'long'):
            for value in self.cart_list:
                tmp_str += f"{value.quantity:5} {value.measure:10}" \
                           f"{value.name} @ ${value.price:.2f}..." \
                           f"${value.quantity*value.price:.2f}\n"
        return tmp_str

cart = Cart()
cart.add(Item(1, 'hardcover', 'book', 30))
cart.add(Item(2, 'tube', 'toothpaste', 4))
cart.add(Item(5, 'silver', 'spoon', 5))
cart.add(Item(2.5, 'boxes', 'apples', 5))

print(f"\nYour cart contains: {cart:short}\n")
print(f"Your cart:\n{cart:long}")
