#I started using just the while and for loops with lists, but then I started figuring out functions and it actually made it easier. I also have the program counting how many duplicate items you have. I also added options to keep adding or removing items from your cart.

actions = ["Add Item", "View Cart", "Remove Item", "Compute Total", "Quit"]
items_in_cart = []
user_action = 1
repeat = False

def call_actions():
    for i, action in enumerate(actions):
        print(f"{i + 1} - {action}")
    return int(input("Which action would you like to use? "))

def add_item():
    repeat = True
    
    while repeat == True:
        item_name = input("What item would you like to add to your cart? ").capitalize()
        price = float(input("What is the price of the item? $"))

        # Check for duplicate items
        found_duplicate = False
        for item in items_in_cart:
            if item["name"] == item_name and item["price"] == price:
                item["count"] += 1
                found_duplicate = True
                break

        if not found_duplicate:
            # If it's a new item, add it to the list
            items_in_cart.append({"name": item_name, "price": price, "count": 1})

        repeat_ask = input("Would you like to add something else to your cart? Y or N: ").capitalize()
        if repeat_ask != "Y":
            repeat = False

def view_cart():
    if len(items_in_cart) != 0:
        for i, item in enumerate(items_in_cart):
            print(f"\n{i + 1}. {item['count']}: {item['name']} - ${(item['price'] * item['count']):.2f}\n")
    else:
        print("Your cart is currently empty.")

def remove_item():
    repeat = True
    
    while repeat:
        view_cart()
        item_number = int(input("Which item NUMBER would you like to remove? "))
        if 1 <= item_number <= len(items_in_cart):
           if removed_item["count"] > 1:
                # If count is greater than 1, decrement count
                removed_item["count"] -= 1
                print(f"Removed one {removed_item['name']}. {removed_item['name']} count: {removed_item['count']}")
           else:
                # If count is 1, remove the item from the list
                removed_item = items_in_cart.pop(item_number - 1)
                print(f"Removed: {removed_item['name']} - ${removed_item['price']:.2f}")

        repeat_ask = input("Would you like to remove something else from your cart? Y or N: ").capitalize()
        if repeat_ask != "Y":
            repeat = False
        

def compute_total():
    total = sum(item["price"] * item["count"] for item in items_in_cart)
    for i, item in enumerate(items_in_cart):
        print(f"\n{i + 1}. {item['name']} - ${item['price']:.2f}\n")
    print(f"The grand total for items in your cart is ${total:.2f}.")

call_actions()

while user_action != 5:
    if user_action == 1:
        add_item()
    elif user_action == 2:
        view_cart()
    elif user_action == 3:
        remove_item()
    elif user_action == 4:
        compute_total()
    
    # Get user action again
    user_action = call_actions()

print("Thank you, goodbye!")