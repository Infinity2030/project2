from bookstore_core import Customer, Stock, Order, Shipping, Invoice, BookStore
from datetime import date

def test_bookstore():
    customer1 = Customer("Alice", "1234567890", "alice@example.com")
    customer2 = Customer("Bob", "9876543210", "bob@example.com")
    customer3 = Customer("Charlie", "5555555555", "charlie@example.com")

    stock1 = Stock("1984", "George Orwell", 8.99)
    stock2 = Stock("To Kill a Mockingbird", "Harper Lee", 12.99)
    stock3 = Stock("The Catcher in the Rye", "J.D. Salinger", 9.99)

    order1 = Order(customer1, stock1)
    order2 = Order(customer2, stock2)
    order3 = Order(customer3, stock3)

    shipping1 = Shipping(order1, date(2025, 1, 15))
    shipping2 = Shipping(order2, date(2025, 1, 16))
    shipping3 = Shipping(order3, date(2025, 1, 17))

    shipping1.set_ship_cost(shipping1.calc_ship_cost(False))
    shipping2.set_ship_cost(shipping2.calc_ship_cost(True))
    shipping3.set_ship_cost(shipping3.calc_ship_cost(False))

    invoice1 = Invoice("INV001", stock1, shipping1)
    invoice2 = Invoice("INV002", stock2, shipping2)
    invoice3 = Invoice("INV003", stock3, shipping3)

    bookstore = BookStore()
    bookstore.add_invoice(invoice1)
    bookstore.add_invoice(invoice2)
    bookstore.add_invoice(invoice3)

    print("--- Test Results ---")
    print(f"Number of invoices: {len(bookstore.get_invoices)}")
    print(f"Invoice 1 total cost: {invoice1.invoice():.2f}")
    print(f"Invoice 2 total cost: {invoice2.invoice():.2f}")
    print(f"Invoice 3 total cost: {invoice3.invoice():.2f}")


    found_invoice = bookstore.search_invoice("INV002")
    if found_invoice:
        print(f"Found Invoice: {found_invoice.invoice_nbr}, Total Cost: {found_invoice.invoice():.2f}")
    else:
        print("Invoice not found")

    not_found_invoice = bookstore.search_invoice("INV004")
    if not_found_invoice:
        print(f"Found Invoice: {not_found_invoice.invoice_nbr}")
    else:
        print("Invoice INV004 not found")

if __name__ == "__main__":
    test_bookstore()

