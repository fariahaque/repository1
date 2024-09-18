'food': ['Sandwich', 'Salad', 'Soup', 'Cake'],
    'drinks': ['Coffee', 'Tea', 'Juice', 'Milk'],
    'specials': ['Ras Malai', 'Jamoon']
}

bestselling_books = ['Mein Kampf', 'Pride & Prejudice', 'Alexander the Great', 'Donald Trump']

customers = []

class Customer:
    def __init__(self, name, address, order):
        self.name = name
        self.address = address
        self.order = order

# Function to display the menu
def display_menu():
    print("\n--- Cafe Menu ---")
    print("Food:")
    for item in menu_items['food']:
        print(f"- {item}")
    print("\nDrinks:")
    for item in menu_items['drinks']:
        print(f"- {item}")
    print("\nSpecials:")
    if menu_items['specials']:
        for special in menu_items['specials']:
            print(f"- {special}")
    else:
        print("- No specials available today.")

# Function to display bestselling books
def display_books():
    print("\n--- Bestselling Books ---")
    for book in bestselling_books:
        print(f"- {book}")

# Function to handle customer orders
def customer_order():
    display_menu()
    display_books()

    order = []
    while True:
        item = input("\nEnter an item from the menu or book (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        # Check if the item exists in menu or book list
        if item in menu_items['food'] or item in menu_items['drinks'] or item in bestselling_books or item in menu_items['specials']:
            order.append(item)
        else:
            print("Item not found. Please choose again.")

    if order:
        name = input("Enter your name: ").strip()
        address = input("Enter your address for delivery (if ordering books): ").strip()
        customer = Customer(name, address, order)

        print(f"\nThank you for your order, {name}!")
        customers.append(customer)
    else:
        print("No items ordered.")

print(customer_order())
print(customers)