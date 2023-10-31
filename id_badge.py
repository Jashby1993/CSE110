first_name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")
email=input("Please enter your email address: ")
phone=input("Please enter your phone number: ")
job_title=input("Please enter your job title: ")
id=input("Please enter your id number: ")
full_name=f"{last_name.upper()}, {first_name.capitalize()}"

def create_table(hair, eyes, month_started, training):
    max_length = max(len(hair), len(month_started), len(month_started), len(training))
    formatted_hair = hair.ljust(max_length)
    formatted_eyes = eyes.ljust(max_length)
    formatted_month_started = month_started.ljust(max_length)
    formatted_training = training.ljust(max_length)
    return f"Hair color: {formatted_hair}  Eye color:{formatted_eyes}\nMonth Started:{formatted_month_started}  Training completed{formatted_training}"

hair = input("What is your hair color? ")
eyes = input("What is your eye color? ")
month_started = input("What month did you start? ")
training = input("Have you completed advanced training? Yes or No ")
def training():
    while True:
        user_input = input("Have you completed advanced training? (Yes/No): ")
        if user_input.lower() == 'yes':
            return 'Yes'
        elif user_input.lower() == 'no':
            return 'No'
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

formatted_output = create_table(hair, eyes, month_started, training)


print(full_name)
print(job_title.title())
print(id)
print(" ")
print(email.lower())
print(phone)
print(" ")
print(formatted_output)