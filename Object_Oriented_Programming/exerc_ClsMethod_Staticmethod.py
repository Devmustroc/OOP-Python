class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {
            'name': name,
            'price': price
        }
        self.items.append(item)
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @staticmethod
    def franchise(store):
        return store.name + ' - franchise'  # return f'{store.name} - franchise'

    @classmethod
    def store_details(cls, store):
       return f'{store.name}, total stock price: {int(store.stock_price())}'  # return f'{store.name}, total stock price: {store.stock_price()}'


store = Store('Test')
store2 = Store('Amazon')
store.add_item('Keyboard', 160)

Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
Store.store_details(store2)
