import tkinter as tk
from tkinter import messagebox
from bookstore_core import Customer, Stock, Order, Shipping, Invoice, BookStore
from datetime import date

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Ordering System")

        # this is the data repositories
        self.customers = []
        self.stocks = []
        self.bookstore = BookStore()

        # Creates the UI elements
        self.create_customer_form()
        self.create_book_form()
        self.create_order_section()
        self.create_invoice_section()

    def create_customer_form(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Customer Name:").grid(row=0, column=0)
        self.customer_name = tk.Entry(frame)
        self.customer_name.grid(row=0, column=1)

        tk.Label(frame, text="Phone:").grid(row=1, column=0)
        self.customer_phone = tk.Entry(frame)
        self.customer_phone.grid(row=1, column=1)

        tk.Label(frame, text="Email:").grid(row=2, column=0)
        self.customer_email = tk.Entry(frame)
        self.customer_email.grid(row=2, column=1)

        tk.Button(frame, text="Add Customer", command=self.add_customer).grid(row=3, columnspan=2)

    def add_customer(self):
        name = self.customer_name.get()
        phone = self.customer_phone.get()
        email = self.customer_email.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            customer = Customer(name, phone, email)
            self.customers.append(customer)
            messagebox.showinfo("Success", "Customer added successfully")
            self.customer_name.delete(0, tk.END)
            self.customer_phone.delete(0, tk.END)
            self.customer_email.delete(0, tk.END)
            self.update_menus()  
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_book_form(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Book Name:").grid(row=0, column=0)
        self.book_name = tk.Entry(frame)
        self.book_name.grid(row=0, column=1)

        tk.Label(frame, text="Author:").grid(row=1, column=0)
        self.book_author = tk.Entry(frame)
        self.book_author.grid(row=1, column=1)

        tk.Label(frame, text="Price:").grid(row=2, column=0)
        self.book_price = tk.Entry(frame)
        self.book_price.grid(row=2, column=1)

        tk.Button(frame, text="Add Book", command=self.add_book).grid(row=3, columnspan=2)

    def add_book(self):
        name = self.book_name.get()
        author = self.book_author.get()
        price = self.book_price.get()

        if not name or not author or not price:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            price = float(price)
            book = Stock(name, author, price)
            self.stocks.append(book)
            messagebox.showinfo("Success", "Book added to stock successfully")
            self.book_name.delete(0, tk.END)
            self.book_author.delete(0, tk.END)
            self.book_price.delete(0, tk.END)
            self.update_menus()  
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number")

    def create_order_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Select Customer:").grid(row=0, column=0)
        self.customer_menu = tk.StringVar()
        self.customer_dropdown = tk.OptionMenu(frame, self.customer_menu, "")
        self.customer_dropdown.grid(row=0, column=1)

        tk.Label(frame, text="Select Book:").grid(row=1, column=0)
        self.book_menu = tk.StringVar()
        self.book_dropdown = tk.OptionMenu(frame, self.book_menu, "")
        self.book_dropdown.grid(row=1, column=1)

        tk.Label(frame, text="Urgent Shipping:").grid(row=2, column=0)
        self.is_urgent = tk.BooleanVar()
        tk.Checkbutton(frame, variable=self.is_urgent).grid(row=2, column=1)

        tk.Button(frame, text="Place Order", command=self.place_order).grid(row=3, columnspan=2)

    def place_order(self):
        customer_name = self.customer_menu.get()
        book_name = self.book_menu.get()

        if not customer_name or not book_name:
            messagebox.showerror("Error", "Select both a customer and a book")
            return

        customer = next((c for c in self.customers if c.name == customer_name), None)
        book = next((b for b in self.stocks if b.name == book_name), None)

        if not customer or not book:
            messagebox.showerror("Error", "Invalid customer or book selection")
            return

        order = Order(customer, book)
        shipping = Shipping(order, date.today())
        shipping.set_ship_cost(shipping.calc_ship_cost(self.is_urgent.get()))
        invoice = Invoice(f"INV{len(self.bookstore.get_invoices) + 1:04}", book, shipping)

        self.bookstore.add_invoice(invoice)
        messagebox.showinfo("Success", f"Order placed. Invoice Total: {invoice.invoice():.2f}")
        self.update_menus()

    def create_invoice_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Invoice Number:").grid(row=0, column=0)
        self.invoice_search = tk.Entry(frame)
        self.invoice_search.grid(row=0, column=1)

        tk.Button(frame, text="Search Invoice", command=self.search_invoice).grid(row=0, column=2)

        tk.Button(frame, text="View All Invoices", command=self.view_all_invoices).grid(row=1, columnspan=3)

    def search_invoice(self):
        invoice_nbr = self.invoice_search.get()
        if not invoice_nbr:
            messagebox.showerror("Error", "Enter an invoice number")
            return

        invoice = self.bookstore.search_invoice(invoice_nbr)
        if invoice:
            messagebox.showinfo("Invoice Found", f"Invoice: {invoice.invoice_nbr}, Total: {invoice.invoice():.2f}")
        else:
            messagebox.showerror("Error", "Invoice not found")

    def view_all_invoices(self):
        if not self.bookstore.get_invoices:
            messagebox.showinfo("Invoices", "No invoices available")
            return

        invoices = "\n".join(f"{inv.invoice_nbr}: {inv.invoice():.2f}" for inv in self.bookstore.get_invoices)
        messagebox.showinfo("All Invoices", invoices)

    def update_menus(self):
        # Updated the customer menu
        self.customer_dropdown['menu'].delete(0, 'end')
        for customer in self.customers:
            self.customer_dropdown['menu'].add_command(
                label=customer.name, command=tk._setit(self.customer_menu, customer.name)
            )

        # Updated the book menu
        self.book_dropdown['menu'].delete(0, 'end')
        for book in self.stocks:
            self.book_dropdown['menu'].add_command(
                label=book.name, command=tk._setit(self.book_menu, book.name)
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()
