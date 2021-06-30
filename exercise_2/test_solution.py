from solution import Item, Cart


def test_item():
    item = Item(2, 'grain', 'rice', 1)
    assert item.quantity == 2
    assert item.measure == 'grain'
    assert item.name == 'rice'
    assert item.price == 1
    assert str(item) == '    2 grain rice       @ $1.0...$2.0'


def test_empty_cart():
    cart = Cart()
    assert cart.items == []
    assert f'{cart:short}' == ''
    assert f'{cart:long}' == ''


def test_cart_1_item():
    cart = Cart()
    assert len(cart.items) == 0

    item = Item(2, 'grain', 'rice', 1)
    cart.add(item)
    assert len(cart.items) == 1
    assert cart.items[0] == item

    assert f'{cart:short}' == 'rice'
    assert f'{cart:long}' == f'\t{item}'
    assert f'{cart:garbage}' == 'unknown format code garbage'


def test_cart_2_item2():
    cart = Cart()
    rice = Item(2, 'grain', 'rice', 1)
    bread = Item(1, 'loaf', 'bread', 1)
    cart.add(rice)
    cart.add(bread)

    assert len(cart.items) == 2
    assert cart.items[0] == rice
    assert cart.items[1] == bread

    assert f'{cart:short}' == 'bread, rice'
    assert f'{cart:long}' == f'\t{bread}\n\t{rice}'
