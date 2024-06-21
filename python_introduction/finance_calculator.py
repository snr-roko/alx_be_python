# Prompting user for monthly income

montly_income = int(input("Enter your monthly income: "))

# Prompting user for total montly expenses

monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculating monthly savings

monthly_savings = monthly_income - monthly_expenses

# Calculating projected savings after one year using the formular: 
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)

annual_savings_forcast = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Displaying the annual projected savings

print("Projected savings after one year, with interest, is: " + "$" + str(annual_savings_forcast) + str("."))
