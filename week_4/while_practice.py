number = -1

while number < 0:
    print("Please input a positive number.")
    number = int(input("Enter a number."))

print(f"Thank you! {number} is positive!")

answer = "no"
while answer != "yes":
    answer = input("Can I have some candy? ").lower()

print("Thank you!")

