first_name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")
email=input("Please enter your email address: ")
phone=input("Please enter your phone number: ")
job_title=input("Please enter your job title: ")
id=input("Please enter your id number: ")
full_name=f"{last_name.upper()}, {first_name.capitalize()}"


hair = input("What is your hair color? ")
eyes = input("What is your eye color? ")
month_started = input("What month did you start? ")
training = input("Have you completed advanced training? Yes or No ")


print(full_name)
print(job_title.title())
print(id)
print(" ")
print(email.lower())
print(phone)
print(" ")
print(f"Hair: {hair:12}Eyes: {eyes}")
print(f"Month: {month_started:11}Training: {training}")