class Person:
    """
    Represents a base class for any person-related entities.
    """
    def __init__(self, name: str, phone: str, email: str):
        """
        Examples:
            >>> person = Person("Alice", "1234567890", "alice@example.com")
            >>> person.name
            'Alice'
        """
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if not value.strip():
            raise ValueError("Phone cannot be empty.")
        self._phone = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not value.strip() or "@" not in value:
            raise ValueError("Invalid email address.")
        self._email = value


class Product:
    """
    Represents a base class for any product-related entities.
    """
    def __init__(self, name: str, price: float):
        """
        Examples:
            >>> product = Product("1984", 8.99)
            >>> product.name
            '1984'
        """
        self.name = name
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Product name cannot be empty.")
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        self._price = value


class Customer(Person):
    """
    Represents a customer in the bookstore system, inheriting from Person.
    """
    def __init__(self, name: str, phone: str, email: str):
        """
        Examples:
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> customer.name
            'Alice'
        """
        super().__init__(name, phone, email)


class Stock(Product):
    """
    Represents a book in the bookstore's stock, inheriting from Product.
    """
    def __init__(self, name: str, author: str, price: float):
        """
        Examples:
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> stock.author
            'George Orwell'
        """
        super().__init__(name, price)
        self.author = author

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not value.strip():
            raise ValueError("Author name cannot be empty.")
        self._author = value


class Order:
    """
    Represents an order placed by a customer for a book.
    """
    def __init__(self, customer: Customer, stock: Stock):
        """
        Examples:
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> order.customer.name
            'Alice'
        """
        self.customer = customer
        self.stock = stock

class Shipping:
    """
    Represents the shipping details for an order.
    """
    count_urgent = 0

    def __init__(self, order: Order, ship_date):
        self.order = order
        self.ship_date = ship_date
        self.ship_cost = 0.0

    def set_ship_cost(self, cost: float):
        """
        Sets the shipping cost.
        """
        self.ship_cost = cost

    def calc_ship_cost(self, is_urgent: bool) -> float:
        """
        Calculates the shipping cost based on urgency.

        Examples:
            >>> from datetime import date
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> shipping = Shipping(order, date(2025, 1, 1))
            >>> shipping.calc_ship_cost(True)
            5.45
        """
        if is_urgent:
            self.ship_cost = 5.45
            Shipping.count_urgent += 1
        else:
            self.ship_cost = 3.95
        return self.ship_cost


class Invoice:
    """
    Represents an invoice for an order.
    """
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
        """
        Examples:
            >>> from datetime import date
            >>> customer = Customer("Alice", "1234567890", "alice@example.com")
            >>> stock = Stock("1984", "George Orwell", 8.99)
            >>> order = Order(customer, stock)
            >>> shipping = Shipping(order, date(2025, 1, 1))
            >>> shipping.set_ship_cost(shipping.calc_ship_cost(False))
            >>> invoice = Invoice("INV001", stock, shipping)
            >>> invoice.invoice()
            12.94
        """
        self.invoice_nbr = invoice_nbr
        self.stock = stock
        self.ship_order = ship_order
        self.total_cost = 0.0

    def invoice(self) -> float:
        """
        Calculates the total cost of the invoice.
        """
        self.total_cost = round(self.stock.price + self.ship_order.ship_cost, 2)
        return self.total_cost

class BookStore:
    """
    Represents a repository for storing and managing invoices.
    """
    def __init__(self):
        self.invoices = []

    @property
    def get_invoices(self) -> list:
        """
        Retrieves the list of invoices.
        """
        return self.invoices

    def add_invoice(self, invoice):
        """
        Adds an invoice to the repository.
        """
        self.invoices.append(invoice)

    def search_invoice(self, invoice_nbr: str):
        """
        Searches for an invoice in the repository by its number.
        """
        for invoice in self.invoices:
            if invoice.invoice_nbr == invoice_nbr:
                return invoice
        return None



if __name__ == "__main__":
    import doctest
    doctest.testmod()
