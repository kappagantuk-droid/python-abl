#MANUFACTURING COST AND PROFITABILITY ANALYSIS
qty = int(input("Products produced: "))
material = float(input("Material quantity: ")) * float(input("Cost per material unit: "))
waste = float(input("Wastage percentage: "))
labour = float(input("Labour hours: ")) * float(input("Wage per hour: "))
machine = float(input("Machine hours: ")) * float(input("Machine cost per hour: "))
selling = float(input("Selling price per product: "))
target = float(input("Target profit percentage: "))

cost = material + material*waste/100 + labour + machine
revenue = qty * selling
profit = revenue - cost
percentage = profit/cost*100 if cost else 0

print("Total cost:", cost)
print("Revenue:", revenue, "Profit:", profit)
print("Profit percentage:", round(percentage, 2))
print("Target achieved" if percentage >= target else "Target not achieved")
