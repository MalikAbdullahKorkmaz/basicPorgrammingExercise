def check_eligibility(age):
    if 18 <= age <= 65:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# Get the user's age
age = int(input("Enter your age: "))

# Check eligibility and print the result
check_eligibility(age)