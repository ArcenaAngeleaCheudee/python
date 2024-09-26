# Input
loan_amt = int(input("Enter Loan Amount: $"))
monthly_salary = float(input("Enter Monthly Salary: $"))

if monthly_salary >= 30000:
    months = int(input("How many months to pay: "))
    interest = loan_amt * 0.10
    new_loan_amt = loan_amt + interest
    payable = new_loan_amt / months
    print(f"To be paid monthly: ${payable:.2f}")
else:
    print("Customer is not eligible due to an insufficient salary and a loan request that exceeds the allowable limit.")
