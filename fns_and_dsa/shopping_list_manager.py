def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
 

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item) # Prompt  for and add an item
            print(F"{add_item} has been added successfully") # Also print "_ item has been added"
            pass
        elif choice == 2:
            remove_item = input("Enter the item you want to remove") 
            shopping_list.remove({remove_item}) # Prompt for and remove an item
            pass
        elif choice == 3:
            print(f"Shoping list \n {shopping_list}") # Display the shopping list
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
print(main())          