class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item = {}

    def add_item(self, name, key, value):
        if name == self.name:
            self.item[key] = value
            return self.item[key]
        else:
            print(f'Магазина {name} нет в списке')

    def remove_item(self, name, key):
        if name == self.name and key in self.item:
            del self.item[key]
            print(f'Элемент {key} удален')
        else:
            print(f'Вы не можете удалить продукт {key} в магазине {name}. Его нет в списке.')

    def get_item_price(self, name, key):
        try:
            if name in self.name and self.item != None:
                print(f'Цена на продукт {key} равна {self.item[key]}')
        except KeyError:
            return None

    def update_item(self, name, key, value):
        if name in self.name:
             self.item[key] = value
        else:
            print(f'Магазина {name} нет в списке')

    def show_info(self):
        print(f'Ваш магазин {self.name}\nнаходится по адресу -- {self.address}\n'
                  f'имеет в своем ассортименте следующие продукты:')
        for key, value in self.item.items():
            print(f'{key} -- цена {value} рубля')


store1 = Store('Корона', 'г. Брест, Варшавское шоссе 2')
banana = store1.add_item(store1.name, 'банан', 5)
apple = store1.add_item(store1.name, 'яблоко', 3)
blueberry = store1.add_item(store1.name, 'голубика', 3)
print(store1.show_info())
print('---------------')
store1.update_item(store1.name, 'голубика', 10)
print(store1.show_info())
print('---------------')
store1.remove_item(store1.name, 'помидор')
print(store1.show_info())
print('---------------')
print(store1.get_item_price(store1.name, 'банан'))
print('------------------------------------------------------------------------------')


store2 = Store('Евроопт', 'г. Брест, Проспект республики 10')
banana2 = store2.add_item(store2.name, 'банан', 8)
tomato = store2.add_item(store2.name, 'помидор', 4)
pineapple = store2.add_item(store2.name, 'ананас', 7)
print(store2.show_info())
print('---------------')
store2.update_item(store2.name, 'ананас', 10)
print(store2.show_info())
print('---------------')
store2.remove_item(store2.name, 'ананас')
print(store2.show_info())
print('---------------')
print(store2.get_item_price(store2.name, 'помидор'))
print('------------------------------------------------------------------------------')


store3 = Store('Green', 'г. Брест, ул. Махновича 2')
cucumber = store3.add_item(store3.name, 'огурец', 2)
pepper = store3.add_item(store3.name, 'перец', 4)
strawberry = store3.add_item(store3.name, 'клубника', 7)
print(store3.show_info())
print('---------------')
store3.update_item(store3.name, 'клубника', 12)
print(store3.show_info())
print('---------------')
store3.remove_item(store3.name, 'клубника')
print(store3.show_info())
print('---------------')
print(store3.get_item_price(store3.name, 'перец'))