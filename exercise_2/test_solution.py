from solution import Item, Cart

def test_empty_cart():
    cart = Cart()
    cart.cart_list == []
    assert f'{cart:short}' == ''
    assert f'{cart:long}' == ''

def test_cart_1_item():
    cart = Cart()
    assert len(cart.cart_list) == 0

    item = Item(2, 'grain', 'rice', 1)
    cart.add(item)
    assert len(cart.cart_list) == 1
    assert cart.cart_list[0] == item

    assert f'{cart:short}' == 'rice'
    assert f'{cart:long}' == '    2 grain     rice @ $1.00...$2.00\n'

def test_cart_2_item2():
    cart = Cart()
    rice = Item(2, 'grain', 'rice', 1)
    bread = Item(1, 'loaf', 'bread', 1)
    cart.add(rice)
    cart.add(bread)

    assert len(cart.cart_list) == 2
    assert cart.cart_list[0] == rice
    assert cart.cart_list[1] == bread

    assert f'{cart:short}' == 'rice, bread'
    assert f'{cart:long}' == '    2 grain     rice @ $1.00...$2.00\n    1 loaf      bread @ $1.00...$1.00\n'
