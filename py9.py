#MULTI CURRENCY TRAVEL BUDGET ANALYSIS
rates = {"INR": 1, "USD": 85, "EUR": 95, "GBP": 110}

budget = float(input("Budget in INR: "))
fee = float(input("Conversion fee percentage: "))
n = int(input("Number of expenses: "))

totals = {}
total = 0

for i in range(n):
    category = input("Category: ")
    amount = float(input("Amount: "))
    currency = input("Currency (INR/USD/EUR/GBP): ").upper()

    if currency in rates:
        expense = amount * rates[currency] * (1 + fee / 100)
        totals[category] = totals.get(category, 0) + expense
        total += expense
    else:
        print("Invalid currency!")

print("\nTotal spending:", round(total, 2))
print("Budget difference:", round(budget - total, 2))

if totals:
    largest = max(totals, key=totals.get)
    print("Largest category:", largest)
else:
    print("No valid expenses")
