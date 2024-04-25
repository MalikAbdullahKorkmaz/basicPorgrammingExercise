# Calculate monthly motorbike loan installment

def calculate_monthly_installment(principal, annual_interest_rate, term_in_years):
    # Convert annual interest rate to monthly and decimal format
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate the number of monthly payments
    num_payments = term_in_years * 12

    # Calculate the monthly payment using the formula:
    # M = P * r * (1 + r)^n / ((1 + r)^n - 1)
    monthly_payment = principal * monthly_interest_rate * ( (1 + monthly_interest_rate) ** num_payments ) / ( ( (1 + monthly_interest_rate) ** num_payments ) - 1 )

    return monthly_payment

# Get user input for the loan amount
loan_amount = float(input("Enter the loan amount (in rupiah): "))

# Set the annual interest rate and term in years
annual_interest_rate = 2 # 2% per month
term_in_years = 3 # 3 years

# Calculate the monthly payment
monthly_payment = calculate_monthly_installment(loan_amount, annual_interest_rate, term_in_years)

# Print the result
print(f"The monthly installment for a {loan_amount} rupiah loan with an annual interest rate of {annual_interest_rate}% and a term of {term_in_years} years is: {monthly_payment:.2f} rupiah")









