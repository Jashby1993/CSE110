
shopping_list = []
print("What item do you want to add to your shopping list? When you've finished, type 'Done'.")
item = input("Item: ").capitalize()


while item != "Done":
    shopping_list.append(item)
    item = input("Item: ").capitalize()

for item in shopping_list:
    print(item)

for index, item in enumerate(shopping_list):
    print(f"{index} {item}")

switch = input("Do you need to switch any items on the list?").capitalize()

while switch == "Yes":
    index_number = int(input("Please enter index number of item: "))
    
