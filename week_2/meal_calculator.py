import math
#Extras: I added an option for adding a tip, and some if elif else statements sprinkled in.
adult_meal_price=float(input("What is the price of an adult meal? $"))
kids_meal_price=float(input("What is the price of a kid's meal? $"))
medium_drink_cost=float(input("What is the cost of a medium drink? $"))
#added drinks
large_drink_cost=float(input("What is the cost of a large drink? $"))
kids_drink_cost=float(input("What is the cost of a kid's drink? $"))

adults=int(input("How many adults in your party?" ))
children=int(input("How many children in your party?" ))
large_drinks=(int(input("How many large drinks will be ordered? ")))
medium_drinks=int(input("How man medium drinks will be ordered? "))
kids_drinks=int(input("How many kid sized drinks will be ordered? "))

#recommended appetizers for party size, with if else statement option to change. Also using math.ceil to always round up.
recommended_appetizers= math.ceil((adults + children) / 4)
recommend_y_n=input(f"The recommended number of appetizers for your party size is {recommended_appetizers}. Is that acceptable? Y or N: ").upper()
if recommend_y_n == "N":
    actual_appetizers=int(input("That's fine, how many appetizers does your party need? "))
elif recommend_y_n == "Y":
    actual_appetizers=recommended_appetizers
else: print("I'm sorry, I didn't understand.")
appetizer_cost=float(input("What is the cost of an appetizer? $"))


adult_total = adult_meal_price * adults
kids_total=kids_meal_price * children
drinks_total= (large_drink_cost * large_drinks) + (medium_drink_cost * medium_drinks) + (kids_drink_cost * kids_drinks)
appetizer_total= actual_appetizers * appetizer_cost
subtotal=adult_total + kids_total +drinks_total + appetizer_total

#determining total
print(f"The price for the adult's meals is ${adult_total:.2f}. ")
print(f"The  price for the children's meals is ${kids_total:.2f}.")
print(f"The total price for all driks is ${drinks_total:.2f}.")
print(f"The total price for all appetizers is ${appetizer_total:.2f}.")
print(f"The price for all items is ${subtotal:.2f}.")

tip_decision = input("Would you like to add a tip? Y or N: ").upper()
if tip_decision == "Y":
    tip_amount = float(input("That's very appreciated! What percentage? "))
elif tip_decision == "N":
    tip_amount = 0
    print("That's ok, it's not required. Just our livlihood, no big deal.")
else: print("I'm sorry, I didn't understand.")

tip_total= (tip_amount / 100) * subtotal
print(f"Thank you for your tip of ${tip_total:.2f}!")
print(f"Your new total comes to ${subtotal + tip_total:.2f}.")

#determining tax and total
tax=float(input("What is the sales tax in your state? (Enter as whole number, ie: enter 6.2 percent as 6.2) "))
tax_charged=tax / 100 * subtotal
total=tax_charged + subtotal + tip_amount
print(f"Total tax charged was ${tax_charged:.2f}.")
print(f"Final total is ${total:.2f}.")

#determining change
payment=float(input("What was the total payment amount? "))
change= payment - total

#thank you message for using exact change. had to overcome a float point precision problem.
if abs(change) < 0.01:
    print("Thank you for using exact change!") 
else:
    print(f"Your change comes out to ${change:.2f}.")  
