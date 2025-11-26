class Customer:
    """
    Represents a customer in the bookstore system.
    """
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def get_name(self) -> str:
        """
        Gets the name of the customer.

        Examples:
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> customer.get_name()
            'Alice'
        """
        return self.name

    def get_phone(self) -> str:
        """
        Gets the phone number of the customer.

        Examples:
            >>> customer = Customer("Bob", "9876543210", "bob@example.com")
            >>> customer.get_phone()
            '9876543210'
        """
        return self.phone

    def get_email(self) -> str:
        """
        Gets the email address of the customer.

        Examples:
            >>> customer = Customer("Charlie", "5555555555", "charlie@example.com")
            >>> customer.get_email()
            'charlie@example.com'
        """
        return self.email

class Stock:
    """
    Represents a book in the bookstore's stock.
    """
    def __init__(self, book_name: str, author: str, price: float):
        self.book_name = book_name
        self.author = author
        self.price = price

    def get_book_name(self) -> str:
        """
        Gets the name of the book.

        Examples:
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> stock.get_book_name()
            '1984'
        """
        return self.book_name

    def get_author(self) -> str:
        """
        Gets the author of the book.

        Examples:
            >>> stock = Stock("To Kill a Mockingbird", "Harper Lee", 12.99)
            >>> stock.get_author()
            'Harper Lee'
        """
        return self.author

    def get_price(self) -> float:
        """
        Gets the price of the book.

        Examples:
            >>> stock = Stock("The Catcher in the Rye", "J.D. Salinger", 9.99)
            >>> stock.get_price()
            9.99
        """
        return self.price

class Order:
    """
    Represents an order in the bookstore system.
    """
    def __init__(self, customer: Customer, stock: Stock):
        self.customer = customer
        self.stock = stock

    def get_customer(self) -> Customer:
        """
        Gets the customer associated with the order.

        Examples:
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> order.get_customer().name
            'Alice'
        """
        return self.customer

    def get_stock(self) -> Stock:
        """
        Gets the book associated with the order.

        Examples:
            >>> customer = Customer("Bob", "9876543210", "bob@example.com")
            >>> stock = Stock("To Kill a Mockingbird", "Harper Lee", 12.99)
            >>> order = Order(customer, stock)
            >>> order.get_stock().book_name
            'To Kill a Mockingbird'
        """
        return self.stock

class Shipping:
    """
    Represents the shipping details for an order.
    """
    def __init__(self, order: Order, ship_date):
        self.order = order
        self.ship_date = ship_date
        self.ship_cost = 0.0
        self.count_urgent = 0

    def set_ship_cost(self, ship_cost: float):
        self.ship_cost = ship_cost

    def calc_ship_cost(self, is_urgent: bool) -> float:
        """
        Calculates the shipping cost.

        Examples:
            >>> from datetime import date
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> shipping = Shipping(order, date.today())
            >>> shipping.calc_ship_cost(True)
            5.45
            >>> shipping.calc_ship_cost(False)
            3.95
        """
        if is_urgent:
            self.count_urgent += 1
            return 5.45
        return 3.95

class Invoice:
    """
    Represents an invoice for an order.
    """
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
        self.invoice_nbr = invoice_nbr
        self.stock = stock
        self.ship_order = ship_order
        self.total_cost = 0.0

    def invoice(self) -> float:
        """
        Calculates the total cost of the invoice.

        Examples:
            >>> from datetime import date
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> shipping = Shipping(order, date.today())
            >>> shipping.set_ship_cost(shipping.calc_ship_cost(True))
            >>> invoice = Invoice("INV001", stock, shipping)
            >>> invoice.invoice()
            14.44
        """
        self.total_cost = round(self.stock.price + self.ship_order.ship_cost, 2)
        return self.total_cost

class BookStore:
    """
    Represents the repository for managing invoices.
    """
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Invoice):
        self.invoices.append(invoice)

    def search_invoice(self, invoice_nbr: str):
        """
        Searches for an invoice by its number.

        Examples:
            >>> from datetime import date
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> shipping = Shipping(order, date.today())
            >>> shipping.set_ship_cost(shipping.calc_ship_cost(False))
            >>> invoice = Invoice("INV001", stock, shipping)
            >>> bookstore = BookStore()
            >>> bookstore.add_invoice(invoice)
            >>> result = bookstore.search_invoice("INV001")
            >>> result.invoice_nbr
            'INV001'
        """
        for invoice in self.invoices:
            if invoice.invoice_nbr == invoice_nbr:
                return invoice
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
