import json

# Mock data for menu and bestselling books
menu_items = {
    'food': ['Sandwich', 'Cake'],
    'drinks': ['Coffee', 'Tea'],
    'specials': ['Special Salad']
}
bestselling_books = ['The Great Gatsby', '1984']

# Customer class definition
class Customer:
    def __init__(self, name, address, order):
        self.name = name
        self.address = address
        self.order = order

    def to_dict(self):
        """Convert customer object to dictionary for JSON serialization."""
        return {
            'name': self.name,
            'address': self.address,
            'order': self.order
        }

def display_menu():
    """Display the menu items."""
    print("\nMenu:")
    print("Food: " + ", ".join(menu_items['food']))
    print("Drinks: " + ", ".join(menu_items['drinks']))
    print("Specials: " + ", ".join(menu_items['specials']))

def display_books():
    """Display the bestselling books."""
    print("\nBestselling Books: " + ", ".join(bestselling_books))

def customer_order():
    """Handles taking the customer order and saving/loading it to/from a file."""
    display_menu()
    display_books()

    order = []
    while True:
        item = input("\nEnter an item from the menu or book (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        # Check if the item exists in the menu or book list
        if item in menu_items['food'] or item in menu_items['drinks'] or item in bestselling_books or item in menu_items['specials']:
            order.append(item)
        else:
            print("Item not found. Please choose again.")

    if order:
        name = input("Enter your name: ").strip()
        address = input("Enter your address for delivery (if ordering books): ").strip()
        customer = Customer(name, address, order)

        # Serialize and save customer data to a file
        customer_data = customer.to_dict()
        filename = "customer_data.json"  # Save the data to a JSON file

        try:
            with open(filename, "w") as file:
                json.dump(customer_data, file, indent=4)
            print(f"\nThank you for your order, {name}!")
            print("Data successfully written to:", filename)

            # Load the customer data from the file to verify
            with open(filename, "r") as file:
                loaded_data = json.load(file)
                print("\nData loaded from:", filename)
                print(loaded_data)
        except IOError:
            print(f"An error occurred while handling the file: ")
    else:
        print("No items ordered.")

# Example usage:
customer_order()