import datetime
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice

# Prompt user for invoice details
customer_name = input("Enter Customer's Name: ")
customer_contact = input("Enter Customer's Mobile Number: ")
invoice_number = int(input("Enter Invoice Number: "))
due_days = int(input("Enter Number of Days until Due: "))

# Create a new invoice
invoice = SimpleInvoice('invoice.pdf')

# Set invoice information
invoice_info = InvoiceInfo(invoice_number, datetime.datetime.now(), datetime.timedelta(days=due_days))
invoice.invoice_info = invoice_info

# Set service provider information
service_provider_info = ServiceProviderInfo(
    name='MyG Digital Hub',
    street='Edapally',
    city='Ernakulam',
    state='Kerala',
    country='India'
)
invoice.service_provider_info = service_provider_info

# Set client information
client_info = ClientInfo()
client_info.name = customer_name
client_info.phone = customer_contact
invoice.client_info = client_info

# Prompt user for item details
while True:
    item_name = input("Enter Item Name (or 'q' to quit): ")
    if item_name == 'q':
        break

    item_description = input("Enter Item Description: ")
    item_quantity = int(input("Enter Item Quantity: "))
    item_price = float(input("Enter Item Price: "))

    # Add item to the invoice
    item = Item(item_name, item_description, item_quantity, item_price)
    invoice.add_item(item)

# Set invoice footer
invoice.set_bottom_tip("Thank you for your business!")

# Generate the invoice
invoice.finish()

print("Invoice generated successfully. Saved as invoice.pdf")
