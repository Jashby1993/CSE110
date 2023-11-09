import math

adult_meal_price=float(input("What is the price of an adult meal? "))
kids_meal_price=float(input("What is the price of a kid's meal? "))

adults=int(input("How many adults in your party?"))
children=int(input("How many children in your party?"))

adult_total=adult_meal_price * adult_meal_price
kids_total=kids_meal_price * children
total=adult_total + kids_total

print(f"The total price for the adult's meals is ${adult_total:.2f}. ")
print(f"The total price for the children's meals is ${kids_total:.2f}.")
print(f"The total price for all meals is ${total:.2f}.")
