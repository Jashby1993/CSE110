def choose_article(word):
    vowels = ['a', 'f']
    if word[0].lower() in vowels:
        return 'an'
    else:
        return 'a'

grade_percentage=int(input("What is the numerical valude of your grade? "))

if grade_percentage >= 90:
    grade = "A"
elif grade_percentage >= 80:
    grade = "B"
elif grade_percentage >= 70:
    grade = "C"
elif grade_percentage >= 60:
    grade = "D"
else:
    grade = "F"

last_digit = grade_percentage % 10

if grade == "F":
    final_grade = grade
elif grade == "A" and last_digit >= 4:
    final_grade = grade
else:
    if last_digit >= 7:
        final_grade = grade + "+"
    elif 1 <= last_digit <= 3:
        final_grade = grade + "-"
    else:
        final_grade = grade
print(f"Your final letter grade is {choose_article(final_grade)} {final_grade}.")

if grade_percentage >= 83:
    print("Congrats, you passed with flying colors!")
elif 70 <= grade_percentage < 83:
    print("You passed, but that was a close one!")
else:
    print("I'm sorry, you have not passed the class.")