def display_menu():
    print("-----------------Shopping List Manager----------------------")
    print("Enter a number(1-4) to perform an operation")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter an Item to be added to the shopping List, ").strip().capitalize()
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter an item to be removed from the Shopping List, ").strip().capitalize()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your shopping list")
            else: 
                print("Item not found")
        elif choice == '3':
            # Display the shopping list
            print("This is your Shopping List")
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Do visit us soon")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()