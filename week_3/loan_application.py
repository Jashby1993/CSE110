print("Please use a scale of 1-10 for the following questions:")

loan_amount=int(input("What is the size of the loan? "))
credit_history=int(input("How good is your credit history? "))
income=int(input("What is your income level? "))
down_payment=int(input("How large is your down payment? "))

approved = False

if loan_amount > 4:
    if (income >= 7 and credit_history >= 7) or((income >= 7 or credit_history >=7) and down_payment >=5):
        approved = True
    else:
        approved = False
if loan_amount <= 4:
    if (income >= 7 or down_payment >=7) or (income >= 4 and down_payment >= 4):
        approved = True
    else:
        approved = False


if approved:
    print("Yes, you are approved for your loan!")
else:
    print("No, your loan was not approved.")
    