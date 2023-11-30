numbers = []
number = int(input("Please enter a number: "))

highest = 0
lowest = 999999999999999

while number != 0:
    numbers.append(number)
    number = int(input("Please enter another number, enter 0 when finished: "))
    if number > highest:
        highest = number
    if number < lowest and number > 0:
        lowest = number

total = sum(numbers)
average = total / len(numbers)


print(numbers)
print(f"The sum of your numbers is {total}.")
print(f"The average of the entered numbers is {average}.")
print(f"The highest number in your list is {highest}.")
new_list = sorted(numbers)
