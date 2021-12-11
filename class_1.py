"""
Laptop
    -brand (str)
    -price (float)
    -in sale (bool)
    -color (str)
"""


class Laptop:
    def __init__(self, brand, price, in_sale, color, percent_sale):
        self.brand = brand
        self.price = price
        self.in_sale = in_sale
        self.color = color
        self.percent_sale = percent_sale
        if not isinstance(brand, str):
            raise ValueError('Brand must be str')
        if not isinstance(price, float) and not isinstance(price, int):
            raise ValueError('Price must be int or float')
        if not isinstance(in_sale, bool):
            raise ValueError('Value in_sale must be bool')
        if not isinstance(color, str):
            raise ValueError('Color must be str')
        if percent_sale > 100 or percent_sale < 0:
            raise ValueError('Check Value (percent_sale)')

    def total_price(self):
        if self.in_sale:
            return self.price * (100 - self.percent_sale) / 100
        else:
            return self.price

    def info(self):
        print('Laptop {}, color {}, price {}'.format(self.brand, self.color, self.total_price()))


lenovo = Laptop('Lenovo', 500, True, 'black', 10)
lenovo_2 = Laptop('Lenovo 888', 500, False, 'black', 10)
hp = Laptop('HP pro book', 700, True, 'gray', 0)
hp_2 = Laptop('HP 830', 600, True, 'white', 50)

lenovo.info()
lenovo_2.info()
hp.info()
hp_2.info()
