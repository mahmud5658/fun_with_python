inventory = {}

def add_book(title, quantity):
    if title in inventory:
        print("Book already exists in inventory.")
    else:
        inventory[title] = quantity
        print(f"Book '{title}' successfully added to inventory.")

def update_quantity(title, new_quantity):
    if title in inventory:
        inventory[title] = new_quantity
        print(f"Quantity of '{title}' successfully updated to {new_quantity}.")
    else:
        print("Book not found in inventory.")

def check_availability(title):
    if title in inventory:
        print(f"Book '{title}' is available in the inventory.")
    else:
        print(f"Book '{title}' not found in inventory.")

def display_inventory():
    print("Current Inventory:")
    print("------------------")
    print("Title\tQuantity")
    print("------------------")
    for title, quantity in inventory.items():
        print(f"{title}\t{quantity}")
    print("------------------")

def main():
    print("Welcome to Emily's Bookstore Inventory Management System!")

    while True:
        print("\n1. Add a new book")
        print("2. Update book quantity")
        print("3. Check book availability")
        print("4. Display inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the new book: ")
            quantity = int(input(f"Enter the quantity of {title}: "))
            add_book(title, quantity)
        elif choice == '2':
            title = input("Enter the title of the book to update quantity: ")
            new_quantity = int(input(f"Enter the new quantity of {title}: "))
            update_quantity(title, new_quantity)
        elif choice == '3':
            title = input("Enter the title of the book to check availability: ")
            check_availability(title)
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            print("Thank you for using Emily's Bookstore Inventory Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
