import datetime


def view_stock_availability(stock):
    print("Item Code \t Item name \t Quantity \t Price")
    for key, value in stock.iteritems():
        print(key, "\t", value.name, "\t", value.quantity, "\t", value.price)


def view_bill(bill):
    """ Prints the final bill statement, ideally can be manipulated based on customer or other factors"""
    print("Final Bill:", bill)


def view_total_sales(total_sales_amount):
    """ To view the total sale for the day"""
    print("Total sal for", datetime.datetime.now(), "::", total_sales_amount)
