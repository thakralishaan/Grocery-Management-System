class Item:
    """
        To store item details
    """
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category


class Store:
    __total_sale = 0

    def get_total(self):
        return Store.__total_sale

    def update_total(self, payment):
        Store.__total_sale += payment


class Customer:
    """ Some sample mobile numbers for privilige customers"""
    __previliged_customer_numbers = [9874563211, 7845129633, 854745874,654654654]

    def __init__(self, mobile_number):
        self.mobile_number = mobile_number

    def checkprevilige(self):
        if self.mobile_number in Customer.__previliged_customer_numbers:
            return True
        return False


class Inventory:
    __stock = {}

    def __init__(self):
        __stock = self.load_items()  # Stock is made private to deny access from other modules

    @staticmethod
    def load_items(self):
        """
        Loads stock using log file, creates item object for each item and stores to Stock
        """
        stock = {}
        with open('inventory_log.txt') as inventory_log:
            next(inventory_log)
            for line in inventory_log:
                line_list = line.split()
                stock[line_list[0]] = Item(line_list[1], line_list[2], line_list[3], line_list[4])
        return stock

    def update_item_prices(self, code, discount):
        """
            First check if item_code is passed by checking in stock keys(),
            otherwise we decide its a category and update the category price.
        """
        if code in Inventory.__stock.getkeys():
            discount_amount = Inventory.__stock[code].price * (discount / 100)
            Inventory.__stock[code].price -= discount_amount
        else:
            for items in Inventory.__stock:
                if items.category == 'code':
                    items.price -= items.price * (discount / 100)

    def get_stock(self):
        return Inventory.__stock

    def update_stock(self, purchased):
        """
            Updates the quantity of items in stock
        """
        for item_code in purchased:
            Inventory.__stock[item_code].quantity -= 1

    @staticmethod
    def get_price_list(self, item_list):
        """ To fetch prices as list[i] for every i in item_list[]"""
        price_list = []
        for item in item_list:
            price_list.append(Inventory.stock[item].price)
        return price_list

    def get_item_code(self, item_name):
        """ Return item_code by finding the Key by its item_code value"""
        for tmp_item in Inventory.__stock:
            if Inventory.__stock[tmp_item].name == 'item_name':
                return tmp_item


class Register:
    def __init__(self):
        self.__bill = 'ItemName\tPrice'
        self.__bill_total = 0

    def checkout(self, item_list, price_list):
        """ frames bill statement and the final bill amount"""
        for i in range(0, len(item_list)):
            self.__bill += ('\n', item_list[i], '\t', price_list[i])
            self.__bill += price_list[i]
        return self.__bill_total

    def get_bill(self):
        self.__bill += ('Total:', str(self.__bill_total))

    def get_bill_amount(self):
        return self.__bill_total

    def update_discount(self, percentage):
        discount = (percentage / 100) * self.__bill
        self.__bill_total -= discount


class Payment:
    def __init__(self):
        self.payment_made = 0

    def receive_payment(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cash(Payment):
    """
    Inherits payment class
    """

    def receive_payment(self, amount):
        print('Payment successful by cash')
        Payment.payment_made += amount


class Card(Payment):
    """
        Inherits payment class
    """

    def receive_payment(self, amount):
        print('Payment successful by card')
        self.payment_made += amount
