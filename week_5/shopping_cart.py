#Making my lists and variables
actions = ["Add Item", "View Cart", "Remove Item", "Compute Total", "Quit" ]
item = ""
price = ""
item_number = ""
items_in_cart = []
prices_items_in_cart = []
user_action = 1
total = sum(prices_items_in_cart)
keep_removing = ""

#making functions for things I'll be doing a lot
def call_actions ():
    for i in range(len(actions)):
        action = actions[i]
        print( f"{i+1} - {action}")
    return  int(input("Which action would you like to use? "))

user_action = call_actions()



#asking for option


while user_action != 5:
    while user_action == 1:
        item = input("What item would you like to add to your cart? ").capitalize()
        price = float(input("What is the price of the item? $"))
        items_in_cart.append(item)
        prices_items_in_cart.append(price)
        keep_buying = input("Would you like to add more items to your cart? Y or N: ").capitalize()
        print(" ")
        if keep_buying == "Y":
            user_action = 1
        elif keep_buying == "N":
            user_action = call_actions()

    

    while user_action == 2:
        for i in range(len(items_in_cart)):
            item = items_in_cart[i]
            price = prices_items_in_cart[i]
            print(f"\n{i+1}. {item} - ${price:.2f}\n")
        user_action = call_actions()

    while user_action == 3:
        for i in range(len(items_in_cart)):
            item = items_in_cart[i]
            price = prices_items_in_cart[i]
            print(" ")
            print(f"{i+1}. {item} - ${price:.2f}")
        item_number = int(input("Which item NUMBER would you like to remove? "))
        if 1 <= item_number <= len(items_in_cart):
            removed_item = items_in_cart.pop(item_number - 1)
            removed_price = prices_items_in_cart.pop(item_number - 1)
            print(f"Removed: {removed_item} - ${removed_price:.2f}")
        else:
            print("Invalid item number. Please choose a valid item number.")
        keep_removing = input("Would you like to continue removing items? Y or N: ").capitalize()
        if keep_removing == "Y":
            user_action = 3
        else:
            user_action = call_actions()
        
        



    while user_action == 4:
        for i in range(len(items_in_cart)):
            item = items_in_cart[i]
            price = prices_items_in_cart[i]
            print(f"\n{i+1}. {item} - ${price:.2f}\n The grand total for items in your cart is ${total}.")
        user_action = call_actions()   

    #error message
    while user_action < 1 or user_action > 5 or not isinstance(user_action, int):
        print("That is not a valid option. Please choose an option on the list.")
        call_actions ()
        user_action = call_actions()
    
