class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}'


class Transaction:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return f'Item: {self.item.name}, Quantity: {self.quantity}'

    @property
    def total_price(self):
        return self.item.price * self.quantity


class Store:
    def __init__(self, items):
        self.items = items
        self.transactions = []

    def make_transaction(self, item_name, quantity):
        for item in self.items:
            if item.name == item_name and item.stock >= quantity:
                item.stock -= quantity
                self.transactions.append(Transaction(item, quantity))
                return f'{quantity} {item_name}s purchased. New stock: {item.stock}'
        return f'Not enough stock or invalid item: {item_name}.'

    def calculate_profit(self):
        return sum(transaction.total_price for transaction in self.transactions)

    def __str__(self):
        items_str = '\n'.join(str(item) for item in self.items)
        return (f'Items:\n{items_str}\n'
                f'Transactions:\n{"-"*20}\n'
                f'{ "\n".join(str(transaction) for transaction in self.transactions) }'
                f'\nTotal profit: ${self.calculate_profit()}')


if __name__ == '__main__':
    items = [
        Item('Apple', 0.5, 50),
        Item('Banana', 0.25, 100),
        Item('Orange', 0.75, 30),
    ]
    store = Store(items)
    store.make_transaction('Apple', 10)
    store.make_transaction('Banana', 25)
    store.make_transaction('Orange', 10)
    print(store)