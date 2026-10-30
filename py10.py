
venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering per participant: "))
transport = float(input("Transport per participant: "))
certificate = float(input("Certificate per participant: "))
n = int(input("Expected participants: "))
fee = float(input("Registration fee: "))
sponsor = float(input("Sponsorship: "))

fixed = venue + equipment
variable = catering + transport + certificate
cost = fixed + variable*n
income = fee*n + sponsor
print("Total event cost:", cost)
print("Total income:", income)
print("Shortfall:", max(cost-income, 0))
print("Surplus:", max(income-cost, 0))

contribution = fee-variable
if contribution > 0:
    remaining = max(fixed-sponsor, 0)
    breakeven = int(remaining/contribution)
    if breakeven*contribution < remaining:
        breakeven += 1
    print("Break-even registrations:", breakeven)
elif sponsor >= fixed:
    print("Break-even registrations: 0")
else:
    print("Break-even not possible at this fee")
