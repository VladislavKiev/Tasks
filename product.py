"""
product
    -name
    -price
    -article

    Phone
        -model
        -color
        -type OS
"""


class Product:
    def __init__(self, name, price, art):
        self.name = name
        self.price = price
        self.art = art

    def __str__(self):
        return 'Product: {} {}$ {}'.format(self.name, self.price, self.art)


class Phone(Product):
    def __init__(self, model, color, type_os, **prod):
        super(Phone, self).__init__(name=prod['name'], price=prod['price'], art=prod['art'])
        self.model = model
        self.color = color
        self.type_os = type_os

    def info(self):
        print('''Phone:
    name: {}
    model: {}
    color: {}
    type_os: {}
    price: {}
    art: {}'''.format(self.name, self.model, self.color, self.type_os, self.price, self.art))


class TV(Product):
    def __init__(self, model, color, diagonal, **prod):
        super(TV, self).__init__(**prod)
        self.model = model
        self.color = color
        self.diagonal = diagonal

    def info(self):
        print('''TV:
    name: {}
    model: {}
    color: {}
    diagonal: {}
    price: {}
    art: {}'''.format(self.name, self.model, self.color, self.diagonal, self.price, self.art))


base_phone = Phone(model='Iphone 5', color='Black', type_os='IOS', name='Phone', price=1000, art='some art')
iphone = Phone(model='Iphone 7', color='Black', type_os='IOS', name='Phone', price=700, art=123123412)
tv = TV(model='Samsung', color='Black', diagonal='48', name='TV', price= 1200, art=324623453)

base_phone.info()
iphone.info()
tv.info()
